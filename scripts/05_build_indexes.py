#!/usr/bin/env python3
"""05 — Generate index files from the cleaned chapter wiki files.

Usage:
    python scripts/05_build_indexes.py <manuals/slug/>

Generates, in <manuals/slug/>/wiki/:
    00-index.md               chapter table of contents (from manifest + headings)
    09-quick-reference.md     harvested specs (number+unit), linked to source anchors
    10-needs-review.md        rollup of every <!-- NEEDS REVIEW: ... --> comment
    11a-alphabetical-index.md alphabetical topic index built from H2/H3 headings

Never edits chapter content — only (re)writes the generated index files above.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir, wiki_dir  # noqa: E402

GENERATED = {"00-index.md", "09-quick-reference.md", "10-needs-review.md"}
# generated alphabetical-index files are "11a-…"/"11b-…" etc. Match that exact shape,
# NOT a bare "11" prefix — a chapter named "11-charging-system.md" must NOT be treated
# as generated (the 4A reference had ≤9 chapters so never surfaced this).
GENERATED_ALPHA_RE = re.compile(r"^11[a-z]?-alphabetical-index\.md$")
HEADING_RE = re.compile(r"^(#{1,3})\s+(.*?)\s*#*$")
REVIEW_RE = re.compile(r"<!--\s*NEEDS REVIEW:\s*(.*?)\s*-->", re.DOTALL)
# number + unit; covers torque, clearance, voltage, resistance, capacity, etc.
SPEC_RE = re.compile(
    r"(?P<val>\d[\d,]*(?:\.\d+)?(?:\s*[–-]\s*\d[\d,]*(?:\.\d+)?)?)\s*"
    r"(?P<unit>N·m|N-m|Nm|kgf·cm|kgf-cm|ft[·-]?lbf?|in[·-]?lbf?|mm|cm|"
    r"V|kΩ|Ω|A|mA|kPa|psi|bar|°C|°F|rpm|L|cc|mL)\b"
)
# per-page marker the cleaned chapters carry (e.g. "**[PDF p.7]**"); used to tag each
# subsection heading with the source page it lives on so 08 can bake a jump target.
PDF_PAGE_RE = re.compile(r"\[PDF p\.(\d+)\]")


def slugify_anchor(heading: str) -> str:
    """GitHub-style anchor from a heading."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s


def is_generated(name: str) -> bool:
    return (name in GENERATED
            or GENERATED_ALPHA_RE.match(name) is not None
            or name == "llm-instructions.md")


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

    specs, reviews, alpha = [], [], defaultdict(list)

    for f in files:
        lines = f.read_text(encoding="utf-8").splitlines()
        cur_page = None  # source PDF page of the most recent "[PDF p.N]" marker
        for ln, line in enumerate(lines, 1):
            pm = PDF_PAGE_RE.search(line)
            if pm:
                cur_page = int(pm.group(1))
            m = HEADING_RE.match(line)
            if m:
                level, text = len(m.group(1)), m.group(2).strip()
                # H2/H3 subsections become alphabetical-index terms, tagged with the
                # source page they sit under (skip any heading before the first marker
                # and the boilerplate "In this chapter" TOC heading).
                if level in (2, 3) and cur_page is not None \
                        and text.strip().lower() != "in this chapter":
                    alpha[text[0].upper() if text else "#"].append((text, f.name, cur_page))
            for sm in SPEC_RE.finditer(line):
                # nearest preceding heading anchor for context
                specs.append((f.name, sm.group("val"), sm.group("unit"), line.strip()))
        for rm in REVIEW_RE.finditer("\n".join(lines)):
            reviews.append((f.name, rm.group(1).strip()))

    # 00-index.md — a chapter TABLE (not a bullet list): this is the contract
    # 08_append_index_pages.py parses to bake the clickable PDF index, so the columns
    # (code | chapter | file | page range) must survive. Rows come from the manifest
    # (authoritative page ranges); the Cleanup column reflects which chapters have a
    # committed wiki file yet.
    present = {f.name for f in files}
    idx = ["# Index — " + manifest["title"], "", "## Chapters", "",
           "| Code | Chapter | File | PDF pages | Cleanup |",
           "|---|---|---|---|---|"]
    for ch in manifest.get("chapters", []):
        fname = ch["file"]
        code = ch.get("section_code", "")
        title = ch.get("title", fname)
        rng = f"{ch['page_start']}-{ch['page_end']}"
        if fname in present:
            filecell, status = f"[{fname}]({fname})", "✅ done"
        else:
            filecell, status = fname, "⬜ pending"
        idx.append(f"| {code} | {title} | {filecell} | {rng} | {status} |")
    idx += ["", "## Reference", "",
            "- [Quick Reference (specs)](09-quick-reference.md)",
            "- [Needs Review](10-needs-review.md)",
            "- [Alphabetical Index](11a-alphabetical-index.md)", ""]
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

    # 11a-alphabetical-index.md — entries in the shape 08 parses:
    #   "- <term> — [<file>#pN](<file>#pN) ([PDF p.N])"
    # (## letter headers; same-term/page entries deduped). 08 collapses repeated
    # terms across pages when it bakes the PDF index.
    ai = ["# Alphabetical Index", "",
          "_Auto-generated from chapter subsection headings. Confirm against the "
          "source manual; same-term entries collapse with all their pages in the "
          "baked PDF index._", "", "---", ""]
    for letter in sorted(alpha):
        ai.append(f"## {letter}")
        ai.append("")
        for text, name, page in sorted(set(alpha[letter])):
            ai.append(f"- {text} — [{name}#p{page}]({name}#p{page}) ([PDF p.{page}])")
        ai.append("")
    (wdir / "11a-alphabetical-index.md").write_text("\n".join(ai) + "\n", encoding="utf-8")

    n_alpha = sum(len(v) for v in alpha.values())
    print(f"Generated indexes: {len(files)} cleaned chapter file(s), "
          f"{len(manifest.get('chapters', []))} manifest chapters, "
          f"{n_alpha} alpha entries, {len(specs)} specs, {len(reviews)} review flags.")
    print("Next: python scripts/06_check_links.py", args.manual_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
