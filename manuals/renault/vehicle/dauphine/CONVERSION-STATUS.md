<!-- TEMPORARY handoff/progress note for the in-progress Renault Dauphine conversion.
     DELETE this file before opening the final PR. -->

# Renault Dauphine (M.R.93) conversion — status & resume guide

Branch: `feat/diagram-image-delivery` (worktree at `/Users/ian/repos/oio-shop-shelf-diagram-images`).
This conversion dogfoods the diagram-delivery feature (issue #1) + the scanned-PDF prep fixes,
on the first non-Toyota manual. Being done **one chapter at a time** (serial) to stay within
usage limits — parallel fan-out worked but risks token exhaustion.

## ⚠️ SESSION NOTE — 2026-07-12 ~19:xx UTC (Cowork dispatch) — READ BEFORE CONTINUING
A prior session had already cleaned **D, E, F, G** (markdown + manifest diagram blocks + the
`[x]` lines below), but **none of it is committed** — `git commit` is blocked by a stale
`.git/.../index.lock` (dated 13:33) that this sandbox mount **cannot delete** ("Operation not
permitted"; the Cowork delete-permission prompt was declined). So HEAD is still at
`chapter C cleaned`; D/E/F/G live only in the working tree.

This dispatch (brief said "C done, D next", reflecting the committed state) re-cleaned **D**
with a fresh image-verified pass and **overwrote the prior uncommitted `d-electrical-and-ignition.md`**.
Consequences to reconcile before committing D:
- The new D markdown delivers **14 diagrams / 10 NEEDS-REVIEW flags** (not the 24/15 in the D line
  below, which describes the prior draft).
- `manifest.yml`'s D block (pre-staged by the prior session, ~25 entries) uses **different filename
  slugs** and registers more figures (distributor/dynamo exploded views, etc.) than the new D
  markdown embeds → **markdown embeds and manifest D entries no longer match 1:1.**
- CLI action: pick the D version to keep, align the `manifest.yml` D slugs + the D status line to it,
  then commit D–G with the usual `wip(renault-dauphine): chapter X …` messages. E, F, G markdown were
  left untouched by this session.
- Housekeeping: an untracked stray file `.__deltest__` at the worktree root (from this session's
  delete-capability probe) could not be removed by the sandbox — `rm` it before committing.

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
- [x] B engine (p16–68) — DONE. 7 diagrams (incl p49 head-bolt sequence, safety). ~30 images opened, 1 flag.
- [x] C clutch (p69–118) — DONE. 11 diagrams (Ferlec wiring + defect chart). ~40 images, 6 flags.
- [x] D electrical & ignition (p119–185) — DONE. 24 diagrams (5 variant wiring schematics + harness layouts, distributor/dynamo/starter exploded views, advance-curve charts). Every ignition/charging/starting spec table verified against page image; page-map offset drifts +118→+117→+116 (printed D-10 and D-18 absent from scan). 15 flags.
- [x] E gearbox (p186–247) — DONE. 13 diagrams (operating diagrams, sections, differential + secondary-shaft exploded views, gear-locking systems for types 289/314/316). Page-map offset clean +184. Every ratio/shim/torque/backlash table verified cell-by-cell against images; recovered printed E-47 from p0231 image. 9 flags.
- [x] F braking (p248–268) — DONE. 12 diagrams (hydraulic layout, master-cylinder operation/exploded views, shoe & adjustment figures, hand brake, pressure-limiting valve). Page-map offset clean +246. Every brake spec/torque/limiter-pressure table verified cell-by-cell against images; limiter setting "50 +0/−8 kg/sqcm" corrected from image. 5 flags (2 safety-critical, resolved from image). SAFETY-CRITICAL chapter — every value cross-checked.
- [x] G steering (p269–286) — DONE. 8 diagrams (box section, pinion/flange & rack exploded views, pinion end-play adjustment, links, column, steering lock). Page-map offset clean +267. All 18 images opened; every geometry/pre-load/torque verified. 4 flags (1 safety torque corrected from image). 
- [x] H front axle (p287–305) — DONE. 11 diagrams, ~15 images, 1 flag (camber/castor label).
- [x] J rear axle (p306–310) — DONE. 4 diagrams, 5 images, 0 flags.
- [x] K wheels-hubs-drums (p311–332) — DONE. 7 diagrams, 22 images, 3 flags (source misprints).
- [~] L suspension-shock-absorbers (p333–353) — NEXT
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
