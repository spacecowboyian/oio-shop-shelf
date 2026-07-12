#!/usr/bin/env python3
"""08 — Append clickable index pages to the source OCR PDF.

Reads the curated markdown index files (00-index.md chapter table + the
11a..11d alphabetical index) and renders them as fresh, text-searchable PDF
pages appended to the END of the source manual. Every entry becomes an internal
hyperlink that jumps to the physical page in the same PDF where the info lives —
so a user who downloads only the PDF still has a working back-of-book index.

Because the index pages are appended after the manual, source PDF page N is the
same as combined-PDF page N; an entry citing "[PDF p.N]" links straight to page N.

Usage:
    python scripts/08_append_index_pages.py <manuals/slug/> [--in-place | --output PATH]

By default the source PDF (manifest source.location) is left untouched and the
result is written to <source-stem>-indexed.pdf. Pass --in-place to bake the index
into the shipped PDF itself (so downloading it from the repo gives the indexed
manual). --in-place is idempotent: a stamped page-count marker lets a re-run find
and replace the previously appended index instead of duplicating it, and the
pristine (pre-index) manual is always recoverable from that marker.

Depends on PyMuPDF (see scripts/requirements.txt).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: PyMuPDF. Run: pip install -r scripts/requirements.txt")

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir, wiki_dir  # noqa: E402

# --- markdown parsing ---------------------------------------------------------

PDF_PAGE_RE = re.compile(r"\[PDF p\.(\d+)\]")
# alphabetical-index entry:  "- <term> — [chapter.md#pX](...) ([PDF p.N](...))"
ENTRY_RE = re.compile(r"^-\s+(?P<term>.*?)\s+—\s+.*?\[PDF p\.(?P<page>\d+)\]")
LETTER_RE = re.compile(r"^##\s+(?P<letter>.+?)\s*$")
# 00-index chapter table row:  "| CODE | Chapter Name | [file.md](...) | [1](...#page=1)-... |"
PAGE_ANCHOR_RE = re.compile(r"#page=(\d+)")


RANGE_RE = re.compile(r"\[?(\d{1,4})\s*[-–—]\s*\d")  # "2-9", "170–188", "[1](...)-[14]"
BARE_PAGE_RE = re.compile(r"^\s*\[?(\d{1,4})\]?\s*$")  # a lone page number in a cell


def parse_chapters(index_md: Path) -> list[tuple[str, int]]:
    """(chapter title, start page) rows from the 00-index.md chapter table.

    Tolerant of format: finds the start page from a `#page=N` link, a `[PDF p.N]`
    marker, or a plain "N-M" / "N" page cell — so it works whether the table uses
    Drive links (manual 1) or plain page ranges (later manuals), and regardless of
    how many columns the table has."""
    rows: list[tuple[str, int]] = []
    for line in index_md.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        title = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cells[1]).strip("* ")
        if title in ("Chapter", "File", "Title", "---", "") or set(title) <= {"-"}:
            continue
        # start page: prefer explicit anchors anywhere in the row, else a range/bare
        # number in a cell after the title (skip the title/file cells' own digits)
        start = None
        m = PAGE_ANCHOR_RE.search(line) or re.search(r"\[PDF p\.(\d+)\]", line)
        if m:
            start = int(m.group(1))
        else:
            for c in cells[2:]:
                rm = RANGE_RE.match(c) or BARE_PAGE_RE.match(c)
                if rm:
                    start = int(rm.group(1))
                    break
        if start is None:  # reference rows (index/torque) with "—" and no page
            continue
        rows.append((title, start))
    return rows


MODEL_MARKER_RE = re.compile(r"<!--\s*index-model:\s*(.+?)\s*-->")


def parse_alpha(files: list[Path]) -> list[tuple[str | None, list[tuple[str, str, list[int]]]]]:
    """Parse the 11*-alphabetical-index files into ordered per-model groups.

    A file may declare `<!-- index-model: 4A-FE -->` at the top; files sharing a
    model marker merge into one group and render as a titled index section ("…
    Alphabetical Index (4A-FE)"). Files with no marker merge into a single default
    group (model=None) that renders as the plain "Alphabetical Index" — so a manual
    whose index is only split by letter range (like manual 1) is unaffected. An entry
    that applies to several models is expected to appear in each of those model files.

    Entries with the SAME display term are collapsed into one (letter, term, [pages])
    with all their pages sorted+deduped — a real back-of-book index lists one term once
    with its several page numbers, not the term repeated per page."""
    order: list[str | None] = []
    # model -> ordered dict: term -> [letter, {pages}]
    by_model: dict[str | None, dict[str, list]] = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        mm = MODEL_MARKER_RE.search(text)
        model = mm.group(1).strip() if mm else None
        if model not in by_model:
            by_model[model] = {}
            order.append(model)
        terms = by_model[model]
        letter = "#"
        for line in text.splitlines():
            lm = LETTER_RE.match(line)
            if lm:
                letter = lm.group("letter")
                continue
            em = ENTRY_RE.match(line)
            if em:
                term = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", em.group("term")).strip()
                page = int(em.group("page"))
                if term not in terms:
                    terms[term] = [letter, set()]
                terms[term][1].add(page)
    out = []
    for m in order:
        rows = [(letter, term, sorted(pages)) for term, (letter, pages) in by_model[m].items()]
        out.append((m, rows))
    return out


# --- PDF rendering ------------------------------------------------------------

MARGIN = 54.0
GUTTER = 20.0
LINK_COLOR = (0.05, 0.30, 0.72)
HEAD_COLOR = (0.15, 0.15, 0.15)
RULE_COLOR = (0.75, 0.75, 0.75)
ENTRY_SIZE = 8.0
LINE_GAP = 3.0
FONT_REG, FONT_BOLD = "helv", "hebo"
_REG = fitz.Font("helv")
_BOLD = fitz.Font("hebo")


def _wrap(font: fitz.Font, text: str, size: float, width: float) -> list[str]:
    """Greedy word-wrap; hard-breaks any single word wider than the column."""
    out: list[str] = []
    for word in text.split():
        if not out:
            out.append(word)
            continue
        trial = out[-1] + " " + word
        if font.text_length(trial, size) <= width:
            out[-1] = trial
        else:
            out.append(word)
    # hard-break over-long tokens
    fixed: list[str] = []
    for line in out:
        while font.text_length(line, size) > width and len(line) > 1:
            cut = len(line)
            while cut > 1 and font.text_length(line[:cut], size) > width:
                cut -= 1
            fixed.append(line[:cut])
            line = line[cut:]
        fixed.append(line)
    return fixed


class Layout:
    """Two-column, top-to-bottom page renderer that appends onto `doc`."""

    def __init__(self, doc: fitz.Document, w: float, h: float, header: str):
        self.doc, self.w, self.h, self.header = doc, w, h, header
        self.col_w = (w - 2 * MARGIN - GUTTER) / 2
        self.col_x = [MARGIN, MARGIN + self.col_w + GUTTER]
        self.top = MARGIN + 24
        self.bottom = h - MARGIN
        self.page = None
        self.col = 0
        self.y = self.bottom + 1  # force a new page on first write
        self.first_page_no = None  # 1-based page number of the first appended page

    def _new_page(self):
        self.page = self.doc.new_page(width=self.w, height=self.h)
        if self.first_page_no is None:
            self.first_page_no = self.doc.page_count  # 1-based
        # running header + rule
        self.page.insert_text(
            fitz.Point(MARGIN, MARGIN - 6), self.header,
            fontname=FONT_REG, fontsize=8, color=HEAD_COLOR,
        )
        self.page.draw_line(
            fitz.Point(MARGIN, MARGIN + 2), fitz.Point(self.w - MARGIN, MARGIN + 2),
            color=RULE_COLOR, width=0.5,
        )
        self.col = 0
        self.y = self.top

    def _advance(self, height: float):
        """Ensure `height` fits in the current column; move column/page if not."""
        if self.page is None or self.y + height > self.bottom:
            if self.page is None or self.col == 1:
                self._new_page()
            else:
                self.col = 1
                self.y = self.top

    def letter(self, text: str):
        self._advance(20)
        # keep a heading with at least one following line
        if self.y + 26 > self.bottom:
            self._advance(20)
        x = self.col_x[self.col]
        self.y += 12
        self.page.insert_text(fitz.Point(x, self.y), text, fontname=FONT_BOLD,
                              fontsize=11, color=HEAD_COLOR)
        self.page.draw_line(fitz.Point(x, self.y + 3),
                            fitz.Point(x + self.col_w, self.y + 3),
                            color=RULE_COLOR, width=0.4)
        self.y += 8

    def entry(self, term: str, pages: list[int]):
        """One index line: the term in black (NOT a link), then its page number(s) in
        blue, right-aligned and comma-separated — and ONLY the page numbers are clickable."""
        pstr = ", ".join(str(p) for p in pages)
        pnum_w = _REG.text_length(pstr, ENTRY_SIZE) + 8
        lines = _wrap(_REG, term, ENTRY_SIZE, self.col_w - pnum_w)
        block_h = len(lines) * (ENTRY_SIZE + LINE_GAP)
        self._advance(block_h)
        x = self.col_x[self.col]
        y0 = self.y
        for line in lines:                        # term text — plain black, no link
            self.y += ENTRY_SIZE
            self.page.insert_text(fitz.Point(x, self.y), line,
                                  fontname=FONT_REG, fontsize=ENTRY_SIZE)
            self.y += LINE_GAP
        # page numbers on the last line's baseline, right-aligned; link ONLY each number
        py = y0 + len(lines) * (ENTRY_SIZE + LINE_GAP) - LINE_GAP
        cursor = x + self.col_w - _REG.text_length(pstr, ENTRY_SIZE)
        for i, p in enumerate(pages):
            s = str(p)
            w = _REG.text_length(s, ENTRY_SIZE)
            self.page.insert_text(fitz.Point(cursor, py), s,
                                  fontname=FONT_REG, fontsize=ENTRY_SIZE, color=LINK_COLOR)
            self.page.insert_link({
                "kind": fitz.LINK_GOTO,
                "from": fitz.Rect(cursor - 1, py - ENTRY_SIZE, cursor + w + 1, py + 2),
                "page": p - 1,                   # 0-based; source page N == combined page N
                "to": fitz.Point(0, 0),
            })
            cursor += w
            if i < len(pages) - 1:               # ", " separator in black (not linked)
                sep = ", "
                self.page.insert_text(fitz.Point(cursor, py), sep,
                                      fontname=FONT_REG, fontsize=ENTRY_SIZE)
                cursor += _REG.text_length(sep, ENTRY_SIZE)


def build(doc: fitz.Document, chapters, alpha, title: str) -> list[tuple[int, str, int]]:
    """Append index pages to `doc`; return TOC rows (level, label, 1-based page)."""
    w = doc[0].rect.width
    h = doc[0].rect.height
    toc: list[tuple[int, str, int]] = []

    # --- Chapter contents page ---
    cp = doc.new_page(width=w, height=h)
    contents_page_no = doc.page_count
    toc.append((1, "Index — Chapter Contents", contents_page_no))
    y = MARGIN + 18
    cp.insert_text(fitz.Point(MARGIN, y), "Index — Chapter Contents",
                   fontname=FONT_BOLD, fontsize=16, color=HEAD_COLOR)
    y += 12
    cp.insert_text(fitz.Point(MARGIN, y),
                   "Click a page number to jump to it. Alphabetical index follows.",
                   fontname=FONT_REG, fontsize=9, color=HEAD_COLOR)
    y += 8
    cp.draw_line(fitz.Point(MARGIN, y), fitz.Point(w - MARGIN, y),
                 color=RULE_COLOR, width=0.5)
    y += 22
    for name, start in chapters:
        pnum = str(start)
        pw = _REG.text_length(pnum, 10)
        px = w - MARGIN - pw
        cp.insert_text(fitz.Point(MARGIN, y), name, fontname=FONT_REG, fontsize=10)  # plain
        cp.insert_text(fitz.Point(px, y), pnum, fontname=FONT_REG,
                       fontsize=10, color=LINK_COLOR)
        cp.insert_link({"kind": fitz.LINK_GOTO,                 # link ONLY the page number
                        "from": fitz.Rect(px - 1, y - 10, px + pw + 1, y + 3),
                        "page": start - 1, "to": fitz.Point(0, 0)})
        y += 20

    # --- Alphabetical index (one titled section per model group) ---
    for model, entries in alpha:
        if not entries:
            continue
        suffix = f" ({model})" if model else ""
        lay = Layout(doc, w, h, f"{title} — Alphabetical Index{suffix}")
        current_letter = None
        for letter, term, pages in entries:
            if letter != current_letter:
                lay.letter(letter)
                current_letter = letter
            lay.entry(term, pages)
        if lay.first_page_no:
            toc.append((1, f"Index — Alphabetical{suffix}", lay.first_page_no))
    return toc


MARKER_RE = re.compile(r"oio-index-base:(\d+)")


def strip_prior_index(doc: fitz.Document) -> None:
    """If this PDF already has appended index pages (from a previous run), remove
    them so the operation is idempotent — re-running never double-appends."""
    kw = (doc.metadata or {}).get("keywords") or ""
    m = MARKER_RE.search(kw)
    if not m:
        return
    base = int(m.group(1))
    if 0 < base < doc.page_count:
        doc.delete_pages(from_page=base, to_page=doc.page_count - 1)
    # drop outline entries that pointed into the removed pages. After delete_pages,
    # entries targeting a removed page come back as page -1, so require a valid page
    # (1..base) — otherwise stale index entries accumulate across re-bakes.
    kept = [t for t in doc.get_toc() if 0 < t[2] <= base]
    doc.set_toc(_sanitize_toc(kept))


def _sanitize_toc(toc: list) -> list:
    """Make an outline valid for set_toc: first row level 1, levels never jump by >1.
    Filtering entries out (above) can orphan a nested child, which PyMuPDF rejects."""
    out, prev = [], 0
    for lvl, title, page in toc:
        lvl = max(1, min(int(lvl), prev + 1))
        out.append([lvl, title, page])
        prev = lvl
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manual_dir")
    ap.add_argument("--output", help="output PDF path (default: <src-stem>-indexed.pdf)")
    ap.add_argument("--in-place", action="store_true",
                    help="write the index back into the source PDF (idempotent: "
                         "existing index pages are replaced, not duplicated)")
    ap.add_argument("--force", action="store_true",
                    help="allow overwriting the source PDF in place")
    args = ap.parse_args()

    mdir = manual_dir(args.manual_dir)
    manifest = load_manifest(mdir)
    wdir = wiki_dir(mdir)

    # The committed, shipped PDF is manifest.source.location. But 01_prepare_pdf.py
    # writes the OCR'd, text-searchable copy to prepared.pdf (gitignored) and does NOT
    # overwrite source.location — so baking onto source.location alone would index the
    # non-searchable raw scan (#12). Bake onto the OCR'd copy when it exists; --in-place
    # then ships the result to source.location so the committed PDF is OCR'd + indexed.
    ship = mdir / manifest["source"]["location"]
    prepared = mdir / "prepared.pdf"
    src = prepared if prepared.is_file() else ship
    if not src.is_file():
        sys.exit(f"Source PDF not found: {src} — run 01_prepare_pdf.py first.")

    index_md = wdir / "00-index.md"
    if not index_md.is_file():
        sys.exit(f"Missing {index_md} — run 05_build_indexes.py first.")
    alpha_files = sorted(wdir.glob("11?-alphabetical-index.md"))

    chapters = parse_chapters(index_md)
    alpha = parse_alpha(alpha_files)
    if not chapters and not alpha:
        sys.exit("No index entries parsed — check 00-index.md / 11*-alphabetical-index.md.")

    # --in-place ships to the committed source.location (making it OCR'd + indexed),
    # reading content from `src` (the OCR'd prepared.pdf when present).
    if args.in_place:
        out = ship.resolve()
    else:
        out = Path(args.output).resolve() if args.output \
            else ship.with_name(ship.stem + "-indexed.pdf")
    in_place = out == src.resolve()
    if out == ship.resolve() and src.resolve() != ship.resolve() \
            and not (args.in_place or args.force):
        sys.exit(f"Refusing to overwrite committed {ship}. Use --in-place, --output, or --force.")
    if in_place and not (args.in_place or args.force):
        sys.exit(f"Refusing to overwrite source {src}. Use --in-place, --output, or --force.")

    doc = fitz.open(src)
    strip_prior_index(doc)                     # idempotent: clear any prior appended index
    n_source = doc.page_count
    bad = [p for _, entries in alpha for _, _, pages in entries for p in pages
           if p < 1 or p > n_source] + \
          [p for _, p in chapters if p < 1 or p > n_source]
    if bad:
        sys.exit(f"{len(bad)} entry page(s) out of range 1..{n_source}, e.g. {bad[:5]}")

    toc = build(doc, chapters, alpha, manifest["title"])
    doc.set_toc(doc.get_toc() + toc)

    # stamp the true (pre-index) page count so a future run can find & replace our pages
    md = doc.metadata or {}
    kw = MARKER_RE.sub("", md.get("keywords") or "").strip()
    md["keywords"] = f"{kw} oio-index-base:{n_source}".strip()
    doc.set_metadata(md)

    out.parent.mkdir(parents=True, exist_ok=True)
    # saving in place requires incremental=False + a temp; PyMuPDF disallows plain
    # same-file save, so write to a sibling temp and replace.
    if in_place:
        tmp = out.with_name(out.name + ".tmp")
        doc.save(str(tmp), deflate=True, garbage=3)
        doc.close()
        tmp.replace(out)
    else:
        doc.save(str(out), deflate=True, garbage=3)
        doc.close()

    final = fitz.open(str(out))
    added = final.page_count - n_source
    final.close()
    n_alpha = sum(len(e) for _, e in alpha)
    groups = ", ".join(f"{m or 'general'}:{len(e)}" for m, e in alpha if e)
    print(f"Appended {added} index page(s): "
          f"{len(chapters)} chapters + {n_alpha} alphabetical entries ({groups}).")
    where = "into the source PDF (in place)" if in_place else "to a new file; source untouched"
    print(f"Wrote {out} ({out.stat().st_size // 1024} KB) — {where}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
