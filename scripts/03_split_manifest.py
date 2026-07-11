#!/usr/bin/env python3
"""03 — Slice the full OCR text into per-chapter raw drafts per manifest.yml.

Usage:
    python scripts/03_split_manifest.py <manuals/slug/>

Reads <manuals/slug/>/raw-ocr/full-text.txt (page-delimited by form-feed, which
pdftotext emits between pages) and writes one draft per chapter into
<manuals/slug/>/raw-ocr/<file>.draft.txt using the page ranges in the manifest.

These drafts are the input to the AI cleanup step (04_cleanup_methodology.md).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir  # noqa: E402


def load_pages(text_file: Path) -> list[str]:
    """Split pdftotext output into a 1-based list of page strings.

    pdftotext separates pages with a form-feed (\\f). Index 0 is a sentinel so
    pages[n] == page n.
    """
    raw = text_file.read_text(encoding="utf-8", errors="replace")
    pages = raw.split("\f")
    if pages and pages[-1].strip() == "":
        pages.pop()
    return [""] + pages  # 1-based


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manual_dir")
    args = ap.parse_args()

    mdir = manual_dir(args.manual_dir)
    manifest = load_manifest(mdir)
    text_file = mdir / "raw-ocr" / "full-text.txt"
    if not text_file.is_file():
        sys.exit("raw-ocr/full-text.txt not found — run 01_prepare_pdf.py first.")

    pages = load_pages(text_file)
    max_page = len(pages) - 1
    print(f"Loaded {max_page} pages of OCR text.")

    for ch in manifest["chapters"]:
        ps, pe = ch["page_start"], ch["page_end"]
        if pe > max_page:
            print(f"  WARNING: {ch['file']} page_end {pe} > pages in PDF ({max_page})")
        chunk = "\n".join(pages[ps:pe + 1])
        header = (
            f"# RAW DRAFT — {ch['title']}\n"
            f"# source pages {ps}-{pe} | output file: wiki/{ch['file']}\n"
            f"# Feed this + scripts/04_cleanup_methodology.md + pages/p{ps:04d}.png..p{pe:04d}.png\n"
            f"# to your AI agent. Do NOT commit this draft.\n\n"
        )
        out = mdir / "raw-ocr" / (Path(ch["file"]).stem + ".draft.txt")
        out.write_text(header + chunk, encoding="utf-8")
        print(f"  wrote {out.name}  (pages {ps}-{pe})")

    print("\nNext: run the AI cleanup step per CONTRIBUTING.md, then 05_build_indexes.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
