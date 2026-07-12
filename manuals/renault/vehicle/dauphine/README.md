---
# AUTO-GENERATED — taxonomy front matter (scripts/10_write_frontmatter.py); do not edit
slug: "renault-dauphine"
title: "Renault Dauphine / Ondine / Gordini Workshop Manual (M.R. 93)"
make: "Renault"
category: "vehicle"
models: ["Dauphine"]
chassis: ["R1090", "R1091", "R1093"]
engines: ["Ventoux (Type 670)"]
years: "1956-1967"
source_pdf: "https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/dauphine.pdf"
---

> 📄 **Source PDF** (hosted on GitHub Releases, not committed): [dauphine.pdf](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/dauphine.pdf)

# Renault Dauphine / Ondine / Gordini — Factory Workshop Manual (M.R. 93)

> Facts taken from the manual's own cover/contents pages are marked *(from manual)*;
> vehicle/engine background is best-effort context *(background — review-pending)*, **not**
> from the manual. For AI assistants answering from this manual, start at
> [`wiki/llm-instructions.md`](wiki/llm-instructions.md).

## What this manual is *(from manual)*

The **Renault M.R. 93 "Manuel de Réparation" / Workshop Manual**, English edition
(*Édition Anglaise*), **November 1964**, ref. `85 093 00 06`. Published by the Régie
Nationale des Usines Renault, Billancourt (France). It **supersedes** M.R.25, M.R.42,
M.R.45, M.R.55, M.R.58 and M.R.60 — i.e. it is the consolidated late-life factory manual
for the whole Dauphine family.

**Vehicles covered** *(from manual cover)* — Renault types:
- **R1090** — Dauphine (and the Ondine trim)
- **R1091** — Dauphine Gordini
- **R1093** — Dauphine "1093" (the competition/rally homologation model)

The scan is **479 pages**. The manual is a multilingual factory book (title/tab pages show
F · A · D · DK · E · It · NL · S); this is the **English** edition, so running text is
English, though some figure labels/tables may retain multilingual headings.

## Chapters *(from manual — the lettered tab index)*

Renault organizes by lettered chapter (skipping I and O), each cross-referenced to its
Renault workshop-section number(s):

| Tab | Chapter | Renault section(s) |
| --- | ------- | ------------------ |
| A | General (specifications, lifting points) | — |
| B | Engine | 14, 15, 16, 17, 73 |
| C | Clutch | 30 |
| D | Electrical equipment and ignition | 18, 62 |
| E | Gearbox (transmission case) | 31 |
| F | Braking system | 34 |
| G | Steering | 40 |
| H | Front axle | 42 |
| J | Rear axle | 43 |
| K | Wheels — Hubs | 44 |
| L | Suspension / shock absorbers | 51 |
| M | Bodywork | 50, 81, 82, 84, 85 |
| N | Heater | — |
| P | Special Tools | — |

This is a **whole-vehicle** manual: it covers engine, driveline, chassis, brakes,
steering, electrical, body and heater. Chapter A carries the general vehicle
specifications (per-year/per-model) and lifting points.

## Sample specifications *(from manual, Chapter A, "models previous to 1960")*

| Spec | Value |
| ---- | ----- |
| Overall length | 3.945 m (155 5/16 in) |
| Overall width | 1.520 m (59 13/16 in) |
| Height, unladen | 1.440 m (56 11/16 in) |
| Wheelbase | 2.270 m (89 3/8 in) |
| Front / rear track | 1.250 m / 1.220 m |
| Ground clearance | 0.150 m (5 29/32 in) |
| Kerb weight | 630 kg (1387 lb) |
| Max laden weight | 1,000 kg (2202 lb) |
| Turning circle radius | 4.55 m (14 ft 11 in) |

Chapter A gives separate spec blocks for pre-1960, 1960, and 1961 models, plus 1961
Ondine, 1960–61 Dauphine Gordini, 1961 Gordini, and the R1093.

## Background *(review-pending — NOT from the manual)*

- The **Renault Dauphine** (1956–1967) is a rear-engine, rear-wheel-drive economy saloon,
  successor to the 4CV. Engine: the **"Ventoux"** OHV inline-four, ~845 cc, mounted in the
  rear. **Gordini** versions are tuned; the **R1093** is the competition homologation car.
- **Ondine** was a higher-trim Dauphine badge.
- Relevant to Ian's car **"Geoffrey"** — a 1962 Dauphine (R1090).

## Provenance / caveats

- **Source:** contributor's own PDF (Google Drive), 14 MB, 479 pp, unencrypted, English
  edition. Original © Renault; no license sought — committed under this repo's considered-
  risk posture (see [CONTRIBUTING.md](../../../../CONTRIBUTING.md)).
- **OCR note:** the source has a sparse non-content text layer (a stray Helvetica
  annotation font) that fooled the pipeline's text-layer detector into skipping OCR on the
  first pass; it was re-run with `--force`. Real page text comes entirely from OCR of the
  scan — expect the usual OCR-uncertainty flags in `10-needs-review.md`.
- First **non-Toyota make** in the repo — exercises the taxonomy end to end (`renault`
  added to `manuals/taxonomy.yml`, vPIC Make_ID 13647).
