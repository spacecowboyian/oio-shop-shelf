#!/usr/bin/env python3
"""01 — Prepare a source PDF: decrypt it if needed, then OCR if it has no text layer.

Usage:
    python scripts/01_prepare_pdf.py <source.pdf> <manuals/slug/>

Produces <manuals/slug/>/prepared.pdf (text-layer PDF) and
<manuals/slug/>/raw-ocr/full-text.txt (extracted text). Source PDFs are never
committed (see .gitignore); this script reads from wherever you point it.

Encrypted PDFs (common for scanned OEM manuals — often owner-password/permission
encryption that blocks copy/print) are detected and decrypted with `qpdf --decrypt`
before anything else, since ocrmypdf and text extraction fail on encrypted input.
A PDF locked with a real *user* password (needed just to open it) can't be decrypted
without that password and is reported as such.

Requires: pdffonts, pdftotext, pdfinfo (poppler-utils) on PATH; qpdf if the source
is encrypted; ocrmypdf if it has no text layer.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir  # noqa: E402


def has_text_layer(pdf: Path) -> bool:
    """True if the PDF has a *usable* text layer.

    A font being listed is not enough: some scans carry a stray non-content font
    (a bookmark/annotation layer) that lists in pdffonts but yields no page text,
    which would fool us into skipping OCR and producing an empty extraction. So we
    also require pdftotext to actually pull a meaningful amount of text out.
    """
    fonts = subprocess.run(
        ["pdffonts", str(pdf)], capture_output=True, text=True, check=True
    ).stdout.splitlines()
    if len(fonts) <= 2:  # header + separator only == no fonts at all
        return False
    # Confirm real extractable text: sample the doc and require a floor of characters
    # per page (a genuine text layer clears this easily; an empty scan does not).
    text = subprocess.run(
        ["pdftotext", "-l", "20", str(pdf), "-"], capture_output=True, text=True
    ).stdout
    n_pages = min(20, page_count(pdf) or 20)
    return len(text.strip()) >= 100 * max(1, n_pages)


def page_count(pdf: Path) -> int:
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("Pages:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                return 0
    return 0


def normalize_page_boxes(pdf: Path, dst: Path | None = None) -> int:
    """Frame each *full-page scan* to its image so renders aren't clipped or distorted.

    Manuals come in every page size and shape, and some scanned PDFs ship page boxes that
    don't match the scanned image on the page: a CropBox *smaller* than the image clips
    content (pages look cut off), while a MediaBox much *larger* than the image leaves big
    blank margins and makes pdftoppm (page render + diagram delivery + the baked-index PDF)
    produce a distorted, oversized page. Both were seen on the Renault M.R.93 scan (CropBox
    595×762 but the image runs to ~595×848, inside a 595×1224 MediaBox).

    Fix, applied per page and adaptive to any dimensions: when a page is **dominated by a
    single full-page scanned image**, set both MediaBox and CropBox to that image's bounding
    box so every renderer frames exactly the scan. A page is treated as a full-page scan
    only when its image spans ≥90% of the page width and ≥50% of its height — so
    born-digital / text-layout pages and sparse pages (a small logo, a divider) are left
    exactly as authored, never cropped to a figure. No-op for well-formed PDFs.

    Runs on the source BEFORE OCR: ocrmypdf --force-ocr rasterizes each page at its page
    box, so a box whose aspect doesn't match the scan bakes a stretched image into the OCR'd
    PDF — fixing the box afterwards can't undo it. With ``dst`` given, writes the corrected
    PDF there (leaving the source untouched) and returns the change count; the caller then
    OCRs ``dst``. With ``dst`` None, rewrites ``pdf`` in place.

    Returns the number of pages reframed (0 == nothing needed it; caller keeps using the src).
    """
    try:
        import fitz  # PyMuPDF (already a pipeline dependency)
    except ImportError:
        print("  (skipping page-box normalization — PyMuPDF not installed)")
        return 0
    MARGIN = 2.0  # pt of slack so we never shave a content edge
    doc = fitz.open(str(pdf))
    changed = 0
    for page in doc:
        if page.rotation:
            continue  # rotation complicates bbox↔box mapping; leave rotated pages alone
        mbox = page.mediabox
        if mbox.width <= 0 or mbox.height <= 0:
            continue
        # Largest image that plausibly IS the page (a full-page scan), if any.
        # get_image_bbox returns fitz coordinates (origin TOP-left, y grows down).
        best = None
        for img in page.get_images(full=True):
            try:
                bb = page.get_image_bbox(img) & mbox
            except Exception:
                continue
            if not bb.is_valid or bb.width <= 1 or bb.height <= 1:
                continue
            if bb.width >= 0.9 * mbox.width and bb.height >= 0.5 * mbox.height:
                if best is None or abs(bb.get_area()) > abs(best.get_area()):
                    best = bb
        if best is None:
            continue  # not a full-page scan — respect the authored layout
        target = fitz.Rect(best.x0 - MARGIN, best.y0 - MARGIN,
                           best.x1 + MARGIN, best.y1 + MARGIN) & mbox
        cur = page.cropbox
        if not (abs(cur.width - target.width) > 1 or abs(cur.height - target.height) > 1
                or abs(cur.x0 - target.x0) > 1 or abs(cur.y0 - target.y0) > 1):
            continue  # already framed to the scan
        # set_mediabox wants PDF coordinates (origin BOTTOM-left, y grows up), so flip the
        # fitz-space target's y-axis about the page height. Passing fitz coords directly
        # silently grabs the wrong vertical band and clips the page (top content lost).
        H = mbox.height
        pdf_box = fitz.Rect(target.x0, H - target.y1, target.x1, H - target.y0)
        page.set_mediabox(pdf_box)  # also resets cropbox to match
        changed += 1
    if changed:
        if dst is not None:
            doc.save(str(dst), garbage=3, deflate=True)
            doc.close()
        else:
            # Can't full-save over the still-open source path; write a sibling and replace.
            tmp = pdf.with_suffix(".normbox.pdf")
            doc.save(str(tmp), garbage=3, deflate=True)
            doc.close()
            tmp.replace(pdf)
    else:
        doc.close()
    return changed


def require_tools(*tools: str) -> None:
    missing = [t for t in tools if shutil.which(t) is None]
    if missing:
        sys.exit(f"Missing required tool(s) on PATH: {', '.join(missing)}")


def is_encrypted(pdf: Path) -> bool:
    """True if pdfinfo reports any encryption (owner- or user-password)."""
    out = subprocess.run(
        ["pdfinfo", str(pdf)], capture_output=True, text=True
    ).stdout
    for line in out.splitlines():
        if line.startswith("Encrypted:"):
            return not line.split(":", 1)[1].strip().lower().startswith("no")
    return False


def decrypt_pdf(src: Path, dest: Path) -> Path:
    """Strip encryption with qpdf. Works for owner-password/permission encryption
    and for an empty user password; a real user password makes this fail loudly."""
    require_tools("qpdf")
    proc = subprocess.run(
        ["qpdf", "--decrypt", str(src), str(dest)], capture_output=True, text=True
    )
    # qpdf exit codes: 0 = ok, 3 = warnings but file written; both usable.
    if proc.returncode not in (0, 3) or not dest.is_file():
        sys.exit(
            "Could not decrypt the PDF with qpdf. If it needs a password to open, "
            "decrypt it yourself first:\n"
            f"    qpdf --decrypt --password=YOURPASS '{src}' '{dest}'\n"
            f"qpdf said:\n{proc.stderr.strip()}"
        )
    return dest


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source_pdf", type=Path)
    ap.add_argument("manual_dir")
    ap.add_argument("--force", action="store_true", help="OCR even if a text layer exists")
    ap.add_argument("--language", help="tesseract language code(s), e.g. 'eng' or 'eng+deu'. "
                                       "Overrides the manifest; use it when running before the "
                                       "manifest exists and the manual isn't English.")
    args = ap.parse_args()

    require_tools("pdffonts", "pdftotext", "pdfinfo")
    # 01 can run before the manifest is authored — you often want the OCR'd text
    # first so you can read the manual's own table of contents while writing the
    # chapter page ranges. So the manifest is optional here (defaults: eng, no force).
    mdir = manual_dir(args.manual_dir, require_manifest=False)
    manifest = load_manifest(mdir, required=False)
    if not manifest:
        print("No manifest.yml yet — using defaults (lang=eng, no force). "
              "Author the manifest next; 01 only needs the source PDF + this directory.")
    if not args.source_pdf.is_file():
        sys.exit(f"Source PDF not found: {args.source_pdf}")

    ocr_cfg = manifest.get("ocr", {}) or {}
    force = args.force or bool(ocr_cfg.get("force"))
    lang = args.language or ocr_cfg.get("language") or "eng"

    prepared = mdir / "prepared.pdf"
    raw_dir = mdir / "raw-ocr"
    raw_dir.mkdir(exist_ok=True)

    # 0) Decrypt first — ocrmypdf and pdftotext both fail on encrypted input.
    source = args.source_pdf
    if is_encrypted(source):
        print("Encrypted PDF detected — decrypting with qpdf...")
        source = decrypt_pdf(source, raw_dir / "decrypted.pdf")

    # 0b) Reframe full-page scans to the image BEFORE OCR. ocrmypdf --force-ocr rasterizes
    # each page at its page box, so a box whose aspect doesn't match the scan bakes a
    # stretched image into the OCR'd PDF that no later fix can undo. No-op for well-formed
    # PDFs and for born-digital/text pages (see normalize_page_boxes).
    normalized = raw_dir / "normalized.pdf"
    fixed = normalize_page_boxes(source, normalized)
    if fixed:
        print(f"Reframed {fixed} full-page-scan page(s) to the scanned image (before OCR) "
              "to prevent clipped/stretched renders.")
        source = normalized

    if has_text_layer(source) and not force:
        print("Text layer detected — copying source to prepared.pdf (no OCR).")
        shutil.copyfile(source, prepared)
    else:
        require_tools("ocrmypdf")
        reason = "forced" if force else "no text layer detected"
        print(f"Running OCR ({reason}, lang={lang}) — this can take a while...")
        subprocess.run(
            ["ocrmypdf", "--rotate-pages", "--deskew", "--language", lang,
             ("--force-ocr" if force else "--skip-text"),
             str(source), str(prepared)],
            check=True,
        )

    text_out = raw_dir / "full-text.txt"
    subprocess.run(["pdftotext", "-layout", str(prepared), str(text_out)], check=True)
    n = sum(1 for _ in text_out.open(encoding="utf-8", errors="replace"))
    print(f"Wrote {prepared} and {text_out} ({n} lines).")
    print("Next: python scripts/02_render_pages.py", args.manual_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
