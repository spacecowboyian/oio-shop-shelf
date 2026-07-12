#!/usr/bin/env python3
"""09 — Generate each manual's README front matter from its manifest + the taxonomy.

Usage:
    python scripts/09_write_frontmatter.py <manuals/.../unit/>   # one manual
    python scripts/09_write_frontmatter.py --all                 # every manual

The manifest `taxonomy:` block (make/category/models/chassis/engines) is the SOURCE OF
TRUTH. This script resolves those keys to their canonical names in manuals/taxonomy.yml and
writes a YAML front-matter block at the TOP of the manual's README.md. That front matter is
the machine-discovery layer: an agent greps it to find the right manual for a given car
(make, models, chassis, engines, years) without opening every wiki.

Only the fenced front-matter block is (re)written — the README body is never touched. If a
README does not exist yet, a minimal stub is created. Re-runs are idempotent.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import (  # noqa: E402
    load_manifest,
    load_taxonomy,
    manual_dir,
    validate_against_taxonomy,
)

MARKER = "AUTO-GENERATED — taxonomy front matter (scripts/09_write_frontmatter.py); do not edit"
# A leading YAML front-matter fence whose first line is our marker comment.
GENERATED_BLOCK_RE = re.compile(
    r"\A---\n#\s*" + re.escape(MARKER) + r".*?\n---\n(?:\n)?",
    re.DOTALL,
)


def _q(s: str) -> str:
    """Double-quote a YAML scalar, escaping backslashes and quotes."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def _list(items: list[str]) -> str:
    return "[" + ", ".join(_q(i) for i in items) + "]"


def _canonical_make(tax: dict, key: str) -> str:
    return ((tax.get("makes") or {}).get(key) or {}).get("name", key)


def _canonical_names(registry: dict, keys: list[str]) -> list[str]:
    """Map a list of taxonomy keys to their `name:` values (fall back to the key)."""
    return [(registry.get(k) or {}).get("name", k) for k in keys]


def build_front_matter(manifest: dict, taxonomy: dict) -> str:
    tax = manifest.get("taxonomy") or {}
    make_key = tax.get("make", "")
    make_entry = (taxonomy.get("makes") or {}).get(make_key) or {}
    category = tax.get("category", "")

    lines = [
        "---",
        f"# {MARKER}",
        f"slug: {_q(manifest.get('slug', ''))}",
        f"title: {_q(manifest.get('title', ''))}",
        f"make: {_q(_canonical_make(taxonomy, make_key))}",
        f"category: {_q(category)}",
    ]
    if category == "vehicle":
        models = _canonical_names(make_entry.get("models") or {}, tax.get("models") or [])
        lines.append(f"models: {_list(models)}")
        if tax.get("chassis"):
            lines.append(f"chassis: {_list(tax['chassis'])}")
    # engines apply to both categories (a vehicle lists the engines it uses)
    if tax.get("engines"):
        engines = _canonical_names(make_entry.get("engines") or {}, tax["engines"])
        lines.append(f"engines: {_list(engines)}")
    if tax.get("years"):
        lines.append(f"years: {_q(tax['years'])}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def write_readme(mdir: Path, front_matter: str) -> str:
    readme = mdir / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if GENERATED_BLOCK_RE.match(text):
            new = GENERATED_BLOCK_RE.sub(front_matter + "\n", text, count=1)
            action = "updated front matter in"
        else:
            new = front_matter + "\n" + text
            action = "prepended front matter to"
    else:
        title = "README"
        for ln in front_matter.splitlines():
            if ln.startswith("title:"):
                title = ln.split(":", 1)[1].strip().strip('"')
        stub = (
            f"# {title} — Overview\n\n"
            "*Overview pending — what this manual is, what it covers, and what it doesn't.*\n\n"
            "See [`wiki/00-index.md`](wiki/00-index.md) for the chapter index.\n"
        )
        new = front_matter + "\n" + stub
        action = "created"
    readme.write_text(new, encoding="utf-8")
    return action


def process(mdir: Path, taxonomy: dict) -> bool:
    manifest = load_manifest(mdir)
    errors = validate_against_taxonomy(manifest, taxonomy)
    if errors:
        print(f"[{mdir.name}] taxonomy does not resolve — fix before generating:",
              file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return False
    fm = build_front_matter(manifest, taxonomy)
    action = write_readme(mdir, fm)
    print(f"[{mdir.name}] {action} README.md")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manual_dir", nargs="?", help="manuals/<make>/<category>/<unit>/")
    ap.add_argument("--all", action="store_true", help="every manual under manuals/")
    args = ap.parse_args()

    root = Path(__file__).resolve().parent.parent / "manuals"
    taxonomy = load_taxonomy(root)

    if args.all:
        dirs = sorted({
            p.parent for p in root.glob("**/manifest.yml")
            if "_template" not in p.relative_to(root).parts
        })
    elif args.manual_dir:
        dirs = [manual_dir(args.manual_dir)]
    else:
        sys.exit("Pass a manuals/<make>/<category>/<unit>/ dir or --all.")

    ok = all(process(d, taxonomy) for d in dirs)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
