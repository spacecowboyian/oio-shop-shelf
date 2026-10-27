#!/usr/bin/env python3
"""Detect abridged / incomplete scans by checking section page-number continuity.

Usage:
    python scripts/check_page_continuity.py <manuals/slug/>

OEM manuals number pages *within* a section (e.g. ST-1, ST-2, ... EM-15). A clean
scan has a contiguous run per section; a jump (ST-3 -> ST-15) means pages are missing
from the scan. This reads raw-ocr/full-text.txt (run 01 first), and for each manifest
chapter reports the section code, the relative page numbers actually seen, and any
suspected gaps. Informational: it warns, it never fails the build — genuine gaps are a
property of the source, to be recorded in 10-needs-review.md, not "fixed."
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir  # noqa: E402

# two-letter section code + relative page number, e.g. "ST-15", "EM-3"
CODE_RE = re.compile(r"\b([A-Z]{2}|6[A-E]|1[0-2]|[1-9])[-–]\s?(\d{1,3})\b")
# section codes Toyota uses in these engine manuals (extend as needed)
KNOWN = {"IN", "EM", "FI", "CO", "LU", "IG", "ST", "CH", "SS",
         "MA", "AX", "BE", "SA", "AT", "AC", "BR", "CL", "TM", "SR",
         *[str(n) for n in range(1, 13)], *[f"6{c}" for c in "ABCDE"]}
# a jump larger than this between consecutive detected pages == likely missing pages
GAP_THRESHOLD = 2


def load_pages(text_file: Path) -> list[str]:
    raw = text_file.read_text(encoding="utf-8", errors="replace")
    pages = raw.split("\f")
    # A trailing form feed leaves one empty trailing element — drop that. But do NOT drop a
    # genuinely BLANK last page: a scan whose final page carries no OCR text (a back cover,
    # say) is a real page, and popping it makes every later page index overrun the list.
    # Only the split artefact is safe to remove, so require the raw text to end in \f.
    if pages and pages[-1] == "" and raw.endswith("\f"):
        pages.pop()
    return [""] + pages  # 1-based


def edge_text(page: str, n_top: int = 2, n_bot: int = 3) -> str:
    """The running header/footer band — first n_top + last n_bot non-empty lines.

    The 'CODE-n' running page number lives here; the body is full of cross-references
    to other pages, so scanning edges only cuts that noise dramatically."""
    lines = [ln for ln in page.splitlines() if ln.strip()]
    return "\n".join(lines[:n_top] + lines[-n_bot:])


def dominant_code(pages: list[str], ps: int, pe: int) -> str | None:
    counts: Counter[str] = Counter()
    for n in range(ps, min(pe, len(pages) - 1) + 1):
        for m in CODE_RE.finditer(edge_text(pages[n])):
            if m.group(1) in KNOWN:
                counts[m.group(1)] += 1
    return counts.most_common(1)[0][0] if counts else None


def page_relnums(pages: list[str], ps: int, pe: int, code: str) -> list[tuple[int, int]]:
    """Best (physical page, relative page number) guess per page for `code`, read from
    the header/footer band only (the running page number), not the body cross-refs."""
    seq: list[tuple[int, int]] = []
    for n in range(ps, min(pe, len(pages) - 1) + 1):
        # Numeric Chevrolet section codes occur frequently in body cross-references.
        # Their running page number is in the first two nonempty OCR lines.
        text = ("\n".join([x for x in pages[n].splitlines() if x.strip()][:2])
                if code[0].isdigit() else edge_text(pages[n]))
        nums = [int(m.group(2)) for m in CODE_RE.finditer(text)
                if m.group(1) == code]
        if nums:
            seq.append((n, min(nums)))
    return seq


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manual_dir")
    args = ap.parse_args()

    mdir = manual_dir(args.manual_dir)
    manifest = load_manifest(mdir)
    if manifest.get("composite"):
        from validate_composite_map import validate  # noqa: E402
        errors = validate(mdir)
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        rows = [json.loads(line) for line in
                (mdir / manifest["composite"]["provenance_map"]).read_text().splitlines()]
        groups = defaultdict(list)
        for row in rows:
            groups[(row["source_id"], row["filename"])].append(row)
        anomalies = 0
        for key, group in groups.items():
            labeled = []
            for row in group:
                match = CODE_RE.fullmatch(row.get("original_page") or "")
                if match:
                    labeled.append((row["pdf_page"], match.group(1), int(match.group(2))))
            for (p0, c0, n0), (p1, c1, n1) in zip(labeled, labeled[1:]):
                if c0 == c1 and n1 - n0 != p1 - p0:
                    anomalies += 1
                    print(f"  review {key[1]}: OCR running page {c0}-{n0} (PDF {p0}) "
                          f"to {c1}-{n1} (PDF {p1})")
        print(f"Composite physical-page continuity OK: {len(rows)} pages from {len(groups)} PDFs. "
              f"{anomalies} printed-number/OCR anomaly pair(s) need image review.")
        return 0
    text_file = mdir / "raw-ocr" / "full-text.txt"
    if not text_file.is_file():
        sys.exit("raw-ocr/full-text.txt not found — run 01_prepare_pdf.py first.")

    pages = load_pages(text_file)
    warnings = 0
    print(f"Page-continuity check — {manifest['slug']} ({len(pages) - 1} pages)\n")

    for ch in manifest["chapters"]:
        for source_range in ch.get("source_ranges") or [ch]:
            ps, pe = source_range["page_start"], source_range["page_end"]
            label = source_range.get("source_file", ch["file"])
            # Honor explicit section codes; infer when absent.
            code = ch.get("section_code") or dominant_code(pages, ps, pe)
            if not code:
                print(f"  {label}: no section code detected (image-heavy?) — skipped")
                continue
            seq = page_relnums(pages, ps, pe, code)
            if not seq:
                print(f"  {label} [{code}]: no '{code}-N' page numbers found — skipped")
                continue
            relnums = [r for _, r in seq]
            lo, hi = min(relnums), max(relnums)
            gaps = []
            for (p0, r0), (p1, r1) in zip(seq, seq[1:]):
                if r1 - r0 > p1 - p0 + GAP_THRESHOLD:
                    gaps.append((r0, r1, p1))
            span_ok = (hi - lo + 1) <= (pe - ps + 1) + GAP_THRESHOLD
            flag = "  ⚠ GAP" if (gaps or not span_ok) else "  ok"
            print(f"{flag}  {label} [{code}]  rel {lo}-{hi} across phys {ps}-{pe}")
            for r0, r1, p1 in gaps:
                print(f"        jump {code}-{r0} → {code}-{r1} at phys p.{p1} "
                      f"(≈{r1 - r0 - 1} page(s) missing)")
                warnings += 1
            if not span_ok:
                print(f"        section spans {hi - lo + 1} numbered pages but only "
                      f"{pe - ps + 1} physical pages present")
                warnings += 1

    print(f"\n{warnings} suspected gap(s). Record real gaps in wiki/10-needs-review.md; "
          "this check never fails the build.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
