#!/usr/bin/env python3
"""06 — Link-integrity checker. Validates every internal markdown link resolves.

Usage:
    python scripts/06_check_links.py <manuals/slug/> [<manuals/slug2/> ...]
    python scripts/06_check_links.py --all          # every manual under manuals/

Checks each internal [text](file#anchor) link in wiki/*.md:
  - the target file exists in the same wiki/ folder
  - the #anchor (if present) resolves to one of:
      * a markdown heading (GitHub-slugified),
      * an explicit HTML anchor: <a id="..."> or <a name="...">,
      * a heading attribute id: ## Title {#custom-id}

Exits non-zero if any link is broken — suitable for CI. External links
(http/https/mailto) and image links are skipped.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# [text](target)  — captures the target; ignores images ![...](...) via negative lookbehind
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*$")
HTML_ANCHOR_RE = re.compile(r'<a\s+[^>]*?(?:id|name)\s*=\s*"([^"]+)"', re.IGNORECASE)
HEADING_ATTR_RE = re.compile(r"\{#([\w-]+)\}")


def _slug(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s)


def anchors_for(md_file: Path) -> set[str]:
    anchors: set[str] = set()
    text = md_file.read_text(encoding="utf-8")
    # explicit HTML anchors (<a id="p3"></a>) and {#custom-id} attributes
    anchors.update(HTML_ANCHOR_RE.findall(text))
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            heading = m.group(1)
            attr = HEADING_ATTR_RE.search(heading)
            if attr:
                anchors.add(attr.group(1))
                heading = HEADING_ATTR_RE.sub("", heading)
            anchors.add(_slug(heading))
    return anchors


def check_manual(mdir: Path) -> list[str]:
    wdir = mdir / "wiki"
    problems: list[str] = []
    if not wdir.is_dir():
        return [f"{mdir}: no wiki/ folder"]
    anchor_cache: dict[Path, set[str]] = {}
    for md in sorted(wdir.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                if target.startswith("#"):
                    # in-page anchor
                    anchor = target[1:]
                    cache = anchor_cache.setdefault(md, anchors_for(md))
                    if anchor and anchor not in cache:
                        problems.append(f"{md.name}: missing in-page anchor '#{anchor}'")
                continue
            file_part, _, anchor = target.partition("#")
            if not file_part:
                continue
            tgt = (wdir / file_part).resolve()
            if not tgt.is_file():
                problems.append(f"{md.name}: broken link target '{file_part}'")
                continue
            if anchor:
                cache = anchor_cache.setdefault(tgt, anchors_for(tgt))
                if anchor not in cache:
                    problems.append(f"{md.name}: '{file_part}' has no anchor '#{anchor}'")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manual_dirs", nargs="*", help="manuals/<slug>/ directories")
    ap.add_argument("--all", action="store_true", help="check every manual under manuals/")
    args = ap.parse_args()

    if args.all:
        root = Path(__file__).resolve().parent.parent / "manuals"
        dirs = [d for d in sorted(root.iterdir())
                if d.is_dir() and d.name != "_template" and (d / "wiki").is_dir()]
    else:
        dirs = [Path(d).resolve() for d in args.manual_dirs]
    if not dirs:
        sys.exit("Nothing to check. Pass manuals/<slug>/ or --all.")

    all_problems: list[str] = []
    for d in dirs:
        probs = check_manual(d)
        tag = d.name
        if probs:
            all_problems += [f"[{tag}] {p}" for p in probs]
        else:
            print(f"[{tag}] OK — all internal links resolve.")

    if all_problems:
        print("\nBROKEN LINKS:", file=sys.stderr)
        for p in all_problems:
            print("  " + p, file=sys.stderr)
        print(f"\n{len(all_problems)} problem(s) found.", file=sys.stderr)
        return 1
    print("\nAll links OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
