---
name: convert-manual
description: Turn a service-manual PDF the contributor owns into this repo's full package — an OCR'd PDF with a baked-in clickable index, per-chapter markdown, and the index files — then walk them through opening a pull request. Use when someone says "convert this manual", "add my manual / PDF to the repo", "turn this service manual into markdown/wiki", "how do I contribute a manual", or points at a PDF file/link and wants it processed into `manuals/<slug>/`.
---

# Convert a manual PDF → repo package (+ PR)

> **Scaffolding, growing over time.** This skill is the on-ramp that turns the
> `scripts/01`–`08` pipeline into something a contributor can run end to end. It
> is intentionally partial — see the [epic](https://github.com/spacecowboyian/oio-shop-shelf/issues/4)
> for what's still being filled in. When a step here is thin, do the sensible
> thing and note it in the PR so the process can grow.

You are helping a **contributor** (not necessarily a developer) take a service
manual PDF they have and produce a `manuals/<slug>/` package that matches the
`toyota-4a-fe-4a-ge` reference. Then you help them open a pull request.

## 0 — Figure out where you're running

The pipeline needs system binaries, not just Python — this determines the path:

- **Local CLI agent** (Claude Code / Codex / Gemini CLI with a shell): full path.
  Requires on PATH: `ocrmypdf`, `tesseract`, `ghostscript`, poppler
  (`pdftotext`, `pdftoppm`, `pdffonts`), plus `pip install -r scripts/requirements.txt`
  (PyYAML, PyMuPDF). Check with `scripts/` step 01 — it fails loudly on missing tools.
- **No shell / plain chat** (claude.ai, Gemini, ChatGPT web): you **cannot** OCR or
  emit a PDF here. Route the contributor to the Colab notebook and do the parts
  chat is good at (cleanup, PR text). See `references/cloud-no-cli.md`.

Language note: the core is **Python on purpose** — it's what agents reach for, the
pipeline is already Python, and PyMuPDF/ocrmypdf/poppler are best-in-class. Don't
rewrite it in another language; the portability wall is the binaries above, not Python.

## 1 — Input

Accept either a local path or a link (Drive/URL). If it's a link, download it
first to a local working file. Confirm the manual's make/engine/system so you can
pick a `slug` (e.g. `toyota-4a-fe-4a-ge`) and title.

## 1a — Place it in the automotive taxonomy

Manuals live at **`manuals/<make>/<vehicle|engine>/<unit>/`** (see
[`manuals/taxonomy.md`](../../../manuals/taxonomy.md)). Decide **category** (engine-family
manual → `engine`; whole-vehicle/chassis manual → `vehicle`) and the **make/model/engine
keys** — which must exist in **`manuals/taxonomy.yml`** (controlled vocab, vPIC-anchored).
If a key isn't there, **add it to `taxonomy.yml` first** (canonical make name + `Make_ID`
via the vPIC API — steps in `taxonomy.md`); CI blocks unregistered entries. Then copy
`_template/` to that path. Below, `manuals/<slug>/` is shorthand for it; `slug` stays the
unique id, `<unit>` is a short folder name.

## 1b — Manual overview & scope — build it FIRST, confirm with the user

Before converting anything, write **`manuals/<slug>/README.md`** — a short overview of
what the manual is, what it covers, and what it doesn't. This gives the whole conversion
its bearings (and tells a future reader whether this manual even applies to their vehicle).

Draw on the manual's own title/contents pages (authoritative) **plus** general context from
the `auto-mechanic` skill + glossary and a quick web lookup (engine family, specs, which
vehicles it was used in, era). **Keep the two sources clearly separated** — mark the
engine/vehicle background as best-effort / review-pending; it is NOT from the manual.

Cover: the engine(s)/vehicle(s) (what it is, rough specs, which cars, years); **what the
manual covers** (its section list) and **what it does NOT** (an *engine* manual won't have
transmission/brakes/body; note if the scan is abridged); and **provenance caveats**
(encryption, abridged scan, bogus stickers/annotations).

**Then STOP and have the user review/correct the overview before continuing** — the web/
background won't be perfect, and a quick confirm prevents a wrong assumption from coloring
the whole conversion. See `manuals/toyota-4a-fe-4a-ge-repair/README.md` for a worked example.

## 2 — Decrypt + OCR (first real step)

Produce a clean, text-searchable working PDF before anything else:

```
mkdir -p manuals/<slug>/                               # the dir just needs to exist
python scripts/01_prepare_pdf.py <source.pdf> manuals/<slug>/
```

`01` runs **before the manifest exists on purpose** — it only needs the source PDF and
the `manuals/<slug>/` directory. That's the right order: OCR first, then read the manual's
own table of contents *out of* `raw-ocr/full-text.txt` when you write the chapter page
ranges in step 3. For a non-English manual, pass `--language` (e.g. `--language eng+deu`)
since there's no manifest yet to read it from.

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

**Known source-PDF gotchas** (auto-handled by `01`, seen on the Renault M.R.93 scan — verify after):
- **Near-empty `full-text.txt`** → a stray annotation font fooled the text-layer check into
  skipping OCR. `01` now also requires real extracted text; if `wc -l …/raw-ocr/full-text.txt`
  is tiny, force it: `python scripts/01_prepare_pdf.py <src.pdf> manuals/<slug>/ --force`.
- **Squished / stretched / cut-off renders** → source page boxes don't match the scanned
  image (any page size). `01` reframes **full-page-scan** pages to the image's own bbox
  (leaves born-digital/text/sparse pages untouched), prints pages fixed. Render one page to
  confirm nothing's cut off or stretched; re-run `01 --force` from the original on any pre-fix PDF.

## 3 — Author the manifest, render & split

Help the contributor write `manuals/<slug>/manifest.yml` (copy `manuals/_template/`).
Two required parts: the **`taxonomy:` block** (make/category/models/chassis/engines from
step 1a — keys must resolve in `taxonomy.yml`) and the **chapter list with 1-based inclusive
source page ranges** — read those off the manual's own table of contents.

```
python scripts/02_render_pages.py manuals/<slug>/     # page images for cross-checking
python scripts/03_split_manifest.py manuals/<slug>/   # raw per-chapter drafts
```

## 4 — Cleanup (the quality step)

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

## 4b — Deliver diagram-only pages

Diagrams/wiring charts/exploded views exist only as images. When a page or figure is
diagram-only and the user must *see* it, deliver it instead of a bare "see PDF p.N"
(rules: `04_cleanup_methodology.md` Rule 12):
1. Add a manifest **`diagrams:`** entry (`page`, `file: diagrams/p<NNNN>-<slug>.webp`,
   `kind`, `depth: mono|gray`, `caption`, `safety_relevant`) — `mono` for line art (~30 KB),
   `gray` for photo/halftone pages.
2. `python scripts/02_render_pages.py manuals/<slug>/ --diagrams` (needs `cwebp`).
3. Embed each at its citation point with a **relative** link
   (`![caption — PDF p.N](../diagrams/pNNNN-...webp)`) so it previews in the PR;
   `publish-release.sh` flips it to the Release URL at merge. **Commit `diagrams/`** (unlike
   the gitignored `pages/`); a maintainer moves the images to the Release, same as the PDF.

## 5 — Build the index files

Also **curate index terms with the `auto-mechanic` lens**: write **component-first** entries
("Water pump — installation", "Injector — resistance inspection"), not verb-first; use the
glossary's canonical names, surface standard aliases (e.g. diagnostic codes also under
**DTC**), and screen every term for OCR artifacts. For multi-model manuals, split the index
per model and tag each entry (issue #9).

```
python scripts/05_build_indexes.py manuals/<slug>/
python scripts/build_lookup_index.py manuals/<slug>/   # data/manual-index.jsonl — the fast path
python scripts/09_link_index.py                       # all-files.md + repo-root MANUALS.md
```

`build_lookup_index.py` flattens every spec **table** AND every prose spec statement (torque
in a NOTE, clearance in a step) into one `_page`-cited JSON row per fact (with `_flags`) — the
fast path a browsing/voice agent greps once for a torque/spec answer instead of reading
chapters. Torque is often prose-only, so a table-only index misses the most-asked question.
Point `wiki/llm-instructions.md`'s fast-path at `../data/manual-index.jsonl`, and remind the
agent to grep the manual's canonical term (via `auto-mechanic`), not the user's literal words.

`05` generates `00-index.md`, quick-reference, `10-needs-review.md`, and the
alphabetical index. (The 4A-GE reference ships hand-curated richer indexes; new
manuals start from the generated ones.)

`09` generates the **absolute-URL** navigation that web-fetch-only agents need:
`manuals/<slug>/wiki/all-files.md` (every file as a `raw.githubusercontent.com` link) and
the repo-root `MANUALS.md`. This is what lets an assistant with no shell and no GitHub MCP
reach the wiki at all — GitHub blocks automated crawling of `/tree/` folder pages, so
relative paths and folder browsing dead-end; the raw-URL lists don't. Run it any time files
are added/renamed (it's idempotent; repo/branch auto-detected from the git remote).

## 5b — Generate the README front matter

```
python scripts/10_write_frontmatter.py manuals/<slug>/
```

Writes the taxonomy front matter (make/models/chassis/engines/years) to the top of the
manual's `README.md` from the manifest — the machine-discovery layer for finding the right
manual for a car. Rewrites only that generated block, never your prose. Don't hand-edit it;
change the manifest/`taxonomy.yml` and re-run.

## 6 — Bake the index into the PDF

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

## 7 — Verify

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

## 8 — Open the pull request

Walk the contributor through it even if they've never made one — fork, branch,
commit, push, PR, and what a good description says. Full step-by-step (with
copy-paste commands and the first-timer path) is in
**`references/pull-request-walkthrough.md`**. Read it and adapt to their setup.

**Do commit the OCR'd + indexed source PDF in the manual folder** — that's the hand-off.
It does **not** stay in git: a maintainer moves it to a `manuals-<slug>` GitHub Release at
merge (`scripts/publish-release.sh`) and it's stripped from the tree, so PDFs never bloat
history. Tell the contributor the **`no-pdf-guard` CI check will be red** while their PDF is
committed — that's expected and clears at merge. Manual PRs are **squash-merged.** Full
contract: `MAINTAINERS.md`.

## What a finished package looks like

Mirror `manuals/toyota-4a-fe-4a-ge/`: `manifest.yml`, the OCR'd + indexed PDF (committed for
the PR; moved to a Release at merge), `wiki/` with per-chapter `.md`, `00-index.md`, `09-*`,
`10-needs-review.md`, `11a..d-alphabetical-index.md`, `llm-instructions.md`, and `diagrams/*.webp`
if any (step 4b — committed for the PR, moved to the Release at merge like the PDF). Don't commit
raw OCR intermediates (`.gitignore` already excludes `raw-ocr/`, `pages/`, `prepared.pdf`).
No GitHub account? Bundle the folder (wiki, manifest, `diagrams/`, PDF) into a zip and hand it
off per `references/cloud-no-cli.md`; a maintainer opens the PR.
