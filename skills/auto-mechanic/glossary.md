<!-- Bundled copy for the auto-mechanic Skill, so it works standalone even if only this
     skill folder is installed. Canonical/most current version lives at the repo root:
     https://github.com/spacecowboyian/oio-shop-shelf/blob/main/glossary.md
     If you're working inside a full oio-shop-shelf clone, prefer that copy. -->

# Automotive repair terminology & OEM manual conventions

**Read this before answering any question that draws on a manual in `manuals/`.** The
wiki files are a faithful OCR transcription of the source PDF — but transcription alone
doesn't tell you what a term, abbreviation, or table layout *means*. This file supplies
that missing domain context, the same way `llm-instructions.md` supplies navigation
context.

This file follows the same honesty rule as the manuals themselves: nothing here is
asserted with more confidence than the sourcing supports. Entries backed by a primary
standard or a directly-quoted manual example are stated plainly. Entries that are
commonly described a certain way but weren't independently re-verified against a primary
source in this pass are flagged `<!-- NEEDS REVIEW -->`, same convention as
`10-needs-review.md` in each manual. Don't upgrade a flagged entry to fact without
checking the cited primary source yourself.

*Compiled 2026-07-10 via multi-source research (SAE standards, a peer-reviewed OCR-error
study, and cross-model Toyota factory service manuals). See "Sources" at the end.*

## The governing standard: SAE J1930

Most powertrain/diagnostic abbreviations in modern (post-OBD-II-era) OEM manuals trace
back to **SAE J1930** — "Electrical/Electronic Systems Diagnostic Terms, Definitions,
Abbreviations, and Acronyms" (first issued 1988-06; the APR2002 revision is equivalent to
ISO/TR 15031-2). It exists specifically to standardize terminology that had proliferated
inconsistently across manufacturers, and its stated scope names diagnostic, service and
repair manuals, bulletins, training manuals, and repair databases as target applications
— i.e., it is the correct authority to point to for *why* a manual uses one term instead
of a dozen synonyms.

Full text: [archive.org OCR transcription](https://archive.org/stream/gov.law.sae.j1930.1993/sae.j1930.1993_djvu.txt) · [CFR-incorporated PDF via law.resource.org](https://law.resource.org/pub/us/cfr/ibr/005/sae.j1930.2002.pdf)

Two things worth knowing about citing it:
- J1930 has been revised multiple times since 1988 (later revisions exist through at
  least 2024). The research behind this file examined the **1993 / APR2002** text
  specifically — exact acronym mappings can shift between revisions, so treat this as
  "consistent with J1930 as of that text," not "current as of whatever revision a given
  manual's publication date implies."
- Its full text is freely retrievable but is not under an explicit open-reuse license —
  treat it as a citable authority, not a source to copy wholesale.

**Verified from the primary text:** J1930's Table 1 ("Cross-Reference and Look-Up")
standardizes "Diagnostic Trouble Code" to the acronym **DTC**, and deliberately splits the
ambiguous shop phrase "Check Engine" (and its synonym "Service Engine Soon") into two
distinct terms depending on function:

| Ambiguous shop term | Standardized term | Acronym | Meaning |
|---|---|---|---|
| "Check Engine" light (diagnostic) | Malfunction Indicator Lamp | **MIL** | The emissions/diagnostic warning light — comes on for a fault the OBD system detected |
| "Check Engine" light (maintenance) | Service Reminder Indicator | **SRI** | A scheduled-maintenance reminder — not a fault indicator |

If a manual or a user says "check engine light," don't assume which one is meant — ask,
or check which condition the manual describes triggering it.
([source](https://law.resource.org/pub/us/cfr/ibr/005/sae.j1930.2002.pdf))

## Common abbreviations

Widely-used industry abbreviations, consistent with J1930-era standardization. These are
in near-universal use across manufacturers and predate/postdate any single manual.

**Engine control & sensors**
| Abbr. | Meaning |
|---|---|
| ECU | Electronic Control Unit — general term for any onboard computer |
| ECM | Engine Control Module |
| PCM | Powertrain Control Module (ECM + transmission control, on vehicles that combine them) |
| MAP | Manifold Absolute Pressure (sensor) |
| MAF | Mass Air Flow (sensor) |
| IAC | Idle Air Control (valve) |
| EGR | Exhaust Gas Recirculation |
| TPS | Throttle Position Sensor |
| VSS | Vehicle Speed Sensor |
| VSV | Vacuum Switching Valve |
| DTC | Diagnostic Trouble Code |
| MIL | Malfunction Indicator Lamp (see table above) |

<!-- NEEDS REVIEW: this table's entries are standard, ubiquitous industry usage and are almost certainly correct, but the specific claim that J1930's Table 1 defines this exact bundled list (as opposed to being general automotive knowledge) did not survive adversarial verification in this research pass (voted 1-2) -- if a manual's usage of one of these ever seems inconsistent with the definition here, re-check against the primary J1930 text directly rather than assuming this table is J1930-sourced verbatim. -->

**Tools & procedures**
| Abbr. | Meaning |
|---|---|
| SST | Special Service Tool — a manufacturer-specific tool required for a procedure, always called out by name/part number in the manual |
| TDC | Top Dead Center — piston at the top of its stroke |
| BTDC | Before Top Dead Center |
| ATDC | After Top Dead Center |
| OHC | Overhead Camshaft |
| DOHC | Double Overhead Camshaft |
| SOHC | Single Overhead Camshaft |
| EFI | Electronic Fuel Injection |
| OEM | Original Equipment Manufacturer |

## Systems & components (quick orientation)

If you're unfamiliar with a chapter's subject, this is the one-line map:

- **Ignition system** — spark generation and timing: coil, distributor (older engines),
  spark plugs, igniter.
- **Charging/starting system** — alternator, battery, starter motor, voltage regulation.
- **Cooling system** — radiator, water pump, thermostat, coolant passages.
- **Lubrication system** — oil pump, oil passages, filter, pressure specs.
- **Fuel/EFI system** — injectors, fuel pump, pressure regulator, throttle body, the
  sensors listed above feeding the ECU/ECM.
- **Engine mechanical** — the block, head, valvetrain, timing belt/chain, pistons,
  bearings — the structural/mechanical half of the engine as opposed to its control
  electronics.
- **Diagnostic trouble codes (DTC)** — codes use a **P**owertrain / **C**hassis /
  **B**ody / **U**network prefix letter, e.g. P0301 (cylinder 1 misfire). This top-level
  P/C/B/U categorization is well-established and safe to rely on.
  <!-- NEEDS REVIEW: a more specific claim -- that the SECOND digit distinguishes ISO/SAE "core" generic codes (2nd digit 0) from manufacturer-specific codes (2nd digit 1 or 2) -- is commonly described this way, but the specific source checked in this research pass (SAE J2012 CFR text) did not confirm the claim as phrased (voted 0-3). The general P/C/B/U prefix meaning is solid; don't treat the second-digit generic-vs-manufacturer rule as confirmed without checking SAE J2012 / ISO 15031-6 primary text directly. -->

## Units & measurement conventions

| Quantity | Units you'll see | Notes |
|---|---|---|
| Torque | N·m (SI), kgf·cm (legacy metric), ft·lbf / ft.·lbf (imperial), in.·lbf / in·lbf (imperial, small values) | Toyota FSMs commonly show N·m / kgf·cm / ft·lbf side by side in one table row for a single spec, and for small torque values show in.·lbf instead of a fractional ft·lbf number. This is a **commonly observed pattern**, not a universally fixed rule with an exact numeric cutoff — the specific claim of "~9-10 N·m is the threshold" did not survive verification (voted 1-2). Don't state a precise cutoff; just recognize the pattern when you see it. |
| Clearance / gap | mm (metric), in. (imperial) | |
| Electrical resistance | Ω (ohm) | See OCR misread note below — Ω is frequently misread as the digit "2" |
| Torque-to-yield fasteners | numeric torque + turn angle, in two rows | See below |

**Torque-to-yield / multi-step tightening.** Head bolts, main bearing caps, and
connecting rod caps are frequently tightened in two steps: a numeric torque value, then
an additional **turn angle** rather than a second torque number. A real Toyota FSM
example: `Cylinder head sub-assembly x Cylinder block sub-assembly / 1st: 36 N·m (367
kgf·cm, 27 ft·lbf) / 2nd: Turn 180°`. If you see a "1st" torque row followed by a "2nd"
row that says "Turn N°" instead of a number, that's this convention — don't try to
interpret the 2nd row as a torque value.
([source](https://toyotamanuals.gitlab.io/RM01J1E/htmlweb/rm01j1e/rm/rm821e/m_03_0048.pdf))

## OCR misread patterns (beyond Ω→"2")

If you're reading OCR'd/scanned manual text, these patterns are worth knowing before
treating an odd-looking value as an error in the original rather than an artifact of the
scan. From a peer-reviewed study of OCR error behavior on degraded documents
([Lopresti, Lehigh University, IJDAR](https://www.cse.lehigh.edu/~lopresti/tmp/AND08journal.pdf)):

- **Ω (ohm) → "2"** — the most common symbol-specific misread in this domain.
- **Character-shape substitutions**: `l → i`, `h → li` (or `h → l1`), `rn → m` — driven
  by ink darkening/smearing on photocopied originals. Watch for these especially in part
  numbers and abbreviations, where a substitution changes meaning rather than just
  looking odd.
- **Space deletion**: e.g. "of the" → "ofthe".
- **Space insertion**: e.g. "project" → "pro ject".
- **Punctuation is disproportionately unreliable** — in the cited study, punctuation
  recognition precision was only ~0.80 even on a dataset where overall character
  accuracy was ~99.3%. A missing or wrong comma/period/parenthesis is far more likely to
  be an OCR artifact than a missing/wrong digit or letter.

None of this is license to silently "correct" anything — flag what looks wrong, don't
guess at a fix.

## What wasn't found / open gaps

- **Diagnostic flowchart notation** (symbols/conventions used in troubleshooting
  flowcharts) — not researched. If a manual's flowchart uses a symbol or convention that
  isn't self-explanatory, say so rather than guessing at a standard meaning.
- **DTC second-digit convention** (generic/core vs. manufacturer-specific) — see the
  flagged note above; needs a primary-source recheck against current SAE J2012 / ISO
  15031-6 text.
- Verified torque-table/DTC examples above are cross-corroborated from multiple Toyota
  models (FJ Cruiser, Corolla, RAV4/Camry) — the pattern generalizes well within Toyota
  but hasn't been independently confirmed for every manufacturer.

## Existing resources evaluated (why this file exists instead of reusing one)

- **ASE Glossary of Automotive Terminology** ([PDF](https://www.asepractice.com/PDF/ASE_Glossary.pdf)) — a bilingual
  English/Spanish **term-translation list** (e.g. "backfire" → "contra explosión"), not a
  definitional glossary, and carries no reuse license. Not usable as a source to copy from.
- **Wikipedia — Glossary of automotive terms** ([link](https://en.wikipedia.org/wiki/Glossary_of_automotive_terms)) — CC BY-SA 4.0. Reusable
  with attribution + share-alike, not a clean drop-in without triggering those
  obligations — used as a reference to write original definitions from, not copied
  verbatim.
- **OBDII.DTC** ([GitHub, lennykean/OBDII.DTC](https://github.com/lennykean/OBDII.DTC)) — genuinely MIT-licensed, a reusable
  dataset of generic (non-manufacturer-specific) DTC codes with descriptions, organized
  by the P/C/B/U prefix convention. Worth pulling in directly for a full DTC lookup
  table if a project ever needs one.
- **Existing Claude Skills / GPTs for automotive work** — an "Automotive Expert" Claude
  Skill and a GitHub "automotive-skills-suite" exist, but both target connected-vehicle
  software, fleet/telematics, ADAS, and functional-safety compliance standards, not
  reading OEM repair manuals or general diagnosis. GPT Store has several consumer-facing
  "Auto Mechanic GPT" chatbots, but they're closed/proprietary with nothing to reuse.

## Sources

- [SAE J1930 — full OCR text (archive.org)](https://archive.org/stream/gov.law.sae.j1930.1993/sae.j1930.1993_djvu.txt)
- [SAE J1930 (APR2002) — CFR-incorporated PDF (law.resource.org)](https://law.resource.org/pub/us/cfr/ibr/005/sae.j1930.2002.pdf)
- [SAE J1930 — mirrored copy (Maserati tech-info portal)](https://techinfo.maserati.com/tch/resources/doc/j1930_200204.pdf)
- [Toyota FSM torque-table example (toyotamanuals.gitlab.io)](https://toyotamanuals.gitlab.io/RM01J1E/htmlweb/rm01j1e/rm/rm821e/m_03_0048.pdf)
- [Toyota FJ Cruiser FSM torque-table example (purefjcruiser.com)](https://www.purefjcruiser.com/docs/2007%20Toyota%20FJ%20Cruiser%20Repair%20Manual/Service%20Specifications/1GR-FE%20Engine%20Mechanical/003000.pdf)
- [Lopresti, "OCR Errors and Their Effects on Natural Language Processing" (Lehigh University, IJDAR)](https://www.cse.lehigh.edu/~lopresti/tmp/AND08journal.pdf)
- [ASE Glossary of Automotive Terminology](https://www.asepractice.com/PDF/ASE_Glossary.pdf) — evaluated, not reused
- [Wikipedia — Glossary of automotive terms](https://en.wikipedia.org/wiki/Glossary_of_automotive_terms) — evaluated, used as reference only
- [OBDII.DTC (GitHub)](https://github.com/lennykean/OBDII.DTC) — evaluated, not currently integrated
