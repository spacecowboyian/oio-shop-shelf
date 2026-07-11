# Ignition System (4A-FE)

*Section code: `IG` | PDF pages 197-207 of `Toyota-4A-FE-4A-GE-engine-repair-manual-OCR.pdf` | 11 pages*

> **Engine applicability:** the ignition content present in this scan is the **4A-FE**
> Integrated Ignition Assembly (IIA). Every on-vehicle inspection and IIA page here is
> titled "(4A-FE)". The 4A-GE ignition (separate distributor/coil) is **not present** in
> this scan. Specs below were resolved against the page images where the OCR was
> ambiguous (Ω vs kΩ). See [llm-instructions.md](llm-instructions.md).
>
> **Scan gaps:** IG-3 (troubleshooting) and IG-5 are missing (pages jump IG-2 → IG-4 →
> IG-6); IG-10 through IG-14 (distributor removal/inspection/installation) are missing
> (pages jump IG-9 → IG-15). See [10-needs-review.md](10-needs-review.md).

## In this chapter

- [PRECAUTIONS](#p198) — [PDF p.198]
- [IGNITION SYSTEM CIRCUIT / ESA](#p199) — [PDF p.199]
- [ON-VEHICLE INSPECTION (4A-FE)](#p200) — [PDF p.200]
- [INSPECTION OF HIGH-TENSION CORDS / SPARK PLUGS](#p201) — [PDF p.201]
- [INSPECTION OF IGNITION COIL / DISTRIBUTOR](#p202) — [PDF p.202]
- [INTEGRATED IGNITION ASSEMBLY (IIA) (4A-FE)](#p204) — [PDF p.204]

---
<a id="p197"></a>
**[PDF p.197]** — IGNITION SYSTEM (section contents)

Contents as printed: PRECAUTIONS (IG-2), TROUBLESHOOTING (IG-3), IGNITION SYSTEM CIRCUIT
(IG-4), ON-VEHICLE INSPECTION — 4A-FE (IG-6), INTEGRATED IGNITION ASSEMBLY (IIA) — 4A-FE
(IG-15).

---
<a id="p198"></a>
**[PDF p.198]** — PRECAUTIONS

1. Do not leave the ignition switch on for more than **10 minutes** if the engine does not start.
2. With a tachometer connected, connect its test probe to terminal **IG⊖** of the check connector.
3. Some tachometers are not compatible with this ignition system — confirm compatibility before use.
4. **NEVER** allow the tachometer terminal to touch ground — it could damage the igniter and/or ignition coil.
5. Do not disconnect the battery while the engine is running.
6. Check that the igniter is properly grounded to the body.

---
<a id="p199"></a>
**[PDF p.199]** — IGNITION SYSTEM CIRCUIT · ELECTRONIC SPARK ADVANCE (ESA)

The ECU is programmed with optimum ignition-timing data for all operating conditions.
Using sensor data (rpm, intake air volume, engine temperature, etc.) the microcomputer
(ECU) triggers the spark at precisely the right instant. Firing order **1-3-4-2**. Circuit
(4A-FE, image on [PDF p.199]): Ignition Switch, FL AM2 30A, FL MAIN 2.0L, Battery, Spark
Plugs, Cap & Rotor, Signal Rotor, Pickup Coil, Ignition Coil, Igniter, ECU (G, G1, NE, IGT,
IGF terminals).

---
<a id="p200"></a>
**[PDF p.200]** — ON-VEHICLE INSPECTION (4A-FE) — SPARK TEST

### SPARK TEST — check that spark occurs
a. Disconnect high-tension cords from spark plugs.
b. Remove the spark plugs (see [PDF p.201]).
c. Install the spark plugs onto each high-tension cord.
d. Ground the spark plug.
e. Check if spark occurs while the engine is cranked.
> **HINT:** To prevent gasoline being injected during this test, crank for no more than
> 1–2 seconds at a time.

If no spark, work the diagnostic sequence (each step's spec verified against the detail pages):

| Check | Spec | If BAD |
| ----- | ---- | ------ |
| High-tension cord resistance | **25 kΩ or less per cord** | Replace the cords |
| Power supply to ignition coil | Battery voltage at coil (+) with IG ON | Check wiring switch→coil |
| Ignition coil resistance (cold) | Primary **1.28–1.56 kΩ** (2WD); Secondary **10.4–14.0 kΩ** (2WD) | Replace the ignition coil |
| Signal generator (pickup coil) resistance | **140–180 Ω** | Replace the IIA housing |
| Distributor air gap | **0.2 mm (0.008 in.) or more** | Replace the IIA housing |
| IGT signal from ECU | (see FI-48, 62) | Check ECU↔IIA wiring, then try another ECU |
| — | — | Try another igniter |

<!-- NEEDS REVIEW: the diagnostic flowchart also lists 4WD coil values (primary 0.38–0.46 Ω, secondary 7.7–10.3 kΩ). These appear ONLY in the flowchart (OCR, unit-ambiguous) — the IG-8 detail page shows 2WD only. Verify 4WD values against a complete copy before relying on them. This scan is a 2WD 4A-FE. -->

---
<a id="p201"></a>
**[PDF p.201]** — INSPECTION OF HIGH-TENSION CORDS · SPARK PLUGS

### HIGH-TENSION CORDS
1. Carefully disconnect the cords by their rubber boots from the spark plugs.
   > **NOTICE:** Pulling on or bending the cords may damage the conductor inside.
2. Remove the IIA cap without disconnecting the high-tension cords.
3. Inspect cord resistance with an ohmmeter (without disconnecting the IIA cap). **Maximum resistance: 25 kΩ per cord.** If greater, check the terminals; if necessary replace the cord and/or IIA cap.
4. Reinstall the IIA cap.
5. Reconnect the high-tension cords to the spark plugs.

### SPARK PLUGS
1. Disconnect the high-tension cords from the spark plugs.
2. Remove the spark plugs using **SST 09155-16100**.
3. Clean the spark plugs (spark plug cleaner or wire brush).
4. Visually inspect for electrode wear, thread damage, insulator damage; replace if abnormal. **Recommended spark plug: ND Q16R-U, NGK BCPR5EY.**

---
<a id="p202"></a>
**[PDF p.202]** — SPARK PLUGS (cont.) · IGNITION COIL · DISTRIBUTOR

5. **ADJUST ELECTRODE GAP** — carefully bend the outer electrode. **Correct electrode gap: 0.8 mm (0.031 in.)**
6. **INSTALL SPARK PLUGS** — using **SST 09155-16100**. **Torque: 180 kg-cm (13 ft-lb, 18 N·m)**
7. Reconnect the high-tension cords.

### INSPECTION OF IGNITION COIL
1. **Primary coil resistance (cold):** measure between the (+) and (−) terminals — **2WD 1.28–1.56 kΩ.** If not as specified, replace the coil.
2. **Secondary coil resistance (cold):** measure between the (+) terminal and the high-tension terminal — **2WD 10.4–14.0 kΩ.** If not as specified, replace the coil.

### DISTRIBUTOR
1. **INSPECT AIR GAP** — using a feeler gauge, measure the gap between the signal rotor and the pickup coil projection. **Air gap: 0.2 mm (0.008 in.) or more.** If not as specified, replace the IIA housing.

---
<a id="p203"></a>
**[PDF p.203]** — DISTRIBUTOR (cont.) · IGNITER

2. **INSPECT SIGNAL GENERATOR (PICKUP COIL) RESISTANCE** — measure between the terminals (G1–G⊖, NE–G⊖). **Pickup coil resistance (cold): 140–180 Ω.** If not as specified, replace the IIA housing.

### INSPECTION OF IGNITER
- See the Spark Test procedure on [PDF p.200].

> **Scan gap:** IG-10 through IG-14 (distributor removal / inspection / installation
> detail) are missing from this scan.

---
<a id="p204"></a>
**[PDF p.204]** — INTEGRATED IGNITION ASSEMBLY (IIA) (4A-FE) — COMPONENTS · DISASSEMBLY

Components (exploded view — image on [PDF p.204]): IIA Wire, Cord Clamp, Igniter Dust
Cover, Igniter, IIA Housing, IIA Cap, Gasket, Rotor, Ignition Coil Dust Cover, Ignition
Coil, O-Ring ✦, Gasket. (✦ = non-reusable.)

### DISASSEMBLY OF IIA
1. Remove distributor cap, gasket and rotor.
2. Remove the ignition coil dust cover.
3. Remove the igniter dust cover.
4. REMOVE IGNITION COIL — remove the two nuts and disconnect the three wires from the coil terminals; remove the four screws, ignition coil and gasket.

---
<a id="p205"></a>
**[PDF p.205]** — IIA — DISASSEMBLY (cont.) · INSPECTION

5. REMOVE IGNITER — remove the two nuts and disconnect the three wires from the igniter terminals; remove the two screws and igniter.
6. REMOVE IIA WIRE — disconnect the connector from the cord clamp; remove the screw and condenser; remove the wire grommet from the housing.

### INSPECTION OF IIA
- **INSPECT GOVERNOR SHAFT** — turn the governor shaft and check that it is not rough or worn. If rough or worn, replace the IIA housing assembly.

---
<a id="p206"></a>
**[PDF p.206]** — IIA — ASSEMBLY

1. INSTALL IIA WIRE
   a. Fit the wire grommet to the IIA housing.
   b. Install the IIA wire with the screw.
   c. Install the connector to the cord clamp.

*(Assembly continues on [PDF p.207] — IG-18.)*

---
<a id="p207"></a>
**[PDF p.207]** — IIA — ASSEMBLY (cont.)

Continuation of the IIA assembly procedure (install condenser, igniter, ignition coil,
dust covers, rotor, cap — image-guided; see [PDF p.207]). This is the last page of the
Ignition section in this scan.
