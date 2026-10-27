#!/usr/bin/env python3
"""Generate docs/manuals.json — the index the hosted reader loads.

The hosted reader is static: it needs one small file telling it which manuals have
pre-rendered page images and where each manual's pages.json lives on the CDN. Only
manuals with data/pages.json qualify, because the hosted page has no server to
rasterise a PDF for it and Release PDFs cannot be fetched cross-origin.

Usage:
  python scripts/tv-reader/build_site.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _common import load_manifest  # noqa: E402

REPO = Path(__file__).resolve().parent.parent.parent
OUT = REPO / "docs" / "manuals.json"


def pinned_ref() -> str:
    """The commit the hosted reader should load assets from.

    jsDelivr caches a branch ref (`@main`) for up to 12 hours, so a reader pointed at
    `@main` can serve a stale pages.json against fresh images — or a pages.json whose
    shape predates the current one. A commit SHA is immutable, cached permanently,
    and served immediately, so pin one and regenerate when a manual changes.
    """
    sha = subprocess.run(["git", "-C", str(REPO), "rev-parse", "origin/main"],
                         capture_output=True, text=True).stdout.strip()
    if not re.fullmatch(r"[0-9a-f]{40}", sha):
        sys.exit("Could not resolve origin/main — fetch first, or pass a ref by hand.")
    return sha


def main() -> None:
    ref = pinned_ref()
    manuals = []
    for mf in sorted(REPO.glob("manuals/*/*/*/manifest.yml")):
        mdir = mf.parent
        pj = mdir / "data" / "pages.json"
        if not pj.is_file():
            continue
        manifest = load_manifest(mdir)
        data = json.loads(pj.read_text(encoding="utf-8"))
        base = (data.get("base_url") or {}).get("cdn")
        if not base:
            print(f"  skip {mdir.relative_to(REPO)}: pages.json has no cdn base_url")
            continue
        # Repoint the manual's own base at the pinned commit.
        base = re.sub(r"@[^/]+/", f"@{ref}/", base.rstrip("/") + "/", count=1)
        manuals.append({
            "slug": manifest.get("slug", mdir.name),
            "title": manifest.get("title", mdir.name),
            "pages": len(data.get("pages") or []),
            "base": base,
            "pages_json": base + "data/pages.json",
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"ref": ref, "manuals": manuals}, indent=1) + "\n",
                   encoding="utf-8")
    print(f"pinned to origin/main {ref[:12]}")
    print(f"{OUT.relative_to(REPO)}: {len(manuals)} manual(s) with page images")
    for m in manuals:
        print(f"  {m['slug']}  {m['pages']} pages")
    if not manuals:
        print("  (none — run the page-image render for a manual first)")


if __name__ == "__main__":
    main()
