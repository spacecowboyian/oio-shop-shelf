# Fuel and Emissions — Part F

Honda S2000 service manual, printed pages 11-454 through 11-546 (PDF pp. 750–842).

### Printed page 11-454

<a id="p750"></a>
Source: [PDF p.750, printed p.11-454](../page-images/p0750.png).

# Idle Control System
## DTC Troubleshooting (cont'd)

12. Update the E C M if it does not have the latest software (see page 11-216), or substitute a known-good E C M (see page 11-217).

13. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

14. Check for Temporary DTCs or DTCs with the HDS.
Is DTC P0507 indicated?
- **Y E S** — C h e c k for poor connections or loose terminals at the throttle body and the E C M . If the ECM was updated, substitute a known-good E C M (see page 11-217), then go to step 13. If the E C M was substituted, go to step 1.
- **NO** — Go to step 15.

15. Monitor the OBD S T A T U S for DTC P0507 in the DTCs MENU with the HDS.
Does the screen indicate PASSED?
- **YES** — If the E C M was updated, troubleshooting is complete. If the ECM w a s substituted, replace the original E C M (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 14, go to the indicated D T C s troubleshooting.
- **NO** — If the screen indicates FAILED, check for poor connections or loose terminals at the throttle body and the E C M . If the ECM w a s updated, substitute a known-good E C M (see page 11-217), then go to step 13. If the E C M was substituted, go to step 1. If the screen indicates EXECUTING, keep idling until a result comes on. If the screen indicates O U T OF CONDITION, go to step 13.

**Page Reference:** 11-454

---

### Printed page 11-455

<a id="p751"></a>
Source: [PDF p.751, printed p.11-455](../page-images/p0751.png).

# A/C Signal Circuit Troubleshooting

1. Start the engine, and let it idle.
2. Turn the blower switch on.
3. Turn the A/C switch on.
4. Check the A/C CLUTCH in the DATA LIST with the HDS.
   Does it indicate ON?
   - **YES** — Go to step 5.
   - **NO** — Go to the A/C pressure switch circuit troubleshooting (see page 21-58).

5. Check the A/C system.
   Does the A/C system operate?
   - **YES** — The air conditioning system circuit is OK.
   - **NO** — Go to step 6.

6. Turn the ignition switch OFF.
7. Turn the ignition switch ON (II).
8. Activate the A/C CLUTCH in the INSPECTION MENU with the HDS.
   Is there a clicking noise from the A/C compressor clutch?
   - **YES** — Do the A/C system test (see page 21-77).
   - **NO** — Go to step 9.

9. Momentarily connect under-hood fuse/relay box 16P connector terminal No. 11 to body ground with a jumper wire several times.

> **UNDER-HOOD FUSE/RELAY BOX CONNECTOR (16P)**
>
> | Pin | Wire Color | Terminal Type |
> | :---: | :---: | :---: |
> | 1 | - | Female |
> | 2 | - | Female |
> | 3 | - | Female |
> | 4 | - | Female |
> | 7 | - | Female |
> | 9 | - | Female |
> | **11** | **ACC (RED)** | **Female** |
> | 12 | - | Female |
> | 16 | - | Female |

- **JUMPER WIRE**: Connect to wire side of female terminals.

Is there clicking noise from the A/C compressor clutch?
   - **YES** — Repair open in the wire between the ECM (E18) and the A/C clutch relay.
   - **NO** — Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217), then recheck. If the symptom/indication goes away with a known-good ECM, replace the original ECM (see page 11-389).

**Page Reference**: 11-455

---

### Printed page 11-456

<a id="p752"></a>
Source: [PDF p.752, printed p.11-456](../page-images/p0752.png).

## Alternator FR signal circuit troubleshooting

1. Start engine and let it idle.
2. Monitor ALTERNATOR in HDS DATA LIST.
3. Turn headlights on. **Indicated percentage varies:** Alternator signal circuit is OK. **No change:** Go to step 4.
4. Turn headlights and ignition OFF.
5. Disconnect alternator 4P connector.
6. Turn ignition ON (II).
7. Measure voltage between ECM **A9 (LG1, BRN/YEL)** and **B13 (ALTF, WHT/RED)**. Continue with the source diagram and next page's branch.
8. Turn ignition OFF.
9. Jump SCS line with HDS.
10. Disconnect ECM connector B (24P).
11. Ground alternator 4P connector terminal **4 (ALTF, WHT/RED)** with a jumper wire.
12. Check continuity between body ground and ECM **B13 (ALTF, WHT/RED)**. Decision continues on next page.

The source image shows connector orientation.

---

### Printed page 11-457

<a id="p753"></a>
Source: [PDF p.753, printed p.11-457](../page-images/p0753.png).

## Alternator FR signal circuit troubleshooting (continued)

13. Turn ignition OFF.
14. Jump SCS line with HDS.
15. Disconnect ECM connector B (24P).
16. Check continuity between body ground and ECM **B13 (ALTF, WHT/RED)**. **Continuity:** Repair short between ECM B13 and alternator. **No continuity:** Update ECM software if needed (p. 11-216) or substitute a known-good ECM (p. 11-217), then recheck. If symptom disappears with known-good ECM, replace original ECM (p. 11-389).

See source image for connector orientation.

---

### Printed page 11-458

<a id="p754"></a>
Source: [PDF p.754, printed p.11-458](../page-images/p0754.png).

# Idle Control System
## Electrical Power Steering (EPS) Signal Circuit Troubleshooting

1. Start the engine, and let it idle.
2. Align the steering wheel straight ahead.
3. Check the EPS SIGNAL in the DATA LIST with the HDS.
   - Does it indicate LOW?
     - **YES** — Go to step 4.
     - **NO** — Go to step 6.

4. Turn the steering wheel quickly to the full lock position.
5. Check the EPS SIGNAL in the DATA LIST with the HDS.
   - Does it change to HIGH?
     - **YES** — The EPS signal circuit is OK.
     - **NO** — Go to step 12.

6. Turn the ignition switch OFF.
7. Jump the SCS line with the HDS.
8. Disconnect ECM connector E (31P).
9. Disconnect the EPS control unit 14P connector.
10. Connect ECM connector terminal E16 to body ground with a jumper wire.

### ECM CONNECTOR E (31P)
| Pin | Terminal Description |
|---|---|
| 1 | / |
| 2 | / |
| 3 | / |
| 4 | / |
| 5 | / |
| 6 | / |
| 7 | / |
| 8 | / |
| 9 | / |
| 10 | / |
| 11 | EPS LD (BLU/BLK) |
| 12 | / |
| 13 | / |
| 14 | / |
| 15 | / |
| 16 | / |
| 17 | / |
| 18 | / |
| 19 | / |
| 20 | / |
| 21 | / |
| 22 | / |
| 23 | / |
| 24 | / |
| 25 | / |
| 26 | / |
| 27 | / |
| 28 | / |
| 29 | / |
| 30 | / |
| 31 | / |

*Wire side of female terminals*

### JUMPER WIRE
*Wire side of female terminals*

11. Check for continuity between EPS control unit 14P connector terminal No. 13 and body ground.

### EPS CONTROL UNIT 14P CONNECTOR
| Pin | Terminal Description |
|---|---|
| 1 | / |
| 2 | / |
| 3 | / |
| 4 | / |
| 5 | / |
| 6 | / |
| 7 | / |
| 8 | / |
| 9 | / |
| 10 | / |
| 11 | EPS LD (BLU/BLK) |
| 12 | / |
| 13 | / |
| 14 | / |

*Wire side of female terminals*

- Is there continuity?
  - **YES** — Substitute a known-good EPS control unit (see page 17-62), and recheck.
  - **NO** — Repair open in the wire between the ECM (E17) and the EPS control unit.

*Page Reference: 11-458*

---

### Printed page 11-459

<a id="p755"></a>
Source: [PDF p.755, printed p.11-459](../page-images/p0755.png).

## EPS signal circuit troubleshooting (continued)

12. Turn ignition OFF.
13. Disconnect EPS control unit 14P connector.
14. Turn ignition ON (II).
15. Measure voltage between ECM **A9 (LG1, BRN/YEL)** and **E16 (EPSLD, BLU/BLK)**. **Battery voltage:** Substitute a known-good EPS control unit (p. 17-62), then recheck. **No voltage:** Go to step 16.
16. Turn ignition OFF.
17. Jump SCS line with HDS.
18. Disconnect ECM connector E (31P).
19. Check continuity between ECM **E16 (EPSLD, BLU/BLK)** and body ground. **Continuity:** Repair short between ECM E16 and EPS control unit. **No continuity:** Update ECM software if needed (p. 11-216) or substitute a known-good ECM (p. 11-217). If symptom disappears, replace original ECM (p. 11-389).

The source image shows connector orientation.

---

### Printed page 11-460

<a id="p756"></a>
Source: [PDF p.756, printed p.11-460](../page-images/p0756.png).

# Idle Control System
## Brake Pedal Position Switch Signal Circuit Troubleshooting

1. Turn the ignition switch ON (II).
2. Check the BRAKE SWITCH in the DATA LIST with the HDS.
   - Does it indicate OFF?
     - **YES** — Go to step 3.
     - **NO** — Inspect the brake pedal position switch (see page 22-144).

3. Press the brake pedal, and check the BRAKE SWITCH in the DATA LIST with the HDS.
   - Does it change to ON?
     - **YES** — The brake pedal position switch signal circuit (BKSW line) is OK.
     - **NO** — Go to step 4.

4. Turn the ignition switch OFF.
5. Jump the SCS line with the HDS.
6. Disconnect the brake pedal position switch 4P connector.
7. Disconnect ECM connector E (31P).
8. Check for continuity between ECM connector terminal E22 and body ground.

> **ECM CONNECTOR E (31P)**
> Wire side of female terminals
>
> | 1 | / | 13 | I | 4 | 5 | / | \ | 7 |
> |---|---|---|---|---|---|---|---|---|
> | I | I« | I » | / | 11 | 12 | 13 | 14 | 15 |
> | | | | 16 | 17 | 18 | 19 | 20 | 21 |
> | | | | 22 | / | 24 | 25 | / | 27 |
> | | | | | 28 | 29 | 30 | / | BKSW |
> | | | | | J | WHT/BLK) |

- Is there continuity?
  - **YES** — Repair short in the wire between the ECM (E22) and the brake pedal position switch.
  - **NO** — Go to step 9.

9. Check for continuity between ECM connector terminal E22 and brake pedal position switch 4P connector terminal No. 3.

> **ECM CONNECTOR E (31P)**
> Wire side of female terminals
>
> | 1 | M | 3 | | 4 | | 5 | / | \ | 7 | | 8 | | 9 |
> |---|---|---|---|---|---|---|---|---|---|---|---|---|
> | / | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
> | 22 | / | 24 | 25 | / | 27 | 28 | 29 | 30 | / | BKSW |
>
> **BRAKE PEDAL POSITION SWITCH 4P CONNECTOR**
>
> `BKSW` ^ (WHT/BLK) i - »

- Is there continuity?
  - **YES** — Repair open in the wire between the brake pedal position switch and the No. 47 STOP (15 A) fuse. Inspect the brake pedal position switch (see page 22-144).
  - **NO** — Repair open in the wire between the ECM (E22) and the brake pedal position switch.

> Page Reference: 11-460

---

### Printed page 11-461

<a id="p757"></a>
Source: [PDF p.757, printed p.11-461](../page-images/p0757.png).

# Idle Speed Inspection

**NOTE:**
*   Before checking the idle speed, check these items:
    *   The malfunction indicator lamp (MIL) has not been reported on.
    *   Ignition timing
    *   Spark plugs
    *   Air cleaner
    *   PCV system
*   Apply the parking brake, and make sure the headlights are off.

1.  Disconnect the evaporative emission (EVAP) canister purge valve connector.
2.  Connect the HDS to the data link connector (DLC) (A) located behind the driver's side of the front console.
3.  Turn the ignition switch ON (II).
4.  Make sure the HDS communicates with the ECM. If it doesn't, go to the DLC circuit troubleshooting (see page 11-367).
5.  Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
6.  Check the idle speed without load conditions—headlights, blower fan, radiator fan, and air conditioner off.
    *   Idle speed should be: **900 ± 50 rpm**
7.  Let the engine idle for 1 minute with high electric load (A/C switch ON, temperature set to max cool, blower fan on high, rear window defogger ON, and headlights on high beam).
    *   Idle speed should be: **900 ± 50 rpm**

**NOTE:** If the idle speed is not within specification, do the ECM idle learn procedure (see page 11-462). If the idle is still out of specification, go to the symptom troubleshooting.

8.  Reconnect the EVAP canister purge valve connector.

*Page Reference: 11-461*

---

### Printed page 11-462

<a id="p758"></a>
Source: [PDF p.758, printed p.11-462](../page-images/p0758.png).

# Idle Control System
## ECM Idle Learn Procedure

The idle learn procedure must be done so the E C M can learn the engine idle characteristics.

Do the idle learn procedure whenever you do any of these actions:
* Replace the E C M .
* Reset the E C M .
* Update the E C M .
* Replace or clean the throttle body.

**NOTE:** Erasing DTCs with the HDS does not require you to do the idle learn procedure.

### Procedure

1. Make sure all electrical items (A/C, audio, rear window defogger, lights, etc.) are off.
2. Reset the E C M with the HDS.
3. Turn the ignition switch ON (II), and wait 2 seconds.
4. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, or until the engine coolant temperature reaches 194 °F (90 °C).
5. Let the engine idle about 5 minutes with the throttle fully closed.

**NOTE:** If the radiator fan comes on, do not include its running time in the 5 minutes.

**Page Reference:** 11-462

---

### Printed page 11-463

<a id="p759"></a>
Source: [PDF p.759, printed p.11-463](../page-images/p0759.png).

## Fuel supply system — component location index

- Fuel feed line and fuel rail: engine compartment.
- Fuel tank: rear; replacement, p. 11-489.
- Fuel tank unit: includes fuel pump (replacement, p. 11-488), fuel gauge sending unit (replacement, p. 11-488; test, p. 11-494), fuel pressure regulator (replacement, p. 11-486), and fuel filter (replacement, p. 11-486).
- Fuel fill cap and fuel vapor line: rear.
- Fuel line quick-connect fittings: precautions, p. 11-480; removal, p. 11-481; installation, p. 11-483.
- PGM-FI main relay 1 (FI MAIN) and relay 2 (FUEL PUMP): driver's side dash.
- ECM: updating, p. 11-216; substitution, p. 11-217; replacement, p. 11-389.

The source image shows the component locations.

---

### Printed page 11-464

<a id="p760"></a>
Source: [PDF p.760, printed p.11-464](../page-images/p0760.png).

## DTC P0461: fuel level sensor circuit range/performance

Record freeze data and snapshot before troubleshooting (p. 11-213). The 162 mile (260 km) drive without refueling needed to complete this diagnosis means the DTC cannot be duplicated during this procedure.

1. Test fuel gauge sending unit (p. 11-494). **OK:** Check connections at sending unit and gauge assembly. **Faulty:** Replace sending unit (p. 11-488), then go to step 2.
2. Turn ignition ON (II).
3. Reset ECM with HDS.
4. Do ECM idle learn (p. 11-462).
5. Check DTCs with HDS. **P0461 indicated:** Check sending unit and gauge assembly connections, then return to step 1. **Not indicated:** Troubleshooting complete; follow any other indicated DTC procedures.

---

### Printed page 11-465

<a id="p761"></a>
Source: [PDF p.761, printed p.11-465](../page-images/p0761.png).

# DTC P0462: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Low Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS, and wait 5 seconds.
3. Check for Temporary DTCs or DTCs with the HDS.

| Is DTC P0462 Indicated? | Action |
| :--- | :--- |
| **Y** (Yes) | Go to step 4 |
| **N** (No) | Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the gauge control module and the fuel gauge sending unit.

4. Turn the ignition switch OFF.
5. Remove the rear tray (see page 20-73).
6. Remove the access panel from the floor.
7. Disconnect the fuel tank unit **5P** connector.
8. Turn the ignition switch ON (**II**).
9. Clear the DTC with the HDS, and wait 5 seconds.
10. Check for Temporary DTCs or DTCs with the HDS.

| Is DTC P0463 indicated? | Action |
| :--- | :--- |
| **Y** (Yes) | Replace the fuel gauge sending unit (see page 11-488), then go to step 22.
| **N** (No) | Go to step 11.

11. Turn the ignition switch OFF.
12. Remove gauge assembly (see page 22-89).
13. Disconnect gauge assembly **B 30P** connector.
14. Check for continuity between fuel tank unit **5P** connector terminal No. 2 and body ground.

> **FUEL TANK UNIT 5P CONNECTOR SIGNAL (YEL/BLK)**
> *Wire side of female terminals*
> \| 4 | 5 / ©

| Is there continuity? | Action |
| :--- | :--- |
| **Y** (Yes) | Repair short in the wire between gauge assembly (signal line) and the fuel gauge sending unit, then go to step 23.
| **N** (No) | Go to step 15.

15. Reconnect the gauge assembly **B 30P** connector.
16. Remove the fuel tank unit (see page 11-487).
17. Connect the fuel tank unit **5P** connector.
18. Turn the ignition switch ON (**II**).
19. Clear the DTC with the HDS.

*(cont'd)*

**Page Reference:** 11-465

---

### Printed page 11-466

<a id="p762"></a>
Source: [PDF p.762, printed p.11-466](../page-images/p0762.png).

# Fuel Supply System
## DTC Troubleshooting (cont'd)

20. Set the float (A) to the E position.
21. Check the fuel gauge.
Does the gauge move to the empty position?
- **YES** — Go to step 29.
- **NO** — Replace the gauge assembly (see page 22-89), then go to step 22.

22. Turn the ignition switch OFF.
23. Reconnect all connectors.
24. Install the parts in the reverse order of removal.
25. Turn the ignition switch ON (II).
26. Reset the ECM with the HDS.
27. Do the ECM idle learn procedure (see page 11-462).
28. Check for Temporary DTCs or DTCs with the HDS.
Is DTC P0462 indicated?
- **YES** — Check for poor connections or loose terminals at the gauge assembly and the fuel gauge sending unit, then go to step 1.
- **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

29. Install the parts in the reverse order of removal.
30. Reconnect all connectors.
31. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
32. Check for Temporary DTCs or DTCs with the HDS.
Is DTC P0462 indicated?
- **YES** — Check for poor connections or loose terminals at the gauge assembly and the fuel gauge sending unit, then go to step 1. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
- **NO** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

*Page Reference: 11-466*

---

### Printed page 11-467

<a id="p763"></a>
Source: [PDF p.763, printed p.11-467](../page-images/p0763.png).

# DTC P0463: Fuel Level Sensor(Fuel Gauge Sending Unit) Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS, and wait 5 seconds.
3. Check for Temporary DTCs or DTCs with the HDS.
   Is DTC P0463 indicated?
   - **Y** — Go to step 4.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the gauge assembly and the fuel gauge sending unit.

4. Turn the ignition switch OFF.
5. Remove the rear tray (see page 20-73).
6. Remove the access panel from the floor.
7. Disconnect the fuel tank unit 5P connector.
8. Connect fuel tank unit 5P connector terminal No. 1 to body ground with a jumper wire.
   **FUEL TANK UNIT 5P CONNECTOR**
   - **GND (BLK)**
   - Wire side of female terminals
9. Remove the gauge assembly (see page 22-89).
10. Disconnect the gauge assembly connector B (30P).
11. Check for continuity between gauge assembly connector B (30P) terminal No. 2 and body ground.
    **GAUGE ASSEMBLY CONNECTOR B (30P)**
    - Wire side of female terminals
    - Pins: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, [X]I23, 24, 25, 26, 27, 28, 29, 30
    Is there continuity?
    - **Y** — Go to step 12.
    - **NO** — Repair open in the wire between the gauge assembly (GND line) and the fuel gauge sending unit, then go to step 24.

*(cont'd)*

Page: 11-467

---

### Printed page 11-468

<a id="p764"></a>
Source: [PDF p.764, printed p.11-468](../page-images/p0764.png).

## DTC P0463 troubleshooting (continued)

12. Ground fuel tank unit 5P connector terminal **2 (SIGNAL, YEL/BLK)** with a jumper wire.
13. Check continuity between gauge assembly connector B (30P) terminal **10 (SIGNAL, YEL/BLK)** and body ground. **Continuity:** Go to step 14. **No continuity:** Repair open signal wire between gauge assembly and fuel gauge sending unit, then go to step 24.
14. Remove jumper from fuel tank unit connector.
15. Remove fuel tank unit (p. 11-487).
16. Test fuel gauge sending unit (p. 11-494). **OK:** Go to step 17. **Faulty:** Replace sending unit (p. 11-488), then go to step 23.
17. Connect fuel tank unit 5P connector.
18. Reconnect gauge assembly connector B (30P).
19. Turn ignition ON (II).
20. Clear DTC with HDS.

See source image for connector orientation.

---

### Printed page 11-469

<a id="p765"></a>
Source: [PDF p.765, printed p.11-469](../page-images/p0765.png).

## DTC P0463 troubleshooting (continued)

21. Set float (A) to F position.
22. Check fuel gauge. **Moves to full:** Go to step 30. **Does not:** Replace gauge assembly (p. 22-89), then go to step 23.
23. Turn ignition OFF.
24. Reconnect all connectors.
25. Install parts in reverse order of removal.
26. Turn ignition ON (II).
27. Reset ECM with HDS.
28. Do ECM idle learn (p. 11-462).
29. Check DTCs. **P0463 indicated:** Check gauge assembly and sending unit connections, then return to step 1; follow other indicated DTCs. **Not indicated:** Troubleshooting complete.
30. Install parts in reverse order of removal.
31. Reconnect all connectors.
32. Update ECM software if needed (p. 11-216) or substitute a known-good ECM (p. 11-217).
33. Check DTCs. **P0463 indicated:** Check gauge assembly and sending unit connections. If ECM was updated, substitute known-good ECM and recheck; if substituted, return to step 1. **Not indicated:** If updated, troubleshooting complete; if substituted, replace original ECM (p. 11-389). Follow other indicated DTCs.

---

### Printed page 11-470

<a id="p766"></a>
Source: [PDF p.766, printed p.11-470](../page-images/p0766.png).

# Fuel Supply System
## Fuel Pump Circuit Troubleshooting

If you suspect a problem with the fuel pump, check that the fuel pump actually runs; when it is on, you will hear some noise if you listen to the fuel fill port with the fuel fill cap removed. The fuel pump should run for 2 seconds when the ignition switch is first turned on. If the fuel pump does not make noise, check as follows:

1. Turn the ignition switch **OFF**.
2. Remove PGM-FI main relay 2 (**FUEL PUMP**) (A).
3. Turn the ignition switch **ON** (II).
4. Measure voltage between PGM-FI main relay 2 (**FUEL PUMP**) 4P connector terminal No. 4 and body ground.

> **PGM-FI MAIN RELAY 2 (FUEL PUMP) 4P CONNECTOR**
> Wire side of female terminals
> IGP1 (YEL/BLK)

Is there battery voltage?

*   **YES — Go to step 5.**
*   **NO — Repair open in the wire between PGM-FI main relay 1 (FL MAIN) and PGM-FI main relay 2 (FUEL PUMP).**

5. Measure voltage between PGM-FI main relay 2 (**FUEL PUMP**) 4P connector terminal No. 1 and body ground.

> **PGM-FI MAIN RELAY 2 (FUEL PUMP) 4P CONNECTOR**
> Wire side of female terminals

Is there battery voltage?

*   **YES — Go to step 6.**
*   **NO — Replace the No. 2 FUEL PUMP SRS (15 A) fuse in the under-dash fuse/relay box.**
    *   If needed, replace the under-dash fuse/relay box.

**Page Reference:** 11-470

---

### Printed page 11-471

<a id="p767"></a>
Source: [PDF p.767, printed p.11-471](../page-images/p0767.png).

## Fuel pump circuit troubleshooting (continued)

6. Turn ignition OFF.
7. Ground PGM-FI main relay 2 (FUEL PUMP) 4P terminal **3** with a jumper wire.
8. Turn ignition OFF.
9. Jump SCS line with HDS.
10. Disconnect ECM connector E (31P).
11. Check continuity between body ground and ECM **E17 (IMOFPR, GRN/YEL)**. **Continuity:** Go to step 12. **No continuity:** Repair open between fuel pump relay and ECM E17.
12. Reinstall PGM-FI main relay 2.
13. Ground ECM connector terminal E7 with a jumper wire.
14. Turn ignition ON (II).
15. Measure voltage between ECM E17 and body ground. **Battery voltage:** Go to step 16. **No voltage:** Replace PGM-FI main relay 2.

The source image shows connector orientation.

---

### Printed page 11-472

<a id="p768"></a>
Source: [PDF p.768, printed p.11-472](../page-images/p0768.png).

Fuel Supply System
Fuel Pump Circuit Troubleshooting (cont'd)
16. Turn the ignition switch OFF.
17. Reconnect E C M connector E (31P), and disconnect
the jumper wire.
18. Open the S C S line with the HDS.
19. Turn the ignition switch OFF.
20. Turn the ignition switch ON (II), and measure
voltage between ECM connector terminal E17 and
body ground within 2 seconds.
E C M C O N N E C T O R E (31P)
21. Turn the ignition switch OFF.
22. Remove the rear tray (see page 20-73).
23. Remove the access panel from the floor (see page
11-487).
24. Turn the ignition switch ON (II), and measure
voltage between fuel tank unit 5P connector
terminal No. 5 and body ground within 2 seconds.
F U E L T A N K UNIT 5P C O N N E C T O R
1 /' 3 4 I 5 / \ 7 8 | 9
/ 11 12 13 14 15 16 17 18 19 20 21
22
/ 24 25
/ 27 28 29 30
/ IMOFPR
J G R N / Y E L )
Wire side of female terminals
Is there battery voltage?
YES—Update the E C M if it does not have the latest
software (see page 11-216), or substitute a known-
good E C M (see page 11-217), then recheck. If the
symptom/indication goes away with a known-good
ECM, replace the original ECM (see page 11-389),
then go to step 21.
N O — G o to step 21.
VH7
F U E L PUMP
(YEL/GRN)
Wire side of female terminals
Is there battery voltage?
Y E S — G o to step 29.
N O — G o to step 25.
25. Turn the ignition switch OFF.
26. Remove PGM-FI main relay 2 (FUEL PUMP).
11-472

---

### Printed page 11-473

<a id="p769"></a>
Source: [PDF p.769, printed p.11-473](../page-images/p0769.png).

## Fuel pump circuit troubleshooting (continued)

27. Jump PGM-FI main relay 2 (FUEL PUMP) 4P connector terminals **1 and 2**.
28. Turn ignition ON (II) and measure voltage between fuel tank unit 5P terminal **5 (FUEL PUMP, YEL/GRN)** and body ground. **Battery voltage:** Replace PGM-FI main relay 2. **No voltage:** Repair open between relay 2 and fuel tank unit 5P connector.
29. Turn ignition OFF.
30. Check continuity between fuel tank unit 5P terminal **4 (GND, BLK)** and body ground. **Continuity:** Replace fuel pump. **No continuity:** Repair open between fuel tank unit 5P connector and G601.

See source image for connector orientation.

---

### Printed page 11-474

<a id="p770"></a>
Source: [PDF p.770, printed p.11-474](../page-images/p0770.png).

# Fuel Supply System
## Fuel Pressure Relieving

Before disconnecting fuel lines or hoses, relieve pressure from the system by disabling the fuel pump and then disconnecting the fuel tube/quick-connect fitting in the engine compartment.

### With the HDS
1. Make sure you have the anti-theft code for the audio system, then write down the audio presets.
2. Turn the ignition switch OFF.
3. Connect the HDS to the data link connector (DLC) **(A)** located behind the driver's side of the front console.
4. Turn the ignition switch ON (**II**).
5. Make sure the HDS communicates with the **E C M**. If it doesn't, go to the DLC circuit troubleshooting (see page 11-367).
6. Turn the ignition switch OFF.
7. Remove the fuel fill cap to relieve the pressure in the fuel tank.
8. Turn the ignition switch ON (**II**).
9. From the **INSPECTION MENU** of the HDS, select **Fuel Pump OFF**, then start the engine, and let it idle until it stalls.

> **NOTE:**
> * Do not allow the engine to idle above 1,000 rpm or the **E C M** will continue to operate the fuel pump.
> * A DTC or a Temporary DTC may be set during this procedure. Check for DTCs, and clear them as needed (see page 11-214).

10. Turn the ignition switch OFF.
11. Disconnect the negative cable from the battery.
12. Remove the quick-connect fitting cover **(A)**.

**Page Reference:** 11-474

---

### Printed page 11-475

<a id="p771"></a>
Source: [PDF p.771, printed p.11-475](../page-images/p0771.png).

## Fuel pressure relieving (continued)

**With HDS, continued:**
13. Check fuel quick-connect fitting for dirt; clean if needed.
14. Cover fitting with rag or shop towel.
15. Hold connector with one hand, squeeze retainer tabs with other to release locking tabs, and pull connector off. Do not damage line or use tools. If stuck, keep tabs pressed and alternately pull and push. Do not remove retainer; once removed, it must be replaced.
16. Check disconnected fitting for dirt or damage (step 4, p. 11-482).
17. Reconnect battery negative cable.
18. Enter audio anti-theft code and presets; set clock.

**Without HDS:**
1. Record audio anti-theft code and presets.
2. Remove PGM-FI main relay 2 (FUEL PUMP).
3. Start engine and idle until it stalls. If DTCs are stored, clear and ignore them.

See source image for quick-connect retainer orientation.

---

### Printed page 11-476

<a id="p772"></a>
Source: [PDF p.772, printed p.11-476](../page-images/p0772.png).

# Fuel Supply System
## Fuel Pressure Relieving (cont'd)

1. Turn the ignition switch OFF.
2. Remove the fuel fill cap.
3. Disconnect the negative cable from the battery.
4. Remove the quick-connect fitting cover (A).
5. Disconnect the quick-connect fitting (A): Hold the connector (B) with one hand, and squeeze the retainer tabs (C) with the other hand to release them from the locking tabs (D). Pull the connector off.

**NOTE:**
*   Be careful not to damage the line (E) or other parts.
*   Do not use tools.
*   If the connector does not move, keep the retainer tabs pressed down, and alternately pull and push the connector until it comes off easily.
*   Do not remove the retainer from the line; once removed, the retainer must be replaced with a new one.
6. After disconnecting the quick-connect fitting, check it for dirt or damage (see step 4 on page 11-482).
7. Reconnect the negative cable to the battery.
8. Enter the anti-theft code for the audio system, then enter the audio presets. Set the clock.

**Page Reference:** 11-476

---

### Printed page 11-477

<a id="p773"></a>
Source: [PDF p.773, printed p.11-477](../page-images/p0773.png).

## Fuel pressure test

Special tools: fuel pressure gauge 07406-004000B and attachment set 07AAJ-S6MA150.

1. Relieve fuel pressure (p. 11-474).
2. Disconnect quick-connect fitting; attach gauge set and gauge as shown in source image.
3. Start engine and idle. **Starts:** Go to step 5. **Does not start:** Go to step 4.
4. Listen at fuel filler port with cap removed. Pump should run for 2 seconds after ignition first turns ON. **Runs:** Go to step 5. **Does not:** Troubleshoot fuel pump circuit (p. 11-470).
5. Read gauge. Specification **380–430 kPa (3.9–4.4 kgf/cm², 55–63 psi)**. If out of specification, replace fuel pressure regulator and fuel filter (p. 11-486), then recheck.

## Fuel tank draining

1. Remove fuel tank unit (p. 11-487).
2. Draw fuel with hand pump, hose, and container suitable for fuel.
3. Install fuel tank unit (p. 11-487).

---

### Printed page 11-478

<a id="p774"></a>
Source: [PDF p.774, printed p.11-478](../page-images/p0774.png).

# Fuel Supply System
## Fuel Line Inspection

Check the fuel system lines and hoses for damage, leaks, and deterioration. Replace any damaged parts.

Make sure the connections are secure and the quick-connect fitting covers are firmly locked in place.

**Page Reference:** 11-478

---

### Printed page 11-479

<a id="p775"></a>
Source: [PDF p.775, printed p.11-479](../page-images/p0775.png).

## Fuel line inspection (continued)

Check all clamps and retighten if needed. Replace the fuel tank base gasket as indicated in the source diagram. The diagram shows fuel fill tube and vapor/fuel rail connections and clamp orientations:

- **A:** Align marks on fuel fill tube and pipe; clamp at 90° from upper side.
- **B:** Align marks on fuel fill tube and pipe; clamp at 90° from upper side. Position relative to tube end is shown at 0.24 in (6 mm) and 0.16 in (4 mm).
- **C:** Clamp at 115° from upper side.
- **D:** Clamp between 90° and 45° relative to upper side, as shown.

Use the source image for exact clamp orientation before installation.

---

### Printed page 11-480

<a id="p776"></a>
Source: [PDF p.776, printed p.11-480](../page-images/p0776.png).

# Fuel Supply System
## Fuel Line/Quick-Connect Fitting Precautions

The fuel tube/quick-connect fittings (A), (B), (C), (D), (E) connect the fuel rail (F) to fuel feed hose (G), the fuel feed hose to the fuel line (H), the fuel line (I) to the fuel feed hose (J), the fuel feed hose (K) to the fuel tank unit (L), and fuel vapor line (M) to the EVAP canister (N).

When removing or installing the fuel feed hose, the fuel tank unit or the fuel tank, it is necessary to disconnect or connect the quick-connect fittings.

Pay attention to the following:
* The fuel feed hose, fuel line and quick-connect fittings are not heat-resistant; be careful not to damage them during welding or other heat-generating procedures.
* The fuel feed hose, fuel line and quick-connect fittings are not acid-proof; do not touch them with a shop towel which was used for wiping battery electrolyte. Replace them if they came into contact with electrolyte or something similar.
* When connecting or disconnecting the fuel feed hose, fuel line and quick-connect fittings, be careful not to bend or twist them excessively. Replace them if damaged.

A disconnected quick-connect fitting can be reconnected, but the retainer on the mating line cannot be reused once it has been removed from the pipe. Replace the retainer when:
* replacing the fuel rail.
* replacing the fuel line.
* replacing the fuel pump.
* replacing the fuel filter.
* replacing the EVAP canister.
* it has been removed from the line.
* it is damaged.

### Retainer location
| Manufacturer | Retainer Color | Line diameter |
| :--- | :--- | :--- |
| A | Tokai Blue green | 0.3 in. (8.0 mm) |
| B | Tokai Blue green | 0.3 in. (8.0 mm) |
| C | Sanoh White | 0.3 in. (8.0 mm) |
| D | Sanoh White | 0.4 in. (9.5 mm) |
| E | Sanoh White | 0.4 in. (9.5 mm) |

**Page Reference:** 11-480

---

### Printed page 11-481

<a id="p777"></a>
Source: [PDF p.777, printed p.11-481](../page-images/p0777.png).

## Fuel line / quick-connect fitting removal

**Note:** Before working on fuel lines and fittings, read the precautions on p. 11-480.

1. Relieve fuel pressure (p. 11-474).
2. Check quick-connect fittings (A) for dirt; clean if needed.

The source image marks fitting locations in the engine compartment, above the fuel tank, and at the rear line. Procedure continues on the next page.

---

### Printed page 11-482

<a id="p778"></a>
Source: [PDF p.778, printed p.11-482](../page-images/p0778.png).

# Fuel Supply System
## Fuel Line/Quick-Connect Fitting Removal (cont'd)

Hold the connector (**A**) with one hand and squeeze the retainer tabs (**B**) with the other hand to release them from the locking pawls (**C**). Pull the connector off.

> **NOTE:**
> *   Be careful not to damage the line (**D**) or other parts. Do not use tools.
> *   If the connector does not move, keep the retainer tabs pressed down, and alternately pull and push the connector until it comes off easily.
> *   Do not remove the retainer from the line; once removed, the retainer must be replaced with a new one.

Check the contact area (**A**) of the line (**B**) for dirt and damage.
*   If it is dirty, clean it.
*   If it is rusty or damaged, replace the fuel pump, fuel filter, or fuel feed line.

To prevent damage and keep foreign matter out, cover the disconnected connector and line end with plastic bags (**A**).

> **NOTE:** The retainer cannot be reused once it has been removed from the line.

Replace the retainer when:
*   replacing the fuel rail.
*   replacing the fuel feed line.
*   replacing the fuel pump.
*   replacing the fuel filter.
*   replacing the EVAP canister
*   it has been removed from the line.
*   it is damaged.

**11-482**

---

### Printed page 11-483

<a id="p779"></a>
Source: [PDF p.779, printed p.11-483](../page-images/p0779.png).

# Fuel Line/Quick-Connect Fitting Installation

**NOTE:** Before you work on the fuel lines and fittings, read the "Fuel Line/Quick-Connect Fitting Precautions" (see page 11-480).

1. Check the contact area (**A**) of the line (**B**) for dirt and damage, and clean if necessary.
   Insert a new retainer (**A**) into the connector (**B**) if the retainer is damaged, or after:
   * replacing the fuel rail.
   * replacing the fuel feed line.
   * replacing the fuel pump.
   * replacing the fuel filter.
   * replacing the EVAP canister
   * removing the retainer from the line.

3. Before connecting a new fuel tube/quick-connect fitting assembly (**A**), remove the old retainer from the mating line.

*(cont'd)*

**11-483**

---

### Printed page 11-484

<a id="p780"></a>
Source: [PDF p.780, printed p.11-484](../page-images/p0780.png).

# Fuel Supply System
## Fuel Line/Quick-Connect Fitting Installation (cont'd)

4. Align the quick-connect fittings with the line (A), and align the retainer locking tabs (B) with the connector grooves (C). Then press the quick-connect fittings onto the line until both retainer tabs lock with a clicking sound.

**NOTE:** If it is hard to connect, put a small amount of new engine oil on the line end.

### Connection with new retainer
### Connection to new fuel feed line
### Reconnection to existing retainer

11-484

---

### Printed page 11-485

<a id="p781"></a>
Source: [PDF p.781, printed p.11-485](../page-images/p0781.png).

## Fuel line / quick-connect fitting installation (continued)

5. Reconnect connector (A) with the old retainer. Confirm tabs (B) lock; inspect and pull connector to verify. With a new fuel line, remove ring pull (C) upward only after the connection is secure; it can break if pulled from an unsecured connection.
6. Reconnect battery negative cable. Turn ignition ON (II) without starting; pump runs about 2 seconds. Repeat two or three times, then check for fuel leaks.

## Fuel pulsation damper replacement

1. Remove fuel rail (p. 11-382).
2. Remove fuel pulsation damper (A) from rail (B). **Tightening torque: 22 N·m (2.2 kgf·m, 16 lbf·ft).**
3. Install parts in reverse order with new washer (C).

The source image shows both retainer types and the damper/washer placement.

---

### Printed page 11-486

<a id="p782"></a>
Source: [PDF p.782, printed p.11-486](../page-images/p0782.png).

# Fuel Supply System

## Fuel Pressure Regulator
### Replacement

1. Remove the fuel tank unit (see page 11-487).
2. Remove the clips (A).
3. Remove the holder (B).
4. Remove the fuel pressure regulator (C).
5. Install the parts in the reverse order of removal with a new O-ring (D) and new clips.

> **NOTE:** Coat the O-ring with clean engine oil.

---

## Fuel Filter Replacement

The fuel filter should be replaced whenever the fuel pressure drops below the specified value (see page 11-477), after making sure that the fuel pump and the fuel pressure regulator are OK.

1. Remove the fuel tank unit (see page 11-487).
2. Remove the fuel filter (A).
3. Check these items before installing the fuel tank unit:
   - When connecting the wire harness, make sure the connection is secure and the connectors (B) are firmly locked into place.
   - When installing the fuel gauge sending unit (C), make sure the connection is secure and the connector is firmly locked into place. Be careful not to bend or twist it excessively.
4. Install the parts in the reverse order of removal with a new O-rings (D), new bracket (E), new spacer (F), new grommet (G), and new clips (H). Then installing the fuel tank unit (see page 11-487).
5. Install the fuel tank unit (see page 11-487).

**Page Reference:** 11-486

---

### Printed page 11-487

<a id="p783"></a>
Source: [PDF p.783, printed p.11-487](../page-images/p0783.png).

# Fuel Tank Unit Removal and Installation

## Removal
1. Relieve the fuel pressure (see page 11-474).
2. Remove the fuel fill cap.
3. Remove the rear tray (see page 20-73).
4. Remove the left trunk side trim panel (see page 20-77).
5. Remove the access panel (A) from the floor.
6. Disconnect the tank fuel unit 5P connector (B).
7. Disconnect the quick-connect fitting (C) from the fuel tank unit.
8. Remove the fuel tank unit (A).

## Installation
1. Attach a new base gasket (A) and new plate (B) to the fuel tank unit, then install the fuel tank unit into the fuel tank.

**NOTE:**
- Be careful not to damage the new base gasket.
- Be careful not to bend the fuel gauge sending unit.
- Do not coat the base gasket with oil.

9.8 N-m (1.0 kgf m, 7.2 Ibfft)
UPPER SIDE
(cont'd)
11-487

---

### Printed page 11-488

<a id="p784"></a>
Source: [PDF p.784, printed p.11-488](../page-images/p0784.png).

# Fuel Supply System
## Fuel Tank Unit Removal and Installation (cont'd)
### Fuel Pump/Fuel Gauge Sending Unit Replacement

**2.** Connect the quick-connect fitting (A) from the fuel tank unit.
*   A - \ - ^ / • / /

**3.** Connect the fuel tank unit 5P connector (B).

**4.** Reconnect the negative cable to the battery, and turn the ignition switch ON (II) (but do not operate the starter motor). The fuel pump will run for about 2 seconds, and fuel pressure will rise. Repeat this two or three times, then check that there is no leakage in the fuel supply system.

**5.** Install the access panel (C).

**6.** Install the left trunk side trim panel (see page 20-77).

**7.** Remove the rear tray (see page 20-73).

**8.** Install the fuel fill cap.

---

**1.** Remove the fuel tank unit (see page 11-487).

**2.** Remove the fuel filter (A), the fuel gauge sending unit (B), and the wire harness (C).

Install the parts in the reverse order of removal with a new O-ring (D), new bracket (E), new spacer (F), new grommet (G), and new clips (H), then check these items:

*   Make sure the connection is secure and the suction filter (I) is firmly connected to the fuel pump (J).
*   When connecting the wire harness, make sure the connection is secure and the connectors (K) are firmly locked into place.
*   When installing the fuel gauge sending unit, make sure the connection is secure and the connector is firmly locked into place. Be careful not to bend or twist it excessively.

**11-488**

---

### Printed page 11-489

<a id="p785"></a>
Source: [PDF p.785, printed p.11-489](../page-images/p0785.png).

# Fuel Tank Replacement
## Removal

1. Remove the fuel fill cap.
2. Relieve the fuel pressure (see page 11-474).
3. Remove the rear tray (see page 20-73).
4. Remove the left trunk side trim panel (see page 20-77).
5. Drain the fuel tank (see page 11-477).
6. Remove the brake fluid from the master cylinder reservoir with a syringe.

> **NOTE:** Do not spill brake fluid on the vehicle; it may damage the paint; if brake fluid does contact the paint, wash it off immediately with water.

7. Remove the access panel (A) from the floor, and disconnect the fuel tank unit 5P connector (B).
   - Connector: B
8. Disconnect both ABS rear wheel speed sensors 2P connectors (A), and push the connectors out.
10. Loosen the rear wheel nuts slightly, then raise the vehicle and make sure it is securely supported.
11. Remove the rear wheels.

*(cont'd)*

**Page Reference:** 11-489

---

### Printed page 11-490

<a id="p786"></a>
Source: [PDF p.786, printed p.11-490](../page-images/p0786.png).

## Fuel tank replacement (continued)

12. Remove bolts from both ABS rear wheel speed sensor harness brackets (A). Diagram callout: **6 × 1.0 mm, 9.8 N·m (1.0 kgf·m, 7.2 lbf·ft)**.
13. Remove both caliper shields (A). Diagram callout: **6 × 1.0 mm, 9.8 N·m (1.0 kgf·m, 7.2 lbf·ft)**.
14. Disconnect both parking brake cables (A) and move them aside.
15. Disconnect brake hoses from both rear brake lines with a **10 mm flare-nut wrench**.

Illustrations show the left side; repeat operations on both sides as stated.

---

### Printed page 11-491

<a id="p787"></a>
Source: [PDF p.787, printed p.11-491](../page-images/p0787.png).

## Fuel tank replacement (continued)

16. Remove flange bolt (A) from both rear dampers (B). Diagram callout: **12 × 1.25 mm, 64 N·m (6.5 kgf·m, 47 lbf·ft)**.
17. Remove canister cover (A) and rear suspension stiffener (B). Diagram callouts: **10 × 1.25 mm, 45 N·m (4.6 kgf·m, 33 lbf·ft)** and **6 × 1.0 mm, 9.8 N·m (1.0 kgf·m, 7.2 lbf·ft)**.
18. Remove propeller shaft (p. 16-18).
19. Remove muffler (A). Diagram callout: **10 × 1.25 mm, 33 N·m (3.4 kgf·m, 25 lbf·ft)**; replace indicated gasket.
20. Disconnect FTP sensor 3P connector (A), EVAP canister vent shut valve 2P connector (B), and vapor line (C).
21. Remove EVAP canister (D). Diagram callout: **6 × 1.0 mm, 9.8 N·m (1.0 kgf·m, 7.2 lbf·ft)**.

The source image maps these callouts to fasteners.

---

### Printed page 11-492

<a id="p788"></a>
Source: [PDF p.788, printed p.11-492](../page-images/p0788.png).

## Fuel Supply System

### Fuel Tank Replacement (cont'd)

**22.** Disconnect the quick-connect fitting (A) (see page 11-481).

**23.** Place a jack or other support under the rear suspension subframe (A). Remove the mounting bolts (B) and the rear suspension subframe (A).

*Diagram Labels:* A, B
*Torque Specifications:*
- 14 x 1.5 mm: 103 N·m (10.5 kgf-m, 76 lbf-ft)
- 12 x 1.5 mm: 59 N·m (6.0 kgf-m, 43 lbf-ft)

**24.** Place the jack or support under the fuel tank (A), then remove the mounting bolts (B) and the fuel tank.

*Diagram Labels:* A, B
*Torque Specifications:*
- 8 x 1.25 mm: 45 N·m (4.6 kgf-m, 33 lbf-ft)

Source printed page: 11-492

---

### Printed page 11-493

<a id="p789"></a>
Source: [PDF p.789, printed p.11-493](../page-images/p0789.png).

# S2000 Fuel and Emissions Part F
## Page 789

### Installation

1. Install the parts in the reverse order of removal.

2. After installing the fuel tank, bleed the brake system (see page 19-9), and adjust the wheel alignment (see page 18-7).

3. Turn the ignition switch ON (II), but do not operate the starter. After the fuel pump runs 2 seconds, the fuel pressure in the fuel line rises. Repeat this 2 or 3 times, then check for fuel leakage.

---

### Printed page 11-494

<a id="p790"></a>
Source: [PDF p.790, printed p.11-494](../page-images/p0790.png).

# Fuel Supply System
## Fuel Gauge Sending Unit Test

**NOTE:** For the fuel gauge system circuit diagram, refer to the Gauges Circuit Diagram (see page 22-63).

1. Check the No. 5 INSTRUMENT LIGHT BACK UP LIGHT (7.5 A) fuse in the under-dash fuse/relay box before testing.
2. Do the DTC troubleshooting (see page 22-6).
   - If no problem is found, go to step 3.
   - If DTC B1175 or B1176 is indicated, go to the indicated DTCs troubleshooting.
3. Turn the ignition switch OFF.
4. Remove the rear tray (see page 20-73).
5. Remove the access panel (A) from the floor.
6. Disconnect the fuel tank unit 5P connector (B).
7. Measure voltage between fuel tank unit 5P connector terminals No. 1 and No. 2 with the ignition switch ON (II). There should be battery voltage.
   - If the voltage is OK, go to step 8.
   - If the voltage is not as specified, check for:
     - a short in the YEL/BLK wire to ground.
     - an open in the YEL/BLK or BLK wire.

**FUEL TANK UNIT 5P CONNECTOR (YEL/BLK)**
Wire side of female terminals

8. Turn the ignition switch OFF.
9. Remove the fuel tank unit from the fuel tank (see page 11-487).

*Page reference: 11-494*

---

### Printed page 11-495

<a id="p791"></a>
Source: [PDF p.791, printed p.11-495](../page-images/p0791.png).

## Fuel gauge sending unit test (continued)

10. Measure resistance across fuel tank unit 5P terminals **1 and 2** at these float positions. Replace sending unit (p. 11-488) if readings differ.

| Float | Distance | Resistance |
|---|---|---|
| F (full) | 3.2 in (81.2 mm) | 11–13 Ω |
| 1/2 | 6.0 in (152 mm) | 52–58 Ω |
| LOW | 8.4 in (214.3 mm) | 114.4–120.4 Ω |
| E (empty) | 8.7 in (221.9 mm) | 130–132 Ω |

11. Reconnect fuel tank unit 5P connector.
12. Remove No. 2 FUEL PUMP (15 A) fuse from under-hood fuse/relay box for at least 10 seconds, then reinstall.
13. Turn ignition ON (II).
14. At float F, verify gauge points to F. If not, replace gauge assembly. Otherwise test complete.

**Notes:** Gauge pointer drops to bottom with ignition OFF, regardless of fuel level. After troubleshooting, remove No. 2 FUEL PUMP fuse for at least 10 seconds or correct gauge indication may take up to 20 minutes. Source image shows float positions and terminal orientation.

---

### Printed page 11-496

<a id="p792"></a>
Source: [PDF p.792, printed p.11-496](../page-images/p0792.png).

# Fuel Supply System
## Low Fuel Indicator Test

1. Do the fuel gauge sending unit test (see page 11-494).
   - If the system is OK, go to step 2.
   - If the system has any malfunction, repair it.

2. Turn the ignition switch OFF. Remove the No. 25 BACK UP (7.5 A) fuse from the under-dash fuse/relay box for at least 30 seconds, then reinstall it.

3. Turn the ignition switch ON (II) with the float at the E (EMPTY) position.
   - If the low fuel indicator is on, go to step 4.
   - If the low fuel indicator is not on, refer to the low fuel indicator Circuit Diagram (see page 22-73), and check the circuit.

4. Turn the ignition switch OFF. Remove the No. 25 BACK UP (7.5 A) fuse from the under-dash fuse/relay box for at least 30 seconds, then reinstall it.

5. Lift the float above the LOW position.
   - If the low fuel indicator goes off, the system is OK.
   - If the low fuel indicator is still on, refer to the low fuel indicator Circuit Diagram (see page 22-73), and check the circuit.

**Page Reference:** 11-496

---

### Printed page 11-497

<a id="p793"></a>
Source: [PDF p.793, printed p.11-497](../page-images/p0793.png).

# Intake Air System
## Component Location Index

### Engine Control Module (ECM)
* Updating: page 11-216
* Substitution: page 11-217
* Replacement: page 11-389

**Page Reference:** 11-497

---

### Printed page 11-498

<a id="p794"></a>
Source: [PDF p.794, printed p.11-498](../page-images/p0794.png).

# Intake Air System
## Throttle Body Test
### Carbon Accumulation Check
1. Connect the HDS to the data link connector (DLC) (A) located behind the driver's side of the front console.
2. Turn the ignition switch ON (II).
3. Make sure the HDS communicates with the ECM. If it doesn't, go to the DLC circuit troubleshooting (see page 11-367).
4. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
5. Check the REL TP S E N S O R in the DATA LIST the HDS. The reading should be below 2.46 deg. If it is not, clean the throttle body (see page 11-499).

## Throttle Position Learning Check
1. Connect the HDS to the data link connector (DLC) (A) located behind the driver's side of the front console.
2. Turn the ignition switch ON (II).
3. Make sure the HDS communicates with the ECM. If it doesn't, go to the DLC circuit troubleshooting (see page 11-367).
4. Select the INSPECTION MENU with the HDS.
5. Do the TP LEARNING CHECK in the ETCS TEST. If needed, clean the throttle body (see page 11-499).

**Page Reference:** 11-498

---

### Printed page 11-499

<a id="p795"></a>
Source: [PDF p.795, printed p.11-499](../page-images/p0795.png).

# Throttle Body Cleaning

**^CAUTION**
Do not insert your fingers into the installed throttle body when you turn the ignition switch ON (II) or while the ignition switch is ON (II). If you do, you will seriously injure your fingers if the throttle valve is activated.

1. Check for damage to the air cleaner. If the air cleaner is damaged, replace it (see page 11-505).
2. Remove the throttle body (see page 11-500).
3. Wipe off the carbon from the throttle valve and inside the throttle body with a paper towel soaked in throttle plate and induction cleaner.

**NOTE:**
*   Remove the throttle body to clean it.
*   To avoid removing the molybdenum coating, do not clean the bearing area of the throttle shaft (A).
*   Do not spray the cleaner directly on the throttle body.
*   Use Honda genuine throttle plate and induction cleaner.
4. Install the throttle body (see page 11-500).
5. Reset the ECM with the HDS.
6. Turn the ignition switch ON (II), and wait 2 seconds.
7. Do the ECM idle learn procedure (see page 11-462).

**Page Reference:** 11-499

---

### Printed page 11-500

<a id="p796"></a>
Source: [PDF p.796, printed p.11-500](../page-images/p0796.png).

# Intake Air System
## Throttle Body Removal/Installation

**Warning:** Do not insert your fingers into the installed throttle body when you turn the ignition switch ON (II) or while the ignition switch is ON (II). If you do, you will seriously injure your fingers if the throttle valve is activated.

**NOTE:** If you are replacing the throttle body, begin at step 1. If you are removing the throttle body, begin at step 4.

1. Connect the HDS while the engine is stopped.
2. Select the INSPECTION MENU with the HDS.
3. Do the TP POSITION CHECK in the E T C S TEST.
4. Turn the ignition switch OFF.
5. Remove the intake air duct (A).
6. Disconnect the throttle body connector (B).
7. Disconnect the water bypass hoses (C), and plug them.
8. Remove the throttle body (D).
9. Install the parts in the reverse order of removal with a new gasket (E), then do this:
   - Do the E C M idle learn procedure (see page 11-462).
   - Refill the radiator with engine coolant (see page 10-9).

**Page Reference:** 11-500

---

### Printed page 11-501

<a id="p797"></a>
Source: [PDF p.797, printed p.11-501](../page-images/p0797.png).

## Throttle body disassembly/reassembly

Exploded diagram shows the throttle body and a replaceable O-ring. The illustrated fastener torque is **3.5 N·m (0.35 kgf·m, 2.5 lbf·ft)**. Follow the source image for the exact parts and fastener placement; this page contains no written procedure.

---

### Printed page 11-502

<a id="p798"></a>
Source: [PDF p.798, printed p.11-502](../page-images/p0798.png).

# Intake Air System
## Accelerator Pedal Replacement

1. Remove the throttle cable (A) from the accelerator pedal (B).
2. Remove the nuts (C) and the accelerator pedal.
3. Install the parts in the reverse order of removal.

**Page Reference:** 11-502

---

### Printed page 11-503

<a id="p799"></a>
Source: [PDF p.799, printed p.11-503](../page-images/p0799.png).

# Throttle Cable Removal/Installation

1. Remove the throttle cable cover (see page 11-504).
2. Fully open the throttle valve, then remove the throttle cable (A) from the throttle link (B). **GREASE** (P/N 08798-9002)
3. Remove the cable housing (C) from the cable bracket (D).
4. Remove the throttle cable (A) from the accelerator pedal (B). **SILICONE GREASE** (P/N 08798-9002)
5. Install the parts in the reverse order of removal.
6. Hold the cable, removing all slack from it.
7. Set the cable on the bracket (A). Turn the adjusting nut (B) so that its free play is **0 mm**. There should be no clearance.
8. Position the adjusting nut on the other side of the bracket, then tighten the locknut (C).
9. Check the throttle cable free play (see page 11-504).
10. With the cable properly adjusted, check the throttle link to be sure it opens fully when you push the accelerator pedal to the floor. Also check the throttle link to be sure it returns whenever you release the accelerator pedal.

**Page Reference:** 11-503

---

### Printed page 11-504

<a id="p800"></a>
Source: [PDF p.800, printed p.11-504](../page-images/p0800.png).

# Intake Air System
## Throttle Cable Adjustment

1. Remove the throttle cable cover (**A**).
2. Check cable free play at the throttle linkage. Cable free play (**A**) should be **0.59—0.71 in.** (**15—18 mm**).
   > *Note: Diagram labels A and B referenced in text but diagram content not provided.*
3. If the free play is not within spec (**0.59—0.71 in., 15—18 mm**), loosen the locknut (**B**), turn the adjusting nut (**C**) until the deflection is as specified, then retighten the locknut.
4. With the cable properly adjusted, check the throttle link to be sure it opens fully when you push the accelerator pedal to the floor. Also check the throttle link to be sure it returns whenever you release the accelerator pedal.

## Air Cleaner Removal/Installation

1. Remove the air cleaner element (see page **11-505**).
2. Remove the bolts (**A**).
3. Remove the air cleaner (**B**).
4. Install the parts in the reverse order of removal.

> *Page Reference: 11-504*

---

### Printed page 11-505

<a id="p801"></a>
Source: [PDF p.801, printed p.11-505](../page-images/p0801.png).

# Air Cleaner Element Inspection/Replacement

1. Remove the air cleaner housing cover (**A**).
2. Remove the air cleaner element (**B**) from the air cleaner housing (**C**).
3. Check the air cleaner element for damage or clogging. If it is damaged or clogged, replace it.
   > **NOTE:** Do not use compressed air to clean the air cleaner element.
4. Clean and remove any debris from inside the air cleaner housing.
5. Install the parts in the reverse order of removal.
6. Reset the maintenance minder, if needed (see page 3-27).
7. Reset the ECM with the HDS.
8. Do the E C M idle learn procedure (see page 11-462).

**A**

**11-505**

---

### Printed page 11-506

<a id="p802"></a>
Source: [PDF p.802, printed p.11-506](../page-images/p0802.png).

# Catalytic Converter System
## Component Location Index

### T H R E E W A Y C A T A L Y T I CC O N V E R T E R (TWC)
*Replacement, page 9-6*

### ENGINE C O N T R O L M O D U L E (ECM)
*Updating, page 11-216*
*Substitution, page 11-217*
*Replacement, page 11-389*

**Page Reference:** 11-506

---

### Printed page 11-507

<a id="p803"></a>
Source: [PDF p.803, printed p.11-507](../page-images/p0803.png).

# DTC Troubleshooting

## DTC P0420: Catalyst System Efficiency Below Threshold

**NOTE:**
*   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   If some of the DTCs listed below are stored at the same time as DTC P0420, troubleshoot them first, then recheck for DTC P0420.
    *   P0137, P0138: Secondary H2S (Sensor 2)
    *   P0141: Secondary H2S (Sensor 2) heater
*   Poor quality fuel may cause this DTC.

1.  Turn the ignition switch ON (II).
2.  Clear the DTC with the HDS.
3.  Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
4.  Test-drive under these conditions:
    *   Engine coolant temperature (ECT SENSOR 1) above 158 °F (70 °C)
    *   Transmission in 5th gear
    *   Vehicle speed between 45—75 mph (72 — 120 km/h) for 5 minutes or more
    *   Vehicle speed 25 mph (40 km/h) or more for 1 minute with cruise control set
5.  Monitor the OBD STATUS for DTC P0420 in the DTCs MENU with the HDS.
    Does the screen indicate EXECUTING?
    *   **YES** — Go to step 6.
    *   **NO** — If the screen indicates OUT OF CONDITION, go to step 4 and recheck. If the screen indicates PASSED, intermittent failure, the system is OK at this time. If the screen indicates FAILED, go to step 8.

6.  Continue test driving until a result comes on.
7.  Monitor the OBD STATUS for DTC P0420 in the DTCs MENU with the HDS.
    Does the screen indicate FAILED?
    *   **YES** — Go to step 8.
    *   **NO** — If the screen indicates PASSED, intermittent failure, the system is OK at this time. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates OUT OF CONDITION, go to step 4 and recheck.

8.  Turn the ignition switch OFF.
9.  Replace the three way catalytic converter (TWC) (see page 9-6).
10. Turn the ignition switch ON (II).
11. Reset the ECM with the HDS.
12. Do the ECM idle learn procedure (see page 11-462).
13. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
14. Test-drive for about 10 minutes, varying the vehicle speed.
15. Check the CATA MONITOR CONDITION in the DATA LIST with the HDS.
    Is the temperature OK?
    *   **YES** — Go to step 16.
    *   **NO** — Go to step 13 and recheck.

16. Test-drive under these conditions:
    *   Engine coolant temperature (ECT SENSOR 1) above 158 °F (70 °C)
        *(Note: OCR detected '7 0 * 0' instead of '70 °C')*
    *   Transmission in 5th gear
    *   Vehicle speed between 45—75 mph (72 — 120 km/h) for 5 minutes or more
    *   Vehicle speed 25 mph (40 km/h) or more for 1 minute with cruise control set

*(cont'd)*
**Page Reference:** 11-507

---

### Printed page 11-508

<a id="p804"></a>
Source: [PDF p.804, printed p.11-508](../page-images/p0804.png).

# Catalytic Converter System
## DTC Troubleshooting (cont'd)

**17.** Monitor the **OBD S T A T U S** for **DTC P0420** in the **DTCs MENU** with the **HDS**.

Does the screen indicate **EXECUTING**?
*   **Y E S** — G o to step 18.
*   **N O** — G o to step 16 and recheck.

**18.** Continue test driving until a result comes on.

**19.** Check for Temporary DTCs or DTCs with the HDS.

Is **DTC P0420** indicated?
*   **Y E S** — C h e c k the fuel quality, then go to step 1.
*   **N O** — G o to step 20.

**20.** Monitor the **OBD S T A T U S** for **DTC P0420** in the **DTCs MENU** with the **HDS**.

Does the screen indicate **PASSED**?
*   **YES**—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 19, go to the indicated **D T C s** troubleshooting.
*   **NO**—If the screen indicates **FAILED**, check for poor connections or loose terminals at the secondary **H 0 2 S** (sensor 2) and the **E C M**. If the screen indicates **EXECUTING**, keep driving until a result comes on. If the screen indicates **O U T OF CONDITION**, go to step 13.

**Page Reference:** 11-508

---

### Printed page 11-509

<a id="p805"></a>
Source: [PDF p.805, printed p.11-509](../page-images/p0805.png).

# PCV System

## Component Location Index

### ENGINE CONTROL MODULE (ECM)

*   **Updating**: page 11-216
*   **Substitution**: page 11-217
*   **Replacement**: page 11-389

**Page Reference**: 11-509

---

### Printed page 11-510

<a id="p806"></a>
Source: [PDF p.806, printed p.11-510](../page-images/p0806.png).

# PCV System
## DTC Troubleshooting
### DTC P2279: Intake Air System Leak

**NOTE:**
*   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   If DTC P0443 is stored at the same time as DTC P2279, troubleshoot DTC P0443 first, then recheck for DTC P2279.

**1. Check for vacuum leaks at these parts:**
*   PCV valve
*   PCV hose
*   Purge (PCS) line
*   Throttle body
*   Brake booster
*   Brake booster hose

Are the parts OK ?
*   **Y E S** — G o to step 2.
*   **NO** — Repair or replace the leaking part(s), then go to step 4.

**2. Start the engine.** Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle 1 minute.

**3. Monitor the OBD S T A T U S for DTC P2279 in the DTCs MENU with the HDS.**

Does the screen indicate FAILED?
*   **YES** — Check the camshaft timing (see page 6-15), then go to step 4.
*   **NO** — If the screen indicates PASSED, intermittent failure, the system is OK at this time. If the screen indicates NOT COMPLETED, go to step 2 and recheck.

**4. Reset the E C M with the HDS.**

**5. Do the E C M idle learn procedure (see page 11-462).**

**6. Start the engine.** Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle 1 minute.

**7. Check for Temporary DTCs or DTCs with the HDS.**

Is DTC P2279 indicated?
*   **Y E S** — C h e c k for vacuum leaks at the PCV valve, the PCV hose, the purge (PCS) line, the throttle body, the brake booster, or the brake booster hose, then go to step 4.
*   **N O** — G o to step 8.

**8. Monitor the OBD S T A T U S for DTC P2279 in the DTCs MENU with the HDS.**

Does the screen indicate PASSED?
*   **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 7, go to the indicated D T C s troubleshooting.
*   **NO** — If the screen indicates FAILED, goto step 1 and recheck. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

**Page Reference:** 11-510

---

### Printed page 11-511

<a id="p807"></a>
Source: [PDF p.807, printed p.11-511](../page-images/p0807.png).

## PCV valve inspection

1. Check PCV valve (A), hoses (B), and connections for leaks or restrictions.
2. At idle, lightly pinch the hose between PCV valve and intake manifold with fingers or pliers; listen for a click from the valve. If none, check hose for cracks or damage. If hose is OK, replace PCV valve and recheck.

## PCV valve replacement

1. Disconnect PCV hose.
2. Remove PCV valve (A). **Tightening torque: 44 N·m (4.5 kgf·m, 33 lbf·ft).**
3. Install in reverse order with new washer (B).

Source image shows valve and washer locations.

---

### Printed page 11-512

<a id="p808"></a>
Source: [PDF p.808, printed p.11-512](../page-images/p0808.png).

# EVAP System Component Location Index

## Canister Purge Valve
*Replacement, page 11-542*

## Canister Vent Shut Valve
*Replacement, page 11-543*

## Fuel Tank Vapor Control Float
*Replacement, page 11-545*

## EVAP Canister
*Replacement, page 11-544*

## Fuel Tank Pressure (FTP) Sensor
*Replacement, page 11-542*

**Index Reference:** 11-512

---

### Printed page 11-513

<a id="p809"></a>
Source: [PDF p.809, printed p.11-513](../page-images/p0809.png).

# ENGINE CONTROL MODULE (ECM)

**Updating**, page 11-216

**Substitution**, page 11-217

**Replacement**, page 11-389

---

*Page Reference: 11-513*

---

### Printed page 11-514

<a id="p810"></a>
Source: [PDF p.810, printed p.11-514](../page-images/p0810.png).

# EVAP System
## DTC Troubleshooting
### DTC P0443: EVAP Canister Purge Valve Circuit Malfunction

**Special Tools Required**
Vacuum pump/gauge, 0—30 in.Hg, Snap-on YA4000A or equivalent, commercially available.

> **NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
4. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P0443 indicated?**
- **Y E S** — G o to step 5.
- **N O** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the EVAP canister purge valve and the ECM.

5. Turn the ignition switch OFF, and allow the engine to cool below 149 °F (65 °C).
6. Disconnect the vacuum hose (A) from the EVAP canister purge valve (B) in the engine compartment, and connect a vacuum pump/gauge, 0—30 in.Hg, to the EVAP canister purge valve.
7. Start the engine, and let it idle.

**Is there vacuum?**
- **Y E S** — G o to step 8.
- **N O** — G o to step 14.

8. Turn the ignition switch OFF.
9. Disconnect the EVAP canister purge valve 2P connector.
10. Check for continuity between EVAP canister purge valve 2P connector terminal No. 2 and body ground.

**E V A P C A N I S T E R P U R G E V A L V E 2P C O N N E C T O R**
- **P C S (RED/YEL)**: Wire side of female terminals

**Is there continuity?**
- **Y E S** — G o t o s t e p 11.
- **N O** — G o to step 24.

11. J u m p the S C S line with the HDS.
12. Disconnect E C M connector B (24P).

*Page reference: 11-514*

---

### Printed page 11-515

<a id="p811"></a>
Source: [PDF p.811, printed p.11-515](../page-images/p0811.png).

## DTC P0443 troubleshooting (continued)

13. Check continuity between EVAP purge valve 2P terminal **2 (PCS, RED/YEL)** and body ground. **Continuity:** Repair short between valve and ECM B21, then go to step 25. **No continuity:** Go to step 31.
14. Turn ignition OFF.
15. Disconnect purge valve 2P connector.
16. Turn ignition ON (II).
17. Measure voltage between purge valve 2P terminal **1 (IG1, BLK/YEL)** and body ground. **Battery voltage:** Go to step 18. **No voltage:** Repair open between valve and No. 6 ACG (15 A) fuse in under-dash fuse/relay box, then go to step 25.
18. Turn ignition OFF.
19. Jump SCS line with HDS.
20. Disconnect ECM connector **B (24P)**.
21. Ground purge valve terminal 2 with jumper wire. Procedure continues on next page.

The source image confirms connector B and terminal positions.

---

### Printed page 11-516

<a id="p812"></a>
Source: [PDF p.812, printed p.11-516](../page-images/p0812.png).

# EVAP System
## DTC Troubleshooting (cont'd)

**22.** Check for continuity between E C M connector terminal B21 and body ground.

```
E C M C O N N E C T O R B(24P)
/ \ 2 I 3 | 4 | 5
8
/ 10 11
/ 13
/ / / 17 18 19 20 21
/ / / I P C S ( Y E L / B L U )
Wire side of female terminals
```

Is there continuity?

* **Y E S** — G o to step 23.
* **NO** — Repair open in the wire between the EVAP canister purge valve and the E C M (B21), then go to step 25.

---

**23.** At the purge valve side, measure resistance between EVAP canister purge valve 2P connector terminals No. 1 and No. 2.

```
E V A P C A N I S T E R P U R G E V A L V E 2P C O N N E C T O R
1 2
Terminal side of male terminals
```

Is there about **33 0** at room temperature?

* **Y E S** — G o to step 31.
* **N O** — G o to step 24.

---

**24.** Replace the EVAP canister purge valve (see page 11-542).

**25.** Reconnect all connectors.

**26.** Turn the ignition switch ON (**II**).

**27.** Reset the E C M with the HDS.

**28.** Do the E C M idle learn procedure (see page 11-462).

**29.** Check for Temporary DTCs or DTCs with the HDS.

Is **DTC P0443** indicated?

* **Y E S** — C h e c k for poor connections or loose terminals at the EVAP canister purge valve and the E C M , then go to step 1.
* **N O** — G o to step 30.

---

**30.** Monitor the OBD **S T A T U S** for DTC P0443 in the DTCs MENU with the HDS.

Does the screen indicate **PASSED**?

* **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 29, go to the indicated **D T C s** troubleshooting.
* **NO** — If the screen indicates **FAILED**, check for poor connections or loose terminals at the EVAP canister purge valve and the E C M , then go to step 1. If the screen indicates **EXECUTING** or **O U T OF CONDITION**, keep idling until a result comes on.

**Page Reference:** 11-516

---

### Printed page 11-517

<a id="p813"></a>
Source: [PDF p.813, printed p.11-517](../page-images/p0813.png).

## DTC P0443 troubleshooting (continued)

31. Reconnect all connectors.
32. Update ECM software if needed (p. 11-216) or substitute known-good ECM (p. 11-217).
33. Start engine and idle.
34. Check DTCs. **P0443 indicated:** Check purge valve and ECM connections. If ECM was updated, substitute known-good ECM and return to step 33; if substituted, return to step 1. **Not indicated:** Go to step 35.
35. Monitor OBD STATUS for P0443. **PASSED:** If ECM was updated, troubleshooting complete; if substituted, replace original ECM (p. 11-389). Follow other DTCs from step 34. **FAILED:** Check purge valve and ECM connections. If ECM was updated, substitute known-good ECM and recheck; if substituted, return to step 1. **EXECUTING/OUT OF CONDITION:** Keep idling until a result appears.

---

### Printed page 11-518

<a id="p814"></a>
Source: [PDF p.814, printed p.11-518](../page-images/p0814.png).

# EVAP System
## DTC Troubleshooting (cont'd)
### DTC P0451: FTP Sensor Circuit Range/Performance Problem

**NOTE:**
*   Before you troubleshoot record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   If DTC P2422 is stored at the same time as DTC P0451, troubleshoot DTC P2422 first, then recheck for DTC P0451.

**Step 1:** Turn the ignition switch ON (II).
**Step 2:** Clear the DTC with the HDS.
**Step 3:** Start the engine, and let it idle.
**Step 4:** Monitor the OBD STATUS for DTC P0451 in the DTCs MENU with the HDS.

*Does the screen indicate FAILED?*

*   **YES — Go to step 5.**
*   **NO — If the screen indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor and the ECM.**
    *   If the screen indicates NOT COMPLETED, keep idling until a result comes on.

**Step 5:** Turn the ignition switch OFF.
**Step 6:** Replace the FTP sensor (see page 11-542).
**Step 7:** Turn the ignition switch ON (II).
**Step 8:** Reset the ECM with the HDS.
**Step 9:** Do the ECM idle learn procedure (see page 11-462).
**Step 10:** Start the engine, and let it idle.

**Step 11:** Check for Temporary DTCs or DTCs with the HDS.
*Is DTC P0451 indicated?*

*   **YES — Check for poor connections or loose terminals at the FTP sensor and the ECM, then go to step 1.**
*   **NO — Go to step 12.**

**Step 12:** Monitor the OBD STATUS for DTC P0451 in the DTCs MENU with the HDS.
*Does the screen indicate PASSED?*

*   **YES — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 11, go to the indicated DTCs troubleshooting.**
*   **NO — If FAILED, check FTP sensor and ECM connections, then go to step 1. If NOT COMPLETED, keep idling until a result appears.**

**Page Reference:** 11-518

---

### Printed page 11-519

<a id="p815"></a>
Source: [PDF p.815, printed p.11-519](../page-images/p0815.png).

# DTC P0452: FTP Sensor Circuit Low Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Turn the ignition switch OFF.
4. Remove the fuel fill cap.
5. Turn the ignition switch ON (II).
6. Check the FTP S E N S O R in the DATA LIST with the HDS.
Is about - 7.3 kPa (-2.16 in.Hg, - 55 mmHg), or 0.3 V or less indicated?

- **Y E S** — G o to step 10.
- **N O** — G o to step 7.

7. Install the fuel fill cap.
8. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.
9. Monitor the OBD S T A T U S for DTC P0452 in the DTCs MENU with the HDS.
Does the screen indicate FAILED?

- **Y E S** — G o to step 10.
- **NO** — If the screen indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor and the E C M . If the screen indicates NOT COMPLETED, go to step 4 and recheck.

10. Turn the ignition switch OFF.
11. Disconnect the FTP sensor 3P connector.
12. Turn the ignition switch ON (II).
13. Check the FTP S E N S O R in the DATA LIST with the HDS.
Is about - 7.3 kPa (-2.16 in.Hg, - 55 mmHg), or 4.90 V indicated?

- **Y E S** — G o to step 14.
- **N O** — G o to step 20.

14. Measure voltage between FTP sensor 3P connector terminal No. 1 and body ground.

> **FTP S E N S O R 3P C O N N E C T O R**
>
> | 1 | 2 | 3 |
> | :---: | :---: | :---: |
> | V C C 3 | ( Y E L / B L U ) | |
>
> Wire side of female terminals

Is there about 5 V?

- **Y E S** — G o to step 16.
- **N O** — G o to step 15.

(cont'd)

Page Reference: 11-519

---

### Printed page 11-520

<a id="p816"></a>
Source: [PDF p.816, printed p.11-520](../page-images/p0816.png).

# EVAP System
## DTC Troubleshooting (cont'd)

**15.** Measure voltage between ECM connector terminal E5 and body ground.

```
ECM CONNECTOR E (31P)
VCC 3 (YEL/BLU) | 1 M » | 4 | B XI 7 | | 8 | «
/ 11 12 13 14 15 16 17 18 19 20 21
22
/ 24 25
/ 27 28 29 30
/
Wire side of female terminals
```

**Is there SV?**
*   **YES**—Repair open in the wire between the ECM (E5) and the FTP sensor, then go to step 22.
*   **NO**—Go to step 28.

**16.** Turn the ignition switch OFF.

**17.** Jump the SCS line with the HDS.

**18.** Disconnect ECM connector E (31P).

**19.** Check for continuity between FTP sensor 3P connector terminal No. 2 and body ground.

```
FTP SENSOR 3P CONNECTOR
FTP (LTGRN)
```

**20.** Turn the ignition switch OFF.

**21.** Replace the FTP sensor (see page 11-542).

**22.** Reconnect all connectors.

**23.** Turn the ignition switch ON (II).

**24.** Reset the ECM with the HDS.

**25.** Do the ECM idle learn procedure (see page 11-462).

**26.** Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P0452 indicated?**
*   **YES**—Check for poor connections or loose terminals at the FTP sensor and the ECM, then go to step 1.
*   **NO**—Go to step 27.

**27.** Monitor the OBD STATUS for DTC P0452 in the DTCs MENU with the HDS.

**Does the screen indicate PASSED?**
*   **YES**—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 26, go to the indicated DTCs troubleshooting.
*   **NO**—If the screen indicates FAILED, check for poor connections or loose terminals at the FTP sensor and the ECM, then go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

**Is there continuity?**
*   **YES**—Repair short in the wire between the ECM (E14) and the FTP sensor, then go to step 22.
*   **NO**—Go to step 29.

**11-520**

---

### Printed page 11-521

<a id="p817"></a>
Source: [PDF p.817, printed p.11-521](../page-images/p0817.png).

Step 28: Turn the ignition switch OFF.
Step 29: Reconnect all connectors.
Step 30: Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
Step 31: Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.
Step 32: Check for Temporary DTCs or DTCs with the HDS. Is DTC P0452 indicated?
Decision Path YES: Check for poor connections or loose terminals at the FTP sensor and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 31. If the ECM was substituted, go to step 1.
Decision Path NO: Go to step 33.
Step 33: Monitor the OBD STATUS for DTC P0452 in the DTCs MENU with the HDS.
Decision Path YES (PASSED): If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 32, go to the indicated DTCs troubleshooting.
Decision Path NO (FAILED): Check for poor connections or loose terminals at the FTP sensor and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 31. If the ECM was substituted, go to step 1.
Decision Path NOT COMPLETED: Keep idling until a result comes on.
Page Reference: 11-521

---

### Printed page 11-522

<a id="p818"></a>
Source: [PDF p.818, printed p.11-522](../page-images/p0818.png).

# EVAP System
## DTC Troubleshooting (cont'd)
### DTC P0453: FTP Sensor Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Turn the ignition switch OFF.
4. Remove the fuel fill cap.
5. Turn the ignition switch ON (**II**).
6. Check the FTP **S E N S O R** in the DATA LIST with the HDS.
   Is about 7.3 kPa (2.16 in.Hg, 55 mmHg), or 4.7 V or more indicated?
   - **Y E S** — G o t o s t e p 10.
   - **NO** — Go to step 7.

7. Install the fuel fill cap.
8. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.
9. Monitor the OBD **S T A T U S** for DTC P0453 in the DTCs MENU with the HDS.
   Does the screen indicate FAILED?
   - **Y E S** — G o t o s t e p 10.
   - **NO** — If the screen indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor and **E C M**. If the screen indicates NOT COMPLETED, go to step 6 and recheck.

10. Turn the ignition switch OFF.
11. Disconnect the FTP sensor 3P connector.

    > **FTP S E N S O R 3P C O N N E C T O R**
    > 1 | 2 | 3
    > ---|---|---
    > FTP (L) | G (R) | N
    > S | G | 3
    > (G R N)
    >
    > **J U M P E R W I R E**
    > Wire side of female terminals

12. Connect FTP sensor 3P connector terminals No. 2 and No. 3 with a jumper wire.

13. Turn the ignition switch ON (**II**).
14. Check the FTP **S E N S O R** in the DATA LIST with the HDS.
    Is about 7.3 kPa (2.16 in.Hg, 55 mmHg), or 4.7 V or more indicated?
    - **Y E S** — G o t o s t e p 15.
    - **N O** — G o t o s t e p 25.

15. Measure voltage between FTP sensor 3P connector terminals No. 1 and No. 3.

    > **FTP S E N S O R 3P C O N N E C T O R**
    > V | C | C | 3
    > (YEL/BLU)
    > ---|---|---|---
    > S | G | 3
    > (G R N)
    >
    > Wire side of female terminals

Is there about 5 V?
- **Y E S** — G o t o s t e p 21.
- **N O** — G o t o s t e p 16.

11-522

---

### Printed page 11-523

<a id="p819"></a>
Source: [PDF p.819, printed p.11-523](../page-images/p0819.png).

## FTP sensor circuit troubleshooting (continued)

16. Turn ignition OFF.
17. Jump SCS line with HDS.
18. Disconnect ECM connector E (31P).
19. Ground FTP sensor 3P terminal **3 (SG3, GRN)** with jumper wire.
20. Check continuity between ECM **E4 (SG3, GRN)** and body ground. **Continuity:** Go to step 34. **No continuity:** Repair open between ECM E4 and FTP sensor, then go to step 27.
21. Turn ignition OFF.
22. Jump ECM terminals **E4 (SG3, GRN)** and **E14 (FTP, LT GRN)**.
23. Turn ignition ON (II).
24. Check FTP SENSOR in HDS DATA LIST. **About 7.3 kPa (2.16 in.Hg, 55 mmHg) or 4.7 V or more:** Go to step 33. **Otherwise:** Repair open between ECM E14 and FTP sensor, then go to step 27.
25. Turn ignition OFF.
26. Replace FTP sensor (p. 11-542).
27. Reconnect all connectors.

The source image confirms the separate step 20 and step 24 decision paths.

---

### Printed page 11-524

<a id="p820"></a>
Source: [PDF p.820, printed p.11-524](../page-images/p0820.png).

# EVAP System
## DTC Troubleshooting (cont'd)

**28.** Turn the ignition switch ON (II).

**29.** Reset the E C M with the HDS.

**30.** Do the E C M idle learn procedure (see page 11-462).

**31.** Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0453 indicated?

*   **YES**—Check for poor connections or loose terminals at the FTP sensor and the E C M, then go to step 1.
*   **NO**—Go to step 32.

**32.** Monitor the OBD S T A T U S for DTC P0453 in the DTCs MENU with the HDS.

Does the screen indicate PASSED?

*   **YES**—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 31, go to the indicated D T C s troubleshooting.
*   **NO**—If the screen indicates FAILED, check for poor connections or loose terminals at the FTP sensor and the E C M, then go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

**33.** Turn the ignition switch OFF.

**34.** Reconnect all connectors.

**35.** Update the E C M if it does not have the latest software (see page 11-216), or substitute a known-good E C M (see page 11-217).

**36.** Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.

**37.** Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0453 indicated?

*   **YES**—Check for poor connections or loose terminals at the FTP sensor and the E C M. If the E C M was updated, substitute a known-good ECM (see page 11-217), then go to step 36. If the E C M was substituted, go to step 1.
*   **NO**—Go to step 38.

**38.** Monitor the OBD S T A T U S for DTC P0453 in the DTCs MENU with the HDS,

Does the screen indicate PASSED?

*   **YES**—If the ECM was updated, troubleshooting is complete. If the E C M w a s substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 37, go to the indicated D T C s troubleshooting.
*   **NO**—If the screen indicates FAILED, check for poor connections or loose terminals at the FTP sensor and the ECM. If the E C M was updated, substitute a known-good E C M (see page 11-217), then go to step 36, If the E C M was substituted, go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

**Page Reference:** 11-524

---

### Printed page 11-525

<a id="p821"></a>
Source: [PDF p.821, printed p.11-525](../page-images/p0821.png).

# DTC P0455: EVAP System Large Leak Detected
# DTC P0456: EVAP System Very Small Leak Detected

## NOTICE
The fuel system is designed to allow specified maximum vacuum and pressure conditions. Do not deviate from the vacuum and pressure tests as indicated in these procedures. Excessive pressure/vacuum would damage the EVAP components or cause eventual fuel tank failure.

### Special Tools Required
Vacuum pump/gauge, 0—30 in.Hg, Snap-on YA4000A or equivalent, commercially available

**NOTE:**
*   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   Fresh fuel has a higher volatility that will create greater pressure/vacuum. The optimum condition for testing is less than a full tank of fresh fuel. If possible, to assist in leak detection, add 1 gallon of fresh fuel to the tank (as long as it will not fill the tank) just before starting these procedures.

1. Check the fuel fill cap (the cap must say "TIGHTEN TO CLICK"). It should turn 1/4 turn after it's tight, then it clicks.
   Is the correct fuel fill cap installed and properly tightened?
   *   **YES** — Go to step 2.
   *   **NO** — Replace or tighten the cap, then go to step 22.

2. Check the fuel fill cap seal (A) and the fuel fill pipe mating surface (B). Verify that the fuel fill cap tether cord (C) is not caught under the cap.
   Is the fuel fill cap seal missing or damaged, is the fuel fill pipe damaged, or is the tether cord caught under the cap?
   *   **YES** — Replace the fuel fill cap or the fuel fill pipe, then go to step 22.
   *   **NO** — Go to step 3.

3. Turn the ignition switch ON (II).
4. Clear the DTC with the HDS.
5. Do the EVAP FUNCTION TEST in the INSPECTION MENU with the HDS.
   Is the result OK?
   *   **YES** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister purge valve, or the EVAP canister vent shut valve and the ECM.
   *   **NO** — Go to step 6.

*(cont'd) 11-525

---

### Printed page 11-526

<a id="p822"></a>
Source: [PDF p.822, printed p.11-526](../page-images/p0822.png).

# EVAP System
## DTC Troubleshooting (cont'd)

6. Turn the ignition switch OFF.
7. Check for a poor connection or damage at the fuel tank vapor recirculation tube and fuel tank vapor control float (see page 11-545).

**Is the tube OK?**
*   **YES — Go to step 8.**
*   **NO —**
    *   Replace the fuel tank vapor control float (see page 11-545), then go to step 22.
    *   If necessary, replace the fuel tank (see page 11-489), then go to step 22.

8. Disconnect the fuel tank vapor recirculation tube (A) from the EVAP canister (B), and plug the EVAP canister port (C).
    *   *(Diagram reference: A, B, C)*

9. Disconnect the vacuum hose (purge line) (A) from the EVAP canister purge valve (B) in the engine compartment, and the vacuum pump/gauge, 0—30 in.Hg, to the hose as shown.
    *   *(Diagram reference: A)*

10. Turn the ignition switch ON (II).

11. Select EVAP CVS ON in the INSPECTION MENU with the HDS.

12. Apply vacuum to the hose until the FTP reads 1.90 V (-0.59 in.Hg, -15.1 mmHg).
    *   **NOTE:** Be careful not to exceed the vacuum. If you do, the FTP sensor can be damaged.

13. Monitor the FTP SENSOR in the DATA LIST for 1 minute with the HDS.

**Does the voltage increase more than 0.2 V (0.in.Hg, 2.5 mmHg)?**
*   **YES — Go to step 14.**
*   **NO — Go to step 19.**

14. Select EVAP CVS OFF in the INSPECTION MENU with the HDS.

11-526

---

### Printed page 11-527

<a id="p823"></a>
Source: [PDF p.823, printed p.11-527](../page-images/p0823.png).

## EVAP function test troubleshooting (continued)

15. Disconnect fresh air hoses (A) from vent shut valve (B); plug valve ports (C).
16. Apply vacuum to the hose from step 9 until FTP reads **1.90 V (−0.59 in.Hg, −15.1 mmHg)**. Do not exceed this vacuum; FTP sensor can be damaged.
17. Monitor FTP SENSOR for 1 minute. **Voltage rises more than 0.2 V (0.1 in.Hg, 2.5 mmHg):** Go to step 18. **Otherwise:** Replace vent shut valve (p. 11-543), then go to step 21.
18. Check purge line between canister and purge valve. **Line OK:** Replace **all listed parts**: FTP sensor O-ring (p. 11-542), vent shut valve case and O-ring (p. 11-543), and EVAP canister (p. 11-544); then go to step 21. **Line damaged:** Reconnect or repair hose, then go to step 21.
19. Select EVAP CVS OFF in HDS INSPECTION MENU.
20. Check fuel fill pipe and fuel vapor return pipe. **Both OK:** Check fuel pump base gasket (p. 11-487) and fuel tank, then go to step 21. **Damaged:** Repair or replace, then go to step 21.
21. Reconnect hoses and connectors.
22. Turn ignition ON (II).
23. Reset ECM with HDS.
24. Do ECM idle learn (p. 11-462).
25. Run EVAP FUNCTION TEST. **Result OK:** Troubleshooting complete. **Not OK:** Check FTP sensor, purge valve, vent shut valve, and ECM connections; return to step 1.

---

### Printed page 11-528

<a id="p824"></a>
Source: [PDF p.824, printed p.11-528](../page-images/p0824.png).

# EVAP System
## DTC Troubleshooting (cont'd)

### DTC P0457: EVAP System Leak Detected/Fuel Fill Cap Loose or Missing

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Check the fuel fill cap (the cap must say "TIGHTEN TO CLICK"). It should turn 1/4 turn after it's tight, then it clicks.

   Is the correct fuel fill cap installed and properly tightened?
   - **YES** — Go to step 2.
   - **NO** — Replace or tighten the cap, then go to step 19.

2. Check the fuel fill cap seal (A) and the fuel fill pipe mating surface (B). Verify that the fuel fill cap tether cord (C) is not caught under the cap.

   The cap, seal, pipe surface, and tether are identified in the source diagram.

   Is the fuel fill cap seal missing or damaged, is the fuel fill pipe damaged, or is the tether cord caught under the cap?
   - **YES** — Replace the fuel fill cap or the fuel fill pipe, then go to step 19.
   - **NO** — Go to step 3.

3. Turn the ignition switch ON (II).

4. Clear the DTC with the HDS.

5. Do the EVAP FUNCTION TEST in the INSPECTION MENU with the HDS.

   Is the result OK?
   - **YES** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor or the EVAP canister vent shut valve and the ECM.
   - **NO** — Go to step 6.

6. Turn the ignition switch OFF.

7. Remove the EVAP canister vent shut valve from the EVAP canister (see page 11-543).

8. Connect the 2P connector to the EVAP canister vent shut valve.

9. Turn the ignition switch ON (II).

10. Select EVAP CVS ON in the INSPECTION MENU with the HDS.

11. Check the EVAP canister vent shut valve (A) operation.

    Does the valve operate?
    - **YES** — Check the routing of the EVAP canister vent tube, then go to step 18.
    - **NO** — Go to step 12.

---

### Printed page 11-529

<a id="p825"></a>
Source: [PDF p.825, printed p.11-529](../page-images/p0825.png).

## EVAP function test troubleshooting (continued)

12. Turn ignition OFF.
13. Replace EVAP canister vent shut valve (p. 11-543).
14. Turn ignition ON (II).
15. Reset ECM with HDS.
16. Do ECM idle learn (p. 11-462).
17. Run EVAP FUNCTION TEST. **OK:** Troubleshooting complete. **Not OK:** Check connections at FTP sensor, vent shut valve, and ECM, then return to step 1.
18. Reinstall EVAP canister vent shut valve (p. 11-543).
19. Turn ignition ON (II).
20. Reset ECM with HDS.
21. Do ECM idle learn (p. 11-462).
22. Run EVAP FUNCTION TEST. **OK:** Troubleshooting complete. **Not OK:** Check connections at FTP sensor, vent shut valve, and ECM, then return to step 1.

---

### Printed page 11-530

<a id="p826"></a>
Source: [PDF p.826, printed p.11-530](../page-images/p0826.png).

# EVAP System
## DTC Troubleshooting (cont'd)
### DTC P0496: EVAP System High Purge Flow Detected

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Do the **EVAP FUNCTION TEST** in the **INSPECTION MENU** with the HDS.

Is the result OK?
*   **YES**—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister purge valve, or the EVAP canister vent shut valve and the ECM.
*   **NO**—Go to step 4.

4. Turn the ignition switch OFF.
5. Replace the EVAP canister purge valve (see page 11-542).
6. Turn the ignition switch ON (**II**).
7. Reset the ECM with the HDS.
8. Do the **ECM idle learn procedure** (see page 11-462).
9. Do the **EVAP FUNCTION TEST** in the **INSPECTION MENU** with the HDS.

Is the result OK?
*   **YES**—Troubleshooting is complete.
*   **NO**—Check for poor connections or loose terminals at the FTP sensor, the EVAP canister purge valve, or the EVAP canister vent shut valve and the **ECM**, then go to step 1.

**Page Reference:** 11-530

---

### Printed page 11-531

<a id="p827"></a>
Source: [PDF p.827, printed p.11-531](../page-images/p0827.png).

# DTC P0497: EVAP System Low Purge Flow

## Detected

### Special Tools Required
*   Vacuum/pressure gauge, 0—4 in.Hg, 07JAZ-001000B
*   Vacuum pump/gauge, 0—30 in.Hg, Snap-on YA4000A or equivalent, commercially available
*   Fuel pressure gauge attachment set 07AAJ-S6MA150

> **NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

---

**1.** Check the fuel fill cap installation (the cap must say "TIGHTEN TO CLICK". The cap should tighten 1/4 turn after it is tight.).

Is the fuel fill cap Installed and properly tightened?
*   **Y E S** — G o to step 2.
*   **N O** — Properly install the fuel fill cap, then go to step 23.

---

**2.** Turn the ignition switch ON (II).

**3.** Clear the DTC with the HDS.

**4.** Do the EVAP FUNCTION T E S T in the INSPECTION MENU with the HDS.

Is the result OK?
*   **YES** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister purge valve, or the EVAP canister vent shut valve and the ECM.
*   **N O** — G o to step 5.

---

**5.** Check for a loose or damaged EVAP canister purge line between the intake manifold and the EVAP canister purge valve.

Is the line OK?
*   **Y E S** — G o to step 6.
*   **N O** — Reconnect or repair the EVAP canister purge line, then go to step 23.

---

**6.** Disconnect the vacuum hose (A) from the EVAP canister purge valve (B) in the engine compartment, and connect a T-fitting (C) from the vacuum gauge and the vacuum pump/gauge, 0—30 in.Hg, to the EVAP canister purge valve as shown.

*(Diagram reference: Vacuum hose A, Valve B, T-fitting C)*

**7.** Select EVAP PCS ON in the INSPECTION MENU with the HDS.

**8.** Slowly apply about 2 kPa (0.6 in.Hg, 15 mmHg) of vacuum to the hose.

Does it hold vacuum?
*   **YES** — Check for blockage in the EVAP canister purge line between the intake manifold and the EVAP canister purge valve. If the vacuum hose is OK, replace the EVAP canister purge valve, then go to step 22.
*   **N O** — G o to step 9.

---

**9.** Reconnect the vacuum hose to the EVAP canister purge valve.

*(Page reference: cont'd on page 11-531)*

---

### Printed page 11-532

<a id="p828"></a>
Source: [PDF p.828, printed p.11-532](../page-images/p0828.png).

## EVAP system DTC troubleshooting (continued)

10. Disconnect vacuum hose from purge line on canister side; connect T-fitting (A), vacuum gauge, and 0–30 in.Hg vacuum pump/gauge.
11. Select EVAP PCS ON in HDS INSPECTION MENU.
12. Slowly apply **about 2 kPa (0.6 in.Hg, 15 mmHg)** vacuum. **Holds:** Check for restriction between purge valve and canister, then go to step 22. **Does not hold:** Go to step 13.
13. Remove FTP sensor with connector attached (p. 11-542).
14. Connect T-fitting (A), vacuum gauge, and 0–30 in.Hg pump/gauge to FTP sensor (B).
15. Record FTP SENSOR reading in HDS DATA LIST.
16. Slowly apply **about 1.3 kPa (0.4 in.Hg, 10 mmHg)** vacuum.
17. Check FTP SENSOR again. **Difference more than 1.1 kPa (0.31 in.Hg, 8 mmHg):** Go to step 18. **Otherwise:** Replace FTP sensor (p. 11-542), then go to step 22.
18. Reconnect vacuum hose to purge line (canister side) and reinstall FTP sensor.

See source image for hose and fitting layout.

---

### Printed page 11-533

<a id="p829"></a>
Source: [PDF p.829, printed p.11-533](../page-images/p0829.png).

Step 19: Disconnect vacuum hose (A) from EVAP canister purge valve (B), connect T-fitting (C) from vacuum gauge and vacuum pump/gauge (0–30 in.Hg) to hose. Step 20: Select EVAP C V S ON in INSPECTION MENU with HDS. Step 21: Apply ~2 kPa (0.6 in.Hg, 15 mmHg) vacuum; check if hose holds vacuum. If YES: Check blockage at EVAP canister port, go to step 22. If NO: Replace EVAP canister vent shut valve, go to step 22. Step 22: Reconnect all hoses. Step 23: Turn ignition switch ON (II). Step 24: Reset ECM with HDS. Step 25: Perform ECM idle learn procedure (see page 11-462). Step 26: Perform EVAP FUNCTION TEST in INSPECTION MENU with HDS. If result OK: Troubleshooting complete. If NO: Check poor connections/loose terminals at FTP sensor, EVAP canister purge valve, EVAP canister vent shut valve, and ECM; go to step 1.

---

### Printed page 11-534

<a id="p830"></a>
Source: [PDF p.830, printed p.11-534](../page-images/p0830.png).

# EVAP System
## DTC Troubleshooting (cont'd)
### DTC P0498: EVAP Canister Vent Shut Valve - Circuit Low Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS, then wait 5 seconds.
3. Check for Temporary DTCs or DTCs with the HDS.
   - Is DTC P0498 indicated?
     - **Y** — Go to step 6.
     - **NO** — Go to step 4.

4. Select EVAP CVS ON in the INSPECTION MENU with the HDS.
5. Check for Temporary DTCs or DTCs with the HDS.
   - Is DTC P0498 indicated?
     - **Y** — Go to step 6.
     - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the EVAP canister vent shut valve and the ECM.

6. Turn the ignition switch OFF.
7. Disconnect the EVAP canister vent shut valve 2P connector.
8. At the valve side, measure resistance between EVAP canister vent shut valve 2P connector terminals No. 1 and No. 2.

   **EVAP CANISTER VENT SHUT VALVE 2P CONNECTOR**
   *Terminal side of male terminals*

   Is there about 25-30 Ω at room temperature?
   - **Y** — Go to step 9.
   - **NO** — Go to step 12.

9. Jump the SCS line with the HDS.
10. Disconnect ECM connector E (31P).

    **ECM CONNECTOR E (31P)**
    *Wire side of female terminals*

    ```
    1 / ' 3 4 | 5
    / 8 9
    / 12 13 14 15 16 17 18 19 20 21
    22
    / 24 25
    / 27 28 2 9 30
    /
    V S V (LT G R N / W H T )
    ```

11. Check for continuity between ECM connector terminal E19 and body ground.

    Is there continuity?
    - **YES** — Repair short in the wire between the EVAP canister vent shut valve and the ECM (E19), then go to step 13.
    - **NO** — Go to step 21.

*Page Reference: 11-534*

---

### Printed page 11-535

<a id="p831"></a>
Source: [PDF p.831, printed p.11-535](../page-images/p0831.png).

## DTC P0498 troubleshooting (continued)

12. Replace EVAP canister vent shut valve (p. 11-543).
13. Reconnect ECM connector E (31P).
14. Reconnect vent shut valve 2P connector.
15. Turn ignition ON (II).
16. Reset ECM with HDS.
17. Do ECM idle learn (p. 11-462).
18. Select EVAP CVS ON in HDS INSPECTION MENU.
19. Check DTCs. **P0498 indicated:** Check vent shut valve and ECM connections, then return to step 1. **Not indicated:** Go to step 20.
20. Monitor OBD STATUS for P0498. **PASSED:** Troubleshooting complete; follow other DTCs from step 19. **FAILED:** Check valve and ECM connections, then return to step 1. **NOT COMPLETED:** Go to step 18.
21. Reconnect all connectors.
22. Update ECM software if needed (p. 11-216) or substitute known-good ECM (p. 11-217).
23. Select EVAP CVS ON in HDS INSPECTION MENU.
24. Check DTCs. **P0498 indicated:** Check valve and ECM connections. If ECM was updated, substitute known-good ECM and return to step 23; if substituted, return to step 1. **Not indicated:** The source says “go to step 24”; the following status check is step 25. Confirm against source image before following this branch.
25. Monitor OBD STATUS for P0498. **PASSED:** If updated, troubleshooting complete; if substituted, replace original ECM (p. 11-389). Follow other DTCs from step 24. **FAILED:** Check valve and ECM connections; if updated, substitute known-good ECM and return to step 23; if substituted, return to step 1. **NOT COMPLETED:** Return to step 23.

---

### Printed page 11-536

<a id="p832"></a>
Source: [PDF p.832, printed p.11-536](../page-images/p0832.png).

# EVAP System
## DTC Troubleshooting (cont'd)
### DTC P0499: EVAP Canister Vent Shut Valve - Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS, then wait 5 seconds.
3. Select EVAP C V S ON in the INSPECTION MENU with the HDS.
4. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P0499 indicated?**
- **Y E S** — G o to step 5.
- **NO** — Intermittent failure, the system is O K at this time. Check for poor connections or loose terminals at the EVAP canister vent shut valve and the E C M . B

5. Turn the ignition switch OFF.
6. Disconnect the EVAP canister vent shut valve 2P connector.
8. Measure voltage between EVAP canister vent shut valve 2P connector terminal No. 2 and body ground.

**E V A P C A N I S T E R V E N T S H U T V A L V E 2P C O N N E C T O R**
- **IG1 (WHT)** - Wire side of female terminals

**Is there battery voltage?**
- **Y E S** — G o to step 9.
- **NO** — Repair open in the wire between the EVAP canister vent shut valve and the A/F sensor relay (LAF), then go to step 16.

9. Turn the ignition switch OFF.
7. Turn the ignition switch ON (II).

**Page Reference:** 11-536

---

### Printed page 11-537

<a id="p833"></a>
Source: [PDF p.833, printed p.11-537](../page-images/p0833.png).

## DTC P0499 troubleshooting (continued)

10. Measure resistance between vent shut valve 2P terminals **1 and 2** at valve side. **About 25–30 Ω at room temperature:** Go to step 11. **Otherwise:** Go to step 15.
11. Jump SCS line with HDS.
12. Disconnect ECM connector E (31P).
13. Ground vent shut valve 2P terminal **1 (VSV, LT GRN/WHT)** with jumper wire.
14. Check continuity between ECM **E19 (VSV, LT GRN/WHT)** and body ground. **Continuity:** Go to step 23. **No continuity:** Repair open between valve and ECM E19, then go to step 16.
15. Replace vent shut valve (p. 11-543).
16. Reconnect all connectors.
17. Turn ignition ON (II).
18. Reset ECM with HDS.
19. Do ECM idle learn (p. 11-462).
20. Select EVAP CVS ON in HDS INSPECTION MENU.

See source image for connector orientation.

---

### Printed page 11-538

<a id="p834"></a>
Source: [PDF p.834, printed p.11-538](../page-images/p0834.png).

# EVAP System
## DTC Troubleshooting (cont'd)

**21.** Check for Temporary DTCs or DTCs with the HDS.

Is **DTC P0499** indicated?

*   **Y E S** — C h e c k f o r p o o r c o n n e c t i o n s o r l o o s e terminals at the EVAP canister vent shut valve and the E C M , then go to step 1.
*   **N O** — G o t o s t e p 2 2 .

**22.** Monitor the OBD S T A T U S f o r DTC P0499 in the DTCs MENU with the HDS.

Does the screen indicate PASSED?

*   **YES**—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 21, go to the indicated D T C s troubleshooting. •
*   **NO**—If the screen indicates FAILED, check for poor connections or loose terminals at the EVAP canister vent shut valve and the E C M , then go to step 1. If the screen indicates NOT COMPLETED, go to step 20.

**23.** Reconnect all connectors.

**24.** Update the E C M if it does not have the latest software (see page 11-216), or substitute a known-good E C M (see page 11-217).

**25.** Select EVAP C V S O N in the INSPECTION MENU with the HDS.

**26.** Check for Temporary DTCs or DTCs with the HDS.

Is **DTC P0499** indicated?

*   **Y E S** — C h e c k f o r p o o r c o n n e c t i o n s o r l o o s e terminals at the EVAP canister vent shut valve and the E C M . If the E C M was updated, substitute a known-good E C M (see page 11-217), then go to step 25. If the E C M was substituted, go to step 1.
*   **N O** — G o t o s t e p 2 7 .

**27.** Monitor the OBD S T A T U S f o r DTC P0499 in the DTCs MENU with the HDS.

Does the screen indicate PASSED?

*   **YES**—If the ECM was updated, troubleshooting is complete. If the E C M was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 26, go to the indicated D T C s troubleshooting. •
*   **NO**—If the screen indicates FAILED, check for poor connections or loose terminals at the EVAP canister vent shut valve and the E C M . If the ECM was updated, substitute a known-good E C M (see page 11-217), then go to step 25. If the E C M was substituted, go to step 1. If the screen indicates NOT COMPLETED, go to step 25.

**11-538**

---

### Printed page 11-539

<a id="p835"></a>
Source: [PDF p.835, printed p.11-539](../page-images/p0835.png).

# DTC P1454: FTP Sensor Range/Performance
## Problem
DTC P2422: EVAP Canister Vent Shut Valve Stuck Closed Malfunction

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Turn the ignition switch OFF.
4. Remove the fuel fill cap, and wait 1 minute.
5. Check the FTP SENSOR in the DATA LIST with the HDS.

Is It between -0.67 kPa and 0.67 kPa (-0.2 and 0.2 in.Hg, -5 and 5 mmHg), or 2.4-2.6 V?

* **Y E S** — G o to step 6.
* **N O** — G o to step 17.

6. Install the fuel fill cap.
7. Clear the DTC with the HDS.
8. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
9. Monitor the OBD **S T A T U S** for DTC P1454 in the DTCs MENU with the HDS.

Does the screen indicate FAILED?

* **Y E S** — G o to step 10.
* **NO** — If the screen indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor or the EVAP canister vent shut valve and the ECM. Also check for a blockage in the canister filter, vent hoses, and drain joint. If the screen indicates **NOT COMPLETED**, go to step 8 and recheck.

10. Clear the DTC with the HDS.
11. Turn the ignition switch OFF.
12. Remove the EVAP canister vent shut valve from the EVAP canister (see page 11-543).
13. Connect the **2P** connector to the EVAP canister vent shut valve.
14. Turn the ignition switch ON (**II**).
15. Select **EVAP C V S O N** in the INSPECTION MENU t with the HDS.
16. Check the EVAP canister vent shut valve (**A**) operation.

Does the valve operate?

* **YES** — Check for a blockage in the EVAP canister, canister filter, vent hoses, and drain joint, then install the EVAP canister vent shut valve, and go to step 23.
* **NO** — Replace the EVAP canister vent shut valve (see page 11-543), then go to step 23.

(cont'd)

11-539

---

### Printed page 11-540

<a id="p836"></a>
Source: [PDF p.836, printed p.11-540](../page-images/p0836.png).

# S2000 Fuel and Emissions Part F
## EVAP System DTC Troubleshooting (cont'd)

**Step 17.** Disconnect the air tube (A) from the FTP sensor (B).

**Step 18.** Check the FTP SENSOR in the DATA LIST with the HDS.

Is it between -0.67 kPa and 0.67 kPa (-0.2 and 0.2 in.Hg, -5 and 5 mmHg), or 2.4-2.6 V?

*   **YES** — Check for a blockage in the FTP sensor air tube, then go to step 23.
*   **NO** — Go to step 19.

**Step 19.** Turn the ignition switch OFF.

**Step 20.** Remove the FTP sensor (A) from the EVAP canister with its connector connected (see page 11-542).

**Step 21.** Turn the ignition switch ON (II).

**Step 22.** Check the FTP SENSOR in the DATA LIST with the HDS.

Is it between -0.67 kPa and 0.67 kPa (-0.2 and 0.2 in.Hg, -5 and 5 mmHg), or 2.4-2.6 V?

*   **YES** — Check for debris or clogging at the EVAP canister and the FTP sensor port, then go to step 23.
*   **NO** — Replace the FTP sensor (see page 11-542), then go to step 23.

**Step 23.** Turn the ignition switch ON (II).

**Step 24.** Reset the ECM with the HDS.

**Step 25.** Do the ECM idle learn procedure (see page 11-462).

**Step 26.** Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

**Step 27.** Check for Temporary DTCs or DTCs with the HDS.

Is DTC P1454 and/or P2422 indicated?

*   **YES** — Check for poor connections or loose terminals at the FTP sensor or the EVAP canister vent shut valve and the ECM, then go to step 1.
*   **NO** — Go to step 28.

---

### Printed page 11-541

<a id="p837"></a>
Source: [PDF p.837, printed p.11-541](../page-images/p0837.png).

Step 28: Monitor the OBD S T A T U S for DTC P1454 in the DTCs MENU with the HDS.

Decision Path:
- YES (Screen indicates PASSED): Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 27, go to the indicated D T C s troubleshooting.
- NO (Screen indicates FAILED): Check for poor connections or loose terminals at the FTP sensor, or the E V A P canister vent shut valve and the E C M, then go to step 1.
- NOT COMPLETED: Keep idling until a result comes on.

---

### Printed page 11-542

<a id="p838"></a>
Source: [PDF p.838, printed p.11-542](../page-images/p0838.png).

# EVAP System
## FTP Sensor Replacement: EVAP Canister Purge Valve Replacement

1. Remove the EVAP canister (see page 11-544).
2. Remove the retaining clip (A). Disconnect the EVAP canister purge valve 2P connector (A) and hoses (B).
3. Remove the FTP sensor (B).
4. Install the parts in the reverse order of removal with a new O-ring (C).

**Page Reference:** 11-542

---

### Printed page 11-543

<a id="p839"></a>
Source: [PDF p.839, printed p.11-543](../page-images/p0839.png).

# EVAP Canister Vent Shut Valve Replacement

1. Remove the EVAP canister (see page 11 -544).
2. Pry the lock tabs (A) outward, and remove the EVAP canister vent shut valve (B).
   **NOTE:** Be careful not to damage the lock tabs.
3. Install the parts in the reverse order of removal with a new O-ring (C).
   **NOTE:** Do not coat the O-ring with oil, etc.

**Page Reference:** 11-543

---

### Printed page 11-544

<a id="p840"></a>
Source: [PDF p.840, printed p.11-544](../page-images/p0840.png).

# EVAP System
## EVAP Canister Replacement

1. Remove the EVAP canister cover (**A**).
2. Remove the hoses (**A**), the FTP sensor 3P connector (**B**), and the EVAP canister vent shut valve 2P connector (**C**).
3. Remove the bolts (**D**).
4. Remove the EVAP canister assembly (**E**).
5. Remove the canister filter (**A**).
6. Remove the EVAP canister bracket (**A**).
7. Install the parts in the reverse order of removal.

**Page Reference:** 11-544

---

### Printed page 11-545

<a id="p841"></a>
Source: [PDF p.841, printed p.11-545](../page-images/p0841.png).

# Fuel Tank Vapor Control Float Replacement

1. Remove the fuel tank (see page 11-489).
2. Remove the fuel tank vapor control float (**A**) from the fuel tank (**B**).
3. Install the parts in the reverse order of removal with a new packing (**C**).

**Page Reference:** 11-545

---

### Printed page 11-546

<a id="p842"></a>
Source: [PDF p.842, printed p.11-546](../page-images/p0842.png).

## Source page condition

This PDF page is blank except for a black scan artifact. No readable manual content is present. Qwen returned an empty draft on the initial attempt and one narrower retry; Codex verified the page image.
