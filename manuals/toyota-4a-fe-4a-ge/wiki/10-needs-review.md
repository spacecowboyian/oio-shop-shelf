# Needs Your Attention — Master Review List

This file consolidates every place across the manual where OCR cleanup left content ambiguous rather than guessing. Nothing numeric (torque, clearance, resistance, voltage, part numbers) was ever altered or deleted anywhere in this manual — when a number looked wrong, it was flagged here, not "corrected." Diagrams/exploded views/wiring charts are never reproduced as text; when a flag says "diagram," the fix is to open the source PDF at that page, not to expect prose here.

Priority items — worth checking against another copy of the manual if you rely on these:

- **[p.20](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=20) (Service Specifications)** — main bearing journal U/S 0.25 diameter range reads `47.745 – 47.555 mm`, upper value smaller than lower. Near-certain digit swap. **Corroborating value found 2026-07-11:** an independent, unflagged listing of the same spec at [p.95](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=95) (`04d-engine-mechanical-cylinder-block.md#p95`) reads `47.745–47.755 mm` — internally consistent, matches its own inch conversion. Likely the correct reading, but verify against the source PDF before relying on either.
- **[p.29](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=29) (Service Specifications, charging/alternator torque table)** — 6 rows (drive end frame, rectifier holder, pulley nut, etc.) have garbled kgf-cm/ft-lbf conversions. The N·m values are intact; the converted columns aren't.
- **[p.32](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=32) (Charging System)** — "Drive belt tension:" and "Drive belt deflection:" specs may be swapped (mm figures under tension, N figures under deflection — backwards from convention). Could lead to the wrong spec being applied to the wrong check.
- **[p.32](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=32) (Charging System)** — "98 N (10 kgf, 288 lbf)" — 10 kgf ≈ 22 lbf, not 288. Likely stray digit.
- **[p.66](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=66) (Engine Mechanical)** — cylinder head bolt loosening sequence/pattern is a diagram, OCR unreadable. Safety-relevant (head warpage) — go straight to the PDF page for this one.
- **[p.104](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=104) vs [p.108](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=108) (Ignition System)** — primary coil resistance possibly conflicts: `0.96-0.55` in a troubleshooting flowchart vs. `0.36-0.55` stated cleanly elsewhere. Not reconciled.
- **[p.130](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=130) (Lubrication System)** — water pump heating spec reads "8.°C (185°F)" — 185°F ≈ 85°C, not 8°C. Likely dropped digit on the Celsius side.

Everything else, by chapter:

## 01-preparation.md
- [p.3](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=3) — `(09201-01050)` sub-item: trailing "5" unclear, may be garbled "Set."
- [p.3](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=3) — `09636-20010` Upper Ball Joint Dust Cover Replacer: trailing "7" unclear.
- [p.11](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=11) — EQUIPMENT list "299er insulation resistance meter" — possibly "Megger" (real brand), not confident.
- [p.13](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=13) — SST `09286-46011` area: "end frame" / "Rectifier" / "Puller" notes appear column-jumbled.

## 02-service-specifications.md
- [p.16](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=16) — "HOW TO DETERMINE BOLT STRENGTH" chart: mark-to-class column pairings scrambled by OCR, left as a block.
- [p.17](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=17) — 6mm/hex-head-8-N·m row in SPECIFIED TORQUE FOR STANDARD BOLTS shows garbage instead of a number.
- [p.20](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=20) — see priority list above (journal diameter inversion).
- [p.24](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=24) — "Throttle valve fully closed" resistance row: stray "2" before the VTA-E2 value, unclear if part of it.
- [p.28](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=28) — starter no-load rpm spec split across broken lines, probably "3,000 rpm or more" but ambiguous.
- [p.29](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=29) — see priority list above (charging torque table).

## 03-charging-system.md
- [p.32](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=32) — battery terminal check: "not loose or cory" cut off, likely "corroded."
- [p.32](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=32) — belt tension/deflection swap + 288 lbf value — see priority list.
- [p.33](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=33) — IC regulator/alternator voltage check passage badly garbled, meaning inferable but not confidently readable.
- [p.33](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=33) — "heater biewer »eatin a" — likely "heater blower switch in" position "HI."
- [p.35](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=35) — "one-half of atu." in a NOTICE about the rotor shaft — likely "one-half of a turn."
- [p.38](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=38) — SST reference `SST 09950-60010 (09951-00260, 099527` — truncated, no closing paren, digits untouched.

## 04-engine-mechanical.md
- [p.66](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=66) — see priority list above (head bolt loosening sequence).
- [p.100](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=100) — connecting-rod-cap install sequence: step marker reads `tb)` where `(b)` expected, torque-adjacent.

## 05-ignition-system.md
- [p.103](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=103) — TOC dot-leaders for "IGNITION SYSTEM" (IG-1) and "DISTRIBUTOR" (IG-7) unreadable noise, section names/codes legible.
- [p.104](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=104) — see priority list above (resistance conflict) — full "Spark Test does-not-occur" flowchart left intact around it.
- [p.107](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=107) — NOTICE on spark plug gap adjustment truncated mid-word.
- [p.107](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=107) — "allow it tq" — likely missing "dry."
- [p.109](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=109) — reassembly step list: step numbers appear out of order (6, 8, 7), structure uncertain.
- [p.110](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=110) — fragment `Lae 27.8)` on distributor diagram — could be a torque value or page cross-ref, left untouched.
- [p.111](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=111) — removal step (a) cut off after "pull out the dig," step (b) has no visible text.
- [p.111](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=111) — rotor-install alignment sentence has a gap mid-sentence.

## 06-lubrication-system.md
- [p.115](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=115) — used-oil safety/disposal caution paragraph heavily garbled.
- [p.115](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=115) — "drain the oil into acon k. / er." — step 1b garbled after "drain the oil into."
- [p.115](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=115) — REPLACE OIL FILTER steps (b)-(e) garbled/truncated with stray digits.
- [p.118](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=118) — legend "Vonifgusable part" — likely "Non-reusable part," not confirmed.
- [p.119](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=119) — "remove the oil puon" — unclear if garble of "pump."
- [p.121](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=121) — "purhg marks" — likely "punch marks."
- [p.121](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=121) — "Install the oil pump body cover with the.¢" — object of sentence missing.
- [p.121](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=121) — "retainey re / body hole" — likely "retainer into the pump body hole."
- [p.121](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=121) — "install the snap" — truncated, likely missing "ring."
- [p.121](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=121) — "cylinder biggaTM" — likely "cylinder block."
- [p.121](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=121) — INSTALLATION step (b) has no text.
- [p.121](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=121) — page code reads "LU-S," sequence suggests "LU-8" (nav only, no data risk).
- [p.129](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=129) — INSPECT WATER PUMP: sentence order looks scrambled by column extraction.
- [p.129](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=129) — DISASSEMBLY step 1 heading/label order looks scrambled.
- [p.129](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=129)/130 — see priority list above (185°F/8°C mismatch).
- [p.126](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=126) — "4. DRAIN ENGINE COOLANT" — step number looks like it should be "1," left untouched (legible digit, not garbled).

## 07-cooling-system.md
- [p.133](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=133) — HINT on not removing the thermostat: missing words across a line wrap.
- [p.135](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=135) — "remove any mud or a / from the radiator core" — a word appears fully missing.
- [p.135](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=135) — NOTICE on high-pressure cleaner, truncated across 3 lines.
- [p.135](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=135) — CAUTION on burn hazard removing radiator cap — garbled/missing words.
- [p.135](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=135) — instruction on holding tester above 30° — garbled.
- [p.135](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=135) — NOTICE on pump speed "for the first pump only" — missing words.
- [p.137](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=137) — diagram dimension-callout interleaved with a real instruction sentence, couldn't be separated.
- [p.137](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=137) — HINT on lock-plate-groove damage heavily garbled.
- [p.137](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=137) — "lightly 10 with sand paper" — unclear if "10" is real or a garbled word.
- [p.139](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=139) — "apply pressure to the 1am" — unclear if "1am" hides a real word (likely "tank").
- [p.139](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=139) — HINT on resin-tank water-leak testing has missing words, cuts off mid-sentence.
- [p.139](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=139) — running header page code (CO-14 expected) missing entirely from OCR — not fabricated.
- [p.143](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=143) — step 1 heading ends mid-parenthetical, apparently cut off.
- [p.143](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=143) — "between terminals 3 aifre" — second terminal number/word illegible.
- [p.143](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=143) — step (a) instruction text appears entirely missing, only a diagram label survived.

## 08-electronic-fuel-injection.md
This chapter had the heaviest OCR damage — mostly diagnostic tables and wiring flowcharts where real data and noise are interleaved on the same lines, too risky to pick apart without touching a value. Flagged at the table/diagram level rather than line-by-line:
- [p.146](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=146) — one garbled connector-terminal line.
- [p.151](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=151) — blink-pattern / "2 trip detection logic" timing chart.
- [p.154](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=154)-[155](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=155) — multi-column DTC table (Code No./System/Diagnosis/Trouble Area/Memory/Page).
- [p.156](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=156)-[157](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=157) — DTC driving-pattern timing diagrams (codes 21, 25).
- [p.158](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=158) — "DIAGNOSIS CIRCUIT INSPECTION" flowchart.
- [p.159](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=159)-[174](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=174) — full "Troubleshooting w/ Volt, Ohmmeter" run: ECU pinout, per-terminal voltage tables, per-circuit flowcharts (one flag per page).
- [p.175](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=175) — "Reference Value for Engine ECU Data" table.
- [p.209](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=209)-[210](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=210) — water-temp and IAT sensor resistance-vs-temperature graphs.
- [p.211](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=211) — applied-vacuum vs. voltage-drop table.
- [p.213](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=213)-[214](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=214) — oxygen sensor feedback-voltage flowchart.
- [p.215](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=215)-[217](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=217) — ECU wiring-connector voltage/resistance reference tables.

## General reading tips (not page-specific)
- **Ω (ohms) symbol frequently OCR's as digit "2"** across resistance specs manual-wide (e.g. "125-200Ω" → "125-2002"). Not an error per se, just how it reads — worth knowing when scanning any resistance value in this manual.

