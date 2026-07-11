# Engine Mechanical (4A-FE / 4A-GE)

*Section code: `EM` | PDF pages 10-75 of `Toyota-4A-FE-4A-GE-engine-repair-manual-OCR.pdf` | 66 pages*

> **Transcription in progress.** This is the largest, most engine-interleaved section.
> **Done so far:** Description (4A-FE), Troubleshooting (partial), Engine Tune-up (4A-FE).
> **Now also transcribed (via parallel agents, image-verified):** Compression check, DP
> system, full Troubleshooting, Timing Belt, and Cylinder Head (disassembly → installation).
> Cylinder Block detail is largely **absent from this scan**. Specs below are recorded
> as printed and cross-checked against the image-verified values elsewhere in this manual
> (Ignition, Charging) and the Service Specifications draft. See
> [llm-instructions.md](llm-instructions.md).
>
> **Heavy scan gaps** (this is the worst-abridged section — `check_page_continuity.py`
> flags ~24 numbered pages missing): pages jump EM-3 → EM-14 (EM-4…EM-13 absent), and
> EM-24 → EM-33 (EM-25…EM-32 absent), among others. Don't assume completeness.

## In this chapter (transcribed so far)

- [DESCRIPTION (4A-FE)](#p10) — [PDF p.10]
- [TROUBLESHOOTING](#p12) — [PDF p.12]
- [ENGINE TUNE-UP (4A-FE)](#p13) — [PDF p.13]

---
<a id="p10"></a>
**[PDF p.10]** — DESCRIPTION — 4A-FE ENGINE

The **4A-FE** engine is an in-line 4-cylinder 1.6 liter **DOHC 16-valve** engine, cylinders
numbered 1-2-3-4 from the front. Crankshaft supported by **5 bearings** (aluminum alloy) in
the crankcase, integrated with 8 cast balance weights; oil holes feed the connecting rods,
bearings, pistons, etc. **Firing order 1-3-4-2.**

---
<a id="p11"></a>
**[PDF p.11]** — DESCRIPTION (cont.)

- Cylinder head: aluminum alloy, cross-flow intake/exhaust, pent-roof combustion chambers, centrally located spark plugs.
- Intake manifold: 4 independent long ports using the inertial supercharging effect for low/medium-speed torque.
- Valves: irregular-pitch springs (special carbon steel). Exhaust camshaft driven by the timing belt; a gear on the exhaust camshaft drives the intake camshaft. Cam journals supported at 5 places.
- Valve clearance adjustment: **outer-shim type** (shims above the valve lifters) — shims can be replaced without removing the camshafts.
- Resin timing belt cover in 3 pieces; a service hole in the No.1 cover is for adjusting timing-belt tension.
- Pistons: temperature-resistant aluminum alloy with a valve-relief depression; semi-floating piston pins pressure-fit to the connecting rods.
- Rings: No.1 compression ring stainless steel, No.2 cast iron, oil ring steel/stainless combination.
- Cylinder block: cast iron with water jacket; pressed-steel oil pan with a dividing plate.

> **Scan gap:** EM-4 through EM-13 (remainder of the description, engine removal/installation,
> and any 4A-GE description) are not present in this scan.

---
<a id="p12"></a>
**[PDF p.12]** — TROUBLESHOOTING (4A-GE page present; excessive fuel consumption / unpleasant odor)

Only the tail of the troubleshooting tables survived the scan (the page is titled 4A-GE).
Representative rows as printed:

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| Poor gasoline mileage | Fuel leak; air cleaner clogged; incorrect ignition timing; EFI problems (injector, deceleration fuel-cut); idle speed too high; spark plug faulty; EGR always on; low compression; tires under-inflated; clutch slips; brakes drag | Repair / check as noted | EM-25, EM-28, EM-30/31, IG-11/12, EM-38 |
| Unpleasant odor | Incorrect idle speed; incorrect ignition timing; vacuum leaks (PCV, EGR, intake manifold, throttle body, brake booster); EFI problems | Adjust / repair as noted | EM-30/31, EM-28 |

> **Scan gap:** the bulk of the troubleshooting section (symptom tables preceding this page)
> is missing.

---
<a id="p13"></a>
**[PDF p.13]** — ENGINE TUNE-UP (4A-FE) — coolant, oil, battery, air filter, cords, plugs, drive belt

- INSPECTION OF ENGINE COOLANT — see [Cooling p.174](04-cooling-system.md#p174).
- INSPECTION OF ENGINE OIL — see [Lubrication p.193](05-lubrication-system.md#p193).
- INSPECTION OF BATTERY — **Standard specific gravity: 1.25 – 1.27 when fully charged at 20°C (68°F).**
- INSPECTION OF AIR FILTER — visually check the element (not excessively dirty/damaged/oily); clean with compressed air (blow from the back first, then the front).
- INSPECTION OF HIGH-TENSION CORDS — see [Ignition p.201](06-ignition-system.md#p201). **Maximum resistance: 25 kΩ per cord.** <!-- NEEDS REVIEW: this tune-up page OCR'd "25 Ω" (missing the "k"); the IG-7 detail page (image-verified) shows 25 kΩ. -->
- INSPECTION OF SPARK PLUGS — see [Ignition p.201](06-ignition-system.md#p201). **Correct electrode gap: 0.8 mm (0.031 in.). Recommended plugs: ND Q16R-U, NGK BCPR5EY.**
- INSPECTION OF ALTERNATOR DRIVE BELT — see [Charging p.215](08-charging-system.md#p215). **Deflection: used belt 10.0–12.0 mm (0.394–0.472 in.), new belt 8.5–10.5 mm (0.335–0.413 in.). Tension (reference): used 40–55 kg, new 60–70 kg.**

---
<a id="p14"></a>
**[PDF p.14]** — TUNE-UP: INSPECTION AND ADJUSTMENT OF VALVE CLEARANCE

> **HINT:** Inspect and adjust valve clearance when the engine is **cold**.

1. Disconnect the high-tension cords from the spark plugs.
2. Remove the cylinder head cover (see EM-62).
3. **SET No.1 CYLINDER TO TDC/COMPRESSION** — turn the crankshaft pulley to align its groove with the "0" timing mark on the No.1 timing belt cover; check that No.1 cylinder lifters are loose and No.4 are tight (if not, turn the crankshaft one revolution / 360° and realign).
4. **INSPECT VALVE CLEARANCE** — using a thickness gauge, measure between the valve lifter and camshaft for the indicated valves; record out-of-spec readings. **Valve clearance (cold): Intake 0.15 – 0.25 mm (0.006 – 0.010 in.); Exhaust 0.20 – 0.30 mm (0.008 – 0.012 in.).** Turn the crankshaft 360° and measure the remaining indicated valves.

---
<a id="p15"></a>
**[PDF p.15]** — TUNE-UP: ADJUST VALVE CLEARANCE (shim selection)

5. **ADJUST VALVE CLEARANCE**
   a. Remove the adjusting shim: turn the crankshaft to point the cam lobe up; using **SST 09248-55010** (A) press down the valve lifter and place SST (B) between camshaft and lifter; remove the shim with a small screwdriver and magnetic finger.
   b. **Determine the replacement shim** by formula (T = shim used, A = measured clearance, N = new shim):
      - **Intake: N = T + (A − 0.20 mm / 0.008 in.)**
      - **Exhaust: N = T + (A − 0.25 mm / 0.010 in.)**
      > **HINT:** Shims come in **17 sizes in 0.05 mm (0.0020 in.) steps, from 2.50 mm (0.0984 in.) to 3.30 mm (0.1299 in.)**.
   c. Install a new shim (press down the lifter with SST (A), remove SST (B)); recheck the clearance.
6. Install the cylinder head cover (see EM-86).
7. Reconnect the high-tension cords.

---
<a id="p16"></a>
**[PDF p.16]** — TUNE-UP: Adjusting Shim Selection Chart — INTAKE

Large lookup matrix (measured clearance × installed shim → new shim number) — **image on
[PDF p.16]**; use the formula above for the same result. Shim size table:

| No. | mm (in.) | No. | mm (in.) |
| --- | -------- | --- | -------- |
| 02 | 2.500 (0.0984) | 20 | 2.950 (0.1161) |
| 04 | 2.550 (0.1004) | 22 | 3.000 (0.1181) |
| 06 | 2.600 (0.1024) | 24 | 3.050 (0.1201) |
| 08 | 2.650 (0.1043) | 26 | 3.100 (0.1220) |
| 10 | 2.700 (0.1063) | 28 | 3.150 (0.1240) |
| 12 | 2.750 (0.1083) | 30 | 3.200 (0.1260) |
| 14 | 2.800 (0.1102) | 32 | 3.250 (0.1280) |
| 16 | 2.850 (0.1122) | 34 | 3.300 (0.1299) |
| 18 | 2.900 (0.1142) | | |

*Example (intake): a 2.800 mm shim installed, measured clearance 0.450 mm → replace with shim No. 24 (3.050 mm).*

---
<a id="p17"></a>
**[PDF p.17]** — TUNE-UP: Adjusting Shim Selection Chart — EXHAUST

Exhaust shim-selection matrix — **image on [PDF p.17]**; same shim sizes as the intake
table above, exhaust target clearance 0.20–0.30 mm (use the exhaust formula).

---
<a id="p18"></a>
**[PDF p.18]** — TUNE-UP: IGNITION TIMING

1. WARM UP ENGINE to normal operating temperature.
2. CONNECT TACHOMETER — connect the test probe to terminal **IG⊖** of the check connector (location: see FI-133).
   > **NOTICE:** Never let the tachometer terminal touch ground (damages the igniter/coil). Confirm tachometer compatibility first.
3. **INSPECT AND ADJUST IGNITION TIMING**
   a. Using **SST 09843-18020**, connect terminals **TE1 and E1** of the check connector.
   b. With a timing light, check the timing. **Ignition timing: 10° BTDC @ idle (transmission in neutral).** If needed, loosen the distributor bolts and turn the distributor; recheck. **Distributor bolt torque: 200 kg-cm (14 ft-lb, 20 N·m).**

---
<a id="p19"></a>
**[PDF p.19]** — TUNE-UP: IGNITION TIMING (further check)

4. **FURTHER CHECK IGNITION TIMING** — remove SST from the check connector (SST 09843-18020); check timing. **Ignition timing: 5 – 15° BTDC @ idle (transmission in neutral).**
   > **HINT:** The timing mark moves in a range between 5° and 15°.
5. Disconnect the tachometer and timing light.

---
<a id="p20"></a>
**[PDF p.20]** — TUNE-UP: IDLE SPEED (w/ TWC)

1. **INITIAL CONDITIONS** — air cleaner installed; normal operating temperature; all air-induction pipes/hoses connected; all vacuum lines connected (incl. EGR); accessories off; EFI connectors fully plugged; ignition timing correct; transmission in neutral.
2. Warm up the engine.
3. Connect the tachometer (see EM-20).
4. Check air valve operation (see FI-131).
5. **INSPECT AND ADJUST IDLE SPEED** — **Idle speed: 800 rpm (w/ cooling fan OFF).** If not as specified, adjust via the IDLE SPEED ADJUSTING SCREW.

---
<a id="p21"></a>
**[PDF p.21]** — TUNE-UP: IDLE SPEED AND IDLE MIXTURE (w/o TWC)

1. INITIAL CONDITIONS — as above, plus HC/CO meter operating normally.
2. Warm up the engine. 3. Connect tachometer (see EM-20). 4. Check air valve operation (see FI-131).
5. **INSPECT AND ADJUST IDLE SPEED** — **Idle speed: 800 rpm (w/ cooling fan OFF).**
6. **ADJUST IDLE MIXTURE**
   > **NOTICE:** Always use an HC/CO meter. In most good-condition vehicles no idle-mixture adjustment is needed. **If no CO meter is available, DO NOT attempt to adjust idle mixture.**
   a. Race the engine at 2,500 rpm for ~90 seconds.
   b. Insert the testing probe at least **40 cm (1.3 ft)** into the tailpipe.
   c. Measure 1–3 minutes after racing (to stabilize). **Idle CO concentration: 1.5 ± 0.5 % (w/ cooling fan OFF).**

---
<a id="p22"></a>
**[PDF p.22]** — TUNE-UP: idle mixture (cont.) · HC/CO troubleshooting

If CO is out of spec, adjust the IDLE MIXTURE ADJUSTING SCREW in the variable resistor;
recheck idle speed afterward. If CO can't be corrected by mixture adjustment, see the
HC/CO troubleshooting table:

| HC | CO | Symptom | Causes |
| -- | -- | ------- | ------ |
| High | Normal | Rough idle | Faulty ignition (timing, fouled/shorted/misgapped plugs, open/crossed wires, cracked IIA cap); incorrect valve clearance; leaky EGR valve; leaky intake/exhaust valves; leaky cylinder |
| High | Low | Rough idle (fluctuating HC) | Vacuum leak: vacuum hose, EGR valve, intake manifold, PCV line, throttle body |

> **Scan gap:** EM-25 through EM-32 (compression check and the remainder of the tune-up /
> troubleshooting cluster) are missing; the section resumes at EM-33 (Timing Belt), which is
> **not yet transcribed** here.

---

## Remaining sections (physical p23–75) — transcribed by image-verified agents

> **Important — this scan's physical pages are out of logical order.** The section's own
> page codes jump around within the PDF (e.g. physical p23=EM-33, but p28–32=EM-6…10).
> The blocks below are in **physical-page order** (so every `[PDF p.N]` link is correct);
> the EM-code in each heading tells you the logical position. Read by the EM-code, not by
> scroll order. Numerous pages are missing (abridged scan).

---
<a id="p23"></a>
**[PDF p.23]** — ENGINE MECHANICAL — Idle HC/CO Concentration Method (w/ TWC) — EM-33

# IDLE HC/CO CONCENTRATION CHECK METHOD (w/ TWC)

> **HINT:** This check is used only to determine whether or not the idle HC/CO complies with regulations.

1. **INITIAL CONDITIONS**
   a. Engine to reach normal operating temperature
   b. Air cleaner installed
   c. All pipes and hoses of air induction system connected
   d. All accessories switched off
   e. All vacuum lines properly connected

   > **HINT:** All vacuum hoses for EGR systems, etc. should be properly connected.

   f. EFI system wiring connectors fully plugged
   g. Ignition timing set correctly
   h. Transmission in neutral range
   i. Tachometer and HC/CO meter calibrated and at hand.

2. **START ENGINE**

3. **CHECK IDLE SPEED**
   **Idle speed: 800 rpm**

4. **CHECK OXYGEN SENSOR OPERATION**
   a. Using SST, connect the terminal TE1 and E1 of the check connector.
      **SST 09843-18020**
   b. Connect the positive (+) probe of a voltmeter to terminal VF1 of the check connector, and negative (−) probe to terminal E1.
   c. Hold the engine speed at **2,500 rpm** for approx. **90 seconds** to warm up the oxygen sensor.
   d. Then, maintaining engine at **2,500 rpm**, count how many times the needle of the voltmeter fluctuates between **0 and 5 V**.

   **Minimum needle fluctuation:**
   **4A-FE — 8 times for every 10 seconds**

   If the fluctuation is less than minimum, check the air induction system. If necessary, see EFI SYSTEM.

*(Left-column images: check connector with SST showing E1 / TE1 terminals [EM7502]; voltmeter connected to E1 / TE1 / VF1 terminals [EM7501].)*

---
<a id="p24"></a>
**[PDF p.24]** — EM-34 — ENGINE MECHANICAL — Idle HC/CO Concentration Method (w/ TWC)

5. **RACE ENGINE AT 2,500 RPM FOR APPROX. 120 SECONDS**

6. **INSERT CO METER TESTING PROBE INTO TAILPIPE AT LEAST 40 cm (1.3 ft)**

7. **CHECK HC/CO CONCENTRATION AT IDLE**
   Wait at least one minute before measuring to allow the concentration to stabilize. Complete the measuring within three minutes.

   **Idle CO concentration: 0 − 0.5 %**
   **(w/ Cooling fan OFF)**

   If the HC/CO concentration does not conform to regulations, see the table below for possible causes.

*(Left-column image: HC/CO meter probe inserted into vehicle tailpipe [EM6862].)*

## Troubleshooting

| HC | CO | SYMPTOMS | CAUSES |
|----|----|----------|--------|
| High | Normal | Rough idle | 1. Faulty ignition:<br>• Incorrect timing<br>• Fouled, shorted or improperly gapped plugs<br>• Open or crossed ignition wires<br>• Cracked IIA or distributor cap<br>2. Incorrect valve clearance<br>3. Leaky EGR valve (w/ EGR system)<br>4. Leaky intake and exhaust valves<br>5. Leaky cylinder |
| High | Low | Rough idle<br><br>(Fluctuating HC reading) | 1. Vacuum leak:<br>• Vacuum hose<br>• EGR valve (w/ EGR system)<br>• Intake manifold<br>• PCV line<br>• Throttle body<br>• Cylinder head gasket<br>• Brake booster line<br>2. Lean mixture causing misfire |
| High | High | Rough idle<br><br>(Black smoke from exhaust) | 1. Clogged air filter<br>2. Plugged PCV valve (4A-FE)<br>3. Faulty EFI system<br>• Faulty pressure regulator<br>• Clogged fuel return line<br>• Faulty air flow meter (w/ air flow meter)<br>• Faulty vacuum sensor (w/o air flow meter)<br>• Defective water temp. sensor<br>• Defective intake air temp. sensor<br>• Faulty ECU<br>• Faulty injector<br>• Faulty cold start injector<br>• Faulty throttle position sensor |

---
<a id="p25"></a>
**[PDF p.25]** — ENGINE MECHANICAL — Inspection and Adjustment of Dash Pot (DP) System (4A-FE) — EM-35

# INSPECTION AND ADJUSTMENT OF DASH POT (DP) SYSTEM (4A-FE)

1. **WARM UP AND STOP ENGINE**
   Allow the engine to reach normal operating temperature.

2. **CHECK IDLE SPEED (See page EM-22, 23)**

3. **REMOVE COVER (2WD), CAP, FILTER AND SEPARATOR FROM DP**

4. **ADJUST DP SETTING SPEED**
   a. (2WD)
      Using SST, connect terminals TE1 and E1 of the check connector.
      **SST 09843-18020**
      LOCATION: See page FI-133
   b. (2WD w/ EGR system)
      Disconnect the VSV connector.
   c. Race the engine at **3,500 rpm** for a few seconds.
   d. Plug the VTV hole with your finger.
   e. Release the throttle valve.
   f. Check the DP setting speed.

   **DP setting speed: M/T 1,800 rpm**
   **(w/ Cooling fan OFF)**

   *(Additional tachometer callouts in figures: **3,500 rpm**; **1,800 rpm (M/T)**; **2,200 rpm (A/T)**.)*

*(Left-column images: DP components exploded view — Separator / Filter / Cap / Cover (2WD) [EC3679]; check connector with SST E1 / TE1 [EM7502]; VTV hole location under hood [EM6985]; tachometer at 3,500 rpm with VTV hole [EC0138 EM4877]; tachometer showing 1,800 rpm (M/T) / 2,200 rpm (A/T) [EC0137].)*

---
<a id="p26"></a>
**[PDF p.26]** — EM-36 — ENGINE MECHANICAL — Inspection and Adjustment of Dash Pot (DP) System (4A-FE)

4. (continued)
   g. Adjust the DP setting speed by turning the DP ADJUSTING SCREW.
   h. Repeat steps from (c) to (e), and recheck the DP setting speed.
   i. (2WD w/ EGR system)
      Connect the VSV connector.
   j. (2WD)
      Remove SST from the check connector.
      **SST 09843-18020**

5. **REINSTALL DP SEPARATOR, FILTER, CAP AND COVER (2WD)**
   > **HINT:** When installing the cover, install it with the ventilate holes below.

6. **CHECK VTV OPERATION**
   Race the engine at **3,500 rpm** for a few seconds, release the throttle valve and check that the engine returns to idle in a few seconds.

*(Left-column images: hexagonal wrench on DP adjusting screw [EM4878]; VSV connector under hood [EM6985]; SST at check connector [EM7503]; DP components exploded view with Ventilate Hole callout — Separator / Filter / Cap / Cover (2WD) [EC3679]; tachometer at 3,500 rpm / "A Few Seconds" stopwatch, Idle [EC0142 EC0147].)*

> **Scan gap:** page EM-37 is missing from this scan (running code jumps from EM-36 to EM-38).

---
<a id="p27"></a>
**[PDF p.27]** — EM-38 — ENGINE MECHANICAL — Compression Check

# COMPRESSION CHECK

> **HINT:** If there is lack of power, excessive oil consumption or poor fuel economy, measure the compression pressure.

1. **WARM UP AND STOP ENGINE**

2. **DISCONNECT COLD START INJECTOR CONNECTOR**

3. **DISCONNECT DISTRIBUTOR CONNECTOR(S)**

4. **(4A-GE) REMOVE PLUG CORD COVER**

5. **REMOVE SPARK PLUGS (See page IG-7, 11)**

6. **CHECK CYLINDER COMPRESSION PRESSURE**
   a. Insert a compression gauge into the spark plug hole.
   b. Fully open the throttle.
   c. While cranking the engine, measure the compression pressure.

   > **HINT:** Always use a fully charged battery to obtain engine revolution of 250 rpm or more.

   d. Repeat steps (a) through (c) for each cylinder.

   > **NOTICE:** This measurement must be done in as short a time as possible.

   **Compression pressure:**
   **4A-FE — 13.5 kg/cm² (191 psi, 1,320 kPa)**

   **Minimum pressure:**
   **10.0 kg/cm² (142 psi, 981 kPa)**

   **Difference between each cylinder:**
   **1.0 kg/cm² (14 psi, 98 kPa) or less**

   e. If the cylinder compression in one or more cylinders is low, pour a small amount of engine oil into the cylinder through the spark plug hole and repeat steps (a) through (c) for the cylinder with low compression.
      • If adding oil helps the compression, chances are that the piston rings and/or cylinder bore are worn or damaged.
      • If pressure stays low, a valve may be sticking or seating improperly, or there may be leakage past the gasket.

7. **REINSTALL SPARK PLUGS (See page IG-8, 12)**
   **Torque: 180 kg-cm (13 ft-lb, 18 N·m)**

8. *(step number printed with no text on this page)* <!-- NEEDS REVIEW: step 8 heading blank in scan; likely "(4A-GE) REINSTALL PLUG CORD COVER" but not legible -->

9. **RECONNECT DISTRIBUTOR CONNECTOR(S)**

10. **RECONNECT COLD START INJECTOR CONNECTOR**

*(Left-column image: 4A-FE — compression gauge inserted in spark plug hole [labeled "4A-FE", "Compression Gauge"].)*

> **Scan gap:** running page code jumps backward from EM-38 to EM-6 at the next physical page — the 4A-FE troubleshooting pages (EM-6 to EM-10) are bound out of sequence in this scan.

---
<a id="p28"></a>
**[PDF p.28]** — EM-6 — ENGINE MECHANICAL — Troubleshooting (4A-FE)

# TROUBLESHOOTING (4A-FE)

## ENGINE OVERHEATING

| Problem | Possible cause | Remedy | Page |
|---------|----------------|--------|------|
| Engine overheats | Cooling system faulty | Troubleshoot cooling system | CO-4 |
| | Incorrect ignition timing | Reset timing | EM-20 |

## HARD STARTING

| Problem | Possible cause | Remedy | Page |
|---------|----------------|--------|------|
| Engine will not crank or cranks slowly | Starting system faulty | Troubleshoot starting system | ST-2 |
| Engine will not start / hard to start (cranks OK) | No fuel supply to carburetor<br>• No fuel in tank<br>• Fuel pump not working<br>• Fuel line clogged or leaking<br>EFI system problems | Troubleshoot EFI system<br><br><br><br>Repair as necessary | FI-10 |
| | Ignition problems<br>• Ignition coil<br>• Igniter<br>• Distributor (IIA) | Perform spark test | IG-6 |
| | Spark plugs faulty | Inspect plugs | IG-7 |
| | High-tension cords disconnected or broken | Inspect cords | IG-7 |
| | Vacuum leaks<br>• PCV line<br>• EGR line (w/ EGR system)<br>• Intake manifold<br>• Throttle body<br>• Brake booster line | Repair as necessary | |
| | Low compression | Check compression | EM-38 |

---
<a id="p29"></a>
**[PDF p.29]** — ENGINE MECHANICAL — Troubleshooting (4A-FE) — EM-7

## ROUGH IDLING

| Problem | Possible cause | Remedy | Page |
|---------|----------------|--------|------|
| Rough idle, stalls or misses | Spark plugs faulty | Inspect plugs | IG-7 |
| | High-tension cords faulty | Inspect cords | IG-7 |
| | Ignition wiring faulty | Inspect wiring | |
| | Ignition problems<br>• Ignition coil<br>• Igniter<br>• Distributor (IIA) | Inspect coil<br>Inspect igniter<br>Inspect IIA | |
| | Incorrect ignition timing | Reset timing | EM-20 |
| | Incorrect valve clearance | Adjust valve clearance | EM-16 |
| | Vacuum leaks<br>• PCV line<br>• EGR line (w/ EGR system)<br>• Intake manifold<br>• Throttle body<br>• Brake booster line | Repair as necessary | |
| | Incorrect idle speed | Adjust idle speed | EM-22, 23 |
| | EFI system problems<br>EGR valve faulty (w/ EGR system) | Repair as necessary<br>Check EGR valve | |
| | Engine overheats | Check cooling system | |
| | Low compression | Check compression | EM-38 |

---
<a id="p30"></a>
**[PDF p.30]** — EM-8 — ENGINE MECHANICAL — Troubleshooting (4A-FE)

## ENGINE HESITATES/POOR ACCELERATION

| Problem | Possible cause | Remedy | Page |
|---------|----------------|--------|------|
| Engine hesitates / poor acceleration | Spark plugs faulty | Inspect plugs | IG-7 |
| | High-tension cords faulty | Inspect cords | IG-7 |
| | Vacuum leaks<br>• PCV line<br>• EGR line (w/ EGR system)<br>• Intake manifold<br>• Throttle body<br>• Brake booster line | Repair as necessary | |
| | Incorrect ignition timing | Reset timing | EM-20 |
| | Incorrect valve clearance | Adjust valve clearance | EM-16 |
| | Fuel system clogged | Check fuel system | |
| | Air cleaner clogged | Check air cleaner | EM-15 |
| | EFI system problems | Repair as necessary | |
| | Engine overheats | Check cooling system | CO-4 |
| | Low compression | Check compression | EM-38 |

## ENGINE DIESELING

| Problem | Possible cause | Remedy | Page |
|---------|----------------|--------|------|
| Engine dieseling (runs after ignition switch is turned off) | EFI system problems | Repair as necessary | |
| | Incorrect ignition timing | Reset timing | EM-20 |
| | EGR system faulty (w/ EGR system) | Check EGR system | |

---
<a id="p31"></a>
**[PDF p.31]** — ENGINE MECHANICAL — Troubleshooting (4A-FE) — EM-9

## AFTER FIRE, BACKFIRE

| Problem | Possible cause | Remedy | Page |
|---------|----------------|--------|------|
| Muffler explosion (after fire) on deceleration only | Deceleration fuel cut system always off | Check fuel cut system | |
| | DP system always off | Check DP system | |
| Muffler explosion (after fire) all the time | Air cleaner clogged | Check air cleaner | EM-15 |
| | EFI system problem | Repair as necessary | |
| | Incorrect ignition timing | Reset timing | EM-20 |
| | Incorrect valve clearance | Adjust valve clearance | EM-16 |
| Engine backfires | EFI system problem | Repair as necessary | |
| | Vacuum leak<br>• PCV hoses<br>• Intake manifold<br>• Throttle body<br>• Brake booster line | Check hoses and repair as necessary | |
| | Insufficient fuel flow | Troubleshoot fuel system | |
| | Incorrect ignition timing | Reset timing | EM-20 |
| | Incorrect valve clearance | Adjust valve clearance | EM-16 |
| | Carbon deposits in combustion chambers | Inspect cylinder head | EM-68 |

## EXCESSIVE OIL CONSUMPTION

| Problem | Possible cause | Remedy | Page |
|---------|----------------|--------|------|
| Excessive oil consumption | Oil leak | Repair as necessary | |
| | PCV line clogged | Check PCV system | |
| | Piston ring worn or damaged | Check rings | EM-130 |
| | Valve stem and guide bushing worn | Check valves and guide bushings | EM-70 |
| | Valve stem oil seal worn or damaged | Check oil seals | |

---
<a id="p32"></a>
**[PDF p.32]** — EM-10 — ENGINE MECHANICAL — Troubleshooting (4A-FE)

## POOR GASOLINE MILEAGE

| Problem | Possible cause | Remedy | Page |
|---------|----------------|--------|------|
| Poor gasoline mileage | Fuel leak | Repair as necessary | |
| | Air cleaner clogged | Check air cleaner | |
| | Incorrect ignition timing | Reset timing | EM-20 |
| | EFI system problems<br>• Injector faulty<br>• Deceleration fuel cut system faulty | Repair as necessary | |
| | Idle speed too high | Adjust idle speed | EM-22, 23 |
| | Spark plugs faulty | Inspect plugs | IG-7 |
| | EGR system always on (w/ EGR system) | Check EGR system | |
| | Low compression | Check compression | EM-38 |
| | Tires improperly inflated | Inflate tires to proper pressure | |
| | Clutch slips | Troubleshoot clutch | |
| | Brakes drag | Troubleshoot brakes | |

## UNPLEASANT ODOR

| Problem | Possible cause | Remedy | Page |
|---------|----------------|--------|------|
| Unpleasant odor | Incorrect idle speed | Adjust idle speed | EM-22, 23 |
| | Incorrect ignition timing | Reset timing | EM-20 |
| | Vacuum leaks<br>• PCV line<br>• EGR line (w/ EGR system)<br>• Intake manifold<br>• Throttle body<br>• Brake booster line | Repair as necessary | |
| | EFI system problems | Repair as necessary | |

> **Scan gap:** running page code jumps forward from EM-10 to EM-39 at the next physical page; pages EM-11 through EM-38 are not present in this range (EM-33..EM-36 and EM-38 appeared earlier at p23–p27).

---
<a id="p33"></a>
**[PDF p.33]** — ENGINE MECHANICAL — Timing Belt (4A-FE) — EM-39

# TIMING BELT (4A-FE)
## COMPONENT

Exploded-view component diagram [EM6978] with specified torques (**kg-cm (ft-lb, N·m)** = specified torque):

| Fastener / location | Torque |
|---------------------|--------|
| Camshaft Timing Pulley bolt | **600 (43, 69)** |
| Idler Pulley bolt | **375 (27, 37)** |
| Crankshaft Pulley bolt | **1,200 (87, 118)** |

Components identified: No.3 Timing Belt Cover, Engine Wire Bracket, Water Pump Pulley, Camshaft Timing Pulley, No.2 Timing Belt Cover, Drive Belt, No.1 Timing Belt Cover, Idler Pulley, Tension Spring, Crankshaft Timing Pulley, Timing Belt, Timing Belt Guide, Crankshaft Pulley.

## REMOVAL OF TIMING BELT

1. **REMOVE DRIVE BELT AND WATER PUMP PULLEY**

2. **REMOVE SPARK PLUGS (See page IG-7)**

3. **REMOVE CYLINDER HEAD COVER (See steps 8 and 12 on pages EM-60 and 62)**

4. **SET NO.1 CYLINDER TO TDC/COMPRESSION**
   a. Turn the crankshaft pulley and align its groove with the timing mark "O" of the No.1 timing belt cover.
   b. Check that the hold of the camshaft timing pulley is aligned with the timing mark of the bearing cap.

   If not, turn the crankshaft one revolution (360°).

*(Left-column image: aligning crankshaft pulley groove with timing mark, close-up of timing scale [EM6238].)*

---
<a id="p34"></a>
**[PDF p.34]** — EM-40 — ENGINE MECHANICAL — Timing Belt (4A-FE)

5. **REMOVE CRANKSHAFT PULLEY**
   a. Using SST to hold the crankshaft pulley, remove the pulley bolt.
      **SST 09213-14010 and 09330-00021**
   b. Using SST, remove the pulley.
      **SST 09213-31021**

6. **REMOVE TIMING BELT COVERS**
   Remove the nine bolts, engine wire bracket and timing belt covers.

7. **REMOVE TIMING BELT GUIDE**

8. **REMOVE TIMING BELT AND IDLER PULLEY**
   > **HINT:** If reusing the timing belt, draw a direction arrow on the belt (in the direction of engine revolution), and place matchmarks on the pulleys and belt as shown in the illustration.

   a. Remove the bolt, idler pulley and tension spring.
   b. Remove the belt.

*(Left-column images: SST holding crankshaft pulley to loosen bolt [EM4145]; SST removing pulley [EM4242]; timing belt cover bolt locations [EM6239]; matchmarks on pulleys and belt [EM4273]; idler pulley and tension spring removal [EM7005].)*

---
<a id="p35"></a>
**[PDF p.35]** — ENGINE MECHANICAL — Timing Belt (4A-FE) — EM-41

9. **REMOVE CRANKSHAFT TIMING PULLEY**
   If the pulley cannot be removed by hand, use two screwdrivers.
   > **NOTICE:** Position shop rags as shown to prevent damage.

10. **REMOVE CAMSHAFT TIMING PULLEY**
    Hold the hexagonal head wrench portion of the camshaft with a wrench, and remove the bolt and timing pulley.
    > **NOTICE:** Be careful not to damage the cylinder head with the wrench.

*(Left-column images: removing crankshaft timing pulley with two screwdrivers and shop rags [EM7028]; holding camshaft hexagonal portion with wrench while removing bolt/pulley [EM7453].)*

---
<a id="p36"></a>
**[PDF p.36]** — EM-42 — ENGINE MECHANICAL — Timing Belt (4A-FE)

## INSPECTION OF TIMING COMPONENTS

1. **INSPECT TIMING BELT**
   > **NOTICE:**
   > • Do not bend, twist or turn the timing belt inside out.
   > • Do not allow the timing belt to come into contact with oil, water or steam.
   > • Do not utilize timing belt tension when installing or removing the mount bolt of the camshaft timing pulley.

   If there are any defects as shown in the illustrations, check the following points:
   a. Premature splitting
      • Check the proper installation.
      • Check the timing cover gasket for damage and proper installation.
   b. If the belt teeth are cracked or damaged, check to see if either camshaft or water pump is locked.
   c. If there is noticeable wear or cracks on the belt face, check to see if there are nicks on one side of the idler pulley lock.
   d. If there is wear or damage on only one side of the belt, check the belt guide and the alignment of each pulley.

*(Left-column images — belt defect illustrations: "No!" — do-not-bend / oil-contact examples [EM4274]; premature splitting [EM4275]; cracked/damaged belt teeth [EM4276]; wear/cracks on belt face [EM4277]; wear on one side of belt [EM4278].)*
---
<a id="p37"></a>
**[PDF p.37]** — ENGINE MECHANICAL — Timing Belt (4A-FE) — EM-43

*(Continuation of timing belt inspection)*

(e) If there is noticeable wear on the belt teeth, check the timing cover for damage and check for correct gasket installation and for foreign material on the pulley teeth.

If necessary, replace the timing belt.

*(image only — belt teeth wear, see [PDF p.37])*

### 2. INSPECT IDLER PULLEY

Check the turning smoothness of the idler pulley.

If necessary, replace the idler pulley.

*(image only — idler pulley, see [PDF p.37])*

### 3. INSPECT TENSION SPRING

(a) Measure the free length of the tension spring.

**Free length: 38.4 mm (1.512 in.)**

If the free length is not as specified, replace the tension spring.

(b) Measure the tension of the tension spring at the specified installed length.

**Installed tension: 3.6 – 4.0 kg (7.9 – 8.8 lb, 35 – 39 N·m) at 50.2 mm (1.976 in.)**

<!-- NEEDS REVIEW: printed page shows tension unit as "N·m"; a spring tension is a force (should read N). Kept exactly as printed. -->

If the tension is not as specified, replace the tension spring.

---
<a id="p38"></a>
**[PDF p.38]** — ENGINE MECHANICAL — Timing Belt (4A-FE) — EM-44

## INSTALLATION OF TIMING BELT
(See page EM-39)

### 1. INSTALL CAMSHAFT TIMING PULLEY

(a) Align the camshaft knock pin with the knock pin groove of the pulley, and slide on the pulley.

(b) Temporarily install the timing pulley bolt.

(c) Hold the hexagonal wrench head portion of the camshaft with a wrench, and tighten the timing pulley bolt.

**Torque: 600 kg-cm (43 ft-lb, 59 N·m)**

(d) Turn the hexagonal wrench head portion of the camshaft, and align the hole of the camshaft timing pulley with the timing mark of the bearing cap.

### 2. INSTALL CRANKSHAFT TIMING PULLEY

(a) Align the pulley set key with the key groove of the pulley.

(b) Slide on the timing pulley, facing the flange side inward.

(c) Using the crankshaft pulley bolt, turn the crankshaft and align the timing marks of the crankshaft timing pulley and oil pump body.

### 3. TEMPORARILY INSTALL IDLER PULLEY AND TENSION SPRING

(a) Install the idler pulley with the bolt. Do not tighten the bolt yet.

(b) Install the tension spring.

(c) Push the pulley toward the left as far as it will go and tighten the bolt.

### 4. INSTALL TIMING BELT

> **NOTICE:** The engine should be cold.

> **HINT:** If reusing the timing belt, align the points marked during removal, and install the belt with the arrow pointing in the direction of engine revolution.

---
<a id="p39"></a>
**[PDF p.39]** — ENGINE MECHANICAL — Timing Belt (4A-FE) — EM-45

### 5. CHECK VALVE TIMING AND TIMING BELT TENSION

(a) Loosen the idler pulley bolt.

(b) Temporarily install the crank pulley bolt and turn the crankshaft two revolutions from TDC to TDC.

> **HINT:** Always turn the crankshaft clockwise.

(c) Check the valve timing. Ensure that each pulley aligns with the marks as shown in the illustration.

(d) Tighten the timing belt idler pulley mount bolt.

**Torque: 375 kg-cm (27 ft-lb, 37 N·m)**

(e) Remove the temporarily installed crank pulley bolt.

**(Reference)**

(a) Measure the timing belt deflection as shown in the illustration.

**Deflection: 5 – 6 mm (0.20 – 0.24 in.) at 2 kg (4.4 lb, 20 N)**

---
<a id="p40"></a>
**[PDF p.40]** — ENGINE MECHANICAL — Timing Belt (4A-FE) — EM-46

(b) If the measured value is not within standard, readjust with the idler pulley.

### 6. INSTALL TIMING BELT GUIDE

Install the guide, facing the cup side outward.

### 7. INSTALL TIMING BELT COVERS

(a) Install the No.1 timing belt cover with the three bolts.

(b) Install the No.2, No.3 timing belt covers and engine wire bracket with the six bolts.

**Torque: 80 kg-cm (69 in.-lb, 7.8 N·m)**

### 8. INSTALL CRANKSHAFT PULLEY

(a) Align the pulley set key with the key groove of the pulley, slide on the pulley.

(b) Temporarily install the pulley bolt.

**SST 09213-14010 and 09330-00021**

**Torque: 1,200 kg-cm (87 ft-lb, 118 N·m)**

### 9. INSTALL CYLINDER HEAD COVER
(See steps 14 and 18 on pages EM-86 and 88)

### 10. INSTALL SPARK PLUGS (See page IG-8)

**Torque: 180 kg-cm (13 ft-lb, 18 N·m)**

### 11. INSTALL WATER PUMP PULLEY AND DRIVE BELT

### 12. CHECK AND ADJUST DRIVE BELT
(See step 3 on pages CH-3 and 4)

> **Scan gap:** pages EM-47 to EM-55 are missing from this scan.

---
<a id="p41"></a>
**[PDF p.41]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-56

## CYLINDER HEAD (4A-FE)
### COMPONENTS — 2WD

*(Exploded-view diagram. Torque callouts shown as **kg-cm (ft-lb, N·m)**.)*

Specified torque callouts (from diagram):

| Location | Torque |
|---|---|
| Intake manifold | **195 (14, 19)** kg-cm (ft-lb, N·m) |
| Gasket / injector (upper) | **180 (13, 18)** kg-cm (ft-lb, N·m) |
| Delivery pipe | **300 (22, 29)** kg-cm (ft-lb, N·m) |
| (valve gear area) | **130 (9, 13)** kg-cm (ft-lb, N·m) |
| Camshaft bearing cap | **610 (44, 60)** kg-cm (ft-lb, N·m) |
| Exhaust manifold | **260 (18, 25)** kg-cm (ft-lb, N·m) |

Components labeled: Intake Manifold, Gasket (◆), Cold Start Injector Pipe, Delivery Pipe, Intake Manifold Stay, Cylinder Head Cover, Cylinder Head Cover Gasket, PCV Hose, Spark Plug Tube Gasket, Adjusting Shim, Valve Lifter, Valve Keepers, Valve Spring Retainer, Valve Spring, Valve Stem Oil Seal (◆), Spring Seat, Valve Guide Bushing, Valve, Camshaft Bearing Cap, Camshaft Sub-gear, Snap Ring, Wave Ring, Oil Seal (◆), Camshaft Gear Spring, Exhaust Camshaft, Intake Camshaft, Water Inlet Housing, Distributor (IIA), Cylinder Head, Water Outlet Pipe, Fan Belt Adjusting Bar, Gasket (◆), Exhaust Manifold Stay, Exhaust Manifold, Manifold Heat Insulator (Upper), Manifold Heat Insulator (Lower).

Legend:
- **kg-cm (ft-lb, N·m)** : Specified torque
- ◆ : Non-reusable part
- ✱ : Must not remove the spark plug tube

> **Scan gap:** page EM-57 is missing from this scan.

---
<a id="p42"></a>
**[PDF p.42]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-58

## REMOVAL OF CYLINDER HEAD
(See pages EM-56, 57)

### 1. REMOVE IIA

### 2. REMOVE EXHAUST MANIFOLD (2WD)

(a) Remove the five bolts and upper heat insulator.

(b) Remove the two bolts and manifold stay.

(c) Remove the two bolts, three nuts, exhaust manifold and gasket.

(d) Remove the three bolts and lower heat insulator from the exhaust manifold.

---
<a id="p43"></a>
**[PDF p.43]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-59

*(Continuation — exhaust manifold removal, 4WD variant)*

(b) Remove the two bolts and manifold stay.

(c) Remove the three bolts, two nuts, manifold and gasket.

(d) Remove the three bolts and lower heat insulator from the exhaust manifold.

### 3. REMOVE WATER OUTLET

Remove the two bolts and water outlet.

### 4. REMOVE WATER INLET AND INLET HOUSING

(a) Disconnect the following connectors:
- Water temperature sender gauge connector
- Water temperature sensor connector
- Start injector time switch connector

(b) Disconnect the following hoses:
1. Inlet water hose
2. Water by-pass hose
3. BVSV vacuum hose(s)

(c) Remove the bolt, two nuts, the water inlet and inlet housing assembly.

### 5. REMOVE COLD START INJECTOR PIPE
(See step 3 on page FI-105)

---
<a id="p44"></a>
**[PDF p.44]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-60

### 6. (4WD)

### 7. REMOVE DELIVERY PIPE AND INJECTORS
(See steps 3 to 6 and 8 on pages FI-113 and 114)

### 8. DISCONNECT ENGINE WIRE FROM NO.3 TIMING BELT COVER

(a) Disconnect the following connectors and wire:
- Alternator connector
- Alternator wire
- Oil pressure switch connector

(b) Remove the bolt.

(c) Disconnect the wire clamp from the wire bracket, and disconnect the engine wire from the timing belt cover.

### 9. DISCONNECT ENGINE WIRE FROM INTAKE MANIFOLD

(a) Disconnect the following connectors:
- Throttle position sensor connector
- ISC valve connector
- (2WD w/ EGR system) EGR VSV connector
- Cold start injector connector

(b) Disconnect the wire clamp from the vacuum pipe.

(c) Remove the three bolts, and disconnect the engine wire from the intake manifold.

### 10. (4WD)

### 11. REMOVE INTAKE MANIFOLD (2WD)

(a) Remove the two bolts and manifold stay.

---
<a id="p45"></a>
**[PDF p.45]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-61

*(Continuation of step 11 — REMOVE INTAKE MANIFOLD)*

**(2WD)**

(b) Disconnect the water by-pass hose from the air pipe.

(c) Remove the seven bolts, ground strap, intake manifold and gasket.

**(4WD)**

(a) *(image only — see [PDF p.45])*

(b) Disconnect the water by-pass hose from the air pipe.

(c) Remove the seven bolts, ground strap, intake manifold and gasket.

---
<a id="p46"></a>
**[PDF p.46]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-62

### 12. REMOVE CYLINDER HEAD COVER

Remove the three cap nuts, grommets, head cover and gasket.

### 13. REMOVE SEMI-CIRCULAR PLUG

### 14. REMOVE NO.3 AND NO.2 TIMING BELT COVERS

Remove the six bolts, engine wire bracket, No.3 and No.2 timing belt covers.

### 15. SET NO.1 CYLINDER TO TDC/COMPRESSION

(a) Turn the crankshaft pulley and align its groove with the timing mark "O" of the No.1 timing belt cover.

(b) Check that the hole of the camshaft timing pulley is aligned with the timing mark of the bearing cap.

If not, turn the crankshaft one revolution (360°).

### 16. REMOVE TIMING BELT FROM CAMSHAFT TIMING PULLEY

(a) Remove the plug from the No.1 timing belt cover.

(b) Place matchmarks on the camshaft timing pulley and belt.

(c) Loosen the idler pulley mount bolt and push the idler pulley toward the left as far as it will go, then tighten it temporarily.

---
<a id="p47"></a>
**[PDF p.47]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-63

*(Continuation of step 16)*

(d) Remove the timing belt from the camshaft timing pulley.

> **NOTICE:**
> - Support the belt so that the meshing of the crankshaft timing pulley and timing belt does not shift.
> - Be careful not to drop anything inside the timing belt cover.
> - Do not allow the belt to come in contact with oil, water or dust.

### 17. REMOVE CAMSHAFT TIMING PULLEY
(See step 10 on page EM-41)

### 18. REMOVE FAN BELT ADJUSTING BAR

Remove the two bolts and adjusting bar.

### 19. REMOVE ENGINE HANGERS

Remove the two bolts and engine hangers.

### 20. REMOVE CAMSHAFTS

> **NOTICE:** Since the thrust clearance of the camshaft is small, the camshaft must be kept level while it is being removed. If the camshaft is not kept level, the portion of the cylinder head receiving the shaft thrust may crack or be damaged, causing the camshaft to seize or break. To avoid this, the following steps should be carried out.

**A. Remove intake camshaft**

(a) Set the intake camshaft so the knock pin is slightly above the top of the cylinder head.

> **HINT:** The above angle allows the No.1 and No.3 cylinder cam lobes of the intake camshaft to push their valve lifters evenly.

---
<a id="p48"></a>
**[PDF p.48]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-64

*(Continuation of step 20 A — Remove intake camshaft)*

(b) Remove the two bolts and front bearing cap.

(c) Secure the intake camshaft sub-gear to the main gear with a service bolt.

**Recommended service bolt:**

| Spec | Value |
|---|---|
| Thread diameter | 6 mm |
| Thread pitch | 1.0 mm |
| Bolt length | 16 – 20 mm (0.63 – 0.79 in.) |

> **HINT:** When removing the camshaft, make certain that the torsional spring force of the sub-gear has been eliminated by the above operation.

(d) Uniformly loosen and remove the eight bearing cap bolts in several passes in the sequence shown.

(e) Remove the four bearing caps and camshaft.

> **HINT:** If the camshaft is not being lifted out straight and level, reinstall the bearing cap with the two bolts. Then alternately loosen and remove the bearing cap bolts with the camshaft gear pulled up.

> **NOTICE:** Do not pry on or attempt to force the camshaft with a tool or other objects.

**B. Remove exhaust camshaft**

(a) Set the exhaust camshaft so that the knock pin is located slightly counterclockwise from the vertical axis of the camshaft.

> **HINT:** The above angle allows the No.1 and No.3 cylinder cam lobes of exhaust camshaft to push their valve lifters evenly.

---
<a id="p49"></a>
**[PDF p.49]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-65

*(Continuation of step 20 B — Remove exhaust camshaft)*

(b) Remove the two bolts, front bearing cap and oil seal.

> **NOTICE:** If the front bearing cap is not removable by hand, do not try to remove by force but leave as it is without bolts.

(c) Uniformly loosen and remove the eight bearing cap bolts in several passes in the sequence shown.

(d) Remove the four bearing caps and camshaft.

> **HINT:** If the camshaft is not being lifted out straight and level, reinstall the No.3 bearing cap with the two bolts. Then alternately loosen and remove the two bearing cap bolts with the camshaft gear pulled up.

> **NOTICE:** Do not pry on or attempt to force the camshaft with a tool or other objects.

### 21. DISASSEMBLE INTAKE CAMSHAFT

(a) Mount the hexagonal wrench head portion of the camshaft in a vise.

> **NOTICE:** Be careful not to damage the camshaft.

(b) Insert service bolts (A) and (B) into the service holes of the camshaft sub-gear.

(c) Using a screwdriver, turn the sub-gear clockwise, and remove the service bolt (C).

> **NOTICE:** Be careful not to damage the camshaft.

---
<a id="p50"></a>
**[PDF p.50]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-66

*(Continuation of step 21 — DISASSEMBLE INTAKE CAMSHAFT)*

(d) Using snap ring pliers, remove the snap ring.

(e) Remove the following parts:
1. Wave washer
2. Camshaft sub-gear
3. Camshaft gear spring

### 22. REMOVE CYLINDER HEAD

(a) Using SST, uniformly loosen and remove the ten cylinder head bolts in several passes in the sequence shown.

**SST 09205-16010**

> **NOTICE:** Head warpage or cracking could result from removing the bolts in an incorrect order.

*(Loosening sequence per illustration, front→rear: 3, 5, 10, 8, 2 / 1, 7, 9, 6, 4)*

(b) Lift the cylinder head from the dowels of the cylinder block and place the head on wooden blocks on a bench.

> **HINT:** If the cylinder head is difficult to lift off, pry with a screwdriver between the cylinder head and block saliences.

> **NOTICE:** Be careful not to damage the cylinder head and the cylinder block surfaces of the cylinder head gasket side.
---
<a id="p51"></a>
**[PDF p.51]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-67

## DISASSEMBLY OF CYLINDER HEAD (4A-FE)
(See pages EM-56, 57)

1. **REMOVE VALVE LIFTERS AND SHIMS**

   > **HINT:** Arrange the valve lifters and shims in correct order.

   *(image only — IN and EX valve lifters/shims laid out in order, see [PDF p.51])*

2. **REMOVE VALVES**
   a. Using SST, compress the valve spring and remove the two keepers.

      **SST 09202-70010**
   b. Remove the spring retainer, valve spring, valve and spring seat.

      > **HINT:** Arrange the valves, valve springs, spring seats and spring retainers in correct order.
   c. Using needle-nose pliers, remove the oil seal.

---
<a id="p52"></a>
**[PDF p.52]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-68

## INSPECTION, CLEANING AND REPAIR OF CYLINDER HEAD COMPONENTS

1. **CLEAN TOP SURFACES OF PISTONS AND BLOCK**
   a. Turn the crankshaft and bring each piston to the top dead center (TDC). Using a gasket scraper, remove all the carbon from the piston top surface.
   b. Using a gasket scraper, remove all the gasket material from the top surfaces of the cylinder block.
   c. Using compressed air, blow carbon and oil from the bolt holes.

   > **CAUTION:** Protect your eyes when using high pressure compressed air.

2. **CLEAN CYLINDER HEAD**

   A. **Remove gasket material**

   Using a gasket scraper, remove all the gasket material from the cylinder head surface.

   > **NOTICE:** Be careful not to scratch the cylinder block contact surface.

   B. **Clean combustion chambers**

   Using a wire brush, remove all the carbon from the combustion chambers.

   > **NOTICE:** Be careful not to scratch the cylinder block contact surface.

   C. **Clean valve guide bushings**

   Using a valve guide bushing brush and solvent, clean all the guide bushings.

---
<a id="p53"></a>
**[PDF p.53]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-69

   D. **Clean cylinder head**

   Using a soft brush and solvent, thoroughly clean cylinder head.

3. **INSPECT CYLINDER HEAD**

   A. **Inspect for flatness**

   Using a precision straight edge and feeler gauge, measure the surfaces contacting the cylinder block and manifolds for warpage.

   **Maximum warpage:**

   | Surface | Max warpage |
   |---|---|
   | Cylinder block side | **0.05 mm (0.0021 in.)** |
   | Manifold side | **0.10 mm (0.0039 in.)** |

   If warpage is greater than maximum, replace the cylinder head.

   B. **Inspect for cracks**

   Using a dye penetrant, check the combustion chamber, intake and exhaust ports, head surface and the top of the head for cracks.

   If cracked, replace the cylinder head.

4. **CLEAN VALVES**
   a. Using a gasket scraper, chip off any carbon from the valve head.
   b. Using a wire brush, thoroughly clean the valve.

---
<a id="p54"></a>
**[PDF p.54]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-70

5. **INSPECT VALVE STEMS AND GUIDE BUSHINGS**
   a. Using a caliper gauge, measure the inside diameter of the guide bushing.

      **Bushing inside diameter: 6.01 − 6.03 mm (0.2366 − 0.2374 in.)**
   b. Using a micrometer, measure the diameter of the valve stem.

      **Valve stem diameter:**

      | | Diameter |
      |---|---|
      | Intake | **5.970 − 0.2356 mm (0.2350 − 0.2356 in.)** |
      | Exhaust | **5.965 − 5.980 mm (0.2348 − 0.2354 in.)** |

      <!-- NEEDS REVIEW: The Intake row is printed exactly as shown in the manual ("5.970 − 0.2356 mm"); the upper mm bound is a manual typo — the inch range 0.2350–0.2356 in. corresponds to 5.970–5.976 mm. Verified against page image. -->
   c. Subtract the valve stem diameter measurement from the guide bushing inside diameter measurement.

      **Standard oil clearance:**

      | | Clearance |
      |---|---|
      | Intake | **0.025 − 0.060 mm (0.0010 − 0.0024 in.)** |
      | Exhaust | **0.030 − 0.065 mm (0.0012 − 0.0026 in.)** |

      **Maximum oil clearance:**

      | | Clearance |
      |---|---|
      | Intake | **0.08 mm (0.0031 in.)** |
      | Exhaust | **0.10 mm (0.0039 in.)** |

      If the clearance is greater than maximum, replace the valve and guide bushing.

6. **IF NECESSARY, REPLACE VALVE GUIDE BUSHINGS**
   a. Gradually heat the cylinder head to **80 − 100°C (176 − 212°F)**.
   b. Using SST and a hammer, tap out the guide bushing.

      **SST 09201-70010**

---
<a id="p55"></a>
**[PDF p.55]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-71

   c. Using a caliper gauge, measure the bushing bore diameter of the cylinder head.

      **Standard valve guide bore (cold): 11.000 − 11.027 mm (0.4331 − 0.4341 in.)**
   d. Select a new guide bushing (STD size or O/S 0.05)

      **Both intake and exhaust**

      | Bushing bore diameter mm (in.) | Bushing size |
      |---|---|
      | 11.000 − 11.027 (0.4331 − 0.4341) | Used STD |
      | 11.050 − 11.077 (0.4350 − 0.4361) | Used O/S 0.05 |

      If the bushing bore diameter of the cylinder head is greater than **11.027 mm (0.4341 in.)**, machine the bushing bore to the following dimensions:

      **Rebored cylinder head bushing bore dimension: 11.050 − 11.077 mm (0.4350 − 0.4361 in.)**

      If the bushing bore diameter of the cylinder head is greater than **11.077 mm (0.4361 in.)**, replace the cylinder head.
   e. Gradually heat the cylinder head to **80 − 100°C (176 − 212°F)**.
   f. Using SST and a hammer, tap in a new guide bushing to where **12.7 − 13.1 mm (0.500 − 0.516 in.)** protruding from the cylinder head.

      **SST 09201-70010**
   g. Using a sharp 6 mm reamer, ream the guide bushing to obtain the standard specified clearance (See page EM-70) between the guide bushing and valve stem.

---
<a id="p56"></a>
**[PDF p.56]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-72

7. **INSPECT AND GRIND VALVES**
   a. Grind the valve enough to remove pits and carbon.
   b. Check that the valve is ground to the correct valve face angle.

      **Valve face angle: 44.5°**
   c. Check the valve head margin thickness.

      **Standard margin thickness:**

      | | Thickness |
      |---|---|
      | Intake | **1.05 − 1.45 mm (0.0413 − 0.0571 in.)** |
      | Exhaust | **1.19 − 1.59 mm (0.0469 − 0.0626 in.)** |

      **Minimum margin thickness: 0.5 mm (0.020 in.)**

      If the margin thickness is less than minimum, replace the valve.
   d. Check the valve overall length.

      **Standard overall length:**

      | | Length |
      |---|---|
      | Intake | **91.45 mm (3.6004 in.)** |
      | Exhaust | **91.90 mm (3.6181 in.)** |

      **Minimum overall length:**

      | | Length |
      |---|---|
      | Intake | **90.95 mm (3.5807 in.)** |
      | Exhaust | **91.40 mm (3.5984 in.)** |

      If the overall length is less than minimum, replace the valve.
   e. Check the surface of the valve stem tip for wear.

      If the valve stem tip is worn, resurface the tip with a grinder or replace the valve.

      > **NOTICE:** Do not grind off more than minimum.

8. **INSPECT AND CLEAN VALVE SEATS**
   a. Using a 45° carbide cutter, resurface the valve seats. Remove only enough metal to clean the seats.

---
<a id="p57"></a>
**[PDF p.57]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-73

   b. Check the valve seating position.

      Apply a thin coat of prussian blue (or white lead) to the valve face. Lightly press the valve against the seat. Do not rotate the valve.
   c. Check the valve face and seat for the following:
      - If blue appears 360° around the face, the valve is concentric. If not, replace the valve.
      - If blue appears 360° around the valve seat, the guide and face are concentric. If not, resurface the seat.
      - Check that the seat contact is in the middle of the valve face with the following width:

        **1.2 − 1.6 mm (0.047 − 0.063 in.)**

      If not, correct the valve seats as follows:
      1. If the seating is too high on the valve face, use 30° and 45° cutters to correct the seat. (seat width **1.2 − 1.6 mm**)
      2. If the seating is too low on the valve face, use 60° and 45° cutters to correct the seat. (seat width **1.2 − 1.6 mm**)
   d. Hand-lap the valve and valve seat with an abrasive compound.
   e. After hand-lapping, clean the valve and valve seat.

9. **INSPECT VALVE SPRINGS**
   a. Using a steel square, measure the squareness of the valve spring.

      **Maximum squareness: 2.0 mm (0.075 in.)**

      If squareness is greater than maximum, replace the valve spring.

---
<a id="p58"></a>
**[PDF p.58]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-74

   b. Using vernier calipers, measure the free length of the valve spring.

      **Free length: 43.8 mm (1.724 in.)**

      If the free length is not as specified, replace the valve spring.
   c. Using a spring tester, measure the tension of the valve spring at the specified installed length.

      **Installed tension: 14.6 − 15.8 kg (32.3 − 34.8 lb, 143 − 155 N) at 34.7 mm (1.366 in.)**

      If the tension is not as specified, replace the valve spring.

10. **INSPECT CAMSHAFTS AND BEARINGS**

    A. **Inspect camshaft for runout**
       a. Place the camshaft on V-blocks.
       b. Using a dial indicator, measure the circle runout at the center journal.

          **Maximum circle runout: 0.04 mm (0.0016 in.)**

          If the circle runout is greater than maximum, replace the camshaft.

    B. **Inspect cam lobes**

    Using a micrometer, measure the cam lobe height.

    **Standard cam lobe height:**

    | | Height |
    |---|---|
    | Intake | **35.21 − 35.31 mm (1.3862 − 1.3092 in.)** |
    | Exhaust | **34.91 − 35.01 mm (1.3744 − 1.3783 in.)** |

    <!-- NEEDS REVIEW: Intake inch range printed as "1.3862 − 1.3092 in."; the upper bound is a manual typo (35.31 mm = 1.3902 in., not 1.3092). Verified against page image — value is printed this way in the manual. -->

    **Minimum cam lobe height:**

    | | Height |
    |---|---|
    | Intake | **34.81 mm (1.3705 in.)** |
    | Exhaust | **34.51 mm (1.3587 in.)** |

    If the cam lobe height is greater than minimum, replace the camshaft.

    C. **Inspect camshaft journals**

    Using a micrometer, measure the journal diameter.

    **Journal diameter:**

    | | Diameter |
    |---|---|
    | Exhaust No.1 | **24.949 − 24.965 mm (0.9822 − 0.9829 in.)** |
    | Others | **22.949 − 22.965 mm (0.9035 − 0.9041 in.)** |

    If the journal diameter is not as specified, check the oil clearance.

---
<a id="p59"></a>
**[PDF p.59]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-75

    D. **Inspect camshaft bearings**

    Check the bearings for flaking and scoring.

    If the bearings are damaged, replace the bearing caps and cylinder head as a set.

    E. **Inspect camshaft gear spring**

    Using vernier calipers, measure the free distance between the spring end.

    **Free distance: 17.1 − 17.5 mm (0.673 − 0.689 in.)**

    If the free distance is not as specified, replace the gear spring.

    F. **Inspect camshaft journal oil clearance**
       a. Clean the bearing caps and camshaft journals.
       b. Place the camshafts on the cylinder head.
       c. Lay a strip of Plastigage across each of the camshaft journals.
       d. Install the bearing caps. (See step 3 on pages EM-81 to 83)

          **Torque: 130 kg-cm (9 ft-lb, 13 N·m)**

          > **NOTICE:** Do not turn the camshaft.
       e. Remove the bearing caps.

---
<a id="p60"></a>
**[PDF p.60]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-76

    F. *(continued)*
       f. Measure the Plastigage at its widest point.

          **Standard oil clearance: 0.035 − 0.072 mm (0.0014 − 0.0028 in.)**
          **Maximum oil clearance: 0.10 mm (0.0039 in.)**

          If the oil clearance is greater than maximum, replace the camshaft. If necessary, replace the bearing caps and cylinder head as a set.
       g. Completely remove the Plastigage.

    G. **Inspect camshaft thrust clearance**
       a. Install the camshaft. (See step 3 on pages EM-81 to 83)
       b. Using a dial indicator, measure the thrust clearance while moving the camshaft back and forth.

          **Standard thrust clearance:**

          | | Clearance |
          |---|---|
          | Intake | **0.030 − 0.085 mm (0.0012 − 0.0033 in.)** |
          | Exhaust | **0.035 − 0.090 mm (0.0014 − 0.0035 in.)** |

          **Maximum thrust clearance: 0.11 mm (0.0043 in.)**

          If the thrust clearance is greater than maximum, replace the camshaft. If necessary, replace the bearing caps and cylinder head as a set.

    H. **Inspect camshaft gear backlash**
       a. Install the camshafts without installing the exhaust camshaft sub-gear. (See step 3 on page EM-81 to 83)
       b. Using a dial indicator, measure the backlash.

          **Standard back lash: 0.020 − 0.020 mm (0.0008 − 0.0079 in.)**
          **Maximum back lash: 0.30 mm (0.0188 in.)**

          <!-- NEEDS REVIEW: Standard backlash printed as "0.020 − 0.020 mm"; the upper mm bound is a manual typo (the inch range 0.0008 − 0.0079 in. corresponds to 0.020 − 0.200 mm). Verified against page image — printed this way in the manual. -->

          If the backlash is greater than maximum, replace the camshafts.

11. **INSPECT VALVE LIFTERS AND LIFTER BORES**
    a. Using a caliper gauge, measure the lifter bore diameter of the cylinder head.

       **Lifter bore diameter: 28.005 − 28.006 mm (1.1026 − 1.1034 in.)**

---
<a id="p61"></a>
**[PDF p.61]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-77

    b. Using a micrometer, measure the lifter diameter.

       **Lifter diameter: 27.975 − 27.985 mm (1.1014 − 1.1018 in.)**
    c. Subtract the lifter diameter measurement from the lifter bore diameter measurement.

       **Standard oil clearance: 0.020 − 0.051 mm (0.0008 − 0.0020 in.)**
       **Maximum oil clearance: 0.07 mm (0.0028 in.)**

       If the oil clearance is greater than maximum, replace the lifter. If necessary, replace the cylinder head.

12. **INSPECT INTAKE AND EXHAUST MANIFOLDS**

    Using precision straight edge and feeler gauge, measure the surface contacting the cylinder head for warpage.

    **Maximum warpage:**

    | | Warpage |
    |---|---|
    | Intake | **0.20 mm (0.0079 in.)** |
    | Exhaust | **0.30 mm (0.0118 in.)** |

    If warpage is greater than maximum, replace the manifold.

13. **IF NECESSARY, REPLACE SPARK PLUG TUBE GASKET**
    a. Using a screwdriver, pry out the gasket.
    b. Using SST, tap in a new gasket until its surface is flush with the upper edge of the cylinder head cover.

       **SST 09950-10012 (09552-10010, 09560-10010)**
    c. Apply a light coat of MP grease to the gasket lip.

---
<a id="p62"></a>
**[PDF p.62]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-78

## ASSEMBLY OF CYLINDER HEAD
(See pages EM-56, 57)

> **HINT:**
> - Thoroughly clean all parts to be assembled.
> - Before installing the parts, apply new engine oil to all sliding and rotating surfaces.
> - Replace all gaskets and oil seals with new ones.

1. **INSTALL SPARK PLUG TUBES**

   > **HINT:** When using a new cylinder head, spark plug tubes must be installed.

   a. Apply adhesive to the spark plug tube hole of the cylinder head.

      **Adhesive: Part No. 08833-00070, THREE BOND 1324 or equivalent**
   b. Using a press, press in a new spark plug tube until **46.8 − 47.6 mm (1.843 − 1.874 in.)** is protruding from the cylinder head.

      > **NOTICE:** Avoid tapping a new spark plug tube in too far by measuring the amount of protrusion while pressing.

2. **INSTALL VALVES**
   a. Using SST, push in a new oil seal.

      **SST 09201-41020**

      > **HINT:** The intake valve oil seal is brown and the exhaust valve oil seal is black.

      | | Oil seal color |
      |---|---|
      | Intake | Painted Brown |
      | Exhaust | Painted Black |

---
<a id="p63"></a>
**[PDF p.63]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-79

   b. Install the following parts:
      1. Valve
      2. Spring seat
      3. Valve spring
      4. Spring retainer
   c. Using SST, compress the valve spring and place the two keepers around the valve stem.

      **SST 09202-70010**
   d. Using a plastic-faced hammer, lightly tap the valve stem tip to assure proper fit.

3. **INSTALL VALVE LIFTERS AND SHIMS**
   a. Install the valve lifter and shim.
   b. Check that the valve lifter rotates smoothly by hand.
---
<a id="p64"></a>
**[PDF p.64]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-80

## INSTALLATION OF CYLINDER HEAD (4A-FE)
(See page EM-56, 57)

### 1. INSTALL CYLINDER HEAD

a. Place a new cylinder head gasket in position on the cylinder block.

> **NOTICE:** Be careful of the installation direction.

b. Place the cylinder head in position on the cylinder head gasket.
c. Apply a light coat of engine oil on the threads and under the heads of the cylinder head bolts.
d. Using SST, install and uniformly tighten the ten cylinder head bolts in several passes in the sequence shown.

SST **09205-16010**

**Torque: 610 kg-cm (44 ft-lb, 60 N·m)**

> **HINT:** Cylinder head bolts are **90 mm (3.54 in.)** and **108 mm (4.25 in.)** in length. Install the **90 mm (3.54 in.)** bolt (A) in RH side positions. Install the **108 mm (4.25 in.)** bolts (B) in LH side position.

*(Tightening sequence diagram — bolts, top row L→R: (B)8, (B)6, (B)1, (B)3, (B)9; bottom row L→R: (A)10, (A)4, (A)2, (A)5, (A)7. See [PDF p.64].)*

### 2. ASSEMBLE INTAKE CAMSHAFT

a. Mount the hexagonal wrench head portion of the camshaft in a vise.

> **NOTICE:** Be careful not to damage the camshaft.

b. Install the following parts:
   1. Camshaft gear spring.
   2. Camshaft sub-gear
   3. Wave washer

> **HINT:** Align the pins on the gears with the gear spring ends.

---
<a id="p65"></a>
**[PDF p.65]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-81

c. Using snap ring pliers, install the snap ring.
d. Insert a service bolts (A) and (B) into the service hole of the camshaft sub-gear.
e. Using a screwdriver, align the holes of the camshaft main gear and sub-gear by turning the camshaft sub-gear clockwise, and install a service bolt (C).

> **NOTICE:** Be careful not to damage the camshaft.

### 3. INSTALL INTAKE AND EXHAUST CAMSHAFT

> **NOTICE:** Since the thrust clearance of the camshaft is small, the camshaft must be kept level while it is being installed. If the camshaft is not kept level, the portion of the cylinder head receiving the shaft thrust may crack or be damaged, causing the camshaft to seize or break.
> To avoid this, the following steps should be carried out.

#### A. Install exhaust camshaft

a. Apply MP grease to the thrust portion of the camshaft.
b. Place the intake camshaft at so the knock pin is located slightly counterclockwise from the vertical axis of the camshaft.

> **HINT:** The above angle allows the No.1 and No.3 cylinder cam lobes of the exhaust camshaft to push their valve lifters evenly.

c. Remove the old packing (FIPG) material.
d. Apply seal packing to the cylinder head as shown in the figure.

**Seal packing: Part No. 08826-00080 or equivalent**

---
<a id="p66"></a>
**[PDF p.66]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-82

e. Install the five bearing caps in their proper locations.

*(Bearing cap layout diagram — caps marked No.1 through No.5. See [PDF p.66].)*

f. Apply a light coat of engine oil on the threads and under the heads of the bearing cap bolts.
g. Install and uniformly tighten the ten bearing cap bolts in several passes in the sequence shown.

**Torque: 130 kg-cm (9 ft-lb, 13 N·m)**

h. Apply MP grease to a new oil seal lip.
i. Using SST, tap in the oil seal.

SST **09223-46011**

> **HINT:**
> - Do not install the oil seal with the lip facing the wrong direction.
> - Insert the oil seal into the deepest part of the cylinder head.

#### B. Install intake camshaft

a. Set the knock pin of the exhaust camshaft so that the knock pin is slightly above the top of the cylinder head.

---
<a id="p67"></a>
**[PDF p.67]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-83

b. Apply MP grease to the thrust portion of the camshaft.
c. Engage the intake camshaft gear to the exhaust camshaft gear by matching the assembly installation marks on each gear.

> **NOTICE:** There are also timing marks (for TDC) on each gear as shown in the illustration. Do not use these marks.

d. Roll down the intake camshaft onto the bearing journals while engaging gears with each other.

> **HINT:** The above angle allows the No.1 and No.3 cylinder cam lobes of the intake camshaft to push their valve lifters evenly.

e. Instale the four bearing caps in their proper locations.

*(Bearing cap layout diagram — caps marked No.2 through No.5. See [PDF p.67].)*

f. Apply a light coat of engine oil on the threads and under the heads of bearing cap bolts.
g. Install and uniformly tighten the eight bearing cap bolts in several passes in the sequence shown.

**Torque: 130 kg-cm (9 ft-lb, 13 N·m)**

*(Bolt tightening sequence diagram — numbered 1 through 8. See [PDF p.67].)*

h. Remove the service bolt (B).
i. Install the No. 1 bearing cap with the arrow mark facing forward.

> **NOTICE:** If the bearing cap does not fit properly, push the camshaft gear backwards by prying apart the cylinder head and camshaft gear with a screwdriver.

j. Apply a light coat of engine oil on the threads and under the heads of bearing cap bolts.
k. Install and alternately tighten the two bolts in several passes.

**Torque: 130 kg-cm (9 ft-lb, 13 N·m)**

---
<a id="p68"></a>
**[PDF p.68]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-84

l. Turn the exhaust camshaft clockwise, and set it with the knock pin facing upward.
m. Check that the timing marks of the camshaft gears are aligned.

> **HINT:** The assembly installation marks are on the upside.

### 4. CHECK AND ADJUST VALVE CLEARANCE
(See page EM-16)

Turn the camshaft and position the cam lobe upward, and check and adjust the valve clearance.

**Valve clearance (Cold):**

| | Clearance |
|---|---|
| Intake | **0.15 – 0.25 mm (0.006 – 0.010 in.)** |
| Exhaust | **0.20 – 0.30 mm (0.008 – 0.012 in.)** |

### 5. INSTALL ENGINE HANGERS

Install the two engine hangers with the two bolts.

**Torque: 280 kg-cm (20 ft-lb, 27 N·m)**

### 6. INSTALL FAN BELT ADJUSTING BAR

Install the adjusting bar with the two bolts.

**Torque: 200 kg-cm (14 ft-lb, 20 N·m)**

### 7. INSTALL CAMSHAFT TIMING PULLEY
(See step 1 on page EM-44)

### 8. INSTALL TIMING BELT

Align the matchmarks of the timing belt and camshaft timing pulley.

a. Remove any oil or water on the camshaft timing pulley, and keep it clean.
b. Install the timing belt, insuring the tension between the crankshaft timing pulley and camshaft timing pulley.

---
<a id="p69"></a>
**[PDF p.69]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-85

### 9. INSTALL VALVE TIMING

a. Loosen the idler pulley bolt 1/2 turn.
b. Turn the crankshaft pulley two revolutions from TDC to TDC.

> **NOTICE:** Always turn the crankshaft clockwise.

c. Check that each pulley aligns with the timing marks as shown in the illustration.

If the timing marks does not align, remove the timing belt and reinstall it.

d. Tighten the idler pulley bolt.

**Torque: 375 kg-cm (27 ft-lb, 37 N·m)**

### 10. (REFERENCE) INSTALL TIMING BELT TENSION

Check that there is belt tension at the portion indicated in the illustration.

**Deflection: 5 – 6 mm (0.20 – 0.24 in.) at 2 kg (4.4 lb, 20 N)**

---
<a id="p70"></a>
**[PDF p.70]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-86

If the deflection is not as specified, adjust with the idler pulley.

### 11. INSTALL NO.2 AND NO.3 TIMING BELT COVERS

Install the No.2, No.3 timing belt covers and engine wire bracket with the six bolts.

### 12. INSTALL SPARK PLUGS (See page IG-8)

**Torque: 180 kg-cm (13 ft-lb, 18 N·m)**

<!-- NEEDS REVIEW: A stray "Torque: 80 kg-cm (69 in.-lb, 7.8 N·m)" is printed in the left column between the illustration (EM7220) and step 13; it appears to be a misplaced value belonging to the cylinder head cover step (14), which repeats it on p.71 EM-87. -->

### 13. INSTALL SEMI-CIRCULAR PLUG

a. Remove any old packing (FIPG) material.
b. Apply seal packing to the circular plug.

**Seal packing: Part No. 08826-00080 or equivalent**

c. Install the semi-circular plug to the cylinder head.

### 14. INSTALL CYLINDER HEAD COVER

a. Remove any old packing (FIPG) material.
b. Apply seal packing to the cylinder head as shown in the figure.

**Seal packing: Parts No. 08826-00080 or equivalent**

---
<a id="p71"></a>
**[PDF p.71]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-87

c. Install the gasket to the head cover.
d. Install the head cover with the three grommets and cap nuts.

**Torque: 80 kg-cm (69 in.-lb, 7.8 N·m)**

### 15. INSTALL INTAKE MANIFOLD

#### (2WD)

a. Install a new gasket and the intake manifold with the seven bolts, ground strap and two nuts.

**Torque: 195 kg-cm (14 ft-lb, 19 N·m)**

b. Connect the water by-pass hose to the air pipe.
c. Install the manifold stay with the two bolts.

**Torque:**

| Bolt | Torque |
|---|---|
| 12 mm bolt head | **195 kg-cm (14 ft-lb, 19 N·m)** |
| 14 mm bolt head | **400 kg-cm (29 ft-lb, 39 N·m)** |

#### (4WD)

---
<a id="p72"></a>
**[PDF p.72]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-88

*(4WD intake manifold, continued)*

b. Connect the water by-pass hose to the air pipe.
c. Install the manifold stay with the bolt and nut.

**Torque: 195 kg-cm (14 ft-lb, 19 N·m)**

### 16. (4WD)

### 17. INSTALL ENGINE WIRE TO INTAKE MANIFOLD

a. Install the engine wire with the three bolts.
b. Install the engine wire the engine to vacuum pipe with the wire clamp.
c. Connect the following connectors:
   - Throttle position sensor connector
   - ISC valve connector
   - (2WD w/ EGR system) EGR VSV connector
   - Cold start injector connector

### 18. INSTALL ENGINE WIRE TO NO.3 TIMING BELT COVER

a. Install the wire clamp on engine wire to the wire bracket.
b. Install the engine wire with the bolt.
c. Connect the following connectors and wire:
   - Alternator connector
   - Alternator wire
   - Oil pressure switch connector

### 19. INSTALL INJECTORS AND DELIVERY PIPE
(See steps 1 and 3 to 6 on pages FI-116 to 119)

---
<a id="p73"></a>
**[PDF p.73]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-89

### 20. (4WD)

### 21. INSTALL COLD START INJECTOR PIPE
(See step 2 on page FI-108)

### 22. INSTALL WATER INLET AND INLET HOUSING

a. Remove any old packing (FIPG) material and be careful not to drop any oil on the contact surfaces of the inlet housing and cylinder head.
   - Using a razor blade and gasket scraper, remove all the oil packing (FIPG) material from the gasket surfaces and sealing groove.
   - Thoroughly clean all components to remove all the loose material.
   - Using a non-residue, clean both sealing surfaces.
b. Apply seal packing to the inlet housing groove.

**Seal packing: Part No. 08826-00100 or equivalent**

   - Install a nozzle that has been cut with a **2 – 3 mm (0.08 – 0.12 in.)** opening.

*(Seal Diameter callout: **2 – 3 mm (0.08 – 0.12 in.)**)*

> **HINT:** Avoid applying an excessive amount to the surface.
> - Parts must be assembled within 15 minutes of application. Otherwise the material must be removed and reapplied.
> - Immediately remove nozzle from the tube and reinstall cap.

c. Install the water inlet housing with the bolt and two nuts.

**Torque: 200 kg-cm (14 ft-lb, 30 N·m)**  <!-- NEEDS REVIEW: unit conversion inconsistent (200 kg-cm ≈ 20 N·m / 14 ft-lb), but image clearly prints "30 N·m"; kept as printed. -->

d. Connect the following hoses:
   1. BVSV vacuum hose(s)
   2. Water by-pass hose
   3. Inlet water hose
e. Connect the following connectors:
   - Water temperature sender gauge connector
   - Water temperature sensor connector
   - Start injector time switch connector

---
<a id="p74"></a>
**[PDF p.74]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-90

### 23. INSTALL WATER OUTLET

a. Remove any old packing (FIPG) material and be careful not to drop any oil on the contact surfaces of the water outlet cylinder head.
   - Using a razor blade and gasket scraper, remove all the oil packing (FIPG) material from the gasket surfaces and sealing groove.
   - Thoroughly clean all components to remove all the loose material.
   - Using a non-residue, clean both sealing surfaces.
b. Apply seal packing to the water outlet groove.

**Seal packing: Part No. 08826-00100 or equivalent**

   - Install a nozzle that has been cut with a **2 – 3 mm (0.08 – 0.12 in.)** opening.

*(Seal Diameter callout: **2 – 3 mm (0.08 – 0.12 in.)**)*

> **HINT:** Avoid applying an excessive amount to the surface.
> - Parts must be assembled within 15 minutes of application. Otherwise the material must be removed and reapplied.
> - Immediately remove nozzle from the tube and reinstall cap.

c. Install the water outlet with the two bolts.

**Torque: 150 kg-cm (11 ft-lb, 15 N·m)**

### 24. INSTALL EXHAUST MANIFOLD

#### (2WD)

a. Install the lower heat insulator to the exhaust manifold with the three bolts.
b. Install a new gasket and the exhaust manifold with the two bolts and three nuts.

**Torque: 250 kg-cm (18 ft-lb, 25 N·m)**

---
<a id="p75"></a>
**[PDF p.75]** — ENGINE MECHANICAL — Cylinder Head (4A-FE) — EM-91

c. Install the manifold stay with the two bolts.

**Torque: 400 kg-cm (29 ft-lb, 39 N·m)**

d. Install the upper heat insulator with the five bolts.
