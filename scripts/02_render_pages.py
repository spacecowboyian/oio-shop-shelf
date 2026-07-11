#!/usr/bin/env python3
"""02 — Render page images so the AI cleanup step can cross-check garbled OCR.

Usage:
    python scripts/02_render_pages.py <manuals/slug/> [--dpi 200]

Renders <manuals/slug/>/prepared.pdf into <manuals/slug/>/pages/p####.png.
The pages/ folder is gitignored (regenerable).

Requires: pdftoppm (poppler-utils) on PATH.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manual_dir")
    ap.add_argument("--dpi", type=int, default=None, help="override render.dpi from manifest")
    args = ap.parse_args()

    if shutil.which("pdftoppm") is None:
        sys.exit("Missing required tool on PATH: pdftoppm (install poppler-utils)")

    mdir = manual_dir(args.manual_dir)
    manifest = load_manifest(mdir)
    prepared = mdir / "prepared.pdf"
    if not prepared.is_file():
        sys.exit("prepared.pdf not found — run 01_prepare_pdf.py first.")

    dpi = args.dpi or (manifest.get("render", {}) or {}).get("dpi", 200)
    pages_dir = mdir / "pages"
    pages_dir.mkdir(exist_ok=True)

    print(f"Rendering {prepared.name} at {dpi} DPI -> {pages_dir}/p####.png ...")
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(dpi), str(prepared), str(pages_dir / "p")],
        check=True,
    )
    # pdftoppm names files p-<n>.png; normalize to zero-padded p####.png.
    for f in sorted(pages_dir.glob("p-*.png")):
        num = f.stem.split("-")[-1]
        f.rename(pages_dir / f"p{int(num):04d}.png")

    count = len(list(pages_dir.glob("p*.png")))
    print(f"Rendered {count} page images.")
    print("Next: python scripts/03_split_manifest.py", args.manual_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
