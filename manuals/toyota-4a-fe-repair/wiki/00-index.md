# Toyota 4A-FE Engine Repair Manual (Sep. 1989) — Index

Source: `Toyota-4A-FE-4A-GE-engine-repair-manual-OCR.pdf` (228 pages, committed in this
folder; text layer via Adobe Paper Capture, decrypted with qpdf).

**New here? Read [`../README.md`](../README.md) first** — a plain-language overview of the
4A-FE engine, which vehicles used it, and what this manual does and doesn't cover.

**Status: all 9 chapters transcribed** (image-verified), with a baked-in alphabetical index.
Added by dogfooding the [`convert-manual`](../../../skills/convert-manual/SKILL.md) skill.

**If you're an AI assistant:** read [llm-instructions.md](llm-instructions.md) first — this
manual has three provenance landmines (encrypted source, an **abridged** scan with missing
pages, and a bogus third-party "reduce torque 40%" sticker). It's a **4A-FE** manual with
only incidental 4A-GE references (tagged `(4A-GE)`). Also read the repo root
`llm-instructions.md` and `glossary.md`.

## This is a DISTINCT manual

Not to be confused with [`manuals/toyota-4a-fe-4a-ge/`](../../toyota-4a-fe-4a-ge/wiki/00-index.md)
— that is the **4A-F / 4A-GE Service & Maintenance Manual** (219 pp). This is the **4A-FE
Engine Repair Manual** (228 pp). Toyota's cover titles this one "4A-FE, 4A-GE," but the
4A-GE content is incidental only (see [`../README.md`](../README.md)) — treat it as a 4A-FE
manual.

## Chapters (section codes verified against each section's TOC page)

| Code | Chapter | File | PDF pages | Cleanup |
|---|---|---|---|---|
| IN | Introduction | [01-introduction.md](01-introduction.md) | 2–9 | ✅ done |
| EM | Engine Mechanical (4A-FE) | [02-engine-mechanical.md](02-engine-mechanical.md) | 10–75 | ✅ done (Cylinder Block largely absent from scan; physical pages out of logical order) |
| FI | EFI System (4A-FE) | [03-efi-system.md](03-efi-system.md) | 76–169 | ✅ done |
| CO | Cooling System | [04-cooling-system.md](04-cooling-system.md) | 170–188 | ✅ done |
| LU | Lubrication System | [05-lubrication-system.md](05-lubrication-system.md) | 189–196 | ✅ done |
| IG | Ignition System (**4A-FE** only in this scan) | [06-ignition-system.md](06-ignition-system.md) | 197–207 | ✅ done |
| ST | Starting System | [07-starting-system.md](07-starting-system.md) | 208–212 | ✅ done |
| CH | Charging System | [08-charging-system.md](08-charging-system.md) | 213–218 | ✅ done |
| A/B/C | Service Specs, Bolt Torque, SST & SSM | [09-service-specifications-torque-sst.md](09-service-specifications-torque-sst.md) | 219–228 | ✅ done |

**Alphabetical index:** [11a-alphabetical-index.md](11a-alphabetical-index.md) — a single
4A-FE index (this is a 4A-FE manual). The few entries the manual prints for the 4A-GE are
tagged `(4A-GE)` as incidental reference.

The alphabetical index (markdown + the copy baked into the PDF) is rebuilt with
`python scripts/08_append_index_pages.py manuals/toyota-4a-fe-repair/ --in-place`.

## Known scan gaps

`scripts/check_page_continuity.py` flags this scan as **abridged** — several sections'
page numbers skip (e.g. ST-2 → ST-15, EM has ~24 numbered pages missing). See
[10-needs-review.md](10-needs-review.md). Don't assume any section is complete.
