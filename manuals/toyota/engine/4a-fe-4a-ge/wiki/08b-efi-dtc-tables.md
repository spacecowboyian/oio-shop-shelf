# Electronic Fuel Injection — DTC Reference Tables (part 2 of 7)

*Section code: `FI` | PDF pages 154-158 | ECU terminal value measurement, full DTC code table, driving-pattern detection tests for codes 21/25, diagnosis circuit inspection flowchart.*

Other parts of this chapter: [System/Diagnosis Basics](08a-efi-system-diagnosis.md) · [Troubleshooting 1](08c-efi-troubleshooting-1.md) · [Troubleshooting 2](08d-efi-troubleshooting-2.md) · [Fuel/Injector](08e-efi-fuel-injector.md) · [Throttle Body](08f-efi-throttle-body.md) · [Sensors/Relays](08g-efi-sensors-relays.md)

See also: [Torque Specifications index](09-torque-specs.md) for every torque value in this manual with links back to source.

---
<a id="p154"></a>

<!-- NEEDS REVIEW: multi-column diagnostic code table (Code No./System/Diagnosis/Trouble Area/Memory/Page) below has broken column alignment from OCR of a scanned table (PDF p.154). Several code numbers in this table were not legible in the OCR at all (marked "illegible" below) and need verification against the source PDF. The diagram surrounding the ECU/break-out-box illustration also produced large amounts of unreadable glyph noise, which has been omitted below as non-content rather than transcribed. -->
**[PDF p.154](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=154)** — DIAGNOSISSYSTEM

### ECU Terminal Values: Measurement Using Break-Out-Box and Hand-Held Tester

Diagram: ECU connected via vehicle harness to an interface box, then to the break-out-box and hand-held tester.

1. Hook up the break-out-box and hand-held tester to the vehicle.
2. Read the ECU input/output values by following the prompts on the tester screen.

HINT: Hand-held tester has a "Snapshot" function. This records the measured values and is effective in the diagnosis of intermittent problems. Please refer to the hand-held tester/break-out-box operator's manual for further details.

### Diagnostic Codes

If a malfunction is detected during the diagnostic code check, refer to the circuit indicated in the table, and turn to the corresponding page.

Your readings may vary from the parameters listed in the table, depending on the instruments used.

| Code No. | System | Diagnosis Mode | Memory | Diagnosis (detection condition) | Trouble Area | Page |
|---|---|---|---|---|---|---|
| (Normal) | Normal | - | - | Output when no other [malfunction code] is present | - | - |
| illegible | RPM Signal (G circuit) | ON | N.A. | No "G" or "NE" signal input to ECU for 2 sec. or more | Open in G-circuit; ECU | - |
| illegible | RPM Signal (NE circuit) | ON | ON | No NE signal to ECU for [value] msec. or more, at 1,000 rpm or more | Open or short in NE circuit; Distributor; ECU | - |
| illegible | IGF Signal | ON | N.A. | No IGF signal to ECU for 4 consecutive IGT signals | Open or short in IGF circuit from igniter to ECU | Fi-26 |
| 21 (see [p.156](#p156) heading) | Oxygen Sensor Signal (OX) | OFF | ON | Oxygen sensor signal fixed between 0.35-0.70 V continuously for 60 sec. or more, at normal driving speed below 100 km/h (60 mph) (2 trip detection logic) | Open or short in oxygen sensor circuit; Sensor; ECU | Fi-21 / Fi-29 / Fi-68 / Fi-66 (unclear which page ref applies here vs. the following row) |
| illegible | Water Temp Signal (THW) | ON | ON | Open or short in water temp sensor circuit for 0.5 sec. or more | Open or short in water temp sensor circuit; ECU | Fi-10 |
| illegible | Intake Air Temp Signal (THA) | unclear | unclear | Open or short in intake air temp sensor circuit for 0.5 sec. or more | Open or short in intake air temp sensor circuit; ECU | table continues on [p.155](#p155) |

<!-- NEEDS REVIEW: code numbers for the "RPM Signal (G circuit)", "RPM Signal (NE circuit)", "IGF Signal", "Water Temp Signal", and "Intake Air Temp Signal" rows above were not legible anywhere in the OCR text and have been left as "illegible" rather than guessed. The exact msec. threshold in the NE-circuit row's detection condition was also illegible (a fragment reading "[50 rpm" appeared but its placement relative to "msec. or more" and "1,000 rpm or more" was ambiguous, so no number has been filled in). The Oxygen Sensor Signal row's trouble-area/page-reference text visually bled together with the following page's Vacuum Sensor (code 31) row in the OCR; the four "Fi-" page numbers listed could not be reliably split between the two rows. -->

---
<a id="p155"></a>

<!-- NEEDS REVIEW: diagnostic code table continues from PDF p.154 with the same broken column alignment (PDF p.155) -->
**[PDF p.155](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=155)** — DIAGNOSISSYSTEM

### Diagnostic Codes (cont'd)

Column header row in source also includes "Number of blinks of Check Engine Warning light": a bar-chart-style blink pattern shown as an icon per code, which did not OCR as usable text and is omitted from the table below (each code still has a distinct blink count in the source; refer to the PDF for the graphic).

| Code No. | System | Diagnosis Mode | Memory | Diagnosis (detection condition) | Trouble Area | Page |
|---|---|---|---|---|---|---|
| 25 | Air-Fuel Ratio Lean Malfunction | OFF | ON | Oxygen sensor output less than 0.45 V for at least 90 sec. when oxygen sensor is warmed up (racing at 1,500 rpm or more) (2 trip detection logic, see note *3 below) | Open in injector circuit; fuel line pressure blockage; ignition system (spark plug, ignition coil, igniter); gear shift(?); air intake leak; open or short in oxygen sensor circuit | - |
| 31 | Vacuum Sensor Signal (PIM) | ON | ON | Open or short in vacuum sensor signal for 0.5 sec. or more | Open or short in vacuum sensor circuit; ECU | - |
| 33 | ISC (Idle Speed Control) Valve Signal | ON | ON | Open or short in idle speed control valve circuit | Open or short in idle speed control valve circuit | Fi-27 |
| 41 | Throttle Position Sensor Signal (VTA) | OFF | ON | Open or short in throttle position sensor circuit for 0.5 sec. or more | Open or short in throttle position sensor circuit; ECU | Fi-19 |
| illegible | Vehicle Speed Signal | ON | OFF | No vehicle speed signal to ECU for at least 8 sec. during heavy load, between 2,000 rpm and 5,000 rpm | Open or short in vehicle speed sensor circuit; ECU | - |
| 43 | Starter Signal (STA) | N.A. | OFF | No starter signal to ECU when cranking, with Test mode | Open or short in starter switch circuit or starter relay circuit; ECU | Fi- (number illegible) |
| 52 | No.1 Knock Sensor Signal (KNK1) | ON | N.A. | No No.1 knock sensor signal to ECU with engine racing, between [value] rpm and 6,000 rpm | Open or short in knock sensor circuit; Knock sensor (looseness); ECU | Fi- (number illegible) |
| reads "463" (see review note) | Knock-related control signal (front side)? | ON | N.A. | [detection condition text garbled] between 700 rpm and 6,000 rpm | ECU | - |
| 51 | Switch Condition Signal | OFF | N.A. / ON | TE1 and E1 terminals connected, with check [switch: accelerator pedal / A-C, unclear] in test mode | ECU | - |

Column notes (from the manual's own footnotes on this page):

- "Diagnosis Mode": "ON" indicates that the check engine warning light lights up when a malfunction is detected. "OFF" indicates that the check engine warning light does not light up during malfunction diagnosis, even if a malfunction is detected.
- "Memory": "O" in the memory column indicates that a diagnostic code is recorded in the ECU memory when a malfunction occurs. "X" indicates that a diagnostic code is not recorded in the ECU memory even if a malfunction occurs. Accordingly, output of diagnostic results is performed with the ignition switch ON.
- *3: "2 trip detection logic." (See step 4(c) in trouble codes output (normal mode).)

<!-- NEEDS REVIEW: the row printed as code "463" in the OCR (front-side / crank-angle-related row, between codes 52 and 51) is very likely a garbled single- or double-digit code number rather than literally 463, but there isn't enough legible surrounding text to determine the real value or full detection condition, so it needs verification against the source PDF rather than a guess. The row for "Vehicle Speed Signal" (between codes 41 and 43) had no legible code number at all in the OCR. The rpm threshold in the No.1 Knock Sensor Signal (code 52) detection condition was illegible (only "and 6,000 rpm" was legible as the upper bound). The manual's footnote describes the Memory column using "O"/"X" symbols, but the table itself was OCR'd showing "ON"/"OFF"/"N.A." in that column, so the mapping between the footnote's O/X and the table's ON/OFF/N.A. values is preserved as-read but is not fully certain. -->

---
<a id="p156"></a>

<!-- NEEDS REVIEW: DTC driving-pattern timing diagram (code 21, oxygen sensor circuit) is garbled diagram OCR (PDF p.156) -->
**[PDF p.156](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=156)** — DIAGNOSIS SYSTEM

### Diagnostic Trouble Code Detection Driving Pattern

Purpose of the driving pattern:

1. To simulate diagnostic code detecting condition after diagnostic code is recorded.
2. To check that the malfunction is corrected when the repair is completed, by confirming that the diagnostic code is no longer detected.

**Code No. 21: Oxygen Sensor Circuit**
Malfunction: Deterioration of Oxygen Sensor

Diagram: vehicle speed vs. time, showing idle, then acceleration up through 64 km/h (40 mph) and 80 km/h (50 mph), with the detection point marked once vehicle speed is sustained in that range; IG switch OFF at the end.

| Step | Action |
|---|---|
| 1 | Disconnect the EFI fuse (15A) for 10 sec. or more, with IG switch OFF. |
| 2 | Initiate test mode (connect terminals TE2 and E1 of check connector with IG switch OFF). |
| 3 | Start the engine and warm it up with all accessories switched OFF. |
| 3a | Let the engine idle for 3 min. |
| 3b | Accelerate gradually within the range 1,300-1,700 rpm (centered around 1,500 rpm) with the A/C switch ON and 5th gear. (Take care that the engine speed does not fall below 1,200 rpm when shifting. Gradually depress the accelerator pedal and keep it steady so that engine braking does not occur.) |
| 3c | Maintain the vehicle speed at 64-80 km/h (40-50 mph). Keep the vehicle running for 1-2 min. after starting acceleration. |

HINT: If a malfunction exists, the malfunction indicator lamp will light up after approx. 60 sec. from the start of acceleration.

NOTICE: If the conditions in this test are not strictly followed, detection of the malfunction will not be possible.

---
<a id="p157"></a>

<!-- NEEDS REVIEW: DTC driving-pattern timing diagram (code 25, air-fuel ratio lean) is garbled diagram OCR (PDF p.157) -->
**[PDF p.157](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=157)** — DIAGNOSIS SYSTEM

### Diagnostic Trouble Code Detection Driving Pattern (cont'd)

Purpose of the driving pattern:

1. To simulate diagnostic code detecting condition after diagnostic code is recorded.
2. To check that the malfunction is corrected when the repair is completed, by confirming that the diagnostic code is no longer detected.

**Code No. 25: Air-Fuel Ratio Lean Malfunction**
Malfunction: Open or Short in Oxygen Sensor

Diagram: engine rpm vs. time, showing idle, three rapid accelerations up to 4,000 rpm, then holding at 2,000 rpm for 90 sec., with IG switch OFF at the end.

HINT: Before this test, check the feedback voltage for the oxygen sensor.

| Step | Action |
|---|---|
| 1 | Disconnect the EFI fuse (15A) for 10 sec. or more, with IG switch OFF. Initiate test mode (connect terminals TE2 and E1 of check connector with IG switch OFF). |
| 2 | Start engine and warm it up with all accessories switched OFF. |
| 3 | Let the engine idle for 3 min. |
| 4 | Accelerate rapidly to 4,000 rpm three times. |
| 5 | Maintain at 2,000 rpm for 90 seconds. |

HINT: If any malfunction is detected, the check engine warning light will light up during step [sentence is cut off in source, the step number is not given].

NOTICE: If the conditions in this test are not strictly followed, detection of the malfunction will not be possible.

<!-- NEEDS REVIEW: the final HINT sentence on this page ("...the check engine warning light will light up during step") is cut off in the OCR with no step number given, left as-is rather than guessing which step. -->

---
<a id="p158"></a>

<!-- NEEDS REVIEW: "DIAGNOSIS CIRCUIT INSPECTION" flowchart (check-engine-light circuit) is garbled diagram OCR; step order/branches (YES/NO, OK/BAD) could not be confidently reconstructed (PDF p.158) -->
**[PDF p.158](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=158)** — DIAGNOSISSYSTEM .

### Diagnosis Circuit Inspection

Diagram: EFI main relay and check-engine warning light wiring from the battery, through the EFI main relay, to the Engine ECU terminals BATT, +B, W, E1, and the check connector terminals TE1/E1.

Best-effort reconstruction of the check sequence below (branch order and which OK/BAD result feeds which subsequent step is uncertain in several places, see flagged note above):

| Step | Check | If YES/OK | If NO/BAD |
|---|---|---|---|
| 1 | Does check engine warning light come on when ignition switch is at ON? | System normal | Continue to step 2 |
| 2 | Does check engine warning light come on when engine ECU terminal W is grounded to the body? | Check wiring between engine ECU terminal E1 and body ground (OK) / Repair or replace (BAD) | Check bulb, fuse, and wiring between engine ECU and ignition switch; repair or replace |
| 3 | Does check engine warning light go off when the engine is started? | System normal | Check wiring between engine ECU and check engine warning light; repair if BAD |
| 4 | (malfunction/diagnostic code output check, condition text unclear) | Continue | Check wiring between engine ECU terminal TE1 and check connector terminal TE1, and between engine ECU terminal E1 and check connector terminal E1 |
| 5 | Does check engine warning light go off after repair according to malfunction code? | System OK; cancel out diagnostic code | Further repair required; try another engine ECU |

<!-- NEEDS REVIEW: step 4's check condition text ("shar lognonte cove eT Aplindipalaaes" in the raw OCR) could not be read at all and is left as "(condition text unclear)" rather than invented. The overall step numbering and which OK/NG branch loops back to which earlier step is a best-effort reading only; verify the actual flowchart against the source PDF before relying on this for diagnosis. -->

