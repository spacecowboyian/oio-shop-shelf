#!/usr/bin/env python3
"""Build a flat one-fact-per-line JSONL lookup index for a manual — the fast-path a
browsing/voice agent fetches ONCE to answer a spec question (torque, clearance, capacity,
part number) in one hop, instead of reading whole chapters.

    python scripts/build_manual_index.py manuals/<make>/<cat>/<unit>/

Writes <manual>/data/manual-index.jsonl. Method: flatten every markdown pipe-table across
the cleaned chapter files into one row per fact. Each row keeps the table's own column
names as fields (values byte-preserved — NEVER altered), plus `_page` (the source PDF page
so the agent can cite it), `_file`, `_section`, `_label`, and `_flags` (the manual's own
NEEDS REVIEW notes, attached only to the row a note is really about).

Recognizes all page-marker styles used across this repo's manuals:
  <!-- PDF p.N -->   ·   <a id="pN"></a>   ·   **[PDF p.N]**
Page is tracked line-by-line, so it works whether or not pages are separated by `---`.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# generated / index / instruction files are not primary content
SKIP_FILES = {
    "00-index.md", "09-quick-reference.md", "09-torque-specs.md", "10-needs-review.md",
    "11a-alphabetical-index.md", "11b-alphabetical-index.md",
    "11c-alphabetical-index.md", "11d-alphabetical-index.md",
    "llm-instructions.md", "all-files.md",
}
PAGE_RES = [
    re.compile(r"<!--\s*PDF p\.(\d+)"),        # Renault-style inline marker
    re.compile(r'<a id="p(\d+)"></a>'),        # anchor style
    re.compile(r"\*\*\[PDF p\.(\d+)\]"),       # linked style
]
HEADING_RE = re.compile(r"^#{2,4}\s+(.*?)\s*#*$")
REVIEW_RE = re.compile(r"<!--\s*NEEDS REVIEW:\s*(.*?)\s*-->", re.DOTALL)
# Prose spec statements — a value+unit stated in running text or a NOTE (e.g. a torque in a
# procedure step), which the table-flattener misses. Torque especially is often prose-only.
PROSE_UNIT_RE = re.compile(
    r"\d[\d.,]*\s*(?:m\.?kg|kg\.?m|lbs?\.?[\s/]?ft|ft\.?[\s/]?lbs?|"
    r"kg/sq\.?cm|lbs?/sq|psi|°|ohms?|Ω)", re.I)
NUM_TOK_RE = re.compile(r"\d[\d.,]{6,}")
QUOTE_RE = re.compile(r'"([^"]*)"')
SEP_RE = re.compile(r"^\|?\s*:?-{2,}")


def comment_tokens(comment: str) -> set[str]:
    toks = {t for t in NUM_TOK_RE.findall(comment) if ("." in t or "," in t)}
    toks |= {q for q in QUOTE_RE.findall(comment) if len(q) >= 6}
    return toks


def slug(header: str) -> str:
    s = re.sub(r"[^\w\s-]", "", header.strip().lower())
    s = re.sub(r"\s+", "-", s).strip("-")
    return s or "col"


def split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def page_of(line: str):
    for rx in PAGE_RES:
        m = rx.search(line)
        if m:
            return "p" + m.group(1)
    return None


def harvest_file(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    comments = [c.strip().replace("\n", " ") for c in REVIEW_RE.findall(text)]
    # doc-level distinctiveness for attaching a flag to a prose row: how many times each
    # comment token occurs in the whole file (attach only when it's specific, ≤3 hits).
    comment_tokens_count: dict[str, int] = {}
    for c in comments:
        for t in comment_tokens(c):
            comment_tokens_count.setdefault(t, text.count(t))
    rows: list[dict] = []
    page = None
    section = None
    i = 0
    while i < len(lines):
        line = lines[i]
        pg = page_of(line)
        if pg:
            page = pg
        hm = HEADING_RE.match(line)
        if hm:
            section = hm.group(1).strip()
        # prose spec statement (value+unit in running text / a NOTE) — the table-flattener
        # misses these, and torque is often prose-only. Strip list/quote/emphasis markers.
        if not line.strip().startswith("|"):
            txt = re.sub(r"^[\s>*\-\d.)]+", "", line).strip().replace("**", "")
            txt = re.sub(r"<!--.*?-->", "", txt).strip()
            if txt and len(txt) <= 240 and PROSE_UNIT_RE.search(txt):
                fl = [c for c in comments
                      if any(t in txt and comment_tokens_count.get(t, 0) <= 3 for t in comment_tokens(c))]
                rows.append({"_file": f"wiki/{path.name}", "_page": page,
                             "_section": section, "_type": "spec", "text": txt, "_flags": fl})
        # table = pipe header row followed by a separator row
        if line.strip().startswith("|") and i + 1 < len(lines) and SEP_RE.match(lines[i + 1].strip()):
            headers = split_row(line)
            keys = [slug(h) for h in headers]
            i += 2
            block_rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not SEP_RE.match(lines[i].strip()):
                    block_rows.append(split_row(lines[i]))
                i += 1
            raws = [" | ".join((cs + [""] * len(keys))[: len(keys)]) for cs in block_rows]
            tok_rowcount: dict[str, int] = {}
            for c in comments:
                for t in comment_tokens(c):
                    tok_rowcount.setdefault(t, sum(1 for r in raws if t in r))
            for cells in block_rows:
                cells = (cells + [""] * len(keys))[: len(keys)]
                obj = {k: v for k, v in zip(keys, cells)}
                raw = " | ".join(cells)
                label_parts = [c for c in cells if c and not re.fullmatch(r"[\d.,\s–-]+", c)][:3]
                flags = [c for c in comments
                         if any(t in raw and tok_rowcount.get(t, 0) <= 2 for t in comment_tokens(c))]
                rows.append({
                    "_file": f"wiki/{path.name}", "_page": page, "_section": section,
                    "_label": " — ".join(label_parts), **obj, "_flags": flags,
                })
            continue
        i += 1
    return rows


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit("usage: python scripts/build_manual_index.py manuals/<make>/<cat>/<unit>/")
    mdir = Path(sys.argv[1]).resolve()
    wiki = mdir / "wiki"
    if not wiki.is_dir():
        sys.exit(f"No wiki/ in {mdir}")
    files = sorted(f for f in wiki.glob("*.md") if f.name not in SKIP_FILES)
    all_rows: list[dict] = []
    for f in files:
        all_rows.extend(harvest_file(f))
    out = mdir / "data" / "manual-index.jsonl"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", encoding="utf-8") as fh:
        for r in all_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    flagged = sum(1 for r in all_rows if r["_flags"])
    no_page = sum(1 for r in all_rows if not r["_page"])
    print(f"Wrote {out} — {len(all_rows)} rows from {len(files)} chapters, "
          f"{flagged} carry flags, {no_page} missing a page.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
