# Electronic Fuel Injection — Fuel Pump, Pressure Regulator, Injector (part 5 of 7)

*Section code: `FI` | PDF pages 176-189 | Fuel pump, fuel pressure regulator, and injector inspection/removal/installation procedures.*

Other parts of this chapter: [System/Diagnosis Basics](08a-efi-system-diagnosis.md) · [DTC Tables](08b-efi-dtc-tables.md) · [Troubleshooting 1](08c-efi-troubleshooting-1.md) · [Troubleshooting 2](08d-efi-troubleshooting-2.md) · [Throttle Body](08f-efi-throttle-body.md) · [Sensors/Relays](08g-efi-sensors-relays.md)

See also: [Torque Specifications index](09-torque-specs.md) for every torque value in this manual with links back to source.

---
<a id="p176"></a>
**[PDF p.176](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=176)** — FUELPUMP

### FUEL PUMP — On-Vehicle Inspection

1. CHECK FUEL PUMP OPERATION
   1. Using SST, connect terminals +B and FP of the check connector.
      SST 09843-18020
      NOTICE: Do not connect the terminals wrong.
   2. Turn the ignition switch ON.
      NOTICE: Do not start the engine.
   3. Check that there is pressure in the fuel inlet hose from the fuel filter.
      HINT: If there is fuel pressure, you will hear the sound of the fuel flowing. If there is no pressure, check these parts:
      - Fusible link
      - Fuses
      - EFI main relay
      - Fuel pump
      - Wiring connections
   4. Turn the ignition switch OFF.
   5. Remove the SST from the check connector.
      SST 09843-18020

2. INSPECT FUEL PRESSURE
   1. Check that battery voltage is above 11 V.
   2. Disconnect the negative (–) terminal cable from the battery.
   3. Remove the union bolt and 2 gaskets, and disconnect the fuel inlet hose from the delivery pipe.
      HINT:
      - Put a suitable container or shop towel under the delivery pipe.
      - Slowly loosen the union bolt.
   4. Install the fuel inlet hose and SST (pressure gauge) to the delivery pipe with the 3 gaskets and SST (union bolt).
      SST 09268-45012
      Torque: 33 N-m (330 kgf-cm, 24 ft-Ibf)  → [torque-specs #t059](09-torque-specs.md#t059)
   5. Wipe off any splattered gasoline.
   6. Reconnect the negative (–) terminal cable to the battery.

<!-- NEEDS REVIEW: several short OCR noise fragments on this page ("sit" after the SST callout in step 1.5, "hen" after "battery voltage is above 11 V" in step 2.1, "ee" after step 2.3) appear to be column-bleed from adjacent page furniture and were omitted as unreadable rather than guessed at -->

---
<a id="p177"></a>
**[PDF p.177](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=177)** — FUEL PUMP

### FUEL PUMP — On-Vehicle Inspection (continued)

2. INSPECT FUEL PRESSURE (continued)
   7. Using SST, connect terminals +B and FP of the check connector.
      SST 09843-18020
   8. Turn the ignition switch ON.
   9. Measure the fuel pressure.

      | Test condition | Fuel pressure |
      |---|---|
      | Static (ignition ON, engine off) | 235 – 275 kPa (2.4 – 2.8 kgf/cm², 34 – 40 psi) |
      | Idle, vacuum sensing hose disconnected & plugged | 235 – 275 kPa (2.4 – 2.8 kgf/cm², 34 – 40 psi) |
      | Idle, vacuum sensing hose connected | 196 kPa (2.0 kgf/cm², 28 psi) |

      If pressure is high, replace the fuel pressure regulator. If pressure is low, check these parts:
      - Fuel hoses and connections
      - Fuel pump
      - Fuel filter
      - Fuel pressure regulator
   10. Remove the SST from the check connector.
       SST 09843-18020
   11. Start the engine.
   12. Disconnect the vacuum sensing hose from the fuel pressure regulator, and plug the hose end.
   13. Measure the fuel pressure at idle (see table above — vacuum sensing hose disconnected & plugged row).
   14. Reconnect the vacuum sensing hose to the fuel pressure regulator.
   15. Measure the fuel pressure at idle (see table above — vacuum sensing hose connected row).
       If pressure is not as specified, check the vacuum sensing hose and fuel pressure regulator.
   16. Stop the engine.
   17. After checking fuel pressure, disconnect the negative (–) terminal cable from the battery and carefully remove the SST to prevent gasoline from splashing.
       SST 09268-45012
   18. Connect the fuel inlet hose to the delivery pipe with 2 new gaskets and the union bolt.
       Torque: 33 N-m (330 kgf-cm, 24 ft-Ibf)  → [torque-specs #t060](09-torque-specs.md#t060)
       Check for fuel leaks.

3. REMOVE REAR SEAT CUSHION
4. REMOVE FLOOR SERVICE HOLE COVER
5. DISCONNECT FUEL PUMP & SENDER GAUGE CONNECTOR

<!-- NEEDS REVIEW: step numbers 3-5 above (REMOVE REAR SEAT CUSHION / REMOVE FLOOR SERVICE HOLE COVER / DISCONNECT FUEL PUMP & SENDER GAUGE CONNECTOR) are not shown as explicit digits in the OCR; they are presented as a continuing numbered list based on the explicit "6." that follows on p.178 ("6. INSPECT FUEL PUMP RESISTANCE") and the explicit "8./9./10." (reconnect/reinstall, the reverse actions) later on p.178 — the sequence is very likely correct but the exact digits 3-5 could not be independently confirmed from the source. Stray fragments "QPog" and "Ld" near these lines and near "Check for fuel leaks." above were omitted as unreadable OCR noise. -->

---
<a id="p178"></a>
**[PDF p.178](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=178)** — FUEL PUMP

### FUEL PUMP — On-Vehicle Inspection (continued)

6. INSPECT FUEL PUMP RESISTANCE

   Using an ohmmeter, measure the resistance between terminals 4 and 5.

   | Test | Spec |
   |---|---|
   | Resistance (terminals 4–5) | 0.2 – 3.0 Ω at 20°C (68°F) |

   If the resistance is not as specified, replace the fuel pump.

7. INSPECT FUEL PUMP OPERATION

   Connect the positive (+) lead from the battery to terminal 4 of the connector, and the negative (–) lead to terminal 5. Check that the fuel pump operates.

   If operation is not as specified, replace the fuel pump.

   NOTICE:
   - These tests must be performed quickly (within 10 seconds) to prevent the coil from burning out.
   - Keep the fuel pump as far away from the battery as possible.
   - Always perform switching at the battery side.

8. RECONNECT FUEL PUMP & SENDER GAUGE CONNECTOR
9. REINSTALL FLOOR SERVICE HOLE COVER
10. REINSTALL REAR SEAT CUSHION

<!-- NEEDS REVIEW: a stray "5" appears immediately before "6." in the OCR at the start of step 6 ([p.178](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=178)) — likely a diagram terminal callout bleeding into the text rather than part of the step number, omitted here -->

---
<a id="p179"></a>
**[PDF p.179](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=179)** — FUEL PUMP

### FUEL PUMP — Components (diagram)

Exploded-view diagram of the fuel pump assembly. Labeled parts visible in the OCR: Clip, Rubber Cushion.

**Legend:**
- N-m (kgf-cm, ft-lbf): Specified torque

<!-- NEEDS REVIEW: diagram label rendered as "Rubber   Cushi   R" ([p.179](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=179)) — reconstructed as "Rubber Cushion" based on the matching term used in the prose on p.180/p.181 ("Remove the rubber cushion from the fuel pump"), but the exact OCR fragment was garbled; verify against original scan -->

---
<a id="p180"></a>
**[PDF p.180](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=180)** — FUEL PUMP

### FUEL PUMP — Removal

CAUTION: Do not smoke or work near an open flame when working on the fuel pump.

1. REMOVE REAR SEAT CUSHION
2. REMOVE FLOOR SERVICE HOLE COVER
   1. Remove the service hole cover.
   2. Disconnect the fuel pump & sender gauge connector.
      INSTALLATION HINT: Check fuel leakage.
3. DISCONNECT FUEL PIPE AND HOSE FROM FUEL PUMP BRACKET
   CAUTION: Remove the fuel filter cap to prevent the fuel from flowing out.
   1. Using SST, disconnect the outlet pipe from the pump bracket.
      SST 09631-22020
      Torque: 30 N-m (310 kgf-cm, 22 ft-Ibf)  → [torque-specs #t061](09-torque-specs.md#t061)
      INSTALLATION HINT: Use a torque wrench with a fulcrum length of 30 cm (11.81 in.).
   2. Disconnect the return hose from the pump bracket.
4. REMOVE FUEL PUMP BRACKET ASSEMBLY FROM FUEL TANK
   1. Remove the 8 bolts.
      Torque: 3.4 N-m (35 kgf-cm, 30 in.-Ibf)
   2. Pull out the pump bracket assembly.
   3. Remove the gasket from the pump bracket.
      INSTALLATION HINT: Install a new gasket to the pump bracket.

### FUEL PUMP — Disassembly

1. REMOVE FUEL PUMP FROM FUEL PUMP BRACKET
   1. Pull off the lower side of the fuel pump from the pump bracket.
   2. Disconnect the fuel pump connector.
   3. Disconnect the fuel hose from the fuel pump, and remove the fuel pump.
      Remove the rubber cushion from the fuel pump.

<!-- NEEDS REVIEW: torque line "Torque: 3.4 N-m (35 kgf-cm, 30 in.-Ibf)" in step 4.1 above ([p.180](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=180)) has no torque-specs index link in the source content (unlike the other torque callouts on this page), and a stray fragment "GGnhe-os" appeared after the "DISASSEMBLY" heading in the OCR — omitted as unreadable page-code noise -->

---
<a id="p181"></a>
**[PDF p.181](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=181)** — FUEL PUMP

### FUEL PUMP — Disassembly (continued)

2. REMOVE FUEL PUMP FILTER FROM FUEL PUMP
   1. Using a small screwdriver, remove the clip.
   2. Pull out the pump filter.
      ASSEMBLY HINT: Install the pump filter with a new [word missing in source].
3. REMOVE FUEL SENDER GAUGE FROM FUEL PUMP BRACKET
   1. Disconnect the fuel sender gauge connector.
   2. Remove the 2 screws and sender gauge.
4. REMOVE CONNECTOR
   Remove the 2 screws, connector support, connector gasket.
   INSTALLATION HINT: Install the connector with a new gasket.

### FUEL PUMP — Reassembly

Reassembly is in the reverse order of disassembly.

### FUEL PUMP — Installation

Installation is in the reverse order of removal.

<!-- NEEDS REVIEW: ASSEMBLY HINT in step 2.2 above ([p.181](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=181)) is cut off mid-word ("Install the pump filter with anew") — likely continues "...with a new clip" but the missing word is not guessed at -->

---
<a id="p182"></a>
**[PDF p.182](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=182)** — FUEL PRESSURE REGULATOR

### FUEL PRESSURE REGULATOR — On-Vehicle Inspection

INSPECT FUEL PRESSURE
(See step 2 in on-vehicle inspection in fuel pump).

### FUEL PRESSURE REGULATOR — Components (diagram)

Exploded-view diagram of the fuel pressure regulator.

**Legend:**
- N-m (kgf-cm, ft-lbf): Specified torque
- ● Non-reusable part

<!-- NEEDS REVIEW: torque callout fragment "(70, 60 in.)" on this diagram ([p.182](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=182)) is incomplete in the OCR — likely the same 7.0 N-m (70 kgf-cm, 60 in.-Ibf) installation torque given in full on p.183, but the fragment itself does not include the "7.0 N-m"/"kgf-cm" portion so it is not being restated as a confirmed value here; refer to the original PDF page. Legend fragment "susablepart" is likewise reconstructed above as "Non-reusable part" (the same legend used on the p.185 COMPONENTS diagram) with reduced confidence — verify against original scan. -->

### FUEL PRESSURE REGULATOR — Removal

1. DISCONNECT VACUUM SENSING HOSE FROM FUEL PRESSURE REGULATOR
2. DISCONNECT FUEL RETURN HOSE FROM FUEL PRESSURE REGULATOR
   HINT: Put a suitable container or shop towel under the pressure regulator.
3. REMOVE FUEL PRESSURE REGULATOR
   1. Remove the 2 bolts, and pull out the pressure regulator.
   2. Remove the O-ring from the pressure regulator.

---
<a id="p183"></a>
**[PDF p.183](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=183)** — FUEL PRESSURE REGULATOR

### FUEL PRESSURE REGULATOR — Installation

1. INSTALL FUEL PRESSURE REGULATOR
   1. Apply a light coat of gasoline to a new O-ring, and install it to the pressure regulator.
   2. While turning the pressure regulator left and right, install it to the delivery pipe.
      Install the pressure regulator with the 2 bolts.
      Torque: 7.0 N-m (70 kgf-cm, 60 in.-Ibf)  → [torque-specs #t062](09-torque-specs.md#t062)
2. CONNECT FUEL RETURN HOSE TO FUEL PRESSURE REGULATOR
3. CONNECT VACUUM SENSING HOSE TO FUEL PRESSURE REGULATOR
4. START ENGINE AND CHECK FOR FUEL LEAKAGE

---
<a id="p184"></a>
**[PDF p.184](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=184)** — INJECTOR

### INJECTOR — On-Vehicle Inspection

4. INSPECT INJECTOR OPERATION

   Check operation sound from each injector.

   1. With the engine running or cranking, use a sound scope to check that there is normal operating noise in proportion to engine speed.
   2. If you have no sound scope, you can check the injector operation with your finger.
      If no sound or unusual sound is heard, check the wiring connector, injector or injection signal from the ECU.

INSPECT INJECTOR RESISTANCE
1. Disconnect the injector connector.
2. Using an ohmmeter, measure the resistance between the terminals.

   | Test | Spec |
   |---|---|
   | Resistance | 13.4 – 14.2 Ω at 20°C (68°F) |

   If the resistance is not as specified, replace the injector.
3. Reconnect the injector connector.

<!-- NEEDS REVIEW: the step number on "INSPECT INJECTOR OPERATION" reads "4." in the source OCR ([p.184](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=184)), even though it is the first step of a new ON-VEHICLE INSPECTION section for the injector — preserved as literally OCR'd rather than silently changed to "1." -->

---
<a id="p185"></a>
**[PDF p.185](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=185)** — INJECTOR

### INJECTOR — Components (diagram)

Exploded-view diagram of the throttle body / injector / delivery pipe assembly. Labeled parts visible in the OCR: Link Rod.

**Legend:**
- N-m (kgf-cm, ft-lbf): Specified torque
- ● Non-reusable part

Torque callout visible in the OCR: 7.0 N-m (70 kgf-cm, 60 in.-Ibf).

<!-- NEEDS REVIEW: a second torque callout on this diagram reads "17.0 (70, 6O In.-ttst))" in the OCR ([p.185](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=185)) — this likely represents the same 7.0 N-m (70 kgf-cm, 60 in.-Ibf) torque shown elsewhere on this page and cross-referenced on p.189 (cable/link bracket bolts), but the leading "1" and garbled unit text ("6O", "ttst") are not being silently corrected. The literal OCR string is preserved here for the record rather than restated as a value: "17.0 (70, 6O In.-ttst))" — verify against original scan. -->

---
<a id="p186"></a>
**[PDF p.186](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=186)** — INJECTOR

### INJECTOR — Removal

1. DISCONNECT ACCELERATOR CABLE FROM THROTTLE BODY
2. REMOVE LINK BRACKET AND CABLE BRACKET
   1. Disconnect link rod from link bracket.
   2. Remove the 2 bolts and link bracket.
   3. Remove the 2 bolts and cable bracket.
3. DISCONNECT INJECTOR CONNECTORS
4. REMOVE INJECTORS
   1. Remove the bolt and injector cover. Remove the 2 injector covers.
   2. Remove the insulator from each injector.
   3. Pull out the 4 injectors from throttle body.
   4. Remove the 2 O-rings and insulator from each injector.

### INJECTOR — Inspection

1. INSPECT INJECTOR INJECTION

   CAUTION: Keep injector clear of sparks during the test.

   1. Remove the throttle body assembly. (See Throttle Body)
   2. Install the 4 injectors to throttle body assembly.
   3. Remove the union bolt and 2 gaskets, and disconnect the fuel inlet hose from the fuel filter outlet.

---
<a id="p187"></a>
**[PDF p.187](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=187)** — INJECTOR

### INJECTOR — Inspection (continued)

*(Diagram on this page labels the SST test setup: Bolt, Gasket, SST (Union), SST (Hose), Fuel Hose.)*

4. Connect SST (union and hose) to the fuel filter outlet with the 2 gaskets and union bolt.
   SST 09268-41046 (90405-09015, 95336-08070)
   Torque: 29.5 N-m (300 kgf-cm, 22 ft-Ibf)  → [torque-specs #t063](09-torque-specs.md#t063)
5. Connect SST (union and hose) to the throttle body assembly with the 2 gaskets and union bolt.
6. Using SST, connect terminals +B and FP of the check connector.
   SST 09843-18020
7. Reconnect the negative (–) terminal cable to the battery.
8. Turn the ignition switch ON.
   NOTICE: Do not start the engine.
9. Using a graduated cylinder, test each injector [garbled in source: "22-or8"] times.
   SST 09842-30070

   | Test | Spec |
   |---|---|
   | Injection volume | 65 – 82 cm³ ([digit missing in source].0 – 5.0 cu in.) per 15 sec |
   | Difference between each injector | 5 cm³ (0.3 cu in.) or less |

   If the injection volume is not as specified, replace the injector.

   INSPECT LEAKAGE

   In the condition above, disconnect the test probes (wire) from the battery and check the fuel leakage from the injector.
   SST 09842-30070

   | Test | Spec |
   |---|---|
   | Fuel drop (leakage) | One drop or less per minute |

<!-- NEEDS REVIEW: "Test each injector 22-or8 times" ([p.187](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=187)) is garbled — likely a small repeat count such as "2 or 3 times" but not confidently readable, so the literal OCR fragment is preserved rather than guessed at. Similarly, the injection volume spec "65 - 82 cm³ (.0 - 5.0 cu in.)" is missing a leading digit before ".0" in the source (the cu-in. figure should presumably start with a digit matching 65 cm³, e.g. "4.0"), but no digit has been inserted — refer to the original PDF page. Stray fragments "jaan", "Ne", "VES", "C3", "O", "oa", "Sa", "rE" scattered around this page's diagram/procedure text were omitted as unreadable column-bleed noise. -->

---
<a id="p188"></a>
**[PDF p.188](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=188)** — INJECTOR

### INJECTOR — Inspection (continued)

10. Turn the ignition switch OFF.
11. Disconnect the negative (–) terminal cable from the battery.
12. Remove the SST.
    SST 09268-41046 (90405-09015, 95336-08070), 09843-18020
13. Reinstall the fuel inlet hose to the fuel filter outlet with 2 new gaskets and the union bolt.
    Torque: 29.5 N-m (300 kgf-cm, 22 ft-Ibf)  → [torque-specs #t064](09-torque-specs.md#t064)
14. Remove the 4 injectors from the throttle body assembly.
15. Reinstall the throttle body assembly. (See Throttle Body)

### INJECTOR — Installation

1. INSTALL INJECTORS AND DELIVERY PIPE
   1. Install 2 new O-rings and a new insulator to each injector.
   2. Apply a light coat of gasoline to 2 new O-rings.
   3. Push in the 4 injectors.
   4. Position the injector connector upward.
   5. Install 4 new insulators.

<!-- NEEDS REVIEW: steps 10-15 above continue the numbered INSPECT LEAKAGE procedure from p.187, whose explicit numbering stopped after step 9; the OCR shows these as lettered sub-steps (b)-(g) of an unlabeled step rather than explicit numbers, so the numbering 10-15 here is inferred continuation, not confirmed from the source -->

---
<a id="p189"></a>
**[PDF p.189](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=189)** — INJECTOR

### INJECTOR — Installation (continued)

1. INSTALL INJECTORS AND DELIVERY PIPE (continued)
   6. Temporarily install the injector cover with the bolt. Install the 2 injector covers.
   7. Check that the injectors rotate smoothly.
      HINT: If the injectors do not rotate smoothly, the probable cause is incorrect installation of the O-rings. Replace the O-rings.
   8. Position the injector connector upward.
   9. Tighten the bolt holding the injector cover to the throttle body. Hold the 2 injector covers.
      Torque: 7.0 N-m (70 kgf-cm, 60 in.-Ibf)  → [torque-specs #t065](09-torque-specs.md#t065)
2. CONNECT INJECTOR CONNECTORS
3. INSTALL LINK BRACKET AND CABLE BRACKET
   1. Install the cable bracket with the 2 bolts.
      Torque: 7.0 N-m (70 kgf-cm, 60 in.-Ibf)  → [torque-specs #t066](09-torque-specs.md#t066)
   2. Install the link bracket with the 2 bolts.
      Torque: 7.0 N-m (70 kgf-cm, 60 in.-Ibf)  → [torque-specs #t067](09-torque-specs.md#t067)
   3. Connect the link rod to the link bracket.
4. CONNECT ACCELERATOR CABLE TO THROTTLE BODY

<!-- NEEDS REVIEW: sub-step numbering 6-9 under step 1 above ([p.189](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=189)) continues the lettered sequence (f)-(i) from the OCR, which is a reasonable but inferred continuation of the 5 sub-steps shown on p.188; not independently confirmed. A short garbled fragment ("insta ae / a / vant") between "Temporarily install the injector cover with the bolt." and "Install the 2 injector covers." was condensed into the reconstructed sentence above — "insta" clearly continues to "install" and "boit" to "bolt", but the isolated fragments "ae" and "vant" could not be placed and were omitted as unreadable. -->

