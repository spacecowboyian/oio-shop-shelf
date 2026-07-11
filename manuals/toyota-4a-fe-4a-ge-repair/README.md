# Toyota 4A-FE / 4A-GE Engine Repair Manual — Overview

*What this manual is, what it covers, and what it doesn't. Skim this first for bearings.*

> **Two kinds of information below, kept separate on purpose:**
> - **From the manual itself** (authoritative) — the title page, section list, and scope.
> - **Engine & vehicle background** (best-effort) — compiled from general automotive
>   knowledge (the repo's `auto-mechanic` skill + glossary) and public web sources, **not**
>   from this manual. It's here for orientation and **should be confirmed** before relying
>   on it. Better to have approximate context than none — but treat it as review-pending.

## The engines (background — review-pending)

Both are members of Toyota's **4A** family: 1.6 L (1587 cc), inline-4, **DOHC 16-valve**,
cast-iron block with an aluminum head.

- **4A-FE** — the economy/mainstream EFI version (the "E" line). ~105 hp / ~142 N·m in this
  era. Produced ~1987–2001. This is the engine this particular scan primarily documents
  (its VIN plate reads a 4A-FE, EU market, Sep. 1989).
- **4A-GE** — the performance version (the "G" line; Yamaha-developed head). The 1989-era
  16-valve made ~112–130 hp / ~149 N·m; later 20-valve versions made more. Higher-revving,
  wider valve angle than the 4A-FE.

**Vehicles (era-appropriate, best-effort):** 4A-FE — Corolla, Carina, Corona, Celica ST,
Camry (late '80s–'90s). 4A-GE — Corolla Levin / Sprinter Trueno (incl. AE86, AE92), Corolla
GT-S, MR2 (AW11). Exact model/chassis coverage for *this* book should be confirmed against
the vehicle it came with. *(Sources at the bottom.)*

## This specific manual (from the manual)

- **Title:** "Toyota 4A-FE, 4A-GE Engine Repair Manual", © 1989 Toyota Motor Corporation,
  Sep. 1989. This scan is a third-party "Auto College Aalborg — Special Edition" copy.
- **Scope: the ENGINE only** — not a whole-vehicle manual. 228 source pages.

### What it covers
| Section | | 
|---|---|
| Introduction | how-to-use, identification, general repair, abbreviations |
| Engine Mechanical | tune-up, compression, timing belt, cylinder head (4A-FE) |
| EFI System | fuel system, air induction, electronic control, sensors, ECU |
| Cooling System | water pump, thermostat, radiator, electric fan |
| Lubrication System | oil pump, oil pressure, oil & filter |
| Ignition System | Integrated Ignition Assembly (IIA) — **4A-FE** |
| Starting System | planetary-type starter |
| Charging System | alternator, IC regulator, drive belt |
| Service Specifications | specs, standard bolt torque, SST & SSM |

Full navigable contents + the split-per-engine alphabetical index are in
[`wiki/00-index.md`](wiki/00-index.md).

### What it does NOT cover
- **Non-engine systems** — transmission/transaxle, brakes, suspension, steering, body,
  HVAC, and vehicle-wide wiring are out of scope (this is an engine repair manual).
- **The 4A-GE ignition/EFI in full** — the ignition detail present is the **4A-FE** IIA;
  the 4A-GE's own ignition is not in this scan.
- **Completeness** — this scan is **abridged**: many pages are missing throughout (e.g.
  Engine Mechanical skips ~24 numbered pages; sub-procedures for the oil pump, alternator,
  and cylinder block are largely absent). See [`wiki/10-needs-review.md`](wiki/10-needs-review.md).

### Provenance caveats (important)
- Source PDF was **AES-encrypted**; decrypted with `qpdf` (no content altered).
- The cover carries a **bogus third-party "reduce all torque 40%" sticker** — it is **NOT
  Toyota's**; ignore it. Torque values in the wiki are Toyota's printed values, verbatim.
- Physical page order in the scan is **scrambled** relative to the section codes; the wiki
  keeps content in physical-page order so `[PDF p.N]` links stay correct.

## For AI assistants
Read [`wiki/llm-instructions.md`](wiki/llm-instructions.md), the repo root
`llm-instructions.md`, and `glossary.md`, and answer following the `auto-mechanic` rules.

## Sources (background section only)
- [Toyota A engine — Wikipedia](https://en.wikipedia.org/wiki/Toyota_A_engine)
- [Toyota 4A-FE specs — Specs Node](https://specsnode.com/engine-detail.php?id=77)
- [Toyota 4A-GE specs — Specs Node](https://specsnode.com/engine-detail.php?id=47)
- [The Toyota 4A Engine Family — CarBuzz](https://carbuzz.com/toyota-4age-engine-history-specifications/)
