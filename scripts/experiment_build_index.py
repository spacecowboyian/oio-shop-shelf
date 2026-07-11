#!/usr/bin/env python3
"""EXPERIMENTAL — build one whole-manual flat lookup index (JSONL) from the wiki chapters.

Part of a one-off read-speed trial (iter6): can a single greppable index answer any
structured lookup in one hop, instead of the agent exploring + reading a chapter file?
Not part of the 01-07 pipeline; not wired into any Skill. See Brains
projects/oio/shop-shelf/eval-results-flatfile-iter6.md for context and results.

Method: flatten EVERY markdown pipe-table across every non-generated chapter file into
one row-per-fact JSONL. Each row keeps the table's own column names as fields (values
byte-preserved — never altered), plus source metadata (`_file`, `_page`, `_section`,
`_label`) and `_flags` (OCR-uncertainty from the manual's own NEEDS REVIEW comments,
attached to a row only when a numeric/quoted token from the comment appears in that row).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

WIKI = Path(__file__).parent.parent / "manuals" / "toyota-4a-fe-4a-ge" / "wiki"
OUT = Path(__file__).parent.parent / "manuals" / "toyota-4a-fe-4a-ge" / "data" / "manual-index.jsonl"

# generated/index files + the instructions file are not primary content
SKIP_FILES = {
    "00-index.md", "09-torque-specs.md", "10-needs-review.md",
    "11a-alphabetical-index.md", "11b-alphabetical-index.md",
    "11c-alphabetical-index.md", "11d-alphabetical-index.md",
    "llm-instructions.md",
}
ANCHOR_RE = re.compile(r'<a id="(p\d+)"></a>')
PDFP_RE = re.compile(r"\*\*\[PDF p\.(\d+)\]")
HEADING_RE = re.compile(r"^#{2,4}\s+(.*?)\s*#*$")
REVIEW_RE = re.compile(r"<!--\s*NEEDS REVIEW:\s*(.*?)\s*-->", re.DOTALL)
# Distinctive tokens for flag→row matching. A review comment is attached to a row ONLY
# through a token that (a) is specific enough to identify a value — a number carrying a
# decimal/comma and ≥5 chars, or a quoted phrase ≥8 chars — AND (b) is distinctive within
# its table (appears in ≤2 rows). This deliberately refuses to flag a clean row just
# because a comment mentions a common comparison value (e.g. "0.0039 in.") or a common
# cell token (e.g. "OFF"/"N.A."); only the row a comment is really about keeps the flag.
NUM_TOK_RE = re.compile(r"\d[\d.,]{6,}")  # ≥7 chars total, digit-led — long enough to
# skip common comparison values like "0.0039" while keeping anomalies like "0.00339"
QUOTE_RE = re.compile(r'"([^"]*)"')  # every quote pair; length-filtered below (a bounded
# {6,} inside the class mis-pairs quotes in comments full of short quoted terms)
SEP_RE = re.compile(r"^\|?\s*:?-{2,}")


def comment_tokens(comment: str) -> set[str]:
    toks = {t for t in NUM_TOK_RE.findall(comment) if ("." in t or "," in t)}
    toks |= {q for q in QUOTE_RE.findall(comment) if len(q) >= 6}
    return toks


def slug(header: str) -> str:
    s = header.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s or "col"


def split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def is_nav_table(headers: list[str]) -> bool:
    hs = {h.lower() for h in headers}
    return "manual page" in hs or hs == {"section", "manual page"}


def harvest_file(path: Path) -> list[dict]:
    rows: list[dict] = []
    # split into page-scoped segments on horizontal rules
    segments = re.split(r"(?m)^---\s*$", path.read_text(encoding="utf-8"))
    for seg in segments:
        lines = seg.splitlines()
        page = None
        section = None
        am = ANCHOR_RE.search(seg)
        if am:
            page = am.group(1)
        else:
            pm = PDFP_RE.search(seg)
            if pm:
                page = "p" + pm.group(1)
        comments = [c.strip().replace("\n", " ") for c in REVIEW_RE.findall(seg)]

        i = 0
        while i < len(lines):
            line = lines[i]
            hm = HEADING_RE.match(line)
            if hm:
                section = hm.group(1).strip()
            # table start: a pipe row followed by a separator row
            if line.strip().startswith("|") and i + 1 < len(lines) and SEP_RE.match(lines[i + 1].strip()):
                headers = split_row(line)
                keys = [slug(h) for h in headers]
                i += 2
                block_rows = []
                while i < len(lines) and lines[i].strip().startswith("|"):
                    cells = split_row(lines[i])
                    if not SEP_RE.match(lines[i].strip()):
                        block_rows.append(cells)
                    i += 1
                if is_nav_table(headers):
                    continue
                raws = [" | ".join((cs + [""] * len(keys))[: len(keys)]) for cs in block_rows]
                # count how many rows of THIS table each comment-token appears in,
                # so we can require a token be distinctive (≤2 rows) before it flags.
                tok_rowcount: dict[str, int] = {}
                for c in comments:
                    for t in comment_tokens(c):
                        if t not in tok_rowcount:
                            tok_rowcount[t] = sum(1 for r in raws if t in r)
                for cells in block_rows:
                    # pad/truncate to header width
                    cells = (cells + [""] * len(keys))[: len(keys)]
                    obj = {k: v for k, v in zip(keys, cells)}
                    raw = " | ".join(cells)
                    # label = first up-to-3 non-empty, non-pure-number cells
                    label_parts = [c for c in cells if c and not re.fullmatch(r"[\d.,\s–-]+", c)][:3]
                    flags = []
                    for c in comments:
                        toks = [t for t in comment_tokens(c) if t in raw and tok_rowcount.get(t, 0) <= 2]
                        if toks:
                            flags.append(c)
                    rows.append({
                        "_file": f"wiki/{path.name}",
                        "_page": page,
                        "_section": section,
                        "_label": " — ".join(label_parts),
                        **obj,
                        "_flags": flags,
                    })
                continue
            i += 1
    return rows


def main() -> None:
    files = sorted(f for f in WIKI.glob("*.md") if f.name not in SKIP_FILES)
    all_rows: list[dict] = []
    for f in files:
        all_rows.extend(harvest_file(f))
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", encoding="utf-8") as out:
        for r in all_rows:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")
    flagged = sum(1 for r in all_rows if r["_flags"])
    print(f"Wrote {OUT} — {len(all_rows)} rows from {len(files)} chapters, {flagged} carry flags.")


if __name__ == "__main__":
    main()
