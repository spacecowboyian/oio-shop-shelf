#!/usr/bin/env python3
"""01 — Prepare a source PDF: decrypt it if needed, then OCR if it has no text layer.

Usage:
    python scripts/01_prepare_pdf.py <source.pdf> <manuals/slug/>

Produces <manuals/slug/>/prepared.pdf (text-layer PDF) and
<manuals/slug/>/raw-ocr/full-text.txt (extracted text). Source PDFs are never
committed (see .gitignore); this script reads from wherever you point it.

Encrypted PDFs (common for scanned OEM manuals — often owner-password/permission
encryption that blocks copy/print) are detected and decrypted with `qpdf --decrypt`
before anything else, since ocrmypdf and text extraction fail on encrypted input.
A PDF locked with a real *user* password (needed just to open it) can't be decrypted
without that password and is reported as such.

Requires: pdffonts, pdftotext, pdfinfo (poppler-utils) on PATH; qpdf if the source
is encrypted; ocrmypdf if it has no text layer.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir  # noqa: E402


def has_text_layer(pdf: Path) -> bool:
    """True if pdffonts reports any embedded font (a proxy for a real text layer)."""
    out = subprocess.run(
        ["pdffonts", str(pdf)], capture_output=True, text=True, check=True
    ).stdout.splitlines()
    # First two lines are the header + separator; any further line == a font.
    return len(out) > 2


def require_tools(*tools: str) -> None:
    missing = [t for t in tools if shutil.which(t) is None]
    if missing:
        sys.exit(f"Missing required tool(s) on PATH: {', '.join(missing)}")


def is_encrypted(pdf: Path) -> bool:
    """True if pdfinfo reports any encryption (owner- or user-password)."""
    out = subprocess.run(
        ["pdfinfo", str(pdf)], capture_output=True, text=True
    ).stdout
    for line in out.splitlines():
        if line.startswith("Encrypted:"):
            return not line.split(":", 1)[1].strip().lower().startswith("no")
    return False


def decrypt_pdf(src: Path, dest: Path) -> Path:
    """Strip encryption with qpdf. Works for owner-password/permission encryption
    and for an empty user password; a real user password makes this fail loudly."""
    require_tools("qpdf")
    proc = subprocess.run(
        ["qpdf", "--decrypt", str(src), str(dest)], capture_output=True, text=True
    )
    # qpdf exit codes: 0 = ok, 3 = warnings but file written; both usable.
    if proc.returncode not in (0, 3) or not dest.is_file():
        sys.exit(
            "Could not decrypt the PDF with qpdf. If it needs a password to open, "
            "decrypt it yourself first:\n"
            f"    qpdf --decrypt --password=YOURPASS '{src}' '{dest}'\n"
            f"qpdf said:\n{proc.stderr.strip()}"
        )
    return dest


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source_pdf", type=Path)
    ap.add_argument("manual_dir")
    ap.add_argument("--force", action="store_true", help="OCR even if a text layer exists")
    ap.add_argument("--language", help="tesseract language code(s), e.g. 'eng' or 'eng+deu'. "
                                       "Overrides the manifest; use it when running before the "
                                       "manifest exists and the manual isn't English.")
    args = ap.parse_args()

    require_tools("pdffonts", "pdftotext", "pdfinfo")
    # 01 can run before the manifest is authored — you often want the OCR'd text
    # first so you can read the manual's own table of contents while writing the
    # chapter page ranges. So the manifest is optional here (defaults: eng, no force).
    mdir = manual_dir(args.manual_dir, require_manifest=False)
    manifest = load_manifest(mdir, required=False)
    if not manifest:
        print("No manifest.yml yet — using defaults (lang=eng, no force). "
              "Author the manifest next; 01 only needs the source PDF + this directory.")
    if not args.source_pdf.is_file():
        sys.exit(f"Source PDF not found: {args.source_pdf}")

    ocr_cfg = manifest.get("ocr", {}) or {}
    force = args.force or bool(ocr_cfg.get("force"))
    lang = args.language or ocr_cfg.get("language") or "eng"

    prepared = mdir / "prepared.pdf"
    raw_dir = mdir / "raw-ocr"
    raw_dir.mkdir(exist_ok=True)

    # 0) Decrypt first — ocrmypdf and pdftotext both fail on encrypted input.
    source = args.source_pdf
    if is_encrypted(source):
        print("Encrypted PDF detected — decrypting with qpdf...")
        source = decrypt_pdf(source, raw_dir / "decrypted.pdf")

    if has_text_layer(source) and not force:
        print("Text layer detected — copying source to prepared.pdf (no OCR).")
        shutil.copyfile(source, prepared)
    else:
        require_tools("ocrmypdf")
        reason = "forced" if force else "no text layer detected"
        print(f"Running OCR ({reason}, lang={lang}) — this can take a while...")
        subprocess.run(
            ["ocrmypdf", "--rotate-pages", "--deskew", "--language", lang,
             ("--force-ocr" if force else "--skip-text"),
             str(source), str(prepared)],
            check=True,
        )

    text_out = raw_dir / "full-text.txt"
    subprocess.run(["pdftotext", "-layout", str(prepared), str(text_out)], check=True)
    n = sum(1 for _ in text_out.open(encoding="utf-8", errors="replace"))
    print(f"Wrote {prepared} and {text_out} ({n} lines).")
    print("Next: python scripts/02_render_pages.py", args.manual_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
