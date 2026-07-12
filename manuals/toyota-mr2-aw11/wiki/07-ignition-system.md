# Ignition System

*Section code: `IG` | Source PDF pages 363–374 (manual pages IG-1 – IG-12) | Covers the 4A-GE and 4A-GZE ignition systems: precautions, troubleshooting, Electronic Spark Advance (ESA), on-vehicle inspection, distributor service, and ignition-timing adjustment.*

Related: 4A-GE engine internals are shared with the repo's [4A-FE / 4A-GE engine manual](../../toyota-4a-fe-4a-ge/wiki/02-service-specifications.md) (see its Ignition — Service Data section) — that manual lists slightly different ignition service-data values for its application; use the AW11 values below for the AW11 chassis.

## In this chapter

- [Precautions](#precautions) (IG-2)
- [Troubleshooting](#troubleshooting) (IG-2)
- [Electronic Spark Advance (ESA)](#electronic-spark-advance-esa) (IG-3)
- [On-Vehicle Inspection](#on-vehicle-inspection) (IG-4 – IG-8)
  - [Spark test](#spark-test) (IG-4)
  - [High-tension cord — inspection](#high-tension-cord-inspection) (IG-5)
  - [Spark plug — inspection](#spark-plug-inspection) (IG-5 – IG-6)
  - [Ignition coil — inspection](#ignition-coil-inspection) (IG-7)
  - [Distributor — inspection](#distributor-inspection) (IG-7 – IG-8)
- [Distributor](#distributor) (IG-9 – IG-12)
  - [Components](#components) (IG-9)
  - [Removal](#removal-of-distributor) (IG-9)
  - [Driven gear — replacement](#driven-gear-replacement) (IG-10)
  - [Installation and ignition-timing adjustment](#installation-and-ignition-timing-adjustment) (IG-10 – IG-12)

---

## Precautions

1. Do not keep the ignition switch on for more than 10 minutes if the engine will not start.
2. There are two methods of connecting the tachometer:
   - **To the ignition coil** — connect the positive (+) terminal to the ignition coil negative (−) terminal.
   - **To the check connector** — connect the tachometer test probe to the check connector terminal IG (−).
3. As some tachometers are not compatible with this ignition system, we recommend that you confirm the compatibility of your unit before using.
4. NEVER allow the ignition coil terminals to touch ground, as it could result in damage to the igniter and/or ignition coil.
5. Do not disconnect the battery when the engine is running.
6. Make sure that the igniter is properly grounded to the body.

---

## Troubleshooting

The "Page" column reproduces the manual's own IG-page cross-references to the remedy procedure.

| Problem | Possible cause | Remedy | Page |
|---|---|---|---|
| Engine will not start / hard to start (cranks OK) | Incorrect ignition timing | Reset timing | IG-10 |
| | Ignition coil faulty | Inspect coil | IG-7 |
| | Igniter faulty | Inspect igniter | IG-4 |
| | Distributor | Inspect distributor | IG-7 |
| | High-tension cord faulty | Inspect high-tension cords | IG-5 |
| | Spark plugs faulty | Inspect plugs | IG-5 |
| | Ignition wiring disconnected or broken | Inspect wiring | — |
| Rough idle or stalls | Spark plugs faulty | Inspect plugs | IG-5 |
| | Ignition wiring faulty | Inspect wiring | — |
| | Incorrect ignition timing | Reset timing | IG-10 |
| | Ignition coil faulty | Inspect coil | IG-7 |
| | Igniter faulty | Inspect igniter | IG-4 |
| | Distributor | Inspect distributor | IG-7 |
| | High-tension cord faulty | Inspect high-tension cords | IG-5 |
| Engine hesitates / poor acceleration | Spark plugs faulty | Inspect plugs | IG-5 |
| | Ignition wiring faulty | Inspect wiring | — |
| | Incorrect ignition timing | Reset timing | IG-10 |
| Engine dieseling (runs after ignition switch is turned off) | Incorrect ignition timing | Reset timing | IG-10 |
| Muffler explosion (after-fire) all the time | Incorrect ignition timing | Reset timing | IG-10 |
| Engine backfires | Incorrect ignition timing | Reset timing | IG-10 |
| Poor fuel economy | Spark plugs faulty | Inspect plugs | IG-5 |
| | Incorrect ignition timing | Reset timing | IG-10 |
| Engine overheats | Incorrect ignition timing | Reset timing | IG-10 |

---

## Electronic Spark Advance (ESA)

The ECU is programmed with data for optimum ignition timing under any and all operating conditions. Using data provided by sensors that monitor various engine functions (rpm, intake air volume, engine temperature, etc.), the microcomputer (ECU) triggers the spark at precisely the right instant.

### ESA system circuit

*(Figure: ESA system circuit — see source page image p.365 / IG-3.)*

Circuit nodes and labels, transcribed from the diagram:

- **Battery** → **Fusible link 1.25B** → **Fuse AM2 7.5A**
- **Ignition switch** (terminals AM2, IG2) → **Engine main relay** (terminals 1, 2, 3, 4, 5)
- **Ignition coil** → **Distributor** → **Spark plugs**
- **Igniter** terminals: B, C, Ne (+), N, IGT, IGF, Ne (−)
- **Signal rotor** and **pickup coil** feed the igniter
- **ECU** terminals: NE, IGT, IGF, G (−), G (+)

---

## On-Vehicle Inspection

### Spark test

**Check that spark occurs:**

1. Disconnect the high-tension cords from the distributor.
2. Hold the end about 12.7 mm (0.500 in.) from the body of the car.
3. See if spark occurs while the engine is being cranked.

> **NOTE:** To prevent gasoline from being injected from the injectors during this test, crank the engine for no more than 1–2 seconds at a time.

If the spark does not occur, perform the following diagnostic sequence. At each step, "If NG" is the action to take when the check fails; otherwise continue to the next step.

| Step | Check | Specification | If NG (BAD) |
|---|---|---|---|
| 1 | Spark test (above) | Spark occurs while cranking | Go to step 2 |
| 2 | Resistance of high-tension cords (see [High-tension cord — inspection](#high-tension-cord-inspection)) | Within maximum | Replace the cord |
| 3 | Power supply to ignition coil: ignition switch ON; check battery voltage at ignition coil positive (+) terminal | Battery voltage present | Check wiring between ignition switch and ignition coil |
| 4 | Resistance of ignition coil (cold) | Primary: 0.5–0.7 Ω · Secondary: 11–16 kΩ | Replace the ignition coil |
| 5 | Resistance of distributor signal generator (pickup coil) | Approx. 160 Ω | Replace the distributor |
| 6 | Air gap of distributor | Each 0.2–0.4 mm (0.008–0.016 in.) | Replace the distributor |
| 7 | IG6 signal from ECU <!-- NEEDS REVIEW: printed as "IG6" on IG-4 (source p.366); page image is not clearer than the OCR. Almost certainly the IGT signal — the ECU ignition-trigger output to the igniter, labeled "IGT" in the ESA circuit on IG-3. Kept as printed per Rule 0. --> | Signal present | Check wiring between ECU and distributor; only then try another ECU |
| 8 | Try another igniter | — | — |

### High-tension cord — inspection

1. **Carefully remove the high-tension cords by their rubber boots.**
   > **CAUTION:** Do NOT pull on the cords or bend the wires. The conductor inside may be damaged.
2. **Inspect resistance of high-tension cord and distributor cap.** Using an ohmmeter, check that the resistance does not exceed the maximum.
   - Maximum resistance: **25 kΩ per cord**
   - If more than maximum, check the terminals, and replace the high-tension cord and/or distributor cap as required.

### Spark plug — inspection

**(Platinum-tipped spark plug)**

> **CAUTION:**
> - Never use a wire brush for cleaning.
> - Never attempt to adjust the gap on a used plug.
> - Spark plugs should be replaced every 60,000 miles (100,000 km).

1. **Inspect electrode.**
   - (a) If using a megger (insulation resistance meter): measure the insulation resistance.
     - Correct insulation resistance: **more than 10 MΩ**
     - If less than 10 MΩ, proceed to step 2.
   - (b) If not using a megger: quickly race the engine to 4,000 rpm five times, then visually inspect the spark plugs.
     - If the electrode is dry ..... okay
     - If the electrode is wet ..... proceed to step 2
2. **Remove spark plugs.** Using a plug wrench (16 mm), remove the spark plugs.
3. **Visually inspect spark plugs.** Inspect the spark plugs for thread or insulator damage. If defective, replace the plug.

   | Engine | Maker | Recommended spark plug |
   |---|---|---|
   | 4A-GE | ND (Nippondenso) | PQ16R |
   | 4A-GE | NGK | BCPR5EP11 |
   | 4A-GZE | ND (Nippondenso) | PQ20R |
   | 4A-GZE | NGK | BCPR6EP11 |

4. **Inspect electrode gap.**
   - Maximum limit: **1.3 mm (0.051 in.)** — if exceeded, replace the plug.
   - Correct electrode gap of new plug: **1.1 mm (0.043 in.)**
   - If adjusting the gap of a new plug, bend only the base of the ground electrode; do not touch the tip.
5. **Clean spark plugs.** If the electrode has traces of wet carbon, allow it to dry and then clean with a spark plug cleaner.
   - Air pressure: **below 6 kg/cm² (85 psi, 588 kPa)**
   - Duration: **20 seconds or less**
   > **NOTE:** If there are traces of oil, remove with gasoline before using the spark plug cleaner.
6. **Install spark plugs.** Using a plug wrench (16 mm), install and torque the spark plugs.
   - Torque: **180 kg-cm (13 ft-lb, 18 N·m)**

### Ignition coil — inspection

1. **Disconnect the high-tension cords from the ignition coil.**
2. **Inspect primary coil resistance.** Using an ohmmeter, measure the resistance between the positive (+) and negative (−) terminals.
   - Primary coil resistance (cold): **0.5–0.7 Ω**
3. **Inspect secondary coil resistance.** Using an ohmmeter, measure the resistance between the positive (+) terminal and the high-tension terminal.
   - Secondary coil resistance (cold): **11–16 kΩ**

### Distributor — inspection

1. **Inspect air gaps.** Using a feeler gauge, measure the gap between the signal rotor and pickup coil projection.
   - Air gap: **0.2–0.4 mm (0.008–0.016 in.)**
   - If the gap is not within specification, replace the distributor.

   *(Figure: pickup layout — 4A-GE has Ne and G pickups; 4A-GZE has Ne, G1 and G2 pickups — see source page image p.369 / IG-7.)*

2. **Check signal generator.** Using an ohmmeter, check the resistance of the two signal generators.

   | Engine | "G" signal generator (cold) | Terminals | Resistance |
   |---|---|---|---|
   | 4A-GE | G | G (+) – G (−) | 140–180 Ω |
   | 4A-GZE | G1 | G1 (+) – G1 (−) | 140–180 Ω |
   | 4A-GZE | G2 | G2 (+) – G2 (−) | 140–180 Ω |

   | "Ne" signal generator (cold) | Terminals | Resistance |
   |---|---|---|
   | Ne | Ne (+) – Ne (−) | 140–180 Ω |

   If the resistance is not correct, replace the distributor.

---

## Distributor

### Components

*(Figure: distributor exploded view — see source page image p.371 / IG-9.)*

Components, transcribed from the diagram:

- Distributor cap
- Dust-proof cover
- Packing (+ non-reusable part)
- Center piece
- Rotor
- O-ring (+ non-reusable part) — 4A-GZE
- Driven gear (+ non-reusable part), pin, cover — 4A-GE / 4A-GZE

> **NOTE:** `+` marks a non-reusable part.

### Removal of distributor

1. Disconnect the high-tension cords from the cylinder head and ignition coil.
2. Disconnect the distributor connectors.
3. Remove the distributor set bolts.
4. Pull out the distributor from the cylinder head.
5. Remove the O-ring.

### Driven gear — replacement

**Replacement of distributor driven gear:**

1. **Grind driven gear and pin.**
   - (a) Align the drilled mark on the driven gear with the cavity of the housing.
   - (b) Place matchmarks on the housing and distributor shaft.
   - (c) Using a grinding wheel, grind the gear and pin.
   > **CAUTION:** Be careful not to damage the shaft.
2. **Remove pin and driven gear.**
   - (a) Using a punch and hammer, drive out the pin.
   - (b) Remove the driven gear and discard it.
3. **Install new drive gear and pin.**
   - (a) Align the matchmarks on the housing and distributor shaft.
   - (b) Align the drilled mark on the new driven gear with the cavity of the housing.
   - (c) Using a hammer, install a new pin.

### Installation and ignition-timing adjustment

1. **Set No. 1 cylinder to TDC/compression.**
   - (a) Turn the crankshaft pulley and align its groove with the "0" mark on the No. 1 timing belt cover.
   - (b) Remove the oil filler cap and check that you can see the cavity in the camshaft.
   - If necessary, turn the crankshaft pulley one complete revolution.
2. **Install distributor.**
   - (a) Install a new O-ring to the distributor.
     > **NOTE:** Always use a new O-ring when installing the distributor.
   - (b) Align the drilled mark on the driven gear with the cavity of the housing.
   - (c) Insert the distributor, aligning the center of the flange with that of the bolt hole on the cylinder head.
   - (d) Lightly tighten the hold-down bolts.
3. **Connect distributor connector.**
4. **Connect high-tension cords to cylinder head and ignition coil.**
5. **Connect tachometer and timing light to engine.** Connect the tachometer (+) terminal to the ignition coil (−) terminal.
   > **CAUTION:**
   > - NEVER allow the ignition coil terminal to touch ground, as it could result in damage to the igniter and/or ignition coil.
   > - As some tachometers are not compatible with this ignition system, we recommend that you confirm the compatibility of your unit before using.
6. **Warm up engine.** Allow the engine to reach normal operating temperature.
7. **Adjust ignition timing.**
   - (a) Short the terminals T and E1 of the check connector.
     > **NOTE:** The service connector is located near the resonator (4A-GE) or intercooler (4A-GZE).
   - (b) Using a timing light, check the ignition timing.
     - Ignition timing: **10° BTDC @ idling** (with short-circuited T–E1, transmission in "N" position)
   - (c) If necessary, loosen the distributor bolt and turn the distributor to align the marks. Recheck the timing after tightening the distributor.
     - Torque: **200 kg-cm (14 ft-lb, 20 N·m)**
   - (d) Unshort the check connector.
8. **Further check ignition timing.** (Transmission in "N" position)
   - M/T: more than **16° BTDC @ idling**
   - A/T: more than **12° BTDC @ idling**
</content>
</invoke>
