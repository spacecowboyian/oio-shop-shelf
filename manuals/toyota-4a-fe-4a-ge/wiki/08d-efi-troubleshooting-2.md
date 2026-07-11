# Electronic Fuel Injection — Troubleshooting w/ Volt-Ohmmeter (2) & Reference ECU Data (part 4 of 7)

*Section code: `FI` | PDF pages 167-175 | Remaining per-circuit troubleshooting flowcharts plus the Reference Value of Engine ECU Data table.*

Other parts of this chapter: [System/Diagnosis Basics](08a-efi-system-diagnosis.md) · [DTC Tables](08b-efi-dtc-tables.md) · [Troubleshooting 1](08c-efi-troubleshooting-1.md) · [Fuel/Injector](08e-efi-fuel-injector.md) · [Throttle Body](08f-efi-throttle-body.md) · [Sensors/Relays](08g-efi-sensors-relays.md)

See also: [Torque Specifications index](09-torque-specs.md) for every torque value in this manual with links back to source.

<!-- NEEDS REVIEW (chapter-wide): every flowchart on pages 167-174 was OCR'd from a wiring-diagram/flowchart page layout, not running text. The step tables below are a best-effort reconstruction of the decision-tree logic (which check leads to which next check on OK vs. NG/BAD). Every voltage/resistance value that was legible has been preserved exactly. Where the branch destination itself could not be traced through the garbled OCR, the table says so explicitly rather than guessing — see the per-page review notes. -->

---
<a id="p167"></a>

<!-- NEEDS REVIEW: injector terminal table and troubleshooting flowchart are garbled diagram OCR (PDF p.167) -->
**[PDF p.167](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=167)** — DIAGNOSIS SYSTEM

### Injector Circuit — Troubleshooting w/ Volt, Ohmmeter

*(Manual page code: FI-22)*

| Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|
| #1, #2, #3, #4 — E01, E02 | No voltage | IG SW ON | 9-14V |

| Step | Check | Condition | Std Value | If OK → | If NG/Bad → |
|---|---|---|---|---|---|
| 1 | Voltage between ECU terminals #1, #2, #3, #4 and E01 and/or E02 | IG SW ON | 9-14V | Circuit OK | Go to step 2 |
| 2 | Voltage between ECU terminal #1, #2, #3, and/or #4 and body ground | IG SW ON | — | Go to step 3 | Check wiring between ECU terminal #1, #2, #3, and/or #4 and battery; repair or replace |
| 3 | Resistance of each injector | — | 13.4-14.2Ω | Go to step 4 | Repair or replace injector |
| 4 | (not confidently traceable — see review note) | — | — | — | — |

<!-- NEEDS REVIEW: two things on this page could not be reconstructed with confidence. (1) A dangling OCR fragment — "...between ECU terminal E01 and / or E02 and" — sits between the step-2 and step-3 text in the source and may indicate an additional ground-circuit check (e.g. continuity between ECU terminal E01/E02 and body ground) that is missing from this table; it was not included because its position in the branch logic is unclear. (2) The injector resistance value is transcribed as "13.4-14.2Ω" reconstructed from the raw OCR string "13.4-1420" — this document's OCR consistently renders the Ω (ohm) symbol as a trailing "0" (confirmed by the same pattern in the ISC valve resistance values on p.172: "22.30"→22.3Ω, "28.50"→28.5Ω, "24.590"→24.5Ω), so the reconstruction is likely correct but should be checked against the source PDF image. -->

---
<a id="p168"></a>

<!-- NEEDS REVIEW: THA-E2 (intake air temp sensor) troubleshooting flowchart is garbled diagram OCR (PDF p.168) -->
**[PDF p.168](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=168)** — DIAGNOSIS SYSTEM

### Intake Air Temperature Sensor Circuit (THA-E2) — Troubleshooting w/ Volt, Ohmmeter

*(Manual page code: FI-23)*

| Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|
| THA — E2 | No voltage | IG SW ON, intake air temperature 20°C (68°F) | 0.5-3.4V |

| Step | Check | Condition | Std Value | If OK → | If NG/Bad → |
|---|---|---|---|---|---|
| 1 | Voltage between ECU terminals THA and E2 | IG SW ON, intake air temperature 20°C (68°F) | 0.5-3.4V | Circuit OK | Go to step 2 |
| 2 | Voltage between ECU terminal +B and body ground | IG SW ON | — | Go to step 3 | Refer to the power-source check ("No.1", see manual page FI-17) |
| 3 | Intake air temperature sensor condition (resistance check) | — | — | Go to step 4 | Replace intake air temperature sensor |
| 4 | Wiring between ECU and intake air temperature sensor | — | — | Try another ECU | Repair or replace wiring |

<!-- NEEDS REVIEW: the OK/BAD column order flips between fragments on this page and the exact routing between steps 2, 3, and 4 is a best-effort reconstruction — the source is too garbled to confirm which outcome ("Replace sensor" vs. "Try another ECU" vs. "Repair or replace wiring") attaches to which check. All four checks and both legible outcomes ("Repair or replace", "Try another ECU") are preserved; only their exact wiring together is uncertain. -->

---
<a id="p169"></a>

<!-- NEEDS REVIEW: THW-E2 (water temp sensor) troubleshooting flowchart is garbled diagram OCR (PDF p.169) -->
**[PDF p.169](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=169)** — DIAGNOSIS SYSTEM

### Water Temperature Sensor Circuit (THW-E2) — Troubleshooting w/ Volt, Ohmmeter

*(Manual page code: FI-24, No.7)*

| Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|
| THW — E2 | No voltage | IG SW ON, coolant temperature 80°C (176°F) | 0.2-1.0V |

| Step | Check | Condition | Std Value | If OK → | If NG/Bad → |
|---|---|---|---|---|---|
| 1 | Voltage between ECU terminals THW and E2 | IG SW ON, coolant temperature 80°C (176°F) | 0.2-1.0V | Circuit OK | Go to step 2 |
| 2 | Voltage between ECU terminal +B and body ground | IG SW ON | — | Go to step 3 | Refer to the power-source check ("No.1", see manual page FI-17) |
| 3 | Wiring between ECU terminal E1 and body ground | — | — | Go to step 4 | Repair or replace wiring |
| 4 | Water temperature sensor condition (resistance check) | — | — | Go to step 5 | Replace water temperature sensor |
| 5 | Wiring between ECU and water temperature sensor | — | — | Try another ECU | Repair or replace wiring |

<!-- NEEDS REVIEW: same caveat as the THA-E2 flowchart on p.168 — steps and outcomes are all present in the OCR but the exact OK/BAD wiring between them is reconstructed from fragmentary text, not confirmed. A stray "ProCarManuals.com" watermark string in the source OCR was dropped as scan noise, not manual content. -->

---
<a id="p170"></a>

<!-- NEEDS REVIEW: STA-E1 (starter signal) troubleshooting flowchart is garbled diagram OCR (PDF p.170) -->
**[PDF p.170](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=170)** — DIAGNOSIS SYSTEM

### Starter Signal Circuit (STA-E1) — Troubleshooting w/ Volt, Ohmmeter

*(Manual page code: FI-25, No.8)*

| Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|
| STA — E1 | No voltage | Cranking | 6V or more |

| Step | Check | Condition | Std Value | If OK → | If NG/Bad → |
|---|---|---|---|---|---|
| 1 | Voltage between ECU terminal STA and E1 | Cranking | 6V or more | Circuit OK | Go to step 2 |
| 2 | Starter operation (does the starter crank the engine?) | IG SW START | — | Go to step 3 | Go to step 5 |
| 3 | Wiring between ECU terminal STA and ignition switch terminal ST2 | — | — | Go to step 4 | Repair or replace wiring |
| 4 | Wiring between ECU terminal E1 and body ground | — | — | Try another ECU | Repair or replace wiring |
| 5 | H-fuses, fusible link, battery, wiring, ignition switch, and starter relay | — | — | Go to step 6 | Repair or replace |
| 6 | Voltage at starter terminal 50 | IG SW START | 6-14V | Check starter, repair or replace if faulty | Check wiring between ignition switch terminal ST2 and starter terminal 50; repair or replace |

<!-- NEEDS REVIEW: the source shows two "check wiring" fragments after the starter-operation check (ECU terminal STA↔ST2, and ECU terminal E1↔body ground) whose sequence relative to each other is not confirmed — they are presented here as sequential steps 3-4, but they may instead be parallel alternative checks. All legible checks, conditions and values (6V or more, 6-14V) are preserved. -->

---
<a id="p171"></a>

<!-- NEEDS REVIEW: IGF-E1/IGT-E1 (igniter) troubleshooting flowchart is garbled diagram OCR (PDF p.171) -->
**[PDF p.171](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=171)** — DIAGNOSIS SYSTEM

### Igniter Circuit (IGF-E1 / IGT-E1) — Troubleshooting w/ Volt, Ohmmeter

*(Manual page code: FI-26, No.9)*

| Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|
| IGF — E1 | No voltage | IG SW ON, igniter connector disconnected | 4.5-5.5V |
| IGT — E1 | No voltage | Idling | Pulse generation |

| Step | Check | Condition | Std Value | If OK → | If NG/Bad → |
|---|---|---|---|---|---|
| 1 | Voltage between ECU terminals IGF and E1 | IG SW ON, igniter connector disconnected | 4.5-5.5V | Circuit OK | Go to step 3 |
| 2 | Voltage/pulse between ECU terminals IGT and E1 | Idling | Pulse generation | Circuit OK | Go to step 3 |
| 3 | Voltage between ECU terminal +B and body ground | IG SW ON | — | Go to step 4 | Refer to the power-source check ("No.1", see manual page FI-17) |
| 4 | Wiring between ECU terminal E1 and body ground | — | — | Go to step 5 | Repair or replace wiring |
| 5 | H-fuse, fuse, fusible link, and ignition switch | — | — | Go to step 6 | (outcome not legible — see review note) |
| 6 | Ignition coil | — | — | Go to step 7 | Repair or replace |
| 7 | Wiring between ECU and battery | — | — | Go to step 8 | Repair or replace |
| 8 | Igniter | — | — | (outcome not legible — see review note) | Repair or replace |

<!-- NEEDS REVIEW: steps 5 and 8's "If OK" outcomes are not present/legible in the source OCR (the flowchart likely continues to another check or concludes "Try another ECU" as on neighboring pages, but this is not stated in the text and was not invented). The relative order of steps 5-8 (fuse/fusible-link check, ignition coil check, ECU-to-battery wiring check, igniter check) is reconstructed from the order the fragments appear on the page and is not fully confirmed. -->

---
<a id="p172"></a>

<!-- NEEDS REVIEW: RSC/RSO-E1 (ISC valve) troubleshooting flowchart is garbled diagram OCR (PDF p.172) -->
**[PDF p.172](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=172)** — DIAGNOSIS SYSTEM

### ISC Valve Circuit (RSC/RSO-E1) — Troubleshooting w/ Volt, Ohmmeter

*(Manual page code: FI-27 — likely "No.10" by sequence, not confirmed legible in source)*

| Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|
| RSC or RSO — E1 | No voltage | IG SW ON | 9-14V |

| Step | Check | Condition | Std Value | If OK → | If NG/Bad → |
|---|---|---|---|---|---|
| 1 | Voltage between ECU terminal RSC or RSO and E1 | IG SW ON | 9-14V | Circuit OK | Go to step 2 |
| 2 | Voltage between ECU terminal +B and body ground | IG SW ON | — | Go to step 3 | Refer to the power-source check ("No.1", see manual page FI-17) |
| 3 | ISC valve resistance | — | 19.3-22.3Ω (nominal); Cold: 17.5-28.5Ω; Hot: 17.0-24.5Ω | Go to step 4 | Replace ISC valve |
| 4 | Wiring between ECU and ISC valve | — | — | Try another ECU | Repair or replace wiring |

<!-- NEEDS REVIEW: a stray "06833" appears near the wiring diagram in the OCR and could not be placed in the table — it is most likely a diagram callout/connector number, not a spec value, but this is not confirmed. The Ω symbol in the resistance values is reconstructed from the OCR's "22.30"/"28.50"/"24.590" (this document's OCR consistently renders Ω as a trailing "0" — see also the p.167 injector resistance note); the digits themselves (19.3, 22.3, 17.5, 28.5, 17.0, 24.5) are exactly as printed. -->

---
<a id="p173"></a>

<!-- NEEDS REVIEW: W-E1 (check engine warning light) troubleshooting flowchart is garbled diagram OCR (PDF p.173) -->
**[PDF p.173](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=173)** — DIAGNOSIS SYSTEM

### Check-Engine Warning Light Circuit (W-E1) — Troubleshooting w/ Volt, Ohmmeter

*(Manual page code: FI-28, No.11)*

| Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|
| W — E1 | No voltage | No trouble codes, idling, engine warning light off | 9-14V |

| Step | Check | Condition | Std Value | If OK → | If NG/Bad → |
|---|---|---|---|---|---|
| 1 | Voltage between ECU terminals W and E1 | Idling, no trouble codes, warning light off | 9-14V | Circuit OK | Go to step 2 |
| 2 | Voltage between ECU terminal W and body ground | — | — | Go to step 4 | Go to step 3 |
| 3 | Wiring between ECU terminal E1 and body ground | — | — | Try another ECU | Repair or replace wiring |
| 4 | GAUGE fuse (10A) and check-engine warning light bulb | — | 10A | (next step not legible — see review note) | Repair or replace |

<!-- NEEDS REVIEW: the source table shows the OK/NG columns for step 2 in "NO | OK" order (reversed from the other flowcharts on these pages), so the step-2 branch destinations above are a best-effort interpretation and should be checked against the source PDF. The flowchart's final check, after the GAUGE-fuse/warning-light-bulb check, is too garbled to transcribe at all (source fragment: "Cl k soe t t : E t s a") — whatever check and outcome followed step 4 on the OK side is lost and not reconstructed here. -->

---
<a id="p174"></a>

<!-- NEEDS REVIEW: VF-E1 (oxygen sensor) troubleshooting flowchart is garbled diagram OCR (PDF p.174) -->
**[PDF p.174](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=174)** — DIAGNOSIS SYSTEM

### Oxygen Sensor Circuit (VF-E1) — Troubleshooting w/ Volt, Ohmmeter

*(Manual page code: FI-29)*

| Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|
| VF — E1 | No voltage | (condition not legible in source) | (value not legible in source) |

| Step | Check | Condition | Std Value | If OK → | If NG/Bad → |
|---|---|---|---|---|---|
| 1 | Voltage between ECU terminal VF and E1 | (not legible) | (not legible) | (see review note) | (see review note) |
| 2 | (check largely illegible — appears related to the oxygen sensor connector) | — | — | (see review note) | Try another ECU (partially legible) |

<!-- NEEDS REVIEW: this page's flowchart OCR is essentially unusable beyond identifying the circuit (oxygen sensor, ECU terminals VF and E1, fed from the EFI main relay) and the fact that the diagnostic tree starts from "no voltage between ECU terminal VF and E1." No reliable step-by-step check sequence, conditions, or std values could be recovered — the two-row table above is the most that can be honestly stated. A stray "23390" in the OCR is most likely a diagram callout/part number, not a spec value. Recommend re-checking this page directly against the source PDF image (p.174) if this circuit needs to be diagnosed. -->

---
<a id="p175"></a>

<!-- NEEDS REVIEW: "Reference Value for Engine ECU Data" table below has broken column alignment (item/inspection condition/reference value) (PDF p.175) -->
**[PDF p.175](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=175)** — DIAGNOSIS SYSTEM

### Reference Value of Engine ECU Data

*(Manual page code: FI-30)*

HINT: Engine ECU data can be monitored by hand-held tester.

1. Hook up the hand-held tester to the check connector.
2. Monitor engine ECU data by following the prompts on the tester screen.

Please refer to the hand-held tester operator's manual for further details.

#### Reference Value for Engine ECU Data (engine at normal operating temp.)

| Item | Inspection Condition | Reference Value |
|---|---|---|
| INJECTOR | (condition not legible — see review note) | Gradually decreases |
| INJECTOR | Engine idling at normal operating temp.*1 | Approx. 3-4 msec |
| IGNITION | Increase engine speed | Gradually increases |
| IGNITION | Engine idling at normal operating temp.*1 | Approx. 29-39% (see review note) |
| ISC DUTY | A/C switch ON | Duty ratio increases |
| ISC DUTY | A/T shifting in "D" position | Duty ratio increases |
| ENGINE SPD | RPM is stable (comparison with tachometer) | No great changes |
| INTAKE MAN. PRESSURE | Engine at normal operating temp. | Approx. 160-380 mmHg (see review note) |
| TEMP | Engine at normal operating temp. | 75-95°C (167-203°F) |
| THROTTLE | Wide open throttle | Above 70° |
| THROTTLE | From closed throttle position to wide open throttle | Gradually increases |
| VEHICLE SPD | During driving (comparison with speedometer) | No large differences |
| (item name not legible — "L" in OCR) | Engine idling at normal operating temp. | 2.5 ± 0.7V |
| A/F FB LEFT | RPM stable at 2,500 rpm with normal operating temp. | ON |
| KNOCK FB | Depress throttle pedal suddenly during idling | ON |
| STA SIGNAL | During cranking | ON |
| IDL SIGNAL | Closed throttle position | ON |
| OX (O2 signal) | RPM stable at 2,500 rpm with normal operating temp. | RICH/LEAN is repeated |

*1: All accessories and A/C are switched OFF.

*2: If the engine coolant temperature sensor circuit is open or shorted, the engine ECU assumes an engine coolant temperature value of 80°C (176°F).

*3: When feedback control is forbidden, 0V is displayed.

<!-- NEEDS REVIEW: several cells in this table are reconstructions from very garbled OCR and should be checked against the source PDF (p.175): (1) the first INJECTOR row's inspection condition is illegible in the source (raw OCR "Enamnecaidto hot") — given the parallel IGNITION row's condition is "increase engine speed," this may originally have been the same condition, but that is not confirmed and was left blank rather than guessed. (2) The IGNITION idling reference value is transcribed as "Approx. 29-39%" exactly as OCR'd, but since this is an ignition-timing spec it may originally have been "29-39°" (degrees BTDC) with the OCR misreading the degree symbol as a percent sign — the digits 29-39 are preserved exactly either way. (3) "Approx. 160-380 mmHg" for intake manifold pressure reconstructs a hyphen into the raw OCR digit string "160380" (no separator was visible) and reads "mmb" as "mmHg" (a standard vacuum unit) — the digit grouping (160 / 380) is the most plausible split but is not confirmed. (4) The row before "A/F FB LEFT" has an item name that is only legible as the single letter "L" in OCR — the value "2.5 ± 0.7V" is preserved exactly, but the item it measures is unidentified. (5) Footnote markers *2 and *3 could not be matched to specific table rows in the garbled OCR (all three footnote definitions are preserved above); by content, *2 most likely applies to the "TEMP" row and *3 most likely applies to the "OX" row, but neither attachment is confirmed in the source text. -->

