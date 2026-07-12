---
# AUTO-GENERATED — taxonomy front matter (scripts/10_write_frontmatter.py); do not edit
slug: "toyota-4a-fe-4a-ge"
title: "Toyota 4A-F / 4A-GE Engine Service & Maintenance Manual"
make: "Toyota"
category: "engine"
engines: ["4A-F", "4A-GE"]
---

# Toyota 4A-F / 4A-GE Engine Service & Maintenance Manual — Overview

*What this manual is, what it covers, and what it doesn't. Skim this first for bearings.*

> **This is the repo's reference/worked-example manual.** Its `wiki/` was produced by the
> original hand transcription (the 16-subagent cleanup pass, ported from Brains) — it's the
> gold-standard the `convert-manual` pipeline generalizes from. It is a **distinct** manual
> from [`../toyota-4a-fe-repair/`](../toyota-4a-fe-repair/README.md): that one is the **4A-FE
> Engine Repair Manual** (228 pp); this one is the **4A-F / 4A-GE Service & Maintenance
> Manual** (219 pp).

> **Two kinds of information below, kept separate on purpose:**
> - **From the manual itself** (authoritative) — the title, section list, and scope.
> - **Engine & vehicle background** (best-effort) — compiled from general automotive
>   knowledge (the repo's `auto-mechanic` skill + glossary) and public web sources, **not**
>   from this manual. Treat it as review-pending until confirmed.

## The engines (background — review-pending)

Both engines are members of Toyota's **4A** family: **1.6 L (1587 cc), inline-4, DOHC
16-valve**, cast-iron block with an aluminum head, produced ~mid-1980s–1990s.

- **4A-F / 4A-FE** — the economy/mainstream DOHC line (the "F"/"FE" designation; FE is the
  EFI version, ~105 hp / ~142 N·m in this era).
- **4A-GE** — the **performance twin-cam** sibling (the "G" line; Yamaha-developed head,
  higher-revving) used in the Corolla GT-S / Levin / Sprinter Trueno (AE86) and MR2 (AW11).

**Per-engine tagging within the manual is review-pending** — the wiki does not yet
consistently mark which specs/procedures are 4A-F vs 4A-GE. Confirm the exact engine before
relying on a spec where the two differ. *(Sources at the bottom.)*

## This specific manual (from the manual)

- **Title:** "Toyota 4A-F / 4A-GE Engine Service & Maintenance Manual", © Toyota Motor
  Corporation.
- **Scope: the ENGINE only** — not a whole-vehicle manual. **219 source pages**, with a
  full **EFI** section (this manual is EFI-era: it has electronic fuel injection, DTC tables,
  and sensor/troubleshooting coverage).

### What it covers
| Section | |
|---|---|
| Preparation | SST & service materials |
| Service Specifications | torque, standard bolt, service limits |
| Charging System | alternator, IC regulator, drive belt |
| Engine Mechanical | inspection, timing belt, cylinder head, cylinder block |
| Ignition System | distributor / IIA, timing |
| Lubrication System | oil pump, oil pressure, oil & filter |
| Cooling System | water pump, thermostat, radiator |
| EFI System | system/diagnosis basics, **DTC tables**, troubleshooting, fuel pump / regulator / injector, throttle body, sensors / relays / VSV / fuel-cut |

Full navigable contents + the ~970-entry alphabetical index (split `11a`–`11d`) are in
[`wiki/00-index.md`](wiki/00-index.md).

### What it does NOT cover
- **Non-engine systems** — transmission/transaxle, brakes, suspension, steering, body,
  HVAC, and vehicle-wide wiring are out of scope (this is an engine manual).

### Provenance caveats (important)
- **Hand-transcribed reference.** The `wiki/` here is a faithful hand transcription ported
  from Brains — not the raw pipeline output. It's the quality bar new manuals aim at.
- **Source PDF** is committed alongside this manifest, and also mirrored on Google Drive
  (links in `wiki/00-index.md`); `[PDF p.N]` markers link straight to the source page.
- **Per-engine (4A-F vs 4A-GE) attribution** is not yet consistently tagged — see the
  background note above. Tracked with the multi-model indexing work in
  [issue #9](https://github.com/spacecowboyian/oio-shop-shelf/issues/9).

## For AI assistants
Read [`wiki/llm-instructions.md`](wiki/llm-instructions.md), the repo root
`llm-instructions.md`, and `glossary.md`, and answer following the `auto-mechanic` rules.

## Sources (background section only)
- [Toyota A engine — Wikipedia](https://en.wikipedia.org/wiki/Toyota_A_engine)
- Manual title/section list (authoritative) for scope and coverage.
