# Contributing to oio-shop-shelf

Thanks for helping turn unreadable scanned manuals into clean, structured wikis.

## ⚠️ Read this first: source-manual copyright

OEM service manuals are almost always copyrighted by the manufacturer or publisher.

- **Do NOT commit source PDFs into this repo.** `.gitignore` blocks `*.pdf` by default.
- Your `manifest.yml` should point (`source:`) to wherever *you* host the source — your
  own Google Drive, a private URL, etc. The repo only ships the derived transcription.
- **Whether the derived markdown transcription itself may be published** under a given
  manual's copyright is an unresolved question and varies by manual and jurisdiction. If
  you are not sure you have the right to publish a transcription of a particular manual,
  **do not open a PR adding it.** When in doubt, ask in an issue first.

This posture is deliberately conservative and will be revisited before any public launch.

## The pipeline, end to end

Prerequisites: Python 3.10+, and the CLI tools `ocrmypdf`, `pdftoppm`, `pdftotext`,
`pdffonts` (from `poppler-utils`). Install Python deps with
`pip install -r scripts/requirements.txt`.

1. **Fork and add a manual folder.**
   Copy `manuals/_template/` to `manuals/<your-manual-slug>/` and fill in `manifest.yml`:
   title, a `source:` pointer to your hosted PDF, a license/rights note, and the
   `chapters:` map of page ranges → output filenames.

2. **Prepare the PDF** (adds a text layer if the scan lacks one):
   ```bash
   python scripts/01_prepare_pdf.py path/to/source.pdf manuals/<slug>/
   ```

3. **Render page images** (the AI cleanup step cross-checks garbled OCR against these):
   ```bash
   python scripts/02_render_pages.py manuals/<slug>/ --dpi 200
   ```

4. **Split into per-chapter raw drafts** per your manifest:
   ```bash
   python scripts/03_split_manifest.py manuals/<slug>/
   ```

5. **AI cleanup — the expensive, human-supervised step.**
   For each chapter draft, run a capable AI agent against
   [`scripts/04_cleanup_methodology.md`](scripts/04_cleanup_methodology.md) + the raw
   draft + the rendered page images, producing the clean `wiki/<chapter>.md`. Use
   whatever agent you like — Claude Code, plain Claude, ChatGPT. The methodology doc is
   the contract; follow it exactly, especially the **never touch numeric values** rule.

6. **Build the index files** from the cleaned chapters:
   ```bash
   python scripts/05_build_indexes.py manuals/<slug>/
   ```

7. **Check links locally** and fix anything flagged:
   ```bash
   python scripts/06_check_links.py manuals/<slug>/
   ```

8. **Open a PR.** CI re-runs the link checker and manifest schema validation on every PR.

## Style rules for the wiki output

These mirror `04_cleanup_methodology.md` — the short version:

- **Tables over ASCII art.** Reconstruct image-based charts as real markdown tables.
- **Lists for procedures.** Numbered steps become ordered lists.
- **Step-tables for flowcharts.** Diagnostic trees become tables (condition → action → next).
- **Never change a number.** Flag ambiguous OCR with
  `<!-- NEEDS REVIEW: reason -->` inline; never guess.
- **Link, don't duplicate.** Cross-reference other chapters/anchors with relative links.

## Questions

Open an issue. Copyright/licensing questions especially — ask before adding a new manual.
