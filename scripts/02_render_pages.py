#!/usr/bin/env python3
"""02 — Render page images.

Two modes:

  # Default: render EVERY page to pages/p####.png so the AI cleanup step can
  # cross-check garbled OCR against the scan. pages/ is gitignored (regenerable).
  python scripts/02_render_pages.py <manuals/slug/> [--dpi 200]

  # --page-images: render EVERY page to page-images/p####.png (black-and-white, 300 dpi by
  # default) and write data/pages.json. These ARE committed: they are how a reader — a person,
  # an AI assistant, or the tv-reader — looks at any page without the source PDF.
  python scripts/02_render_pages.py <manuals/slug/> --page-images [--page-image-dpi 300]

  # --diagrams: render ONLY the pages listed in the manifest `diagrams:` block,
  # each at its declared depth, to the image at its `file:` path. The format follows
  # the extension: .png (the default for new manuals — readable by every tool and AI
  # pipeline) or .webp (kept for manuals that already ship WebP).
  # These are the diagram-only pages delivered to the user in-chat (issue #1).
  python scripts/02_render_pages.py <manuals/slug/> --diagrams [--diagram-dpi 150]

Requires: pdftoppm (poppler-utils) on PATH; ImageMagick (`magick`) for --diagrams;
cwebp (webp) only if a diagram's `file:` ends in .webp.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir  # noqa: E402

# Diagram delivery targets B/W print scans: color is dead weight. Depth is per-diagram:
#   mono = pure black-and-white (~25-50 KB). The page is rendered in grayscale, contrast-
#          stretched, then THRESHOLDED (not dithered). Thresholding drops the gray paper
#          tone, scanner shading and light watermarks entirely and keeps line art and type
#          crisp; pdftoppm's own -mono dithers that gray into speckle, which made thin
#          numbers unreadable. Right for wiring, exploded views, sequences, typed plates.
#   gray = grayscale, contrast-stretched. Only for a genuine photo/halftone that a
#          threshold would turn into blotches.
# Optional per-diagram `threshold:` (percent, default 60) tunes mono. Lower keeps more of a
# faint drawing; higher darkens thin strokes but starts pulling light watermarks back in as
# solid black — check the render.
DEFAULT_DIAGRAM_DPI = 150
DEFAULT_THRESHOLD = 60
# Every page, rendered for delivery. 300 dpi suits scans around 200-300 ppi: it adds no
# information above the native resolution but upsampling before the threshold gives smoother
# edges when a page is zoomed on a large screen (a TV, say). ~100 KB per page.
DEFAULT_PAGE_IMAGE_DPI = 300
REPO_ROOT = Path(__file__).resolve().parent.parent


def render_all_pages(mdir: Path, manifest: dict, dpi_override: int | None) -> int:
    prepared = mdir / "prepared.pdf"
    if not prepared.is_file():
        sys.exit("prepared.pdf not found — run 01_prepare_pdf.py first.")

    dpi = dpi_override or (manifest.get("render", {}) or {}).get("dpi", 200)
    pages_dir = mdir / "pages"
    pages_dir.mkdir(exist_ok=True)

    print(f"Rendering {prepared.name} at {dpi} DPI -> {pages_dir}/p####.png ...")
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(dpi), str(prepared), str(pages_dir / "p")],
        check=True,
    )
    # pdftoppm names files p-<n>.png; normalize to zero-padded p####.png.
    for f in sorted(pages_dir.glob("p-*.png")):
        num = f.stem.split("-")[-1]
        f.rename(pages_dir / f"p{int(num):04d}.png")

    count = len(list(pages_dir.glob("p*.png")))
    print(f"Rendered {count} page images.")
    print("Next: python scripts/03_split_manifest.py", mdir)
    return 0


def render_diagrams(mdir: Path, manifest: dict, dpi_override: int | None) -> int:
    if shutil.which("magick") is None:
        sys.exit("Missing required tool on PATH: magick (install ImageMagick)")

    diagrams = manifest.get("diagrams") or []
    if not diagrams:
        print("No `diagrams:` block in manifest.yml — nothing to render.")
        return 0
    if any(str(d["file"]).endswith(".webp") for d in diagrams) and shutil.which("cwebp") is None:
        sys.exit("Missing required tool on PATH: cwebp (install the 'webp' package) — "
                 "needed because some diagram `file:` paths end in .webp")

    prepared = mdir / "prepared.pdf"
    if not prepared.is_file():
        sys.exit("prepared.pdf not found — run 01_prepare_pdf.py first.")

    dpi = dpi_override or (manifest.get("render", {}) or {}).get(
        "diagram_dpi", DEFAULT_DIAGRAM_DPI
    )
    tmp_dir = mdir / "pages"
    tmp_dir.mkdir(exist_ok=True)

    print(f"Rendering {len(diagrams)} diagram page(s) at {dpi} DPI ...")
    for d in diagrams:
        page, depth = d["page"], d["depth"]
        if depth not in ("mono", "gray"):
            sys.exit(f"Diagram p{page}: unknown depth {depth!r} (use mono or gray)")
        out = mdir / d["file"]
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.suffix.lower() not in (".png", ".webp"):
            sys.exit(f"Diagram p{page}: file must end in .png or .webp, got {d['file']!r}")

        # Always start from a fresh grayscale render of the PDF page — never from a
        # previously shipped (dithered or lossy) image.
        stem = tmp_dir / f"_diagram_p{page:04d}"
        subprocess.run(
            ["pdftoppm", "-gray", "-png", "-r", str(dpi), "-singlefile",
             "-f", str(page), "-l", str(page), str(prepared), str(stem)],
            check=True,
        )
        src = stem.with_suffix(".png")
        if not src.is_file():
            sys.exit(f"pdftoppm produced no image for page {page} — is it within the PDF?")

        if depth == "mono":
            t = int(d.get("threshold", DEFAULT_THRESHOLD))
            ops = ["-normalize", "-level", "25%,75%", "-threshold", f"{t}%", "-type", "bilevel"]
            png_out = ["-strip", "-depth", "1"]
        else:
            ops = ["-normalize"]
            png_out = ["-strip"]

        if out.suffix.lower() == ".png":
            subprocess.run(["magick", str(src), *ops, *png_out, f"PNG:{out}"], check=True)
        else:
            mid = stem.with_name(stem.name + "_proc.png")
            subprocess.run(["magick", str(src), *ops, str(mid)], check=True)
            subprocess.run(["cwebp", "-quiet", "-lossless", str(mid), "-o", str(out)], check=True)
            mid.unlink()
        src.unlink()
        kb = out.stat().st_size // 1024
        note = f" threshold {d.get('threshold', DEFAULT_THRESHOLD)}%" if depth == "mono" else ""
        print(f"  p{page:<4} {depth:<4}{note} -> {d['file']}  ({kb} KB)")
    print(f"Rendered {len(diagrams)} diagram image(s).")
    print("These are committed to the repo (see MAINTAINERS.md) so raw URLs serve them.")
    return 0

def render_page_images(mdir: Path, manifest: dict, dpi_override: int | None) -> int:
    """Render EVERY page to page-images/p####.png and write data/pages.json.

    Committed, unlike `pages/` (the gitignored grayscale working renders the cleanup step
    cross-checks OCR against). Two different jobs, so two directories:
      pages/        grayscale, render.dpi, gitignored — for reading faint values during cleanup
      page-images/  black-and-white, 300 dpi, committed — for SHOWING a page to a reader

    data/pages.json is the machine-readable index: a JS client (scripts/tv-reader) or an AI
    assistant can load it and address any page without parsing markdown or the PDF.
    """
    for tool in ("pdftoppm", "magick"):
        if shutil.which(tool) is None:
            sys.exit(f"Missing required tool on PATH: {tool}")
    prepared = mdir / "prepared.pdf"
    if not prepared.is_file():
        sys.exit("prepared.pdf not found — run 01_prepare_pdf.py first.")

    n_pages = int((manifest.get("source", {}) or {}).get("pages") or 0)
    if not n_pages:
        sys.exit("manifest source.pages is not set — needed to know how many pages to render.")

    render_cfg = manifest.get("render", {}) or {}
    dpi = dpi_override or render_cfg.get("page_image_dpi", DEFAULT_PAGE_IMAGE_DPI)
    threshold = int(render_cfg.get("page_image_threshold", DEFAULT_THRESHOLD))

    # Per-page threshold overrides, same idea as a diagram's `threshold:`. A page with darker
    # paper or a darker watermark needs a lighter cut or it comes out speckled / with the
    # watermark as solid black. Two sources, manifest wins:
    #   - any `diagrams:` entry that already carries a tuned `threshold:` for that page
    #   - `render.page_image_thresholds: {8: 35, 467: 42}` for pages with no diagram entry
    overrides = {int(d["page"]): int(d["threshold"])
                 for d in (manifest.get("diagrams") or []) if d.get("threshold")}
    overrides.update({int(k): int(v)
                      for k, v in (render_cfg.get("page_image_thresholds") or {}).items()})
    if overrides:
        print(f"  (threshold overrides on {len(overrides)} page(s): "
              + ", ".join(f"p{k}={v}%" for k, v in sorted(overrides.items())) + ")")

    out_dir = mdir / "page-images"
    out_dir.mkdir(exist_ok=True)
    tmp_dir = mdir / "pages"
    tmp_dir.mkdir(exist_ok=True)

    # pdftoppm reparses the whole PDF for every page it is asked for, so a serial loop over a
    # 450-page, 90 MB scan takes the better part of an hour. The pages are independent, so run
    # them across a worker pool — minutes instead.
    workers = max(1, min(8, (os.cpu_count() or 4)))
    print(f"Rendering {n_pages} page image(s) at {dpi} DPI, threshold {threshold}%, "
          f"{workers} workers -> {out_dir.relative_to(mdir)}/p####.png ...")

    def render_one(page: int) -> int:
        t = overrides.get(page, threshold)
        out = out_dir / f"p{page:04d}.png"
        stem = tmp_dir / f"_page_p{page:04d}"
        subprocess.run(
            ["pdftoppm", "-gray", "-png", "-r", str(dpi), "-singlefile",
             "-f", str(page), "-l", str(page), str(prepared), str(stem)],
            check=True, capture_output=True,
        )
        src = stem.with_suffix(".png")
        if not src.is_file():
            raise RuntimeError(f"pdftoppm produced no image for page {page}")
        subprocess.run(
            ["magick", str(src), "-normalize", "-level", "25%,75%",
             "-threshold", f"{t}%", "-type", "bilevel",
             "-strip", "-depth", "1", f"PNG:{out}"],
            check=True, capture_output=True,
        )
        src.unlink()
        return page

    done = 0
    with cf.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(render_one, p): p for p in range(1, n_pages + 1)}
        for fut in cf.as_completed(futures):
            try:
                fut.result()
            except Exception as exc:                      # noqa: BLE001 — report and stop
                sys.exit(f"Failed rendering page {futures[fut]}: {exc}")
            done += 1
            if done % 50 == 0 or done == n_pages:
                print(f"  ...{done}/{n_pages}")

    write_pages_json(mdir, manifest, dpi, threshold)
    total = sum(f.stat().st_size for f in out_dir.glob("p*.png"))
    print(f"Rendered {n_pages} page image(s), {total / 1048576:.1f} MB total.")
    print(f"Wrote {(mdir / 'data' / 'pages.json')}")
    return 0


def write_pages_json(mdir: Path, manifest: dict, dpi: int, threshold: int) -> None:
    """Index every page image: page number, file, pixel size, bytes, chapter, diagram caption."""
    import json

    out_dir = mdir / "page-images"
    chapters = manifest.get("chapters") or []
    diagrams = {d["page"]: d for d in (manifest.get("diagrams") or [])}

    def chapter_of(page: int):
        for ch in chapters:
            if ch["page_start"] <= page <= ch["page_end"]:
                return ch
        return None

    pages = []
    for f in sorted(out_dir.glob("p*.png")):
        page = int(f.stem[1:])
        try:
            w, h = subprocess.run(["magick", "identify", "-format", "%w %h", str(f)],
                                  capture_output=True, text=True, check=True).stdout.split()
        except (subprocess.CalledProcessError, ValueError):
            w = h = None
        ch = chapter_of(page)
        d = diagrams.get(page)
        pages.append({
            "page": page,
            "file": f"page-images/{f.name}",
            "width": int(w) if w else None,
            "height": int(h) if h else None,
            "bytes": f.stat().st_size,
            "chapter_file": (f"wiki/{ch['file']}" if ch else None),
            "chapter_title": (ch.get("title") if ch else None),
            "section_code": (ch.get("section_code") if ch else None),
            "diagram": ({"file": d["file"], "kind": d["kind"],
                         "caption": d["caption"],
                         "safety_relevant": bool(d.get("safety_relevant", False))} if d else None),
        })

    # Both base URLs, so a consumer picks: raw is verified to work with external AI readers,
    # the CDN is better for a client that loads many images (scripts/tv-reader). Same files.
    repo = branch = None
    try:
        remote = subprocess.run(["git", "remote", "get-url", "origin"], cwd=mdir,
                                capture_output=True, text=True, check=True).stdout.strip()
        m = re.search(r"github\.com[:/](.+?)(?:\.git)?$", remote)
        repo = m.group(1) if m else None
        branch = subprocess.run(["git", "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD"],
                                cwd=mdir, capture_output=True, text=True).stdout.strip().split("/")[-1] or "main"
    except subprocess.CalledProcessError:
        pass
    try:
        rel = mdir.resolve().relative_to(REPO_ROOT).as_posix() if repo else None
    except ValueError:          # manual dir outside the repo — no canonical public URL
        rel = repo = None

    doc = {
        "slug": manifest.get("slug"),
        "title": manifest.get("title"),
        "page_count": len(pages),
        "image": {"format": "png", "depth": "bilevel", "dpi": dpi,
                  "threshold_default": threshold, "dir": "page-images"},
        "base_url": ({
            # verified working with external AI readers (correct content-type, no redirect)
            "raw": f"https://raw.githubusercontent.com/{repo}/{branch}/{rel}/",
            # CDN in front of the same files — better for a client loading many pages
            "cdn": f"https://cdn.jsdelivr.net/gh/{repo}@{branch}/{rel}/",
        } if repo else None),
        "source_pdf": (manifest.get("source", {}) or {}).get("location"),
        "chapters": [
            {"file": f"wiki/{c['file']}", "title": c.get("title"),
             "section_code": c.get("section_code"),
             "page_start": c["page_start"], "page_end": c["page_end"]}
            for c in chapters
        ],
        "pages": pages,
    }
    data = mdir / "data"
    data.mkdir(exist_ok=True)
    (data / "pages.json").write_text(json.dumps(doc, indent=1) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manual_dir")
    ap.add_argument("--dpi", type=int, default=None, help="override render.dpi (all-pages mode)")
    ap.add_argument(
        "--diagrams", action="store_true",
        help="render only the manifest `diagrams:` pages (PNG or WebP, by file extension)",
    )
    ap.add_argument(
        "--diagram-dpi", type=int, default=None,
        help=f"override render.diagram_dpi (default {DEFAULT_DIAGRAM_DPI}) in --diagrams mode",
    )
    ap.add_argument(
        "--page-images", action="store_true",
        help="render EVERY page to page-images/ and write data/pages.json",
    )
    ap.add_argument(
        "--page-image-dpi", type=int, default=None,
        help=f"override render.page_image_dpi (default {DEFAULT_PAGE_IMAGE_DPI})",
    )
    args = ap.parse_args()

    if shutil.which("pdftoppm") is None:
        sys.exit("Missing required tool on PATH: pdftoppm (install poppler-utils)")

    mdir = manual_dir(args.manual_dir)
    manifest = load_manifest(mdir)

    if args.diagrams:
        return render_diagrams(mdir, manifest, args.diagram_dpi)
    if args.page_images:
        return render_page_images(mdir, manifest, args.page_image_dpi)
    return render_all_pages(mdir, manifest, args.dpi)


if __name__ == "__main__":
    raise SystemExit(main())
