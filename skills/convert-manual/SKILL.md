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

## 1b. Manual overview & scope — build it FIRST, confirm with the user

Before converting anything, write **`manuals/<slug>/README.md`** — a short overview of
what the manual is, what it covers, and what it doesn't. This gives the whole conversion
its bearings (and tells a future reader whether this manual even applies to their vehicle).

Draw on the manual's own title/contents pages (authoritative) **plus** general context from
the `auto-mechanic` skill + glossary and a quick web lookup (engine family, specs, which
vehicles it was used in, era). **Keep the two sources clearly separated** — mark the
engine/vehicle background as best-effort / review-pending; it is NOT from the manual.

Cover:
- **The engine(s)/vehicle(s):** what it is, rough specs, which cars it went in, years.
- **What the manual covers** (its section list) and **what it does NOT** (e.g. an *engine*
  manual won't have transmission/brakes/body; note if the scan is abridged/missing pages).
- **Provenance caveats** (encryption, abridged scan, any bogus stickers/annotations).

**Then STOP and have the user review/correct the overview before continuing.** The web/
background details won't be perfect; a quick confirm here prevents a wrong assumption from
coloring the whole conversion. Only proceed once the overview is right. See
`manuals/toyota-4a-fe-4a-ge-repair/README.md` for a worked example.

## 2. Decrypt + OCR (first real step)

Produce a clean, text-searchable working PDF before anything else:

```
python scripts/01_prepare_pdf.py <source.pdf> manuals/<slug>/
```

`01` handles two things automatically:
- **Encryption** — scanned OEM PDFs are often owner-password/permission-encrypted
  (copy/print disabled), which breaks OCR and text extraction. `01` detects this and
  decrypts with `qpdf --decrypt`. (A PDF that needs a password just to *open* can't be
  decrypted without it — `01` says so; decrypt it yourself with
  `qpdf --decrypt --password=… in.pdf out.pdf` and point `01` at the result.)
- **OCR** — if there's no text layer it runs ocrmypdf; if a good text layer already
  exists it skips re-OCR.

Produces `manuals/<slug>/prepared.pdf` + `raw-ocr/full-text.txt` (both gitignored).
Requires `qpdf` on PATH for encrypted input.

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

**REQUIRED — use the `auto-mechanic` skill for domain judgment.** Load the
[`auto-mechanic`](../auto-mechanic/SKILL.md) skill and its `glossary.md` while cleaning up
**and** while making index decisions. Transcription alone doesn't tell you what a term,
table, or code *means*. The glossary supplies: canonical component/abbreviation names
(ECU, TPS, VSV, ISC, DTC, MIL vs SRI…), torque-table + torque-to-yield conventions, and the
**OCR-misread patterns** (Ω→"2", l→i, h→li, rn→m, unreliable punctuation) you must screen
for before treating an odd value or term as real. This is not optional polish — it's how a
faithful transcription becomes a *usable* one.

## 5. Build the index files

```
python scripts/05_build_indexes.py manuals/<slug>/
```

**Curate index terms with the `auto-mechanic` lens.** A mechanic looks things up by
**component and symptom**, not by procedure verb: write **component-first** entries
("Water pump — installation", "Injector — resistance inspection", "Auxiliary air valve —
removal"), not verb-first ("Install Water Pump"). Use the glossary's canonical names and
surface standard aliases (e.g. also list diagnostic codes under **DTC**). Screen every
term for OCR artifacts. For multi-model manuals, split the index per model and tag each
entry (see [issue #9](https://github.com/spacecowboyian/oio-shop-shelf/issues/9)).

Generates `00-index.md`, quick-reference, `10-needs-review.md`, and the
alphabetical index. (The 4A-GE reference ships hand-curated richer indexes; new
manuals start from the generated ones.)

## 6. Bake the index into the PDF

```
python scripts/08_append_index_pages.py manuals/<slug>/ --in-place
```

Appends the chapter table + alphabetical index as searchable, clickable pages to
the end of the OCR'd PDF. Every entry jumps to the source page where the info
lives, so a standalone PDF download still has a working index. `--in-place` bakes
the index into the shipped PDF (idempotent — re-runs replace the index, never
duplicate it; the pristine manual stays recoverable via a stamped marker). Drop
`--in-place` to write a separate `<src-stem>-indexed.pdf` instead. See issue #2
for where this is headed in the pipeline.

## 7. Verify

```
python scripts/06_check_links.py manuals/<slug>/
python scripts/validate_manifests.py
python scripts/check_page_continuity.py manuals/<slug>/   # abridged-scan / missing-page detector
```

Fix broken links and manifest errors before opening the PR. `check_page_continuity.py`
warns (never fails) when a section's page numbers skip — a sign the scan is missing
pages. Record genuine gaps in `wiki/10-needs-review.md`; they're a property of the
source, not something to "fix." Add a `section_code:` (e.g. `EM`) to each manifest
chapter so the check keys off the real code instead of guessing.

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
