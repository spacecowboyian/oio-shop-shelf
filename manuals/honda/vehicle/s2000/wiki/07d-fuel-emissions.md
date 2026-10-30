# Fuel and Emissions Systems (Part D)

Reviewed conversion of PDF pp.568–658 (printed pp.11-272–11-362). Each page links to its source image for layout and connector details.

### Printed page 11-272

<a id="p568"></a>
Source: [PDF p.568, printed p.11-272](../page-images/p0568.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0117: ECT Sensor 1 Circuit Low Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Check **ECT SENSOR 1** in the DATA LIST with the HDS.
   Is about 356 °F (180 °C) or higher, or 0.08 V or less indicated?
   - **YES— Go to step 3.**
   - **NO— Intermittent failure, the system is OK at this time.** Check for poor connections or loose terminals at **ECT sensor 1** and the ECM.

3. Turn the ignition switch OFF.
4. Disconnect the **ECT sensor 1 2P connector**.
5. Turn the ignition switch ON (**II**).
6. Check **ECT SENSOR 1** in the DATA LIST with the HDS.
   Is about 356 °F (180 °C) or higher, or 0.08 V or less indicated?
   - **YES— Go to step 7.**
   - **NO— Go to step 11.**

7. Turn the ignition switch OFF.
8. Jump the **SCS line** with the HDS.
9. Disconnect ECM connector B (**24P**).
10. Check for continuity between **ECT sensor 1 2P connector terminal No. 1** and body ground.

    > **ECT SENSOR 1 2P CONNECTOR**
    > d&i
    > ECT1 I
    > (RED/WHT) I
    > Wire side of female terminals

    Is there continuity?
    - **YES— Repair short in the wire between ECT sensor 1 and the ECM (B8), then go to step 13.**
    - **NO— Go to step 18.**

11. Turn the ignition switch OFF.
12. Replace **ECT sensor 1** (see page 11-385).
13. Reconnect all connectors.
14. Turn the ignition switch ON (**II**).
15. Reset the ECM with the HDS.
16. Do the ECM idle learn procedure (see page 11-462).

**Page Reference:** 11-272

---

### Printed page 11-273

<a id="p569"></a>
Source: [PDF p.569, printed p.11-273](../page-images/p0569.png).

# PGM-FI System — DTC Troubleshooting

17. Check for Temporary DTCs or DTCs with the HDS. Is DTC P0117 indicated?

YES—Check for poor connections or loose terminals at ECT sensor 1 and the ECM ,then go to step 1.

NO—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •

18. Reconnect all connectors.

19. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

20. Check for Temporary DTCs or DTCs with the HDS. Is DTC P0117 indicated?

YES—Check for poor connections or loose terminals at ECT sensor 1 and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.

NO—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-274

<a id="p570"></a>
Source: [PDF p.570, printed p.11-274](../page-images/p0570.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0118: ECT Sensor 1 Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Check **ECT SENSOR 1** in the DATA LIST with the HDS.
   Is about ~40°F (**-40 °C**) or less, or 4.92 V or more indicated?
   - **YES** — Go to step 3.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at **ECT sensor 1** and the ECM.

3. Turn the ignition switch OFF.
4. Disconnect the **ECT sensor 1 2P connector**.
5. Connect **ECT sensor 1 2P connector** terminals No. 1 and No. 2 with a jumper wire.

   > **ECT SENSOR 1 2P C O N N ECT O R**
   > ECT1
   > (RED/WHT) | 1 | 2
   > SG 2 | ( G R N / Y E L )
   > JUMPER wire
   > Wire side of female terminals

6. Turn the ignition switch ON (**II**).
7. Check **ECT SENSOR 1** in the DATA LIST with the HDS.
   Is about -40°F (**-40 °C**) or less, or 4.92 V or more indicated?
   - **YES** — Go to step 8.
   - **NO** — Go to step 18.

8. Turn the ignition switch OFF.
9. Remove the jumper wire from **ECT sensor 1 2P connector**.
10. Turn the ignition switch ON (**II**).
11. Measure voltage between **ECT sensor 1 2P connector** terminal No. 1 and body ground.

    > **ECT SENSOR 1 2P C O N N ECT O R**
    > ECT1
    > (RED/WHT) | Wire side of female terminals
    > Is there about 5 V?
    - **YES** - Go to step 1 2 .
    - **NO** ^ Go to step 17.

12. Turn the ignition switch OFF.
13. Jump the **SCS line** with the HDS.
14. Disconnect **ECM connector A (31P)**.
15. Connect **ECT sensor 1 2P connector** terminal No. 2 to body ground with a jumper wire.

    > **ECT SENSOR 1 2P C O N N ECT O R**
    > 1 | 2
    > SG 2 (GRN/YEL)
    > JUMPER wire
    > Wire side of female terminals

**Page Reference:** 11-274

---

### Printed page 11-275

<a id="p571"></a>
Source: [PDF p.571, printed p.11-275](../page-images/p0571.png).

# S2000 Fuel and Emissions Part D
## Page 571

### Step 16
Check for continuity between ECM connector terminal A23 and body ground.

**ECM CONNECTOR A (31P)**
```
      1   2   3   4 | 5   6   7 | 8 | 9
     / / 13 14 15 16
     / 18
     / 20 21
     / 23 24 25 26
     / 28
     / 30 31
SG 2
```
*(Wire side of female terminals)*

**Terminal A23:** (GRN/YEL)

Is there continuity?
- **YES** — Go to step 26.
- **NO** — Repair open in the wire between the ECM (A23) and ECT sensor 1, then go to step 20.

---

### Step 17
Measure voltage between ECM connector terminal B8 and body ground.

**ECM CONNECTOR B (24P)**
```
      / 2 | 3   4   5   6 /
     M 8 / 10 11 / 13 / / /
     18 19 20 21 / / /
```
*(Wire side of female terminals)*

**Terminal B8:** ECT1 (RED/WHT)

Is there about 5 V?
- **YES** — Repair open in the wire between the ECM (B8) and ECT sensor 1, then go to step 20.
- **NO** — Go to step 25.

---

### Step 18
Turn the ignition switch OFF.

### Step 19
Replace ECT sensor 1 (see page 11-385).

### Step 20
Reconnect all connectors.

### Step 21
Turn the ignition switch ON (II).

### Step 22
Reset the ECM with the HDS.

### Step 23
Do the ECM idle learn procedure (see page 11-462).

### Step 24
Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0118 indicated?
- **YES** — Check for poor connections or loose terminals at ECT sensor 1 and the ECM, then go to step 1.
- **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

---

### Step 25
Turn the ignition switch OFF.

### Step 26
Reconnect all connectors.

### Step 27
Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

### Step 28
Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0118 indicated?
- **YES** — Check for poor connections or loose terminals at ECT sensor 1 and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
- **NO** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

---

*Source Page Reference: 11-275*

---

### Printed page 11-276

<a id="p572"></a>
Source: [PDF p.572, printed p.11-276](../page-images/p0572.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0125: ECT Sensor 1 Malfunction/Slow Response

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Start the engine, and let it idle for 5 minutes or more.
2. Check **ECT SENSOR 1** in the DATA LIST with the HDS.
   Is about 10°F (—12 °C) or less, or 4.45 V or more indicated?
   - **YES** — Go to step 9.
   - **NO** — Go to step 3.
3. Allow the engine to cool to 104 °F (40 °C) or less.
4. Note the value of **ECT SENSOR 1** and **ECT SENSOR 2** in the DATA LIST with the HDS.
5. Start the engine, and let it idle.
6. Let the engine idle until **ECT SENSOR 1** goes up 49 °F (27 °C) or more from the recorded temperature.
7. Note the value of **ECT SENSOR 2** in the DATA LIST with the HDS.
8. Compare **ECT SENSOR 2** and the recorded temperature.
   Did **ECT SENSOR 2** change 17 °F (9.5 °C) or more?
   - **YES** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM.
   - **NO** — Check the thermostat (see page 10-7). If the thermostat is OK, go to step 9. If the thermostat is faulty, replace it (see page 10-11), then go to step 9.

Turn the ignition switch OFF.

10. Replace **ECT sensor 1** (see page 11-385).
11. Turn the ignition switch ON (**II**).
12. Reset the ECM with the HDS.
13. Do the ECM idle learn procedure (see page 11-462).
14. Allow the engine to cool to ambient temperature.
15. Start the engine, and let it idle for 20 minutes.
16. Check for Temporary DTCs or DTCs with the HDS.
   Is **DTC P0125** indicated?
   - **YES** — Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM, then go to step 1.
   - **NO** — Go to step 17.
17. Monitor the **OBD STATUS** for **DTC P0125** in the DTCs MENU with the HDS.
   Does the screen indicate **PASSED**?
   - **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 16, go to the indicated **DTC** troubleshooting.
   - **NO** — If the screen indicates **FAILED**, check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the **ECM**, then go to step 1. If the screen indicates **NOT COMPLETED**, go to step 14.

---
**Page Reference:** 11-276

---

### Printed page 11-277

<a id="p573"></a>
Source: [PDF p.573, printed p.11-277](../page-images/p0573.png).

# DTC P0128: Cooling System Malfunction

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Turn the blower switch OFF.
4. Check the **FAN CTRL** in the DATA LIST with the HDS.
   - Is it **OFF**?
     - **YES** — Go to step 5.
     - **NO** — Wait until the FAN CTRL is off, then go to step 5.

5. Check the radiator fan operation.
   - Does the radiator fan keep running?
     - **YES** — Check the radiator fan circuit (see page 10-20). If the circuits and the switch are OK, go to step 19.
     - **NO** — Go to step 6.

6. Let the engine cool until the coolant temperature is **104 °F (40 °C)** or less.

7. Note the value of **ECT SENSOR 1** and **ECT SENSOR 2** in the DATA LIST with the HDS.

8. Start the engine, and let it idle.

9. Let the engine idle until **ECT SENSOR 1** goes up **49 °F (27 °C)** or more from the recorded temperature.

10. Check **ECT SENSOR 2** in the DATA LIST with the HDS.

11. Compare the value of recorded **ECTSENSOR 2** and the value of present **ECT SENSOR 2**.
    - Did temperature rise **17 °F (9.5 °C)** or more?
      - **YES** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM.
      - **NO** — Test the thermostat (see page 10-7), then go to step 12.

12. Turn the ignition switch ON (**II**).

13. Reset the ECM with the HDS.

14. Let the engine cool until the coolant temperature is between **21 °F (-6 °C)** and **104 °F (40 °C)**.

15. Do the ECM idle learn procedure (see page 11-462).

16. Test-drive at a steady speed between **15—75 mph (24—120 km/h)** for 10 minutes.

17. Check for Temporary DTCs or DTCs with the HDS.
    - Is DTC P0128 indicated?
      - **YES** — Check the cooling system, then go to step 1.
      - **NO** — Go to step 18.

18. Monitor the OBD **STATUS** for DTC P0128 in the DTCs MENU with the HDS.
    - Does the screen indicate **PASSED**?
      - **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 17, go to the indicated DTCs troubleshooting.
      - **NO** — If the screen indicates **FAILED**, check the cooling system, then go to step 1. If the screen indicates **NOT COMPLETED**, go to step 14.

*(cont'd)*

**Page Reference:** 11-277

---

### Printed page 11-278

<a id="p574"></a>
Source: [PDF p.574, printed p.11-278](../page-images/p0574.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

**19.** Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

**20.** Let the engine cool until the coolant temperature is between 21 °F (−6 °C) and 104 °F (40 °C).

**21.** Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

**22.** Test-drive at a steady speed between 15—75 mph (24—120 km/h) for 10 minutes.

**23.** Check for Temporary DTCs or DTCs with the HDS. Is DTC P0128 indicated?

*   **YES** — C h e c k for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM . If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 20. If the ECM was substituted, go to step 1.
*   **NO** — Go to step 24.

**24.** Monitor the OBD STATUS for DTC P0128 in the DTCs MENU with the HDS.

Does the screen indicate PASSED?

*   **YES**—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 23, go to the indicated DTCs troubleshooting.
*   **NO**—If the screen indicates FAILED, check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM . If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 20. If the ECM was substituted, go to step 1. If the screen indicates NOT COMPLETED, go to step 20 and recheck.

**11-278**

---

### Printed page 11-279

<a id="p575"></a>
Source: [PDF p.575, printed p.11-279](../page-images/p0575.png).

# DTC P0133: A/F Sensor (Sensor 1) Malfunction/Slow Response

**NOTE:**
*   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   If DTC P0139 is stored at the same time as DTC P0133, troubleshoot DTC P0139 first, then recheck for DTC P0133.

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
4. Test-drive under these conditions:
    *   Engine coolant temperature (ECT SENSOR 1) above 176 °F (80 °C)
    *   Transmission in 4th gear
    *   Drive the vehicle at 25 mph (40 km/h) or less for 5 minutes, then drive at steady speed between 2 6 - 8 1 mph ( 4 1 - 1 3 0 km/h).
5. Monitor the OBD STATUS for DTC P0133 in the DTCs MENU with the HDS.
    Does the screen indicate FAILED?
    *   **YES** — Go to step 6.
    *   **NO** — If the screen indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates O U T OF CONDITION, go to step 3 and recheck.

6. Turn the ignition switch OFF.
7. Replace the A/F sensor (Sensor 1) (see page 11-386).
8. Turn the ignition switch ON (II).
9. Reset the ECM with the HDS.
10. Do the ECM idle learn procedure (see page 11-462).
11. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
12. Test-drive under these conditions:
    *   Engine coolant temperature (ECT SENSOR 1) above 176 °F ( 8 0 * 0
    *   Transmission in 4th gear
    *   Drive the vehicle at 25 mph (40 km/h) or less for 5 minutes, then drive at steady speed between 2 6 - 8 1 mph ( 4 1 - 1 3 0 km/h).
13. Check for Temporary DTCs or DTCs with the HDS.
    Is DTC P0133 indicated?
    *   **YES** — Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM, then go to step 1.
    *   **NO** — Go to step 14.
14. Monitor the OBD STATUS for DTC P0133 in the DTCs MENU with the HDS.
    Does the screen indicate PASSED?
    *   **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 13, go to the indicated DTCs troubleshooting. •
    *   **NO** — If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM, then go to step 1. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates OUT OF CONDITION, goto step 11.

**Page Reference:** 11-279

---

### Printed page 11-280

<a id="p576"></a>
Source: [PDF p.576, printed p.11-280](../page-images/p0576.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0134: A/F Sensor (Sensor 1) Heater System Malfunction

**NOTE:**
*   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   If DTC P0135 is stored at the same time as DTC P0134, troubleshoot DTC P0135 first, then recheck for DTC P0134.

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

**11.** Monitor the OBD STATUS for DTC P0134 in the DTCs MENU with the HDS.

Does the screen indicate PASSED?
*   **YES**—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 10, go to the indicated DTCs troubleshooting.
*   **NO**—If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1), the A/F sensor relay (LAF), and the ECM , then go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

4. Check for Temporary DTCs or DTCs with the HDS.
Is DTC P0134 indicated?
*   **YES** — Go to step 5.
*   **NO**—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the A/F sensor relay (LAF), and the ECM . B

5. Turn the ignition switch OFF.
6. Replace the A/F sensor (Sensor 1) (see page 11-386).
7. Turn the ignition switch ON (II).
8. Reset the ECM with the HDS.
9. Do the ECM idle learn procedure (see page 11-462).
10. Check for Temporary DTCs or DTCs with the HDS.
Is DTC P0134 indicated?
*   **YES**—Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the A/F sensor relay (LAF), and the ECM , then go to step 1.
*   **NO**—Go to step 11.

**11-280**

---

### Printed page 11-281

<a id="p577"></a>
Source: [PDF p.577, printed p.11-281](../page-images/p0577.png).

# DTC P0135: A/F Sensor (Sensor 1) Heater Circuit Malfunction

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
4. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P0135 indicated?**
- **YES** — Go to step 5.
- **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the A/F sensor relay (LAF), and the ECM.

5. Turn the ignition switch OFF.
6. Check these fuses:
   - No. 15 LAF ('06-07 models: 20 A, '08 model: 15 A) fuse in the under-dash fuse/relay box.
   - No. 10IGP (LAF) (7.5 A) fuse in the under-dash fuse/relay box.
   - No. 59 DBW (20 A) fuse in the under-hood fuse/relay box.

**Are any of the above fuses blown?**
- **YES** — Repair short in the wire between the A/F sensor relay (LAF) and the fuses. Also replace the blown fuse(s), then go to step 23.
- **NO** — Go to step 7.

7. Disconnect the A/F sensor (Sensor 1) 4P connector.
8. At the A/F sensor side, measure resistance between A/F sensor (Sensor 1) 4P connector terminals No. 3 and No. 4.

> **A / F SENSOR ( SENSOR 1) 4P C O N N ECT O R**
> + B
> 1 2
> o A
> O 4
> A F S H T C
> Terminal side of male terminals

**Is there 2.1—2.9 Ω at room temperature?**
- **YES** — Go to step 9.
- **NO** — Go to step 22.

9. At the A/F sensor side, check for continuity between A/F sensor (Sensor 1) 4P connector terminal No. 2 and A/F sensor (Sensor 1) 4P connector terminals No. 3 and No. 4 individually.

> **A / F SENSOR ( SENSOR 1) 4P C O N N ECT O R**
> A F S H T C
> Terminal side of male terminals

**Is there continuity?**
- **YES** — Go to step 22.
- **NO** — Go to step 10.

*(cont'd)*

**Page Reference:** 11-281

---

### Printed page 11-282

<a id="p578"></a>
Source: [PDF p.578, printed p.11-282](../page-images/p0578.png).

# A/F Sensor Heater Circuit Troubleshooting (continued)

10. Jump the SCS line with the HDS.
11. Disconnect ECM connector A (31P).
12. Check continuity from ECM **A10 AFSHTC (GRN)** to ground. **YES:** Repair the short between ECM A10 and A/F sensor 1, then go to step 23. **NO:** Step 13.
13. Ground A/F sensor 1 4P connector terminal **4 AFSHTC (GRN)** with a jumper.
14. Check continuity from ECM A10 to ground. **YES:** Step 15. **NO:** Repair the open between ECM A10 and A/F sensor 1, then go to step 23.
15. Remove the A/F sensor relay (LAF), marked A in the source location diagram.

Refer to the source image for connector orientation and relay location.

---

### Printed page 11-283

<a id="p579"></a>
Source: [PDF p.579, printed p.11-283](../page-images/p0579.png).

# A/F Sensor Heater Circuit Troubleshooting (continued)

16. Ground A/F sensor 1 4P connector terminal **3 +B (WHT/BLK)** with a jumper.
17. Check continuity from A/F sensor relay (LAF) 4P connector terminal **2 +B (WHT)** to ground. **YES:** Step 18. **NO:** Repair the open between A/F sensor 1 and the relay; step 23.
18. Disconnect ECM connector E (31P).
19. Check continuity from ECM **E8 AFSHTCR (ORN)** to ground. **YES:** The printed source says to repair the open between ECM E8 and the A/F sensor relay; step 23. **NO:** Step 20.
20. Check continuity between ECM E8 and A/F sensor relay 4P connector terminal **3 AFSHTCR (ORN)**. **YES:** Step 21. **NO:** Repair the open between ECM E8 and the relay; step 23.

Refer to the source image for connector orientation.

---

### Printed page 11-284

<a id="p580"></a>
Source: [PDF p.580, printed p.11-284](../page-images/p0580.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

**21.** Check the A/F sensor relay (LAF) (see page 22-48).

Is the A/F sensor relay (LAF) OK ?

*   **YES** — Go to step 29.
*   **NO** — Replace the A/F sensor relay (LAF), then go to step 23.

**22.** Replace the A/F sensor (Sensor 1) (see page 11-386).

**23.** Reconnect all connectors.

**24.** Turn the ignition switch ON (**II**).

**25.** Reset the ECM with the HDS.

**26.** Do the ECM idle learn procedure (see page 11-462).

**27.** Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0135 indicated?

*   **YES** — Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1.
*   **NO** — Go to step 28.

**28.** Monitor the OBD STATUS for DTC P0135 in the DTCs MENU with the HDS.

Does the screen indicate PASSED?

*   **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 27, go to the indicated DTCs troubleshooting. •
*   **NO** — If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

**29.** Reconnect all connectors.

**30.** Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

**31.** Start the engine.

**32.** Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0135 indicated?

*   **YES** — Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the A/F sensor relay (LAF), and the ECM . If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 31. If the ECM was substituted, go to step 1.
*   **NO** — Go to step 33.

**33.** Monitor the OBD STATUS for DTC P0135 in the DTCs MENU with the HDS.

Does the screen indicate PASSED?

*   **YES** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 32, go to the indicated DTCs troubleshooting. •
*   **NO** — If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1), the A/F sensor relay (LAF), and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

**11-284**

---

### Printed page 11-285

<a id="p581"></a>
Source: [PDF p.581, printed p.11-285](../page-images/p0581.png).

# DTC P0137: Secondary HO2S (Sensor2)
## Circuit Low Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.
4. Check the HO2S S2 in the DATA LIST with the HDS.
   - Does the voltage stay at **0.29 V** or less?
     - **YES— Go to step 5.**
     - **NO— Intermittent failure, the system is OK at this time.** Check for poor connections or loose terminals at the secondary HO2S (Sensor 2) and at the ECM.

5. Turn the ignition switch OFF.
6. Disconnect the secondary HO2S (Sensor 2) **4P** connector.
7. Turn the ignition switch ON (**II**).
8. Check the HO2S S2 in the DATA LIST with the HDS.
   - Does the voltage stay at **0.29 V** or less?
     - **YES— Go to step 9.**
     - **NO— Go to step 13.**

9. Turn the ignition switch OFF.
10. Jump the **SCS** line with the HDS.
11. Disconnect ECM connector **E (31P)**.
12. Check for continuity between secondary HO2S (Sensor 2) **4P** connector terminal No. **2** and body ground.

> **SECONDARY HO2S (SENSOR 2) 4P CONNECTOR**
>
> ```
> 1 ? -
> 3 4
> SHO2S(WHT)
> ```
> *Terminal side of male terminals*

- Is there continuity?
  - **YES— Repair short in the wire between the ECM (E20) and the secondary HO2S (Sensor 2), then go to step 15.**
  - **NO— Go to step 23.**

13. Turn the ignition switch OFF.
14. Replace the secondary HO2S (Sensor 2) (see page **11-386**).
15. Reconnect all connectors.
16. Turn the ignition switch ON (**II**).
17. Reset the ECM with the HDS.
18. Do the ECM idle learn procedure (see page **11-462**).
19. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.

*(cont'd)*

**Page Reference:** 11-285

---

### Printed page 11-286

<a id="p582"></a>
Source: [PDF p.582, printed p.11-286](../page-images/p0582.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

**20.** Test-drive under these conditions:
*   Engine coolant temperature (**ECT SENSOR 1**) above **176 °F (80 °C)**
*   Transmission in **4th gear**
*   Engine speed at **1,500—3,000 rpm**
*   Drive about **1 minute or more**

**21.** Check for Temporary DTCs or DTCs with the HDS.
Is **DTC P0137** indicated?
*   **YES**—Check for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the **ECM**, then go to step **1**.
*   **NO**—Go to step **22**.

**22.** Monitor the **OBD STATUS** for **DTC P0137** in the **DTCs MENU** with the HDS.
Does the screen indicate **PASSED**?
*   **YES**—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step **21**, go to the indicated **DTCs** troubleshooting. •
*   **NO**—If the screen indicates **FAILED**, check for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the **ECM**, then go to step **1**. If the screen indicates **EXECUTING**, keep driving until a result comes on. If the screen indicates **O U T O F CONDITION**, go to step **20**.

**23.** Reconnect all connectors.

**24.** Update the **ECM** if it does not have the latest software (see page **11-216**), or substitute a known-good **ECM** (see page **11-217**).

**25.** Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.

**26.** Test-drive under these conditions:
*   Engine coolant temperature (**ECT SENSOR 1**) above **176 °F (80 °C)**
*   Transmission in **4th gear**
*   Engine speed at **1,500—3,000 rpm**
*   Drive about **1 minute or more**

**27.** Check for Temporary DTCs or DTCs with the HDS.
Is **DTC P0137** indicated?
*   **YES— C h e c k** for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the **ECM**. If the **ECM was updated**, substitute a known-good **ECM** (see page **11-217**), then go to step **26**. If the **ECM was substituted**, go to step **1**.
*   **NO— Go** to step **28**.

**28.** Monitor the **OBD STATUS** for **DTC P0137** in the **DTCs MENU** with the HDS.
Does the screen indicate **PASSED**?
*   **YES**—If the ECM was updated, troubleshooting is complete. If the **ECM was substituted**, replace the original **ECM** (see page **11-389**). If any other Temporary DTCs or DTCs were indicated in step **27**, go to the indicated **DTCs** troubleshooting. •
*   **NO**—If the screen indicates **FAILED**, check for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the **ECM**. If ECM was updated, substitute a known-good ECM (see page **11-217**), then go to step **26**. If ECM was substituted, go to step **1**. If the screen indicates **EXECUTING**, keep driving until a result comes on. If the screen indicates **O U T OF CONDITION**, go to step **26**.

**11-286**

---

### Printed page 11-287

<a id="p583"></a>
Source: [PDF p.583, printed p.11-287](../page-images/p0583.png).

# DTC P0138: Secondary HO2S (Sensor 2)
## Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.
4. Check the **HO2S S 2** in the DATA LIST with the HDS.
   - Does the voltage stay at **1.27 V** or more?
     - **YES** — Go to step 5.
     - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the ECM.

5. Turn the ignition switch OFF.
6. Disconnect the secondary **HO2S (Sensor 2) 4P** connector.
7. Connect secondary **HO2S (Sensor 2) 4P** connector terminals No. 1 and No. 2 with a jumper wire.

```
S E C O N D A R Y HO2S ( SENSOR 2)
4P C O N N ECT O R
JUMPER wire
S G 2 (GRN/YEL)   1
                    |
                    | Jumper Wire
                    |
S HO2S (WHT)   2
                    |
                    |
                    +--+
                    |  |
                    3  4
Terminal side of male terminals
```

8. Turn the ignition switch ON (**II**).
9. Check the **HO2S S2** in the DATA LIST with the HDS.
   - Does the voltage stay at **1.27 V** or more?
     - **YES** — Go to step 10.
     - **NO** — Go to step 19.

10. Turn the ignition switch OFF.
11. Remove the jumper wire from the secondary **HO2S (Sensor 2) 4P** connector,
12. Connect secondary **HO2S (Sensor 2) 4P** connector terminal No. 2 to body ground with a jumper wire.

```
S E C O N D A R Y HO2S ( SENSOR 2)
4P C O N N ECT O R
1
                    |
                    | Jumper Wire
                    |
                    +--+
                    |  |
                    3  4
S HO2S (WHT)   2
Terminal side of male terminals
```

13. Turn the ignition switch ON (**II**).
14. Check the **HO2S S 2** in the DATA LIST with the HDS.
    - Does the voltage stay at **1.27 V** or more?
      - **YES** — Go to step 15.
      - **NO** — Repair open in the wire between the ECM (**A23**) and the secondary **HO2S (Sensor 2)**, then go to step 21.

(cont'd)

Page Reference: 11-287

---

### Printed page 11-288

<a id="p584"></a>
Source: [PDF p.584, printed p.11-288](../page-images/p0584.png).

# PGM-FI System — DTC Troubleshooting

15. Turn the ignition switch OFF.

16. Jump the SCS line with the HDS.

17. Disconnect ECM connector E (31P).

18. Check for continuity between ECM connector terminal E20 and body ground. ECM C O N N ECT O R E (31P) 1 /' 3 4 | 5 / \ 7 I8 i 9 / 11 12 13 14 15 16 17 18 19 20 21 22 24 25 / 27 28 29 3D / S HO2S (RED) Wire side of female terminals Is there continuity? YES— Go to step 29.

NO—Repair open in the wire between the ECM (E20) and the secondary HO2S (Sensor 2), then go to step 21.

19. Turn the ignition switch OFF.

20. Replace the secondary HO2S (Sensor 2) (see page 11-386).

21. Reconnect all connectors.

22. Turn the ignition switch ON (II).

23. Reset the ECM with the HDS.

24. Do the ECM idle learn procedure (see page 11-462).

25. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.

26. Test-drive under these conditions:

• Engine coolant temperature (ECT SENSOR 1) above 176 °F (80 °C)

• Transmission in 4th gear

• Engine speed at 1,500—3,000 rpm

• Drive 1 minute or more

27. Check for Temporary DTCs or DTCs with the HDS. Is DTC P0138 indicated? YES— Check for poor connections or loose terminals at the secondary HO2S (Sensor 2) and the ECM , then go step 1. NO— Go to step 28.

28. Monitor the OBD STATUS for DTC P0138 in the DTCs MENU with the HDS. Does the screen indicate PASSED?

YES—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 27, go to the indicated DTCs troubleshooting. • NO— I f the screen indicates FAILED, check for poor connections or loose terminals at the secondary HO2S (Sensor 2) and the ECM , then go to step 1. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates OUT OF CONDITION, go to step 26.

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-289

<a id="p585"></a>
Source: [PDF p.585, printed p.11-289](../page-images/p0585.png).

# PGM-FI System — DTC Troubleshooting

29. Reconnect all connectors.

30. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

31. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.

32. Test-drive under these conditions:

• Engine coolant temperature (ECT SENSOR 1) above 176 °F (80 °C)

• Transmissionin 4th gear

• Engine speed at 1,500—3,000 rpm

• Drive 1 minute or more

33. Check for Temporary DTCs or DTCs with the HDS. Is DTC P0138 indicated?

YES—Check for poor connections or loose terminals at the secondary HO2S (Sensor 2) and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 32. If the ECM was substituted, go to step 1.

NO—Go to step 34.

34. Monitor the OBD STATUS for DTC P0138 in the DTCs MENU with the HDS. Does the screen indicate PASSED?

YES—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 33, go to the indicated DTCs troubleshooting. •

NO—If the screen indicates FAILED, check for poor connections or loose terminals at the secondary HO2S (Sensor 2) and the ECM . If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 32. If the ECM was substituted, go to step 1. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates OUT OF CONDITION, go to step 32.

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-290

<a id="p586"></a>
Source: [PDF p.586, printed p.11-290](../page-images/p0586.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0139: Secondary HO2S (Sensor2) Slow Response

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.
4. Test-drive under these conditions:
   - Engine coolant temperature (**ECT SENSOR 1**) above 176 °F (80 °C)
   - Transmission in 4th gear
   - Vehicle speed at 35 mph (56 km/h) or more
   - Drive 50 seconds
5. Monitor the **OBD STATUS** for DTC P0139 in the **DTCs MENU** with the HDS.
   Does the screen indicate **FAILED**?
   - **YES** — Go to step 6.
   - **NO** — If the screen indicates **PASSED**, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the **ECM**. If the screen indicates **EXECUTING**, keep driving until a result comes on. If the screen indicates **O U T OF CONDITION**, go to step 3 and recheck.

6. Turn the ignition switch OFF.
7. Replace the secondary **HO2S (Sensor 2)** (see page 11-386).
8. Turn the ignition switch ON (**II**).
9. Reset the **ECM** with the HDS.
10. Do the **ECM** idle learn procedure (see page 11-462).
11. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.
12. Test-drive under these conditions:
    - Engine coolant temperature (**ECT SENSOR 1**) above 176 °F (80 °C)
    - Transmission in 4th gear
    - Vehicle speed at 35 mph (56 km/h) or more
    - Drive 50 seconds
13. Check for Temporary DTCs or DTCs with the HDS.
    Is DTC P0139 indicated?
    - **YES** — Check for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the **ECM**, then go to step 1.
    - **NO** — Go to step 14.
14. Monitor the **OBD STATUS** for DTC P0139 in the **DTCs MENU** with the HDS.
    Does the screen indicate **PASSED**?
    - **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 13, goto the indicated **DTCs** troubleshooting.*
    - **NO** — If the screen indicates **FAILED**, check for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the **ECM**. If the screen indicates **EXECUTING**, keep driving until a result comes on. If the screen indicates **O U T OF CONDITION**, go to step 12.

*See page 11-290

---

### Printed page 11-291

<a id="p587"></a>
Source: [PDF p.587, printed p.11-291](../page-images/p0587.png).

# DTC P0141: Secondary HO2S (Sensor 2)
## Heater Circuit Malfunction

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine.
4. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P0141 indicated?**
- **YES** — Go to step 5.
- **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the secondary HO2S (Sensor 2) and the ECM . B

5. Turn the ignition switch OFF.
6. Check the No. 6 ACG (15 A) fuse in the under-dash fuse/relay box.

**Is the fuse OK?**
- **YES** — Go to step 6.
- **NO** — Repair short in the wire between the secondary H 02S (Sensor2) and the No. 6 ACG (15 A) fuse, then go to step 23.

7. Disconnect the secondary HO2S (Sensor 2) 4P connector.
8. At the secondary H 02S (Sensor 2) side, measure resistance between secondary H 02S (Sensor 2) 4P connector terminals No. 3 and No. 4.

```
S E C O N D A R Y HO2S ( SENSOR 2)
4P C O N N ECT O R
r 2
3 4
Wire side of female terminals
```

**Is there 5.0—6.4 Ω at room temperature?**
- **YES** — Go to step 9.
- **NO** — Go to step 22.

9. At the secondary H 02S (Sensor 2) side, check for continuity between body ground and secondary HO2S (Sensor 2) 4P connector terminals No. 3 and No. 4 individually.

```
S E C O N D A R Y HO2S ( SENSOR 2)
4P C O N N ECT O R
Wire side of female terminals
```

**Is there continuity?**
- **YES** — Go to step 22.
- **NO** — Go to step 10.

(cont'd)

11-291

---

### Printed page 11-292

<a id="p588"></a>
Source: [PDF p.588, printed p.11-292](../page-images/p0588.png).

# Secondary HO2S Heater Troubleshooting (continued)

10. Turn ignition ON (II).
11. Check for battery voltage between secondary HO2S sensor 2 4P connector terminals **3 SO2SHTC (BLK/WHT)** and **4 IG1 (BLK/YEL)**, measured from the terminal side of male terminals. **YES:** Step 12. **NO:** Step 16.
12. Turn ignition OFF.
13. Jump SCS with HDS.
14. Disconnect ECM connector E (31P).
15. Check continuity from ECM **E21 SO2SHTC (BLK/WHT)** to ground. **YES:** Repair short between ECM E21 and secondary HO2S; step 23. **NO:** Step 29.
16. Check for battery voltage from secondary HO2S connector terminal **4 IG1 (BLK/YEL)** to ground. **YES:** Step 17. **NO:** Check No. 6 ACG (15 A) fuse in under-dash box; if good, repair open between fuse and secondary HO2S; step 23.
17. Turn ignition OFF.
18. Jump SCS with HDS.
19. Disconnect ECM connector E (31P).
20. Ground secondary HO2S connector terminal **3 SO2SHTC (BLK/WHT)** with a jumper.

Refer to the source image for connector orientation.

---

### Printed page 11-293

<a id="p589"></a>
Source: [PDF p.589, printed p.11-293](../page-images/p0589.png).

# Page 589 Transcription

## Step 21
Check for continuity between ECM connector terminal E21 and body ground.

**ECM Connector Diagram (31P)**
```
      1 .1/ 3 4 | 5 /\ 7
     I8 | 9
    / 11 12 13 14 15 16 17 18 19 20 21
   22
  / 24 25
 / 27 28 29 30
/
S 0 2 S H T C
(BLK/WHT)
```
*Wire side of female terminals*

**Is there continuity?**
- **YES** — Go to step 29.
- **NO** — Repair open in the wire between the ECM (E21) and the secondary HO2S (Sensor 2), then go to step 23.

## Step 22
Replace the secondary HO2S (Sensor 2) (see page 11-386).

## Step 23
Reconnect all connectors.

## Step 24
Turn the ignition switch ON (II).

## Step 25
Reset the ECM with the HDS.

## Step 26
Do the ECM idle learn procedure (see page 11-462).

## Step 27
Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P0141 indicated?**
- **YES** — Check for poor connections or loose terminals at the secondary HO2S (Sensor 2) and the ECM, then go to step 1.
- **NO** — Go to step 28.

## Step 28
Monitor the OBD STATUS for DTC P0141 in the DTCs MENU with the HDS.

**Does the screen indicate PASSED?**
- **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 27, go to the indicated DTCs troubleshooting.
- **NO** —
  - If the screen indicates **FAILED**, check for poor connections or loose terminals at the secondary HO2S (Sensor 2) and the ECM, then go to step 1.
  - If the screen indicates **NOT COMPLETED**, keep idling until a result comes on.

## Step 29
Reconnect all connectors.

## Step 30
Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

## Step 31
Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P0141 indicated?**
- **YES** — Check for poor connections or loose terminals at the secondary HO2S (Sensor 2) and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
- **NO** — Go to step 32.

## Step 32
Monitor the OBD STATUS for DTC P0141 in the DTCs MENU with the HDS.

**Does the screen indicate PASSED?**
- **YES** —
  - If the ECM was updated, troubleshooting is complete.
  - If the ECM was substituted, replace the original ECM (see page 11-389).
  - If any other Temporary DTCs or DTCs were indicated in step 31, go to the indicated DTCs troubleshooting.
- **NO** —
  - If the screen indicates **FAILED**, check for poor connections or loose terminals at the secondary HO2S (Sensor 2) and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
  - If the screen indicates **NOT COMPLETED**, keep idling until a result comes on.

**Page Reference:** 11-293

---

### Printed page 11-294

<a id="p590"></a>
Source: [PDF p.590, printed p.11-294](../page-images/p0590.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0171: Fuel System Too Lean
### DTC P0172: Fuel System Too Rich

**NOTE:**
*   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   If some of the DTCs listed below are stored at the same time as DTC P0171 and/or P0172, troubleshoot those DTCs first, then recheck for P0171 and/or P0172.

| Related DTCs | Description |
| :--- | :--- |
| P0107, P0108, P1128, P1129 | Manifold absolute pressure (MAP) sensor |
| P0133, P1157, P2195, P2238, P2252, P2A00 | Air fuel ratio (A/F) sensor (Sensor 1) |
| P0134, P0135 | Air fuel ratio (A/F) sensor (Sensor 1) heater |
| P0137, P0138, P0139 | Secondary H2S (Sensor 2) |
| P0141 | Secondary H2S (Sensor 2) heater |
| P0443, P0496 | EVAP canister purge valve |
| P2646, P2647, P2648, P2649 | VTEC system |
| P2279 | Intake air leakage |

1.  Check the fuel pressure (see page 11-477).

    **Is the fuel pressure OK?**

    *   **YES** — Check the engine valve clearances and adjust if necessary (see page 6-10). If the valve clearances are OK, replace the injectors (see page 11-382), then go to step 2.
        *   **NO**
            *   If the pressure is too high, replace the fuel pressure regulator (see page 11-486), then go to step 2.
            *   If the pressure is too low, check the fuel pump (see page 11-470) and the fuel feed line (see page 11-478), then go to step 2.

2.  Turn the ignition switch ON (**II**).
3.  Reset the ECM with the HDS.
4.  Do the **ECM** idle learn procedure (see page 11-462).
5.  Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
6.  Test-drive under these conditions:
    *   Engine coolant temperature (**ECT SENSOR 1**) above 158 °F (70 °C)
    *   Transmission in 5th gear
    *   Drive at a steady speed between 15—75 mph (24–120 km/h)

**NOTE:** DTC P0171 and/or P0172 may take up to 80 minutes of test driving to set. Using the HDS, monitor the air fuel feed back average (**AF FB AVE**). If the **AF FB AVE** stays within 0.8—1.25, there is no problem at this time.

7.  Check for Temporary DTCs or DTCs with the HDS.

    **Is DTC P0171 or P0172 indicated?**

    *   **YES** — Go to step 1.
    *   **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated **DTCs** troubleshooting.

*Page Reference: 11-294*

---

### Printed page 11-295

<a id="p591"></a>
Source: [PDF p.591, printed p.11-295](../page-images/p0591.png).

# PGM-FI System — DTC Troubleshooting

DTC P0300: Random Misfire and Any Combination of the Following:

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected Special Tools Required

• Pressure gauge adapter 07NAJ-P07010A

•A/T low pressure gauge w/panel 07406-0070301

•A/T pressure hose 07406-0020201

•A/T pressure hose, 2,210 mm 07MAJ-PY4011A

•A/T pressure hose, adapter 07MAJ-PY40120

NOTE:

• Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

• If the misfire is frequent enough to trigger detection of increased emissions during 2 consecutive driving cycles, the MIL will come on, and DTC P0300 (and some combination of P0301 through P0304) will be stored.

• If the misfire is frequent enough to damage the catalyst, the MIL will flash whenever the misfire occurs, and DTC P0300 (and some combination of P0301 through P0304) will be stored. When the misfire stops, the MIL will remain on.

• Troubleshoot the following DTCs first, if any of them were stored along with the random misfire DTC(s): P0107, P0108, P1128, P1129: Manifold absolute pressure (MAP) sensor P0171, P0172: Fuel system P0335, P0339: Crankshaft position (CKP) sensor P0365, P0369: Camshaft position (CMP) sensor P0506, P0507: Idle control system P2646, P2647, P2648, P2649: VTEC system

1. Turn the ignition switch ON (II).

2. Clear the DTC with the HDS.

3. Start the engine (in neutral), then let it idle without load.

4. Monitor the OBD STATUS for DTC P0301, P0302, P0303, or P0304 in the DTCs MENU with the HDS. Does the screen indicate FAILED? YES— Go to step 9.

NO—If the screen indicates PASSED, go to step 5. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates OUT OF CONDITION, wait for several minutes, and recheck.

5. Check the CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE in the DATA LIST for 10 minutes with the HDS. Does CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE show misfire counts? YES— Go to step 9.

NO—Go to step 6.

6. Test-drive the vehicle for several minutes in the range of these recorded freeze data parameters:

• ENGINE S P E E D

• VSS

• REL TP SENSOR

• CLV (calculated load value)

7. Monitor the OBD STATUS for DTC P0301, P0302, P0303, or P0304 in the DTCs MENU with the HDS. Does the screen indicate FAILED? YES— Go to step 9.

NO—If the screen indicates PASSED, go to step 8. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates OUT OF CONDITION, go to step 6 and recheck. (cont'd)

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-296

<a id="p592"></a>
Source: [PDF p.592, printed p.11-296](../page-images/p0592.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

8. Check the CYL1 MISFIRE/CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE In the DATA LIST for 10 minutes with the HDS.

Does CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE show misfire counts?

*   **YES** — Go to step 9.
*   **NO** — Intermittent failure, the system is OK at this time.

9. Turn the ignition switch OFF.

10. Check the fuel quality.

Is the quality good?

*   **YES** — Go to step 11.
*   **NO** — Drain the tank and fill with known-good fuel, then go to step 20.

11. Inspect the spark plugs (see page 4-28). If the spark plugs are fouled or worn, replace them.

12. Test-drive the vehicle for several minutes in the range of these recorded freeze data parameters:
    *   ENGINE S P E E D
    *   VSS
    *   REL TP SENSOR
    *   CLV (calculated load value)

13. Check the CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE in the DATA LIST for 10 minutes with the HDS.

Does CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE show misfire counts?

*   **YES** — Go to step 14.
*   **NO** — Go to step 20.

14. Check the fuel pressure (see page 11-477).

Is the fuel pressure OK ?

*   **YES** — Go to step 15.
*   **NO**
    *   If the pressure is too high, replace the fuel pressure regulator (see page 11-486), then go to step 20.
    *   If the pressure is too low, check the fuel pump, the fuel feed pipe, and the fuel filter. If they are OK, replace the fuel pressure regulator (see page 11-486), then go to step 20.

15. Turn the ignition switch OFF.

16. Remove the rocker arm oil pressure switch (VTEC oil pressure switch) (A), and install the special tools as shown, then attach the rocker arm oil pressure switch (VTEC oil pressure switch) (A) to the pressure gauge adapter (B).

> **NOTE:** Install the parts in the reverse order of removal with a new O-ring.

(2.2 kgf m, 16 Ibf ft)

17. Reconnect the rocker arm oil pressure switch (VTEC oil pressure switch) 2P connector.

18. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

**11-296**

---

### Printed page 11-297

<a id="p593"></a>
Source: [PDF p.593, printed p.11-297](../page-images/p0593.png).

# Misfire Troubleshooting (continued)

19. Check oil pressure at 1,000 and 2,000 rpm. Is it below **49 kPa (0.5 kgf/cm², 7 psi)**? **YES:** Check for air in the fuel line, then go to step 20. **NO:** Inspect the VTEC system, then go to step 20.
20. Turn ignition ON (II).
21. Reset ECM with HDS.
22. Clear CKP pattern with HDS.
23. Perform ECM idle learn (p.11-462).
24. Perform CKP pattern learn (p.11-214).
25. Test-drive for several minutes under recorded freeze-data conditions: engine speed, VSS, relative TP sensor, and CLV.
26. Check Temporary DTCs or DTCs. **P0300, P0301, P0302, P0303, or P0304 YES:** Check ignition coil, injector, and ECM connections, then use the cylinder-misfire procedure (p.11-298). **NO:** Go to step 27.
27. Monitor OBD STATUS for P0301–P0304. **PASSED:** Troubleshooting complete; address other DTCs from step 26. **FAILED:** Return to step 1. **EXECUTING:** Keep driving. **OUT OF CONDITION:** Return to step 25.

---

### Printed page 11-298

<a id="p594"></a>
Source: [PDF p.594, printed p.11-298](../page-images/p0594.png).

PGM-FI System
DTC Troubleshooting (cont'd)
DTC P0301: No. 1 Cylinder Misfire Detected
DTC P0302: No. 2 Cylinder Misfire Detected
DTC P0303: No. 3 Cylinder Misfire Detected
DTC P0304: No. 4 Cylinder Misfire Detected
NOTE: Before you troubleshoot, record all freeze data
and any on-board snapshot, and review the general
troubleshooting information (see page 11-213).
1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine, then let it idle without load
(in neutral).
4. Monitor the OBD STATUS for DTC P0301, P0302,
P0303, or P0304 in the DTCs MENU with the HDS.
Does the screen indicate FAILED?
YES— Go to step 9.
NO—If the screen indicate PASSED, go to step 5. If
the screen indicates EXECUTING, keep idling until
a result comes on. If the screen indicates O U T OF
CONDITION, wait for several minutes, and recheck.
5. Check the CYL1 MISFIRE, CYL2 MISFIRE, CYL3
MISFIRE and/or CYL4 MISFIRE in the DATA LIST for
10 minutes with the HDS.
Does CYL1 MISFIRE, CYL2 MISFIRE, CYL3
MISFIRE and/or CYL4 MISFIRE show misfire
counts?
YES— Go to step 9.
NO— Go to step 6.
6. Test-drive the vehicle for several minutes in the
range of these recorded freeze data parameters:
• ENGINE S P E E D
• VSS
• REL TP SENSOR
• CLV (calculated load value)
7. Monitor the OBD STATUS for DTC P0301, P0302,
P0303, or P0304 in the DTCs MENU with the HDS.
Does the screen indicate FAILED?
YES— Go to step 9.
NO—If the screen indicate PASSED, go to step 8. If
the screen indicates EXECUTING, keep driving until
a result comes on. If the screen indicates O U T OF
CONDITION, go to step 6 and recheck.
8. Check the CYL1 MISFIRE,CYL2 MISFIRE, CYL3
MISFIRE, and/or CYL4 MISFIRE in the DATA LIST
for 10 minutes with the HDS.
Does CYL1 MISFIRE, CYL2 MISFIRE, CYL3
MISFIRE, and/or CYL4 MISFIRE show misfire
counts?
YES— Go to step 9.
NO—Intermittent failure, the system is OK at this
time. Check for loose wires or poor connections in the fuel system c i r c u i t s
9. Turn the ignition switch OFF.
10. Remove the fuel rail cover.
11. Start the engine, and listen for a clicking sound at
the injector of the problem cylinder.
Does the injector click?
YES— Go to step 12.
NO— Go to step 43.
12. Turn the ignition switch OFF.
13. Exchange the ignition coil from the problem
cylinder with one from another cylinder.
14. Test-drive the vehicle for several minutes in the
range of these recorded freeze data parameters:
• ENGINE S P E E D
• VSS
• REL TP SENSOR
• CLV (calculated load value)
11-298

---

### Printed page 11-299

<a id="p595"></a>
Source: [PDF p.595, printed p.11-299](../page-images/p0595.png).

# PGM-FI System — DTC Troubleshooting

15. Check the CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE in the DATA LIST for 10 minutes with the HDS. Does CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE show misfire counts? YES— Go to step 16.

NO—Intermittent misfire due to poor contact at the ignition coil connector (no misfire at this time). Make sure the coil connections are secure. •

16. Determine which cylinder had the misfire. Does the misfire occur in the cylinder where the ignition coil was exchanged?

YES—Replace the faulty ignition coil (see page 4-25), then go to step 63.

NO—Go to step 17.

17. Turn the ignition switch OFF.

18. Exchange the spark plug from the problem cylinder with one from another cylinder.

19. Test-drive the vehicle for several minutes in the range of these recorded freeze data parameters:

• E N G I N E S P E E D

• VSS

• REL TP SENSOR

• CLV (calculated load value)

20. Check the CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE in the DATA LIST for 10 minutes with the HDS. Does CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE show misfire counts? YES— Go to step 21.

NO—Intermittent misfire due to spark plug fouling (no misfire at this time). •

21. Determine which cylinder had the misfire. Does the misfire occur in the cylinder where the spark plug was moved?

YES—Replace the faulty spark plug, then go to step 63.

NO—Go to step 22.

22. Turn the ignition switch OFF.

23. Exchange the injector from the problem cylinder with one from the another cylinder.

24. Start the engine, and let it idle for 2 minutes.

25. Test-drive the vehicle for several minutes in the range of these recorded freeze data parameters:

• ENGINE S P E E D

• VSS

• R E L TP SENSOR

• CLV (calculated load value)

26. Check the CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE in the DATA LIST for 10 minutes with the HDS. Does CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE show misfire counts? YES— Go to step 27.

NO—Intermittent misfire due to bad contact in the injector connector (no misfire at this time). Check for poor connections or loose terminals at the injector.!

27. Determine which cylinder had the misfire. Does the misfire occur in the cylinder where the injector was exchanged?

YES—Replace the faulty injector (see page 11-382), then go to step 63.

NO—Go to step 28.

28. Turn the ignition switch OFF. (cont'd)

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-300

<a id="p596"></a>
Source: [PDF p.596, printed p.11-300](../page-images/p0596.png).

# Misfire Troubleshooting (continued)

29. Disconnect the ignition coil 3P connector from the problem cylinder.
30. Turn ignition ON (II).
31. Check for battery voltage between ignition coil 3P terminal **3, IG (BLK/YEL)** and ground. **YES:** Step 32. **NO:** Repair open between ignition coil and ignition coil relay; step 63.
32. Turn ignition OFF.
33. Check continuity between ignition coil 3P terminal **2, GND (BLK)** and ground. **YES:** Step 34. **NO:** Repair open between ignition coil and G101; step 63.
34. Turn ignition OFF.
35. Jump SCS with HDS.
36. Disconnect ECM connector A (31P).
37. Check continuity between ground and the ECM terminal for the problem cylinder. **YES:** Repair short between ECM and ignition coil; step 63. **NO:** Step 38.

| Cylinder | DTC | ECM terminal | Wire |
|---|---|---|---|
| 1 | P0301 | A16 | WHT |
| 2 | P0302 | A15 | WHT/GRN |
| 3 | P0303 | A14 | WHT/BLK |
| 4 | P0304 | A13 | WHT/BLU |

Refer to the source image for the connector orientation.

---

### Printed page 11-301

<a id="p597"></a>
Source: [PDF p.597, printed p.11-301](../page-images/p0597.png).

# Step 38
Connect appropriate ignition coil 3P connector terminal No. 1 to body ground with a jumper wire (see table).

| PROBLEM DTC | WIRE COLOR |
| :--- | :--- |
| No. 1 P0301 | WHT |
| No. 2 P0302 | WHT/GRN |
| No. 3 P0303 | WHT/BLK |
| No. 4 P0304 | WHT/BLU |

**IGNITION COIL 3P CONNECTOR**
1 IGPLS JUMPER WIRE Wire side of female terminals

# Step 39
Check for continuity between body ground and the appropriate ECM connector terminal (see table).

| PROBLEM DTC | ECM TERMINAL COLOR |
| :--- | :--- |
| No. 1 P0301 | A16 WHT |
| No. 2 P0302 | A15 WHT/GRN |
| No. 3 P0303 | A14 WHT/BLK |
| No. 4 P0304 | A13 WHT/BLU |

**ECM CONNECTOR A (31P)**
IGPLS4 (WHT/BLU) IGPLS1 (WHT)
1 | 2 | 3 4 | .5 6 | 7 | 8 9
10 / 13 14 15 16 / 18 / 20 21 23 24 25 26 / 28 / 30 31 IGPLS3 ^ (WHT/BLK) . IGPLS2 (WHT/GRN)
Wire side of female terminals

**Is there continuity?**
* **YES** — Go to step 40.
* **NO** — Repair open in the wire between the ECM and the ignition coil, then go to step 63.

# Step 40
Reconnect the ignition coil 3P connector and ECM connector A (31P).

# Step 41
Do an engine compression and a cylinder leakdown test (see page 6-7).

**Did the engine pass both tests?**
* **YES** — Go to step 42.
* **NO** — Repair the engine, then go to step 63.

*(cont'd)*

---

### Printed page 11-302

<a id="p598"></a>
Source: [PDF p.598, printed p.11-302](../page-images/p0598.png).

# Misfire Troubleshooting (continued)

42. Perform the VTEC rocker arm test (p.6-8). **PASS:** Step 72. **FAIL:** Repair as necessary; step 63.
43. Turn ignition OFF.
44. Jump SCS with HDS.
45. Disconnect ECM connector B (24P).
46. Turn ignition ON (II).
47. Check for battery voltage between ground and the ECM terminal for the problem cylinder. **YES:** Step 57. **NO:** Step 48.

| Cylinder | DTC | ECM terminal | Wire |
|---|---|---|---|
| 1 | P0301 | B5 | BRN |
| 2 | P0302 | B4 | RED |
| 3 | P0303 | B3 | BLU |
| 4 | P0304 | B2 | YEL |

48. Turn ignition OFF.
49. Remove the fuel rail cover.
50. Disconnect the injector 2P connector from the problem cylinder.
51. Turn ignition ON (II).
52. Check for battery voltage between injector 2P terminal **1, IGP (YEL/BLK)** and ground. **YES:** Step 53. **NO:** Repair open between injector and PGM-FI main relay 1 (FI MAIN); step 63.
53. Turn ignition OFF.

Refer to the source image for connector orientation.

---

### Printed page 11-303

<a id="p599"></a>
Source: [PDF p.599, printed p.11-303](../page-images/p0599.png).

# Misfire Troubleshooting (continued)

54. Check continuity between body ground and the appropriate ECM connector B terminal (table). **YES:** Repair short between ECM and injector; step 63. **NO:** Step 55.

| Cylinder | DTC | ECM terminal | Wire |
|---|---|---|---|
| 1 | P0301 | B5 | BRN |
| 2 | P0302 | B4 | RED |
| 3 | P0303 | B3 | BLU |
| 4 | P0304 | B2 | YEL |

55. Ground terminal **2** of the appropriate injector 2P connector with a jumper wire. The injector wire colors are BRN for cylinder 1, RED for 2, BLU for 3, and YEL for 4. Refer to the source image for connector orientation.

---

### Printed page 11-304

<a id="p600"></a>
Source: [PDF p.600, printed p.11-304](../page-images/p0600.png).

PGM-FI System
DTC Troubleshooting (cont'd)
56. Check for continuity between body ground and the appropriate ECM connector terminal (see table).
PROBLEM DTC ECM WIRE
CYLINDER TERMINAL COLOR
No. 1 P0301 B5 BRN
No. 2 P0302 B4 RED
No. 3 P0303 B3 BLU
No. 4 P0304 B2 Y E L
ECM C O N N ECT O R B (24P)
INJ3 (BLU) INJ2(RED)
INJ4 (YEL) INJ1 (BRN)
H 2 | 3 | 4 | 5
18
10
19 20
1.3
21
Wire side of female terminals
Is there continuity?
YES— Go to step 57.
NO—Repair open in the wire between the ECM and the injector, then go to step 63.
57. At the injecotor side, measure resistance between injector 2P connector terminals No. 1 and No. 2.
INJECTOR 2P C O N N ECT O R
1 2
IGP
INJ
Terminal side of male terminals
Is there 10- 13 0,?
YES— Go to step 58.
NO—Replace the injector (see page 11-382), then go to step 63.
58. Substitute a known-good injector into the problem cylinder.
59. Reconnect all connectors.
60. Start the engine, and let it idle for 2 minutes.
61. Test-drive the vehicle for several minutes in the range of these recorded freeze data parameters:
• ENGINE S P E E D
• VSS
• R E L T P SENSOR
• CLV (calculated load value)
62. Check the CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE in the DATA LIST for 10 minutes with the HDS.
Does CYL1 MISFIRE, CYL2 MISFIRE, CYL3 MISFIRE, and/or CYL4 MISFIRE show misfire counts?
YES— Go to step 72.
NO—Replace the original injector (see page 11-382), then go to step 63.
11-304

---

### Printed page 11-305

<a id="p601"></a>
Source: [PDF p.601, printed p.11-305](../page-images/p0601.png).

# PGM-FI System — DTC Troubleshooting

63. Reconnect all connectors.

64. Turn the ignition switch ON (II).

65. Reset the ECM with the HDS.

66. Clear the CKP pattern with the HDS.

67. Do the ECM idle learn procedure (see page 11-462).

68. Do the CKP pattern learn procedure (see page 11-214).

69. Test-drive the vehicle for several minutes in the range of these recorded freeze data parameters:

• ENGINE S P E E D

• VSS

• REL TP SENSOR '• CLV (calculated load value)

70. Check for Temporary DTCs or DTCs with the HDS. Is DTC P0301, P0302, P0303, or P0304 indicated?

YES—Check for poor connections or loose terminals at the ignition coil, the injector, and the ECM, then go to DTC P0300, P0301, P0302, P0303, or P0304 troubleshooting (see page 11-295).

NO—Go to step 71.

71. Monitor the OBD STATUS for DTC P0301, P0302, P0303, or P0304 in the DTCs MENU with the HDS. Does the screen indicate FAILED?

YES—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 70, go to the indicated DTCs troubleshooting. •

NO—If the screen indicate FAILED, go to step 1 and recheck. If the screen indicated EXECUTING, keep driving until a result comes on. If the screen indicates OUT OF CONDITION, go to step 69.

72. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

73. Test-drive the vehicle for several minutes in the range of these recorded freeze data parameters:

• ENGINE S P E E D

• VSS

• R E L T P SENSOR

• C L V (calculated load value)

74. Check for Temporary DTCs or DTCs with the HDS. Is DTC P0301, P0302, P0303, or P0304 indicated? YES— Check for poor connections or loose terminals at the injector, the ignition coil, and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 72. If the ECM was substituted, go to step 1. NO— Go to step 75.

75. Monitor the OBD STATUS for DTC P0301, P0302, P0303, or P0304 in the DTCs MENU with the HDS. Does the screen indicate PASSED?

YES—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 74, go to the indicated DTCs troubleshooting. •

NO—If the screen indicates FAILED, check for poor connections or loose terminals at the ignition coil, the injector, and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 73. If the ECM was substituted, go to step 1. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates OUT OF CONDITION, go to step 73.

For connector orientation and terminal positions, refer to the source image.

**Source inconsistency:** Step 71 asks whether OBD STATUS indicates FAILED, yet the printed YES branch says troubleshooting is complete and the NO branch also addresses FAILED. The source image confirms this wording; verify against authoritative service guidance before applying that branch.

---

### Printed page 11-306

<a id="p602"></a>
Source: [PDF p.602, printed p.11-306](../page-images/p0602.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0325: Knock Sensor Circuit Malfunction

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
4. Hold the engine speed between 3,000—4,000 rpm for at least 10 seconds.
5. Check for Temporary DTCs or DTCs with the HDS.
   - Is DTC P0325 indicated?
     - **Y** — Go to step 6.
     - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the knock sensor and the ECM.

6. Turn the ignition switch OFF.
7. Jump the SCS line with the HDS.
8. Disconnect the knock sensor 1P connector.
9. Disconnect ECM connector A (31P).
10. Check for continuity between ECM connector terminal A1 and body ground.

**ECM CONNECTOR A (31P)**
```
K S
(RED/BLU)
1 2 3 4 | 5 6 | 7 | | 8 | 9
10
/ / 13 14 15 16
/ 18
/ 20 21
/ 23 24 25 26
/ 28
/ 30 31
Wire side of female terminals
```

- Is there continuity ?
  - **YES** — Repair short in the wire between the ECM (A1) and the knock sensor, then go to step 14.
  - **NO** — Go to step 11.

11. Connect the knock sensor 1P connector terminal to body ground with a jumper wire.

**KNOCK SENSOR 1P CONNECTOR**
```
1
K S (RED/BLU)
JUMPER wire
Wire side of female terminals
```

*Page reference: 11-306*

---

### Printed page 11-307

<a id="p603"></a>
Source: [PDF p.603, printed p.11-307](../page-images/p0603.png).

# Page 603 Transcription

## Step 12
**Instruction:** Check for continuity between ECM connector terminal A1 and body ground.

**Diagram Data:**
- **Connector Label:** ECM C O N N ECT O R A (31P)
- **Wire Color:** (RED/BLU)
- **Terminal Pins:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 18, 20, 21, 23, 24, 25, 26, 28, 30, 31
- **Note:** Wire side of female terminals

**Decision Logic:**
- **Is there continuity?**
  - **YES:** Go to step 13.
  - **NO:** Repair open in the wire between the ECM (A1) and the knock sensor, then go to step 14.

---

## Step 13
**Instruction:** Replace the knock sensor (see page 11-388).

---

## Step 14
**Instruction:** Reconnect all connectors.

---

## Step 15
**Instruction:** Turn the ignition switch ON (II).

---

## Step 16
**Instruction:** Reset the ECM with the HDS.

---

## Step 17
**Instruction:** Do the ECM idle learn procedure (see page 11-462).

---

## Step 18
**Instruction:** Hold the engine speed between 3,000—4,000 rpm for at least 10 seconds.

---

## Step 19
**Instruction:** Check for Temporary DTCs or DTCs with the HDS.

**Decision Logic:**
- **Is DTC P0325 indicated?**
  - **YES:** Go to step 21.
  - **NO:** Go to step 20.

---

## Step 20
**Instruction:** Monitor the OBD STATUS for DTC P0325 in the DTCs MENU with the HDS.

**Decision Logic:**
- **Does the screen indicate PASSED?**
  - **YES:** Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 19, go to the indicated DTCs troubleshooting.
  - **NO:**
    - If FAILED: Check for poor connections or loose terminals at the knock sensor and the ECM, then go to step 1.
    - If NOT COMPLETED: Go to step 18.

---

## Step 21
**Instruction:** Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

---

## Step 22
**Instruction:** Hold the engine speed between 3,000—4,000 rpm for at least 10 seconds.

---

## Step 23
**Instruction:** Check for Temporary DTCs or DTCs with the HDS.

**Decision Logic:**
- **Is DTC P0325 indicated?**
  - **YES:**
    - Check for poor connections or loose terminals at the knock sensor and the ECM.
    - If the ECM was updated: Substitute a known-good ECM (see page 11-217), then go to step 22.
    - If the ECM was substituted: Go to step 1.
  - **NO:** Go to step 24.

---

## Step 24
**Instruction:** Monitor the OBD STATUS for DTC P0325 in the DTCs MENU with the HDS.

**Decision Logic:**
- **Does the screen indicate PASSED?**
  - **YES:**
    - If the ECM was updated: Troubleshooting is complete.
    - If the ECM was substituted: Replace the original ECM (see page 11-389).
    - If any other Temporary DTCs or DTCs were indicated in step 23, go to the indicated DTCs troubleshooting.
  - **NO:**
    - If FAILED: Check for poor connections or loose terminals at the knock sensor and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 22. If the ECM was substituted, go to step 1.
    - If NOT COMPLETED: Go to step 22.

**Page Reference:** 11-307

---

### Printed page 11-308

<a id="p604"></a>
Source: [PDF p.604, printed p.11-308](../page-images/p0604.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0335: CKP Sensor No Signal

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine.
4. Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0335 indicated?
- **YES** — Go to step 5.
- **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CKP sensor and the ECM .

5. Turn the ignition switch OFF.
6. Disconnect the CKP sensor 3P connector.
7. Turn the ignition switch ON (**II**).
8. Measure voltage between CKP sensor 3P connector terminal No. 3 and body ground.

```
CKP SENSOR 3P C O N N ECT O R
IGP (YEL/BLK)
Wire side of female terminals
```

Is there battery voltage?
- **YES** — Go to step 9.
- **NO** — Repair open in the wire between the CKP sensor and PGM-FI main relay 1 (**FI MAIN**), then go to step 18.

9. Measure voltage between CKP sensor 3P connector terminal No. 1 and body ground.

```
CKP SENSOR 3P C O N N ECT O R
Wire side of female terminals
```

Is there about 5 V?
- **YES** — Go to step 10.
- **NO** — Go to step 11.

10. Measure voltage between CKP sensor 3P connector terminals No. 2 and No. 3.

```
CKP SENSOR 3P C O N N ECT O R
1 2 3
L G IGP (BRN/YEL) (YEL/BLK)
Wire side of female terminals
```

Is there battery voltage?
- **YES** — Go to step 16.
- **NO** — Repair open in the wire between the CKP sensor and G101, then go to step 18.

11-308

---

### Printed page 11-309

<a id="p605"></a>
Source: [PDF p.605, printed p.11-309](../page-images/p0605.png).

# CKP Sensor Troubleshooting

## Step 11
Measure voltage between ECM connector terminal A7 and body ground.

**ECM Connector A (31P)**
| Pin | Wire Color | Description |
|---|---|---|
| 1 | BLU | CKP |
| 2-6 | - | - |
| 8-9 | - | - |
| 10 | - | - |
| 13-16 | - | - |
| 18 | - | - |
| 20-21 | - | - |
| 23-26 | - | - |
| 28 | - | - |
| 30-31 | - | - |

*Wire side of female terminals*

Is there about 5 V?

- **YES**—Repair open in the wire between the ECM (A7) and the CKP sensor, then go to step 18.
- **NO**—Go to step 12.

## Step 12
Turn the ignition switch OFF.

## Step 13
Jump the SCS line with the HDS.

## Step 14
Disconnect ECM connector A (31P).

## Step 15
Check for continuity between ECM connector terminal A7 and body ground.

**ECM Connector A (31P)**
| Pin | Wire Color | Description |
|---|---|---|
| 1 | BLU | CKP |
| 2, 5-6 | - | - |
| 8-9 | - | - |
| 10 | - | - |
| 13-16 | - | - |
| 18 | - | - |
| 20-21 | - | - |
| 23-24, 25-26 | - | - |
| 28 | - | - |
| 30-31 | - | - |

*Wire side of female terminals*

Is there continuity?

- **YES**—Repair short in the wire between the ECM (A7) and the CKP sensor, then go to step 18.
- **NO**—Go to step 25.

## Step 16
Turn the ignition switch OFF.

## Step 17
Replace the CKP sensor (see page 11-387).

## Step 18
Reconnect all connectors.

## Step 19
Turn the ignition switch ON (II).

## Step 20
Reset the ECM with the HDS.

## Step 21
Clear the CKP pattern with the HDS.

## Step 22
Do the ECM idle learn procedure (see page 11-462).

## Step 23
Do the CKP pattern learn procedure (see page 11-214).

## Step 24
Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0335 indicated?

- **YES**—Check for poor connections or loose terminals at the CKP sensor and the ECM, then go to step 1.
- **NO**—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

## Step 25
Reconnect all connectors.

## Step 26
Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

## Step 27
Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0335 indicated?

- **YES**—Check for poor connections or loose terminals at the CKP sensor and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
- **NO**—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

**Page Reference:** 11-309

---

### Printed page 11-310

<a id="p606"></a>
Source: [PDF p.606, printed p.11-310](../page-images/p0606.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0339: CKP Sensor Circuit Intermittent Interruption

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine, and let it idle for 10 seconds.
4. Check the CKP **NOISE** in the DATA LIST with the HDS.
   - Are 0 counts indicated?
     - **YES** — Go to step 7.
     - **NO** — Go to step 5.

5. Test-drive the vehicle for several minutes in the range of these recorded freeze data parameters:
   - **E N G I N E S P E E D**
   - **VSS**

6. Check the CKP **NOISE** in the DATA LIST with the HDS.
   - Are 0 counts indicated ?
     - **YES** — Go to step 7.
     - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CKP sensor and the ECM. •

7. Check for poor or loose connections and terminals at these locations:
   - CKP sensor
   - ECM
   - Engine ground
   - Body ground
   - Are the connections and terminals OK?
     - **YES** — Go to step 8.
     - **NO** — Repair the connectors or terminals, then go to step 11.

8. Remove the cam chain case (see page 6-13), and check the CKP sensor pulse plate for damage.
   - Is the pulse plate damaged?
     - **YES** — Replace the CKP sensor pulse plate (see page 6-19), then goto step 11.
     - **NO** — Go to step 9.

9. Turn the ignition switch OFF.

10. Replace the CKP sensor (see page 11-387).

11. Turn the ignition switch ON (**II**).

12. Reset the **ECM** with the HDS.

13. Clear the CKP pattern with the HDS.

14. Do the **ECM** idle learn procedure (see page 11-462).

15. Do the CKP pattern learn procedure (see page 11-214).

16. Start the engine, and let it idle for 10 seconds.

17. Check for Temporary DTCs or DTCs with the HDS.
    - Is DTC P0339 indicated?
      - **YES** — C h e c k for poor connections or loose terminals at the CKP sensor and the **ECM**, then go to step 1.
      - **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated **DTCs** troubleshooting. •

**11-310**

---

### Printed page 11-311

<a id="p607"></a>
Source: [PDF p.607, printed p.11-311](../page-images/p0607.png).

# DTC P0365: CMP Sensor No Signal

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine.
4. Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0365 indicated?
- **YES** — Go to step 5.
- **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CMP sensor and the ECM.

5. Turn the ignition switch OFF.
6. Disconnect the CMP sensor 3P connector.
7. Turn the ignition switch ON (II).
8. Measure voltage between CMP sensor 3P connector terminal No. 3 and body ground.

```
      C M P SENSOR 3P C O N N ECT O R
          1   2   3
          |   |   |
         IGP (YEL/BLK)
Wire side of female terminals
```

Is there battery voltage?
- **YES** — Go to step 9.
- **NO** — Repair open in the wire between the CMP sensor and PGM-FI main relay 1 (FI MAIN), then go to step 18.

9. Measure voltage between CMP sensor 3P connector terminal No. 1 and body ground.

```
      C M P SENSOR 3P C O N N ECT O R
          1   2   3
          |   |   |
         CMP . (GRN)
Wire side of female terminals
```

Is there about 5 V?
- **YES** — Go to step 10.
- **NO** — Go to step 11.

10. Measure voltage between CMP sensor 3P connector terminals No. 2 and No. 3.

```
      C M P SENSOR 3P C O N N ECT O R
          1   2   3
          |   |   |
         LG (BRN/YEL)
         IGP (YEL/BLK)
Wire side of female terminals
```

Is there battery voltage?
- **YES** — Go to step 16.
- **NO** — Repair open in the wire between the CMP sensor and G101, then go to step 18.

(cont'd)

Page Reference: 11-311

---

### Printed page 11-312

<a id="p608"></a>
Source: [PDF p.608, printed p.11-312](../page-images/p0608.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

**11.** Measure voltage between ECM connector terminal **A6** and body ground.

```
ECM CONNECTOR A (31P)
      | CMP (GRN)
  1 | 2 | 3 4 | 5 6 | 7 | 8 | 9
  10
/ 13 14 15 16
/ 18
/ 20 21
23 24 25 26
/ 28
/ 30 31
X
Wire side of female terminals
```

Is there about **5 V**?

*   **YES**—Repair open in the wire between the ECM (**A6**) and the CMP sensor, then go to step **18**.
*   **NO**—Go to step **12**.

**12.** Turn the ignition switch OFF.

**13.** Jump the **SCS** line with the HDS.

**14.** Disconnect ECM connector **A (31P)**.

**15.** Check for continuity between ECM connector terminal **A6** and body ground.

```
ECM CONNECTOR A (31P)
      | CMP (GRN)
  1 | 2 3 4 5 6 7 | 8 9
  10
/ 13 14 15 16
/ 18
/ 20 21
23 24 25 26
/ 28
/ 30 31
Wire side of female terminals
```

Is there continuity?

*   **YES**—Repair short in the wire between the ECM (**A6**) and the CMP sensor, then go to step **19**.
*   **NO**—Go to step **23**.

**16.** Turn the ignition switch OFF.

**17.** Replace the CMP sensor (see page **11-387**).

**18.** Reconnect all connectors.

**19.** Turn the ignition switch ON (**II**).

**20.** Reset the ECM with the HDS.

**21.** Do the ECM idle learn procedure (see page **11-462**).

**22.** Check for Temporary DTCs or DTCs with the HDS.

Is DTC **P0365** indicated?

*   **YES**—Check for poor connections or loose terminals at the CMP sensor and the ECM, then go to step **1**.
*   **NO**—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

**23.** Reconnect all connectors.

**24.** Update the ECM if it does not have the latest software (see page **11-216**), or substitute a known-good ECM (see page **11-217**).

**25.** Check for Temporary DTCs or DTCs with the HDS.

Is DTC **P0365** indicated?

*   **YES**—Check for poor connections or loose terminals at the CMP sensor and the ECM. If the ECM was updated, substitute a known-good ECM (see page **11-217**), then recheck. If the ECM was substituted, go to step **1**.
*   **NO**—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page **11-389**). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

**Page Reference:** 11-312

---

### Printed page 11-313

<a id="p609"></a>
Source: [PDF p.609, printed p.11-313](../page-images/p0609.png).

# DTC P0369: CMP Sensor Circuit Intermittent

## Interruption

> **NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine, and let it idle for 10 seconds.
4. Check the CMP **NOISE** in the DATA LIST with the HDS.

Are 0 counts indicated?
- **YES** - Go to step 7.
- **NO**—Go to step 5.

5. Test-drive the vehicle for several minutes in the range of these recorded freeze data parameters:
   - **ENGINE S P E E D**
   - **VSS**

6. Check the CMP **NOISE** in the DATA LIST with the HDS.

Are 0 counts indicated?
- **YES** — Go to step 7.
- **NO**—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CMP sensor and the ECM.

7. Check for poor or loose connections and terminals at these locations:
   - CMP sensor
   - ECM
   - Engine ground
   - Body ground

8. Check for damage on the CMP pulse plate (see page 6-34).

Is the plate damaged?
- **YES**—Replace the CMP pulse plate (see page 6-34), then go to step 11.
- **NO**—Go to step 9.

9. Turn the ignition switch OFF.

10. Replace the CMP sensor (see page 11-387).

11. Turn the ignition switch ON (**II**).

12. Reset the **ECM** with the HDS.

13. Do the **ECM** idle learn procedure (see page 11-462).

14. Start the engine, and let it idle for 10 seconds.

15. Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0369 indicated?
- **YES**—Check for poor connections or loose terminals at the CMP sensor and the **ECM**, then go to step 1.
- **NO**—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated **DTCs** troubleshooting.

Are the connections and terminals OK?
- **YES** — Go to step 8.
- **NO**—Reconnect the connectors or terminals, then go to step 11.

**Page Reference:** 11-313

---

### Printed page 11-314

<a id="p610"></a>
Source: [PDF p.610, printed p.11-314](../page-images/p0610.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0563: ECM Power Source Circuit
**Unexpected Voltage**

> **NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Turn the ignition switch OFF.
4. Wait 10 seconds.
5. Turn the ignition switch ON (**II**).
6. Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0563 indicated?
- **YES** — Go to step 7.
- **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the No. 46 A C G S (15 A) fuse in the under-hood fuse/relay box, PGM-FI main relay 1 (**FI MAIN**), and the **ECM**.

7. Turn the ignition switch OFF.
8. Jump the **SCS** line with the HDS.
9. Disconnect **ECM** connector **E** (31P).
10. Measure voltage between ECM connector terminal E7 and body ground.

> **ECM CONNECTOR E (31P)**
> **MR L Y (GRN)**
> 1 | 1 | 2 | 3 | 4 | 5 | y\i | 8 | 9
> / | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21
> 22
> / | 24 | 25
> / | 27 | 28 | 29 | 30
> /
> *Wire side of female terminals*

Is there battery voltage?
- **YES** — Go to step 13.
- **NO** — Go to step 11.

11. Remove PGM-FI main relay 1 (**FI MAIN**) (**A**).

> **Page Reference:** 11-314

---

### Printed page 11-315

<a id="p611"></a>
Source: [PDF p.611, printed p.11-315](../page-images/p0611.png).

# PGM-FI Main Relay Troubleshooting (continued)

12. Check continuity from ECM **E7 MRLY (GRN)** to ground. **YES:** Repair short between ECM E7 and PGM-FI main relay 1 (FI MAIN); step 20. **NO:** Step 19.
13. Reconnect ECM connector E (31P).
14. Check for battery voltage from ECM E7 to ground. **YES:** Step 15. **NO:** Step 27.
15. Disconnect ECM connector A (31P).
16. Check for battery voltage from ground to ECM **A3 IGP1 (YEL/BLK)** and **A2 IGP2 (YEL/BLK)** individually. **YES:** Step 17. **NO:** Step 27.
17. Remove PGM-FI main relay 1 (FI MAIN), marked A in the source diagram.

Refer to the source image for connector orientation and relay location.

---

### Printed page 11-316

<a id="p612"></a>
Source: [PDF p.612, printed p.11-316](../page-images/p0612.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

### Step 18
Measure voltage between body ground and ECM connector terminals A3 and A2 individually.

**ECM Connector A (31P)**
- **IGP2**: (YEL/BLK) | Pin: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 18, 20, 21, 23, 24, 25, 26, 28, 30, 31
- **IGP1**: (YEL/BLK)

*Wire side of female terminals*

**Is there battery voltage?**
- **YES**—Repair short to power in the wire between the ECM (A2, A3) and PGM-FI main relay 1 (FI MAIN), then go to step 20.
- **NO**—Go to step 19.

### Step 19
Test PGM-FI main relay 1 (FI MAIN) (see page 22-48).

**Is PGM-FI main relay 1 (FI MAIN) OK?**
- **YES**—Go to step 27.
- **NO**—Replace the PGM-FI main relay 1 (FI MAIN), then go to step 20.

### Step 20
Reconnect all connectors.

### Step 21
Turn the ignition switch ON (II).

### Step 22
Reset the ECM with the HDS.

### Step 23
Do the ECM idle learn procedure (see page 11-462).

### Step 24
Turn the ignition switch OFF.

### Step 25
Wait 10 seconds.

### Step 26
Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P0563 indicated?**
- **YES**—Check for poor connections or loose terminals at PGM-FI main relay 1 (FI MAIN) and the ECM, then go to step 1.
- **NO**—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

### Step 27
Reconnect all connectors.

### Step 28
Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

### Step 29
Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P0563 indicated?**
- **YES**—Check for poor connections or loose terminals at PGM-FI main relay 1 (FI MAIN) and the ECM, then go to step 1. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
- **NO**—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

**Page Reference**: 11-316

---

### Printed page 11-317

<a id="p613"></a>
Source: [PDF p.613, printed p.11-317](../page-images/p0613.png).

# Page 613: S2000 Fuel and Emissions Part D

## DTC P0600: Serial Communication Link
**Malfunction**

> **NOTE:**
> *   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
> *   This DTC is stored when there is a problem in the serial communication system. Go to the gauge assembly troubleshooting.

## DTC P0602: ECM Programming Error
> **NOTE:**
> *   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
> *   This DTC is indicated when the ECM update is not completed.
> *   Do not turn the ignition switch OFF while updating the ECM. If you turn the ignition switch OFF before completion, the ECM can be damaged.

### Procedure
1.  Do the ECM update procedure (see page 11-216).
2.  Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P0602 indicated?**
*   **YES**—Replace the original ECM (see page 11-389).
*   **NO**—Updating is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

---
**Page Reference:** 11-317

---

### Printed page 11-318

<a id="p614"></a>
Source: [PDF p.614, printed p.11-318](../page-images/p0614.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

### DTC P0603: ECM Internal Control Module Keep Alive Memory (KAM) Error
**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Check for Temporary DTCs or DTCs with the HDS.
   Are any Temporary DTCs or DTCs indicated?
   - **YES** — Go to step 4.
   - **NO** — Intermittent failure, the system is OK at this time.

4. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
5. Check for Temporary DTCs or DTCs with the HDS.
   Is DTC P0603 indicated?
   - **YES** — If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
   - **NO** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

---

### DTC P0606: ECM Processor Malfunction
**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Turn the ignition switch OFF.
4. Turn the ignition switch ON (**II**).
5. Wait 40 seconds.
6. Check for Temporary DTCs or DTCs with the HDS.
   Is DTC P0606 indicated?
   - **YES** — Go to step 7.
   - **NO** — Intermittent failure, the system is OK at this time.

7. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
8. Turn the ignition switch OFF.
9. Turn the ignition switch ON (**II**).
10. Wait 40 seconds.
11. Check for Temporary DTCs or DTCs with the HDS.
    Is DTC P0606 indicated?
    - **YES** — If the ECM was updated/substitute a known-good ECM (see page 11-217), then go to step 8. If the ECM was substituted, go to step 1.
    - **NO** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

**Page Reference:** 11-318

---

### Printed page 11-319

<a id="p615"></a>
Source: [PDF p.615, printed p.11-319](../page-images/p0615.png).

# DTC P0630: VIN Not Programmed or Mismatch

**NOTE:**
*   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   This DTC is stored only when the ECM does not have the VIN information of the vehicle. Use the HDS to input the missing VIN information.

1. Turn the ignition switch ON (II).
2. Check the VIN with the HDS.
   *   Does the HDS show the vehicle's VIN?
       *   **YES** — Go to step 5.
       *   **NO** — Go to step 3.
3. Input the VIN to the ECM with the HDS.
   *   Does the screen show COMPLETE?
       *   **YES** — Go to step 5.
       *   **NO** — Go to step 4.
4. Check for DTCs with the HDS.
   *   Is DTC P0603 indicated?
       *   **YES** — Go to the DTC P0603 troubleshooting.
       *   **NO** — Go to step 9.
5. Clear the DTC with the HDS.
6. Turn the ignition switch OFF.
7. Turn the ignition switch ON (II), and wait 5 seconds.
8. Check for Temporary DTCs or DTCs with the HDS.
   *   Is DTC P0630 indicated?
       *   **YES** — Go to step 9.
       *   **NO** — Intermittent failure, the system is OK at this time. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.
9. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
10. Check for Temporary DTCs or DTCs with the HDS.
    *   **YES** — If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
    *   **NO** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

**Page Reference:** 11-319

---

### Printed page 11-320

<a id="p616"></a>
Source: [PDF p.616, printed p.11-320](../page-images/p0616.png).

# DTC P0685 — ECM Power Control Circuit/Internal Circuit Malfunction

Record freeze data and on-board snapshot; review general troubleshooting (p.11-213). If the problem does not return after clearing the DTC, or is intermittent, check loose terminals at IGP line connectors before replacing the ECM.

1. Turn ignition ON (II).
2. Clear DTC with HDS.
3. Start engine and idle for 30 seconds.
4. Turn ignition OFF.
5. Start engine and idle for 30 seconds.
6. Turn ignition OFF.
7. Turn ignition ON (II).
8. Check DTCs with HDS. **P0685 YES:** Step 9. **NO:** Intermittent failure; system OK now. Address other indicated DTCs.
9. Update ECM software if needed (p.11-216), or substitute a known-good ECM (p.11-217).
10. Start engine and idle for 30 seconds.
11. Turn ignition OFF.
12. Start engine and idle for 30 seconds.
13. Turn ignition OFF.
14. Turn ignition ON (II).
15. Check DTCs. **P0685 YES:** If ECM was updated, substitute known-good ECM, then return to step 10; if substituted, return to step 1. **NO:** If updated, troubleshooting complete; if substituted, replace original ECM (p.11-389). Address any other indicated DTCs.

---

### Printed page 11-321

<a id="p617"></a>
Source: [PDF p.617, printed p.11-321](../page-images/p0617.png).

# DTC P0720: Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
2. Test-drive several miles.
3. Check the C SHAFT SPD in the DATA LIST with the HDS.

Is any vehicle speed indicated?
- **YES** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the ECM . B
- **NO** — Go to step 4.

4. Turn the ignition switch OFF.
5. Disconnect the output shaft (countershaft) speed sensor 3P connector.
6. Turn the ignition switch ON (II).
7. Measure voltage between output shaft (countershaft) speed sensor 3P connector terminal No. 1 and body ground.

> **OUTPUT SHAFT (COUNTERSHAFT) SPEED SENSOR 3P CONNECTOR**
> VCC 2 (YEL/BLU)
> Wire side of female terminals

Is there about 5 V?
- **YES** — Go to step 8.
- **NO** — Repair open in the wire between the ECM (A20) and the output shaft (countershaft) speed sensor, then go to step 17.

8. Measure voltage between output shaft (countershaft) speed sensor 3P connector terminal No. 2 and body ground.

> **OUTPUT SHAFT (COUNTERSHAFT) SPEED SENSOR 3P CONNECTOR**
> 1 2 3
> NC (BLU/WHT)
> Wire side of female terminals

Is there about 5 V?
- **YES** — Go to step 9.
- **NO** — Go to step 10.

(cont'd)

11-321

---

### Printed page 11-322

<a id="p618"></a>
Source: [PDF p.618, printed p.11-322](../page-images/p0618.png).

PGM-FI System DTC Troubleshooting (cont'd)

9. Measure voltage between output shaft (countershaft) speed sensor 3P connector terminals No. 1 and No. 3.

[Diagram: OUTPUT SHAFT (COUNTERSHAFT) SPEED SENSOR 3P CONNECTOR]
- Terminal VCC2 (YEL/BLU): 1.23 kg^-1 SG2
- Wire side of female terminals

Is there about 5 V?
- YES— Go to step 15.
- NO—Repair open in the wire between the ECM (A23) and the output shaft (countershaft) speed sensor, then go to step 17.

10. Measure voltage between ECM connector terminal A18 and body ground.

[Diagram: ECM CONNECTOR A (31P)]
- Pin layout: 1|2|3|4 B6 IT | 8|9 | 10 / 13 14 15 16 / 18 / 20 21 23 24 25 26 / 23 / 30 31 NC
- Terminal A18 (BLU/WHT)
- Wire side of female terminals

Is there about 5 V?
- YES—Repair open in the wire between the ECM (A18) and the output shaft (countershaft) speed sensor, then go to step 17.
- NO—Go to step 11.

11. Turn the ignition switch OFF.

12. Jump the SCS line with the HDS.

13. Disconnect ECM connector A (31P).

[Diagram: ECM CONNECTOR A (31P)]
- Pin layout: 1 3 5 6 I 8 J 9 | 10 / 13 14 15 16 / 18 / 20 21 23 24 25 26 / 23 / 30 31 NC
- Terminal A18 (BLU/WHT)
- Wire side of female terminals

Is there continuity?
- YES—Repair short in the wire between the ECM (A18) and the output shaft (countershaft) speed sensor, then go to step 17.
- NO—Go to step 24.

11-322

---

### Printed page 11-323

<a id="p619"></a>
Source: [PDF p.619, printed p.11-323](../page-images/p0619.png).

# DTC P0720 — Output Shaft Speed Sensor (continued)

15. Turn ignition OFF.
16. Replace the output shaft (countershaft) speed sensor (p.11-388).
17. Reconnect all connectors.
18. Turn ignition ON (II).
19. Reset ECM with HDS.
20. Perform ECM idle learn (p.11-462).
21. Test-drive with ECT sensor 1 above **158 °F (70 °C)**, in **5th gear** at **2,000–3,000 rpm** for several minutes, then decelerate with throttle fully closed for **8 seconds**.
22. Check DTCs with HDS. **P0720 YES:** Check sensor/ECM connections, then step 1. **NO:** Step 23.
23. Monitor OBD STATUS for P0720. **PASSED:** Troubleshooting complete; address any other DTCs from step 22. **FAILED:** Check connections, then step 1. **NOT COMPLETED:** Step 21.
24. Reconnect all connectors.
25. Update ECM software if needed (p.11-216) or substitute a known-good ECM (p.11-217).
26. Repeat the test drive conditions from step 21.
27. Check DTCs with HDS. **P0720 YES:** Check sensor/ECM connections. **NO:** Step 28.

---

### Printed page 11-324

<a id="p620"></a>
Source: [PDF p.620, printed p.11-324](../page-images/p0620.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

### Step 28
Monitor the OBD STATUS for DTC P0720 in the DTCs MENU with the HDS.

**Does the screen indicate PASSED?**

*   **YES**—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 27, go to the indicated DTCs troubleshooting.
*   **NO**—If the screen indicates FAILED, check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the ECM . If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 26. If the ECM was substituted, go to step 1. If the screen indicates NOT COMPLETED, go to step 26.

---

### DTC P1109: BARO Sensor Circuit Out of Range High

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Reset the ECM with the HDS.
3. Start the engine.
4. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P1109 indicated?**

*   **YES**—Go to step 5.
*   **NO**—If intermittent failure, the system is OK at this time. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

**Step 5:** Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

**Step 6:** Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P1109 indicated?**

*   **YES**—If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
*   **NO**—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

**Page Reference:** 11-324

---

### Printed page 11-325

<a id="p621"></a>
Source: [PDF p.621, printed p.11-325](../page-images/p0621.png).

# DTC P1116: ECT Sensor 1 Circuit Range/Performance Problem

**NOTE:**
*   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   If DTC P0111 is stored at the same time as DTC P1116, troubleshoot DTC P0111 first, then recheck for DTC P1116.

**1.** Check for poor connections or loose terminals at ECT sensor 1 and ECT sensor 2.
*   Are the connections and terminals OK?
    *   **YES— Go to step 2.**
    *   **NO—Repair the connectors or terminals, then go to step 27.**

**2.** Turn the ignition switch ON (II).

**3.** Check for Temporary DTCs or DTCs with the HDS.
*   Are DTC P1116 and P2183 indicated at the same time?
    *   **YES— Go to step 15.**
    *   **NO—Go to step 4.**

**4.** Start the engine, and let it idle for 10 minutes.

**5.** Check ECT SENSOR 1 in the DATA LIST with the HDS.
*   Is about 113 °F (45 °C) or less indicated?
    *   **YES—Replace ECT sensor 1 (see page 11-385), then go to step 27.**
    *   **NO—Go to step 6.**

**6.** Turn the ignition switch OFF.

**7.** Drain the coolant (see page 10-9).

**8.** Remove ECT sensor 1 (see page 11-385).

**9.** Allow ECT sensor 1 to cool to ambient temperature.

**10.** Note the ambient temperature.

**11.** Connect ECT sensor 1 to the 2P connector, but do not install sensor on the engine.

**12.** Turn the ignition switch ON (II).

**13.** Note the value of ECT SENSOR 1 quickly in the DATA LIST with the HDS.

**14.** Compare the value of ECT SENSOR 1 and the ambient temperature.
*   Does the value of ECT SENSOR 1 differ 5.4 °F (3 °C) or more?
    *   **YES—Replace ECT sensor 1 (see page 11-385), then go to step 27.**
    *   **NO—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM .**

**15.** Start the engine, and let it idle for 10 minutes.

**16.** Check ECT SENSOR 1 in the DATA LIST with the HDS.
*   Is about 113 °F (45 °C) or less indicated?
    *   **YES—Replace ECT sensor 1 (see page 11-385), then go to step 27.**
    *   **NO—Go to step 17.**

**17.** Let the engine idle for 10 minutes.

**18.** Check ECT SENSOR 2 in the DATA LIST with the HDS.
*   Is about 113 °F (45 °C) or less indicated?
    *   **YES—Replace ECT sensor 2 (see page 11-385), then goto step 27.**
    *   **NO—Go to step 19.**

*(cont'd)*

**Page Reference:** 11-325

---

### Printed page 11-326

<a id="p622"></a>
Source: [PDF p.622, printed p.11-326](../page-images/p0622.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

19. Turn the ignition switch OFF.
20. Drain the coolant (see page 10-9).
21. Remove ECT sensor 1 (see page 11-385) and ECT sensor 2 (see page 11 -385).
22. Allow the sensors to cool to ambient temperature.
23. Note the ambient temperature.
24. Connect ECT sensor 1 to the 2P connector, and ECT sensor 2 to the 2P connector, but do not install them on the engine.
25. Note the value of ECT SENSOR 1 and ECT SENSOR 2 quickly in the DATA LIST with the HDS.
26. Compare the value of ECT SENSOR 1 and the ambient temperature, and the value of ECT SENSOR 2 and the ambient temperature individually.

Does one of the sensors differ more than 5.4 °F (3 °C) from the ambient temperature?

**YES**—Replace the sensor that differed more than 5.4 °F (3 °C) from the ambient temperature, then go to step 27.

**NO**—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM . H

27. Turn the ignition switch ON (II).
28. Reset the ECM with the HDS.
29. Do the ECM idle learn procedure (see page 11-462).
30. Check for Temporary DTCs or DTCs with the HDS.

Is DTC P1116 indicated?

**YES— C h e c k for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM, then go to step 1.**

**NO—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •**

11-326

---

### Printed page 11-327

<a id="p623"></a>
Source: [PDF p.623, printed p.11-327](../page-images/p0623.png).

# DTC P1128: MAP Sensor Signal Lower Than Expected

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Inspect the air cleaner element (see page 11-505).
   Is there damage or clogging?
   - **YES**—Replace the air cleaner element (see page 11-505). Then clear the DTC with the HDS, and go to step 13.
   - **NO**—Go to step 2.

2. Turn the ignition switch ON (**II**).

3. Check the MAP SENSOR in the DATA LIST with the HDS.
   Is less than 54.1 kPa (16.0 in.Hg, 406 mmHg), or 1.61 V held for more than 5 seconds?
   - **YES**—Go to step 8.
   - **NO**—Go to step 4.

4. Clear the DTC with the HDS.

5. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

6. Test-drive under these conditions:
   - Engine coolant temperature (**ECT SENSOR 1**) above 158°F (70 °C)
   - Transmission in 3rd gear
   - Vehicle speed at 15 mph (24 km/h) or more, and engine speed between 1,300 rpm and 7,600 rpm for 2 seconds or more.

7. Monitor the **OBD STATUS** for DTC P1128 in the DTCs MENU with the HDS.
   Does the screen indicate **FAILED**?
   - **YES**—Go to step 8.
   - **NO**—If the screen indicates **PASSED**, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the ECM. If the screen indicates **NOT COMPLETED**, go to step 5 and recheck.

8. Turn the ignition switch OFF.

9. Replace the MAP sensor (see page 11-384).

10. Turn the ignition switch ON (**II**).

11. Reset the **ECM** with the HDS.

12. Do the **ECM** idle learn procedure (see page 11-462).

13. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

14. Test-drive under these conditions:
    - Engine coolant temperature (**ECT SENSOR 1**) above 158°F (70 °C)
    - Transmission in 3rd gear
    - Vehicle speed at 15 mph (24 km/h) or more, and engine speed between 1,300 rpm and 7,600 rpm for 2 seconds or more.

15. Check for Temporary DTCs or DTCs with the HDS.
    Is **DTC P1128** indicated?
    - **YES**—Check for poor connections or loose terminals at the MAP sensor and the ECM, then go to step 1.
    - **NO**—Go to step 16.

16. Monitor the **OBD STATUS** for DTC P1128 in the DTCs MENU with the HDS.
    Does the screen indicate **PASSED**?
    - **YES**—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 15, go to the indicated **DTCs** troubleshooting.
    - **NO**—If the screen indicates **FAILED**, check for poor connections or loose terminals at the MAP sensor and the **ECM**, then go to step 1. If the screen indicates **NOT COMPLETED**, go to step 14.

**Page Reference:** 11-327

---

### Printed page 11-328

<a id="p624"></a>
Source: [PDF p.624, printed p.11-328](../page-images/p0624.png).

# PGM-FI System — DTC Troubleshooting

DTC P1129: MAP SensorSignal Higher Than Expected

NOTE: Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Check for vacuum leaks in these parts.

• PCV valve

• PCV hose

• EVAP canister purge valve

• Throttle body

• Brake booster hose

• Intake manifold Are there any vacuum leaks?

YES—Repair or replace parts with vacuum leaks, then go to step 9. NO— Go to step 2.

2. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

3. Check the MAP SENSOR in the DATA LIST with the HDS. Is more than 36.9 kPa (11.0 in.Hg, 277 mmHg), or 1.1 V held for more than for 5 seconds? YES— Go to step 7.

NO—Go to step 4.

4. Clear the DTC with the HDS.

5. Test-drive under these conditions:

• Engine coolant temperature (ECT SENSOR 1) above 158 T ( 7 0 * 0

• Transmission in 5th gear

• Vehicle speed between 55—75 mph (88— 121 km/h) for 10 seconds

• Vehicle speed decelerated with throttle fully closed for at least 2 secondsfor more

6. Monitor the OBD STATUS for DTC P1129 in the DTCs MENU with the HDS. Does the screen indicate FAILED? YES— Go to step 7.

NO—If the screen indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the ECM . If the screen indicates NOT COMPLETED, go to step 5 and recheck.

7. Turn the ignition switch OFF.

8. Replace the MAP sensor (see page 11-384).

9. Turn the ignition switch ON (II).

10. Reset the ECM with the HDS.

11. Do the ECM idle learn procedure (see page 11-462).

12. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

13. Test-drive under these conditions:

• Engine coolant temperature (ECT SENSOR 1) above 158 °F (70°C)

• Transmission in 5th gear

• Vehicle speed between 55—75 mph (88— 121 km/h) for 10 seconds

• Vehicle speed decelerated with throttle fully closed for at least 2 secondsfor more

14. Check for Temporary DTCs or DTCs with the HDS. Is DTC P1129 indicated?

YES—Check for poor connections or loose terminals at the MAP sensor and the ECM , then go to step 1.

NO—Go to step 15.

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-329

<a id="p625"></a>
Source: [PDF p.625, printed p.11-329](../page-images/p0625.png).

# PGM-FI System — DTC Troubleshooting

15. Monitor the OBD STATUS for DTC P1129 in the DTCs MENU with the HDS. Does the screen indicate PASSED?

YES—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 14, go to the indicated DTCs troubleshooting. •

NO—If the screen indicates FAILED, check for poor connections or loose terminals at the MAP sensor and the ECM , then go to step 1. If the screen indicates NOT COMPLETED, go to step 13.

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-330

<a id="p626"></a>
Source: [PDF p.626, printed p.11-330](../page-images/p0626.png).

# PGM-FI System — DTC Troubleshooting

DTC P1157:A/F Sensor (Sensor 1) AFS Circuit High Voltage

NOTE: Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).

2. Clear the DTC with the HDS.

3. Start the engine, and wait 20 seconds.

4. Check for Temporary DTCs or DTCs with the HDS. Is DTC P1157 indicated? YES— Go to step 5.

NO—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM. •

5. Turn the ignition switch OFF.

6. Jump the SCS line with the HDS.

7. Disconnectthe A/F sensor (Sensor 1) 4P connector.

8. Disconnect ECM connector A (31P).

9. Connect A/F sensor (Sensor 1) 4P connector terminal No. 1 to body ground with a jumper wire. A / F SENSOR ( SENSOR 1) 4P C O N N ECT O R A F S + (RED) 1 2 3 4 JUMPER wire

10. Check for continuity between ECM connector terminal A31 and body ground. ECM C O N N ECT O R A (31P) 1 | 2 | 3 | 4 | 5 6 | 7 | | 8 | 9 10 / / 13 14 15 16 / 18 / 20 21 / 23 24 25 26 / 28 / 30 31 A F S + (RED) Wire side of female terminals Is there continuity? YES— Go to step 11.

NO—Repair open in the wire between the ECM (A31) and the A/F sensor (Sensor 1), then go to step 15.

11. Remove the jumper wire from the A/F sensor (Sensor 1) 4P connector.

12. Connect A/F sensor (Sensor 1) 4P connector terminal No. 2 to body ground with a jumper wire. A / F SENSOR ( SENSOR 1) 4P C O N N ECT O R A F S - (RED/YEL) 1 2 3 4 J U M P E R WIRE Wire side of female terminals Wire side of female terminals

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-331

<a id="p627"></a>
Source: [PDF p.627, printed p.11-331](../page-images/p0627.png).

# PGM-FI System — DTC Troubleshooting

13. Check for continuity between ECM connector terminal A28 and body ground. [Connector view in source image.] Is there continuity ? YES— Go to step 14.

NO—Repair open in the wire between the ECM (A28) and the A/F sensor (Sensor 1), then go to step 15.

14. Replace the A/F sensor (Sensor 1) (see page 11-386).

15. Reconnect all connectors.

16. Turn the ignition switch ON (II).

17. Reset the ECM with the HDS.

18. Do the ECM idle learn procedure (see page 11-462).

19. Check for Temporary DTCs or DTCs with the HDS. Is DTC P1157 indicated?

YES—Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1. If the connector and terminal fits are OK, go to step 21.

NO—Go to step 20.

20. Monitor the OBD STATUS for DTC P1157 in the DTCs MENU with the HDS. Does the screen indicate PASSED?

YES—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 19, go to the indicated DTCs troubleshooting. •

NO—If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

21. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

22. Start the engine, and let it idle.

23. Check for Temporary DTCs or DTCs with the HDS. Is DTC P1157 indicated?

YES—If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 22. If the ECM was substituted, go to step 1. NO— Go to step 24.

Circuit labels: ECM A28 AFS− (RED/YEL). Refer to the source image for connector orientation.

---

### Printed page 11-332

<a id="p628"></a>
Source: [PDF p.628, printed p.11-332](../page-images/p0628.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

**24.** Monitor the OBD **S T A T U S** for DTC **P1157** in the **DTCs M E N U** with the **HDS**.

Does the screen indicate **PASSED**?

*   **YES** — If the **ECM** was updated, troubleshooting is complete. If the **ECM** was substituted, replace the original **ECM** (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 23, go to the indicated **DTCs** troubleshooting.
*   **NO** — If the screen indicates **FAILED**, go to step 1. If the **ECM** was updated, substitute a known-good **ECM** (see page 11-217), then go to step 22. If the **ECM** was substituted, go to step 1. If the screen indicates **NOT COMPLETED**, keep idling until a result comes on.

**11-332**

---

### Printed page 11-333

<a id="p629"></a>
Source: [PDF p.629, printed p.11-333](../page-images/p0629.png).

# DTC P1172: A/F Sensor (Sensor 1) Circuit Out of Range High

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at **3,000 rpm** without load (in neutral) until the radiator fan comes on, then let it idle.
4. Monitor the OBD **S T A T U S** for DTC P1172 in the DTCs MENU with the HDS.

Does the screen indicate FAILED?
- **YES** — Go to step 5.
- **NO** — If the screen indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM . If the screen indicates EXECUTING, keep idling until a result comes on. If the screen indicates O U T OF CONDITION, go to step 3 and recheck.

5. Turn the ignition switch OFF.
6. Replace the A/F sensor (Sensor 1) (see page **11-386**).
7. Turn the ignition switch ON (**II**).
8. Reset the ECM with the HDS.
9. Do the ECM idle learn procedure (see page **11-462**).
10. Start the engine. Hold the engine speed at **3,000 rpm** without load (in neutral) until the radiator fan comes on, then let it idle.
11. Check for Temporary DTCs or DTCs with the HDS.

Is DTC P1172 indicated?
- **YES** — Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1.
- **NO** — Go to step 12.

12. Monitor the OBD **S T A T U S** for DTC P1172 in the DTCs MENU with the HDS.

Does the screen indicate PASSED?
- **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 11, go to the indicated DTCs troubleshooting.
- **NO** — If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1. If the screen indicates EXECUTING, keep idling until a result comes on. If the screen indicates O U T OF CONDITION, go to step 10.

**Page Reference:** 11-333

---

### Printed page 11-334

<a id="p630"></a>
Source: [PDF p.630, printed p.11-334](../page-images/p0630.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P1297: ELD Circuit Low Voltage

**NOTE:** Before you troubleshoot record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Check the ELD in the DATA LIST with the HDS.
   Is **72 A** or more indicated?
   - **YES** — Go to step 3.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the ELD and the ECM. •

3. Turn the ignition switch OFF.
4. Disconnect the ELD 3P connector.
5. Turn the ignition switch ON (**II**).
6. Check the ELD in the DATA LIST with the HDS.
   Is **72 A** or more indicated?
   - **YES** — Go to step 7.
   - **NO** — Go to step 11.

7. Turn the ignition switch OFF.
8. Jump the **SCS** line with the HDS.
9. Disconnect **ECM** connector **E (31P)**.
10. Check for continuity between ECM connector terminal **E15** and body ground.

    > **ECM CONNECTOR E (31P)**
    > ~7_1 8 9
    > / 11 12 13 14 15 16 17 18 19 20 21
    > 22
    > / 24 25 / 27 28 29 30
    > / **E L D**
    > (GRN/RED)
    > Wire side of female terminals

    Is there continuity?
    - **YES** — Repair short in the wire between the ECM (**E15**) and the ELD, then go to step-13.
    - **NO** — Go to step 20.

11. Turn the ignition switch OFF.
12. Replace the under-hood fuse/relay box.
13. Reconnect all connectors.
14. Turn the ignition switch ON (**II**).
15. Reset the **ECM** with the HDS.
16. Do the **ECM** idle learn procedure (see page 11-462).
17. Start the engine.
18. Turn on the headlights.
19. Check for Temporary DTCs or DTCs with the HDS.
    Is DTC **P1297** indicated?
    - **YES** — C h e c k for poor connections or loose terminals at the ELD and the **ECM**, then go to step 1.
    - **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated **DTCs** troubleshooting. •

**Page Reference:** 11-334

---

### Printed page 11-335

<a id="p631"></a>
Source: [PDF p.631, printed p.11-335](../page-images/p0631.png).

# PGM-FI System — DTC Troubleshooting

20. Reconnect all connectors.

21. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

22. Start the engine.

23. Turn on the headlights.

24. Check for Temporary DTCs or DTCs with the HDS. Is DTC P1297 indicated?

YES—Check for poor connections or loose terminals at the ELD and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 22. If the ECM was substituted, go to step 1.

NO—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-336

<a id="p632"></a>
Source: [PDF p.632, printed p.11-336](../page-images/p0632.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P1298: ELD Circuit High Voltage

**NOTE:** Before you troubleshoot record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Start the engine, and let it idle.
2. Check the ELD in the DATA LIST with the HDS.
   Is 0.2 A or less indicated?
   - **YES** — Go to step 3.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the ELD and the ECM.

3. Turn the ignition switch OFF.
4. Disconnect the ELD 3P connector.
5. Turn the ignition switch ON (II).
6. Measure voltage between ELD 3P connector terminal No. 1 and body ground.

   **ELD 3P CONNECTOR**
   - Wire side of female terminals
   - IG1 (BLK/YEL)

   Is there battery voltage?
   - **YES** — Go to step 7.
   - **NO** — Check the No. 6 ACG (15 A) fuse in the main under-dash fuse/relay box. If the fuse is OK, repair open in the wire between the No. 6 ACG (15 A) fuse and the ELD, then go to step 14.

7. Turn the ignition switch OFF.
8. Connect ELD 3P connector terminal No. 3 to body ground with a jumper wire.

   **ELD 3P CONNECTOR**
   - Wire side of female terminals
   - ELD (GRN/RED)
   - JUMPER WIRE

9. Jump the SCS line with the HDS.
10. Disconnect ECM connector E (31P).

    **ECM CONNECTOR E (31P)**
    - Wire side of female terminals
    - Pins: 1, 3, 4, 5, X, 7, 8, 9, /, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, /, 24, 25, /, /, 27, 28, 29, 30, /
    - ELD (GRN/RED)

11. Check for continuity between ECM connector terminal E15 and body ground.

    Is there continuity?
    - **YES** — Go to step 12.
    - **NO** — Repair open in the wire between the ECM (E15) and the ELD, then go to step 14.

*Page Reference: 11-336*

---

### Printed page 11-337

<a id="p633"></a>
Source: [PDF p.633, printed p.11-337](../page-images/p0633.png).

Step 12: Check for continuity between ELD 3P connector terminal No. 2 and body ground. [Diagram: ELD 3P Connector Ground (BLK) Wire side of female terminals]. Decision: Is there continuity? YES— Go to step 13. NO— Repair open in the wire between the ELD and G201, then go to step 14.

Step 13: Replace the under-hood fuse/relay box.
Step 14: Reconnect all connectors.
Step 15: Turn the ignition switch ON (II).
Step 16: Reset the ECM with the HDS.
Step 17: Do the ECM idle learn procedure (see page 11-462).
Step 18: Check for Temporary DTCs or DTCs with the HDS. Is DTC P1298 indicated? YES— Go to step 19. NO— Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

Step 19: Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
Step 20: Check for Temporary DTCs or DTCs with the HDS. Is DTC P1298 indicated? YES— Check for poor connections or loose terminals at the ELD and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1. NO— If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

Page Reference: 11-337

---

### Printed page 11-338

<a id="p634"></a>
Source: [PDF p.634, printed p.11-338](../page-images/p0634.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P2183: ECT Sensor 2 Circuit Range/Performance Problem

**NOTE:**
*   Before you troubleshoot, record all freeze data and any onboard snapshot, and review the general troubleshooting information (see page 11-213).
*   If DTC P0111 is stored at the same time as DTC P2183, troubleshoot DTC P0111 first, then recheck for DTC P2183.

1.  Check for poor connections or loose terminals at ECT sensor 1 and ECT sensor 2.
    *   Are the connections and terminals OK?
        *   **YES** — Go to step 2.
        *   **NO** — Repair the connectors or terminals, then go to step 27.

2.  Turn the ignition switch ON (II).

3.  Check for Temporary DTCs or DTCs with the HDS.
    *   Are DTC P1116 and P2183 indicated at the same time?
        *   **YES** — Go to step 15.
        *   **NO** — Go to step 4.

4.  Start the engine, and let it idle for 10 minutes.

5.  Check ECT SENSOR 2 in the DATA LIST with the HDS.
    *   Is about 129 °F (54 °C) or less indicated?
        *   **YES** — Replace ECT sensor 2 (see page 11-385), then go to step 27.
        *   **NO** — Go to step 6.

6.  Turn the ignition switch OFF.

7.  Drain the coolant (see page 10-9).

8.  Remove ECT sensor 2 (see page 11-385).

9.  Allow ECT sensor 2 to cool to ambient temperature.

10. Note the ambient temperature.

11. Connect ECT sensor 2 to the 2P connector, but do not install it on the engine.

12. Turn the ignition switch ON (II).

13. Note the value of ECT SENSOR 2 quickly in the DATA LIST with the HDS.

14. Compare the value of ECT SENSOR 2 and the ambient temperature.
    *   Does ECT SENSOR 2 differ 5.4 °F (3 °C) or more?
        *   **YES** — Replace ECT sensor 2 (see page 11-385), then go to step 27.
        *   **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM . B

15. Start the engine, and let it idle for 10 minutes.

16. Check ECT SENSOR 1 in the DATA LIST with the HDS.
    *   Is about 129 °F (54 °C) or less indicated?
        *   **YES** — Replace ECT sensor 1 (see page 11-385), then go to step 27.
        *   **NO** — Go to step 17.

17. Let the engine idle for 10 minutes.

18. Check ECT SENSOR 2 in the DATA LIST with the HDS.
    *   Is about 129 °F (54 °C) or less indicated?
        *   **YES** — Replace ECT sensor 2 (see page 11-385), then go to step 27.
        *   **NO** — Go to step 19.

*Page reference: 11-338*

---

### Printed page 11-339

<a id="p635"></a>
Source: [PDF p.635, printed p.11-339](../page-images/p0635.png).

# PGM-FI System — DTC Troubleshooting

19. Turn the ignition switch OFF.

20. Drain the coolant (see page 10-9).

21. Remove ECT sensor 1 (see page 11-385) and ECT sensor 2 (see page 11-385).

22. Allow the sensors to cool to ambient temperature.

23. Note the ambient temperature.

24. Connect ECT sensor 1 to 2P connector, and ECT sensor 2 to the 2P connector, but do not install them into the engine.

25. Note the value of ECTSENSOR 1 and ECT SENSOR 2 quickly in the DATA LIST with the HDS.

26. Compare the value of ECT SENSOR 1 and the ambient temperature, and the value of ECT SENSOR 2 and the ambient temperature individually. Does one of the sensors differ more than 5.4 °F (3 °C) from the ambient temperature?

YES—Replace the sensor that differed more than 5.4 °F (3 °C) from the ambient temperature, then go to step 27.

NO—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM . B

27. Turn the ignition switch ON (II).

28. Reset the ECM with the HDS.

29. Do the ECM idle learn procedure (see page 11-462).

30. Check for Temporary DTCs or DTCs with the HDS. Is DTC P2183 indicated? YES— Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the ECM, then go to step 1.

NO—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. B

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-340

<a id="p636"></a>
Source: [PDF p.636, printed p.11-340](../page-images/p0636.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P2184: ECT Sensor 2 Circuit Low Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Check **ECT SENSOR 2** in the DATA LIST with the HDS.
   Is about 356 °F (180 °C) or more, or 0.08 V or less indicated?
   - **YES** — Go to step 3.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at **ECT sensor 2** and the **ECM**. B

3. Turn the ignition switch OFF.
4. Disconnect the **ECT sensor 2** 2P connector.
5. Turn the ignition switch ON (**II**).
6. Check **ECT SENSOR 2** in the DATA LIST with the HDS.
   Is about 356 °F (180 °C) or more, or 0.08 V or less indicated?
   - **YES** — Go to step 7.
   - **NO** — Go to step 11.

7. Turn the ignition switch OFF.
8. Jump the **SCS** line with the HDS.
9. Disconnect **ECM** connector **E** (31P).
10. Check for continuity between **ECT sensor 2** 2P connector terminal No. 1 and body ground.

    > **ECT SENSOR 2 2P C O N N ECT O R**
    > **ECT 2**
    > **J B L U )**
    > Wire side of female terminals

    Is there continuity?
    - **YES** — Repair short in the wire between **ECT sensor 2** and the **ECM** (El), then goto step 13.
    - **NO** — Go to step 18.

11. Turn the ignition switch OFF.
12. Replace **ECT sensor 2** (see page 11-385).
13. Reconnect all connectors.
14. Turn the ignition switch ON (**II**).
15. Reset the ECM with the HDS.
16. Do the ECM idle learn procedure (see page 11-462).

---
**Page Reference:** 11-340

---

### Printed page 11-341

<a id="p637"></a>
Source: [PDF p.637, printed p.11-341](../page-images/p0637.png).

# PGM-FI System — DTC Troubleshooting

17. Check for Temporary DTCs or DTCs with the HDS. Is DTC P2184 indicated?

YES—Check for poor connections or loose terminals at ECT sensor 2 and the ECM , then go to step 1.

NO—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •

18. Reconnect all connectors.

19. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

20. Check for Temporary DTCs or DTCs with the HDS. Is DTC P2184 indicated?

YES—Check for poor connections or loose terminals at ECT sensor 2 and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.

NO—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-342

<a id="p638"></a>
Source: [PDF p.638, printed p.11-342](../page-images/p0638.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P2185: ECT Sensor 2 Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Check **ECT SENSOR 2** in the DATA LIST with the HDS.
   Is about -40°F (-40 °C) or less, or 4.92 V or more indicated?
   * **YES** — Go to step 3.
   * **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at **ECT sensor 2** and the **ECM**.

3. Turn the ignition switch OFF.
4. Disconnect the **ECT sensor 2 2 P connector**.
5. Connect **E** and No. **2**
6. Turn the ignition switch ON (**II**).
7. Check **ECT SENSOR 2** in the DATA LIST with the HDS.
   Is about -40°F(-40 °C) or less, or 4.92 V or more indicated?
   * **YES** — Go to step 8.
   * **NO** — Go to step 18.

8. Turn the ignition switch OFF.
9. Remove the jumper wire from **ECT sensor 2 2 P connector**.
10. Turn the ignition switch ON (**II**).
11. Measure voltage between **ECT sensor 2 2 P connector terminal No. 1** and body ground.

> **ECT SENSOR 2 2P CONNECTOR**
>
> **ECT sensor 2 2 P connector terminals No. 1** with a jumper wire.
>
> ```
> l 1 [ 2
> ECT2 (BLU)
> S G 3 (GRN)
> JUMPER wire
> Wire side of female terminals
> Viz]
> ECT2 (BLU)
> Wire side of female terminals
> ```

Is there about 5 V?
* **YES** — Go to step 12.
* **NO** — Go to step 17.

**ECT SENSOR 2 2P C O N N ECT O R**

Page: 11-342

---

### Printed page 11-343

<a id="p639"></a>
Source: [PDF p.639, printed p.11-343](../page-images/p0639.png).

# PGM-FI System — DTC Troubleshooting

12. Turn the ignition switch OFF.

13. Jump the SCS line with the HDS.

14. Disconnect ECM connector E (31P).

15. Connect ECT sensor 2 2P connector terminal No. 2 to body ground with a jumper wire. [Connector view in source image.]

16. Check for continuity between ECM connector terminal E4 and body ground. [Connector view in source image.] Is there continuity? YES— Go to step 26.

NO—Repair open in the wire between the ECM (E4) and ECT sensor 2, then go to step 20.

17. Measure voltage between ECM connector terminal E1 and body ground. [Connector view in source image.] Is there about 5 V?

YES—Repair open in the wire between the ECM (E1) and ECT sensor 2, then go to step 20.

NO—Go to step 25.

18. Turn the ignition switch OFF.

19. Replace ECT sensor 2 (see page 11-385).

20. Reconnect all connectors.

21. Turn the ignition switch ON (II).

22. Reset the ECM with the HDS.

23. Do the ECM idle learn procedure (see page 11-462).

Circuit labels: ECT sensor 2 terminal 2 SG3 (GRN) to ECM E4; ECT2 (BLU) to ECM E1. Refer to the source image for connector orientation.

---

### Printed page 11-344

<a id="p640"></a>
Source: [PDF p.640, printed p.11-344](../page-images/p0640.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

**24.** Check for Temporary DTCs or DTCs with the HDS.

Is **DTC P2185** Indicated?

*   **YES** — Check for poor connections or loose terminals at ECM sensor 2 and the ECM, then go to step 1.
*   **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTC troubleshooting.

**25.** Turn the ignition switch OFF.

**26.** Reconnect all connectors.

**27.** Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

**28.** Check for Temporary DTCs or DTCs with the HDS.

Is **DTC P2185** indicated?

*   **YES** — Check for poor connections or loose terminals at ECM sensor 2 and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
*   **NO** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTC troubleshooting.

•

11-344

---

### Printed page 11-345

<a id="p641"></a>
Source: [PDF p.641, printed p.11-345](../page-images/p0641.png).

# DTC P2195: A/F Sensor (Sensor 1) Signal Stuck Lean

**NOTE:**
*   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   If the vehicle was out of fuel and the engine stalled before this DTC was stored, refuel, then clear the DTC with the HDS.
*   If DTC P2101, P2118, P2135, P2138, P2176, or a combination of P2122 and P2127, P2122 and P2138, or P2127 and P2138 is stored at the same time, troubleshoot them first, then recheck for DTC P2195.

1.  Check the installation of the A/F sensor (Sensor 1). Is the A/F sensor loose or disconnected from the exhaust pipe?
    *   **YES** — Go to step 6.
    *   **NO** — Go to step 2.

2.  Turn the ignition switch ON (II).
3.  Clear the DTC with the HDS.
4.  Start the engine, then let it idle.
5.  Check for Temporary DTCs or DTCs with the HDS. Are any Temporary DTCs or DTCs indicated?
    *   **YES** — If DTC P2195 is indicated, check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM, then go to step 13. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.
    *   **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM.

6.  Turn the ignition switch OFF.
7.  Reinstall the A/F sensor (Sensor 1) (see page 11-386).
8.  Turn the ignition switch ON (II).
9.  Reset the ECM with the HDS.
10. Do the ECM idle learn procedure (see page 11-462).
11. Check for Temporary DTCs or DTCs with the HDS. Is DTC P2195 indicated?
    *   **YES** — Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM, then go to step 1.
    *   **NO** — Go to step 12.

12. Monitor the OBD STATUS for DTC P2195 in the DTCs MENU with the HDS. Does the screen indicate PASSED?
    *   **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 11, go to the indicated DTCs troubleshooting.
    *   **NO** — If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM, then go to step 1. If the screen indicated NOT COMPLETED, keep idling until a result comes on.

(cont'd)

**Page Reference:** 11-345

---

### Printed page 11-346

<a id="p642"></a>
Source: [PDF p.642, printed p.11-346](../page-images/p0642.png).

PGM-FI System DTC Troubleshooting (cont'd)

13. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

14. Start the engine, then let it idle.

15. Check for Temporary DTCs or DTCs with the HDS.
Is DTC P2195 indicated?
YES— C h e c k for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM . If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 14. If the ECM was substituted, go to step 1.
NO— Go to step 16.

16. Monitor the OBD STATUS for DTC P2195 in the DTCs MENU with the HDS.
Does the screen indicate PASSED?
YES—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 15, go to the indicated DTCs troubleshooting.
NO—If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM . If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 14. If the ECM was substituted, go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

Page Reference: 11-346

---

### Printed page 11-347

<a id="p643"></a>
Source: [PDF p.643, printed p.11-347](../page-images/p0643.png).

# DTC P2227: BARO Sensor Circuit Range/Performance Problem

**NOTE:**
*   Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
*   If DTC P0107, P0108, P1128, and/or P1129 are stored at the same time as DTC P2227, troubleshoot those DTCs first, then recheck for DTC P2227.

**1.** Inspect the air cleaner element (see page 11-505).
Is there damage or clogging?
*   **YES**—Replace the air cleaner element (see page 11-505). Clear the DTC with the HDS, then go to step 9.
*   **NO**—Go to step 2.

**2.** Turn the ignition switch ON (**II**), and wait 2 seconds.

**3.** Check the BARO SENSOR in the DATA LIST with the HDS.
Is about 101 kPa (29.9 in.Hg, 760 mmHg), or about 2.9 V at sea level indicated?
*   **YES**—Go to step 4.
*   **NO**—Go to step 8.

**4.** Clear the DTC with the HDS.

**5.** Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

**6.** Test-drive under these conditions, then connect the HDS.

**7.** Monitor the OBD **S T A T U S** for DTC P2227 in the DTCs MENU with the HDS.
Does the screen indicate FAILED?
*   **YES**—Go to step 8.
*   **NO**—If the screen indicates PASSED, intermittent failure, the system is OK at this time. If the screen indicates NOT COMPLETED, go to step 5 and recheck.

**8.** Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

**9.** Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

**10.** Test-drive under these conditions:
*   Engine coolant temperature (**ECT SENSOR 1**) above 158 °F (70 °C)
*   Transmission in 4th gear
*   **REL TP SENSOR** between 11 deg and 23 deg for 3 seconds or more

**11.** Check for Temporary DTCs or DTCs with the HDS.
Is DTC P2227 indicated?
*   **YES**—Check for poor connections or loose terminals at the ECM, then go to step 1. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
*   **NO**—Go to step 12.

• Engine coolant temperature (**ECT SENSOR 1**) above 158 °F (70 °C)
• Transmission in 4th gear
• **REL TP SENSOR A** between 11 deg and 23 deg for 3 seconds or more

*(cont'd)*

**Page Reference:** 11-347

---

### Printed page 11-348

<a id="p644"></a>
Source: [PDF p.644, printed p.11-348](../page-images/p0644.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

**12.** Monitor the **OBD STATUS** for **DTC P2227** in the **DTCs MENU** with the **HDS**.

Does the screen indicate **PASSED**?

*   **YES**—If the **ECM** was updated, troubleshooting is complete. If the **ECM** was substituted, replace the original **ECM** (see page 11-389). If any other **Temporary DTCs** or **DTCs** were indicated in step 11, go to the indicated **DTCs** troubleshooting.
*   **NO**—If the screen indicates **FAILED**, check for poor connections or loose terminals at the **ECM**. If the **ECM** was updated, substitute a known-good **ECM** (see page 11-217), then go to step 10. If the **ECM** was substituted, go to step 1. If the screen indicates **NOT COMPLETED**, go to step 10.

**Page Reference:** 11-348

---

### Printed page 11-349

<a id="p645"></a>
Source: [PDF p.645, printed p.11-349](../page-images/p0645.png).

# S2000 Fuel and Emissions Part D
## Page 645

### DTC P2228: BARO Sensor Circuit Low Voltage

**NOTE:** Before you troubleshoot record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Check the BARO SENSOR in the DATA LIST with the HDS.
   Is about 53 kPa (15.6 in.Hg, 397 mmHg), or 1.58 V or less indicated?
   - **YES** — Go to step 3.
   - **NO** — Intermittent failure, the system is OK at this time.

3. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
4. Check for Temporary DTCs or DTCs with the HDS.
   Is DTC P2228 indicated?
   - **YES** — C h e c k for poor connections or loose terminals at the ECM . If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
   - **NO** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

---

### DTC P2229: BARO Sensor Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Check the BARO SENSOR in the DATA LIST with the HDS.
   Is about 160 kPa (47.2 in.Hg, 1,200 mmHg), or 4.49 V or more indicated?
   - **YES** — Go to step 3.
   - **NO** — I ntermitte nt fai Iure, the system is OK at th is time.

3. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
4. Check for Temporary DTCs or DTCs with the HDS.
   Is DTC P2229 indicated?
   - **YES** — C h e c k for poor connections or loose terminals at the ECM . If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
   - **NO** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

**Page Reference:** 11-349

---

### Printed page 11-350

<a id="p646"></a>
Source: [PDF p.646, printed p.11-350](../page-images/p0646.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P2238: A/F Sensor (Sensor 1) AFS+ Circuit Low Voltage

**NOTE:** Before you troubleshoot record all freeze data and any on-board snapshot and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Check for Temporary DTCs or DTCs with the HDS.
   - **Is DTC P2238 indicated?**
     - **Y** — Go to step 4.
     - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM . •

4. Turn the ignition switch OFF.
5. Jump the SCS line with the HDS.
6. Disconnect the A/F sensor (Sensor 1) 4P connector.
7. Disconnect ECM connector A (31P).
8. Check for continuity between ECM connector terminal A31 and body ground.

> **ECM CONNECTOR A (31P)**
> Wire side of female terminals
>
> | 1 | 2 | 3 | 4 | 5 |
> |---|---|---|---|---|
> | 6 | 7 | | 8 | 9 |
> | 10 | / 13 | 14 | 15 | 16 |
> | / 18 | / 20 | 21 | 23 | 24 |
> | 25 | 26 | / 28 | / 30 | 31 |
>
> **AFS+ (RED)**

9. Replace the A/F sensor (Sensor 1) (see page 11-386).
10. Reconnect all connectors.
11. Turn the ignition switch ON (**II**).
12. Reset the ECM with the HDS.
13. Do the ECM idle learn procedure (see page 11-462).
14. Check for Temporary DTCs or DTCs with the HDS.
    - **Is DTC P2238 indicated?**
      - **Y** — C h e c k for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1. If the connector and terminal fits are OK, go to step 16.
      - **NO** — Go to step 15.

15. Monitor the OBD STATUS for DTC P2238 in the DTCs MENU with the HDS.
    - **Does the screen indicated PASSED?**
      - **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 14, go to the indicated DTCs troubleshooting. •
      - **NO** — If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

- Wire side of female terminals
  - **Is there continuity?**
    - **YES** — Repair short in the wire between the ECM (A31) and the A/F sensor (Sensor 1), then go to step 11.
    - **NO** — Go to step 9.

*Page 11-350*

---

### Printed page 11-351

<a id="p647"></a>
Source: [PDF p.647, printed p.11-351](../page-images/p0647.png).

# PGM-FI System — DTC Troubleshooting

16. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

17. Start the engine, and let it idle.

18. Check for Temporary DTCs or DTCs with the HDS. Is DTC P2238 indicated?

YES—If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 17. If the ECM was substituted, go to step 1.

NO—Go to step 19.

19. Monitor the OBD STATUS for DTC P2238 in the DTCs MENU with the HDS. Does the screen indicate PASSED?

YES—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 18, go to the indicated DTCs troubleshooting. •

NO—If the screen indicates FAILED, go to step 1. If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 17. If the ECM was substituted, go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-352

<a id="p648"></a>
Source: [PDF p.648, printed p.11-352](../page-images/p0648.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P2252: A/F Sensor (Sensor 1) AFS—Circuit Low Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine.
4. Check for Temporary DTCs or DTCs with the HDS.

| Is DTC P2252 Indicated? |
| :--- |
| **Y** | **E S** — Go to step 5.
| **NO** | Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM. •

5. Turn the ignition switch OFF.
6. Jump the SCS line with the HDS.
7. Disconnect the A/F sensor (Sensor 1) **4P** connector.
8. Disconnect ECM connector A (**31P**).
9. Check for continuity between ECM connector terminals A28 and body ground.

```
ECM CONNECTOR A (31P)
1 | 2 | 3 | 4 | 5 6 | 7 | 8 | 9
10
/ / 13 14 15 16
/ 18
/ 20 21
/ 23 24 25 26
/ 28
/ 30 31
```

**AFS — X j R E D / Y E L )**

10. Replace the A/F sensor (Sensor 1) (see page 11-386).
11. Reconnect all connectors.
12. Turn the ignition switch ON (**II**).
13. Reset the ECM with the HDS.
14. Do the ECM idle learn procedure (see page 11-462).
15. Check for Temporary DTCs or DTCs with the HDS.

| Is DTC P2252 indicated? |
| :--- |
| **YES** | Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1. If the connectors and terminal fits are OK, go to step 17.
| **NO** | Go to step 16.

16. Monitor the OBD STATUS for DTC P2252 in the DTCs MENU with the HDS.

| Does the screen indicate PASSED? |
| :--- |
| **YES** | Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 15, go to the indicated DTCs troubleshooting. •
| **NO** | If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

Wire side of female terminals

| Is there continuity? |
| :--- |
| **YES** | Repair short in the wire between the ECM (A28) and the A/F sensor (Sensor 1), then go to step 11.
| **NO** | Go to step 10.

**Page Reference:** 11-352

---

### Printed page 11-353

<a id="p649"></a>
Source: [PDF p.649, printed p.11-353](../page-images/p0649.png).

# PGM-FI System — DTC Troubleshooting

17. Update the ECM if it does not have the latest * software (see page 11-216), or substitute a known-good ECM (see page 11-217).

18. Start the engine, and let it idle.

19. Check for Temporary DTCs or DTCs with the HDS. Is DTC P2252 Indicated?

YES—If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 18. If the ECM was substituted, go to step 1. NO— Go to step 20.

20. Monitor the OBD STATUS for DTC P2252 in the DTCs MENU with the HDS. Does the screen indicate PASSED?

YES—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 19, goto the indicated DTCs troubleshooting. •

NO—If the screen indicates FAILED, go to step 1. If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 18. If the ECM was substituted, go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

For connector orientation and terminal positions, refer to the source image.

---

### Printed page 11-354

<a id="p650"></a>
Source: [PDF p.650, printed p.11-354](../page-images/p0650.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P2270: Secondary HO2S (Sensor2) Circuit Signal Stuck Lean
### DTC P2271: Secondary HO2S (Sensor2) Circuit Signal Stuck Rich

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.
4. Test-drive under these conditions:
   - Engine coolant temperature (**ECT SENSOR 1**) above 176 °F (80 °C)
   - Vehicle speed at 35 mph (56 km/h) or more
   - Drive 26 seconds or more
5. Monitor the **OBD STATUS** for DTC P2270 or P2271 in the DTCs MENU with the HDS.
   Does the screen indicate FAILED?
   - **YES** — Go to step 6.
   - **NO** — If the screen indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the **ECM**. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates **O U T OF CONDITION**, go to step 3 and recheck.

6. Turn the ignition switch OFF.
7. Replace the secondary **HO2S (Sensor 2)** (see page 11-386).
8. Turn the ignition switch ON (**II**).
9. Reset the ECM with the HDS.
10. Do the **ECM** idle learn procedure (see page 11-462).
11. Start the engine, and let it idle without load (in neutral) until the radiator fan comes on.
12. Test-drive under these conditions:
    - Engine coolant temperature (**ECT SENSOR 1**) above 176°F(80 °C)
    - Vehicle speed at 35 mph (56 km/h) or more
    - Drive 26 seconds or more
13. Check for Temporary DTCs or DTCs with the HDS.
    Is **D T C P2270** or **P2271** indicated?
    - **YES** — Check for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the **ECM**, then go to step 1.
    - **NO** — Go to step 14.

14. Monitor the **OBD STATUS** for DTC P2270 or P2271 in the DTCs MENU with the HDS.
    Does the screen indicate PASSED?
    - **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 13, go to the indicated **DTCs** troubleshooting.
    - **NO** — If the screen indicates FAILED, check for poor connections or loose terminals at the secondary **HO2S (Sensor 2)** and the **ECM**, then go to step 1. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates **O U T OF CONDITION**, go to step 12.

**Page Reference:** 11-354

---

### Printed page 11-355

<a id="p651"></a>
Source: [PDF p.651, printed p.11-355](../page-images/p0651.png).

# DTC P2610: ECM Ignition Off Internal Timer

## Performance Problem

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P2610 indicated?**

*   **YES— Go to step 4.**
*   **NO— Intermittent failure, the system is OK at this time.**

4. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

5. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P2610 indicated?**

*   **YES— If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.**
*   **NO— If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.**

**Page Reference:** 11-355

---

### Printed page 11-356

<a id="p652"></a>
Source: [PDF p.652, printed p.11-356](../page-images/p0652.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P2A00: A/F Sensor (Sensor 1) Circuit Range/Performance Problem

**NOTE:** Before you troubleshoot record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
4. Test-drive under these conditions:
   - Engine coolant temperature (**ECT SENSOR 1**) above 158°F(70< C)
   - Transmission in 3rd gear
   - Drive the vehicle between 25—55 mph (40 — 88 km/h) for 5 minutes.
   - Drive at a steady speed between 55—75 mph (88—120 km/h) for 10 minutes, then slow down with the throttle completely closed for 4 seconds.
5. Monitor the OBD **S T A T U S** for DTC P2A00 in the DTCs MENU with the HDS.
   Does the screen indicate FAILED?
   - **YES** — Go to step 6.
   - **NO** — If the screen indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose at the A/F sensor (Sensor 1) and the ECM . If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates O U T OF CONDITION, go to step 3 and recheck.

6. Turn the ignition switch OFF.
7. Replace the A/F sensor (Sensor 1) (see page 11-386).
8. Turn the ignition switch ON (**II**).
9. Reset the ECM with the HDS.
10. Do the ECM idle learn procedure (see page 11-462).
11. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
12. Test-drive under these conditions:
   - Engine coolant temperature (**ECT SENSOR 1**) above 158 °F (70 X )
   - Transmission in 3rd gear
   - Drive first the vehicle between 25—55 mph (40— 88 km/h) for 5 minutes.
   - Drive at steady speed between 55—75 mph (88—120 km/h) for 10 minutes, then slow down with the throttle completely closed for 4 seconds.
13. Check for Temporary DTCs or DTCs with the HDS.
   Is DTC P2A00 indicated?
   - **YES** — C h e c k for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1.
   - **NO** — Go to step 14.
14. Monitor the OBD **S T A T U S** for DTC P2A00 in the DTCs MENU with the HDS.
   Does the screen indicate PASSED?
   - **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 13, go to the indicated DTCs troubleshooting. •
   - **NO** — If the screen indicates FAILED, check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the ECM , then go to step 1. If the screen indicates EXECUTING, keep driving until a result comes on. If the screen indicates OUT OF CONDITION, go to step 12.

**11-356**

---

### Printed page 11-357

<a id="p653"></a>
Source: [PDF p.653, printed p.11-357](../page-images/p0653.png).

# DTC U0122: F-CAN Malfunction (ECM-VSA Modulator-Control Unit)

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC U0122 Indicated?**
*   **YES** — Go to step 4.
*   **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the VSA modulator-control unit and the ECM.

4. Check for a DTCs in the DTCs MENU with the HDS.

**VSA DTC 86 Indicated?**
*   **YES** — Go to step 5.
*   **NO** — Go to step 13.

5. Turn the ignition switch OFF.
6. Jump the SCS line with the HDS.
7. Disconnect the VSA modulator-control unit 47P connector (see page 19-127).
8. Disconnect ECM connector E (31P).
9. Connect VSA modulator-control unit 47P connector terminal No. 11 to body ground with a jumper wire.

**V S A M O D U L A T O R - C O N T R O L UNIT 47P C O N N ECT O R**
*   **1 C A N H (RED)**
*   `1 | 2 | / U M e L / M 9 M n M i 3 M i 5 | 16`
*   `1 7 | / | / | / | / | / | / | y l 2 5 | / j 2 7 | / | 2 9 | / | 3 1`
*   `32 47 32`
*   `|33|34|35|36|37|/|/|/1/l42|43|44|45|46|`
*   `47`
*   **J U M P E R WIRE**
*   Wire side of female terminals

10. Check for continuity between ECM connector terminal E11 and body ground.

**ECM C O N N ECT O R E (31P)**
*   `t | / | 3 | 4 | 5 / I 7 | | 8 | 9`
*   `/ 11 12 13 14 15 16 17 18 19 20 21`
*   `22`
*   `/ 24 25`
*   `/ 27 28 29 30`
*   `/ C A N H (RED)`
*   Wire side of female terminals

**Is there continuity?**
*   **YES** — Go to step 11.
*   **NO** — Repair open in the wire between the ECM (E11) and the VSA modulator-control unit, then go to step 13.

**(cont'd)**

---

### Printed page 11-358

<a id="p654"></a>
Source: [PDF p.654, printed p.11-358](../page-images/p0654.png).

# DTC U0122 Troubleshooting (continued)

11. Ground VSA modulator-control unit 47P connector terminal **15, CANL (WHT)** with a jumper wire.
12. Check continuity between ECM connector **E24, CANL (WHT)** and ground. **YES:** Substitute a known-good VSA modulator-control unit (p.19-127), then reconnect at step 13 and recheck. If U0122 is absent, replace the original VSA unit (p.19-127), then go to step 13. **NO:** Repair open between ECM E24 and VSA unit; step 13.
13. Reconnect all connectors.
14. Turn ignition ON (II).
15. Reset ECM with HDS.
16. Perform ECM idle learn (p.11-462).
17. Check DTCs with HDS. **U0122 YES:** Check VSA unit/ECM connections and return to step 1. **NO:** Troubleshooting complete; address other indicated DTCs.

Refer to the source image for connector orientation.

---

### Printed page 11-359

<a id="p655"></a>
Source: [PDF p.655, printed p.11-359](../page-images/p0655.png).

# DTC U1102: F-CAN Malfunction (BUS-OFF)

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Check for Temporary DTCs or DTCs with the HDS.

Is DTC U1102 Indicated?
* **YES** — Go to step 4.
* **NO** — Intermittent failure, the system is OK at this time.

4. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
5. Turn the ignition switch ON (**II**).
6. Check for Temporary DTCs or DTCs with the HDS.

Is DTC U1102 indicated?
* **YES** — If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
* **NO** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

---

### Printed page 11-360

<a id="p656"></a>
Source: [PDF p.656, printed p.11-360](../page-images/p0656.png).

# F-CAN Circuit Troubleshooting

*The source marks CANL-line instructions with an asterisk.*

1. Turn ignition OFF.
2. Jump SCS with HDS.
3. Disconnect ECM connector E (31P).
4. Disconnect HDS from DLC.
5. Measure resistance between ECM **E11 CANH (RED)** and **E24 CANL (WHT)**. Is it **108–132 Ω**? **YES:** Step 16. **NO:** Step 6.
6. Disconnect VSA modulator-control unit 47P connector.
7. Disconnect steering angle sensor 5P connector.
8. Check continuity between ECM E11 and E24. **YES:** Repair short between those wires. **NO:** Step 9.

Refer to the source image for connector orientation.

---

### Printed page 11-361

<a id="p657"></a>
Source: [PDF p.657, printed p.11-361](../page-images/p0657.png).

# F-CAN Circuit Troubleshooting (continued)

9. Ground ECM connector **E11 CANH (RED)** with a jumper wire.
10. Check continuity between VSA modulator-control unit 47P terminal **11 CANH (RED)** and ground. **YES:** Step 11. **NO:** Repair open between ECM E11 and VSA unit.
11. Check continuity between steering angle sensor 5P terminal **4 CANH (RED)** and ground. **YES:** Step 12. **NO:** Repair open between ECM E11 and steering angle sensor.
12. Remove the jumper from ECM connector E.

Refer to the source image for connector orientation.

---

### Printed page 11-362

<a id="p658"></a>
Source: [PDF p.658, printed p.11-362](../page-images/p0658.png).

# F-CAN Circuit Troubleshooting (continued)

13. Ground ECM connector **E24 CANL (WHT)** with a jumper wire.
14. Check continuity between VSA modulator-control unit 47P terminal **15 CANL (WHT)** and ground. **YES:** Step 15. **NO:** Repair open between ECM E24 and VSA unit.
15. Check continuity between steering angle sensor 5P terminal **2 CANL (WHT)** and ground. **YES:** Replace VSA modulator-control unit (p.19-127). **NO:** Repair open between ECM E24 and steering angle sensor.

Refer to the source image for connector orientation.
