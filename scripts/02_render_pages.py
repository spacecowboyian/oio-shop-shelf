#!/usr/bin/env python3
"""02 — Render page images.

Two modes:

  # Default: render EVERY page to pages/p####.png so the AI cleanup step can
  # cross-check garbled OCR against the scan. pages/ is gitignored (regenerable).
  python scripts/02_render_pages.py <manuals/slug/> [--dpi 200]

  # --diagrams: render ONLY the pages listed in the manifest `diagrams:` block,
  # each at its declared depth, to the image at its `file:` path. The format follows
  # the extension: .png (the default for new manuals — readable by every tool and AI
  # pipeline) or .webp (kept for manuals that already ship WebP).
  # These are the diagram-only pages delivered to the user in-chat (issue #1).
  python scripts/02_render_pages.py <manuals/slug/> --diagrams [--diagram-dpi 150]

Requires: pdftoppm (poppler-utils) on PATH; ImageMagick (`magick`) for --diagrams;
cwebp (webp) only if a diagram's `file:` ends in .webp.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir  # noqa: E402

# Diagram delivery targets B/W print scans: color is dead weight. Depth is per-diagram:
#   mono = pure black-and-white (~25-50 KB). The page is rendered in grayscale, contrast-
#          stretched, then THRESHOLDED (not dithered). Thresholding drops the gray paper
#          tone, scanner shading and light watermarks entirely and keeps line art and type
#          crisp; pdftoppm's own -mono dithers that gray into speckle, which made thin
#          numbers unreadable. Right for wiring, exploded views, sequences, typed plates.
#   gray = grayscale, contrast-stretched. Only for a genuine photo/halftone that a
#          threshold would turn into blotches.
# Optional per-diagram `threshold:` (percent, default 60) tunes mono. Lower keeps more of a
# faint drawing; higher darkens thin strokes but starts pulling light watermarks back in as
# solid black — check the render.
DEFAULT_DIAGRAM_DPI = 150
DEFAULT_THRESHOLD = 60


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
    if shutil.which("magick") is None:
        sys.exit("Missing required tool on PATH: magick (install ImageMagick)")

    diagrams = manifest.get("diagrams") or []
    if not diagrams:
        print("No `diagrams:` block in manifest.yml — nothing to render.")
        return 0
    if any(str(d["file"]).endswith(".webp") for d in diagrams) and shutil.which("cwebp") is None:
        sys.exit("Missing required tool on PATH: cwebp (install the 'webp' package) — "
                 "needed because some diagram `file:` paths end in .webp")

    prepared = mdir / "prepared.pdf"
    if not prepared.is_file():
        sys.exit("prepared.pdf not found — run 01_prepare_pdf.py first.")

    dpi = dpi_override or (manifest.get("render", {}) or {}).get(
        "diagram_dpi", DEFAULT_DIAGRAM_DPI
    )
    tmp_dir = mdir / "pages"
    tmp_dir.mkdir(exist_ok=True)

    print(f"Rendering {len(diagrams)} diagram page(s) at {dpi} DPI ...")
    for d in diagrams:
        page, depth = d["page"], d["depth"]
        if depth not in ("mono", "gray"):
            sys.exit(f"Diagram p{page}: unknown depth {depth!r} (use mono or gray)")
        out = mdir / d["file"]
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.suffix.lower() not in (".png", ".webp"):
            sys.exit(f"Diagram p{page}: file must end in .png or .webp, got {d['file']!r}")

        # Always start from a fresh grayscale render of the PDF page — never from a
        # previously shipped (dithered or lossy) image.
        stem = tmp_dir / f"_diagram_p{page:04d}"
        subprocess.run(
            ["pdftoppm", "-gray", "-png", "-r", str(dpi), "-singlefile",
             "-f", str(page), "-l", str(page), str(prepared), str(stem)],
            check=True,
        )
        src = stem.with_suffix(".png")
        if not src.is_file():
            sys.exit(f"pdftoppm produced no image for page {page} — is it within the PDF?")

        if depth == "mono":
            t = int(d.get("threshold", DEFAULT_THRESHOLD))
            ops = ["-normalize", "-level", "25%,75%", "-threshold", f"{t}%", "-type", "bilevel"]
            png_out = ["-strip", "-depth", "1"]
        else:
            ops = ["-normalize"]
            png_out = ["-strip"]

        if out.suffix.lower() == ".png":
            subprocess.run(["magick", str(src), *ops, *png_out, f"PNG:{out}"], check=True)
        else:
            mid = stem.with_name(stem.name + "_proc.png")
            subprocess.run(["magick", str(src), *ops, str(mid)], check=True)
            subprocess.run(["cwebp", "-quiet", "-lossless", str(mid), "-o", str(out)], check=True)
            mid.unlink()
        src.unlink()
        kb = out.stat().st_size // 1024
        note = f" threshold {d.get('threshold', DEFAULT_THRESHOLD)}%" if depth == "mono" else ""
        print(f"  p{page:<4} {depth:<4}{note} -> {d['file']}  ({kb} KB)")
    print(f"Rendered {len(diagrams)} diagram image(s).")
    print("These are hosted on the manual's GitHub Release at merge (see MAINTAINERS.md).")
    return 0

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manual_dir")
    ap.add_argument("--dpi", type=int, default=None, help="override render.dpi (all-pages mode)")
    ap.add_argument(
        "--diagrams", action="store_true",
        help="render only the manifest `diagrams:` pages (PNG or WebP, by file extension)",
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
