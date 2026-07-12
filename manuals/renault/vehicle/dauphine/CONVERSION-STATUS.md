<!-- TEMPORARY handoff/progress note for the in-progress Renault Dauphine conversion.
     DELETE this file before opening the final PR. -->

# Renault Dauphine (M.R.93) conversion — status & resume guide

Branch: `feat/diagram-image-delivery` (worktree at `/Users/ian/repos/oio-shop-shelf-diagram-images`).
This conversion dogfoods the diagram-delivery feature (issue #1) + the scanned-PDF prep fixes,
on the first non-Toyota manual. Being done **one chapter at a time** (serial) to stay within
usage limits — parallel fan-out worked but risks token exhaustion.

## Environment to rebuild (nothing here is committed except source scripts)
- **Source PDF**: Google Drive id `1FJnayZ3hCiUMyRHCA_oRFhxmO5K7aHG9` (14 MB, 479 pp).
  Download: `curl -sL "https://drive.google.com/uc?export=download&id=1FJnayZ3hCiUMyRHCA_oRFhxmO5K7aHG9" -o renault.pdf`
- **venv** (PyYAML + PyMuPDF needed by the scripts):
  `python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt`
- **Regenerate prepared.pdf + text + pages** (all gitignored, regenerable):
  `.venv/bin/python scripts/01_prepare_pdf.py renault.pdf manuals/renault/vehicle/dauphine/ --force --language eng`
  then `.venv/bin/python scripts/02_render_pages.py manuals/renault/vehicle/dauphine/ --dpi 150`
  (01 auto-forces OCR and reframes the scan's bad page boxes — see the fix in 01_prepare_pdf.py).

## Key facts / gotchas
- OCR on this 1964 typescript is BADLY garbled on numbers (e.g. `3.945 m`→"34945 m"). Rule 0:
  never guess a number → **verify every published number against the page image**, flag if unsure.
- Page mapping: PDF page ≈ printed "<Letter>-n" but the offset drifts per chapter and skips slots
  (e.g. C skips C8). Cite the **PDF page number** (matches pNNNN.png), note printed page if handy.
- Chapter files use **letter prefixes** (`a-general.md` … `p-special-tools.md`) to avoid colliding
  with generated `00/09/10/11` index files.

## Chapter status  (source-PDF page ranges from manifest.yml)
- [x] A general (p1–15) — `wiki/a-general.md` DONE (committed). 2 diagrams registered (p13, p14).
- [~] B engine (p16–68) — cleanup agent RUNNING (selective-image approach).
- [ ] C clutch (p69–118)
- [ ] D electrical & ignition (p119–185) — has wiring diagrams to deliver
- [ ] E gearbox (p186–247) — exploded views
- [ ] F braking (p248–268) — safety-critical specs
- [ ] G steering (p269–286)
- [ ] H front axle (p287–305)
- [ ] J rear axle (p306–310) — short
- [ ] K wheels-hubs-drums (p311–332)
- [ ] L suspension-shock-absorbers (p333–353)
- [ ] M bodywork (p354–436) — LARGE, figure-heavy
- [ ] N heater (p437–449)
- [ ] P special tools (p450–479) — catalogue; render as ref#→description TABLE, don't image-dump

## Per-chapter cleanup subagent prompt (template)
Spawn a `general-purpose` subagent PER chapter (serial). Prompt skeleton (fill <LETTER>/<title>/
<file>/<start>/<end>/§codes):
- Read `scripts/04_cleanup_methodology.md` (Rule 0 inviolable) + `glossary.md`; glance at `wiki/a-general.md` for house style.
- PRIMARY source = `raw-ocr/<file>.draft.txt`. **Image policy (economical):** build prose/procedures
  from OCR; ONLY open `pages/pNNNN.png` for pages with spec/torque/dimension tables, garbled-looking
  numbers, or diagrams to deliver. Don't view pure-prose pages.
- Output `wiki/<file>.md`: H1 = chapter title, tables for specs (units on numbers), ordered lists for
  procedures, blockquotes for CAUTION/NOTE, `<!-- PDF p.N -->` per page. Every number byte-identical.
- Rule 12 diagram delivery: embed diagram-only pages as `![caption — PDF p.N](../diagrams/pNNNN-<slug>.webp)`
  (relative link — publish-release.sh flips it to the Release URL at merge). Still transcribe readable callouts.
- RETURN concise: path, quality note, NEEDS REVIEW count, and a YAML `diagrams:` list
  (page, file `diagrams/pNNNN-<slug>.webp`, kind sequence|wiring|exploded|chart, depth mono|gray, caption, safety_relevant).

**Collect each chapter's returned `diagrams:` list** into the master list below.

## Diagram registry (accumulate from each chapter's return, then write into manifest.yml `diagrams:`)
```yaml
# A:
- {page: 13, file: diagrams/p0013-lifting-points.webp, kind: exploded, depth: mono, caption: "Dauphine lifting points A–F (side view and underbody views)", safety_relevant: true}
- {page: 14, file: diagrams/p0014-lifting-trolley-jack.webp, kind: exploded, depth: gray, caption: "Trolley-jack lifting points — front (A) and rear (B)", safety_relevant: true}
# B..P: append as chapters finish
```

## Remaining pipeline AFTER all chapters cleaned
1. Write the accumulated `diagrams:` block into `manuals/renault/vehicle/dauphine/manifest.yml`; `validate_manifests.py`.
2. Render diagram images: `.venv/bin/python scripts/02_render_pages.py manuals/renault/vehicle/dauphine/ --diagrams` → writes `diagrams/*.webp`.
3. `05_build_indexes.py` (00-index, quick-reference, 10-needs-review, alphabetical index) — NOTE: verify it
   handles letter-prefixed chapter filenames; fix if it assumes numeric prefixes.
4. `09_link_index.py` (all-files.md + MANUALS.md); `10_write_frontmatter.py` (README front matter).
5. `08_append_index_pages.py --in-place` (bake index into prepared.pdf → the shipped PDF).
6. Verify: `06_check_links.py`, `validate_manifests.py`, `check_page_continuity.py`.
7. Commit the source PDF into the manual folder (named e.g. `renault-dauphine-mr93.pdf`) — `no-pdf-guard`
   goes red (expected; a maintainer runs `publish-release.sh` at merge, which also moves `diagrams/*.webp`
   to the Release and flips the relative embeds to Release URLs).
8. DELETE this CONVERSION-STATUS.md, commit, open the PR (per `skills/convert-manual` step 8).
