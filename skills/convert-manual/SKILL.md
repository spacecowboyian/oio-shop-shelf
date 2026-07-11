---
name: convert-manual
description: "Turn a service-manual PDF the contributor owns into this repo's full package using ChatGPT, Claude, Codex, or another capable assistant: an OCR'd PDF with a baked-in clickable index, per-chapter markdown, generated indexes, and pull-request guidance. Use when someone says \"convert this manual\", \"add my manual / PDF to the repo\", \"turn this service manual into markdown/wiki\", \"how do I contribute a manual\", or points at a PDF file/link and wants it processed into a manuals slug folder."
---

# Convert a manual PDF to repo package plus PR

> **Scaffolding, growing over time.** This skill is the on-ramp that turns the
> `scripts/01`–`08` pipeline into something a contributor can run end to end. It
> is intentionally partial — see the [epic](https://github.com/spacecowboyian/oio-shop-shelf/issues/4)
> for what's still being filled in. When a step here is thin, do the sensible
> thing and note it in the PR so the process can grow.

You are helping a **contributor** (not necessarily a developer) take a service
manual PDF they have and produce a `manuals/<slug>/` package that matches the
`toyota-4a-fe-4a-ge` reference. Then you help them open a pull request.

## 0. Figure out where the assistant is running

The pipeline needs system binaries, not just Python — this determines the path:

- **Local CLI agent** (Codex, Claude Code, Gemini CLI, or another assistant with a shell):
  run the full path.
  Requires on PATH: `ocrmypdf`, `tesseract`, `ghostscript`, poppler
  (`pdftotext`, `pdftoppm`, `pdffonts`), plus `pip install -r scripts/requirements.txt`
  (PyYAML, PyMuPDF). Check with `scripts/` step 01 — it fails loudly on missing tools.
- **Hosted code sandbox** (for example ChatGPT Advanced Data Analysis): try only for
  small manuals and expect file-size/runtime limits. If binary dependencies are missing,
  use the cloud fallback below.
- **No shell / plain chat** (ChatGPT web without tools, claude.ai without artifacts/code,
  Gemini chat): you **cannot** OCR or emit a PDF here. Route the contributor to the
  Colab notebook and do the parts
  chat is good at (cleanup, PR text). See `references/cloud-no-cli.md`.

Language note: the core is **Python on purpose** — it's what agents reach for, the
pipeline is already Python, and PyMuPDF/ocrmypdf/poppler are best-in-class. Don't
rewrite it in another language; the portability wall is the binaries above, not Python.

## 1. Input

Accept either a local path or a link (Drive/URL). If it's a link, download it
first to a local working file. Confirm the manual's make/engine/system so you can
pick a `slug` (e.g. `toyota-4a-fe-4a-ge`) and title.

## 2. OCR (first real step)

If the PDF has no text layer, produce an OCR'd copy — do this before anything else:

```
python scripts/01_prepare_pdf.py <source.pdf> manuals/<slug>/
```

Produces `manuals/<slug>/prepared.pdf` + `raw-ocr/full-text.txt`. If the PDF
already has a good text layer, `01` detects it and skips re-OCR. The OCR'd PDF is
the artifact everything else (including the final indexed PDF) is built on.

## 3. Author the manifest, render, and split

Help the contributor write `manuals/<slug>/manifest.yml` (copy `manuals/_template/`).
The key content is the **chapter list with 1-based inclusive source page ranges** —
read them off the manual's own table of contents.

```
python scripts/02_render_pages.py manuals/<slug>/     # page images for cross-checking
python scripts/03_split_manifest.py manuals/<slug>/   # raw per-chapter drafts
```

## 4. Cleanup (the quality step)

Reconstruct each chapter's raw draft into faithful markdown following
**`scripts/04_cleanup_methodology.md`** — these are hard rules, not suggestions.
**Rule 0 is inviolable: never silently change a number.** Flag anything uncertain
with `<!-- NEEDS REVIEW: ... -->` instead of guessing; those roll up into
`10-needs-review.md`. Cross-check ambiguous values against the rendered page image
from step 02. The rules are a *living standard* — if this manual surfaces a case
they don't cover, propose an edit to that file in your PR (see issue #3).

## 5. Build the index files

```
python scripts/05_build_indexes.py manuals/<slug>/
```

Generates `00-index.md`, quick-reference, `10-needs-review.md`, and the
alphabetical index. (The 4A-GE reference ships hand-curated richer indexes; new
manuals start from the generated ones.)

## 6. Bake the index into the PDF

```
python scripts/08_append_index_pages.py manuals/<slug>/
```

Appends the chapter table + alphabetical index as searchable, clickable pages to
the end of the OCR'd PDF (`<src-stem>-indexed.pdf`). Every entry jumps to the
source page where the info lives, so a standalone PDF download still has a working
index. See issue #2 for where this is headed in the pipeline.

## 7. Verify

```
python scripts/06_check_links.py manuals/<slug>/
python scripts/validate_manifests.py
```

Fix broken links and manifest errors before opening the PR.

## 8. Open the pull request

Walk the contributor through it even if they've never made one — fork, branch,
commit, push, PR, and what a good description says. Full step-by-step (with
copy-paste commands and the first-timer path) is in
**`references/pull-request-walkthrough.md`**. Read it and adapt to their setup.

## What a finished package looks like

Mirror `manuals/toyota-4a-fe-4a-ge/`: `manifest.yml`, the OCR'd + indexed PDF,
`wiki/` with per-chapter `.md`, `00-index.md`, `09-*`, `10-needs-review.md`,
`11a..d-alphabetical-index.md`, and `llm-instructions.md`. Don't commit raw OCR
intermediates (`.gitignore` already excludes `raw-ocr/`, `pages/`, `prepared.pdf`).
