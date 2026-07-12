# Electronic Fuel Injection — Sensors, Relays, VSV & Fuel Cut RPM (part 7 of 7)

*Section code: `FI` | PDF pages 201-219 | Camshaft timing oil control valve, ISC valve, EFI main relay, circuit opening relay, VSV for EVAP, water temp/IAT/vacuum/knock/oxygen sensors, fuel cut rpm.*

Other parts of this chapter: [System/Diagnosis Basics](08a-efi-system-diagnosis.md) · [DTC Tables](08b-efi-dtc-tables.md) · [Troubleshooting 1](08c-efi-troubleshooting-1.md) · [Troubleshooting 2](08d-efi-troubleshooting-2.md) · [Fuel/Injector](08e-efi-fuel-injector.md) · [Throttle Body](08f-efi-throttle-body.md)

See also: [Torque Specifications index](09-torque-specs.md) for every torque value in this manual with links back to source.

---
<a id="p201"></a>
**[PDF p.201](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=201)** — THROTTLEBODY

### CAMSHAFT TIMING OIL CONTROL VALVE

**ON-VEHICLE INSPECTION**

1. Disconnect the oil control valve connector.
2. Using an ohmmeter, measure the resistance between the terminals.
   - Resistance: 1M = 13 Ω at 20°C (68°F) <!-- NEEDS REVIEW: OCR text is "1M = 13 Q at 20°C (68°F)"; the Ω symbol is restored from the recurring "Q"→Ω OCR pattern in this chapter, but the "1M =" portion is uncertain — it may originally have been a range such as "11 - 13 Ω" rather than a value labeled "1M". Transcribed literally; verify against source PDF. -->
   - If the resistance is not as specified, replace the valve.
3. Reconnect the oil control valve connector.

**REMOVAL**

1. Remove oil control valve.
   - Disconnect the oil control valve connector.
   - Remove the 2 bolts, oil control valve and O-ring.
   - INSTALLATION HINT: Use a new O-ring.
   - Torque: 8.0 N·m (80 kgf-cm, 71 in.lbf) → [torque-specs #t076](09-torque-specs.md#t076)

**INSPECTION**

1. Inspect oil control valve operation.
   - Apply battery voltage across the terminals, then check the movement of the valve. <!-- NEEDS REVIEW: this sentence is reassembled from fragmented OCR lines ("then cl." / "the movement of the valve"); exact original wording is uncertain -->
   - If operation is not as specified, replace the valve.

**INSTALLATION**

Installation is in the reverse order of removal.

---
<a id="p202"></a>
**[PDF p.202](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=202)** — THROTTLEBODY

### ISC VALVE — ON-VEHICLE INSPECTION

**Inspect ISC valve operation**

1. Initial conditions:
   - Engine at normal operating temperature.
   - Idle speed set correctly.
   - Transmission in neutral position.
2. Using SST, connect terminals TE1 and E1 of the check connector. (SST 09843-18020) <!-- NEEDS REVIEW: OCR shows "Terand E1"; read as "TE1 and E1" matching the standard check-connector terminal designator used elsewhere in this chapter (e.g. p.213-214) -->
3. After engine speed is kept at 1,000 - 1,500 rpm for 5 seconds, check that it returns to idle speed.
   - If the rpm operation is not as specified, check the ISC valve, wiring, and ECU.
4. Remove the SST from the check connector. (SST 09843-18020)

**Inspect ISC valve resistance**

NOTICE: "Cold" and "Hot" in the following sentences express the temperature of the coils themselves. "Cold" is from -10°C (14°F) to 50°C (122°F) and "Hot" is from 50°C (122°F) to 100°C (212°F).

1. Disconnect the ISC valve connector.
2. Using an ohmmeter, measure the resistance between terminal +B and other terminals (RSC, RSO).
   - Resistance:
     - Cold: 17.5 - 28.5 Ω <!-- NEEDS REVIEW: OCR shows "17.5 - 28.52"; the trailing "2" is interpreted as a misrendered Ω symbol (matching the pattern of the "Hot" value directly below and other Ω values on this page), giving 17.5 - 28.5 Ω. Verify against source PDF. -->
     - Hot: 17.0 - 24.5 Ω <!-- NEEDS REVIEW: OCR shows "17.0 — 24.5 Q"; Q restored as Ω per the recurring OCR pattern in this chapter -->
   - If resistance is not as specified, replace the ISC valve.
3. Reconnect the ISC valve connector.

---
<a id="p203"></a>
**[PDF p.203](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=203)** — THROTTLEBODY

### ISC VALVE — COMPONENTS

Exploded-view diagram: Surge Tank Bracket (with Engine Wire), ISC Valve.

Legend:
- N·m (kgf-cm, ft·lbf): Specified torque
- ⊙ Non-reusable part

<!-- NEEDS REVIEW: this is a components/exploded-view diagram page; beyond the two labeled parts and the torque/non-reusable-part legend, no further diagram detail (individual part callouts, bolt positions) is recoverable from OCR (PDF p.203) -->

---
<a id="p204"></a>
**[PDF p.204](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=204)** — THROTTLEBODY

### ISC VALVE — REMOVAL

1. Remove throttle body assembly (see Throttle Body).
2. Remove ISC valve.
   - Remove the 2 bolts and ISC valve.
   - Torque: 22 N·m (220 kgf-cm, 16 ft·lbf) → [torque-specs #t077](09-torque-specs.md#t077)

### ISC VALVE — INSPECTION

**Inspect ISC valve operation**

1. Connect the positive (+) lead from the battery to terminal +B and negative (-) lead to terminal RSC, and check operating sound.
2. Connect the positive (+) lead from the battery to terminal +B and negative (-) lead to terminal RSO, and check operating sound.
3. If operation is not as specified, replace the ISC valve.

### ISC VALVE — INSTALLATION

Installation is in the reverse order of removal.

---
<a id="p205"></a>
**[PDF p.205](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=205)** — THROTTLEBODY

### EFI MAIN RELAY — INSPECTION

1. Remove EFI main relay (marking: EFI).
2. Inspect EFI main relay continuity.
   - Using an ohmmeter, check that there is continuity between terminals 1 and 2.
   - Check that there is no continuity between terminals 3 and 5. <!-- NEEDS REVIEW: OCR truncates this to "no continuity between terminals 3 an[d]"; "5" is inferred from the parallel operation-test step below and from the matching Circuit Opening Relay procedure on the next page -->
   - If continuity is not as specified, replace the relay.
3. Inspect EFI main relay operation.
   - Apply battery voltage across terminals 1 and 2.
   - Using an ohmmeter, check that there is continuity between terminals 3 and 5.
   - If operation is not as specified, replace the relay.
4. Reinstall EFI main relay.

---
<a id="p206"></a>
**[PDF p.206](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=206)** — THROTTLEBODY

### CIRCUIT OPENING RELAY — INSPECTION

1. Remove RH cowl side trim.
2. Remove circuit opening relay.
3. Inspect circuit opening relay continuity.
   - Using an ohmmeter, check that there is continuity between terminals 1 and 2.
   - Check that there is no continuity between terminals 3 and 5. <!-- NEEDS REVIEW: OCR truncates this to "no continuity between terminals 3 an[d]"; "5" is inferred from the parallel operation-test step below -->
   - If continuity is not as specified, replace the relay.
4. Inspect circuit opening relay operation.
   - Apply battery voltage across terminals 1 and 2.
   - Using an ohmmeter, check that there is continuity between terminals 3 and 5.
   - If operation is not as specified, replace the relay.
5. Reinstall circuit opening relay.
6. Install RH cowl side trim.

---
<a id="p207"></a>
**[PDF p.207](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=207)** — THROTTLEBODY

### VSV FOR EVAP — COMPONENTS

<!-- NEEDS REVIEW: component diagram page; no legible parts list or callouts survive OCR beyond the section header (PDF p.207) -->

---
<a id="p208"></a>
**[PDF p.208](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=208)** — THROTTLEBODY

### VSV FOR EVAP — INSPECTION

1. Remove surge tank.
2. Remove VSV.
   - Disconnect the 2 EVAP hoses from the VSV.
   - Remove the 2 bolts and VSV.
3. Inspect VSV for open circuit.
   - Using an ohmmeter, check that there is continuity between the terminals.
   - Resistance: 30 - 33 Ω at 20°C (68°F)
   - If there is no continuity, replace the VSV.
4. Inspect VSV for ground.
   - Using an ohmmeter, check that there is no continuity between each terminal and the body.
   - If there is continuity, replace the VSV.
5. Inspect VSV operation.
   - Check that air flows with difficulty from port E to port F.
   - Apply battery voltage across the terminals.
   - Check that air flows from port E to port F.
   - If operation is not as specified, replace the VSV.
6. Reinstall VSV.
   - Install the VSV with the screw.
   - Connect the 2 EVAP hoses to the VSV.
7. Reinstall emission control valve set.
8. Reinstall high-tension cord cover.
9. Reinstall V-bank cover.

---
<a id="p209"></a>

<!-- NEEDS REVIEW: water-temperature-sensor resistance-vs-temperature graph below is garbled diagram OCR; only endpoint axis values are legible (PDF p.209) -->
**[PDF p.209](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=209)** — THROTTLEBODY

### WATER TEMPERATURE SENSOR — INSPECTION

1. Drain engine coolant.
2. Remove water temperature sensor.
3. Inspect water temperature sensor.
   - Using an ohmmeter, measure the resistance between the terminals.
   - Resistance: refer to the graph below.
   - If the resistance is not as specified, replace the water temperature sensor.
4. Reinstall water temperature sensor.
   - Install a new gasket to the water temperature sensor.
5. Fill radiator with engine coolant.

**Resistance vs. temperature graph (reference, FIA741) — legible data points only:**

| Temperature | °F equivalent |
|---|---|
| -20°C | -4°F |
| 0°C | 32°F |
| 20°C | 68°F |
| 40°C | 104°F |
| 60°C | 140°F |
| 80°C | 176°F |
| 100°C | 212°F |

<!-- NEEDS REVIEW: this is a resistance-vs-temperature curve graph (labeled "FIA741"). Only the X-axis (temperature) tick marks in the table above are legible from OCR. The Y-axis (resistance, likely kΩ on a log scale) tick marks are too garbled to transcribe reliably — raw OCR fragments include "20", "‘0b", ".8", "2", "2k", "0.5", "0.3", "0.2" — and the actual curve (which resistance value corresponds to which temperature) is not recoverable from this OCR. Refer to the original PDF p.209 for the actual curve. -->

---
<a id="p210"></a>

<!-- NEEDS REVIEW: IAT-sensor resistance-vs-temperature graph below is garbled diagram OCR; only endpoint axis values are legible (PDF p.210) -->
**[PDF p.210](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=210)** — THROTTLEBODY

### INTAKE AIR TEMPERATURE (IAT) SENSOR — INSPECTION

1. Remove IAT sensor.
2. Inspect IAT sensor resistance.
   - Using an ohmmeter, measure the resistance between the terminals.
   - Resistance: refer to the graph below.
   - If the resistance is not as specified, replace the IAT sensor.
3. Reinstall IAT sensor.

**Resistance vs. temperature graph (reference) — legible data points only:**

| Temperature | °F equivalent |
|---|---|
| -20°C | -4°F |
| 0°C | 32°F |
| 20°C | 68°F |
| 40°C | 104°F |
| 60°C | 140°F |
| 80°C | 176°F |
| 100°C | 212°F |

<!-- NEEDS REVIEW: resistance-vs-temperature curve graph. Only the X-axis (temperature) tick marks in the table above are legible from OCR. The graph appears to show an "Acceptable" range band, but the Y-axis (resistance) values and the actual curve are too garbled to transcribe reliably (raw OCR fragment: "1 ye ©"). Refer to the original PDF p.210 for the actual curve. -->

---
<a id="p211"></a>

<!-- NEEDS REVIEW: applied-vacuum vs. voltage-drop table below has broken column alignment (PDF p.211) -->
**[PDF p.211](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=211)** — VACUUM SENSOR

### VACUUM SENSOR — INSPECTION

**1. Inspect power source voltage of vacuum sensor**

1. Disconnect the vacuum sensor connector.
2. Turn the ignition switch ON.
3. Using a voltmeter, measure the voltage between connector terminals VC and E2 of the wiring harness side.
   - Voltage: 4.5 - 5.5 V <!-- NEEDS REVIEW: OCR shows "45-5.5V"; read as 4.5-5.5 V, consistent with the same VC reference-voltage spec appearing elsewhere in this chapter's ECU wiring connector voltage table (terminal VC-E2) -->
4. Turn the ignition switch OFF.
5. Reconnect the vacuum sensor connector.

**2. Inspect power output of vacuum sensor**

1. Turn the ignition switch ON.
2. Disconnect the vacuum hose on the air intake manifold side.
3. Connect a voltmeter to terminals PIM and E2 of the ECU and measure the output voltage under ambient atmospheric pressure. <!-- NEEDS REVIEW: OCR shows "EG:2" where "ECU" is expected; read as ECU by context -->
4. Apply vacuum to the vacuum sensor in 13.3 kPa (100 mmHg, 3.94 in.Hg) segments up to 66.7 kPa (500 mmHg, 19.69 in.Hg). <!-- NEEDS REVIEW: this step's OCR is heavily fragmented ("mmHg, 3.94 in.Hg) segments to 66.7 kPa (500 moe / 19.69 in.Hg)"); the mmHg/in.Hg unit values are standard conversions of the kPa figures and are transcribed with reasonable confidence, but exact original phrasing is uncertain -->
5. Measure the voltage drop from step 3 above for each segment.
6. Reconnect the vacuum hose to the intake manifold.

**Voltage drop table:**

| Applied vacuum (kPa) | Voltage drop (V) |
|---|---|
| 13.3 | 0.3 - 0.5 |
| 26.7 | 0.7 - 0.9 |
| 40.0 | 1.1 - 1.3 |
| 53.5 | 1.5 - 1.7 |

<!-- NEEDS REVIEW: applied-vacuum/voltage-drop table — OCR shows raw digit strings "133 | 267 | 400 | 535" for the kPa row with no decimal points. These are reconstructed as 13.3/26.7/40.0/53.5 kPa, consistent with the 13.3 kPa step size stated in the procedure text above. The procedure text implies the vacuum is stepped up to 66.7 kPa (500 mmHg), suggesting a possible 5th column, but no further legible data survives in the OCR beyond a stray unreadable fragment ("4."). Verify the full table, including whether a 66.7 kPa row exists, against the source PDF p.211. -->

---
<a id="p212"></a>
**[PDF p.212](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=212)** — KNOCK SENSOR .

### KNOCK SENSOR — COMPONENTS & INSPECTION

<!-- NEEDS REVIEW: exploded-view component diagram graphics on this page are not recoverable from OCR; only the inspection procedure text below is transcribed (PDF p.212) -->

1. Remove surge tank.
2. Remove knock sensor.
   - Disconnect the knock sensor connector.
   - Using SST, remove the knock sensor. (SST 09816-30010)
3. Inspect knock sensor.
   - Using an ohmmeter, check that there is no continuity between the terminal and body.
   - If there is continuity, replace the sensor.
4. Reinstall knock sensor.
   - Using SST, install the knock sensor. (SST 09816-30010)
   - Torque: 44 N·m (450 kgf-cm, 33 ft·lbf) → [torque-specs #t078](09-torque-specs.md#t078)
   - Connect the knock sensor connector.
5. Reinstall surge tank.

---
<a id="p213"></a>

<!-- NEEDS REVIEW: oxygen sensor feedback-voltage inspection flowchart is garbled diagram OCR (PDF p.213) -->
**[PDF p.213](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=213)** — KNOCK SENSOR .

<!-- NEEDS REVIEW: running header merged with unreadable trailing diagram noise -->

### OXYGEN SENSOR — INSPECTION

1. Inspect heater resistance of oxygen sensor.
   - Disconnect the oxygen sensor connector.
   - Using an ohmmeter, measure the resistance between terminals +B and HT.
   - Resistance: 11-16 Ω at 20°C (68°F)
   - If the resistance is not as specified, replace the sensor.
   - Torque: 44 N·m (450 kgf-cm, 33 ft·lbf) → [torque-specs #t079](09-torque-specs.md#t079)
   - Reconnect the oxygen sensor connector.
2. Warm up engine — allow the engine to warm up to normal operating temperature.
3. Inspect feedback voltage.
   - Connect the positive (+) tester probe of a voltmeter to terminal VF1 of the check connector, and the negative (-) tester probe to terminal E1.
   - HINT: Use SST when connecting between terminals TE1 and E1 of the check connector. Do the test as described. (SST 09843-18020)

**Feedback-voltage check flowchart (steps 4+, reconstructed from garbled diagram OCR spanning p.213-214):**

<!-- NEEDS REVIEW: from this point the source is a flowchart diagram, not numbered procedural text. The step numbers below (4 onward) are added by this cleanup for readability and do not appear in the source. The OCR appears to contain duplicated/overlapping passes over the same diagram boxes — in particular, the fluctuation-count check (step 5) appears twice with different figures: one occurrence reads "8 times or more" / "Less than 8 times", another reads "5 times or more". Both are shown below; the correct threshold could not be confidently determined from OCR and should be verified against the source PDF (p.213-214). Branch destinations ("If OK" / "If NG") for steps 5-10 are best-effort reconstructions from the legible fragments and are not fully traceable to explicit arrows/labels in the source. -->

| Step | Check | Condition | Std Value | If OK → | If NG/Bad → |
|---|---|---|---|---|---|
| 1 | Heater resistance of oxygen sensor | Ohmmeter between terminals +B and HT | 11-16 Ω at 20°C (68°F) | Reconnect connector, go to step 2 | Replace the oxygen sensor |
| 2 | Warm up engine | Allow engine to reach normal operating temperature | — | Go to step 3 | — |
| 3 | Connect voltmeter for feedback voltage | (+) probe to terminal VF1 of check connector, (-) probe to terminal E1; use SST 09843-18020 to connect terminals TE1 and E1 of the check connector | — | Go to step 4 | — |
| 4 | Warm up oxygen sensor | Maintain engine speed at 2,500 rpm for approx. 120 seconds | — | Go to step 5 | — |
| 5 | Count voltmeter needle fluctuations | With engine held at 2,500 rpm, count fluctuations of the voltmeter needle in 10 seconds | 8 times or more (OCR also shows a conflicting "5 times or more" fragment — see review note) | Sensor circuit judged OK; go to step 6 | Less than 8 times → go to step 6 |
| 6 | Re-check with check connector disconnected | Disconnect terminals TE1 and E1 of the check connector; maintain engine speed at 2,500 rpm; measure voltage between VF1 and E1 (continued on p.214) | — | More than 0 V → go to step 7 | 0 V → go to step 7 |
| 7 (p.214) | Read diagnostic trouble codes | Read and record DTCs (see DTC Tables page) | — | Normal code / code Nos. 21 and 25 → go to step 8 | Malfunction code(s) (except Nos. 21, 25) → repair the relevant diagnostic trouble code(s) |
| 8 (p.214) | Re-measure feedback voltage | Disconnect terminals TE1 and E1 of check connector again; maintain engine speed at 2,500 rpm; measure voltage between VF1 and E1 | — | 5 V → go to step 9 (see review note) | 0 V → go to step 9 (see review note) |
| 9 (p.214) | Check with PCV hose disconnected | Disconnect the PCV hose; measure voltage between VF1 and E1 | — | More than 0 V → go to step 10 | 0 V → Repair (Over rich) |
| 10 (p.214) | Simulate warm coolant temperature and re-check | Disconnect water temp. sensor connector; connect a resistor with a resistance of 4-8 kΩ (or send an equivalent simulation signal); connect terminals TE1 and E1 of check connector; warm up oxygen sensor at 2,500 rpm for approx. 120 seconds; maintain 2,500 rpm; measure voltage between VF1 and E1 | Resistor: 4-8 kΩ | 0 V → Replace the oxygen sensor | Other reading → Repair (Over lean) |

---
<a id="p214"></a>

<!-- NEEDS REVIEW: oxygen sensor feedback-voltage inspection flowchart continues, garbled diagram OCR (PDF p.214) -->
**[PDF p.214](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=214)** — OXYGEN SENSOR

*(Continued from PDF p.213 — see the step-sequence table above, steps 7-10, for the reconstructed flowchart logic that spans both pages.)*

---
<a id="p215"></a>

<!-- NEEDS REVIEW: "ECU Wiring Connectors Voltage" reference table below has broken column alignment (PDF p.215) -->
**[PDF p.215](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=215)** — OXYGEN SENSOR

### ENGINE ECU — INSPECTION

HINT: The EFI circuit can be checked by measuring resistance and voltage at the wiring connectors of the engine ECU.

1. Preparation (see EFI check procedure in Troubleshooting w/ Volt, Ohmmeter).
2. Inspect voltage of ECU.
   - Turn the ignition switch ON.
   - Measure the voltage between each terminal of the connectors.
   - HINT:
     - Perform all voltage measurements with the connectors connected.
     - Verify that the battery voltage is 11 V or more when the ignition switch is ON.

**Engine ECU Terminals (connector pinout diagram)**

<!-- NEEDS REVIEW: the ECU connector pinout diagram (physical terminal position grid) on this page is illegible ASCII-art-like OCR noise and could not be reconstructed. Only the terminal designators that also appear by name in the value table below are recoverable (PDF p.215). -->

**ECU Wiring Connectors Voltage:**

| Terminal pair | Condition | Voltage (V) |
|---|---|---|
| BATT-E1 | (condition not legible) | (value not legible) <!-- NEEDS REVIEW: this row's condition and value are almost entirely garbled in OCR; only the terminal pair "BATT-E1" is confidently legible --> |
| +B-E1 | IG SW ON | 9-14 |
| VC-E2 | IG SW ON | 4.5-5.5 <!-- NEEDS REVIEW: OCR shows "45-55"; read as 4.5-5.5 V, the standard ECU sensor reference voltage, also consistent with the VC value on p.211 --> |
| VTA-E2 | IG SW ON (throttle valve fully closed) | (value not legible) <!-- NEEDS REVIEW: OCR shows "08-08", an internally inconsistent range; exact value not recoverable -->|
| VTA-E2 | IG SW ON (throttle valve open) | (value not legible) <!-- NEEDS REVIEW: OCR shows "B2-49"; exact value not recoverable --> |
| PIM-E2 | IG SW ON | 3.3-3.9 |
| #1-E01, E02 | IG SW ON | 9-14 |
| #2-E01, E02 | IG SW ON | 9-14 |
| #3-E01, E02 | IG SW ON | 9-14 |
| #4-E01, E02 | IG SW ON | 9-14 |
| THA-E2 | IG SW ON (intake air temp. 20°C (68°F)) | 0.6-3.4 <!-- NEEDS REVIEW: OCR shows "06=3.4"; read as 0.6-3.4 V, but decimal placement is not fully certain --> |
| THW-E2 | IG SW ON (coolant temp. 80°C (176°F)) | 0.2-1.0 <!-- NEEDS REVIEW: OCR shows "02-1.0"; read as 0.2-1.0 V --> |
| STA-E1 | Cranking | 6 or more |
| IGF-E1 | IG SW ON (igniter connector disconnected) | 4.5-5.5 <!-- NEEDS REVIEW: OCR shows "4.5~55"; read as 4.5-5.5 V, consistent with the VC-E2 value above --> |
| IGT-E1 | Idling | Pulse generation |
| RSC-E1 | IG SW ON (engine ECU connector disconnected) | 9-14 |
| RSO-E1 | IG SW ON (engine ECU connector disconnected) | 9-14 |

---
<a id="p216"></a>

<!-- NEEDS REVIEW: ECU wiring connector voltage table continues, broken column alignment (PDF p.216) -->
**[PDF p.216](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=216)** — OXYGEN SENSOR

**ECU Wiring Connectors Voltage (continued):**

| Terminal pair | Condition | Voltage (V) |
|---|---|---|
| W-E1 | No trouble (check engine warning light off) and engine running | 9-14 |
| AC1-E1 | IG SW ON (air conditioning ON) | (value not legible) <!-- NEEDS REVIEW: OCR shows "47.5 / or less" for this row, and a second, apparently duplicate row for the same terminal pair and condition immediately below shows "45-55" — the two could not be reconciled and both are transcribed for reference; see next row --> |
| AC1-E1 | IG SW ON (air conditioning ON) | 4.5-5.5 <!-- NEEDS REVIEW: see note on row above; this may be a duplicate/OCR-doubled reading of the same spec line rather than a genuinely separate row -->|
| VF-E1 | Maintain engine speed at 2,500 rpm for 2 minutes after warming up, then return to idling | 1.8-3.2 <!-- NEEDS REVIEW: OCR shows "18-32"; read as 1.8-3.2 V -->|
| G1-G- | Idling | Pulse generation |
| G2-G- | Idling | Pulse generation |
| OX-E1 | Maintain engine speed at 2,500 rpm for 2 minutes after warming up, then return to idling | Pulse generation |
| KNK-E1 | Idling | Pulse generation |
| ELS1-E1 | Electric cooling fan ON | 7.5-14 |
| ELS1-E1 | Electric cooling fan OFF | 0-1.5 <!-- NEEDS REVIEW: OCR shows "0-15"; read as 0-1.5 V by analogy with the 0-1.5 pattern in the ELS2/ELS3/ELS4 rows below, but could also be 0-15 --> |
| ELS2-E1 | Blower motor ON | 7.5-14 |
| ELS2-E1 | Blower motor OFF | 0-1.5 <!-- NEEDS REVIEW: see note on ELS1-E1 OFF row above --> |
| ELS3-E1 | Taillight switch ON | 7.5-14 |
| ELS3-E1 | Taillight switch OFF | 0-1.5 <!-- NEEDS REVIEW: see note on ELS1-E1 OFF row above --> |
| ELS4-E1 | Defogger switch ON | 7.5-14 |
| ELS4-E1 | Defogger switch OFF | 0-1.5 <!-- NEEDS REVIEW: see note on ELS1-E1 OFF row above --> |
| HT-E1 | IG SW ON | 9-14 |
| HT-E1 | Idling | 0-3 |
| FC-E1 | IG SW ON | 9-14 <!-- NEEDS REVIEW: terminal designator OCR'd as "FOL"/"FED"; read as "FC" (fuel cut / fuel pump control terminal) by analogy with the adjacent HT-E1 rows' condition pattern (IG SW ON / Idling), but the exact terminal name is uncertain --> |
| FC-E1 | Idling | 0-3 |
| TE1-E1 | IG SW ON | 9-14 |
| TE2-E1 | IG SW ON | 9-14 |

<!-- NEEDS REVIEW: several rows on this page (AC1-E1 duplicate, VF-E1, ELS1-4 OFF values, FC-E1 designator) required best-effort decimal-point or letter reconstruction from badly garbled OCR; see individual row comments above. Verify all values on this page against source PDF p.216 before relying on them for diagnostic work. -->

---
<a id="p217"></a>

<!-- NEEDS REVIEW: "ECU Wiring Connectors Resistance" reference table below has broken column alignment (PDF p.217) -->
**[PDF p.217](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=217)** — OXYGEN SENSOR

### ENGINE ECU — INSPECTION (continued)

3. Inspect resistance of ECU.
   - Turn the ignition switch OFF.
   - Disconnect the 3 connectors from the ECU.
   - Measure the resistance between each terminal of the wiring connectors.
   - NOTICE:
     - Do not touch the ECU terminals.
     - The tester probe should be inserted into the wiring connector from the wiring side.

**Engine ECU Terminals (connector pinout diagram)**

<!-- NEEDS REVIEW: the ECU connector pinout diagram (physical terminal position grid) on this page is illegible ASCII-art-like OCR noise and could not be reconstructed. Only the terminal designators that also appear by name in the value table below are recoverable (PDF p.217). -->

**ECU Wiring Connectors Resistance:**

| Terminal pair | Condition | Resistance (Ω) |
|---|---|---|
| VTA-E2 | Throttle valve fully open | 2,400-11,200 |
| VTA-E2 | Throttle valve fully closed | 340-6,300 |
| VC-E2 | (condition not legible) | 3,100-7,200 |
| THA-E2 | Intake air temp. 20°C (68°F) | 2,000-3,000 |
| THW-E2 | Coolant temp. 80°C (176°F) | 200-400 |
| G1, G2-G- | Cold (-10°C (14°F) to 50°C (122°F)) | 125-200 |
| G1, G2-G- | Hot (50°C (122°F) to 100°C (212°F)) | 160-250 |
| NE-G- | Cold (-10°C (14°F) to 50°C (122°F)) | 125-200 |
| NE-G- | Hot (50°C (122°F) to 100°C (212°F)) | 160-250 |
| RSC-+B | Cold (-10°C (14°F) to 50°C (122°F)) | 17-24.5 <!-- NEEDS REVIEW: OCR shows "17-245"; read as 17-24.5 Ω by inserting a decimal before the final digit, but this is not corroborated elsewhere in the document — verify against source PDF --> |
| RSC-+B | Hot (50°C (122°F) to 100°C (212°F)) | 21.5-28.5 |
| RSO-+B | Cold (-10°C (14°F) to 50°C (122°F)) | 17-24.5 <!-- NEEDS REVIEW: see note on RSC-+B Cold row above --> |
| RSO-+B | Hot (50°C (122°F) to 100°C (212°F)) | 21.5-28.5 <!-- NEEDS REVIEW: OCR shows "215-285" here vs. "21.5—28.5" (with decimal clearly visible) on the RSC-+B Hot row directly above for what appears to be the identical spec; normalized to match the clearer OCR occurrence --> |
| HT-+B | (condition not legible; likely 20°C (68°F) per the matching oxygen sensor heater resistance spec on p.213) | 11-16 |

---
<a id="p218"></a>
**[PDF p.218](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=218)** — FUELCUT RPM

### FUEL CUT RPM — INSPECTION

1. Warm up engine — allow the engine to warm up to normal operating temperature.
2. Connect tachometer to engine (see EM section).
3. Inspect fuel cutoff operation.
   - Increase the engine speed to at least 2,500 rpm.
   - Check for injector operating noise.
   - Check that when the throttle lever is released, injector operating noise stops momentarily and then resumes.
   - HINT: Measure with the A/C OFF.
   - Fuel return speed: 1,400 rpm
4. Disconnect tachometer.

---
<a id="p219"></a>
**[PDF p.219](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=219)** — FUELCUT RPM

### Appendix — Manual Chapter Index (source back matter)

Toyota 4A-GE repair manual, 20V 'Blacktop'

1. Preparation
2. Service Specifications
3. Charging
4. Engine Mechanical
5. Ignition
6. Lubrication
7. Cooling
8. Electronic Fuel Injection
9. Starting System

<!-- NEEDS REVIEW: this back-matter chapter list (source PDF p.219) is transcribed as-is; its chapter numbering/ordering does not match this wiki's own chapter files/links elsewhere in the manual -->

---

