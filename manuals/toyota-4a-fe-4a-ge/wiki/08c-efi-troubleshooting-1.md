# Electronic Fuel Injection — Troubleshooting w/ Volt-Ohmmeter (1) (part 3 of 7)

*Section code: `FI` | PDF pages 159-166 | ECU pinout and per-terminal voltage/circuit troubleshooting flowcharts, first half.*

Other parts of this chapter: [System/Diagnosis Basics](08a-efi-system-diagnosis.md) · [DTC Tables](08b-efi-dtc-tables.md) · [Troubleshooting 2](08d-efi-troubleshooting-2.md) · [Fuel/Injector](08e-efi-fuel-injector.md) · [Throttle Body](08f-efi-throttle-body.md) · [Sensors/Relays](08g-efi-sensors-relays.md)

See also: [Torque Specifications index](09-torque-specs.md) for every torque value in this manual with links back to source.

---
<a id="p159"></a>

<!-- NEEDS REVIEW: pages FI-14 through FI-29 (PDF p.159-174) are wiring-diagram/flowchart pages for "Troubleshooting w/ Volt, Ohmmeter"; terminal-location diagrams and flowchart branches on these pages are heavily garbled from OCR of wiring diagrams. Numeric spec values (voltages/resistances) were left untouched, but should be cross-checked against the source scan. Individual pages are flagged below. -->
<!-- NEEDS REVIEW: this whole chapter (part 3 of 7) converts flowchart/decision-tree diagrams into step-sequence tables per an explicit editorial decision. Where the source OCR did not clearly preserve which check leads to which next step, the branch targets below are a best-effort reconstruction based on the visible order of fragments and on the standard Toyota EFI troubleshooting-chart pattern (established check → OK/NG split → repair-or-continue), NOT a direct transcription of legible flow-arrow text. Every legible voltage/resistance value has been preserved exactly as OCR'd, including apparent typos (missing decimal points, digit swaps) — these are flagged individually below rather than silently corrected. -->
**[PDF p.159](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=159)** — DIAGNOSIS SYSTEM

### EFI — Troubleshooting w/ Volt, Ohmmeter

**HINT:**

- The following troubleshooting procedures are designed for inspection of each separate system, therefore the actual procedure may vary somewhat. However, troubleshooting should be performed while referring to the inspection methods described in this manual.
- Before beginning inspection, it is best to first make a simple check of the fuses, H-fuses, fusible link, and the condition of the connectors.
- The following troubleshooting procedures are based on the supposition that the trouble lies in either a short or open circuit within the computer.
- If engine trouble occurs even though proper operating voltage is detected in the computer connector, then it can be assumed that the ECU is faulty and should be replaced.

**LOCATION**

Fuse label (from diagram): "WGN 7.5A"

<!-- NEEDS REVIEW: "H-tuses" in the second HINT bullet (PDF p.159) transcribed here as "H-fuses" — could not confirm exact wording, may be a garbled repeat of "fuses" rather than a distinct fuse type -->
<!-- NEEDS REVIEW: the fuse/relay "LOCATION" diagram on PDF p.159 did not OCR as legible text beyond the fragment "WGN 7.5A" — likely an ignition- or EFI-related fuse amperage label, but the diagram itself (fuse box layout) could not be reconstructed from OCR -->

---
<a id="p160"></a>

<!-- NEEDS REVIEW: Engine ECU pin-out diagram and terminal name table below are garbled diagram OCR (PDF p.160) -->
**[PDF p.160](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=160)** — DIAGNOSIS SYSTEM

### Engine ECU Terminals

The source page prints the terminal list as three side-by-side Symbol/Terminal Name column groups (a print-layout artifact of the pinout diagram). They are reproduced below as three separate tables in the same left-to-right order as the source, rather than merged, since cross-column row pairing could not be confirmed from the OCR.

**Column group 1:**

| Symbol | Terminal Name |
|---|---|
| E01 | POWER GROUND |
| E02 | POWER GROUND |
| #1 | INJECTOR |
| #3 | INJECTOR |
| #2 | INJECTOR |
| #4 | INJECTOR |
| RSO | ISC VALVE |
| RSC (?) | ISC VALVE |
| ELS1 | ELECTRIC COOLING FAN RELAY |
| HT | HEATED OXYGEN SENSOR |
| ELS2 | BLOWER RELAY |
| ELS3 | TAIL LIGHT RELAY |
| IGT | IGNITER |
| G2 | CRANKSHAFT POSITION SENSOR |
| G1 | CRANKSHAFT POSITION SENSOR |
| NE | CRANKSHAFT POSITION SENSOR |
| G⊖ (?) | CRANKSHAFT POSITION SENSOR |
| IGF | IGNITER |
| CF | COOLING FAN RELAY |

**Column group 2:**

| Symbol | Terminal Name |
|---|---|
| E1 | ENGINE GROUND |
| VF | CHECK CONNECTOR |
| VVT | CAMSHAFT [OIL?] CONTROL VALVE |
| TE1 | CHECK CONNECTOR |
| OX | OXYGEN SENSOR |
| TE2 | CHECK CONNECTOR |
| KNK | KNOCK SENSOR |
| ELS4 | DEFOGGER SWITCH |
| THW | WATER TEMP. SENSOR |
| THA | INTAKE AIR TEMP. SENSOR |
| VTA | THROTTLE POSITION SENSOR |
| PIM | VACUUM SENSOR |
| EVP | EVAP |
| VC | SENSOR POWER (THROTTLE) (?) |
| E2 | SENSOR GROUND |
| STA | STARTER RELAY |

**Column group 3:**

| Symbol | Terminal Name |
|---|---|
| AC1 | A/C AMPLIFIER |
| ACT | A/C AMPLIFIER (?) |
| SP1 | SPEED SENSOR |
| W | WARNING LIGHT |
| FC | CIRCUIT OPENING RELAY |
| BATT | BATTERY |
| +B | BATTERY |

<!-- NEEDS REVIEW: "RSC (?)" (column group 1) — source shows only a ">" glyph in place of a symbol for the second ISC VALVE row; "RSC" is a plausible reconstruction (paired with RSO as the two common ISC-valve coil terminals) but is not directly legible in the OCR -->
<!-- NEEDS REVIEW: "G⊖ (?)" (column group 1) — source shows "G-." next to CRANKSHAFT POSITION SENSOR; exact symbol form uncertain (could be a 4th crank-position-related terminal or ground-reference notation) -->
<!-- NEEDS REVIEW: "VVT | CAMSHAFT [OIL?] CONTROL VALVE" (column group 2) — source shows "CAMSHAFT" on one line and "Of CONTROL VALVE}" on the next; "Of" plausibly reads "OIL" (i.e. "camshaft oil control valve") but not confirmed -->
<!-- NEEDS REVIEW: "VC | SENSOR POWER (THROTTLE) (?)" (column group 2) — source text for this row is badly garbled ("NACTRA SERSON, THROTTLE"); reconstructed only by inference from VC's known role as the throttle-position-sensor supply voltage terminal elsewhere on this page (see Engine ECU Wiring Connectors Voltage table, PDF p.161) — not a direct transcription -->
<!-- NEEDS REVIEW: "ACT | A/C AMPLIFIER (?)" (column group 3) — appears as a second, separate A/C AMPLIFIER row immediately below AC1 in the source; may be a genuinely distinct terminal (e.g. compressor-clutch related) whose real label got OCR'd identically to AC1, rather than an actual duplicate -->
<!-- NEEDS REVIEW: below the Symbol/Terminal Name tables, the source (PDF p.160) also has a physical ECU-connector pin-block diagram showing the pins arranged by connector shape. It OCR'd to unreadable fragments (e.g. "i}#1 | #2 RsORSCHT Est /1a2|NElIGr vF| /lo Pmivc! KTAAcises w mi") and could not be reconstructed positionally. Every terminal symbol visible in those fragments (#1, #2, RSO/RSC, HT, E1, IGF, VF, PIM, VC, W, etc.) is already captured in the tables above. A stray number "2853" also appears near this diagram in the source with no clear meaning. -->

---
<a id="p161"></a>

<!-- NEEDS REVIEW: "Engine ECU Wiring Connectors Voltage" table below has broken column alignment (PDF p.161) -->
**[PDF p.161](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=161)** — DIAGNOSIS SYSTEM

### Engine ECU Wiring Connectors Voltage

| No. | Terminals | Condition | STD Voltage (V) | See Page |
|---|---|---|---|---|
| 1 | +B-E1 | IG SW ON | 9-14 | FI-17 |
| 2 | BATT-E1 | IG SW ON | 0-14 | FI-18 |
| 3 | VC-E2 | IG SW ON | 45-55 | FI-19 |
| 3 | VTA-E2 | IG SW ON, throttle valve fully closed | 0.3-0.8 | FI-19 |
| 3 | VTA-E2 | IG SW ON, throttle valve fully open | 9.2-4.9 | FI-19 |
| 4 | PIM-E2 | IG SW ON | 3.3-3.9 | FI-21 |
| 4 | VC-E2 | IG SW ON | 4.5-5.5 | FI-21 |
| 5 | #1-E01 (?) | (illegible in source) | o14 | FI-22 |
| 6 | THA-E2 | Intake air temperature 20°C (68°F) | 0.5-3.4 | FI-23 |
| 7 | THW-E2 | Coolant temperature 80°C (176°F) | 0.2-1.0 | FI-24 |
| 8 | STA-E1 | Cranking | 6 or more | FI-25 |
| 9 | IGF-E1 (?) | IG SW ON, igniter connector disconnected | 45-55 | FI-26 (?) |
| 9 | IGT-E1 | Idling | Pulse generation | FI-26 (?) |
| 10 | ISC-E1 (?) | IG SW ON, engine ECU connectors disconnected | 9-14 | FI-27 |
| 11 | W-E1 (?) | No trouble (check engine warning light off) and engine running | 9-14 | FI-28 |

<!-- NEEDS REVIEW: row 2 (BATT-E1) STD voltage prints as "0-14" here, but the same spec is clearly legible as "9-14V" on the BATT-E1 flowchart page (PDF p.163) — likely an OCR misread of "9" as "0". Value preserved exactly as printed in this table; not corrected. -->
<!-- NEEDS REVIEW: row 3/4 VC-E2 STD voltage prints as "45-55" (no decimal points) in this table, vs. the clean "4.5-5.5" rendering in row 4 and on the VC-E2 flowchart page (PDF p.164, also "45-55V" there). Almost certainly "4.5-5.5V" with OCR dropping the decimal points; digits preserved exactly as printed, not corrected. -->
<!-- NEEDS REVIEW: row 3 VTA-E2 "fully open" STD voltage prints as "9.2-4.9" — this is internally inconsistent (lower bound greater than upper bound). The same spec is legible on PDF p.164 as "3.2-49V" (i.e. likely 3.2-4.9V), suggesting the leading "9" here is an OCR misread of "3". Value preserved exactly as printed; not corrected. -->
<!-- NEEDS REVIEW: row 5 (#1-E01) is almost entirely illegible in the source OCR — condition column is unreadable, and the STD voltage "o14" is a literal transcription of the OCR characters (likely "0-14" with "o" misread for "0"). Terminal designator "#1-E01" is a low-confidence guess based on position in the table sequence (between row 4 / PIM-E2-VC-E2 and row 6 / THA-E2). -->
<!-- NEEDS REVIEW: row 9 terminal symbol "IGF-E1" reconstructed from heavily garbled OCR ("1@F-€1.°"); low confidence. Its "See Page" value and the following IGT-E1 row's "See Page" value both print as an unreadable fragment ("7 96"); left untranscribed as "FI-26 (?)" by inference from the surrounding FI-17/18/19/21/23/24/25/27/28 sequence, not because "FI-26" is actually legible in the source. -->
<!-- NEEDS REVIEW: row 10 terminal symbol "ISC-E1" reconstructed from garbled OCR ("BSC-ey"); low confidence. Note the Engine ECU Terminals pinout (PDF p.160) lists "RSO"/"RSC (?)" — not "ISC" — as the ISC valve terminals, so this row's true terminal designator is uncertain. -->
<!-- NEEDS REVIEW: row 11 terminal symbol "W-E1" reconstructed from garbled OCR ("Wet"); low confidence, though "W" (WARNING LIGHT) is a real terminal per the Engine ECU Terminals pinout on PDF p.160, which supports this reading. -->

---
<a id="p162"></a>

<!-- NEEDS REVIEW: +B-E1 troubleshooting flowchart/wiring diagram is garbled diagram OCR (PDF p.162) -->
**[PDF p.162](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=162)** — DIAGNOSIS SYSTEM

### +B-E1 Circuit

| Terminals | Trouble | Condition | STD Voltage |
|---|---|---|---|
| +B-E1 | No voltage | IG SW ON | 9-14V |

Circuit path (from wiring diagram): Battery → EFI 15A fuse → EFI Main Relay → Engine ECU terminal +B; Ignition Switch (IG2) feeds the EFI main relay coil.

| Step | Check | Condition | Std Value | If OK → | If NG → |
|---|---|---|---|---|---|
| 1 | Confirm no voltage between ECU terminals +B and E1 | IG SW ON | 9-14V expected | — (this is the starting trouble condition) | Proceed to step 2 |
| 2 | Voltage between ECU terminal +B and body ground | IG SW ON | 9-14V (battery voltage) | Go to step 3 | Go to step 4 |
| 3 | Wiring/continuity between ECU terminal E1 and body ground | — | Continuity expected | Try another ECU | Repair or replace wiring |
| 4 | Fuses, fuse, fusible link, and ignition switch | — | — | Go to step 5 | Repair or replace |
| 5 | EFI main relay | — | — | Go to step 6 | Repair or replace relay |
| 6 | Wiring between EFI main relay and battery | — | — | (chain OK — recheck elsewhere) | Repair or replace wiring |

<!-- NEEDS REVIEW: step numbering/order above is reconstructed from the visible sequence of check descriptions on PDF p.162 ("Check that there is voltage between ECU terminal +B and body [ground]" → NO/OK split → "Check wiring between ECU terminal E1 and body [ground]" → OK/BAD split → then a separate linear chain "Check fuses, fuse, fusible link and ignition switch" → "Check EFI main relay" → "Check wiring between EFI main relay and battery", each followed by a "BAD → repair or replace" marker). The exact OK/NG arrow routing between step 2 and steps 4-6 (i.e. which branch of step 2 leads into the fuse/relay chain) is inferred from the standard Toyota EFI power-supply troubleshooting pattern, not directly legible in the OCR — a human should verify against the source scan. -->

---
<a id="p163"></a>

<!-- NEEDS REVIEW: BATT-E1 troubleshooting flowchart/wiring diagram is garbled diagram OCR (PDF p.163) -->
**[PDF p.163](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=163)** — DIAGNOSIS SYSTEM

### BATT-E1 Circuit

| Terminals | Trouble | Condition | STD Voltage |
|---|---|---|---|
| BATT-E1 | No voltage | — | 9-14V |

Circuit path (from wiring diagram): Battery → EFI [fuse/fusible link] → Engine ECU terminal BATT (direct battery feed, not via ignition switch).

| Step | Check | Condition | Std Value | If OK → | If NG → |
|---|---|---|---|---|---|
| 1 | Confirm no voltage between ECU terminals BATT and E1 | — | 9-14V expected | — (this is the starting trouble condition) | Proceed to step 2 |
| 2 | Voltage between ECU terminal BATT and body ground | — | 9-14V (battery voltage) | Go to step 3 | Go to step 4 |
| 3 | Wiring/continuity between ECU terminal E1 and body ground | — | Continuity expected | Try another ECU | Repair or replace wiring |
| 4 | Wiring between ECU terminal BATT and battery | — | — | (chain OK — recheck elsewhere) | Repair or replace wiring |

<!-- NEEDS REVIEW: step 4 above is reconstructed from a single trailing fragment on PDF p.163 ("...and battery" / "Repair or replace") by analogy with the parallel +B-E1 chart (PDF p.162); the check description that should precede it is illegible in the OCR, so this step is a low-confidence placeholder. The "Condition" column for this circuit (elsewhere shown as "IG SW ON" on similar charts) is also illegible on this page — BATT is typically a hot-at-all-times circuit, but that isn't independently confirmed here. -->

---
<a id="p164"></a>

<!-- NEEDS REVIEW: VC-E2/VTA-E2 table and troubleshooting flowchart/wiring diagram are garbled diagram OCR (PDF p.164) -->
**[PDF p.164](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=164)** — DIAGNOSIS SYSTEM

### VC-E2 / VTA-E2 Circuit (Throttle Position Sensor)

| Terminals | Trouble | Condition | STD Voltage |
|---|---|---|---|
| VC-E2 | No voltage | IG SW ON | 45-55V |
| VTA-E2 | No voltage | IG SW ON, throttle valve fully closed | 0.3-08V |
| VTA-E2 | No voltage | IG SW ON, throttle valve fully open | 3.2-49V |

Circuit: Engine ECU ↔ Throttle Position Sensor.

**VC-E2 sub-check:**

| Step | Check | Condition | Std Value | If OK → | If NG → |
|---|---|---|---|---|---|
| 1 | Voltage between ECU terminals VC and E2 | IG SW ON | 45-55V (see review note) | Go to step 2 | Refer to No.1 (+B-E1 check, see FI-17 / PDF p.162) |
| 2 | (illegible check in source) | IG SW ON | — | Go to step 3 | — |
| 3 | Check throttle position sensor, then check wiring between ECU and throttle position sensor | — | — | Try another ECU | Repair or replace (sensor/wiring) |

<!-- NEEDS REVIEW: STD voltage values on this page print without decimal points ("45-55V", "0.3-08V", "3.2-49V"). These are almost certainly "4.5-5.5V", "0.3-0.8V", and "3.2-4.9V" respectively (compare to the Engine ECU Wiring Connectors Voltage table, PDF p.161, where the same VC-E2 spec shows as "45-55" and "4.5-5.5" in different rows). Digits preserved exactly as OCR'd; not corrected. -->
<!-- NEEDS REVIEW: step 2 of the VC-E2 sub-check is essentially illegible in the source ("Cae at ee tee bron ECW..."); it is left as a placeholder rather than invented. Step 3 merges two source lines ("Check throttle position sensor" and "Check wiring between ECU and throttle position sensor") whose individual OK/BAD branches could not be confidently separated — treat as a single combined check pending verification against the scan. -->

---
<a id="p165"></a>

<!-- NEEDS REVIEW: VTA-E2 troubleshooting flowchart continues, garbled diagram OCR (PDF p.165) -->
**[PDF p.165](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=165)** — DIAGNOSIS SYSTEM

### VTA-E2 Circuit (continued)

| Step | Check | Condition | Std Value | If OK → | If NG → |
|---|---|---|---|---|---|
| 1 | Confirm no voltage between ECU terminals VTA and E2 | IG SW ON | — (starting trouble condition) | — | Proceed to step 2 |
| 2 | Voltage between ECU terminals VC and E2 | IG SW ON | — | Go to step 3 | Refer to VC-E2 trouble (see p.164 table above) |
| 3 | Wiring between ECU and throttle position sensor | — | — | Try another ECU | Repair or replace wiring |

<!-- NEEDS REVIEW: this page is a continuation of the VTA-E2 flowchart begun on PDF p.164. The reconstruction above follows the legible fragments "...there is voltage between ECU terminals VC and E2 (IG SW ON)", "[NO/OK", "Refer to VC-E2 trouble", "Check wiring between ECU and... throttle position sensor", "OK ... Try another ECU". The word "Repair or replace" appears twice in the source on this page and could belong to either step 2's NG branch or step 3's NG branch (or both, for a sensor-vs-wiring split) — routing between the two is not fully confirmed. -->

---
<a id="p166"></a>

<!-- NEEDS REVIEW: PIM-E2 vacuum sensor table and troubleshooting flowchart are garbled diagram OCR (PDF p.166) -->
**[PDF p.166](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=166)** — DIAGNOSIS SYSTEM

### PIM-E2 Circuit (Vacuum / Manifold Pressure Sensor)

| Terminals | Trouble | Condition | STD Voltage |
|---|---|---|---|
| PIM-E2 | No voltage | IG SW ON | (illegible — see PIM-E2 row in Engine ECU Wiring Connectors Voltage table, PDF p.161: 3.3-3.9) |
| VC-E2 | — | IG SW ON | 45-5.5V |

Circuit: Engine ECU ↔ Vacuum Sensor (Manifold Pressure Sensor), terminals VC / PIM / E1.

| Step | Check | Condition | Std Value | If OK → | If NG → |
|---|---|---|---|---|---|
| 1 | Confirm no voltage between ECU terminals PIM and E2 | IG SW ON | — (starting trouble condition) | — | Proceed to step 2 |
| 2 | (illegible check in source — likely voltage between ECU terminals VC and E2) | IG SW ON | — | Go to step 3 | Refer to No.1 (+B-E1 check, see FI-17 / PDF p.162) |
| 3 | Wiring between ECU terminal E1 and body ground | IG SW ON | Continuity expected | Go to step 4 | — |
| 4 | Wiring between ECU and vacuum sensor / vacuum sensor itself | — | — | (chain OK) | Repair or replace |

<!-- NEEDS REVIEW: the PIM-E2 STD voltage on this page prints as fragmented, uncertain OCR ("38 39V" / "39." as separate fragments) rather than a clean number; it has been left as "illegible" with a cross-reference to the clean value on PDF p.161 (3.3-3.9V) rather than transcribing a guessed digit string into the value cell. The "VC-E2 ... 45-5.5V" value is transcribed exactly as printed (note inconsistent decimal placement vs. "4.5-5.5V" elsewhere — not corrected). -->
<!-- NEEDS REVIEW: steps 2-4 of this flowchart are heavily garbled ("Baa a nn Ea ia aL", "Snake Bann EU wa 8 ado") and are reconstructed largely by analogy with the parallel VC-E2/VTA-E2 flowchart pattern on PDF p.164-165, not by direct transcription of legible source text. The one clearly legible cross-reference is "Refer to No.1 (See page FI-17)", which is preserved above; everything else in this table should be treated as low-confidence and checked against the original scan. -->

---

