#!/usr/bin/env python3
"""Serve a manual's PDF as a TV-friendly two-page reader, and optionally cast it.

The reader (reader.html) renders pages with pdf.js, so it works on any browser the
TV can run — including the DashCast receiver, which needs no app installed on the
TV. Pages are fetched by HTTP range, so only the spread you are looking at (plus a
small preload window) ever crosses the network.

Usage:
  python scripts/tv-reader/serve.py --manual renault-dauphine
  python scripts/tv-reader/serve.py --manual renault-dauphine --page 39 --cast "Living Room TV"

Casting needs catt (pip install catt) and a Chromecast/Google TV on the same subnet.
The source PDF is read from manuals/<path>/ when present, else downloaded once from
the manifest's source URL into scripts/tv-reader/.cache/.
"""
from __future__ import annotations

import argparse
import errno
import os
import re
import shutil
import json
import socket
import subprocess
import sys
import threading
import time
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _common import load_manifest  # noqa: E402

STATE = {"page": 1, "rev": 0}      # the reader polls this; --goto bumps rev
STATE_LOCK = threading.Lock()

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CACHE = HERE / ".cache"
CHUNK = 1 << 16


def find_manual(slug: str) -> Path:
    """Resolve a manual by manifest slug, or by its directory name as a fallback."""
    candidates = sorted(REPO.glob("manuals/*/*/*/manifest.yml"))
    by_dir = None
    for mf in candidates:
        data = load_manifest(mf.parent)
        if data.get("slug") == slug:
            return mf.parent
        if mf.parent.name == slug:
            by_dir = mf.parent
    if by_dir:
        return by_dir
    known = "\n  ".join(
        f"{load_manifest(mf.parent).get('slug')}  ({mf.parent.relative_to(REPO)})"
        for mf in candidates
    )
    sys.exit(f"No manual with slug {slug!r}. Known manuals:\n  {known}")


def resolve_pdf(mdir: Path, manifest: dict) -> Path:
    """Prefer a PDF in the manual directory; else fetch the manifest source once."""
    local = sorted(p for p in mdir.glob("*.pdf") if p.name != "prepared.pdf")
    if local:
        return local[0]

    source = manifest.get("source") or {}
    if source.get("type") != "url" or not source.get("location"):
        sys.exit(f"No PDF in {mdir.relative_to(REPO)} and no source URL in manifest.yml")

    url = source["location"]
    CACHE.mkdir(exist_ok=True)
    cached = CACHE / f"{manifest.get('slug', mdir.name)}.pdf"
    if cached.is_file() and cached.stat().st_size > 0:
        return cached

    print(f"Downloading {url}\n  -> {cached.relative_to(REPO)} (one time) ...", flush=True)
    tmp = cached.with_suffix(".part")
    with urllib.request.urlopen(url) as r, open(tmp, "wb") as f:
        shutil.copyfileobj(r, f)
    tmp.rename(cached)
    print(f"  {cached.stat().st_size / 1e6:.0f} MB cached", flush=True)
    return cached


def lan_ip() -> str:
    """Best-effort LAN address — the TV has to reach us by IP, not localhost."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def make_handler(pdf: Path, page_html: bytes):
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def _head(self, code: int, ctype: str, length: int, extra: dict | None = None):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(length))
            self.send_header("Accept-Ranges", "bytes")
            self.send_header("Access-Control-Allow-Origin", "*")
            for k, v in (extra or {}).items():
                self.send_header(k, v)
            self.end_headers()

        def do_GET(self):  # noqa: N802
            path = self.path.split("?", 1)[0]
            if path in ("/", "/index.html"):
                self._head(200, "text/html; charset=utf-8", len(page_html))
                self.wfile.write(page_html)
                return
            if path in ("/state", "/goto"):
                if path == "/goto":
                    q = urllib.parse.parse_qs(self.path.partition("?")[2])
                    try:
                        want = int(q.get("page", ["1"])[0])
                    except ValueError:
                        self.send_error(400, "page must be an integer")
                        return
                    with STATE_LOCK:
                        STATE["page"] = max(1, want)
                        STATE["rev"] += 1
                with STATE_LOCK:
                    body = json.dumps(STATE).encode()
                self._head(200, "application/json", len(body),
                           {"Cache-Control": "no-store"})
                self.wfile.write(body)
                return

            if path != "/manual.pdf":
                self.send_error(404)
                return

            size = pdf.stat().st_size
            rng = self.headers.get("Range")
            m = re.match(r"bytes=(\d*)-(\d*)", rng) if rng else None
            if not m:
                self._head(200, "application/pdf", size)
                with open(pdf, "rb") as f:
                    shutil.copyfileobj(f, self.wfile, CHUNK)
                return

            start = int(m.group(1)) if m.group(1) else 0
            end = min(int(m.group(2)) if m.group(2) else size - 1, size - 1)
            if start > end:
                self.send_error(416)
                return
            self._head(206, "application/pdf", end - start + 1,
                       {"Content-Range": f"bytes {start}-{end}/{size}"})
            remaining = end - start + 1
            with open(pdf, "rb") as f:
                f.seek(start)
                while remaining > 0:
                    buf = f.read(min(CHUNK, remaining))
                    if not buf:
                        break
                    self.wfile.write(buf)
                    remaining -= len(buf)

        def do_HEAD(self):  # noqa: N802
            if self.path.split("?", 1)[0] == "/manual.pdf":
                self._head(200, "application/pdf", pdf.stat().st_size)
            else:
                self._head(200, "text/html; charset=utf-8", len(page_html))

        def log_message(self, fmt, *a):
            sys.stderr.write("  %s %s\n" % (self.address_string(), fmt % a))

    return Handler


def cast(device: str, url: str) -> None:
    # DashCast ignores a cast of the URL it already holds, so make each cast unique —
    # otherwise re-running after a restart leaves a dead page on the screen.
    url = f"{url}&t={int(time.time())}"
    catt = shutil.which("catt")
    if not catt:
        print("catt not found (pip install catt) — open the URL on the TV yourself.")
        return
    print(f"Casting to {device!r} ...", flush=True)
    # A session still holding the previous URL swallows the new cast silently, so
    # end it first. Nothing playing is not an error here.
    subprocess.run([catt, "-d", device, "stop"], capture_output=True, text=True, timeout=60)
    r = subprocess.run([catt, "-d", device, "cast_site", url],
                       capture_output=True, text=True, timeout=120)
    print(r.stdout.strip(), flush=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        print("Cast failed. Check the device name with: catt scan", flush=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manual",
                    help="manifest slug (e.g. renault-dauphine) or manual directory name")
    ap.add_argument("--page", type=int, default=1, help="page to open on (left of the spread)")
    ap.add_argument("--port", type=int, default=8789)
    ap.add_argument("--cast", metavar="DEVICE",
                    help='cast to this Chromecast/Google TV by name (see: catt scan)')
    ap.add_argument("--goto", type=int, metavar="N",
                    help="tell an already-running tv-reader to show page N, and exit")
    ap.add_argument("--oversample", type=float, default=2.0,
                    help="render scale above display size; lower is faster, softer (default 2)")
    args = ap.parse_args()

    if args.goto is not None:
        # Jump an already-running reader. The page polls /state, so this lands in
        # about a second with no reload and no re-cast.
        try:
            with urllib.request.urlopen(
                f"http://127.0.0.1:{args.port}/goto?page={args.goto}", timeout=5
            ) as r:
                print(f"showing page {json.load(r)['page']}")
        except OSError as e:
            sys.exit(f"No tv-reader answering on port {args.port} ({e}).\n"
                     f"  start one: python {Path(__file__).name} --manual <slug> --cast <device>")
        return

    if not args.manual:
        ap.error("--manual is required (or use --goto N to steer a running reader)")

    STATE["page"] = args.page
    mdir = find_manual(args.manual)
    manifest = load_manifest(mdir)
    pdf = resolve_pdf(mdir, manifest)

    title = manifest.get("title", mdir.name)
    page_html = (HERE / "reader.html").read_text(encoding="utf-8") \
        .replace("__TITLE__", title).encode("utf-8")

    # Bind before announcing anything, so a busy port fails loudly and not halfway.
    try:
        server = ThreadingHTTPServer(("0.0.0.0", args.port), make_handler(pdf, page_html))
    except OSError as e:
        if e.errno != errno.EADDRINUSE:
            raise
        sys.exit(
            f"Port {args.port} is already in use \u2014 an earlier tv-reader is probably "
            f"still running.\n"
            f"  reuse it:   http://{lan_ip()}:{args.port}/index.html?page={args.page}\n"
            f"  stop it:    lsof -nP -iTCP:{args.port} -sTCP:LISTEN -t | xargs kill\n"
            f"  other port: --port {args.port + 1}"
        )

    url = (f"http://{lan_ip()}:{args.port}/index.html"
           f"?page={args.page}&os={args.oversample:g}")
    print(f"{title}\n  {pdf.relative_to(REPO) if pdf.is_relative_to(REPO) else pdf}")
    print(f"  serving {url}")
    print("  controls: ◀ ▶ select / turn page · OK zoom · arrows pan · BACK exit zoom", flush=True)

    if args.cast:
        import threading
        threading.Thread(target=server.serve_forever, daemon=True).start()
        cast(args.cast, url)
        print("Serving until Ctrl-C.", flush=True)
        try:
            threading.Event().wait()
        except KeyboardInterrupt:
            print("\nstopped")
        return
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()
