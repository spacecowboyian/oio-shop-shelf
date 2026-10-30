# Fuel and Emissions Systems (Part C)

Reviewed conversion of PDF pp.477–567 (printed pp.11-181–11-271). Each page links to its source image for layout and diagram details.

### Printed page 11-181

<a id="p477"></a>
Source: [PDF p.477, printed p.11-181](../page-images/p0477.png).

# EVAP System — DTC P0497 (continued)

16. Disconnect the vacuum hose from EVAP canister vent filter line **A** and attach a 0–30 in.Hg vacuum pump/gauge.
17. Ground ECM terminal **A4 (VSV, light green/white)** with a jumper wire.
18. Turn ignition ON (II).
19. Apply vacuum. If the valve holds vacuum, inspect the line between the EVAP canister purge valve and canister. If it does not, replace the EVAP canister vent shut valve.
20. Turn ignition OFF.
21. Disconnect vent shut valve 2P connector.
22. Check continuity between vent shut valve connector terminal **2 (VSV, light green/white)** and body ground. If continuity exists, go to step 23; otherwise repair the open between valve and ECM.
23. Turn ignition ON (II).
24. Measure between vent shut valve connector terminal **1 (IG1, black/yellow)** and body ground. If battery voltage is present, go to step 25; otherwise repair the open between valve and No. 6 ACG (15 A) fuse in under-dash fuse/relay box.

---

### Printed page 11-182

<a id="p478"></a>
Source: [PDF p.478, printed p.11-182](../page-images/p0478.png).

# EVAP System — DTC P0497 (continued)

25. At the valve side, measure resistance between vent shut valve 2P connector terminals **1** and **2**. If about **33 Ω at room temperature**, substitute a known-good ECM (page 11-5) and retest; if the symptom disappears, replace the original ECM (page 11-115). Otherwise, replace the vent shut valve. The illustration shows the terminal side of the male connector.

---

### Printed page 11-183

<a id="p479"></a>
Source: [PDF p.479, printed p.11-183](../page-images/p0479.png).

# DTC P1456: EVAP Control System Leakage (Fuel Tank System)

## NOTICE
The fuel system is designed to allow specified maximum vacuum and pressure conditions. Do not deviate from the vacuum and pressure tests as indicated in these procedures. Excessive pressure/vacuum would damage the EVAP components or cause eventual fuel tank failure.

### Special Tools Required
Vacuum pump/gauge, 0—30 in.Hg, Snap-on YA4000A or equivalent, commercially available

This is a two-trip code; once cleared, it cannot be reproduced in one trip. Also, certain specific driving and ambient conditions must occur before the ECM will complete the system checks. Additional test drives may still not meet the specific conditions needed to reproduce the code. If necessary, use the test drive procedures for setting the readiness code (see page 11-40).

Follow these troubleshooting procedures carefully to ensure the integrity of the system and to confirm the cause of the problem or code.

**NOTE:**
*   Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).
*   Fresh fuel has a higher volatility that will create greater pressure/vacuum. The optimum condition for testing is fresh fuel, and must be less than a full tank of gas. If possible, to assist in leak detection, add 1 gallon of fresh fuel to the tank (as long as it will not fill the tank), just before starting these procedures.

### Fuel Fill Cap Check
1. Check the fuel fill cap (the cap must say "If not tightened 3 clicks check engine light may come on.")
   Is the proper fuel fill cap installed and properly tightened?
   *   **YES** — Go to step 2.
   *   **NO** — Replace or tighten the cap.

2. Check the fuel fill cap seal and the fuel fill pipe sealing surface.
   Is the fuel fill cap seal missing or damaged, or is the fill pipe damaged?
   *   **YES** — Replace the fuel fill cap (gray or black colored cap), or the fuel fill pipe.
   *   **NO** — The fuel fill cap is OK. Go t o step 3.

### EVAP Canister Purge Valve Test
3. Disconnect the vacuum hose from the EVAP purge joint (A), and connect a commercially available vacuum pump/gauge, 0—30 in.Hg, to the hose.
4. Turn the ignition switch ON (II).
5. Apply vacuum to the hose.
   Does the valve hold vacuum?
   *   **YES** — The EVAP canister purge valve is OK. Go to step 11.
   *   **NO** — Go to step 6.

6. Turn the ignition switch OFF.
7. Disconnect the EVAP canister purge valve 2P connector.
(cont'd)
11-183

---

### Printed page 11-184

<a id="p480"></a>
Source: [PDF p.480, printed p.11-184](../page-images/p0480.png).

# EVAP System
## DTC Troubleshooting (cont'd)

### Step 8
Check for continuity between EVAP canister purge valve 2P connector terminal No. 2 and body ground.

**EVAP CANISTER PURGE VALVE 2P CONNECTOR**
```
1   2
PCS (RED/YEL) [Wire side of female terminals]
```

Is there continuity?
- **YES** — Go to step 9.
- **NO** — Replace the EVAP canister purge valve. •

### Step 9
Disconnect ECM connector A (32P).

### Step 10
Check for continuity between EVAP canister purge valve 2P connector terminal No. 2 and body ground.

**EVAP CANISTER PURGE VALVE 2P CONNECTOR**
```
1   2
PCS (RED/YEL) [Wire side of female terminals]
```

Is there continuity?
- **YES** — Repair short in the wire between the EVAP canister purge valve and the ECM (A6). •
- **NO** — Substitute a known-good ECM (see page 11-5), then recheck. If the symptom/indication goes away, replace the original ECM (see page 11-115). •

---

## EVAP Bypass Solenoid Valve Test

### Step 11
Disconnect both vacuum hoses from the EVAP two way valve (A), and connect a commercially available vacuum pump/gauge, 0—30 in.Hg, to the canister port on the two way valve.

### Step 12
Turn the EVAP bypass solenoid valve ON with the HDS, or connect ECM connector terminal A3 to body ground with a jumper wire.

**ECM CONNECTOR A (32P)**
```
      WBS (ORN)
    1   2   3   4
    /   6   /   /   9  10
    12  13
    /   15
    /   17  18  19  20  21
    /   24
    25  26  27  28  29  30
    /   32
```
**JUMPER WIRE** [Wire side of female terminals]

### Step 13
Turn the ignition switch ON (II).

### Step 14
Apply vacuum to the hose.

Does the valve hold vacuum?
- **YES** — Go to step 15.
- **NO** — Go to step 20.

*Page Reference: 11-184*

---

### Printed page 11-185

<a id="p481"></a>
Source: [PDF p.481, printed p.11-185](../page-images/p0481.png).

# S2000 Fuel and Emissions Part C
## Page 481

### EVAP Bypass Solenoid Valve Circuit Test

**Step 15.** Turn the ignition switch OFF.

**Step 16.** Disconnect the EVAP bypass solenoid valve 2P connector.

**Step 17.** Check for continuity between EVAP bypass solenoid valve 2P connector terminal No. 2 and body ground.

> **EVAP BYPASS SOLENOID VALVE 2P CONNECTOR**
>
> Terminal 2: WBS (orange), wire side of female connector.

**Is there continuity?**

*   **YES** — Go to step 18.
*   **NO** — Repair open in the wire between the EVAP bypass solenoid valve and the ECM (A3).

---

**Step 18.** Turn the ignition switch ON (II).

**Step 19.** Measure voltage between EVAP bypass solenoid valve 2P connector terminal No. 1 and body ground.

> Terminal 1: IG1 (black/yellow), wire side of female connector.

**Is there battery voltage?**

*   **YES** — Replace the EVAP bypass solenoid valve (A) and the O-rings (B).
*   **NO** — Repair open in the wire between the EVAP bypass solenoid valve and the No. 6 ACG (15 A) fuse.

*(cont'd)*

**Page Reference:** 11-185

---

### Printed page 11-186

<a id="p482"></a>
Source: [PDF p.482, printed p.11-186](../page-images/p0482.png).

# EVAP System
## DTC Troubleshooting (cont'd)

**20.** Plug the upper port (A) of the EVAP two way valve.



**21.** While monitoring FTP sensor voltage with the HDS, or measuring the voltage between ECM connector terminals A29 and C18, slowly pump the vacuum pump/gauge until the voltage drops to about 1.5 V.

ECM measurement points: A29 (PTANK, light green) and C18 (SG2, green/yellow).

**Does the voltage drop to 1.5 V and hold for at least 20 seconds?**

*   **YES** — The EVAP bypass solenoid valve/EVAP two way valve is OK. Go to step 22.
*   **NO** — Repair leak from the EVAP bypass solenoid valve, EVAP two way valve, FTP sensor, or O-rings.

## EVAP Canister Vent Shut Valve Test

**22.** Disconnect the vacuum hose from the EVAP canister vent filter line (A), and connect a commercially available vacuum pump/gauge, 0—30 in.Hg, to the hose.

**23.** Turn the ignition switch ON (II).

**24.** Apply vacuum to the hose with 5 strokes of the pump.

**Does the valve hold vacuum?**

*   **YES** — Go to step 25.
*   **NO** — The EVAP canister vent shut valve is OK. Go to step 30.

**25.** Turn the ignition switch OFF.

**26.** Disconnect the EVAP canister vent shut valve 2P connector.

> Terminal 2: VSV (light green/white), wire side of female connector.

**27.** Check for continuity between EVAP canister vent shut valve 2P connector terminal No. 2 and body ground.

---

### Printed page 11-187

<a id="p483"></a>
Source: [PDF p.483, printed p.11-187](../page-images/p0483.png).

# EVAP System — DTC P1456 (continued)

**Vent shut valve test, continued:** If continuity is present at step 27, go to step 28. Otherwise, replace vent shut valve **A** and O-ring **B**.

28. Disconnect ECM connector A (32P).
29. Check continuity between vent shut valve 2P connector terminal **2 (VSV, light green/white)** and body ground. If continuity exists, repair the short between valve and ECM A4. Otherwise, substitute a known-good ECM (page 11-5), then replace the original ECM (page 11-115) if symptom disappears.

## Vacuum Hoses and Connections Test

30. Perform the fuel tank vapor control valve test (page 11-195). If valve is OK, continue; otherwise replace it.
31. Tighten fuel cap three clicks and monitor FTP readings with HDS.
32. Start engine and idle **5 minutes**.
33. Check FTP sensor reading. If **above 4 mmHg pressure or below −4 mmHg vacuum**, substitute a known-good ECM and retest; replace original ECM if symptom disappears. Otherwise, inspect for vacuum leaks at: fuel tank **A**, fill cap **B**, fill pipe **C**, vapor control valve **D**, vapor recirculation valve **E**, vapor recirculation tube **F**, vapor signal tube **G**, and vapor control vent tube **H**. Repair or replace parts as needed.

---

### Printed page 11-188

<a id="p484"></a>
Source: [PDF p.484, printed p.11-188](../page-images/p0484.png).

# EVAP System
## DTC Troubleshooting (cont'd)
### DTC P1457: EVAP Control System Leakage
#### (EVAP Canister System)

**NOTICE**
The fuel system is designed to allow specified maximum vacuum and pressure conditions. Do not deviate from the vacuum and pressure tests as indicated in these procedures. Excessive pressure/vacuum would damage the EVAP components or cause eventual fuel tank failure.

**Special Tools Required**
Vacuum pump/gauge, 0—30 in.Hg, Snap-on YA4000A or equivalent, commercially available

This is a two-trip code; once cleared, it cannot be reproduced in one trip. Also, certain specific driving and ambient conditions must occur before the ECM will complete the system checks. Additional test drives may still not meet the specific conditions needed to reproduce the code. If necessary, use the test drive procedures for setting the readiness code (see page 11-40).

Follow these troubleshooting procedures carefully to ensure the integrity of the system and to confirm the cause of the problem or code.

**NOTE:**
*   Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).
*   Fresh fuel has a higher volatility that will create greater pressure/vacuum. The optimum condition for testing is fresh fuel, at least half, but less than a full tank. If possible, to assist in leak detection, add **1 gallon** of fresh fuel to the tank (as long as it will not fill the tank), just before starting these procedures.

---

### EVAP Canister Purge Valve Test

1.  Disconnect the vacuum hose from the EVAP purge joint (**A**), and connect a commercially available vacuum pump/gauge, 0—30 in.Hg, to the hose.
    *   **A**
2.  Turn the EVAP canister purge valve on with the HDS, or connect ECM connector terminal **A6** to body ground with a jumper wire.
    *   **ECM C O N N E C T O R A (32P)**
        *   **P C S (RED/YEL)**
        *   1 2 3 4
        *   / 6
        *   / / 9 10
        *   12 13
        *   / 15
        *   / 17 18 19 20 21 24
        *   25 26 27 28 29 30
        *   / 32
    *   **J U M P E R WIRE**
    *   Wire side of female terminals
3.  Turn the ignition switch ON (**II**).
4.  Apply vacuum to the hose.
    *   Does the valve hold vacuum?
        *   **YES** — Go to step 5.
        *   **N O** — The EVAP canister purge valve is OK. Go to step 10.
5.  Turn the ignition switch OFF.
6.  Disconnect the EVAP canister purge valve 2P connector.

*Page Reference: 11-188*

---

### Printed page 11-189

<a id="p485"></a>
Source: [PDF p.485, printed p.11-189](../page-images/p0485.png).

# EVAP Canister Purge Valve Test

## Step 7
Check for continuity between EVAP canister purge valve 2P connector terminal No. 2 and body ground.

**EVAP CANISTER PURGE VALVE 2P CONNECTOR**
```
1 2
[ PCS (RED/YEL) ]
Wire side of female terminals
```

Is there continuity?
- **YES** — Go to step 8.
- **NO** — Repair open in the wire between the EVAP canister purge valve and the ECM (A6).

## Step 8
Turn the ignition switch ON (II).

## Step 9
Measure voltage between EVAP canister purge valve 2P connector terminal No. 1 and body ground.

**EVAP CANISTER PURGE VALVE 2P CONNECTOR**
```
1 2
[ IG1 (BLK/YEL) ]
Wire side of female terminals
```

Is there battery voltage?
- **YES** — Replace the EVAP canister purge valve.
- **NO** — Repair open in the wire between the EVAP canister purge valve and the No. 6 ACG (15 A) fuse.

---

## EVAP Bypass Solenoid Valve Test

### Step 10
Disconnect both vacuum hoses from the EVAP two way valve (A), and connect a commercially available vacuum pump/gauge, 0—30 in.Hg, to the canister port on the two way valve.

### Step 11
Turn the ignition switch ON (II).

### Step 12
Apply vacuum to the hose.

Does the valve hold vacuum?
- **YES** — The EVAP bypass solenoid valve/EVAP two way valve is OK. Go to step 18.
- **NO** — Go to step 13.

### Step 13
Turn the ignition switch OFF.

### Step 14
Disconnect the EVAP bypass solenoid valve 2P connector.

### Step 15
Check for continuity between EVAP bypass solenoid valve 2P connector terminal No. 2 and body ground.

**EVAP BYPASS SOLENOID VALVE 2P CONNECTOR**
```
1 2
[ 2WBS (ORN) ]
Wire side of female terminals
```

---

**

---

### Printed page 11-190

<a id="p486"></a>
Source: [PDF p.486, printed p.11-190](../page-images/p0486.png).

# EVAP System
## DTC Troubleshooting (cont'd)

### Is there continuity?
*   **YES** — Go to step 16.
*   **NO** — Replace the EVAP bypass solenoid valve (A) and O-rings (B).

---

### Step 16
Disconnect ECM connector A (32P).

### Step 17
Check for continuity between EVAP bypass solenoid valve 2P connector terminal No. 2 and body ground.

**EVAP BYPASS SOLENOID VALVE 2P CONNECTOR**
```
    1   2
    WBS (ORN)
```
*Wire side of female terminals*

*   **Is there continuity?**
    *   **YES** — Repair the short in the wire between the EVAP bypass solenoid valve and the ECM (A3).
    *   **NO** — Substitute a known-good ECM (see page 11-5), then recheck. If the symptom/indication goes away, replace the original ECM (see page 11-115).

---

### EVAP Canister Vent Shut Valve Test

**Step 18**
Disconnect the vacuum hose from the EVAP canister vent filter line (A), and connect a commercially available vacuum pump/gauge, 0—30 in.Hg, to the hose.

**Step 19**
Turn the EVAP canister vent shut valve on with the HDS, or connect ECM connector terminal A4 to body ground with a jumper wire.

**ECM CONNECTOR A (32P)**
```
    VSV (LT GRN/WHT)
    1   2   3   4
    /   6   /   /
    9  10  12  13
    /  15  /  17  18  19  20  21
    /  24
    25  26  27  28  29  30
    /  32
```
*Wire side of female terminals*

**Step 20**
Turn the ignition switch ON (II).

**Step 21**
Apply vacuum to the hose.

**Does the valve hold vacuum?**
*   **YES** — The EVAP canister vent shut valve is OK. Go to step 27.
*   **NO** — Go to step 22.

**Step 22**
Turn the ignition switch OFF.

**Step 23**
Disconnect the EVAP canister vent shut valve 2P connector.

---

*Page Reference: 11-190*

---

### Printed page 11-191

<a id="p487"></a>
Source: [PDF p.487, printed p.11-191](../page-images/p0487.png).

# EVAP System — DTC P1457 (continued)

24. Check continuity between vent shut valve 2P connector terminal **2 (VSV, light green/white)** and ground. If using HDS to turn valve on, turn ignition ON (II). If continuity exists, go to step 25; otherwise repair open between valve and ECM A4.
25. Turn ignition ON (II).
26. Measure between vent shut valve connector terminal **1** and ground. If battery voltage is present, replace vent shut valve **A** and O-ring **B**; otherwise repair open to No. 6 ACG (15 A) fuse.

## Canister System Leak Test

27. Turn ignition OFF.
28. Insert two three-way T-fittings **A** into hose from EVAP canister to two-way valve. Attach FTP sensor to one and 0–30 in.Hg vacuum pump/gauge to the other.
29. Remove vent hose from vent shut valve **A** and cap port **B** to seal canister fresh-air vent.
30. Turn ignition ON (II).
31. Monitor FTP voltage with HDS or between ECM **A29 and C18**, and slowly pump vacuum. Continue on next page.

---

### Printed page 11-192

<a id="p488"></a>
Source: [PDF p.488, printed p.11-192](../page-images/p0488.png).

# EVAP System
## DTC Troubleshooting (cont'd)

**32.** Continue to pump vacuum until the voltage drops to about **1.5 V**. Make sure that the engine coolant temperature is still above **95 °F (35 °C)** and your vacuum pump has no leak.

**33.** Check the voltage for **20 seconds**.
Does the voltage drop to **1.5 V** and hold for at least **20 seconds**?

*   **YES**—Inspect the EVAP canister vent shut valve line and connections.
*   **NO**—Go to step **34**.

**34.** Turn the ignition switch **OFF**.

**35.** Disconnect the quick-connect fitting **(A)** from the EVAP canister, and plug the canister port **(B)**.

**36.** Turn the ignition switch **ON (II)**.

**37.** While monitoring FTP sensor voltage with the HDS, or measuring voltage between ECM connector terminals **A29** and **C18**, slowly pump the vacuum pump.

ECM measurement points: A29 (PTANK, light green) and C18 (SG2, green/yellow).

**38.** Continue to pump vacuum until the voltage drops to about **1.5 V**. Make sure the engine coolant temperature is still above **95 °F (35 °C)** and your vacuum pump/gauge has no leak.

*Page Reference: 11-192*

---

### Printed page 11-193

<a id="p489"></a>
Source: [PDF p.489, printed p.11-193](../page-images/p0489.png).

# EVAP System — DTC P1457 (continued)

39. Monitor FTP voltage for **20 seconds**. If it drops to **1.5 V** and holds for at least 20 seconds, inspect fuel tank vapor control line and connections; otherwise continue.
40. Turn ignition OFF.
41. Disconnect purge line hose **A** from canister at metal line; plug hose **B**.
42. Turn ignition ON (II).
43. Monitor FTP voltage with HDS, or measure between ECM **A29 and C18**, while slowly pumping vacuum.
44. Continue until voltage reaches about **1.5 V**. Ensure engine coolant remains above **95 °F (35 °C)** and pump/gauge does not leak.
45. Observe voltage for **20 seconds**. If it holds at **1.5 V**, inspect EVAP canister purge valve line and connections; if sound, test two-way valve (page 11-194) and fuel tank vapor control valve (page 11-195). Otherwise, replace EVAP canister.

---

### Printed page 11-194

<a id="p490"></a>
Source: [PDF p.490, printed p.11-194](../page-images/p0490.png).

# EVAP System
## EVAP Two Way Valve Test

### Special Tools Required
* Vacuum/pressure gauge, 0—4 in.Hg (Part No: 07JAZ-001000B)
* Vacuum pump/gauge, 0—30 in.Hg, Snap-on YA4000A or equivalent, commercially available

### Test Procedure

**Step 1:** Remove the fuel fill cap.

**Step 2:** Disconnect the vapor line from the EVAP two way valve (A). Connect it to a T-fitting (B) from the vacuum gauge and a commercially available vacuum pump/gauge, 0—30 in.Hg, as shown.
*Part No: 07JAZ-001000B*

**Step 3:** Apply vacuum slowly and continuously while watching the gauge.
The vacuum should stabilize momentarily at **0.8-2.1 kPa (0.2-0.6 in.Hg, 6 - 16 mmHg)**.

*   If the vacuum stabilizes (valve opens) below **0.8 kPa (0.2 in.Hg, 6 mmHg)** or above **2.1 kPa (0.6 in.Hg, 16 mmHg)**, install a new valve and retest.

**Step 4:** Move the vacuum pump hose from the vacuum fitting to the pressure fitting, and move the vacuum gauge hose from the vacuum side to the pressure side (A) as shown.
*Part No: 07JAZ-001000B*

**Step 5:** Slowly pressurize the vapor line while watching the gauge. The pressure should stabilize momentarily **above 1.0 kPa (0.3 in.Hg, 8 mmHg)**.

*   If the pressure momentarily stabilizes (valve opens) above **1.0 kPa (0.3 in.Hg, 8 mmHg)**, the valve is OK.
*   If the pressure stabilizes below **1.0 kPa (0.3 in.Hg, 8 mmHg)**, install a new valve and retest.

**Reference:** Page 11-194

---

### Printed page 11-195

<a id="p491"></a>
Source: [PDF p.491, printed p.11-195](../page-images/p0491.png).

# Fuel Tank Vapor Control Valve Test

## Special Tools Required
Vacuum pump/gauge, 0—30 in.Hg, Snap-on YA4000A or equivalent, commercially available

## Float Test
1. Make sure the fuel tank is less than half full.
2. Remove the fuel fill cap to relieve the fuel tank pressure, then reinstall the cap.
3. Remove the fuel pipe cover. Disconnect the fuel tank vapor recirculation tube (A), and connect a commercially available vacuum pump/gauge, 0—30 in.Hg, to the hose.

4. Plug the fuel tank vapor recirculation pipe (B).
5. Apply vacuum to the fuel tank vapor recirculation tube (A).
   - If the vacuum holds, replace the fuel tank vapor control valve (see page 11-196).
   - If the vacuum does not hold, the float is OK. Go to step 1 of the valve test.

## Valve Test
1. Make sure the fuel tank is less than half full.
2. Remove the fuel fill cap.
3. Remove the fuel pipe cover. Disconnect the fuel tank vapor signal tube (A).

4. Disconnect the vacuum hoses (A) from the EVAP canister (B), and then plug the ports with plugs (C).

5. Disconnect the vacuum hose (D) from the EVAP canister vent shut valve (E), and connect a commercially available vacuum pump/gauge, 0—30 in.Hg, to the EVAP canister vent shut valve.
6. Pump the vacuum pump 80 times.
   - If the vacuum holds, go to step 7.
   - If the vacuum does not hold, go to step 9.

(cont'd)
11-195

---

### Printed page 11-196

<a id="p492"></a>
Source: [PDF p.492, printed p.11-196](../page-images/p0492.png).

# EVAP System
## Fuel Tank Vapor Control Valve Test (cont'd)

7. Connect a second vacuum pump/gauge to the fuel tank vapor signal tube (A).

8. Apply vacuum (1 pump) to the fuel tank vapor signal tube (A), then check the vacuum on the pump in step 6.
   * If the vacuum holds, replace the fuel tank vapor control valve (see page 11-196).
   * If the vacuum is released, the fuel tank vapor control valve is OK.

9. Disconnect the fuel tank vapor quick disconnect from the EVAP canister, then plug the port on the canister. Reapply vacuum (80 pumps).
   * If the vacuum holds, replace the fuel tank vapor control valve (see page 11-196).
   * If the vacuum does not hold, inspect the EVAP canister vent shut valve O-ring. If the O-ring is OK, replace the EVAP canister and repeat step 4.

### Fuel Tank Vapor Control Valve Replacement

1. Remove the fuel tank (see page 11-156).
2. Remove the fuel tank vapor control valve (A) from the fuel tank (B).
3. Replace the base gasket (C).
4. Install the fuel tank vapor control valve.
5. Install the fuel tank.

**Page Reference:** 11-196

---

### Printed page 11-197

<a id="p493"></a>
Source: [PDF p.493, printed p.11-197](../page-images/p0493.png).

# Pulsed Secondary Air Injection System — Component Location Index

The source illustration locates the **air control valve vacuum control solenoid valve**, **air control valve** (removal/installation page 9-2), **air pump relay** (removal/installation page 11-208; test page 11-209), **air pump** (removal/installation page 11-208), and **air pump electrical current sensor** (removal/installation page 11-209). Refer to the source image for their physical positions.

---

### Printed page 11-198

<a id="p494"></a>
Source: [PDF p.494, printed p.11-198](../page-images/p0494.png).

# Pulsed Secondary Air Injection System
## DTC Troubleshooting
### DTC P0410: Air Pump Circuit Malfunction

**NOTE:** Before you troubleshoot record all freeze data and review the general troubleshooting information (see page 11-3).

1. Reset the E C M (see page 11-4).
2. Make sure the engine coolant temperature is over 32 °F (0 °C) and below 158 °F (60 °C) with a scan tool or the HDS.
3. Start the engine. During air pump operation, hold the engine at idle speed without load (in neutral) for at least 10 seconds.
4. Check for a Temporary DTC with a scan tool or the HDS.

**Is Temporary DTC P0410 Indicated?**
- **Y E S** — G o to step 5.
- **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the air control valve vacuum control solenoid valve and at the E C M . H

5. Check the air pump.

**Does the air pump operate?**
- **Y E S** — G o to step 35.
- **N O** — G o to step 6.

6. Turn the ignition switch OFF.
7. Check the No. 32 AIR PUMP (60 A) fuse in the auxiliary under-hood fuse box.

**Is the fuse OK?**
- **Y E S** — G o to step 8.
- **NO** — Repair short in the wire between the No. 32 AIR PUMP (60 A) fuse and the air pump. Then replace the No. 32 AIR PUMP (60 A) fuse.


8. Remove the left-front inner fender (see page 20-126).
9. Disconnect the air pump electrical current sensor 2P connector.
10. Turn the ignition switch ON (II).
11. At the left engine compartment wire harness side, measure voltage between air pump electrical current sensor 2P connector terminal No. 1 and body ground.

```
AIR P U M P E L E C T R I C A L C U R R E N T S E N S O R
2P C O N N E C T O R
IG
(WHT)
Wire side of female terminals
```

**Is there battery voltage?**
- **Y E S** — G o to step 12.
- **NO** — Repair open in the wire between the air pump electrical current sensor and the No. 32 AIR PUMP (60 A) fuse in the auxiliary under-hood fuse box.

12. Turn the ignition switch OFF.
11-198

---

### Printed page 11-199

<a id="p495"></a>
Source: [PDF p.495, printed p.11-199](../page-images/p0495.png).

# Pulsed Secondary Air Injection System — DTC P0410 (continued)

13. At current sensor side, check continuity across its 2P connector terminals **1 (white)** and **2 (white/red)**. If continuous, go to step 14; otherwise replace sensor (page 11-209).
14. Reconnect sensor 2P connector.
15. Disconnect large air pump relay 2P connector.
16. Turn ignition ON (II).
17. Measure large relay connector terminal **1 (white/red)** to ground. Battery voltage: go to step 18; otherwise repair open between current sensor and relay.
18. Turn ignition OFF.
19. Test air pump relay (page 11-209). If OK, continue; otherwise replace relay (page 11-208).
20. Turn ignition ON (II).
21. Jumper large relay connector terminals **1 (white/red)** and **2 (white/green)**. If air pump runs, go to step 22; otherwise go to step 30.
22. Turn ignition OFF.
23. Remove jumper from large relay connector.
24. Disconnect small air pump relay 2P connector.

---

### Printed page 11-200

<a id="p496"></a>
Source: [PDF p.496, printed p.11-200](../page-images/p0496.png).

# Pulsed Secondary Air Injection System
## DTC Troubleshooting (cont'd)

### Step 25
Check for continuity between small air pump relay **2P** connector terminal No. 2 (GND, black) and body ground.

| Component | Terminal/Connection | Wire Color | Note |
| :--- | :--- | :--- | :--- |
| Small Air Pump Relay 2P Connector | GND (BLK) | Black | Wire side of female terminals |

**Is there continuity?**
*   **YES** — Go to step 26.
*   **NO** — Repair open in the wire between the air pump relay and body ground.

---

### Step 26
Disconnect **ECM** connector **A (32P)**.

---

### Step 27
Check for the continuity between **ECM** connector terminal **A28** and body ground.

| Component | Terminal/Connection | Wire Color | Note |
| :--- | :--- | :--- | :--- |
| ECM Connector A (32P) | A28 | APR (BLU) | Wire side of female terminals |

**Is there continuity?**
*   **YES** — Repair short in the wire between the air pump relay and the **ECM** (**A28**).
*   **NO** — Go to step 28.

---

### Step 28
Connect small air pump relay **2P** connector terminal No. 1 to body ground with a jumper wire.

| Component | Terminal/Connection | Wire Color | Note |
| :--- | :--- | :--- | :--- |
| Small Air Pump Relay 2P Connector | APR (BLU) | Blue | Jumper Wire; Wire side of female terminals |

---

### Step 29
Check for continuity between **ECM** connector terminal **A28** and body ground.

| Component | Terminal/Connection | Wire Color | Note |
| :--- | :--- | :--- | :--- |
| ECM Connector A (32P) | A28 | APR (BLU) | Wire side of female terminals |

**Is there continuity?**
*   **YES** — Substitute a known-good **ECM** (see page 11-5), then recheck. If the symptom/indication goes away, replace the original **ECM** (see page 11-115).
*   **NO** — Repair open in the wire between the air pump relay and the **ECM** (**A28**).

---

### Step 30
Turn the ignition switch **OFF**.

### Step 31
Disconnect the jumper wire from the large air pump relay **2P** connector.

### Step 32
Disconnect the air pump **2P** connector.

*Page Reference: 11-200*

---

### Printed page 11-201

<a id="p497"></a>
Source: [PDF p.497, printed p.11-201](../page-images/p0497.png).

# Pulsed Secondary Air Injection System — DTC P0410 (continued)

33. Check continuity between large air pump relay connector terminal **2** and air pump connector terminal **1** (white/green wire). If continuous, go to step 34; otherwise repair open between relay and pump.
34. Check continuity between air pump connector terminal **2** and ground (black wire). If continuous, replace pump (page 11-208); otherwise repair ground wire.
35. Turn ignition OFF.
36. Test air pump relay (page 11-209). If OK, continue; otherwise replace relay (page 11-208).
37. Disconnect ECM connector A (32P).
38. Turn ignition ON (II).
39. Measure ECM terminal **A28 (APR, blue)** to ground. If voltage exists, repair short to power between relay and ECM A28. Otherwise, substitute known-good ECM (page 11-5); if symptom disappears, replace original ECM (page 11-115).

---

### Printed page 11-202

<a id="p498"></a>
Source: [PDF p.498, printed p.11-202](../page-images/p0498.png).

# Pulsed Secondary Air Injection System
## DTC Troubleshooting (cont'd)
### DTC P0411: Secondary Air Injection System Incorrect Flow

**Special Tools Required**
Vacuum pump/gauge, 0—30 in.Hg, Snap-on YA4000A or equivalent, commercially available.

> **NOTE:** Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).

1. Reset the E C M (see page 11-4).
2. Make sure the engine coolant temperature is over 32 °F (0 °C) and below 158 °F (60 °C) with a scan tool or the HDS.
3. Start the engine. While the air pump operates, let the engine idle without load (in neutral) for at least 10 seconds.
4. Check for a Temporary DTC with a scan tool or the HDS.

**Is Temporary DTC P0411 Indicated?**
- **Y E S** — G o to step 5.
- **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the air control valve vacuum control solenoid valve and at the E C M . •

5. Turn the ignition switch OFF.
6. Check the vacuum lines of the air pump system for misrouting, leakage, breakage, and clogging.

**Are the vacuum lines OK?**
- **Y E S** — G o to step 7.
- **NO** — Repair or replace vacuum lines as necessary. •

7. Reset the E C M (see page 11-4).
8. Make sure the engine coolant temperature is over 32 °F (0 °C) and below 158 °F (60 °C) with a scan tool or the HDS.
9. Disconnect the vacuum hose from the air control valve (A), and connect a commercially available vacuum pump/gauge, 0—30 in.Hg, to the hose.
10. Start the engine. While the air pump operates, let the engine idle without load (in neutral).

**Is there vacuum while the air pump operates?**
- **Y E S** — G o to step 11.
- **NO** — Go to step 16.

11. Turn the ignition switch OFF.
12. Disconnect the air control valve vacuum control solenoid valve 2P connector.

> AIR CONTROL VALVE VACUUM CONTROL SOLENOID VALVE 2P CONNECTOR
> Wire side of female terminals

13. Check for continuity between air control valve vacuum control solenoid valve 2P connector terminal No. 2 and body ground.

**Is there continuity?**
- **Y E S** — G o to step 14.
- **NO** — Replace the air control valve vacuum control solenoid valve. •

11-202

---

### Printed page 11-203

<a id="p499"></a>
Source: [PDF p.499, printed p.11-203](../page-images/p0499.png).

# Pulsed Secondary Air Injection System — DTC P0411 (continued)

14. Disconnect ECM connector A (32P).
15. Check continuity between air control valve vacuum control solenoid 2P connector terminal **2 (SAVS, red)** and ground. If continuous, repair short to ECM A2. Otherwise substitute known-good ECM and recheck; replace original if symptom disappears.
16. Turn ignition OFF.
17. Check No. 6 ACG (15 A) fuse in under-dash fuse/relay box. If OK, continue; otherwise repair short between fuse and gauge assembly, then replace fuse. The source specifically names the gauge assembly.
18. Disconnect solenoid 2P connector.
19. Turn ignition ON (II).
20. Measure solenoid connector terminal **1 (IG1, black/yellow)** to ground. If battery voltage exists, continue; otherwise repair open between No. 6 ACG fuse and solenoid.
21. Turn ignition OFF.
22. Reconnect solenoid 2P connector.
23. Disconnect ECM connector A (32P).

---

### Printed page 11-204

<a id="p500"></a>
Source: [PDF p.500, printed p.11-204](../page-images/p0500.png).

# Pulsed Secondary Air Injection System
## DTC Troubleshooting (cont'd)

**24.** Turn the ignition switch ON (II), and measure voltage between ECM connector terminal A2 and body ground.

```
ECM CONNECTOR A (32P)
1 2 3 4
/ 6
/ / 9 10
12 13
/ 15
/ 17 18 19 20 21 24
25 26 27 28 29 30
/ 32
```
*Wire side of female terminals*

**Is there less than 1.0 V?**

- **YES**—Repair open in the wire between the air control valve vacuum control solenoid valve and the ECM (A2). If the wire is OK, replace the air control valve vacuum control solenoid valve.
- **NO**—Substitute a known-good ECM (see page 11-5), then recheck. If the symptom/indication goes away, replace the original ECM (see page 11-115).

---

## DTC P1410: Air Pump Malfunction ('00-03 models)
### DTC P2445: Air Pump Malfunction ('04-05 models)

**NOTE:**
- Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).
- Information marked with an asterisk (*) applies to '00-03 models.
- Information marked with double asterisk (* *) applies to '04-05 models.

**1.** Reset the ECM (see page 11-4).

**2.** Make sure the engine coolant temperature is over 32 °F (0 °C) and below 158 °F (60 °C) with a scan tool or the HDS.

**3.** Start the engine. While the air pump operates, let the engine idle without load (in neutral) for at least 10 seconds.

**4.** Check for a Temporary DTC with a scan tool or the HDS.

**Is Temporary DTC P1410* or P2445** indicated?

- **YES**—Replace the air pump.
- **NO**—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the air pump and the air pump relay.

**Page Reference:** 11-204

---

### Printed page 11-205

<a id="p501"></a>
Source: [PDF p.501, printed p.11-205](../page-images/p0501.png).

# DTC P1415: Air Pump Electrical Current
## Sensor Circuit Low Voltage

**NOTE:** Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).

1. Reset the ECM (see page 11-4).
2. Turn the ignition switch ON (II).
3. Check for a DTC with a scan tool or the HDS.

**Is DTC P1415 Indicated?**

*   **YES — Go to step 4.**
*   **NO — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the air pump electrical current sensor and the ECM.** B

4. Turn the ignition switch OFF.
5. Disconnect the air pump electrical current sensor 3P connector.
6. Turn the ignition switch ON (II).
7. Measure voltage between air pump electrical current sensor 3P connector terminals No. 1 and No. 2.

> **AIR PUMP ELECTRICAL CURRENT SENSOR**
> **3P CONNECTOR**
>
> | Label | Wire Color | Description |
> | :--- | :--- | :--- |
> | VCC2 | YEL/BLU | Wire side of female terminals |
> | SG2 | GRN | Wire side of female terminals |

**Is there about 5 V?**

*   **YES — Go to step 8.**
*   **NO — Go to step 17.**

8. Turn the ignition switch OFF.
9. Disconnect ECM connector C (31P).
10. Check for continuity between air pump electrical current sensor 3P connector terminal No. 3 and body ground.

> **AIR PUMP ELECTRICAL CURRENT SENSOR**
> **3P CONNECTOR**
>
> | Label | Wire Color | Description |
> | :--- | :--- | :--- |
> | ECS | WHT/BLK | Wire side of female terminals |

**Is there continuity?**

*   **YES — Repair short in the wire between the air pump electrical current sensor and the ECM (C24).** B
*   **NO — Go to step 11.**

11. Connect air pump electrical current sensor 3P connector terminals No. 2 and No. 3 with a jumper wire.

> **AIR PUMP ELECTRICAL CURRENT SENSOR**
> **3P CONNECTOR**
>
> | Label | Wire Color | Description |
> | :--- | :--- | :--- |
> | SG2 | GRN | Wire side of female terminals |
> | ECS | WHT/BLK | Wire side of female terminals |

*JUMPER WIRE*

**11-205**

---

### Printed page 11-206

<a id="p502"></a>
Source: [PDF p.502, printed p.11-206](../page-images/p0502.png).

# Pulsed Secondary Air Injection System — DTC P1415 (continued)

12. With the sensor 3P connector terminals 2 and 3 jumpered from prior page, check continuity between ECM connector terminals **C24 (ECS, white/black)** and **C18 (SG2, green/yellow)**. If continuous, continue; otherwise repair open between ECM C24 and current sensor.
13. Remove jumper from sensor 3P connector.
14. Reconnect ECM C (31P) and sensor 3P connectors.
15. Turn ignition ON (II).
16. Measure ECM terminal **C24** to body ground. If about **0.5 V**, substitute known-good ECM, recheck and replace original if symptom disappears. Otherwise replace current sensor (page 11-209).
17. Measure between ECM terminals **C18 (SG2, green/yellow)** and **C28 (VCC2, yellow/blue)**. If about **5 V**, repair open between ECM C28 and current sensor. Otherwise substitute known-good ECM and recheck; replace original if voltage normalizes.

---

### Printed page 11-207

<a id="p503"></a>
Source: [PDF p.503, printed p.11-207](../page-images/p0503.png).

# DTC P1416: Air Pump Electrical Current Sensor Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).

1. Reset the ECM (see page 11-4).
2. Turn the ignition switch ON (II).
3. Check for a DTC with a scan tool or the HDS.

**Is DTC P1416 Indicated?**

*   **Y E S** — G o to step 4.
*   **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the air pump electrical current sensor and at the ECM . B

4. Turn the ignition switch OFF.
5. Disconnect the air pump electrical current sensor 3P connector.
6. Turn the ignition switch ON (II).
7. Measure voltage between air pump electrical current sensor 3P connector terminals No. 1 and No. 2.

```
AIR PUMP E L E C T R I C A L C U R R E N T S E N S O R
3P C O N N E C T O R
V C C 2 S G 2
(YEL/BLU) (GRN)
Wire side of female terminals
```

**Is there about 5 V?**

*   **YES** — Replace the air pump electrical current sensor (see page 11-209).
*   **NO** — Go to step 8.

8. Measure voltage between ECM connector terminals C18 and C28.

```
ECM C O N N E C T O R C (31P)
S G 2
( G R N / Y E L )
1 2
/ 4 5
/ 8 9 10
11 12 13 14 15 16 17 18 19 20 21 22
/ 24 25 26 27 28 29 30
/
V C C 2
( Y E L / B L U )
Wire side of female terminals
```

**Is there about 5 V?**

*   **YES** — Repair open in the wire between the ECM (C18) and the air pump electrical current sensor.
*   **NO** — Substitute a known-good ECM (see page 11-5), then recheck. If voltage is normal, replace the original ECM (see page 11-115). B

11-207

---

### Printed page 11-208

<a id="p504"></a>
Source: [PDF p.504, printed p.11-208](../page-images/p0504.png).

# Pulsed Secondary Air Injection System
## Air Pump/Air Pump Relay Removal/Installation

1. Remove the front bumper; '00-03 models (see page 20-104), '04-05 models (see page 20-105).
2. Remove the air pump (A), and the air pump relay (B).
   - **Connector Label**: 2P connector (small)
3. Install the parts in the reverse order of removal.

**Page Reference**: 11-208

---

### Printed page 11-209

<a id="p505"></a>
Source: [PDF p.505, printed p.11-209](../page-images/p0505.png).

# Pulsed Secondary Air Injection System
## Air Pump Relay Test

Check continuity between **A1 and A2** of the large relay 2P connector. With power and ground connected to **B1 and B2** of the small relay 2P connector, there **should be continuity**. With power disconnected from the small connector, there **should be no continuity**. The source diagram shows terminal sides of male connectors.

## Air Pump Electrical Current Sensor Removal/Installation

1. Pull away left inner fender as needed (page 20-126).
2. Disconnect sensor 2P connector **A** and remove lower cover **B**; then disconnect sensor 3P connector **C**.
3. Remove sensor **D**.
4. Install in reverse order.

---

### Blank Source Scan

<a id="p506"></a>
Source: [PDF p.506, printed p.blank](../page-images/p0506.png).

# Blank Source Scan

No readable service content. The source page is almost entirely blank with a black scan artifact. The next page begins the 2006–2008 section.

---

### Printed page 11-211

<a id="p507"></a>
Source: [PDF p.507, printed p.11-211](../page-images/p0507.png).

# Fuel and Emissions Systems — 2006–2008 Contents

## Fuel and Emissions Systems
- Special Tools — 11-212
- General Troubleshooting Information — 11-213
- DTC Troubleshooting Index — 11-219
- Symptom Troubleshooting Index — 11-222
- System Description — 11-224
- How to Set Readiness Codes — 11-256

## PGM-FI System
- Component Location Index — 11-259
- DTC Troubleshooting — 11-261
- F-CAN Circuit Troubleshooting — 11-360
- MIL Circuit Troubleshooting — 11-366
- DLC Circuit Troubleshooting — 11-367
- Injector Replacement — 11-382
- MAP Sensor Replacement — 11-384
- IAT Sensor Replacement — 11-384
- ECT Sensor 1 Replacement — 11-385
- ECT Sensor 2 Replacement — 11-385
- A/F Sensor Replacement — 11-386
- Secondary HO2S Replacement — 11-386
- CMP Sensor Replacement — 11-387
- CKP Sensor Replacement — 11-387
- Output Shaft (Countershaft) Speed Sensor Replacement — 11-388
- Knock Sensor Replacement — 11-388
- ECM Replacement — 11-389

## Electronic Throttle Control System
- Component Location Index — 11-391
- DTC Troubleshooting — 11-392
- APP Sensor Signal inspection — 11-436
- APP Sensor Replacement — 11-437
- Throttle Actuator Control Module Replacement — 11-437

## VTEC
- Component Location Index — 11-438
- DTC Troubleshooting — 11-439
- Rocker Arm Oil Control Valve (VTEC Solenoid Valve) Removal/Installation — 11-449
- Rocker Arm Oil Pressure Switch (VTEC Oil Pressure Switch) Removal/Installation — 11-449

## Idle Control System
- Component Location Index — 11-450
- DTC Troubleshooting — 11-451
- A/C Signal Circuit Troubleshooting — 11-455
- Alternator FR Signal Circuit Troubleshooting — 11-456
- Electrical Power Steering (EPS) Signal Circuit Troubleshooting — 11-458
- Brake Pedal Position Switch Signal Circuit Troubleshooting — 11-460
- Idle Speed Inspection — 11-461
- ECM Idle Learn Procedure — 11-462

## Fuel Supply System
- Component Location Index — 11-463
- DTC Troubleshooting — 11-464
- Fuel Pump Circuit Troubleshooting — 11-470
- Fuel Pressure Relieving — 11-474
- Fuel Pressure Test — 11-477
- Fuel Tank Draining — 11-477
- Fuel Line Inspection — 11-478
- Fuel Line/Quick-Connect Fitting Precautions — 11-480
- Fuel Line/Quick-Connect Fitting Removal — 11-481
- Fuel Line/Quick-Connect Fitting Installation — 11-483
- Fuel Pulsation Damper Replacement — 11-485
- Fuel Pressure Regulator Replacement — 11-486
- Fuel Filter Replacement — 11-486
- Fuel Tank Unit Removal and Installation — 11-487
- Fuel Pump/Fuel Gauge Sending Unit Replacement — 11-488
- Fuel Tank Replacement — 11-489
- Fuel Gauge Sending Unit Test — 11-494
- Low Fuel Indicator Test — 11-496

## Intake Air System
- Component Location Index — 11-497
- Throttle Body Test — 11-498
- Throttle Body Cleaning — 11-499
- Throttle Body Removal/Installation — 11-500
- Throttle Body Disassembly/Reassembly — 11-501
- Accelerator Pedal Replacement — 11-502
- Throttle Cable Removal/Installation — 11-503
- Throttle Cable Adjustment — 11-504
- Air Cleaner Removal/Installation — 11-504
- Air Cleaner Element Inspection/Replacement — 11-505

## Catalytic Converter System
- Component Location Index — 11-506
- DTC Troubleshooting — 11-507

## PCV System
- Component Location Index — 11-509
- DTC Troubleshooting — 11-510
- PCV Valve Inspection — 11-511
- PCV Valve Replacement — 11-511

## EVAP System
- Component Location Index — 11-512
- DTC Troubleshooting — 11-514
- FTP Sensor Replacement — 11-542
- EVAP Canister Purge Valve Replacement — 11-542
- EVAP Canister Vent Shut Valve Replacement — 11-543
- EVAP Canister Replacement — 11-544
- Fuel Tank Vapor Control Float Replacement — 11-545

---

### Printed page 11-212

<a id="p508"></a>
Source: [PDF p.508, printed p.11-212](../page-images/p0508.png).

# Fuel and Emissions Systems — Special Tools

| Ref. | Tool number | Description | Qty |
|---|---|---|---:|
| 1 | 07AAJ-S6MA150 | Fuel pressure gauge attachment set | 1 |
| 2 | 07JAZ-001000B | Vacuum/pressure gauge, 0–4 in.Hg | 1 |
| 3 | 07SAZ-001000A | Backprobe set | 2 |
| 4 | 07NAJ-P07010A | Pressure gauge adapter | 1 |
| 5-1 | 07406-0020201 | A/T pressure hose | 1 |
| 5-2 | 07406-0070301 | A/T low-pressure gauge with panel | 1 |
| 5-3 | 07MAJ-PY4011A | A/T pressure hose, 2,210 mm | 1 |
| 5-4 | 07MAJ-PY40120 | A/T pressure hose adapter | 1 |
| 6 | 07406-004000B | Fuel pressure gauge | 1 |

The source image identifies the pictured tools by these reference numbers.

---

### Printed page 11-213

<a id="p509"></a>
Source: [PDF p.509, printed p.11-213](../page-images/p0509.png).

# General Troubleshooting Information
## Intermittent Failures
The term "intermittent failure" means a system may have had a failure, but it checks OK now. If the malfunction indicator lamp (MIL) on the dash does not come on, check for poor connections or loose terminals at all connectors related to the circuit that you are troubleshooting. If the MIL was on, but then went out, the original problem may have been intermittent.

## Service Information
Periodically, new ECM software or new service procedures may become available. Always check online for the latest software or service information related to the DTCs or symptoms you are troubleshooting.

## Opens and Shorts
"Open" and "short" are common electrical terms. An open is a break in a wire or at a connection. A short is an accidental connection of a wire to ground or to another wire. In simple electronics, this usually means something won't work at all. With complex electronics (such as ECMs) this can sometimes mean something works, but not the way it's supposed to.

## How to Use the HDS (Honda Diagnostic System)
If the MIL (malfunction indicator lamp) has come on
1. Start the engine, and check the MIL (A).
   NOTE: If the ignition switch is turned ON (II), and the engine is not started, the MIL will stay on for 15—20 seconds (see page 11-256).
2. If the MIL stays on, connect the HDS to the data link connector (DLC) (A) located behind the driver's side of the front console.
3. Turn the ignition switch ON (II).
4. Make sure the HDS communicates with the ECM and other vehicle systems. If it doesn't go to the DLC circuit troubleshooting (see page 11-367).
5. Check the diagnostic trouble code (DTC) and note it. Also check the freeze data and on-board snapshot data, and download any data found. Then refer to the indicated DTCs troubleshooting, and begin the appropriate troubleshooting procedure.
   NOTE:
   • Freeze data indicates the engine conditions when the first malfunction, misfire, or fuel trim malfunction was detected.
   • The HDS can read the DTC, freeze data, current data, and other engine control module (ECM) data.
   • For specific operations, refer to the user's manual that came with the HDS.
6. If no DTCs are found, go to MIL troubleshooting (see page 11-366).

If the MIL did not stay on
If the MIL did not stay on but there is a driveability problem, do the symptom troubleshooting.

If you can't duplicate the DTC
Some of the troubleshooting requires you to reset the ECM and try to duplicate the DTC. If the problem is intermittent and you can't duplicate the code, do not continue through the procedure. To do so will only result in confusion and possibly, a needlessly replaced ECM.

(cont'd)
11-213

---

### Printed page 11-214

<a id="p510"></a>
Source: [PDF p.510, printed p.11-214](../page-images/p0510.png).

# Fuel and Emissions Systems
## General Troubleshooting Information
### HDS Clear Command
The ECM stores various specific data to correct the system even if there is no electrical power such as when the battery negative terminal or No. 46 ACGS (15 A) fuse are disconnected.
Stored data based on failed parts should be cleared by using the "CLEAR COMMAND" of the HDS if parts are replaced.
The HDS has three kinds of clear commands to meet this purpose. They are DTC clear, ECM reset, and crank (CKP) pattern clear.
DTC clear command erases all stored DTC codes, freeze data, readiness codes, and the on-board snapshot. This must be done with the HDS after reproducing the DTC during troubleshooting.
The ECM reset command erases all stored DTC codes, freeze data, readiness codes, on-board snapshot, and all specific data to correct the system except crank (CKP) pattern. If the crank (CKP) pattern data in the ECM was cleared, you must do the crank (CKP) pattern learn procedure.
The crank (CKP) pattern clear command erases only crank (CKP) pattern data. This command is for repair of a misfire or the CKP sensor.

### Scan Tool Clear Command
If you are using a generic scan tool to clear commands, be aware that there is only one setting for clearing the ECM, and it clears all commands at the same time (crank (CKP) pattern learn, idle learn, readiness codes, freeze data, on-board snapshot, and DTCs). After you clear all commands, you then need to do these procedures, in this order: ECM idle learn procedure (see page 11-462); crank (CKP) pattern learn procedure; Test-drive to set readiness codes to complete (see page 11-256).

### DTC Clear
1. Clear the DTC with the HDS while the engine is stopped.
2. Turn the ignition switch OFF.
3. Turn the ignition switch ON (II), and wait 30 seconds.
4. Turn the ignition switch OFF, and disconnect the HDS from the DLC.
*(cont'd)*

### ECM Reset
1. Reset the ECM with the HDS while the engine is stopped.
2. Turn the ignition switch OFF.
3. Turn the ignition switch ON (II), and wait 30 seconds.
4. Turn the ignition switch OFF, and disconnect the HDS from the DLC.
5. Do the ECM idle learn procedure (see page 11-462).

### Crank (CKP) Pattern Clear/Crank (CKP) Pattern Learn
#### Clear/Learn Procedure (with the HDS)
1. Connect the HDS to the data link connector (DLC) (A) located behind the driver's side of the front console.
2. Turn the ignition switch ON (II).
3. Make sure the HDS communicates with the ECM and other vehicle systems. If it doesn't, go to the DLC circuit troubleshooting (see page 11-367).
4. Select CRANK PATTERN in the ADJUSTMENT MENU with the HDS.
5. Select CRANK PATTERN LEARNING with the HDS, and follow the screen prompts.

---

### Printed page 11-215

<a id="p511"></a>
Source: [PDF p.511, printed p.11-215](../page-images/p0511.png).

# Page 511: S2000 Fuel and Emissions Part C

## Learn Procedure (without the HDS)
1. Start the engine. Hold the engine speed at **3,000 rpm** without load (in neutral) until the radiator fan comes on.
2. Test-drive the vehicle on a level road: Decelerate (with the throttle fully closed) from an engine speed of **2,500 rpm** down to **1,000 rpm** with the transmission in 1st gear.
3. Repeat step 2 several times.
4. Turn the ignition switch OFF.
5. Turn the ignition switch ON (**II**), and wait **30 seconds**.

## How to End a Troubleshooting Session
*(required after any troubleshooting)*
1. Reset the ECM with the HDS.
2. Do the ECM idle learn procedure (see page **11-462**).
3. Turn the ignition switch OFF.
4. Disconnect the HDS from the DLC.

> **NOTE:** The ECM is part of the immobilizer system. If you replace the **ECM**, it will have a different immobilizer code. In order for the engine to start, you must rewrite the immobilizer code with the HDS.

## How to Troubleshoot Circuits at the ECM
### Special Tools Required
*   Digital multimeter **KS-AHM-32-003** (1) or a commercially available digital multimeter
*   Backprobe set **07SAZ-001000A** (2)

1. Connect the backprobe adapters (**A**) to the stacking patch cords (**B**), and connect the cords to a digital multimeter (**C**).
2. Using the wire insulation as a guide for the contoured tip of the backprobe adapter, gently slide the tip into the connector from the wire side until it touches the end of the wire terminal.
3. If you cannot get to the wire side of the connector or the wire side is sealed (**A**), disconnect the connector and probe the terminals (**B**) from the terminal side. Do not force the probe into the connector.

> **NOTICE:** Do not puncture the insulation on a wire. Punctures can cause poor or intermittent electrical connections.

**Diagram Labels:**
*   **A**: Backprobe adapter / Wire side seal
*   **B**: Stacking patch cord / Terminal side
*   **C**: Digital multimeter

*(cont'd)*

---

### Printed page 11-216

<a id="p512"></a>
Source: [PDF p.512, printed p.11-216](../page-images/p0512.png).

# Fuel and Emissions Systems
## General Troubleshooting Information
### Updating the ECM
#### Special Tools Required
* Honda diagnostic system (HDS) tablet tester
* Honda interface module (HIM) and an iN workstation with HDS and CM update software
* HDS pocket tester
* GNA-600 and an iN workstation with HDS and C M update software

Use any one of these update tools.

**NOTE:**
* Use this procedure when you need to update the E C M during troubleshooting procedures.
* Make sure the HDS/HIM has the latest software version.
* Before you update the E C M , make sure the battery in the vehicle is fully charged, and connect a jumper battery (not a battery charger) to maintain system voltage.
* Never turn the ignition switch O F F during the update. If there is a problem with the update, leave the ignition switch ON.
* To prevent E C M damage, do not operate anything electrical (headlights, audio system, brakes, A / C , power windows, door locks, etc.) during the update.
* To ensure the latest program is installed, do E C M update whenever the E C M is substituted or replaced.
* You cannot update E C M with a program it already has. It will only accept a new program.
* If you need to diagnose the Honda interface module (HIM) because the HIM's red (#3) light came on or was flashed during the update, leave the ignition switch in the ON (II) position when you disconnect the HIM from the data link connector (DLC). This will prevent E C M damage.

(cont'd)

1. Turn the ignition switch ON (II), but do not start the engine.
2. Connect the HDS to the data link connector (DLC) (A) located under the driver's side of the dashboard.
3. Make sure the HDS communicates with the E C M and other vehicle system. If it doesn't, go to the DLC circuit troubleshooting (see page 11-367). If you are returning from the DLC circuit troubleshooting, skip steps 4 and 5, then clean the throttle body after updating the E C M (see page 11-499).
4. Selectthe INSPECTION MENU with the HDS.
5. Select the E T C S TEST, then select the TP POSITION CHECK, and follow the screen prompts.

**NOTE:** If the TP POSITION CHECK indicates FAILED, continue this procedure.
6. Exit the HDS, then select the update mode, and follow the screen prompts to update the E C M .

11-216

---

### Printed page 11-217

<a id="p513"></a>
Source: [PDF p.513, printed p.11-217](../page-images/p0513.png).

# Fuel and Emissions Systems — General Troubleshooting Information

## Updating the ECM (continued)

7. If the software in the ECM is the latest, disconnect the HDS/HIM from the DLC, and go back to the procedure that you were doing. If the software in the ECM is not the latest, follow the instructions on the screen. If prompted to choose the PGM-FI system, make sure you update both.

**NOTE:** If the ECM update system requires you to cool the ECM, follow the screen prompts. If you run into a problem (programming takes over 15 minutes, status bar goes over 100 %, or immobilizer indicator flashes, HDS tablet freezes, etc.) during the update procedure, follow these steps to minimize the chance of damaging the ECM:
* Leave the ignition switch in the "ON (II)" position.
* Connect a jumper battery (do not connect a battery charger).
* Shut down the HDS.
* Disconnect the HDS from the DLC.
* Reboot the HDS.
* Reconnect the HDS to the DLC, and try the update procedure again.

8. If the TP POSITION CHECK failed in step 6, clean the throttle body (see page 11-499).
9. Do the ECM idle learn procedure (see page 11-462).
10. Do the crank (CKP) pattern learn procedure.

---

## Substituting the ECM

## Special Tools Required
* Honda diagnostic system (HDS) tablet tester
* Honda interface module (HIM) and an iN workstation with HDS and CM update software
* HDS pocket tester
* GNA-600 and an iN workstation with HDS and CM update software

Use any one of these update tools.

**NOTE:** Use this procedure when you need to substitute a known-good ECM during troubleshooting procedures.

1. Connect the HDS to the data link connector (DLC) (A) located behind the driver's side of the front console.
2. Turn the ignition switch ON (II).
3. Make sure the HDS communicates with the ECM and other vehicle systems. If it doesn't, go to the DLC circuit troubleshooting (see page 11-367). If you are returning from DLC circuit troubleshooting, skip steps 4 thru 10, then clean the throttle body after substituting the ECM (see page 11-499).
4. Select the INSPECTION MENU with the HDS.
5. Select the ETCS TEST, then select the TP POSITION CHECK, and follow the screen prompts.

**NOTE:** If the TP POSITION CHECK indicates FAILED, continue this procedure.
6. Turn the ignition switch OFF.
7. Jump the SCS line with the HDS.

---

---

### Printed page 11-218

<a id="p514"></a>
Source: [PDF p.514, printed p.11-218](../page-images/p0514.png).

# Fuel and Emissions Systems
## General Troubleshooting Information

8. Remove the left side kick panel (see page 20-71).
9. Disconnect the ECM connectors (A).
10. Remove the bolts (R), then remove the ECM (C).
11. Install the ECM in the reverse order of removal.
12. Open the SCS with the HDS.
13. Turn the ignition switch ON (II).

> **NOTE:** DTC P0630 "VIN Not Programmed or Mismatch" may be stored because the VIN has not been programmed into the ECM ; ignore it, and continue this procedure.

14. Manually input the VIN to the ECM with the HDS.
15. Update the ECM if it does not have the latest software.
16. Select the IMMOBI S Y S T E M with the HDS.
17. Enter the immobilizer code with the ECM replacement procedure in the HDS; it allows you to start the engine.
18. Reset the ECM with the HDS.
19. If the TP POSITION CHECK failed in step 5, clean the throttle body (see page 11-499).
20. Do the ECM idle learn procedure (see page 11-462).
21. Do the crank (CKP) pattern learn procedure.

*(cont'd)*

### OBD Status

The OBD status shows the current system status of each DTC and all of the parameters. This function is used to see if the repair was successfully completed.

The results of diagnostic tests for the DTC are displayed as:

*   **PASSED**: The on board diagnosis is successfully finished.
*   **FAILED**: The on board diagnosis has finished but failed.
*   **EXECUTING**: The vehicle is in enable criteria conditions for the DTC and the on board diagnosis is running.
*   **NOT COMPLETED**: The on board diagnosis w a s running but is out of the enable conditions of the DTC.
*   **O U T OF CONDITION**: The vehicle has stayed out of the enable conditions for the DTC.

**Page Reference:** 11-218

---

### Printed page 11-219

<a id="p515"></a>
Source: [PDF p.515, printed p.11-219](../page-images/p0515.png).

# Fuel and Emissions Systems — DTC Troubleshooting Index

A circle in the two-drive-cycle column is shown as **Yes**. The MIL column reports the printed ON/OFF state.

| DTC (MIL blink code) | Two-drive cycle | Detection item | MIL | Procedure |
|---|---|---|---|---|
| P0107 (3) | — | Manifold Absolute Pressure (MAP) Sensor Circuit Low Voltage | ON | 11-261 |
| P0108 (3) | — | Manifold Absolute Pressure (MAP) Sensor Circuit High Voltage | ON | 11-263 |
| P0111 (10) | Yes | Intake Air Temperature (IAT) Sensor Circuit Range/Performance Problem | ON | 11-266 |
| P0112 (10) | — | Intake Air Temperature (IAT) Sensor Circuit Low Voltage | ON | 11-267 |
| P0113 (10) | — | Intake Air Temperature (IAT) Sensor Circuit High Voltage | ON | 11-269 |
| P0116 (86) | Yes | Engine Coolant Temperature (ECT) Sensor 1 Circuit Range/Performance Problem | ON | 11-271 |
| P0117 (6) | — | Engine Coolant Temperature (ECT) Sensor 1 Circuit Low Voltage | ON | 11-272 |
| P0118 (6) | — | Engine Coolant Temperature (ECT) Sensor 1 Circuit High Voltage | ON | 11-274 |
| P0122 (7) | — | Throttle Position (TP) Sensor A Circuit Low Voltage | ON | 11-392 |
| P0123 (7) | — | Throttle Position (TP) Sensor A Circuit High Voltage | ON | 11-395 |
| P0125 (86) | Yes | Engine Coolant Temperature (ECT) Sensor 1 Malfunction/Slow Response | ON | 11-276 |
| P0128 (87) | Yes | Cooling System Malfunction | ON | 11-277 |
| P0133 (61) | Yes | Air Fuel Ratio (A/F) Sensor (Sensor 1) Slow Response | ON | 11-279 |
| P0134 (41) | Yes | Air Fuel Ratio (A/F) Sensor (Sensor 1) Heater System Malfunction | ON | 11-280 |
| P0135 (41) | — | Air Fuel Ratio (A/F) Sensor (Sensor 1) Heater Circuit Malfunction | ON | 11-281 |
| P0137 (63) | — | Secondary Heated Oxygen Sensor (secondary HO2S, sensor 2) Circuit Low Voltage | ON | 11-285 |
| P0138 (63) | — | Secondary Heated Oxygen Sensor (secondary HO2S, sensor 2) Circuit High Voltage | ON | 11-287 |
| P0139 (63) | Yes | Secondary Heated Oxygen Sensor (secondary HO2S, sensor 2) Slow Response | ON | 11-290 |
| P0141 (65) | — | Secondary Heated Oxygen Sensor (secondary HO2S, sensor 2) Heater Circuit Malfunction | ON | 11-291 |
| P0171 (45) | Yes | Fuel System Too Lean | ON | 11-294 |
| P0172 (45) | Yes | Fuel System Too Rich | ON | 11-294 |
| P0222 (7) | — | Throttle Position (TP) Sensor B Circuit Low Voltage | ON | 11-398 |
| P0223 (7) | — | Throttle Position (TP) Sensor B Circuit High Voltage | ON | 11-401 |
| P0300 (75) | Yes | Random Misfire Detected (any combination of P0301–P0304) | ON | 11-295 |
| P0301 (71) | Yes | No. 1 Cylinder Misfire Detected | ON | 11-298 |
| P0302 (72) | Yes | No. 2 Cylinder Misfire Detected | ON | 11-298 |
| P0303 (73) | Yes | No. 3 Cylinder Misfire Detected | ON | 11-298 |
| P0304 (74) | Yes | No. 4 Cylinder Misfire Detected | ON | 11-298 |
| P0325 (23) | — | Knock Sensor Circuit Malfunction | ON | 11-306 |
| P0335 (4) | — | Crankshaft Position (CKP) Sensor No Signal | ON | 11-308 |
| P0339 (4) | — | Crankshaft Position (CKP) Sensor Circuit Intermittent Interruption | ON | 11-310 |
| P0365 (8) | — | Camshaft Position (CMP) Sensor No Signal | ON | 11-311 |
| P0369 (8) | — | Camshaft Position (CMP) Sensor Circuit Intermittent Interruption | ON | 11-313 |
| P0420 (67) | Yes | Catalyst System Efficiency Below Threshold | ON | 11-507 |
| P0443 (92) | — | Evaporative Emission (EVAP) Canister Purge Valve Circuit Malfunction | ON | 11-514 |

*The parenthesized number is the MIL blink indication when the SCS line is jumped with the HDS.*

---

### Printed page 11-220

<a id="p516"></a>
Source: [PDF p.516, printed p.11-220](../page-images/p0516.png).

# Fuel and Emissions Systems — DTC Troubleshooting Index

A circle in the two-drive-cycle column is shown as **Yes**. The MIL column reports the printed ON/OFF state.

| DTC (MIL blink code) | Two-drive cycle | Detection item | MIL | Procedure |
|---|---|---|---|---|
| P0451 (91) | Yes | Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem | ON | 11-518 |
| P0452 (91) | — | Fuel Tank Pressure (FTP) Sensor Circuit Low Voltage | ON | 11-519 |
| P0453 (91) | — | Fuel Tank Pressure (FTP) Sensor Circuit High Voltage | ON | 11-522 |
| P0455 (90) | Yes | Evaporative Emission (EVAP) System Large Leak Detected | ON | 11-525 |
| P0456 (90) | Yes | Evaporative Emission (EVAP) System Very Small Leak Detected | ON | 11-525 |
| P0457 (90) | Yes | Evaporative Emission (EVAP) System Leak Detected/Fuel Fill Cap Loose or Missing | ON | 11-528 |
| P0461 (121) | — | Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Range/Performance Problem | OFF | 11-464 |
| P0462 (121) | — | Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Low Voltage | OFF | 11-465 |
| P0463 (121) | — | Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit High Voltage | OFF | 11-467 |
| P0496 (92) | Yes | Evaporative Emission (EVAP) System High Purge Flow Detected | ON | 11-530 |
| P0497 (90) | Yes | Evaporative Emission (EVAP) System Low Purge Flow Detected | ON | 11-531 |
| P0498 (117) | — | Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit Low Voltage | ON | 11-534 |
| P0499 (117) | — | Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit High Voltage | ON | 11-536 |
| P0506 (14) | Yes | Idle Control System RPM Lower Than Expected | ON | 11-451 |
| P0507 (14) | Yes | Idle Control System RPM Higher Than Expected | ON | 11-453 |
| P0563 (34) | — | Engine Control Module (ECM) Power Source Circuit Unexpected Voltage | OFF | 11-314 |
| P0600 (39) | — | Serial Communication Link Malfunction | ON | 11-317 |
| P0602 (196) | — | Engine Control Module (ECM) Programming Error | ON | 11-317 |
| P0603 (131) | — | Engine Control Module (ECM) Internal Control Module Keep Alive Memory (KAM) Error | ON | 11-318 |
| P0606 (0) | — | Engine Control Module (ECM) Processor Malfunction | ON | 11-318 |
| P0630 (139) | — | VIN Not Programmed or Mismatch | ON | 11-319 |
| P0685 (135) | Yes | Engine Control Module (ECM) Power Control Circuit/Internal Circuit Malfunction | ON | 11-320 |
| P0720 (122) | — | Output Shaft (Countershaft) Speed Sensor Circuit Malfunction | ON | 11-321 |
| P1109 (13) | — | Barometric Pressure (BARO) Sensor Circuit Out of Range High | ON | 11-324 |
| P1116 (86) | Yes | Engine Coolant Temperature (ECT) Sensor 1 Circuit Range/Performance Problem | ON | 11-325 |
| P1128 (5) | Yes | Manifold Absolute Pressure (MAP) Sensor Signal Lower Than Expected | ON | 11-327 |
| P1129 (5) | Yes | Manifold Absolute Pressure (MAP) Sensor Signal Higher Than Expected | ON | 11-328 |
| P1157 (48) | — | Air Fuel Ratio (A/F) Sensor (Sensor 1) AFS Circuit High Voltage | ON | 11-330 |
| P1172 (61) | — | Air Fuel Ratio (A/F) Sensor (Sensor 1) Circuit Out of Range High | ON | 11-333 |

*The parenthesized number is the MIL blink indication when the SCS line is jumped with the HDS.*

---

### Printed page 11-221

<a id="p517"></a>
Source: [PDF p.517, printed p.11-221](../page-images/p0517.png).

# Fuel and Emissions Systems — DTC Troubleshooting Index

A circle in the two-drive-cycle column is shown as **Yes**. The MIL column reports the printed ON/OFF state.

| DTC (MIL blink code) | Two-drive cycle | Detection item | MIL | Procedure |
|---|---|---|---|---|
| P1297 (20) | — | Electrical Load Detector (ELD) Circuit Low Voltage | OFF | 11-334 |
| P1298 (20) | — | Electrical Load Detector (ELD) Circuit High Voltage | OFF | 11-336 |
| P1454 (91) | Yes | Fuel Tank Pressure (FTP) Sensor Range/Performance Problem | ON | 11-539 |
| P1683 (40) | — | Throttle Valve Default Position Spring Performance Problem | ON | 11-404 |
| P1684 (40) | — | Throttle Valve Return Spring Performance Problem | ON | 11-405 |
| P2101 (40) | — | Throttle Actuator System Malfunction | ON | 11-406 |
| P2108 (40) | — | Throttle Actuator Control Module Problem | ON | 11-408 |
| P2118 (40) | — | Throttle Actuator Current Range/Performance Problem | ON | 11-409 |
| P2122 (37) | — | Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Circuit Low Voltage | ON | 11-411 |
| P2123 (37) | — | Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Circuit High Voltage | ON | 11-414 |
| P2127 (37) | — | Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Circuit Low Voltage | ON | 11-416 |
| P2128 (37) | — | Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Circuit High Voltage | ON | 11-419 |
| P2135 (7) | — | Throttle Position (TP) Sensor A/B Incorrect Voltage Correlation | ON | 11-421 |
| P2138 (37) | — | Accelerator Pedal Position (APP) Sensor A/B (Throttle Position (TP) Sensor D/E) Incorrect Voltage Correlation | ON | 11-423 |
| P2176 (40) | — | Throttle Actuator Control System Idle Position Not Learned | ON | 11-425 |
| P2183 (192) | Yes | Engine Coolant Temperature (ECT) Sensor 2 Circuit Range/Performance Problem | ON | 11-338 |
| P2184 (192) | — | Engine Coolant Temperature (ECT) Sensor 2 Circuit Low Voltage | ON | 11-340 |
| P2185 (192) | — | Engine Coolant Temperature (ECT) Sensor 2 Circuit High Voltage | ON | 11-342 |
| P2195 (48) | — | Air Fuel Ratio (A/F) Sensor (Sensor 1) Signal Stuck Lean | ON | 11-345 |
| P2227 (13) | Yes | Barometric Pressure (BARO) Sensor Circuit Range/Performance Problem | ON | 11-347 |
| P2228 (13) | — | Barometric Pressure (BARO) Sensor Circuit Low Voltage | ON | 11-349 |
| P2229 (13) | — | Barometric Pressure (BARO) Sensor Circuit High Voltage | ON | 11-349 |
| P2238 (48) | — | Air Fuel Ratio (A/F) Sensor (Sensor 1) AFS + Circuit Low Voltage | ON | 11-350 |
| P2252 (48) | — | Air Fuel Ratio (A/F) Sensor (Sensor 1) AFS — Circuit Low Voltage | ON | 11-352 |
| P2270 (63) | Yes | Secondary Heated Oxygen Sensor (secondary HO2S, sensor 2) Circuit Signal Stuck Lean | ON | 11-354 |
| P2271 (63) | Yes | Secondary Heated Oxygen Sensor (secondary HO2S, sensor 2) Circuit Signal Stuck Rich | ON | 11-354 |
| P2279 (109) | Yes | Intake Air System Leak Detected | ON | 11-510 |
| P2422 (117) | Yes | Evaporative Emission (EVAP) Canister Vent Shut Valve Stuck Closed Malfunction | ON | 11-539 |
| P2552 (40) | — | Throttle Actuator Control Module Relay Malfunction | ON | 11-427 |
| P2610 (132) | — | Engine Control Module (ECM) Ignition Off Internal Timer Performance Problem | ON | 11-355 |
| P2646 (22) | — | Rocker Arm Oil Pressure Switch (VTEC Oil Pressure Switch) Circuit Low Voltage | ON | 11-439 |
| P2647 (22) | — | Rocker Arm Oil Pressure Switch (VTEC Oil Pressure Switch) Circuit High Voltage | ON | 11-442 |
| P2648 (21) | — | Rocker Arm Oil Control Solenoid (VTEC Solenoid Valve) Circuit Low Voltage | ON | 11-445 |
| P2649 (21) | — | Rocker Arm Oil Control Solenoid (VTEC Solenoid Valve) Circuit High Voltage | ON | 11-447 |
| P2A00 (61) | Yes | Air Fuel Ratio (A/F) Sensor (Sensor 1) Circuit Range/Performance Problem | ON | 11-356 |
| U0107 (30) | — | Lost Communication With Throttle Actuator Control Module | ON | 11-429 |
| U0122 (126) | — |  | OFF | 11-357 |
| U1102 (126) | — | F-CAN Malfunction (BUS-) | OFF | 11-359 |

*The parenthesized number is the MIL blink indication when the SCS line is jumped with the HDS.*

---

### Printed page 11-222

<a id="p518"></a>
Source: [PDF p.518, printed p.11-222](../page-images/p0518.png).

# Fuel and Emissions Systems
## Symptom Troubleshooting Index

When the vehicle has one of these symptoms, check for a diagnostic trouble code (DTC) with the HDS. If there is no DTC, do the diagnostic procedure for the symptom, in the sequence listed, until you find the cause.

### Engine will not start
#### (MIL works OK, no DTCs set)
1. Test the battery (see page 22-47).
2. Test the starter (see page 4-10).
3. Check the fuel pressure (see page 11-477).
4. Troubleshoot the fuel pump circuit (see page 11-470).

*Possible causes:*
* Low compression
* No ignition spark
* Intake air leaks
* Locked up engine
* Broken cam chain
* Contaminated fuel

### Engine will not start
#### (MIL works OK, no DTCs set, immobilizer indicator stays on or flashes)
Check the immobilizer system (see page 22-213).

### MIL comes on and stays on, or never comes on at all, no DTCs set
Troubleshoot the MIL circuit (see page 11-366).

### Engine starts but stalls immediately
#### (MIL works OK, no DTCs set, immobilizer indicator stays on or flashes)
Check the immobilizer system (see page 22-213).

### Engine is hard to start
#### (MIL works OK, no DTCs set)
1. Test the battery (see page 22-47).
2. Check the fuel pressure (see page 11-477).
3. Clean the throttle body (see page 11-499).

*Possible causes:*
* Low compression
* Intake air leaks
* Contaminated fuel
* Weak spark

### Cold fast idle too low
#### (MIL works OK, no DTCs set)
1. Do the ECM idle learn procedure (see page 11-462).
2. Check the idle speed (see page 11-461).
3. Clean the throttle body (see page 11-499).

### Cold fast idle too high
#### (MIL works OK, no DTCs set)
1. Do the ECM idle learn procedure (see page 11-462).
2. Check the idle speed (see page 11-461).
3. Adjust the throttle cable (see page 11-504).
4. Do the throttle position learning check (see page 11-498).

### Intake air leaks
#### Idle speed fluctuates
(MIL works OK, no DTCs set)
1. Do the ECM idle learn procedure (see page 11-462).
2. Check the idle speed (see page 11-461).
3. Adjust the throttle cable (see page 11-504).
4. Do the carbon accumulation check (see page 11-498).
5. Troubleshoot the A/C signal circuit (see page 11-455).

### Incorrect valve timing or clearance adjustment
#### After warming up, idle speed is below specification without load
(MIL works OK, no DTCs set)
1. Troubleshoot the alternator FR signal circuit (see page 11-456).
2. Do the carbon accumulation check (see page 11-498).

### Incorrect valve timing or clearance adjustment
#### After warming up, idle speed is above specification without load
(MIL works OK, no DTCs set)
1. Adjust the throttle cable (see page 11-504).
2. Troubleshoot the alternator FR signal circuit (see page 11-456).
3. Inspect the APP sensor (see page 11-436).
4. Troubleshoot the A/C signal circuit (see page 11-455).
5. Troubleshoot the EPS signal circuit (see page 11-458).

*Possible causes:*
Intake air leaks

---
**Page Reference:** 11-222

---

### Printed page 11-223

<a id="p519"></a>
Source: [PDF p.519, printed p.11-223](../page-images/p0519.png).

# S2000 Fuel and Emissions Part C - Page 519

## Symptom Diagnostic procedure

### Low power
**(MIL works OK, no DTCs set)**
1. Check the fuel pressure (see page 11-477).
2. Adjust the throttle cable (see page 11-504).
*   Low compression
*   Incorrect camshaft timing
*   Incorrect engine oil level

### Engine stalls
**(MIL works OK, no DTCs set)**
1. Do the E C M idle learn procedure (see page 11-462).
2. Check the fuel pressure (see page 11-477).
3. Check the idle speed (see page 11 -461).
4. Troubleshoot the brake pedal position switch signal circuit (see page 11 -460).
*   Intake air leaks
*   Faulty harness and sensor connections
*   Fuel contamination

### Difficult to refuel
**(MIL works OK, no DTCs set)**
1. Check the fuel vent tube between the EVAP canister and the fuel tank.
2. Check the fuel tank vapor recirculation tube between the fuel pipe and the fuel tank.
3. Replace the fuel tank vapor control float (see page 11-545).

### Fuel overflows during refueling
**(No DTCs set)**
Replace the fuel tank vapor control float (see page 11-545).

### Malfunctioning gas station filling nozzle.

### HDS does not communicate with the ECM or the vehicle
Troubleshoot the DLC circuit (see page 11-367).

**Page Reference:** 11-223

---

### Printed page 11-224

<a id="p520"></a>
Source: [PDF p.520, printed p.11-224](../page-images/p0520.png).

# Fuel and Emissions Systems
## System Description
### Electronic Control System
The fuel and emission control systems are managed by the engine control module (ECM).

### Self-diagnosis
The ECM detects a failure of a signal from a sensor or from another control unit and stores a Temporary DTC or a DTC.
Depending on the failure, a DTC is stored in either the first or the second drive cycle. When a DTC is stored, the ECM turns on the malfunction indicator lamp (MIL) by supplying ground to the MIL circuit.

#### One Drive Cycle Detection Method
When an abnormality occurs in the signal from a sensor or from another control unit, the ECM stores a DTC and turns on the MIL immediately.

#### Two Drive Cycle Detection Method
When an abnormality occurs in the signal from a sensor or from another control unit in the first drive cycle, the ECM stores a Temporary DTC. The MIL does not come on at this time. If the failure continues in the second drive cycle, the ECM stores a DTC in erasable memory and turns on the MIL.

### Fail-safe Function
When an abnormality occurs in the signal from a sensor or from another control unit, the ECM ignores that signal and substitutes a pre-programmed value that allows the engine to continue running. This causes a DTC to be stored and the MIL to come on.

### MIL Bulb Check and Readiness Code Condition
When the ignition switch is turned ON (II), the ECM supplies ground to the MIL circuit for about 15 to 20 seconds to check the bulb condition. If any readiness codes are not set to complete, the MIL flashes five times. If all readiness codes are set to complete, the MIL goes off.

### Self Shut Down (SSD) Mode
After the ignition switch is turned OFF, the ECM stays on (up to 25 minutes). If the ECM connector is disconnected during this time, the ECM may be damaged. To cancel this mode, disconnect the negative cable from the battery or jump the SCS line with the HDS after the ignition switch is turned OFF.

**Page Reference:** 11-224

---

### Printed page 11-225

<a id="p521"></a>
Source: [PDF p.521, printed p.11-225](../page-images/p0521.png).

# Fuel and Emissions Systems — ECM Electrical Connections

This is the first sheet of the ECM wiring schematic. It shows battery feed through the under-hood and under-dash fuse/relay boxes to the ignition switch, PGM-FI main relays, fuel pump, ignition coil relay, throttle actuator control module relay, A/F sensor relay, starter cut relay, IG2 cut relay, and ECM. The left side identifies A/C compressor clutch, condenser fan, and radiator fan relays. Fuse ratings and model-year footnotes are printed in the source image. **Use the schematic image for wiring paths and terminal locations**; this text is an index, not a substitute for the diagram.

---

### Printed page 11-226

<a id="p522"></a>
Source: [PDF p.522, printed p.11-226](../page-images/p0522.png).

# Fuel and Emissions Systems — ECM Electrical Connections (continued)

The schematic shows No. 1–4 injectors to ECM **B5 INJ1, B4 INJ2, B3 INJ3, B2 INJ4**; immobilizer unit to **E27 IMOCD**; CMP sensor to **A6 CMP**; CKP sensor to **A7 CKP**; MAP sensor to **A21 VCC1, A30 MAP, A24 SG1**; IAT sensor to **B17 IAT**; ECT sensor 1 to **B8 ECT1**; ECT sensor 2 to **E1 ECT2**; and knock sensor to **A1 KS**. The BARO sensor is built into the ECM. **Use the source schematic for physical connections and paths.**

---

### Printed page 11-227

<a id="p523"></a>
Source: [PDF p.523, printed p.11-227](../page-images/p0523.png).

# Fuel and Emissions Systems — ECM Electrical Connections (continued)

The schematic includes EVAP canister purge valve (**B21 PCS**), EVAP vent shut valve (**E19 VSV**), alternator (**B10 ALTL, B13 ALTF, B18 ALTC**), four ignition coils (**A16/A15/A14/A13 IGPLS1–4**), A/F sensor 1 (**A10 AFSHTC, A31 AFS+, A28 AFS−**), secondary HO2S sensor 2 (**E20 SHO2S, E21 SO2SHTC**), VTEC oil pressure switch (**B11 VTPSW**), VTEC solenoid (**B6 VTS**), and output shaft speed sensor (**A18 NC**). **Refer to the source schematic for wiring paths.**

---

### Printed page 11-228

<a id="p524"></a>
Source: [PDF p.524, printed p.11-228](../page-images/p0524.png).

# Fuel and Emissions Systems — ECM Electrical Connections (continued)

The schematic includes FTP sensor (**E5 VCC3, E14 FTP, E4 SG3**), gauge assembly, test tachometer connector, data link connector, throttle actuator control module, TP sensor, throttle actuator, cruise switches, brake and clutch pedal position switches, A/C pressure switch, EPS control unit, steering angle sensor, VSA modulator-control unit, and APP sensor A/B (**A26 APSA, A25 APSB**). Connector terminal location drawings for ECM A (31P), B (24P), D (17P), and E (31P) are at the bottom of the source page. **Refer to the source schematic for wiring paths.**

---

### Printed page 11-229

<a id="p525"></a>
Source: [PDF p.525, printed p.11-229](../page-images/p0525.png).

# ECM Inputs and Outputs at Connector A (31P)

## Diagram Labels
KS, IGP2, IGP1, PG2, PG1, CMP, CKP, LG2, LG1, AFS HTC, IGPLS4, IGPLS3, IGPLS2, IGPLS1, NC, VCC2, VCC1, SG2, SG1, APSB, APSA, AFS- / 30, AFS+

## Safety Note
NOTE: Standard battery voltage is about 12 V.

## Terminal Data Table

| Terminal Number | Wire Color | Terminal Name | Description | Signal |
| :--- | :--- | :--- | :--- | :--- |
| 1 | RED/BLU | KS (KNOCK SENSOR) | Detects knock sensor signal | With engine knocking: pulses |
| 2 | YEL/BLK | IGP2 (POWER SOURCE) | Power source for ECM circuit | With ignition switch ON (II): battery voltage<br>With ignition switch OFF: about 0 V |
| 3 | YEL/BLK | IGP1 (POWER SOURCE) | Power source for ECM circuit | With ignition switch ON (II): battery voltage<br>With ignition switch OFF: about 0 V |
| 4 | BLK | PG2 (POWER GROUND) | Ground circuit for ECM | Less than 1.0 V at all times |
| 5 | BLK | PG1 (POWER GROUND) | Ground circuit for ECM | Less than 1.0 V at all times |
| 6 | GRN | CMP (CAMSHAFT POSITION SENSOR) | Detects CMP sensor signal | With engine running: pulses<br>With ignition switch ON (II): about 5.0 V |
| 7 | BLU | CKP (CRANKSHAFT POSITION SENSOR) | Detects CKP sensor signal | With engine running: pulses<br>With ignition switch ON (II): about 5.0 V |
| 8 | BRN/YEL | LG2 (LOGIC GROUND) | Ground circuit for ECM | Less than 1.0 V at all times |
| 9 | BRN/YEL | LG1 (LOGIC GROUND) | Ground circuit for ECM | Less than 1.0 V at all times |
| 10 | GRN | AFS HTC (AIR FUEL RATIO (A/F) SENSOR HEATER CONTROL) | Drives A/F sensor heater | With ignition switch ON (II): battery voltage<br>With fully warmed up engine running: about 0 V |
| 13 | WHT/BLU | IGPLS4 (No. 4 IGNITION COIL PULSE) | Drives No. 4 ignition coil | With ignition switch ON (II): about 0 V<br>With engine running: pulses |
| 14 | WHT/BLK | IGPLS3 (No. 3 IGNITION COIL PULSE) | Drives No. 3 ignition coil | With ignition switch ON (II): about 0 V<br>With engine running: pulses |
| 15 | WHT/GRN | IGPLS2 (No. 2 IGNITION COIL PULSE) | Drives No. 2 ignition coil | With ignition switch ON (II): about 0 V<br>With engine running: pulses |
| 16 | WHT | IGPLS1 (No. 1 IGNITION COIL PULSE) | Drives No. 1 ignition coil | With ignition switch ON (II): about 0 V<br>With engine running: pulses |
| 18 | BLU/WHT | NC (OUTPUT SHAFT (COUNTERSHAFT) SPEED SENSOR) | Detects output shaft (countershaft) speed sensor signal | With ignition switch ON (II): about 0 V or 5.0 V<br>While driving: about 2.5 V |

## Page Reference
11-229

---

### Printed page 11-230

<a id="p526"></a>
Source: [PDF p.526, printed p.11-230](../page-images/p0526.png).

# Fuel and Emissions Systems
## System Description (cont'd)
### ECM Inputs and Outputs at Connector A (31P)

**Wire side of female terminals**

> **NOTE:** Standard battery voltage is about 12 V.

| Terminal number | Wire color | Terminal name | Description |
| :--- | :--- | :--- | :--- |
| 20 | YEL/BLU | VCC2 (SENSOR VOLTAGE) | Provides sensor voltage<br>With ignition switch ON (II): about 5.0 V<br>With ignition switch OFF: about 0 V |
| 21 | YEL/RED | VCC1 (SENSOR VOLTAGE) | Provides sensor voltage<br>With ignition switch ON (II): about 5.0 V<br>With ignition switch OFF: about 0 V |
| 23 | GRN/YEL | SG2 (SENSOR GROUND) | Sensor ground<br>Less than 1.0 V at all times |
| 24 | GRN/WHT | SG1 (SENSOR GROUND) | Sensor ground<br>Less than 1.0 V at all times |
| 25 | RED/YEL | APSB (ACCELERATOR PEDAL POSITION (APP) SENSOR B) | Detects APP sensor B signal<br>With ignition switch ON (II) and accelerator pedal pressed: about 2.3 V<br>With ignition switch ON (II) and accelerator pedal released: about 0.2 V |
| 26 | RED/BLU | APSA (ACCELERATOR PEDAL POSITION (APP) SENSOR A) | Detects APP sensor A signal<br>With ignition switch ON (II) and accelerator pedal pressed: about 4.5 V<br>With ignition switch ON (II) and accelerator pedal released: about 0.5 V |
| 28 | RED/YEL | AFS- (AIR FUEL RATIO (A/F) SENSOR, SENSOR 1 - SIDE) | Detects A/F sensor (sensor 1) signal |
| 30 | GRN/RED | MAP (MANIFOLD ABSOLUTE PRESSURE SENSOR) | Detects MAP sensor signal<br>With ignition switch ON (II): about 3.0 V<br>At idle: about 1.0 V (depending on engine speed) |
| 31 | RED | AFS+ (AIR FUEL RATIO (A/F) SENSOR, SENSOR 1 +SIDE) | Detects A/F sensor (sensor 1) signal |

*Source page reference: 11-230*

---

### Printed page 11-231

<a id="p527"></a>
Source: [PDF p.527, printed p.11-231](../page-images/p0527.png).

# S2000 Fuel and Emissions Part C
## Page 527: Wire side of female terminals

> **NOTE:** Standard battery voltage is about 12 V.

| Terminal number | Wire color | Terminal name | Description | Signal |
| :--- | :--- | :--- | :--- | :--- |
| 2 | YEL | INJ4 (No. 4 INJECTOR) | Drives No. 4 injector | At idle: duty controlled<br>With ignition switch ON (II): battery voltage |
| 3 | BLU | INJ3 (No. 3 INJECTOR) | Drives No. 3 injector | At idle: duty controlled<br>With ignition switch ON (II): battery voltage |
| 4 | RED | INJ2 (No. 2 INJECTOR) | Drives No. 2 injector | At idle: duty controlled<br>With ignition switch ON (II): battery voltage |
| 5 | BRN | INJ1 (No. 1 INJECTOR) | Drives No. 1 injector | At idle: duty controlled<br>With ignition switch ON (II): battery voltage |
| 6 | GRN/YEL | VTS (ROCKER ARM OIL CONTROL SOLENOID (VTEC SOLENOID VALVE)) | Drives rocker arm oil control solenoid (VTEC solenoid valve) | At idle: about 0 V |
| 8 | RED/WHT | ECT1 (ENGINE COOLANT TEMPERATURE SENSOR 1) | Detects ECT sensor 1 signal | With ignition switch ON (II): about 0.1—4.8 V (depending on engine coolant temperature)<br>With fully warmed up engine: about 0.5—0.7 V |
| 10 | WHT/BLU | ALTL (ALTERNATOR L SIGNAL) | Detects alternator signal | With ignition switch ON (II): about 0 V<br>With engine running: battery voltage |
| 11 | BLU/BLK | VTPSW (ROCKER ARM OIL PRESSURE SWITCH (VTEC OIL PRESSURE SWITCH)) | Detects rocker arm oil pressure switch (VTEC oil pressure switch) signal | With engine at low rpm: about 0 V<br>With engine at high rpm: battery voltage |
| 13 | WHT/RED | ALTF (ALTERNATOR FR SIGNAL) | Detects alternator FR signal | With engine running: about 0—5.0 V (depending on electrical load) |
| 17 | RED/YEL | IAT (INTAKE AIR TEMPERATURE SENSOR) | Detects IAT sensor signal | With ignition switch ON (II): about 0.1—4.8 V (depending on intake air temperature) |
| 18 | WHT/GRN | ALTC (ALTERNATOR CONTROL) | Sends alternator control signal | With fully warmed up engine running: about 8.0 V |
| 19 | GRN | SEFD (THROTTLE ACTUATOR CONTROL SERIAL SIGNAL) | Sends throttle actuator control serial signal | |
| 20 | BLU | SEDF (THROTTLE ACTUATOR CONTROL SERIAL SIGNAL) | Detects throttle actuator control serial signal | |
| 21 | YEL/BLU | PCS (EVAPORATIVE EMISSION CANISTER PURGE VALVE) | Drives EVAP canister purge valve | With engine running, engine coolant below 149 °F (65 °C): battery voltage<br>With engine running, engine coolant above 149 °F (65 °C): duty controlled |

*Page reference: 11-231*

---

### Printed page 11-232

<a id="p528"></a>
Source: [PDF p.528, printed p.11-232](../page-images/p0528.png).

# Fuel and Emissions Systems
## System Description (cont'd)
### ECM Inputs and Outputs at Connector D (17P)
**Wire side of female terminals**

> **NOTE:** Standard battery voltage is about 12 V.

| Terminal number | Wire color | Terminal name | Description | Signal |
| :--- | :--- | :--- | :--- | :--- |
| 1 | LT GRN/RED | C C S E T S W (CRUISE CONTROL S E T SWITCH) | Detects cruise S E T switch signal | With cruise S E T switch ON: about 0 V<br>With cruise S E T switch OFF: battery voltage |
| 4 | L T G R N | CCMSW (CRUISE CONTROL MAIN SWITCH) | Detects cruise MAIN switch signal | With cruise MAIN switch ON: about 0 V<br>With cruise MAIN switch OFF: battery voltage |
| 7 | LT GRN/BLK | C C R E S S W (CRUISE CONTROL RES SWITCH) | Detects cruise R E S switch signal | With cruise RES switch ON: about 0 V<br>With cruise RES switch OFF: battery voltage |
| 8 | GRY | BKSWNC (BRAKE PEDAL POSITION SWITCH) | Detects brake pedal position switch signal | With ignition switch ON (II) and brake pedal released: battery voltage<br>With ignition switch ON (II) and brake pedal pressed: about 5.0 V |
| 9 | PNK | CCCLSW (CRUISE CONTROL CLUTCH PEDAL POSITION SIGNAL) | Detects cruise control clutch pedal position switch signal | With ignition switch ON (II) and clutch pedal released: about 5.0 V<br>With ignition switch ON (II) and clutch pedal pressed: battery voltage |
| 15 | BRN | ETCSRLY (THROTTLE ACTUATOR CONTROL MODULE RELAY) | Drives throttle actuator control module relay | With ignition switch ON (II): about 0 V |

*Page reference: 11-232*

---

### Printed page 11-233

<a id="p529"></a>
Source: [PDF p.529, printed p.11-233](../page-images/p0529.png).

# ECM Inputs and Outputs at Connector E (31P)

**Wire side of female terminals**

| Terminal number | Wire color | Terminal name | Description | Signal |
| :--- | :--- | :--- | :--- | :--- |
| 1 | BLU | ECT2 (ENGINE COOLANT TEMPERATURE SENSOR 2) | Detect ECT sensor 2 signal | With ignition switch ON (II): about 0.1—4.8 V (depending on engine coolant temperature) |
| 3 | GRN/WHT | LG3 (LOGIC GROUND) | Ground for ECM control circuit | Less than 1.0 V at all times |
| 4 | GRN | SG3 (SENSOR GROUND) | Sensor ground | Less than 1.0 V at all times |
| 5 | YEL/BLU | VCC3 (SENSOR VOLTAGE) | Provides sensor voltage | With ignition switch ON (II): about 5.0 V<br>With ignition switch OFF: about 0 V |
| 7 | GRN | MRLY (PGM-FI MAIN RELAY 1 (FL MAIN)) | Drives PGM-FI main relay 1 (FL MAIN)<br>Power source for DTC memory | With ignition switch ON (II): about 0 V<br>With ignition switch OFF: battery voltage |
| 8 | ORN | AFSHTCR (AIR FUEL RATIO (A/F) SENSOR HEATER CONTROL RELAY) | Drives A/f sensor heater relay | With ignition switch ON (II): about 0 V |
| 9 | BLK/YEL | IG1 (IGNITION SIGNAL) | Detects ignition signal | With ignition switch ON (II): battery voltage<br>With ignition switch OFF: about 0 V |
| 11 | RED | CANH (CAN COMMUNICATION SIGNAL HIGH) | Sends communication signal | With ignition switch ON (II): pulses |
| 12 | GRN | FANC (RADIATOR FAN CONTROL) | Drives radiator fan relay | With radiator fan running: about 0 V<br>With radiator fan stopped: battery voltage |
| 13 | YEL | SEFMJ | Communicates with multiplex control unit | With ignition switch ON (II): about 5.0 V<br>With engine running with load: pulses |
| 14 | L T G R N | FTP (FUELTANK PRESSURE (FTP) SENSOR) | Detects FTP sensor signal | With ignition switch ON (II) and fuel fill cap removed: about 2.5 V |
| 15 | GRN/RED | ELD (ELECTRICAL LOAD DETECTOR) | Detects ELD signal | With ignition switch ON (II): about 0.1—4.8 V (depending on electrical load) |
| 16 | BLU/BLK | EPSLD (ELECTRICAL P/S LOAD DETECT) | Detects P/S load signal | At idle with steering wheel straight ahead: about 0 V<br>At idle with steering wheel at full lock: battery voltage |
| 17 | GRN/YEL | IMOFPR (IMMOBILIZER FUEL PUMP RELAY) | Drives PGM-FI main relay 2 (FUEL PUMP) | 0 V for 2 seconds after turning ignition switch ON (II), then battery voltage |
| 18 | RED | ACC (A/C CLUTCH RELAY) | Drives A/C clutch relay | With compressor ON: about 0 V<br>With compressor OFF: battery voltage |
| 19 | LT GRN/WHT | VSV (EVAPORATIVE EMISSION (EVAP) CANISTER VENT SHUT VALVE) | Drives EVAP canister vent shut valve | With ignition switch ON (II): battery voltage |

**NOTE:** Standard battery voltage is about 12 V.

*Source page reference: 11-233*

---

### Printed page 11-234

<a id="p530"></a>
Source: [PDF p.530, printed p.11-234](../page-images/p0530.png).

# Fuel and Emissions Systems
## System Description (cont'd)
### ECM Inputs and Outputs at Connector E (31P)

| Terminal number | Wire color | Terminal name | Description | Signal |
| :--- | :--- | :--- | :--- | :--- |
| 20 | RED | SHO2S (SECONDARY HEATED OXYGEN SENSOR (SECONDARY HO2S), SENSOR 2) | Detects secondary HO2S (sensor 2) signal | With fully warmed up engine at idle and throttle fully closed: above 0.6 V<br>With throttle quickly closed: below 0.4 V |
| 21 | BLK/WHT | S02SHTC (SECONDARY HEATED OXYGEN SENSOR (SECONDARY HO2S) HEATER CONTROL) | Drives secondary HO2S (sensor 2) heater | With ignition switch ON (II): battery voltage<br>With fully warmed up engine running: duty controlled |
| 22 | WHT/BLK | BKSW (BRAKE PEDAL POSITION SWITCH) | Detects brake pedal position switch signal | With brake pedal released: about 0 V<br>With brake pedal pressed: battery voltage |
| 24 | WHT | CANL (CAN COMMUNICATION SIGNAL LOW) | Sends communication signal | With ignition switch ON (II): pulses |
| 25 | BLU | NEP (ENGINE SPEED PULSE) | Outputs engine speed pulse | With engine running: pulses |
| 27 | RED/BLU | IMOCD (IMMOBILIZER CODE) | Detects immobilizer signal | - |
| 28 | BLU/RED | ACS (A/C SWITCH SIGNAL) | Detects A/C switch signal | With A/C switch ON: about 0 V<br>With A/C switch OFF: about 5.0 V |
| 29 | BRN | SCS (SERVICE CHECK SIGNAL) | Detects servicecheck signal | With servicecheck signal shorted using HDS: about 0 V<br>With servicecheck signal open: about 5.0 V |
| 30 | GRN/WHT | WEN (WRITE ENABLE SIGNAL) | Detects service enable signal | With ignition switch ON (II): about 0 V |

**NOTE:** Standard battery voltage is about 12 V.

*Wire side of female terminals*

---

### Printed page 11-235

<a id="p531"></a>
Source: [PDF p.531, printed p.11-235](../page-images/p0531.png).

# Fuel and Emissions Systems — Vacuum Hose Routing

The routing illustration shows the EVAP canister purge valve and purge joint connected toward the EVAP canister, with the vehicle front marked. **Use the source image for the hose route and physical orientation.**

---

### Printed page 11-236

<a id="p532"></a>
Source: [PDF p.532, printed p.11-236](../page-images/p0532.png).

# Fuel and Emissions Systems — Vacuum Distribution

The numbered schematic identifies: 1 A/F sensor (sensor 1); 2 secondary HO2S (sensor 2); 3 MAP sensor; 4 ECT sensor 1; 5 IAT sensor; 6 CKP sensor; 7 knock sensor; 8 CMP sensor; 9 throttle body; 10 injector; 11 fuel pulsation damper; 12 fuel filter; 13 fuel pressure regulator; 14 fuel pump; 15 fuel tank; 16 air cleaner; 17 PCV valve; 18 three-way catalytic converter; 19 EVAP canister; 20 EVAP canister purge valve; 21 EVAP canister vent shut valve; 22 FTP sensor; 23 fuel tank vapor control valve. Refer to the source image for the vacuum and fuel routing.

---

### Printed page 11-237

<a id="p533"></a>
Source: [PDF p.533, printed p.11-237](../page-images/p0533.png).

# PGM-FI System

The programmed fuel injection (PGM-FI) system is a sequential multiport fuel injection system.

## Air Conditioning (A/C) Compressor Clutch Relay
When the ECM receives a demand for cooling from the A/C system, it delays the compressor from being energized, and enriches the mixture to assure smooth transition to the A/C mode.

## Air Fuel Ratio (A/F) Sensor
The A/F sensor operates over a wide air/fuel range. The A/F sensor is installed upstream of the TWC, and sends signals to the ECM which varies the duration of fuel injection accordingly.

### ZIRCONIA SENSOR ELEMENT TERMINALS HEATER TERMINALS

## Barometric Pressure (BARO) Sensor
The BARO sensor is inside the ECM. It converts atmospheric pressure into a voltage signal that is used by the ECM to modify the basic duration of the fuel injection discharge.

## Camshaft Position (CMP) Sensor
The CMP sensor detects the position of the No. 1 cylinder as a reference for sequential fuel injection to each cylinder.

### O-RING

## Crankshaft Position (CKP) Sensor
The CKP sensor detects crankshaft speed and is used by the ECM to determine ignition timing and timing for fuel injection of each cylinder as well as detecting engine misfire.

### O-RING

## Engine Coolant Temperature (ECT) Sensor 1 and Engine Coolant Temperature (ECT) Sensor 2
ECT sensor 1 and ECT sensor 2 are temperature dependent resistors (thermistors). The resistance decreases as the engine coolant temperature increases.

### O-RING

## Ignition Timing Control
The ECM contains the memory for basic ignition timing at various engine speeds and manifold absolute pressures. It also adjusts the timing according to engine coolant temperature.

---
**Page Reference:** 11-237

---

### Printed page 11-238

<a id="p534"></a>
Source: [PDF p.534, printed p.11-238](../page-images/p0534.png).

# Fuel and Emissions Systems
## System Description (cont'd)
### Injector Timing and Duration
The ECM contains the memory for basic discharge duration at various engine speeds and manifold pressures. The basic discharge duration, after being read out from the memory, is further modified by signals sent from various sensors to obtain the final discharge duration.

By monitoring long term fuel trim, the ECM detects long term malfunctions in the fuel system and sets a diagnostic trouble code (DTC).

### Intake Air Temperature (IAT) Sensor
The IAT sensor is a temperature dependent resistor (thermistor). The resistance of the thermistor decreases as the intake air temperature increases.

### Knock Sensor
The knock control system adjusts the ignition timing to minimize knock.

### Malfunction Indicator Lamp (MIL) Indication (In relation to Readiness Codes)
The vehicle has certain "readiness codes" that are part of the on-board diagnostics for the emissions systems.

If the vehicle's battery has been disconnected or gone dead, if the DTCs have been cleared, or if the ECM has been reset, these codes are reset. In some states, part of the emissions testing is to make sure these codes are set to complete. If all of them are not set to complete, the vehicle may fail the test, or the test cannot be finished.

To check if the readiness codes are set to complete, turn the ignition switch ON (II), but do not start the engine. The MIL will come on for 15—20 seconds. If it then goes off, the readiness codes are complete. If it flashes five times, one or more readiness codes are not complete. To set each code, drive the vehicle or run the engine as described in the procedures (see page 11-256).

### Manifold Absolute Pressure (MAP) Sensor
The MAP sensor converts manifold absolute pressure into electrical signals to the ECM.

### Output Shaft (Countershaft) Speed Sensor
This sensor detects countershaft speed.

**MAGNET O-RING**

Page 11-238

---

### Printed page 11-239

<a id="p535"></a>
Source: [PDF p.535, printed p.11-239](../page-images/p0535.png).

# Secondary Heated Oxygen Sensor (Secondary HO2S)

The secondary HO2S detects the oxygen content in the exhaust gas downstream of the three way catalytic converter (TWC), and sends signals to the ECM which varies the duration of fuel injection accordingly. To stabilize its output, the sensor has an internal heater.

The ECM compares the HO2S output with the A/F sensor output to determine catalyst efficiency. The secondary HO2S is located on the TWC.

**ZIRCONIA ELEMENT SENSOR TERMINALS HEATER TERMINALS**

---

## Electronic Throttle Control System

The throttle is electronically controlled by the electronic throttle control system. Refer to the system diagram to see a functional layout of the system.

*   **Idle control:** When the engine is idling, the ECM controls the throttle actuator to maintain the proper idle speed according to engine loads.
*   **Acceleration control:** When the accelerator pedal is pressed, the ECM opens the throttle valve depending on the accelerator pedal position (APP) sensor signal.
*   **Cruise control:** The ECM controls the throttle actuator to maintain set speed when the cruise control is operating.

The throttle actuator takes the place of the cruise control actuator.

---

## Accelerator Pedal Position (APP) Sensor

As the accelerator pedal position changes, the sensor varies the signal voltage to the ECM.

**APP SENSOR BRUSH TERMINAL LEVER**

---

## Throttle Body

The throttle body is a single-barrel side draft type. The lower portion of the throttle valve is heated by engine coolant from the cylinder head to prevent icing of the throttle plate.

**THROTTLE VALVE THROTTLE POSITION (TP) SENSOR A/B and THROTTLE ACTUATOR**

---

*Page 11-239*

---

### Printed page 11-240

<a id="p536"></a>
Source: [PDF p.536, printed p.11-240](../page-images/p0536.png).

# Fuel and Emissions Systems
## System Description (cont'd)
### Idle Control System
When the engine is cold, the A/C compressor is on, the transmission is in gear, the brake pedal is pressed, the power steering load is high, or the alternator is charging, the ECM sends signals to the throttle actuator to maintain the correct idle speed.

**Brake Pedal Position Switch**
The brake pedal position switch signals the ECM when the brake pedal is pressed.

**Electrical Power Steering (EPS) Signal**
The EPS signals the ECM when the power steering load is high.

**Engine Start Switch**
The engine start switch signals the ECM when the engine is cranking.

### Fuel Supply System
#### Fuel Cutoff Control
During deceleration with the throttle valve closed, current to the injectors is cut off to improve fuel economy at engine speeds over 1,050 rpm. Fuel cutoff control also occurs when the engine speed exceeds 8,200 rpm, regardless of the position of the throttle valve, to protect the engine from over-revving. On a cold engine, fuel cut occurs at a lower engine speed.

#### Fuel Pump Control
When the ignition is turned on, the ECM grounds PGM-FI main relay 2 (FUEL PUMP) which feeds current to the fuel pump for 2 seconds to pressurize the fuel system. With the engine running, the ECM grounds PGM-FI main relay 2 (FUEL PUMP) and feeds current to the fuel pump. When the engine is not running and the ignition is on, the ECM cuts ground to PGM-FI main relay 2 (FUEL PUMP) which cuts current to the fuel pump.

**PGM-FI Main Relay 1 (Fl MAIN) and 2 (FUEL PUMP)**
PGM-FI main relay 1 (Fl MAIN) is energized whenever the ignition switch is ON (II) to supply battery voltage to the ECM, power to the injectors, and power for PGM-FI main relay 2 (FUEL PUMP). PGM-FI main relay 2 (FUEL PUMP) is energized to supply power to the fuel pump for 2 seconds when the ignition switch is turned ON (II), and when the engine is cranking or running.

*Page Reference: 11-240*

---

### Printed page 11-241

<a id="p537"></a>
Source: [PDF p.537, printed p.11-241](../page-images/p0537.png).

# Catalytic Converter System
TWC (Three Way Catalytic Converter)
The TWC converts hydrocarbons (HC), carbon monoxide (CO), and oxides of nitrogen (NOx) in the exhaust gas to carbon dioxide (CO2 ), nitrogen (N2 ), and water vapor.

# Positive Crankcase Ventilation (PCV) System
The PCV valve prevents blow-by gases from escaping into the atmosphere by venting them into the intake manifold.
Diagram labels: PCV valve, PCV hose, breather.

# Evaporative Emission (EVAP) Control System
Refer to the system diagram to see a functional layout of the system.

## EVAP Canister
The EVAP canister temporarily stores fuel vapor from the fuel tank until it can be purged from the EVAP canister into the engine and burned.

## EVAP Canister Purge Valve
When the engine coolant temperature is below 149 °F (65 °C), the ECM turns off the EVAP canister purge valve which cuts vacuum to the EVAP canister.

## Fuel Tank Pressure (FTP) Sensor
The FTP sensor converts fuel tank absolute pressure into an electrical input to the ECM .
Sensor unit
O-RING
(cont'd)
11-241

---

### Printed page 11-242

<a id="p538"></a>
Source: [PDF p.538, printed p.11-242](../page-images/p0538.png).

# Fuel and Emissions Systems
## System Description (cont'd)
### EVAP Canister Vent Shut Valve

The EVAP canister vent shut valve is on the EVAP canister.
The EVAP canister vent shut valve controls the venting of the EVAP canister.

**Diagram Elements:**
- O-RING
- Valve terminal

---

### Printed page 11-243

<a id="p539"></a>
Source: [PDF p.539, printed p.11-243](../page-images/p0539.png).

# Fuel Cap Warning Message

The ECM detects a loose or missing fuel fill cap as an evaporative system leak and alerts the driver by showing a warning message in the gauge display.

## First drive cycle

The first time a leak is detected a "CHECK FUEL C A P" message appears in the gauge display (A). To scroll to another message, press the select/reset button.

The "CHECK FUEL C A P" message will appear each time you restart the engine until the system turns the message off. Turn the engine off then replace or tighten the fuel fill cap until it clicks at least once.

### Shows "CHECK FUEL C A P" in the gauge display

#### To make the message go off (With the HDS)
**Procedure**
1. Tighten the fuel fill cap until it clicks.
2. Clear the Temporary DTC with the HDS.
3. Verify there is no leak by doing the EVAP FUNCTION TEST in the INSPECTION MENU with the HDS.

#### To make the message go off (Without the HDS) ('06-07 models)
**Procedure**
1. Tighten the fuel fill cap until it clicks.
2. The message should go off after several days of normal driving.

#### To make the message go off (Without the HDS)
**Procedure**
1. Tighten the fuel fill cap until it clicks.
2. Start the engine, then turn the ignition switch OFF.
3. Repeat step 2 two more times.

*(cont'd) 11-243*

---

### Printed page 11-244

<a id="p540"></a>
Source: [PDF p.540, printed p.11-244](../page-images/p0540.png).

# Fuel and Emissions Systems — Electronic Throttle Control System Diagram

The system comprises the throttle actuator, TP sensor A/B, APP sensor A/B, throttle actuator control module, and ECM. APP sensor A has yellow/red, red/blue, and green/white wires; APP sensor B has yellow/blue, red/yellow, and green wires. The ECM communicates with the throttle actuator control module, which drives the throttle actuator and receives the TP sensor signals. Both modules receive power from the throttle actuator control module relay. **Refer to the source image for exact wire routing and connections.**

---

### Printed page 11-245

<a id="p541"></a>
Source: [PDF p.541, printed p.11-245](../page-images/p0541.png).

# Fuel and Emissions Systems — EVAP Control Diagram

Fuel vapor from the tank is held in the EVAP canister until it is drawn through the canister into the intake manifold and burned. Fresh air enters during purge. The ECM controls the EVAP canister purge valve when coolant temperature is above **149 °F (65 °C)**.

The source diagram shows the fuel filler vapor recirculation tube, fuel tank vapor control valve, fuel tank vapor recirculation tube, FTP sensor, EVAP canister, vent shut valve, purge valve, ECM, intake manifold, and connections from the A/F sensor relay and No. 6 ACG (15 A) fuse. Refer to the source image for hose and wire routing.

---

### Printed page 11-246

<a id="p542"></a>
Source: [PDF p.542, printed p.11-246](../page-images/p0542.png).

# Fuel and Emissions Systems — ECM Circuit Diagram

ECM circuit diagram: injector control and position sensors. ECM B5 INJ1 (brown), B4 INJ2 (red), B3 INJ3 (blue), and B2 INJ4 (yellow) run to the four injectors. The common injector feed is yellow/black through the 20P junction connector. ECM A3 IGP1 and A2 IGP2 are yellow/black power feeds. CMP uses A6 (green); CKP uses A7 (blue). Connectors C101 and C105 are shown.

Refer to the source image for exact wiring paths, splice positions, connector orientation, and circuit variants.

---

### Printed page 11-247

<a id="p543"></a>
Source: [PDF p.543, printed p.11-247](../page-images/p0543.png).

# Fuel and Emissions Systems — ECM Circuit Diagram

ECM circuit diagram: VTEC, MAP, knock, and immobilizer. VTEC oil pressure switch connects to B11 VTPSW (blue/black); VTEC solenoid to B6 VTS (green/yellow). MAP sensor connections are A21 VCC1 (yellow/red), A30 MAP (green/red), and A24 SG1 (green/white). Knock sensor connects to A1 KS (red/blue). Immobilizer signal connects to E27 IMOCD (red/blue).

Refer to the source image for exact wiring paths, splice positions, connector orientation, and circuit variants.

---

### Printed page 11-248

<a id="p544"></a>
Source: [PDF p.544, printed p.11-248](../page-images/p0544.png).

# Fuel and Emissions Systems — ECM Circuit Diagram

ECM circuit diagram: temperature sensors and grounds. IAT sensor signal connects to B17 (red/yellow); ECT sensor 1 to B8 (red/white); ECT sensor 2 to E1 (blue). A23 SG2 is green/yellow. Logic grounds A9 LG1 and A8 LG2 are brown/yellow. The 20P junction connector is shown.

Refer to the source image for exact wiring paths, splice positions, connector orientation, and circuit variants.

---

### Printed page 11-249

<a id="p545"></a>
Source: [PDF p.545, printed p.11-249](../page-images/p0545.png).

# Fuel and Emissions Systems — ECM Circuit Diagram

ECM circuit diagram: purge valve, alternator, and ignition coils. EVAP purge valve connects to B21 PCS (yellow/blue). Alternator connections are B10 ALTL (white/blue), B13 ALTF (white/red), and B18 ALTC (white/green). Ignition coil control connections are A16 IGPLS1 (white), A15 IGPLS2 (white/green), A14 IGPLS3 (white/black), and A13 IGPLS4 (white/blue). The 20P junction connector is shown.

Refer to the source image for exact wiring paths, splice positions, connector orientation, and circuit variants.

---

### Printed page 11-250

<a id="p546"></a>
Source: [PDF p.546, printed p.11-250](../page-images/p0546.png).

# Fuel and Emissions Systems — ECM Circuit Diagram

ECM circuit diagram: accelerator pedal and electronic throttle. Accelerator pedal position sensor connections are A26 APSA (red/blue), A20 VCC2 (yellow/blue), and A25 APSB (red/yellow). ECM B19 SEFD (green) and B20 SEDF (blue) connect to the throttle actuator control module. The throttle body contains TP sensors A/B and the throttle actuator. The BARO sensor is built into the ECM.

Refer to the source image for exact wiring paths, splice positions, connector orientation, and circuit variants.

---

### Printed page 11-251

<a id="p547"></a>
Source: [PDF p.547, printed p.11-251](../page-images/p0547.png).

# Fuel and Emissions Systems — ECM Circuit Diagram

ECM circuit diagram: oxygen sensors, EPS, gauges, and cruise/brake inputs. A/F sensor connections are A31 AFS+ (red), A28 AFS− (red/yellow), A10 AFSHTC (green). Secondary HO2S connections are E20 SHO2S (red) and E21 SO2SHTC (black/white). E16 EPSLD (blue/black) connects to EPS; E25 NEP (blue) goes to test tachometer/gauge; E13 SEFMJ (yellow) goes to gauge. Brake/cruise connections include E22 BKSW (white/black), D8 BKSWNC (gray), D4 CCMSW (light green), D1 CCSETSW (light green/red), and D7 CCRESSW (light green/black). The source distinguishes 2008 (*1) from 2006–07 (*2) equipment.

Refer to the source image for exact wiring paths, splice positions, connector orientation, and circuit variants.

---

### Printed page 11-252

<a id="p548"></a>
Source: [PDF p.548, printed p.11-252](../page-images/p0548.png).

# Fuel and Emissions Systems — ECM Circuit Diagram

ECM circuit diagram: diagnostic, CAN, clutch, and EVAP tank circuits. E29 SCS (brown) and E30 WEN (green/white) connect to the DLC. E11 CANH (red) and E24 CANL (white) connect to steering angle/VSA circuits. D9 CCCLSW (pink) comes from the cruise clutch switch. Fuel tank pressure sensor connections are E5 VCC3 (yellow/blue), E14 FTP (light green), and E4 SG3 (green). EVAP vent shut valve is E19 VSV (light green/white). The source marks a 2008-specific circuit.

Refer to the source image for exact wiring paths, splice positions, connector orientation, and circuit variants.

---

### Printed page 11-253

<a id="p549"></a>
Source: [PDF p.549, printed p.11-253](../page-images/p0549.png).

# Fuel and Emissions Systems — ECM Circuit Diagram

ECM circuit diagram: vehicle speed, power grounds, and relays. A18 NC (blue/white) is shown with the speed signal. A5 PG1 and A4 PG2 are black grounds. Fuel pump and PGM-FI main relay circuits include E9 IG1 (black/yellow), E17 IMOFPR (green/yellow), and E7 MRLY (green). D15 ETCSRLY (brown) controls the throttle actuator control module relay; E8 AFSHTCR (orange) controls the A/F sensor relay. The ignition coil relay is also shown.

Refer to the source image for exact wiring paths, splice positions, connector orientation, and circuit variants.

---

### Printed page 11-254

<a id="p550"></a>
Source: [PDF p.550, printed p.11-254](../page-images/p0550.png).

# Fuel and Emissions Systems — ECM Circuit Diagram

ECM circuit diagram: air conditioning, cooling fan, and electrical load. E28 ACS (blue/red) is the A/C pressure switch input. E18 ACC (red) runs to the compressor clutch relay. E12 FANC (green) runs to the radiator fan control. E15 ELD (green/red) receives electrical load detector input. The drawing includes under-hood fuse/relay box feeds, with *1 for 2008 and *3 for vehicles with A/C.

Refer to the source image for exact wiring paths, splice positions, connector orientation, and circuit variants.

---

### Printed page 11-255

<a id="p551"></a>
Source: [PDF p.551, printed p.11-255](../page-images/p0551.png).

# Fuel and Emissions Systems — ECM Circuit Diagram

ECM power and starting circuit diagram. The under-dash fuse/relay box, ignition/start switch, starter cut relay, IG2 cut relay, clutch interlock switch, and junctions are shown. Fuse index: No. 6 ACG (15 A), No. 2 FUEL PUMP SRS (15 A), No. 11 IGP DBW (7.5 A), No. 10 IGP LAF (7.5 A), No. 15 LAF (20 A in 2006–07; 15 A in 2008), No. 14 DBW (15 A), No. 16 IG COIL (15 A), No. 3 ENGINE START (7.5 A), and No. 20 heater control/cooling fan relay (7.5 A).

Refer to the source image for exact wiring paths, splice positions, connector orientation, and circuit variants.

---

### Printed page 11-256

<a id="p552"></a>
Source: [PDF p.552, printed p.11-256](../page-images/p0552.png).

# Fuel and Emissions Systems
## How to Set Readiness Codes
### Malfunction Indicator Lamp (MIL) Indication
#### (In relation to Readiness Codes)

The vehicle has certain "readiness codes" that are part of the on-board diagnostics for the emissions systems.

If the vehicle's battery has been disconnected or gone dead, if the DTCs have been cleared, or if the ECM has been reset, these readiness codes are reset to incomplete. In some states, part of the emissions testing is to make sure these codes are set to complete. If all of them are not set to complete, the vehicle may fail the emission test, or the test cannot be finished.

To check if the readiness codes are set to complete, turn the ignition switch ON (II), but do not start the engine. The MIL will come on for 15—20 seconds. If it then goes off, the readiness codes are complete. If it flashes five times, one or more readiness codes are not set to complete. To set readiness codes from incomplete to complete, do the procedure for the appropriate code.

To check the status of a specific DTC system, check the OBD status in the DTC MENU with the HDS (see page 11-218). This screen displays the code, the current data list of the enable criteria, and the status of the readiness testing.

---

## Catalytic Converter Monitor and Readiness Code

**NOTE:**
*   Do not turn the ignition switch off during the procedure.
*   All readiness codes are cleared when the battery is disconnected, if the DTCs have been cleared, or if the ECM is reset with the HDS.
*   Low ambient temperatures or excessive stop-and-go traffic may increase the drive time needed to switch the readiness code from incomplete to complete.
*   The readiness code will not switch to complete until all the enable criteria are met.
*   If a fault in the secondary HO2S system caused the MIL to come on, the readiness code cannot be set to complete until you correct the fault.

### Enable Criteria
*   ECT SENSOR 1 at 158 °F (70 °C) or more.
*   IAT SENSOR at 20 °F (- 7 °C) or more.
*   V S S reads more than 25 mph (40 km/h).

### Procedure
1.  Connect the HDS to the vehicle's data link connector (DLC), and bring up the READINESS CODEs screen for Catalyst in the DTCs MENU.
2.  Start the engine.
3.  Test-drive the vehicle under stop-and-go conditions with short periods of steady cruise. After about 5 miles (8 km), the readiness code should switch to completed.
4.  If the readiness code is still not set to complete, check for a Temporary DTC with the HDS. If there is no DTC, one or more of the enable criteria were probably not met; repeat the procedure.

**Page Reference:** 11-256

---

### Printed page 11-257

<a id="p553"></a>
Source: [PDF p.553, printed p.11-257](../page-images/p0553.png).

# Page 553: S2000 Fuel and Emissions Part C

## Evaporative Emission (EVAP) Control System Monitor and Readiness Code

**NOTE:** All readiness codes are cleared when the battery is disconnected, if the DTCs have been cleared, or if the ECM is reset with the HDS.

### Enable Criteria
*   Battery voltage is higher than 10.5 V.
*   Engine at idle.
*   ECT SENSOR 1 and SENSOR 2 between 176 °F (80 °C) and 212 °F (100 °C).
    *   *(Unclear OCR: "<€" likely represents "°C")*
*   MAP sensor less than 46.6 kPa (14 in.Hg, 350 mmHg).
*   VSS 0 mph (0 km/h).
*   IAT SENSOR between 32 °F (0 °C) and 212 °F (100 °C).
    *   *(Unclear OCR: "°Z" likely represents "°C")*

### Procedure
1.  Connect the HDS to the vehicle's data link connector (DLC).
2.  Start the engine.
3.  Select EVAP TEST in the INSPECTION MENU with the HDS, then select the FUNCTION TEST in the EVAP TEST MENU.
    *   If the result is normal, readiness is complete.
        *   *(Unclear OCR: "are" likely a typo for "is")*
    *   If the result is not normal, go to the next step.
        *   *(Unclear OCR: "are" likely a typo for "is")*
4.  Check for a Temporary DTC. If there is no DTC, one or more of the enable criteria were probably not met; repeat the procedure.

---

## Air Fuel Ratio (A/F) Sensor Monitor and Readiness Code

**NOTE:**
*   Do not turn the ignition switch off during the procedure.
*   All readiness codes are cleared when the battery is disconnected, if the DTCs have been cleared, or if the ECM is reset with the HDS.
    *   *(Unclear OCR: "AH" likely refers to A/F Sensor readiness codes based on context)*

### Enable Criteria
*   ECT S E N S O R 1 at 140 °F (60 °C) or more.

### Procedure
1.  Start the engine.
2.  Test-drive the vehicle under stop-and-go conditions with short periods of steady cruise. During the drive, decelerate (with the throttle fully closed) for 5 seconds. After about 3.5 miles (5.6 km), the readiness code should switch from incomplete to complete.
3.  Check the readiness codes screen for the AIR FUEL RATIO (A/F) S E N S O R in the DTCs MENU with the HDS.
    *   If the screen shows complete, readiness is complete.
    *   If the screen shows not complete, go to the next step.
4.  Check for a Temporary DTC. If there is no DTC, the enable criteria was probably not met. Select the DATA LIST menu. Check the ECT SENSOR 1 in the ALL DATA LIST with the HDS. If ECT SENSOR 1 is lower than 140 °F (60 °C), run the engine until it is higher than 140 °F (60 °C), then repeat the procedure.

*(cont'd)*

**Page Reference:** 11-257

---

### Printed page 11-258

<a id="p554"></a>
Source: [PDF p.554, printed p.11-258](../page-images/p0554.png).

# Fuel and Emissions Systems
## How to Set Readiness Codes (cont'd)

### Air Fuel Ratio (A/F) Sensor Heater Monitor
**Readiness Code**

> **NOTE:** All readiness codes are cleared when the battery is disconnected, if the DTCs have been cleared, or if the ECM is reset with the HDS.

**Procedure**
1. Start the engine, and let it idle for 1 minute. The readiness code should switch from incomplete to complete.
2. If the readiness code is still not set to complete, check for a Temporary DTC. If there is no DTC, repeat the procedure.

---

### Misfire Monitor and Readiness Code
* This readiness code is always set to available because misfiring is continuously monitored.
* Monitoring pauses, and the misfire counter resets, if the vehicle is driven over a rough road.
* Monitoring also pauses, and the misfire counter holds at its current value, if the throttle position changes more than a predetermined value, or if driving conditions fall outside the range of any related enable criteria.

---

### Fuel System Monitor and Readiness Code
* This readiness code is always set to available because the fuel system is continuously monitored during closed loop operation.
* Monitoring pauses when the catalytic converter, EVAP control system, and A/F sensor monitors are active.
* Monitoring also pauses when any related enable criteria are not being met. Monitoring resumes when the enable criteria is again being met.

---

### Comprehensive Component Monitor and Readiness Code
This readiness code is always set to available because the comprehensive component monitor is continuously running whenever the engine is cranking or running.

**Page Reference:** 11-258

---

### Printed page 11-259

<a id="p555"></a>
Source: [PDF p.555, printed p.11-259](../page-images/p0555.png).

# PGM-FI System — Component Location Index

The source diagram shows these components and replacement references:

| Component | Replacement page |
|---|---|
| Electrical load detector (ELD) | — |
| Intake air temperature (IAT) sensor | 11-384 |
| Camshaft position (CMP) sensor | 11-387 |
| Engine coolant temperature (ECT) sensor 1 | 11-385 |
| Engine coolant temperature (ECT) sensor 2 | 11-385 |
| Knock sensor | 11-388 |
| Manifold absolute pressure (MAP) sensor | 11-384 |
| Crankshaft position (CKP) sensor | 11-387 |
| Output shaft (countershaft) speed sensor | 11-388 |
| Air fuel ratio (A/F) sensor (sensor 1) | 11-386 |
| Secondary heated oxygen sensor (secondary HO2S, sensor 2) | 11-386 |

Refer to the source image for the exact vehicle locations.

---

### Printed page 11-260

<a id="p556"></a>
Source: [PDF p.556, printed p.11-260](../page-images/p0556.png).

# PGM-FI System — Component Location Index (continued)

The source image locates the injectors, ECM, data link connector (DLC), PGM-FI main relay 1 (FI main), PGM-FI main relay 2 (fuel pump), and A/F sensor relay (LAF).

| Component | Service reference |
|---|---|
| Injectors | Replacement, p.11-382 |
| ECM | General troubleshooting, p.11-213; updating, p.11-216; substitution, p.11-217; replacement, p.11-389 |
| DLC | General troubleshooting, p.11-213; troubleshooting, pp.11-367 |

Refer to the source image for exact locations.

---

### Printed page 11-261

<a id="p557"></a>
Source: [PDF p.557, printed p.11-261](../page-images/p0557.png).

# DTC Troubleshooting

## DTC P0107: MAP Sensor Circuit Low Voltage

> **NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Check the MAP SENSOR in the DATA LIST with the HDS.
   Is about 3 kPa (1.0 in.Hg, 26 mmHg), or 0.23 V or less indicated?
   - **YES** — Go to step 3.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the ECM .

3. Turn the ignition switch OFF.
4. Disconnect the MAP sensor 3P connector.
5. Turn the ignition switch ON (**II**).
6. Check the MAP SENSOR in the DATA LIST with the HDS.
   Is about 3 kPa (1.0 in.Hg, 26 mmHg), or 0.23 V or less indicated?
   - **YES** — Go to step 9.
   - **NO** — Go to step 7.

7. Measure voltage between MAP sensor 3P connector terminals No. 1 and No. 3.

MAP sensor 3P connector: terminal 1 VCC1 (YEL/RED), terminal 2 MAP, terminal 3 SG1 (GRN/WHT); wire side of female terminals.

Is there about 5 V?
- **YES** — Go to step 13.
- **NO** — Go t o step 8.

8. Measure voltage between ECM connector terminals A21 and A24.

ECM connector A (31P): A21 VCC1 (YEL/RED), A24 SG1 (GRN/WHT); wire side of female terminals.

Is there about 5 V?
- **YES** — Repair open in the wire between the ECM (A21) and the MAP sensor, then go to step 15.
- **NO** — Go to step 20.

(cont'd)

> **Source Page Reference:** 11-261

---

### Printed page 11-262

<a id="p558"></a>
Source: [PDF p.558, printed p.11-262](../page-images/p0558.png).

# DTC P0107 — MAP Sensor Circuit Low Voltage (continued)

9. Turn ignition OFF.
10. Jump the SCS line with the HDS.
11. Disconnect ECM connector A (31P).
12. Check continuity between MAP sensor 3P connector terminal 2, MAP (GRN/RED), and body ground. **YES:** Repair the short between ECM A30 and the MAP sensor, then go to step 15. **NO:** Go to step 21.
13. Turn ignition OFF.
14. Replace the MAP sensor (p.11-384).
15. Reconnect all connectors.
16. Turn ignition ON (II).
17. Reset the ECM with the HDS.
18. Perform the ECM idle learn procedure (p.11-462).
19. Check for Temporary DTCs or DTCs. **P0107 YES:** Check for poor connections or loose terminals at MAP sensor and ECM, then return to step 1. **NO:** Troubleshooting is complete; address any other indicated DTCs.
20. Turn ignition OFF.
21. Reconnect all connectors.
22. Update ECM software if needed (p.11-216), or substitute a known-good ECM (p.11-217).
23. Check for Temporary DTCs or DTCs. **P0107 YES:** Check MAP/ECM connections. If ECM was updated, substitute a known-good ECM and recheck; if it was substituted, return to step 1. **NO:** If ECM was updated, troubleshooting is complete; if substituted, replace the original ECM (p.11-389). Address any other indicated DTCs.

---

### Printed page 11-263

<a id="p559"></a>
Source: [PDF p.559, printed p.11-263](../page-images/p0559.png).

# DTC P0108: MAP Sensor Circuit High Voltage
NOTE: Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
1. Turn the ignition switch ON (II).
2. Check the MAP S E N S O R in the DATA LIST with the HDS.
Is about 160 kPa (47.1 in.Hg, 1,197 mmHg), or 4.49 V or more indicated?
YES — Go to step 3.
NO—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the ECM.
•
3. Turn the ignition switch OFF.
4. Disconnect the MAP sensor 3P connector.
5. Connect the MAP sensor 3P connector terminals No. 2 and No. 3 with a jumper wire.
MAP SENSOR 3P CONNECTOR
I 1 (z\ 3 |
M A P
(GRN/RED)
S G I
(GRN/WHT)
J U M P E R W I R E
Wire side of female terminals
6. Turn the ignition switch ON (II).
7. Check the MAP SENSOR in the DATA LIST with the HDS.
Is about 160 kPa (47.1 in.Hg, 1,197 mmHg), or 4.49 V or more indicated?
YES — Go t o s t e p 8.
NO—Go to step 19.
8. Remove the jumper wire from the MAP sensor 3P connector.
9. Measure voltage between MAP sensor 3P connector terminals No. 1 and No. 3.
MAP SENSOR 3P CONNECTOR
V C C 1 A.
( Y E L / R E D ) . — A
1 2 3
S G I
(GRN/WHT)
Wire side of female terminals
Is there about 5 V?
YES — Go to step 15.
NO — Go to step 10.
10. Turn the ignition switch OFF.
11. J u m p the SCS line with the HDS.
12. Disconnect ECM connector A (31P).
13. Connect MAP sensor 3P connector terminal No. 3 to body ground with a jumper wire.
MAP SENSOR 3P CONNECTOR
vv 1[2|3l
S G I
(GRN/WHT)
J U M P E R WIRE
Wire side of female terminals
(cont'd)
11-263

---

### Printed page 11-264

<a id="p560"></a>
Source: [PDF p.560, printed p.11-264](../page-images/p0560.png).

# DTC P0108 — MAP Sensor Circuit High Voltage (continued)

14. Check continuity between ECM connector A24, SG1 (GRN/WHT), and body ground. **YES:** Go to step 27. **NO:** Repair the open between ECM A24 and MAP sensor, then go to step 21.
15. Turn ignition OFF.
16. Jumper ECM connector A24 SG1 (GRN/WHT) to A30 MAP (GRN/RED).
17. Turn ignition ON (II).
18. Check MAP SENSOR in HDS DATA LIST. Is about 160 kPa (47.1 in.Hg, 1,197 mmHg) or 4.49 V or more indicated? **YES:** Go to step 26. **NO:** Repair the open between ECM A30 and MAP sensor, then go to step 21.
19. Turn ignition OFF.
20. Replace the MAP sensor (p.11-384).
21. Reconnect all connectors.
22. Turn ignition ON (II).
23. Reset the ECM with the HDS.
24. Perform the ECM idle learn procedure (p.11-462).
25. Check for Temporary DTCs or DTCs with the HDS. **P0108 YES:** Check MAP sensor/ECM connections and return to step 1. **NO:** Troubleshooting is complete; address other indicated DTCs.

---

### Printed page 11-265

<a id="p561"></a>
Source: [PDF p.561, printed p.11-265](../page-images/p0561.png).

Step 26: Turn the ignition switch OFF.
Step 27: Reconnect all connectors.
Step 28: Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
Step 29: Check for Temporary DTCs or DTCs with the HDS.
Decision Point: Is DTC P0108 Indicated?
Path YES: Check for poor connections or loose terminals at the MAP sensor and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
Path NO: If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

---

### Printed page 11-266

<a id="p562"></a>
Source: [PDF p.562, printed p.11-266](../page-images/p0562.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0111: IAT Sensor Circuit Range/Performance Problem

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the IAT sensor.
   Are the connections and terminals OK?
   - **YES** — Go to step 2.
   - **NO** — Repair the connections or terminals, then go to step 15.

2. Remove the IAT sensor (see page 11-384).

3. Allow the IAT sensor to cool to ambient temperature.

4. Note the ambient temperature.

5. Connect IAT sensor to its 2P connector, but do not install it on the intake air duct.

6. Turn the ignition switch ON (II).

7. Note the value of the IAT SENSOR quickly in the DATA LIST with the HDS.

8. Compare the value of the IAT SENSOR and the ambient temperature.
   Does the value of the IAT SENSOR differ 5.4 °F (3 °C) or more?
   - **YES** — Go to step 13.
   - **NO** — Go to step 9.

9. Disconnect the IAT sensor from the 2P connector.

10. Using a heat gun, blow hot air on the IAT sensor for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor.

11. Connect the IAT sensor to its 2P connector, but do not install it on the intake air duct.

12. Check the IAT SENSOR in the DATA LIST with the HDS.
    Does the IAT SENSOR change 58 °F (32 °C) or more?
    - **YES** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the IAT sensor and the ECM. •
    - **NO** — Go to step 13.

13. Turn the ignition switch OFF.

14. Replace the IAT sensor (see page 11-384).

15. Turn the ignition switch ON (II).

16. Reset the ECM with the HDS.

17. Do the ECM idle learn procedure (see page 11-462).

18. Check for Temporary DTCs or DTCs with the HDS.
    Is DTC P0111 indicated?
    - **YES** — Check for poor connections or loose terminals at the IAT sensor and the ECM, then go to step 1.
    - **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •

**Page Reference:** 11-266

---

### Printed page 11-267

<a id="p563"></a>
Source: [PDF p.563, printed p.11-267](../page-images/p0563.png).

# DTC P0112: IAT Sensor Circuit Low Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Check the **IAT SENSOR** in the **DATA LIST** with the **HDS**.
   Is about 356 °F (180 °C) or higher, or 0.08 V or less indicated?
   - **YES** — Go t o s t e p 3.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the IAT sensor and the ECM.

3. Turn the ignition switch OFF.
4. Disconnect the IAT sensor 2P connector.
5. Turn the ignition switch ON (**II**).
6. Check the **IAT SENSOR** in the **DATA LIST** with the **HDS**.
   Is about 356 °F (180 °C) or higher, or 0.08 V or less indicated?
   - **YES** — Go t o s t e p 7.
   - **NO** — Go to step 11.

7. Turn the ignition switch OFF.
8. Jump the **SCS** line with the **HDS**.
9. Disconnect ECM connector B (24P).
10. Check for continuity between IAT sensor 2P connector terminal No. 1 and body ground.

    > **IAT SENSOR 2P C O N N E C T O R**
    > **IAT** (RED/YEL) Wire side of female terminals

    Is there continuity?
    - **YES** — Repair short in the wire between the IAT sensor and the ECM (**B17**), then go to step 13.
    - **NO** — Go t o s t e p 18.

11. Turn the ignition switch OFF.
12. Replace the IAT sensor (see page 11-384).
13. Reconnect all connectors.
14. Turn the ignition switch ON (**II**).
15. Reset the **ECM** with the **HDS**.
16. Do the **ECM** idle learn procedure (see page 11-462).

*(cont'd)*

**Page Reference:** 11-267

---

### Printed page 11-268

<a id="p564"></a>
Source: [PDF p.564, printed p.11-268](../page-images/p0564.png).

PGM-FI System
DTC Troubleshooting (cont'd)
17. Check for Temporary DTCs or DTCs with the HDS.
Is DTC P0112 indicated?
YES — C h e c k for poor connections or loose terminals at the IAT sensor and the ECM , then go to step 1.
NO—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •
18. Reconnect all connectors.
19. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
20. Check for Temporary DTCs or DTCs with the HDS.
Is DTCP0112 indicated?
YES — C h e c k for poor connections or loose terminals at the IAT sensor and the ECM . If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM w a s substituted, go to step 1.
NO—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •
11-268

---

### Printed page 11-269

<a id="p565"></a>
Source: [PDF p.565, printed p.11-269](../page-images/p0565.png).

# DTC P0113: IAT Sensor Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Check the **IAT SENSOR** in the DATA LIST with the HDS.
   Is about -40°F (-40 °C) or less, or 4.92 V or more indicated?
   * **YES** — Go to step 3.
   * **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the IAT sensor and the ECM.

3. Turn the ignition switch OFF.
4. Disconnect the IAT sensor 2P connector.
5. Connect IAT sensor 2P connector terminals No. 1 and No. 2 with a jumper wire.

   **IAT SENSOR 2P C O N N E C T O R**
   IAT sensor 2P connector: terminal 1 IAT (RED/YEL) and terminal 2 SG3 (GRN); jumper between 1 and 2. View from wire side of female terminals.

6. Turn the ignition switch ON (**II**).
7. Check the **IAT SENSOR** in the DATA LIST with the HDS.
   Is about -40 °F (-40 °C) or less, or 4.92 V or more indicated?
   * **YES** — Go to step 8.
   * **NO** — Go to step 18.

8. Turn the ignition switch OFF.
9. Remove the jumper wire from the IAT sensor 2P connector.
10. Turn the ignition switch ON (**II**).
11. Measure voltage between IAT sensor 2P connector terminal No. 1 and body ground.

    **IAT SENSOR 2P C O N N E C T O R**
    Terminal 1 IAT (RED/YEL), wire side of female terminals.
    Is there about 5 V?
    * **YES** — Go t o step 12.
    * **NO** — Go to step 17.

12. Turn the ignition switch OFF.
13. Jump the **SCS** line with the HDS.
14. Disconnect **ECM** connector **E (31P)**.
15. Connect IAT sensor 2P connector terminal No. 2 to body ground with a jumper wire.

    **IAT SENSOR 2P C O N N E C T O R**
    Terminal 2 SG3 (GRN) jumpered to body ground, wire side of female terminals.
    *(cont'd)*

---

### Printed page 11-270

<a id="p566"></a>
Source: [PDF p.566, printed p.11-270](../page-images/p0566.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

### 16. Check for continuity between ECM connector terminal E4 and body ground.
**ECM CONNECTOR E (31P)**
- SG3 (GRN) f
- Wire side of female terminals

**Is there continuity?**
- **YES** — Go to step 26.
- **NO** — Repair open in the wire between the ECM (E4) and the IAT sensor, then go to step 20.

### 17. Measure voltage between ECM connector terminal B17 and body ground.
**ECM CONNECTOR B (24P)**
- IAT (RED/YEL)
- Wire side of female terminals

**Is there about 5 V?**
- **YES** — Repair open in the wire between the ECM (B17) and the IAT sensor, then go to step 20.
- **NO** — Go to step 25.

### 18. Turn the ignition switch OFF.
### 19. Replace the IAT sensor (see page 11-384).
### 20. Reconnect all connectors.
### 21. Turn the ignition switch ON (II).
### 22. Reset the ECM with the HDS.
### 23. Do the ECM idle learn procedure (see page 11-462).
### 24. Check for Temporary DTCs or DTCs with the HDS.
**Is DTC P0113 indicated?**
- **YES** — Check for poor connections or loose terminals at the IAT sensor and the ECM, then go to step 1.
- **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

### 25. Turn the ignition switch OFF.
### 26. Reconnect all connectors.
### 27. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
### 28. Check for Temporary DTCs or DTCs with the HDS.
**Is DTC P0113 indicated?**
- **YES** — Check for poor connections or loose terminals at the IAT sensor and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then recheck. If the ECM was substituted, go to step 1.
- **NO** — If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

---
*Source Page Reference: 11-270*

---

### Printed page 11-271

<a id="p567"></a>
Source: [PDF p.567, printed p.11-271](../page-images/p0567.png).

# DTC P0116: ECT Sensor 1 Circuit Range/Performance Problem

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Check **ECT SENSOR 1** in the DATA LIST with the HDS.
   Is about 176 °F (80 °C) or higher, or 0.78 V or less indicated?
   - **YES** — Go to step 6.
   - **NO** — Go to step 3.

3. Note the value of **ECT SENSOR 1** in the DATA LIST with the HDS.
4. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
5. Check **ECT SENSOR 1** in the DATA LIST with the HDS.
   Does **ECT SENSOR 1** change 18 °F (10 °C) or more?
   - **YES** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at **ECT sensor 1** and the ECM.
   - **NO** — Go to step 11.

6. Note the value of **ECT SENSOR 1** in the DATA LIST with the HDS.
7. Turn the ignition switch OFF.
8. Open the engine hood, and let the engine cool for 3 hours.
9. Turn the ignition switch ON (II).
10. Check **ECT SENSOR 1** in the DATA LIST with the HDS.
    Does **ECT SENSOR 1** change 18 °F (10 °C) or more?
    - **YES** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at **ECT sensor 1** and the ECM.
    - **NO** — Go to step 11.

11. Turn the ignition switch OFF.
12. Replace **ECT sensor 1** (see page 11-385).
13. Turn the ignition switch ON (II).
14. Reset the ECM with the HDS.
15. Do the ECM idle learn procedure (see page 11-462).
16. Check for Temporary DTCs or DTCs with the HDS.
    Is DTC P0116 indicated?
    - **YES** — Check for poor connections or loose terminals at **ECT sensor 1** and the ECM, then go to step 1.
    - **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

Page Reference: 11-271
