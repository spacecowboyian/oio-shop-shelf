# Toyota 4A-FE / 4A-GE Engine Repair Manual (Sep. 1989) — Index

Source: `Toyota-4A-FE-4A-GE-engine-repair-manual-OCR.pdf` (228 pages, committed in this
folder; text layer via Adobe Paper Capture, decrypted with qpdf).

**Status: IN PROGRESS (scaffold).** This manual was added by dogfooding the
[`convert-manual`](../../../skills/convert-manual/SKILL.md) skill. The mechanical
pipeline (decrypt → prepare → split → manifest) is done and verified; the per-chapter
OCR cleanup is **mostly not done yet** — only Starting System is transcribed so far.
Full transcription + the plan to cross-check against the other 4A manual is issue-tracked.

**If you're an AI assistant:** read [llm-instructions.md](llm-instructions.md) first — this
manual has three provenance landmines (encrypted source, an **abridged** scan with missing
pages, and a bogus third-party "reduce torque 40%" sticker) plus heavy 4A-FE/4A-GE
interleaving. Also read the repo root `llm-instructions.md` and `glossary.md`.

## This is a DISTINCT manual

Not to be confused with [`manuals/toyota-4a-fe-4a-ge/`](../../toyota-4a-fe-4a-ge/wiki/00-index.md)
— that is the **Service & Maintenance Manual** (219 pp). This is the **Engine Repair
Manual** (228 pp). Both cover 4A-FE and 4A-GE. A future pass may merge best-of-breed
content from the two into per-engine manuals; for now treat this as its own manual.

## Chapters (section codes verified against each section's TOC page)

| Code | Chapter | File | PDF pages | Cleanup |
|---|---|---|---|---|
| IN | Introduction | [01-introduction.md](01-introduction.md) | 2–9 | ✅ done |
| EM | Engine Mechanical (4A-FE / 4A-GE) | [02-engine-mechanical.md](02-engine-mechanical.md) | 10–75 | ◑ partial (Description, Troubleshooting, Tune-up done; Timing Belt / Cylinder Head / Block pending) |
| FI | EFI System (4A-FE / 4A-GE) | [03-efi-system.md](03-efi-system.md) | 76–169 | ☐ pending |
| CO | Cooling System | [04-cooling-system.md](04-cooling-system.md) | 170–188 | ✅ done |
| LU | Lubrication System | [05-lubrication-system.md](05-lubrication-system.md) | 189–196 | ✅ done |
| IG | Ignition System (**4A-FE** only in this scan) | [06-ignition-system.md](06-ignition-system.md) | 197–207 | ✅ done |
| ST | Starting System | [07-starting-system.md](07-starting-system.md) | 208–212 | ✅ done |
| CH | Charging System | [08-charging-system.md](08-charging-system.md) | 213–218 | ✅ done |
| A/B/C | Service Specs, Bolt Torque, SST & SSM | [09-service-specifications-torque-sst.md](09-service-specifications-torque-sst.md) | 219–228 | ☐ pending |

**Alphabetical index — split per engine** (shared entries appear in both; grows as chapters
are cleaned): [4A-FE](11a-alphabetical-index.md) · [4A-GE](11b-alphabetical-index.md). A
4A-GE user won't be handed 4A-FE-only content (e.g. the IIA ignition specs), and vice
versa. See [issue #9](https://github.com/spacecowboyian/oio-shop-shelf/issues/9) for the
per-model direction.

Pending chapters have a raw draft in `raw-ocr/` (gitignored) ready for the cleanup step
per [`scripts/04_cleanup_methodology.md`](../../../scripts/04_cleanup_methodology.md).
The alphabetical index (markdown + the copy baked into the PDF) is rebuilt with
`python scripts/08_append_index_pages.py manuals/toyota-4a-fe-4a-ge-repair/ --in-place`.

## Known scan gaps

`scripts/check_page_continuity.py` flags this scan as **abridged** — several sections'
page numbers skip (e.g. ST-2 → ST-15, EM has ~24 numbered pages missing). See
[10-needs-review.md](10-needs-review.md). Don't assume any section is complete.
