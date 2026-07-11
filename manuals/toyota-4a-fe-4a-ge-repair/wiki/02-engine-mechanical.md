# Engine Mechanical (4A-FE / 4A-GE)

*Section code: `EM` | PDF pages 10-75 of `Toyota-4A-FE-4A-GE-engine-repair-manual-OCR.pdf` | 66 pages*

> **Transcription in progress.** This is the largest, most engine-interleaved section.
> **Done so far:** Description (4A-FE), Troubleshooting (partial), Engine Tune-up (4A-FE).
> **Still pending:** Timing Belt, Cylinder Head, Cylinder Block. Specs below are recorded
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

## Not yet transcribed (this scan, pending)

- **Timing Belt** (≈ EM-33 onward) — [PDF pages ~23–32]
- **Cylinder Head** (≈ EM-41 onward) — [PDF pages ~33–56]
- **Cylinder Block** — [PDF pages ~57–75]

Read the source PDF pages directly for these until transcribed. Tracked in
[issue #7](https://github.com/spacecowboyian/oio-shop-shelf/issues/7).
