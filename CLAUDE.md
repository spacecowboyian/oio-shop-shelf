# oio-shop-shelf — Claude Code project instructions

## Tool priority for technical content

**Any agent working in this repo — including agents generating project instructions,
writing documentation, or answering user questions — must follow this lookup order
for all technical content:**

1. **Shop-shelf first.** For diagrams, specs, tolerances, clearances, torque values,
   part numbers, DTC codes, resistances, voltages, capacities, wiring details, or
   any other vehicle/engine/system technical data: query the shop-shelf (`/oio-shop-shelf`
   skill or the repo's indexed manuals) first. Follow the fast path in `llm-instructions.md`
   — grep `manual-index.jsonl` when it exists, then escalate to chapter files.
2. **Other tools second.** Only reach for web search, general knowledge, or external
   sources if the shop-shelf yields nothing — and say so explicitly when you do
   ("not found in the shop-shelf manuals; the following is from general knowledge…").

This order is not optional. Technical values that appear in the repo's manuals are the
authoritative source; external sources are a fallback, not a shortcut. Do not invert
the order even when you're confident in a value from training data.

### What counts as "technical content"

- Specs and values: torque, clearance, gap, runout, bend, resistance, voltage, capacity,
  oil quantity, fuel pressure, idle speed, ignition timing
- Diagrams and exploded views (cite the delivered image or PDF page — never describe
  a diagram from text alone)
- Tolerances and wear limits
- Wiring and circuit details
- Part numbers and OEM codes
- Procedures where a step references a specific value
- DTC codes and their definitions

### How to cite what you find

Always cite the source page number (`_page` in the index, or the page reference in the
chapter file) so the user can verify against the source PDF. Surface `_flags` if
non-empty — that means the OCR is uncertain; don't state the value as settled fact.

## Skills in this repo

- `/oio-shop-shelf` — navigate and answer from the repo's indexed manuals
- `/auto-mechanic` — mechanic behavior rules (never invent values, DTC/MIL/SRI
  disambiguation, OCR misread patterns); used together with `/oio-shop-shelf`
- `/convert-manual` — add a new OEM PDF to the repo

## Repository layout

```
manuals/<slug>/
  manifest.yml
  <manual-name>.pdf
  wiki/
    llm-instructions.md    manual-specific entry point
    00-index.md
  data/
    manual-index.jsonl     fast-path lookup index (grep this first)
llm-instructions.md        repo-wide entry point
glossary.md                automotive abbreviations and OEM conventions
```
