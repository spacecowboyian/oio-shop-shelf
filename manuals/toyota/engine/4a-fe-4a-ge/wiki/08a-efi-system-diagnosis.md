# Electronic Fuel Injection — System Precautions & Diagnosis Basics (part 1 of 7)

*Section code: `FI` | PDF pages 145-153 | EFI/fuel system precautions, connector handling, fuel line service, diagnostic code output (normal/test mode).*

Other parts of this chapter: [DTC Tables](08b-efi-dtc-tables.md) · [Troubleshooting 1](08c-efi-troubleshooting-1.md) · [Troubleshooting 2](08d-efi-troubleshooting-2.md) · [Fuel/Injector](08e-efi-fuel-injector.md) · [Throttle Body](08f-efi-throttle-body.md) · [Sensors/Relays](08g-efi-sensors-relays.md)

See also: [Torque Specifications index](09-torque-specs.md) for every torque value in this manual with links back to source.

---
<a id="p145"></a>
**[PDF p.145](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=145)** — Electronic Fuel Injection (EFI)

### Chapter Contents (FI section page index)

| Section | Manual page |
|---|---|
| EFI System | FI-1 |
| Diagnosis System | FI-5 |
| Troubleshooting w/ Volt, Ohmmeter | FI-14 |
| Reference Value of Engine ECU Data | FI-30 |
| Fuel Pump | FI-31 |
| Fuel Pressure Regulator | FI-37 |
| Injector | FI-39 |
| Throttle Body | FI-45 |
| Camshaft Timing Oil Control [Valve] | FI-56 |
| ISC Valve | FI-57 |
| EFI Main Relay | FI-60 |
| Circuit Opening Relay | FI-61 |
| VSV for EVAP | FI-62 |
| Water Temperature Sensor | FI-64 |
| Intake Air Temperature (IAT) Sensor | FI-65 |
| Vacuum Sensor | *(garbled: "FLés")* |
| Knock Sensor | *(garbled: "FROZ")* |
| Oxygen Sensor | *(page number not visible in OCR)* |
| Engine ECU | FI-70 |
| Fuel Cut RPM | FI-73 |

<!-- NEEDS REVIEW: page numbers for Vacuum Sensor, Knock Sensor, and Oxygen Sensor in this chapter TOC ([p.145](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=145)) are illegible/missing in the OCR ("FLés", "FROZ", and no page number at all for Oxygen Sensor) — not guessed at. Also the "CAMSHAFT TIMING OIL CONTROL" entry appears truncated (a garbled "7|" follows where another word, likely "VALVE", would be expected) but was not completed since uncertain. -->

---
<a id="p146"></a>
**[PDF p.146](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=146)** — EFISYSTEM

### EFI SYSTEM

#### Precaution

1. Before working on the fuel system, disconnect the negative (–) terminal cable from the battery.
   HINT: Any diagnostic trouble code retained by the computer will be erased when the negative (–) terminal cable is removed from the battery. Therefore, if necessary, read the diagnosis before removing the negative (–) terminal cable from the battery.
2. Do not smoke or work near an open flame when working on the fuel system.
3. Keep gasoline away from rubber or leather parts.

#### Maintenance Precautions

1. PRECAUTION WHEN CONNECTING GAUGE
   (a) Use battery as the power source for the timing light, tachometer, etc.
   (b) Connect the tester probe of a tachometer to the terminal IGO© of the check connector. <!-- NEEDS REVIEW: line is garbled ("HL doen a" prefix); likely a terminal symbol/name preceding "of the check connector" -->

2. IN EVENT OF ENGINE MISFIRE, FOLLOWING PRECAUTIONS SHOULD BE TAKEN
   (a) Check proper connection of battery terminal cables, etc.
   (b) Handle high-tension cords carefully.
   (c) After repair work, check that the ignition coil terminals and all other ignition system lines are reconnected securely.
   (d) When cleaning the engine compartment, be especially careful to protect the electrical system from water.

3. PRECAUTIONS WHEN HANDLING OXYGEN SENSOR
   (a) Do not allow oxygen sensor to drop or hit against an object.
   (b) Do not allow the sensor to come into contact with water.

#### Air Induction System

1. Separation of the engine oil dipstick, oil filler cap, PCV hose, etc. may cause the engine to run out of tune.

---
<a id="p147"></a>
**[PDF p.147](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=147)** — EFISYSTEM

### EFI SYSTEM (continued)

#### Air Induction System (continued)

2. Disconnection, looseness or cracks in the parts of the air induction system between the throttle body and cylinder head will allow air suction and cause the engine to run out of tune.

#### Electronic Control System

1. Before removing EFI wiring connectors, terminals, etc., first disconnect the power by either turning the ignition switch OFF or disconnecting the negative (–) terminal cable from the battery.

   HINT: Always check the diagnostic code before disconnecting the negative (–) terminal cable from the battery. When installing the battery, be especially careful not to incorrectly connect the positive (+) and negative (–) cables.

   Do not permit parts to receive a severe impact during removal or installation. Handle all EFI parts carefully, especially the ECU.

   Do not be careless during troubleshooting as there are numerous transistor circuits and even slight terminal contact can cause further troubles.

   Do not open the ECU cover.

   When inspecting during rainy weather, take care to prevent entry of water. Also, when washing the engine compartment, prevent water from getting on the EFI parts and wiring connectors.

   Parts should be replaced as an assembly.

   Care is required when pulling out and inserting wiring connectors.
   (a) Release the lock and pull out the connector, pulling on the connectors.
   (b) Fully insert the connector and check that it is locked.

   *(Diagram callout: "Press Down" — connector-release illustration.)*

   When inspecting a connector with a volt/ohmmeter:
   (a) Carefully take out the water-proofing rubber if it is a water-proof type connector.
   (b) Insert the test probe into the connector from the wiring side when checking the continuity, amperage or voltage.
   (c) Do not apply unnecessary force to the terminal.
   (d) After checking, install the waterproofing rubber on the connector securely.

<!-- NEEDS REVIEW: the "Electronic Control System" precautions on p.147 (https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=147) read as one long unnumbered paragraph in the OCR, ending with a jump to item "10." on p.148 ("Use SST for inspection or test of the injector..."). The source likely split this content across numbered items 2-9, but the individual item numbers/boundaries could not be recovered from the OCR and were not guessed at. -->

---
<a id="p148"></a>
**[PDF p.148](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=148)** — 30070

### EFI SYSTEM (continued)

#### Electronic Control System (continued)

10. Use SST for inspection or test of the injector or its wiring connector.
    SST 09842-30070

#### Fuel System

1. When disconnecting the high pressure fuel line, a large amount of gasoline will spill out, so observe the following procedures:
   (a) Put a container under the connection.
   (b) Slowly loosen the connection.
   (c) Disconnect the connection.
   (d) Plug the connection with a rubber plug.

2. When connecting the flare nut or union bolt on the high pressure pipe union, observe the following procedures:

   **Union Bolt Type:**
   (a) Always use a new gasket.
   (b) Tighten the union bolt by hand.
   (c) Tighten the union bolt to the specified torque.
       Torque: 29.5 N-m (300 kgf-cm, 22 ft-Ibf)  → [torque-specs #t057](09-torque-specs.md#t057)

   **Flare Nut Type:**
   (a) Apply a light coat of engine oil to the flare and tighten the flare nut by hand.
   (b) Using SST, tighten the flare nut to the specified torque.
       SST 09631-22020
       Torque: 30 N-m (310 kgf-cm, 22 ft-lbf)  → [torque-specs #t058](09-torque-specs.md#t058)
       HINT: Use a torque wrench with a fulcrum length of 30 cm (11.81 in.).

3. Observe the following precautions when removing and installing the injectors.
   (a) Never reuse the O-ring.
   (b) When placing a new O-ring on the injector, take care not to damage it in any way.
   (c) Coat a new O-ring with spindle oil or gasoline before installing — never use engine, gear or brake oil.

---
<a id="p149"></a>
**[PDF p.149](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=149)** — 30070

### EFI SYSTEM (continued)

#### Fuel System (continued)

4. Install the injector to delivery pipe and intake manifold as shown in the illustration.
5. Check that there are no fuel leaks after performing maintenance anywhere on the fuel system.
   (a) Using SST, connect terminals +B and FP of the check connector.
       SST 09843-18020
   (b) Turn the ignition switch ON.
       NOTICE: Do not start the engine.
   (c) Pinch the fuel return hose. The pressure in the high pressure line will rise to approx. 392 kPa (4 kgf/cm², 57 psi). In this state, check to see that there are no leaks from any part of the fuel system.
       NOTICE: Always pinch the hose. Avoid bending as it may cause the hose to crack.
   (d) Turn the ignition switch OFF.
   (e) Remove the SST from the check connector.
       SST 09843-18020

---
<a id="p150"></a>
**[PDF p.150](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=150)** — 30070

### DIAGNOSIS SYSTEM

#### Check Engine Warning Light

*(Figure: "CHECK" engine warning light indicator.)*

1. The check engine warning light will come on when the ignition switch is at ON and the engine is not running.
2. When the engine is started, the check engine warning light should go off. If the light remains on, the diagnosis system has detected a malfunction or abnormality in the system.

#### Diagnostic Codes Output

**Normal mode:**

To obtain an output of diagnostic codes, proceed as follows:

1. Initial conditions
   (a) Battery voltage 11 V or more
   (b) Throttle valve fully closed
   (c) Accessories switched OFF
   (d) Engine at normal operating temperature
2. Turn the ignition switch ON.
   CAUTION: Do not start the engine.
3. Using SST, connect terminals TE1 and E of the check connector. <!-- NEEDS REVIEW: OCR shows only "E" here, not "E1" as elsewhere on this page and on p.152 ("TE1 and E1", "TE2 and E1") for what appears to be the same check-connector terminal — likely an OCR-dropped "1", but the digit was not guessed at -->
   SST 09843-18020
4. Read the diagnostic code as indicated by the number of flashes of the check engine warning light.

#### Diagnostic Codes

(a) Normal System Operation (no malfunction)
    - The light will alternately blink ON and OFF at 0.26 second intervals.
(b) Malfunction Code Indication
    - In the event of a malfunction, the light will blink every 0.52 seconds. The 1st number of blinks will equal the 1st digit of a 2 digit diagnostic code, and after a 1.5 second pause, the 2nd number of blinks will equal

---
<a id="p151"></a>

<!-- NEEDS REVIEW: the diagnostic-code blink-pattern timing chart and "2 trip detection logic" flowchart on this page (PDF p.151) are heavily garbled diagram OCR; blink counts/timings could not be confidently verified -->
**[PDF p.151](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=151)** — DIAGNOSISSYSTEM

### DIAGNOSIS SYSTEM (continued)

#### Diagnostic Codes (continued)

the second digit. If there are 2 or more codes, there will be a 2.5 second pause between each code. After all the codes have been output, there will be a 4.5 second pause and they will all be repeated, as long as the terminals TE1 and E1 of the check connector are connected.

HINT: In the event of a number of trouble codes, indication will begin from the smaller value and continue to the larger.

*(Diagram: blink-pattern timing chart showing "Code No.13" and "Code No.31" examples with 0.52-second ON/OFF blink intervals and 1.5/2.5/4.5-second pauses between digits and codes — see NEEDS REVIEW above.)*

(c) 2 trip detection logic:

Diagnostic code 21 uses "2 trip detection logic". With this logic, when a malfunction is first detected, the malfunction is temporarily stored in the ECU memory. If the same malfunction is detected again during the second drive test, this second detection causes the warning light to light up. The 2 trip [logic] repeats the same mode a 2nd time. (However, the ignition switch must be turned OFF between the 1st time and 2nd time.) In the Test Mode, the check engine warning light lights up the 1st time a malfunction is detected.

*(Diagram: ignition-switch "2 trips" pattern chart — see NEEDS REVIEW above.)*

5. After the diagnosis check, remove the SST from the check connector.
   SST 09843-18020

**Test mode:**

HINT:
- Compared to the normal mode, the test mode has increased sensing ability to detect malfunctions.
- It can also detect malfunctions in the starter signal circuit, air conditioning signal.
- Furthermore, the same diagnostic items which are detected in the normal mode can also be detected in the test mode.

To obtain an output of diagnostic codes, proceed as follows:

1. Initial conditions
   (a) Battery voltage 11 V or more
   (b) Throttle valve fully closed
   (c) Accessories switched OFF
2. Turn the ignition switch OFF.

---
<a id="p152"></a>
**[PDF p.152](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=152)** — DIAGNOSIS SYSTEM

### DIAGNOSIS SYSTEM (continued)

#### Diagnostic Codes Output (continued) — Test mode

3. First, using SST, connect terminals TE2 and E1 of the check connector.
   SST 09843-18020
   Turn the ignition switch ON to begin the diagnosis in the test mode.
   HINT: To confirm that the test mode is operating, check that the check engine warning light flashes when the ignition switch is turned ON.
4. Start the engine and drive the vehicle at a speed of 10 km/h (6 mph) or higher.
5. Simulate the conditions of the malfunction described by the customer.
6. Using SST, connect terminals TE1 and E1 of the check connector.
   SST 09843-18020
7. Read the diagnostic code as indicated by the number of flashes of the check engine warning light.
8. After the diagnosis check, remove the SST from the check connector.
   SST 09843-18020

<!-- NEEDS REVIEW: step numbers 4-8 in this Test Mode diagnostic-code procedure (p.152) are not shown as explicit digits in the OCR — the steps run together as unlabeled sentences. They are presented here as a continuing numbered list in the order the OCR text appears, which is consistent with the "step 5" back-reference in the HINT block below, but the original numbering could not be independently verified. -->

HINT:
- The test mode will not start if terminals TE2 and E1 are connected after the ignition switch is turned ON.
- The starter signal and vehicle speed signal will be diagnosed by the ECU as malfunctions, and code Nos. 42 and 43 will be output, if the operation in step 5 is not done.
- When the air conditioning is on or when the accelerator pedal is depressed, code "51" (Switch condition signal) is output, but this is not abnormal.

#### Diagnostic Code Check Using Hand-Held Tester

1. Hook up the hand-held tester to the check connector.
2. Read the diagnostic codes by following the prompts on the tester screen. Please refer to the hand-held tester operator's manual for further details.

---
<a id="p153"></a>
**[PDF p.153](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=153)** — DIAGNOSIS SYSTEM

### DIAGNOSIS SYSTEM (continued)

#### Diagnostic Code Cancellation

After repair of the trouble area, the diagnostic code retained in memory by the ECU must be cancelled out by removing the EFI fuse (15A) for 10 seconds or more, depending on ambient temperature (the lower the temperature, the longer the fuse must be left out) with the ignition switch OFF.

HINT: Cancellation can also be done by removing the negative (–) terminal cable from the battery, but in this case, other memory systems (clock, etc.) will also be cancelled out.

- If the diagnostic code is not cancelled out, it will be retained by the ECU and appear along with a new code in the event of future trouble.
- If it is necessary to work on engine components requiring removal of the battery terminal, a check must first be made to see if a diagnostic code has been recorded.

After cancellation, road test the vehicle to check that a normal code is now read on the check engine warning light. If the same diagnostic code appears, it indicates that the trouble area has not been repaired thoroughly.

#### Diagnosis Indication

1. When 2 or more codes are indicated, the lowest number (code) will appear first.
2. All detected diagnostic codes, except code Nos. 42, and 51 under the test mode, will be retained in memory by the ECU from the time of detection until cancelled out. Once malfunction is cleared, the check engine warning light in the combination meter will go off but the diagnostic code(s) remains stored in ECU memory. <!-- NEEDS REVIEW: a code number between "42," and "and 51" is illegible in the OCR (rendered as a stray quote mark). Page 152 discusses codes 42, 43, and 51 together, so a missing "43" here is plausible but was not inserted — the digit could not be confirmed. -->

#### ECU Data Monitor Using Hand-Held Tester

1. Hook up the hand-held tester to the check connector.
2. Monitor the ECU data by following the prompts on the tester screen.
   HINT: Hand-held tester has a "Snapshot" function which records the monitored data. Please refer to the hand-held tester operator's manual for further details.

