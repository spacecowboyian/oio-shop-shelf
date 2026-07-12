# Toyota 18R / 18R-C / 18R-G Engine Repair Manual — Overview

*What this manual is, what it covers, and what it doesn't. Skim this first for bearings.*

> **A note on scope.** Unlike a single-engine manual, this book genuinely documents **three
> related engines** side by side: the base **18R**, the emission-controlled **18R-C**, and
> the twin-cam **18R-G**. Tune-up and engine-service sections are split per engine (separate
> 18R and 18R-G chapters); shared systems (lubrication, cooling, fuel, starting, ignition,
> charging) cover all variants with `(18R-G)`-tagged differences called out inline.

> **Two kinds of information below, kept separate on purpose:**
> - **From the manual itself** (authoritative) — the foreword, section index, and scope.
> - **Engine & vehicle background** (best-effort) — compiled from general automotive
>   knowledge (the repo's `auto-mechanic` skill + glossary) and public web sources, **not**
>   from this manual. Treat it as review-pending until confirmed.

## The engines (background — review-pending)

The **18R** is part of Toyota's **R family**: **1.968 L (1968 cc), inline-4, SOHC 8-valve**,
cast-iron block with an aluminum head, chain-driven cam — a workhorse pushrod-era-successor
truck/sedan engine produced roughly **1971–1982**.

- **18R** — base carbureted SOHC.
- **18R-C** — the **emission-controlled** variant (lower compression / emissions hardware for
  regulated markets); shares the SOHC bottom end.
- **18R-G** — the **performance twin-cam**: a **DOHC** head (Yamaha-developed) on the R block,
  twin sidedraft carburetors, higher-revving. The "G" line, analogous to the later 2T-G / 4A-GE.

**Vehicles (from the manual's own foreword):** Toyota **Celica, Corona, Cressida, Hi-Lux, and
HiAce** (image-verified against the foreword, [PDF p.3]). *(Sources at the bottom.)*

## This specific manual (from the manual)

- **Title:** "18R Engine Repair Manual — Includes 18R, 18R-C & 18R-G", © 1983 Toyota Motor
  Corporation.
- **Scope: the ENGINE(S) only** — not a whole-vehicle manual. **335 source pages** across 13
  sections (merged here from 13 separate per-section scan PDFs).

### What it covers
| Section | |
|---|---|
| General | repair instructions, abbreviations, symbols |
| Engine Tune-Up | separate **18R** and **18R-G** tune-up procedures |
| Engine Service | separate **18R** and **18R-G** service (cylinder head, timing, block) |
| Lubrication System | oil pump, oil circuit |
| Cooling System | water pump (with/without fluid-coupling fan), radiator, thermostat |
| Fuel System | fuel pump + carburetor (18R South-Africa / non-SA / 18R-G variants) |
| Starting System | starter disassembly, inspection, performance test |
| Ignition System | distributor (18R & 18R-G), coil, high-tension cord, spark plug |
| Charging System | alternator (incl. IC-regulator type), regulator |
| SST & Service Specifications | special service tools, standard bolt torque, per-engine specs |

Full navigable contents + the per-model alphabetical index are in
[`wiki/00-index.md`](wiki/00-index.md).

### What it does NOT cover
- **Non-engine systems** — transmission, brakes, suspension, steering, body, HVAC, and
  vehicle-wide wiring are out of scope (this is an engine repair manual).
- **Emission-control devices in detail** — the foreword defers these to separate emission-
  control repair manuals.

### Provenance caveats (important)
- **Source is 13 separate per-section scan PDFs** from a public Google Drive folder, merged
  in section order into one 335-page `source.pdf`. No content altered; only concatenated.
- **Not encrypted** — decrypt step was a no-op.
- **Heavy OCR noise expected.** This is a low-resolution 1983 scan; the raw text layer is
  badly garbled (figure callouts, torque tables, and specs are the worst hit). Cleanup will
  be substantial and every number must be cross-checked against the rendered page image.
- **Completeness pending** — run `check_page_continuity.py`; record any genuine gaps.

## For AI assistants
Read [`wiki/llm-instructions.md`](wiki/llm-instructions.md), the repo root
`llm-instructions.md`, and `glossary.md`, and answer following the `auto-mechanic` rules.

## Sources (background section only)
- [Toyota R engine — Wikipedia](https://en.wikipedia.org/wiki/Toyota_R_engine)
- Manual foreword (authoritative) for the vehicle list and engine variants.
