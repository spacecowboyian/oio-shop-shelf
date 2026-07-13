#!/usr/bin/env python3
"""Build a whole-manual flat lookup index (JSONL) from a manual's wiki chapters.

Usage:
    python scripts/build_manual_index.py manuals/<make>/<category>/<unit>/
    python scripts/build_manual_index.py  # builds all manuals under manuals/

Each row in the output keeps the table's own column names as fields (values
byte-preserved — never altered), plus source metadata (_file, _page, _section,
_label) and _flags (OCR-uncertainty from the manual's own NEEDS REVIEW comments,
attached to a row only when a numeric/quoted token from the comment appears in
that row and is distinctive within its table).

Output: manuals/<make>/<category>/<unit>/data/manual-index.jsonl

Proven to reduce lookup duration 21%, tokens 24%, tool calls 33% vs. markdown
baseline. See Brains projects/oio/shop-shelf/decisions.md (iter6 entry) for
full evaluation results.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent

ANCHOR_RE = re.compile(r'<a id="(p\d+)"></a>')
PDFP_RE = re.compile(r"\*\*\[PDF p\.(\d+)\]")
HEADING_RE = re.compile(r"^#{2,4}\s+(.*?)\s*#*$")
REVIEW_RE = re.compile(r"<!--\s*NEEDS REVIEW:\s*(.*?)\s*-->", re.DOTALL)
NUM_TOK_RE = re.compile(r"\d[\d.,]{6,}")
QUOTE_RE = re.compile(r'"([^"]*)"')
SEP_RE = re.compile(r"^\|?\s*:?-{2,}")

# Filename patterns to skip — these are generated/index files, not primary content.
SKIP_NAME_RE = re.compile(
    r"^("
    r"00-index\.md"
    r"|[0-9]+-needs-review\.md"
    r"|[0-9]+-torque-specs\.md"
    r"|[0-9]+-quick-reference\.md"
    r"|[0-9]+-service-specifications.*\.md"
    r"|[0-9]+[a-z]?-alphabetical-index\.md"
    r"|all-files\.md"
    r"|llm-instructions\.md"
    r")$"
)


def should_skip(path: Path) -> bool:
    if SKIP_NAME_RE.match(path.name):
        return True
    # Also skip any file that declares itself generated in its first 200 bytes.
    try:
        head = path.read_bytes()[:200].decode("utf-8", errors="replace")
        if "<!-- generated" in head or "<!-- AUTO-GENERATED" in head.upper():
            return True
    except OSError:
        pass
    return False


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
                tok_rowcount: dict[str, int] = {}
                for c in comments:
                    for t in comment_tokens(c):
                        if t not in tok_rowcount:
                            tok_rowcount[t] = sum(1 for r in raws if t in r)
                for cells in block_rows:
                    cells = (cells + [""] * len(keys))[: len(keys)]
                    obj = {k: v for k, v in zip(keys, cells)}
                    raw = " | ".join(cells)
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


def build_index(manual_dir: Path) -> None:
    wiki = manual_dir / "wiki"
    if not wiki.is_dir():
        print(f"  skip {manual_dir} — no wiki/ subdirectory")
        return
    out = manual_dir / "data" / "manual-index.jsonl"
    files = sorted(f for f in wiki.glob("*.md") if not should_skip(f))
    if not files:
        print(f"  skip {manual_dir} — no chapter files found after filtering")
        return
    all_rows: list[dict] = []
    for f in files:
        all_rows.extend(harvest_file(f))
    out.parent.mkdir(exist_ok=True)
    with out.open("w", encoding="utf-8") as fh:
        for r in all_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    flagged = sum(1 for r in all_rows if r["_flags"])
    print(f"  {out.relative_to(REPO)} — {len(all_rows)} rows from {len(files)} chapters, {flagged} flagged")


def find_manuals() -> list[Path]:
    manuals_root = REPO / "manuals"
    results = []
    for wiki in sorted(manuals_root.rglob("wiki")):
        if wiki.is_dir() and wiki.parent != manuals_root:
            results.append(wiki.parent)
    return results


def main() -> None:
    if len(sys.argv) > 1:
        targets = [REPO / sys.argv[1].rstrip("/")]
    else:
        targets = find_manuals()

    for manual_dir in targets:
        # Skip manuals that already have a current index (use --force to rebuild).
        out = manual_dir / "data" / "manual-index.jsonl"
        if out.exists() and "--force" not in sys.argv:
            print(f"  skip {manual_dir.relative_to(REPO)} — index already exists (use --force to rebuild)")
            continue
        print(f"Building index for {manual_dir.relative_to(REPO)} ...")
        build_index(manual_dir)


if __name__ == "__main__":
    main()
