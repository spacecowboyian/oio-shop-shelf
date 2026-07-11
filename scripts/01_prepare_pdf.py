#!/usr/bin/env python3
"""01 — Prepare a source PDF: detect a missing text layer and OCR it if needed.

Usage:
    python scripts/01_prepare_pdf.py <source.pdf> <manuals/slug/>

Produces <manuals/slug/>/prepared.pdf (text-layer PDF) and
<manuals/slug/>/raw-ocr/full-text.txt (extracted text). Source PDFs are never
committed (see .gitignore); this script reads from wherever you point it.

Requires: ocrmypdf, pdffonts, pdftotext (poppler-utils) on PATH.
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source_pdf", type=Path)
    ap.add_argument("manual_dir")
    ap.add_argument("--force", action="store_true", help="OCR even if a text layer exists")
    args = ap.parse_args()

    require_tools("pdffonts", "pdftotext")
    mdir = manual_dir(args.manual_dir)
    manifest = load_manifest(mdir)
    if not args.source_pdf.is_file():
        sys.exit(f"Source PDF not found: {args.source_pdf}")

    ocr_cfg = manifest.get("ocr", {}) or {}
    force = args.force or bool(ocr_cfg.get("force"))
    lang = ocr_cfg.get("language", "eng")

    prepared = mdir / "prepared.pdf"
    raw_dir = mdir / "raw-ocr"
    raw_dir.mkdir(exist_ok=True)

    if has_text_layer(args.source_pdf) and not force:
        print("Text layer detected — copying source to prepared.pdf (no OCR).")
        shutil.copyfile(args.source_pdf, prepared)
    else:
        require_tools("ocrmypdf")
        reason = "forced" if force else "no text layer detected"
        print(f"Running OCR ({reason}, lang={lang}) — this can take a while...")
        subprocess.run(
            ["ocrmypdf", "--rotate-pages", "--deskew", "--language", lang,
             ("--force-ocr" if force else "--skip-text"),
             str(args.source_pdf), str(prepared)],
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
