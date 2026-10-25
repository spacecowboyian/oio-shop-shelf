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
import json
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
    provenance = {}
    map_file = mdir / (manifest.get("composite") or {}).get("provenance_map", "")
    if manifest.get("composite"):
        if not map_file.is_file():
            sys.exit(f"Composite provenance map missing: {map_file}")
        for line in map_file.read_text().splitlines():
            row = json.loads(line)
            provenance[row["combined_page"]] = row

    for ch in manifest["chapters"]:
        ranges = ch.get("source_ranges") or [ch]
        for source_range in ranges:
            if source_range["page_end"] > max_page:
                print(f"  WARNING: {ch['file']} page_end {source_range['page_end']} > pages in PDF ({max_page})")
        if provenance:
            chunk = "\n".join(
                f"\n<!-- ORIGINAL {provenance[n]['source_id']}/{provenance[n]['filename']}"
                f" physical PDF page {provenance[n]['pdf_page']}; combined PDF page {n};"
                f" printed page {provenance[n].get('original_page') or 'UNVERIFIED'} -->\n"
                + pages[n] for source_range in ranges
                for n in range(source_range["page_start"], min(source_range["page_end"], max_page) + 1))
        else:
            chunk = "\n".join(pages[n] for source_range in ranges
                              for n in range(source_range["page_start"], min(source_range["page_end"], max_page) + 1))
        ps, pe = ranges[0]["page_start"], ranges[-1]["page_end"]
        header = (
            f"# RAW DRAFT — {ch['title']}\n"
            f"# source ranges {[(r['page_start'], r['page_end']) for r in ranges]} | output file: wiki/{ch['file']}\n"
            f"# Feed this + scripts/04_cleanup_methodology.md + images for the listed source ranges\n"
            f"# to your AI agent. Do NOT commit this draft.\n\n"
        )
        out = mdir / "raw-ocr" / (Path(ch["file"]).stem + ".draft.txt")
        out.write_text(header + chunk, encoding="utf-8")
        print(f"  wrote {out.name}  ({len(ranges)} source range(s))")

    print("\nNext: run the AI cleanup step per CONTRIBUTING.md, then 05_build_indexes.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
