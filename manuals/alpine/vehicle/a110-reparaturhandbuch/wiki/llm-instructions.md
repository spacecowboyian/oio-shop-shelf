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

## Conversion status

**All 35 chapters are transcribed**, covering every one of the 468 PDF pages (each carries its
own `**[PDF p.N]**` marker). There are no stubs. **437 review flags** — high, and earned: this is
a watermarked, hand-annotated typescript scan, and much of the value sits in dense tables whose
OCR was unusable and which were read from page images instead. Read the flag before quoting a
flagged value.

## When the book disagrees with itself — say so

The book prints much of its data two or three times (the large handbook, the October 1970
factory manual, the supplement, and the key-settings plate), and the printings do not always
agree. These are recorded in flags in both places, never silently reconciled. The ones a user is
most likely to hit:

- **Crankshaft end float for the 810** — 0.05–0.23 mm in chapter 05 (p.84) against 0.044–0.16
  in chapter 03. The 0.05–0.23 figure is the 807's, possibly carried over in the source.
- **Front toe** — toe-OUT 2 ± 1 mm for every car in chapter 13 (p.250), against toe-out for the
  1300 VC but toe-IN for the 1600 VD/VH on the key-settings plate.
- **Front-radiator coolant capacity** — 13 L (chapter 09, p.159) and 13–14 L (supplement)
  against 9 L on the plate and in the factory manual.
- **Liner protrusion for the 807** — 0.15–0.20 mm on the plate, 0.10–0.15 at B-9.
- **Maximum head skim for the 807-25** — 0.30 mm at B-6. Do not use 0.5 mm.
- **1300 VC idle** — 675–725 rpm (chapter 08, p.151) against 800 ± 50 on the plate.

Where two printings DO agree (main-bearing and big-end torques, the B-2 valve timing, the
1300 VC brake disc and pad sizes), the flags say so — that agreement is the strongest evidence
this wiki has that a value is right.

## Images: every page, plus the named diagrams

**Every one of the 468 pages is a committed image.** Each `**[PDF p.N]**` marker in a chapter is
a link to that page's picture, so you can always show a reader the page you are citing — there is
no page you cannot produce. The URL pattern:

```
https://raw.githubusercontent.com/spacecowboyian/oio-shop-shelf/main/manuals/alpine/vehicle/a110-reparaturhandbuch/page-images/pNNNN.png
```

`NNNN` is the PDF page, zero-padded to four digits (page 37 → `p0037.png`). They are
black-and-white PNGs at 300 dpi, around 100 KB each, so they stand up to zooming on a big screen.

**72 pages are also registered as named diagrams** under `diagrams/`, with a caption and a
safety flag, and embedded at the point in the text where they matter. Those are the figures
worth calling out by name (bolt sequences, wiring, exploded views, chassis measuring points).

**[`../data/pages.json`](https://raw.githubusercontent.com/spacecowboyian/oio-shop-shelf/main/manuals/alpine/vehicle/a110-reparaturhandbuch/data/pages.json)** is the machine-readable index, and the reliable
way to get an image URL: **don't construct one, read it.** Every entry in its `pages` array
carries an absolute **`url`**, plus the page number, pixel and byte size, owning chapter, and —
where the page has a named figure — a `diagram` object with its own `url` and caption. Prefer the
diagram's `url` when there is one, otherwise the page's.

**Use the baked `url`, not a base.** `base_url.raw` is the host those urls were built from
(raw.githubusercontent.com — GitHub itself, always current). `base_url.cdn` is jsDelivr over the
same files, pinned to the commit the images were generated from: immutable and fast, good for a
client loading hundreds of images, but frozen, so it will not pick up a later correction.

## How to display a page — follow this, don't improvise

Showing the scanned page is most of the value here, and it is the part that most often goes
wrong. The rules below are the ones that were actually tested; a user should not have to paste
them into a prompt.

**Use the `url` from `pages.json`.** It is already absolute and already points at the CDN
(jsDelivr), which is what chat clients will render. Do not rebuild it from `base_url.raw`:
raw.githubusercontent.com is fine for *fetching* a file but is commonly refused as an image
source, which is exactly how you end up showing a broken image. Prefer a page entry's
`diagram.url` when it has one.

**Embed it so it is visible, not merely linked**, in this order of preference:

1. **Attach it as a normal chat image** if you can download the file and present it the way you
   present an image you generated. This is the only route that gets the client's native viewer,
   so the reader can tap to zoom. Prefer it.
2. **Otherwise use your client's inline image block.** A plain markdown `![](url)` is frequently
   downgraded to a link or a "Show Image" placeholder (seen in both ChatGPT web and Claude
   desktop), and raw HTML in ordinary prose is usually stripped. In ChatGPT an `AppBlock`
   wrapping a native `<img>` does render inline:

   ```
   <AppBlock title="PDF page N" variant="inline" app_block_id="manual-page-N">
     <div style="width:100%;display:flex;justify-content:center;background:#f2f2f2;border-radius:8px;padding:8px;">
       <a href="IMAGE_URL" target="_blank" rel="noopener" title="Open full size">
         <img src="IMAGE_URL" alt="Factory manual page N" style="display:block;width:100%;max-width:760px;height:auto;cursor:zoom-in;" />
       </a>
     </div>
   </AppBlock>
   ```

   Wrap the `<img>` in that link: an image inside a custom block gets no tap-to-zoom of its own,
   so the anchor is what lets the reader open the full-size page (these are ~2500 x 3500 px).

**Caption every image**, on the line directly beneath it:

```
PDF page N · IMAGE_URL
```

**Show every page the answer rests on**, each with its own caption — not just the first.

**Never claim a page is unavailable.** Every page of this manual has an image. If one genuinely
fails to render, say that it failed, give the url, and carry on — do not silently substitute a
different figure, and do not redraw the page. You may add your own SVG to clarify a sequence or
layout, clearly marked as yours, *alongside* the real page and never instead of it.

All of these are served as `image/png` from the same host as this markdown, with no redirect —
unlike the source PDF, which is a GitHub Release asset and is unreachable for most web-only
readers.

**Answer from the text first.** Wherever a figure carries information — a bolt tightening
sequence, a torque callout, a setting — it is also transcribed in the chapter next to the image,
with its flags. Quote the text, cite the PDF page, and show the picture alongside it.

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
  safety-relevant. For the **1300 VC** it is confirmed by the brakes chapter (discs 261 x 7.5 mm
  new, identical front and rear; pads 9.5 mm new, 5.5 mm limit). For the **1600 VD / VH** the
  plate's figures (11 mm disc minimum; pads 7 / 16 / 14 mm) appear nowhere else in the book —
  say so if a user asks.
- **Hand annotation affects a setting**: the Paris-Rhône starter pinion clearance on p.345 has
  been inked over ("ca 5 mm"; the typed original may have been 0.5 mm). Do not give a user that
  figure as settled.
- **Printed page 192 is missing** from the scan, leaving a gap in the 353/364 gearbox
  dismantling sequence; chassis section G(b) is announced on p.374 but absent.
- The **chassis dimension drawings** (pp.369–372) are too faint to set a gauge from; use the
  typed gauge dimensions on pp.367 and 372, which are clear and agree.
- **Misfiled pages**: PDF pp.156–157 are clutch pages bound inside the fuel chapter.
