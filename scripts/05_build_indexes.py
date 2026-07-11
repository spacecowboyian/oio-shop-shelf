#!/usr/bin/env python3
"""05 — Generate index files from the cleaned chapter wiki files.

Usage:
    python scripts/05_build_indexes.py <manuals/slug/>

Generates, in <manuals/slug/>/wiki/:
    00-index.md               chapter table of contents (from manifest + headings)
    09-quick-reference.md     harvested specs (number+unit), linked to source anchors
    10-needs-review.md        rollup of every <!-- NEEDS REVIEW: ... --> comment

No back-of-book alphabetical index is generated (dropped 2026-07-11 — an eval run found
a direct grep across chapter files beat a curated ~970-entry index on 8/9 real
questions; see the oio-shop-shelf decisions log). Never edits chapter content — only
(re)writes the generated index files above.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir, wiki_dir  # noqa: E402

GENERATED = {"00-index.md", "09-quick-reference.md", "10-needs-review.md"}
HEADING_RE = re.compile(r"^(#{1,3})\s+(.*?)\s*#*$")
REVIEW_RE = re.compile(r"<!--\s*NEEDS REVIEW:\s*(.*?)\s*-->", re.DOTALL)
# number + unit; covers torque, clearance, voltage, resistance, capacity, etc.
SPEC_RE = re.compile(
    r"(?P<val>\d[\d,]*(?:\.\d+)?(?:\s*[–-]\s*\d[\d,]*(?:\.\d+)?)?)\s*"
    r"(?P<unit>N·m|N-m|Nm|kgf·cm|kgf-cm|ft[·-]?lbf?|in[·-]?lbf?|mm|cm|"
    r"V|kΩ|Ω|A|mA|kPa|psi|bar|°C|°F|rpm|L|cc|mL)\b"
)


def is_generated(name: str) -> bool:
    return name in GENERATED or name == "llm-instructions.md"


def chapter_files(wdir: Path) -> list[Path]:
    return sorted(f for f in wdir.glob("*.md") if not is_generated(f.name))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manual_dir")
    args = ap.parse_args()

    mdir = manual_dir(args.manual_dir)
    manifest = load_manifest(mdir)
    wdir = wiki_dir(mdir)
    files = chapter_files(wdir)
    if not files:
        sys.exit("No chapter .md files in wiki/ yet — run the AI cleanup step first.")

    toc_rows, specs, reviews = [], [], []

    for f in files:
        lines = f.read_text(encoding="utf-8").splitlines()
        h1 = None
        for ln, line in enumerate(lines, 1):
            m = HEADING_RE.match(line)
            if m:
                level, text = len(m.group(1)), m.group(2).strip()
                if level == 1 and h1 is None:
                    h1 = text
                    toc_rows.append((f.name, text))
            for sm in SPEC_RE.finditer(line):
                # nearest preceding heading anchor for context
                specs.append((f.name, sm.group("val"), sm.group("unit"), line.strip()))
        for rm in REVIEW_RE.finditer("\n".join(lines)):
            reviews.append((f.name, rm.group(1).strip()))

    # 00-index.md
    idx = ["# Index — " + manifest["title"], "", "## Chapters", ""]
    for name, title in toc_rows:
        idx.append(f"- [{title}]({name})")
    idx += ["", "## Reference", "",
            "- [Quick Reference (specs)](09-quick-reference.md)",
            "- [Needs Review](10-needs-review.md)", ""]
    (wdir / "00-index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    # 09-quick-reference.md
    qr = ["# Quick Reference — Specifications", "",
          "_Auto-harvested spec values. Always confirm against the source manual._", "",
          "| Value | Unit | Chapter | Context |", "| ----- | ---- | ------- | ------- |"]
    for name, val, unit, ctx in specs:
        # flatten any markdown links to plain text and neutralize table-breaking chars
        ctx_clean = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", ctx)
        ctx_clean = ctx_clean.replace("|", " ").replace("`", "").replace("<", "&lt;")
        ctx_clean = re.sub(r"\s+", " ", ctx_clean).strip()[:90]
        qr.append(f"| {val} | {unit} | [{name}]({name}) | {ctx_clean} |")
    (wdir / "09-quick-reference.md").write_text("\n".join(qr) + "\n", encoding="utf-8")

    # 10-needs-review.md
    nr = ["# Needs Review", "",
          f"_{len(reviews)} flag(s) across {len(files)} chapter file(s)._", ""]
    if reviews:
        nr += ["| Chapter | Reason |", "| ------- | ------ |"]
        for name, reason in reviews:
            nr.append(f"| [{name}]({name}) | {reason.replace(chr(10), ' ').replace('|', chr(92)+'|')} |")
    else:
        nr.append("No open review flags. 🎉")
    (wdir / "10-needs-review.md").write_text("\n".join(nr) + "\n", encoding="utf-8")

    print(f"Generated indexes: {len(toc_rows)} chapters, {len(specs)} specs, "
          f"{len(reviews)} review flags.")
    print("Next: python scripts/06_check_links.py", args.manual_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
