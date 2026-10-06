# Instructions for the AI assistant — Alpine A110 Reparaturhandbuch

You have the **Alpine A110 German-language factory repair handbook** (*Reparaturhandbuch*,
Typ A 110, RENAULT · ALPINE imprint): 468 pages, re-OCR'd markdown for search, the source PDF
for anything visual, and selected diagram-only pages delivered as images. Read this file first,
before answering from it.

> **Fetch-only agent (no shell / no GitHub MCP)?** Don't browse the folder — every file in this
> manual is listed as an absolute raw URL in [`all-files.md`](all-files.md). See the repo-root
> [`llm-instructions.md`](../../../../../llm-instructions.md) for why `/tree/` browsing fails.

## Read this before quoting any value

**This manual is German; this wiki is an English translation made by the conversion.** Two
passes stand between the printed page and the text you are reading — OCR, then translation.
Per cleanup Rule 13, **no unit was converted and no digit was changed**: `mkp`, `m.daN`, `bar`
and `kg/cm²` stay exactly as printed, and part numbers and type codes are untouched. Do not
"helpfully" convert a unit for the user unless they ask, and say so when you do.

**Decimal separators ARE normalized.** The German pages print `0,044 mm`; this wiki writes
`0.044 mm`, and `10.000 km` becomes `10,000 km`. So if a user compares a line here against the
source page and sees a comma where the wiki has a point, that is expected and the value is the
same. Only the separator moved.

**This copy is annotated.** A previous owner inked corrections onto several pages — a "353"
over a printed gearbox type, a handwritten "364 / 2.2 L" column, "1600 S" beside the axle
blocks, a row label on the service chart. Every one is flagged in place and is **not** factory
data. If a flag says "HANDWRITTEN", tell the user it is an annotation.

## Fast path — a specific value (do this FIRST)

For a single value — torque, clearance, capacity, bore, timing, part number — grep the flat
lookup index **[`../data/manual-index.jsonl`](../data/manual-index.jsonl)** (one JSON row per
fact, covering spec tables and prose spec statements alike). Read the matching row, cite its
`_page`, and **if `_flags` is non-empty, surface that uncertainty** rather than stating the
value as settled. One grep, one line — don't open a chapter for a value lookup.

**Grep the manual's term, not the user's words.** This is a German manual rendered to English,
so a value may sit under either wording. Use the `auto-mechanic` skill and
[`glossary.md`](../../../../../glossary.md) to reach the canonical English term, and try the
German where a term survives in a flag: *Ventildeckel* (valve cover), *Laufbuchsen* (liners),
*Kolbenbolzen* (gudgeon pin), *Pleuel* (con-rod), *Kurbelwelle* (crankshaft), *Anzugsdrehmoment*
(tightening torque), *Ventilspiel* (valve clearance), *Überstehmaß* (protrusion),
*Spur* (toe), *Sturz* (camber), *Nachlauf* (castor).

## The PDF is three bound documents

This matters when you cite a page, because the same subject is covered twice at different
depths:

| PDF pages | Document | Use it for |
|---|---|---|
| 1–374 | The large Reparaturhandbuch | Full overhaul of engines and gearboxes; the **only** part covering the later 1600 SC / SC-SI cars (types 1600 VD / 1600 VH) |
| 375–433 | The 1st edition factory manual, October 1970, in German | Section-coded reference data (`A-1`, `B-2`, `H-1` …); often the cleaner printing of a spec table |
| 434–468 | The update supplement, December 1970 onward | Amendments, cable directory, bulb table, lacquer tables |

When the two disagree, **say so** rather than picking one. They do disagree: the engine
valve-timing rows on PDF p.15 and at B-2 (PDF p.383) OCR differently, and that is recorded as a
flag in [`03-engine-ignition-data.md`](03-engine-ignition-data.md).

## Page numbering — do not do arithmetic on it

The printed page number and the PDF page number are **not** offset by a constant. Unnumbered
plate and divider pages are interleaved, so the offset drifts from **−1 at the front to +10**
by the electrical and body chapters, and the book also inserts suffixed pages (e.g. `114a`).
The factory-manual part (375–433) does not use continuous numbers at all — it uses section
codes. **Always cite the PDF page** (`_page` in the index, `**[PDF p.N]**` in the chapters). If
a user gives you a printed page number, do not convert it; ask which they mean or search for
the content.

## Which car does this cover?

| Type | Engine | Displacement |
|---|---|---|
| 1300 VA (G) | 812 | 1255 cm³ |
| 1300 VB (S) | 812-00 derivative | 1296 cm³ |
| 1300 VC (V85) | 810 / 810-05 / 810-30 | 1289 cm³ |
| 1600 VA | 807 | 1565 cm³ |
| 1600 VB (S) | 807-25 | 1565 cm³ |
| 1600 VC (S) | 844 / 844-32 | 1605 cm³ |
| 1600 VD (SC / SI) | 844-30 / 844-34 | 1605 cm³ |
| 1600 VH (SX) | 843-30 | 1647 cm³ |
| 1600 GS | derived from 807-25 | 1596 cm³ |

The **cover understates the coverage** — it lists only 1300 VA/VB/VC, 1600 VB and GS. Always
check the type table in [`01-front-matter.md`](01-front-matter.md), which also gives the
Renault equivalents (R8, R10, R12, R15/17, R16) for sourcing parts.

## What's in this bundle

- `00-index.md` — chapter list with PDF page ranges.
- **35 chapters** across the three documents. Each carries `**[PDF p.N]**` markers so every
  passage cites its source page.
- `09-quick-reference.md` — harvested spec values linked to their source page.
- `10-needs-review.md` — every uncertain value and every source misprint. Nothing was guessed.
- `11a-alphabetical-index.md` — built from chapter subsection headings.
- `../diagrams/*.webp` — diagram-only pages delivered as images (key-settings plate with the
  head-bolt sequences, the Renault/Alpine type table, the service schedule).
- The source PDF — all other diagrams, wiring and exploded views live there.

## Conversion status — IMPORTANT

**This conversion is in progress.** Only chapters **01, 02 and 03** are transcribed. The other
32 chapters are **stubs**: they state their PDF page range and nothing else.

If a chapter you need is a stub, **say so and point the user at the source PDF pages** — do not
tell them the manual has no answer. The absence of a value in this wiki currently means "not
yet transcribed", not "not in the manual".

## Known problems in this source

- The scan carries a **"DerFranzose" watermark** across every page, which overlaps figures and
  some body text and costs OCR accuracy.
- **PDF p.18 is a misaligned scan**: a neighbouring page's valve / tappet / pushrod data table
  bleeds into the left margin, clipped. That data is printed complete at **B-7 (PDF p.388)**.
- The **cover is clipped** at the bottom in the scan itself.
- **PDF p.468** (back cover) carries no OCR text at all.
- The dense reference plates (PDF pp.8, 9, 13, 15, 19, 20, 21) OCR to near-noise and were
  transcribed from page images. Their flags are worth reading before you quote them.
- The **brake disc and pad thickness block** on the key-settings plate (PDF p.13) is
  safety-relevant and the least legible thing in the manual. Do not let a user judge a disc or
  pad serviceable from it — send them to the source page.
