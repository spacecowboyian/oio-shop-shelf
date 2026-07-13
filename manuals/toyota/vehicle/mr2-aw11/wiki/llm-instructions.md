# Instructions for the AI assistant

You have access to the **Toyota MR2 (AW11) 1988 factory service manual** — OCR'd markdown
for search, plus the original scanned PDF for diagrams. Read this file first, before
answering anything from these documents. This is a **whole-vehicle** manual covering the
**4A-GE** and supercharged **4A-GZE** engines and the AW11 chassis.

## Fast path for a specific value — `../data/manual-index.jsonl`
For any single-value lookup (a spec, torque, clearance, resistance, voltage, capacity, DTC code, or part number), `grep ../data/manual-index.jsonl` for the term and stop — one flat file holds one JSON row per retrievable fact across the *whole* manual, so this resolves in one hop with no chapter-file read. Each row has the value fields plus `_page` (cite it), `_file`, `_section`, and `_flags`. **If `_flags` is non-empty, surface that OCR-uncertainty rather than stating the value as fact; if it's empty, the value is a clean transcription — answer directly.** This index is authoritative; do not also check the chapter files for the same value. Only fall through to the chapter files when the value isn't in `manual-index.jsonl` or the question is a procedure/diagram/diagnosis rather than a value lookup.

## What's in this bundle
- `00-index.md` — chapter list (24 chapters across 19 numbered sections) + reference links.
- `01`–`19` — the manual's chapters: Introduction, Maintenance, Engine Mechanical (2 parts),
  Supercharger (4A-GZE), EFI & Emission Control (2 parts) **+ Engine Cooling** (in 05b),
  Lubrication, Ignition, Starting, Charging, Clutch, Manual Transmission C52/E51 (2 parts),
  Automatic Transmission A240E/A241E (2 parts), Front & Rear Suspension/Axle, Brakes,
  Steering, Body Electrical + Body (2 parts), Air Conditioning, and the **Appendix**
  (master Service Specifications, standard bolt torque, SST/SSM lists, hydraulic & wiring
  reference).
- `09-quick-reference.md` — every number+unit spec harvested from the manual, linked to its
  chapter/heading.
- `10-needs-review.md` — every spot (90 flags) where OCR was garbled or the **manual itself**
  misprints a value. Nothing here was guessed at or silently changed.
- `11a-alphabetical-index.md` — back-of-book index (component/procedure/symptom → chapter#heading).
- `mr2-aw11-1988-fsm.pdf` — the source PDF. Diagrams, exploded views, wiring schematics, and
  the illustrated SST matrix exist ONLY here, never as text in the markdown.

## Where the PDF lives
Committed at `manuals/toyota-mr2-aw11/mr2-aw11-1988-fsm.pdf`, a sibling of this `wiki/`
folder — open it directly. Source-PDF page number = the `p.NN` in figure callouts
(`*(Figure: … — see page image p.NN)*`). The manual's own page codes (e.g. `EM-18`,
`FI-14`, `A-7`) are printed in the body for cross-reference; they are NOT PDF page numbers.

## Rules
1. **Grep first.** For a specific spec, torque, clearance, resistance, DTC, or part number,
   `grep` across `wiki/*.md` — usually one hop to the right passage. Escalate to
   `11a-alphabetical-index.md` only when a common component name (e.g. "oil pump", "cylinder
   head") is too noisy across chapters. For a master spec, the **Appendix (ch 19)** collects
   every service specification in one place.
2. Every numeric value in the markdown is faithful to the OCR scan / page image. Nothing
   numeric was "corrected" silently — where a value was resolved from the page image or is a
   suspected manual typo, it's noted inline and rolled into `10-needs-review.md`.
3. **Before stating any spec as fact, check `10-needs-review.md`.** If it's flagged, tell the
   user it's flagged and why (OCR-uncertain, or an internally-inconsistent manual misprint —
   e.g. the `1,450 (105, 42)` torque, whose N·m figure is a manual typo for 142).
4. **Torque is printed as `kg-cm (ft-lb, N·m)`** in this manual, e.g. `650 (47, 64)` — all
   three are the same torque in different units. Quote all three; never convert.
5. This manual covers **two engines**: confirm whether a spec is for the **4A-GE** or the
   supercharged **4A-GZE** before quoting it — many tables list both.
6. OCR quirks in this scan: **Ω (ohms) often reads as `2`, `0`, `n`, or `fl`**; `kg-cm`
   sometimes OCR'd as `kg-em`. Keep this in mind for resistance/torque specs.
7. Diagrams, wiring schematics, hydraulic circuits, and the SST illustrations are image-only
   — follow the figure placeholder to the PDF page rather than describing them from markdown.
8. Always cite the source PDF page (`p.NN`) or the manual's section-page code back to the
   user so they can verify against the scan.
