# Instructions for the AI assistant — Alpine A110 (Type A 110, 1st edition October 1970)

You have the **ALPINE A110 factory repair manual**, 1st edition October 1970, plus its
**October 1971 update supplement** — covering types **1300 VA · 1300 VB · 1300 VC · 1600 VB**
and the **GS** competition engine option. Read this file before answering from the manual.

> **Fetch-only agent (no shell / no GitHub MCP)?** Don't browse the folder — every file is
> listed as an absolute raw URL in [`all-files.md`](all-files.md). See the repo-root
> [`llm-instructions.md`](../../../../../llm-instructions.md) for why `/tree/` browsing fails.

## READ THIS FIRST — this manual is a machine translation, and it is damaged

This copy is an **English machine translation of the French original**, and the translation
is poor. That changes how you must answer from it:

1. **Never state a value from this manual as settled fact.** Give the value, cite the PDF
   page, and say it comes from a machine-translated scan that should be checked against the
   source PDF page before the user touches the car.
2. **French decimal commas are rendered inconsistently as periods.** The same dimension
   appears as both `3.850` and `3.85 m` on one page. A number that looks off by a factor of
   ten or a hundred is usually this, not a real value.
3. **Several pages are illegible and were NOT transcribed** — see "Images only" below. Do not
   invent data for them.
4. **The translator sometimes emitted an apology** ("I'm sorry.", "That's right.", "You're a
   biante.") where the French text continued. Those gaps are marked in the chapters and are
   genuinely unrecoverable from this copy.
5. **The supplement supersedes the manual.** Always check
   [`u1`](u1-supplement-general-engine-electrical.md) and
   [`u3`](u3-supplement-steering-brakes.md) before quoting a Chapter A/B/C/D/E/G/H/J/L/M/N
   value — several are explicitly corrected there (pushrod lengths, cooling capacity, air
   corrector jet, distributor references, damper and axle types).

## Fast path — a specific value (do this FIRST)

Grep the flat lookup index **[`../data/manual-index.jsonl`](../data/manual-index.jsonl)** —
one JSON row per fact across the whole manual, from both spec tables and prose. Read the
matching row, cite its `_page`, and **if `_flags` is non-empty, surface that uncertainty**.

**Grep the manual's term, not the user's words — and here that means the MISTRANSLATED term.**
This manual's vocabulary is the single biggest obstacle to finding anything. Use this table
before you grep:

| User says | This manual prints | French original |
| --------- | ------------------ | --------------- |
| ignition | **"lighting"** | allumage |
| spark plug | **"candle"** | bougie |
| distributor | **"lighter"**, "allower" | allumeur |
| flywheel | **"steering wheel"** | volant |
| connecting rod | **"believe"**, "bial" | bielle |
| rocker arm | **"cultivator"** | culbuteur |
| pushrod | "tige/shaft of buttocks" | tige de culbuteur |
| valve seat | **"litter"**, "steel" | siège de soupape |
| castor | **"hunting"** | chasse |
| camber | **"carrossing"**, "bodywork" | carrossage |
| toe-in / toe-out | **"clamps"/"pinching"** / **"opening"** | pincement / ouverture |
| stub axle / upright | **"rocket"**, "rocket door" | fusée / porte-fusée |
| gearbox | **"box of vitses"**, "B.V." | boîte de vitesses |
| clutch | "embrayage" (untranslated) | embrayage |
| shim | **"hold"** | cale |
| spring | **"resent"**, "resort" | ressort |
| damper | **"amorist"**, "major" | amortisseur |
| brakes | **"breins"** | freins |
| brake pad | **"platelet"**, "plate" | plaquette |
| proportioning valve | **"splitter"** | répartiteur |
| final drive pair | **"torque"** (NOT a tightening torque!) | couple |
| rear screen | **"AR bezel"** | lunette AR |
| roof | **"flag"**, "pavillon" | pavillon |
| wiring harness | **"failures"** | faisceaux |
| starter | **"demarrier"** | démarreur |
| front / rear | **AV / AR** | avant / arrière |
| left / right | **G / D** | gauche / droite |
| lacquer | **"lake"** | laque |

Also watch the standard OCR patterns (`Ω`→"2", `l`↔`1`↔`I`, `±`→`:` or `$` or `^` or `*`,
degree sign → `o`). See [`glossary.md`](../../../../../glossary.md) and the `auto-mechanic`
skill.

## What's in this bundle

- `00-index.md` — chapter list with page ranges.
- **12 lettered chapters** mirroring the manual's own tabs (the factory skips F, I, K, O, P, Q):
  `a-general` · `b-engine-ignition` · `c-electrical-equipment` · `d-clutch` · `e-gearbox` ·
  `g-steering` · `h-front-axle` · `j-rear-axle` · `l-suspension-shock-absorbers` ·
  `m-braking-system` · `n-bodywork` · `r-special-tooling`.
- **5 supplement chapters** (`u1`…`u5`) — the October 1971 additive, bound after the manual.
  **These win over the main manual.**
- `09-quick-reference.md` — harvested spec values linked to their source page.
- `10-needs-review.md` — **92 flags**, triaged into a ranked worklist (see `../TRIAGE.md`). Unusually many, and that is the point: this manual
  earns them. Read the flag before quoting the value it sits next to.
- `11a-alphabetical-index.md` — generated from headings.
- The source PDF (on the Release) — the authority for anything visual, and the thing to check
  whenever a value matters.

## Diagrams ARE delivered here — surface them

**26 pages** are rendered to WebP images, registered in `manifest.yml`'s `diagrams:` block and
embedded at their citation point in the chapters. Prefer the delivered image; fall back to
citing the PDF page only when a needed figure is not in `diagrams:`.

Two kinds of entry:

**Genuine diagrams** — the Version 85 wiring diagram (p.29), the timing chain arrangement
(p.20), the ignition advance curves (pp.25 and 63), the general dimension drawing (p.7), the
castor-measuring flags (p.44), the screen-seal drawings (p.82) and the tool drawings
(pp.84–87).

**Pages that are "images only" because no faithful transcription is possible.** On these the
English overlay sits at 90° across the French original and destroys both:

| Page(s) | What it is | Where |
| ------- | ---------- | ----- |
| 31 | **The entire clutch characteristics table (D-1)** | [`d-clutch.md`](d-clutch.md) |
| 35–36 | **Gearbox ratio / final-drive / cone-distance columns (E-2, E-3)** | [`e-gearbox.md`](e-gearbox.md) |
| 57, 76 | Table 2 — lacquer compositions | [`n-bodywork.md`](n-bodywork.md), [`u4`](u4-supplement-bodywork-paint.md) |
| 64–72 | **The whole 9-page wiring harness and connector directory** | [`u2`](u2-supplement-wiring-harness-directory.md) |

If a user asks for a clutch part number, a gearbox ratio or a harness connector, **say the
page is illegible in this copy and give them the image / PDF page** — do not reconstruct it.
Readable substitutes exist for two of these: clutch part numbers for the 85 / 1300 G / 1300 S
are in [`u3`](u3-supplement-steering-brakes.md#chapter-d-clutch-embrayage), and the BV 364
ratios are in [`u3`](u3-supplement-steering-brakes.md#chapter-e-gearbox-boîte-de-vitesses).

Do **not** paraphrase a safety-relevant diagram (ignition advance curve, wiring, alignment
jig) from memory.

## This manual is NOT self-contained

Section R says so outright: apart from one spark-plug wrench for the 1600 S, the tooling and
much of the mechanical content is Renault's. The manual repeatedly hands you off:

| For | Go to |
| --- | ----- |
| Engine internals, version 85 | **MR 131** (R. 1192) |
| Engine internals, 1300 G / 1300 S | **MR 133** (R. 1135) |
| Engine internals, 1600 S | **MR 96** (R. 1151) |
| Gearboxes 330-06 / 330-08 | **MR 131** |
| Gearboxes 353 / 364 | **MR 133** (R 1135) |
| Steering overhaul | **MR 68** |
| Front axle overhaul | **MR 68** or **MR 131** |
| Rear axle, suspension, brakes overhaul | **MR 133**, chapters J / L / M |
| Chassis checking | **MR 131**, chapter N |
| Front-axle alignment preliminaries | **MR 101**, fascicle G 100 |
| Body / parts plates | **PR 871** |

None of those are in this repo. Say so rather than improvising.

## The scan is abridged

Pages **B-1, J-1, L-2+, M-1, N-6 … N-13** and anything after **G-1**, **E-4**, **R-1** are
simply absent. The supplement cites page N-13, so it existed. If a user asks for something
that would live in a missing page, say it is missing from this scan — see
[`10-needs-review.md`](10-needs-review.md).

## Which version is the user's car?

Always pin this down before quoting a value — almost every table in this manual has five
columns and they differ:

| Version | Type | Engine |
| ------- | ---- | ------ |
| 85 | 1300 VC | 810-30 |
| 1300 G | 1300 VA | 812-00 (see flag) |
| 1300 S | 1300 VB | 812-00 derived (see flag) |
| 1600 S | 1600 VB | 807-25 |
| 1600 GS | — (option) | competition |

The **1300 G / 1300 S engine codes are contradictory in the source** — see the flag in
[`a-general.md`](a-general.md#a-2-general-characteristics). Many changes are also keyed to a
**vehicle or bodywork number** (2162, 4500, 11779, 11872, 11912, 12037, 12249, 16951), so ask
for it when the answer depends on one.
