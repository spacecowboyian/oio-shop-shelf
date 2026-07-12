#!/usr/bin/env python3
"""02 — Render page images.

Two modes:

  # Default: render EVERY page to pages/p####.png so the AI cleanup step can
  # cross-check garbled OCR against the scan. pages/ is gitignored (regenerable).
  python scripts/02_render_pages.py <manuals/slug/> [--dpi 200]

  # --diagrams: render ONLY the pages listed in the manifest `diagrams:` block,
  # each at its declared depth, to a compact lossless WebP at its `file:` path.
  # These are the diagram-only pages delivered to the user in-chat (issue #1).
  python scripts/02_render_pages.py <manuals/slug/> --diagrams [--diagram-dpi 150]

Requires: pdftoppm (poppler-utils) on PATH; also cwebp (webp) for --diagrams.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir  # noqa: E402

# Diagram delivery targets B/W print scans: color is dead weight, so we render at a
# reduced depth and store lossless WebP (see issue #1). Depth is per-diagram:
#   mono = 1-bit line art (~30 KB) — wiring diagrams, exploded views, torque sequences
#   gray = page has a photo/halftone (~70 KB) — a 1-bit threshold would wreck the photo
DEPTH_FLAG = {"mono": "-mono", "gray": "-gray"}
DEFAULT_DIAGRAM_DPI = 150


def render_all_pages(mdir: Path, manifest: dict, dpi_override: int | None) -> int:
    prepared = mdir / "prepared.pdf"
    if not prepared.is_file():
        sys.exit("prepared.pdf not found — run 01_prepare_pdf.py first.")

    dpi = dpi_override or (manifest.get("render", {}) or {}).get("dpi", 200)
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
    print("Next: python scripts/03_split_manifest.py", mdir)
    return 0


def render_diagrams(mdir: Path, manifest: dict, dpi_override: int | None) -> int:
    if shutil.which("cwebp") is None:
        sys.exit("Missing required tool on PATH: cwebp (install the 'webp' package)")

    diagrams = manifest.get("diagrams") or []
    if not diagrams:
        print("No `diagrams:` block in manifest.yml — nothing to render.")
        return 0

    prepared = mdir / "prepared.pdf"
    if not prepared.is_file():
        sys.exit("prepared.pdf not found — run 01_prepare_pdf.py first.")

    dpi = dpi_override or (manifest.get("render", {}) or {}).get(
        "diagram_dpi", DEFAULT_DIAGRAM_DPI
    )
    tmp_dir = mdir / "pages"
    tmp_dir.mkdir(exist_ok=True)

    print(f"Rendering {len(diagrams)} diagram page(s) at {dpi} DPI -> lossless WebP ...")
    for d in diagrams:
        page, depth = d["page"], d["depth"]
        out = mdir / d["file"]
        out.parent.mkdir(parents=True, exist_ok=True)

        # pdftoppm writes <stem>-<page>.png (page not zero-padded when -f == -l).
        stem = tmp_dir / f"_diagram_p{page:04d}"
        subprocess.run(
            ["pdftoppm", DEPTH_FLAG[depth], "-png", "-r", str(dpi),
             "-f", str(page), "-l", str(page), str(prepared), str(stem)],
            check=True,
        )
        png = next(tmp_dir.glob(f"{stem.name}-*.png"), None)
        if png is None:
            sys.exit(f"pdftoppm produced no image for page {page} — is it within the PDF?")
        subprocess.run(["cwebp", "-quiet", "-lossless", str(png), "-o", str(out)], check=True)
        png.unlink()
        kb = out.stat().st_size // 1024
        print(f"  p{page:<4} {depth:<4} -> {d['file']}  ({kb} KB)")

    print(f"Rendered {len(diagrams)} diagram image(s).")
    print("These are hosted on the manual's GitHub Release at merge (see MAINTAINERS.md).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manual_dir")
    ap.add_argument("--dpi", type=int, default=None, help="override render.dpi (all-pages mode)")
    ap.add_argument(
        "--diagrams", action="store_true",
        help="render only the manifest `diagrams:` pages to lossless WebP",
    )
    ap.add_argument(
        "--diagram-dpi", type=int, default=None,
        help=f"override render.diagram_dpi (default {DEFAULT_DIAGRAM_DPI}) in --diagrams mode",
    )
    args = ap.parse_args()

    if shutil.which("pdftoppm") is None:
        sys.exit("Missing required tool on PATH: pdftoppm (install poppler-utils)")

    mdir = manual_dir(args.manual_dir)
    manifest = load_manifest(mdir)

    if args.diagrams:
        return render_diagrams(mdir, manifest, args.diagram_dpi)
    return render_all_pages(mdir, manifest, args.dpi)


if __name__ == "__main__":
    raise SystemExit(main())
