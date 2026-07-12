# Instructions for the AI assistant — Renault Dauphine (M.R. 93)

You have the **Renault Dauphine / Ondine / Gordini factory workshop manual (M.R. 93, English
edition, Nov 1964)**: OCR'd markdown for search, the original scanned PDF for anything visual,
and — unusually for this repo — **the diagram-only figures delivered as images** (see below).
Covers types **R1090 / R1091 / R1093**. Read this file first, before answering from it.

> **Fetch-only agent (no shell / no GitHub MCP)?** Don't browse the folder — every file in
> this manual is listed as an absolute raw URL in [`all-files.md`](all-files.md). See the
> repo-root [`llm-instructions.md`](../../../../../llm-instructions.md) for why `/tree/`
> browsing fails and how to navigate by raw URL.

## What's in this bundle
- `00-index.md` — chapter list.
- **14 lettered chapters** — the manual's own tab structure (letters skip I and O):
  `a-general` · `b-engine` · `c-clutch` · `d-electrical-and-ignition` · `e-gearbox` ·
  `f-braking-system` · `g-steering` · `h-front-axle` · `j-rear-axle` · `k-wheels-hubs-drums` ·
  `l-suspension-shock-absorbers` · `m-bodywork` · `n-heater` · `p-special-tools`.
  Each opens with an "In this chapter" heading structure and carries `<!-- PDF p.N -->`
  markers so every passage cites its source page.
- `09-quick-reference.md` — harvested spec values (torque, clearance, resistance, capacity…),
  each linked to its source page. ~1000 specs — usually the fastest way to a single value.
- `10-needs-review.md` — every spot where a value was OCR-uncertain or a **source misprint**.
  **58 flags** — this is a 1964 typescript scan, so it has more than a clean manual. Nothing
  here was guessed at or silently "fixed".
- `11a-alphabetical-index.md` — present but sparse: this manual has no back-of-book index
  (it navigates by lettered tab + per-chapter contents), so prefer grep + the quick-reference.
- The source PDF — diagrams/wiring/exploded views exist there; but many are also delivered
  as images here (next section).

## Diagrams ARE delivered here — surface them
**Precedence: prefer the delivered image; only when a needed diagram isn't in `manifest.yml`
`diagrams:` do you fall back to citing the PDF page.** This manual dogfoods diagram delivery.
**~120 diagram-only figures** (wiring schematics,
exploded views, torque/loosening sequences, body-jig dimensions, gauge setups) are rendered
to images and **embedded at their citation point** in the chapter markdown as
`![caption — PDF p.N](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/pNNNN-….webp)`, and registered in `manifest.yml`'s
`diagrams:` block (with `kind`, `depth`, and a `safety_relevant` flag).

When the user needs one of these — e.g. the **cylinder-head bolt tightening sequence**
(`b-engine.md`, PDF p.49) or a **wiring diagram** (`d-electrical-and-ignition.md`) — surface
the embedded image: a markdown-rendering client shows it inline; otherwise give the user the
image URL. Do **not** paraphrase a safety-relevant diagram (bolt sequence, jack points, brake
layout) from memory — deliver the image and cite the page.

## Rules
1. **Grep first.** For a specific spec value, part number, or exact procedure name, `grep`
   across `wiki/*.md` — with `<!-- PDF p.N -->` markers you'll land on the right passage and
   its source page in one hop.
2. **Every numeric value is byte-identical to the OCR scan** — nothing was "corrected" during
   cleanup, even when it looked wrong. Where a value was resolved from the page image, or is a
   confirmed **source misprint**, it is flagged inline and rolled into `10-needs-review.md`.
3. **Before stating any spec as fact, check `10-needs-review.md`.** If it's flagged, tell the
   user it's flagged and why — don't just state it. Watch especially for the manual's own
   misprints (several imperial conversions, a couple of dropped digits) documented there.
4. **Cite the PDF page** (matches the `<!-- PDF p.N -->` markers and the `pNNNN.png` renders).
   Note: the PDF page runs a little ahead of the printed "`<Letter>-n`" page, and the offset
   drifts per chapter — always cite the PDF page number, not the printed one.
5. **Multi-model manual.** Specs often differ across R1090 / R1091 (Gordini) / R1093 and by
   year (pre-1960 / 1960 / 1961) and heater/clutch variant — make sure you quote the row for
   the user's exact model/year, not a neighbouring one.

## Where the PDF lives
Committed as `manuals/renault/vehicle/dauphine/renault-dauphine-mr93.pdf` (a sibling of this
`wiki/`) for the PR; a maintainer moves it — and the `diagrams/*.webp` — to the manual's
GitHub Release at merge. If you're reading this via a wiki tool that stores markdown only, the
PDF/images may not be siblings there; fall back to the source pointer in `manifest.yml`.
