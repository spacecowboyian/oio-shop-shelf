# Instructions for the AI assistant

You have access to the **Haynes Toyota Corolla (FWD, 1984-1992) repair manual** — cleaned
markdown for search, plus the original scanned PDF for diagrams. Read this file first,
before answering anything from these documents. This is a **whole-vehicle** aftermarket
(Haynes, not factory) manual covering the **4A-C, 4A-F, 4A-FE, and 4A-GE** engines and the
FWD Corolla chassis (E80/E90 generations, chassis AE80/AE82/AE91/AE92). Diesel and
all-wheel-drive (All-Trac) models are explicitly NOT covered.

## Fast path for a specific value — `../data/manual-index.jsonl`
For any single-value lookup (a spec, torque, clearance, resistance, voltage, capacity, DTC
code, or part number), `grep ../data/manual-index.jsonl` for the term and stop — one flat
file holds one JSON row per retrievable fact across the *whole* manual, so this resolves in
one hop with no chapter-file read. Each row has the value fields plus `_page` (cite it),
`_file`, `_section`, and `_flags`. **If `_flags` is non-empty, surface that OCR-uncertainty
rather than stating the value as fact; if it's empty, the value is a clean transcription —
answer directly.** This index is authoritative; do not also check the chapter files for the
same value. Only fall through to the chapter files when the value isn't in
`manual-index.jsonl` or the question is a procedure/diagram/diagnosis rather than a value
lookup.

## What's in this bundle
- `00-index.md` — chapter list + reference links.
- `00`–`13` — the manual's chapters: Introduction (incl. VIN, tools, troubleshooting),
  Tune-up & Routine Maintenance, Engines (2 parts: in-vehicle repair + general
  overhaul/rebuild), Cooling/Heating/AC, Fuel & Exhaust, Engine Electrical, Emissions
  Control, Manual Transaxle, Automatic Transaxle, Clutch & Driveaxles, Brakes, Suspension &
  Steering, Body, Chassis Electrical (+ Wiring Diagrams), and an Index/reference chapter
  (spark plug diagnosis chart).
- `09-quick-reference.md` — every number+unit spec harvested from the manual, linked to its
  chapter/heading.
- `10-needs-review.md` — every spot where OCR was garbled, a value was truncated in the
  source scan, or a pattern was inferred rather than read cleanly. Nothing here was guessed
  at or silently changed — check this before quoting a flagged value as settled fact.
- `11a-alphabetical-index.md` — topic index (component/procedure/symptom → chapter#heading),
  auto-generated from this conversion's own section headings — **not** a transcription of
  the original book's back-of-book index (that stays in `13-index-and-reference.md` as a
  provenance note only).
- `Toyota_Corolla_1984_1992_Haynes.pdf` — the source PDF, with a baked-in clickable index.
  Diagrams, exploded views, and wiring schematics exist ONLY here, never as text in the
  markdown — every diagram-only figure is flagged inline in the chapter markdown with
  `<!-- DIAGRAM CANDIDATE: p.N — ... -->`, citing the source page.

## Where the PDF lives
Committed at `manuals/toyota/vehicle/corolla-e80-e90/Toyota_Corolla_1984_1992_Haynes.pdf`, a
sibling of this `wiki/` folder — open it directly. Source-PDF page number = the `p.NN` in
`(PDF p.N)` citations throughout the chapter markdown, matching `<a id="pN"></a>` anchors at
the same spot. The manual's own printed page codes (e.g. `2A-15`, `9B-3`) sometimes appear
in illustration captions transcribed verbatim from the source — they are NOT PDF page
numbers; always use the `(PDF p.N)` citation for navigation.

## Rules
1. **Grep first.** For a specific spec, torque, clearance, resistance, DTC, or part number,
   check `data/manual-index.jsonl` first (see Fast path above), then `grep` across
   `wiki/*.md` if it's not there. Escalate to `11a-alphabetical-index.md` only when a common
   component name (e.g. "water pump", "cylinder head") is too noisy across chapters.
2. Every numeric value in the markdown is faithful to the OCR/extracted text or the source
   scan. Nothing numeric was "corrected" silently — where a value was ambiguous, cut off in
   the source, or reconstructed from context, it's flagged inline with
   `<!-- NEEDS REVIEW: ... -->` and rolled into `10-needs-review.md`.
3. **Before stating any spec as fact, check whether it's flagged in `10-needs-review.md`.**
   If flagged, tell the user it's flagged and why (OCR-uncertain, source-truncated, or an
   internally-inconsistent manual misprint).
4. This manual covers **four engines** (4A-C carbureted SOHC; 4A-F carbureted DOHC; 4A-FE
   fuel-injected DOHC; 4A-GE fuel-injected DOHC, GT-S trim) across **multiple model years**
   (1984-1992) with running changes — many spec tables are split by engine and/or year.
   Confirm which engine/year a spec applies to before quoting it; don't assume one engine's
   spec applies to another.
5. This is a **Haynes aftermarket manual**, not a Toyota factory service manual — expect
   less depth on specialty/SST procedures than the repo's factory manuals (e.g.
   `toyota/vehicle/mr2-aw11` or `toyota/engine/4a-fe-4a-ge`). The 4A-GE engine internals
   overlap those manuals; this Corolla book adds Corolla-chassis-specific context (body,
   FWD driveaxles/transaxle, suspension) around the shared engine family.
6. OCR/extraction quirks to watch for in this scan: **Ω (ohms) can read as `2`**; `l`↔`i`,
   `h`↔`li`, `rn`↔`m` substitutions in scanned text; multi-column source layout occasionally
   interleaves unrelated table cells — cross-check any value that looks internally
   inconsistent (e.g. an inch figure that doesn't match its stated mm equivalent) against
   `10-needs-review.md` before trusting it.
7. Diagrams, wiring schematics, and exploded views are image-only — follow the
   `<!-- DIAGRAM CANDIDATE: p.N -->` marker to the PDF page rather than describing them from
   markdown; none of them have been rendered/delivered as separate image files in this
   conversion yet.
8. Always cite the source PDF page (`(PDF p.N)`) back to the user so they can verify against
   the scan.
