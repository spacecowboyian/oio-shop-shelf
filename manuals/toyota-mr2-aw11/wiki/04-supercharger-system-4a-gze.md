# Supercharger System (4A-GZE)

*Section code: `SC` | source PDF pages 156–174 (manual pages SC-1 – SC-19) | 4A-GZE supercharged engine, AW11 chassis.*

Torque is given as **kg-cm (ft-lb or in.-lb, N·m)**, exactly as printed in the manual. Cross-references such as `MA-4`, `AT-8`, `SC-9` are the manual's own page codes; where they point at other chapters they are linked, otherwise they refer to a section within this chapter.

## In this chapter

- [Troubleshooting](#troubleshooting)
- [Supercharger](#supercharger)
- [Supercharger Relay](#supercharger-relay)

---

## Troubleshooting

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| **No supercharger pressure** | Compressor does not rotate properly — (a) Drive belt loose or broken | Adjust or replace drive belt | MA-4 |
| | Compressor does not rotate properly — (b) Compressor faulty | Repair compressor | SC-9 |
| | Magnetic clutch does not engage — (a) Fuses blown | Check "EFI" or "IGN" fuse | — |
| | Magnetic clutch does not engage — (b) Supercharger relay faulty | Check supercharger relay | SC-19 |
| | Magnetic clutch does not engage — (c) Magnetic clutch faulty | Check magnetic clutch | SC-3 |
| | Magnetic clutch does not engage — (d) EFI ECU faulty | Check EFI ECU | — |
| | Magnetic clutch does not engage — (e) Wiring faulty | Check wiring | — |
| **Supercharger pressure too low** | Drive belt slipping | Check or replace drive belt | MA-4 |
| | Magnetic clutch faulty | Check magnetic clutch | SC-3 |
| | Compressor faulty | Check compressor | SC-9 |
| | ABV VSV faulty | Check ABV VSV | SC-12 |
| | ABV faulty | Check ABV | SC-12 |
| | EFI ECU faulty | Check EFI ECU | — |
| **Supercharger pressure too high** | ABV VSV faulty | Check ABV VSV | SC-12 |
| | ABV faulty | Check ABV | SC-12 |
| | EFI ECU faulty | Check EFI ECU | — |

---

## Supercharger

### On-Vehicle Inspection of Supercharger

#### 1. Check supercharger oil level

> **NOTE:** With the engine cold, check the oil level on the dipstick.

1. Park the vehicle on a level spot and turn the engine off.
2. Remove the brake booster hose clamp.
3. Remove the VSV retaining bolt.
   > **CAUTION:** Do not disconnect the hoses from the VSV.
4. Turn the yellow-headed supercharger oil level dipstick counterclockwise and pull it out.
5. Wipe the dipstick clean with a rag.
6. Reinsert the dipstick. Turn it fully clockwise or the reading will not be correct.
7. Remove the dipstick again and look at the oil level on the end.
8. The oil level should be between the "L" and "F" marks on the dipstick.

   *(The dipstick head is painted yellow.)*

   If low, check for leakage and add oil up to the "F" mark as follows.
9. Add supercharger oil through the dipstick tube using a vinyl tube and syringe. <!-- source prints "though"; transcribed as "through" -->

   **Supercharger oil:** Part No. 08885-80108 or equivalent
10. Recheck the oil level.

> **NOTE:** Avoid overfilling and low level, or the supercharger could be damaged.

#### 2. Inspect magnet clutch

1. Check that the magnet clutch goes ON when the throttle valve is suddenly opened during engine idling.
2. Using an ohmmeter, measure the resistance of the stator coil between the clutch lead wire terminals.

   **Standard resistance:** 3.7 ± 0.2 Ω at 20°C (68°F) <!-- NEEDS REVIEW: OCR read the unit as "n"; page image (SC-3) clearly shows the ohm symbol Ω — corrected from image -->

   If the resistance is not as specified, replace the clutch stator.

#### 3. Inspect air by-pass valve (ABV)

While the engine running, disconnect the ABV vacuum hose and check that there is normal operating noise in ABV.

#### 4. Inspect stall test (A/T vehicle)

See page AT-8 (Automatic Transmission chapter).

#### 5. Inspect supercharger pressure

1. Install SST (turbocharger pressure gauge) between the VSV and intake manifold with a three way.

   **SST 09992-00241**
2. **(M/T vehicle)** While driving with the engine running at 1,500 rpm on the fourth gear, fully open the throttle valve and check the supercharger pressure with the engine rpm at 2,000 rpm.

   **Standard pressure:** 0.25 kg/cm² (3.6 psi, 25 kPa)
3. **(A/T vehicle)** Check the supercharger pressure with a stall test.

   **Standard pressure:** 0.30 kg/cm² (4.3 psi, 29 kPa)

If the pressure is less than that specified, inspect the supercharger assembly. If the pressure is above specification, inspect the ABV system.

### Removal of Supercharger

*(Figure: exploded component layout — reservoir tank, throttle body with air intake connector / No. 1 air inlet duct / No. 1 air outlet duct, VSV, vacuum hose (for booster), intercooler, air control valve, +gasket, supercharger, drive belt. "+" marks non-reusable parts — see page image p.160 / SC-5.)*

1. Disconnect cable from negative terminal of battery.
2. Drain engine coolant.
3. Remove radiator reservoir tank.
4. Remove VSV.
5. Remove intercooler. Disconnect the two hose clamps, and remove the four bolts and intercooler.
6. Remove air flow meter with No. 3 air cleaner hose.
   1. Disconnect the air flow meter connector.
   2. Remove the bolt and EGR VSV without disconnecting the connector.
   3. Loosen the two clamps, and remove the three bolts and air flow meter with No. 3 air cleaner hose.
7. Disconnect accelerator cable (rod) and throttle cable.
8. Disconnect the following hoses:
   1. PCV hose
   2. Brake booster hose
   3. ACV hose
   4. A/C idle up vacuum hose
   5. Emission control vacuum hoses
9. Remove No. 1 intake air connector pipe with air hose.
10. Remove drive belt (for supercharger). Loosen the idler pulley lock nut and adjusting bolt, and remove the drive belt.
11. Disconnect No. 2 and No. 3 water by-pass hoses.
12. Loosen air hose clamp.
13. Remove two bolts and air inlet duct stay.
14. Remove throttle body with air intake connector, No. 1 air inlet duct, and No. 1 air outlet duct.
    1. Remove the four bolts holding the No. 1 inlet duct to the intake manifold.
    2. Remove the three bolts and two nuts holding the No. 1 air outlet duct to the supercharger housing.
    3. Remove the throttle body with air intake connector, No. 1 air inlet duct and No. 1 air outlet duct.
15. Remove supercharger.
    1. Disconnect the ACV and supercharger connectors.
    2. Disconnect the two ACV hoses.
    3. Remove the two nuts and ACV.
    4. Remove the pivot bolt and nut.
    5. Remove the two stud bolts.
    6. As shown in the illustration, rotate the supercharger assembly so that the clutch hub is uppermost, then lift it upwards.
       > **CAUTION:** The vehicle body is easily scratched, so use a cloth or rag to protect it.

### Disassembly of Supercharger

*(Figure: exploded component layout — housing, dipstick, rear cover, rear plate (+gasket), magnet plug, front cover (+gasket), No. 2 air inlet duct, clutch hub, ring nut, clutch pulley, snap ring, clutch stator, clutch flange. "+" marks non-reusable parts — see page image p.164 / SC-9.)*

1. Drain supercharger oil. Remove the magnet plug under the rear cover and drain the oil.
2. Remove No. 2 air inlet duct. Remove the five bolts and No. 2 air inlet duct.
3. Remove clutch hub. Using SST, remove the nut, clutch hub and shim.

   **SST 09504-00011**
4. Remove clutch pulley.
   1. Using SST, remove the ring nut. **SST 09814-22010**
   2. Remove the clutch pulley and shim.
5. Remove clutch stator.
   1. Disconnect the connector from the clamp.
   2. Using snap ring pliers, remove the snap ring.
   3. Remove the clutch stator.
6. Remove clutch flange. Remove the five bolts and clutch flange.
7. Remove front cover.
   1. Disconnect the air hoses from the housing.
   2. Remove the nut and air pipe.
   3. Remove the two bolts, stud bolt, front cover and gasket.
8. Remove rear cover. Remove the eight bolts, rear cover and gasket.
9. Remove rear plate.
   1. Mount the supercharger in a soft jaw vise.
   2. Secure the bolt and remove the nut. Remove the two nuts.
   3. Remove the two bolts and rear plate.
10. If necessary, remove elbows.
11. If necessary, remove union.

### Inspection of Supercharger Components

1. **Inspect housing.** Check that there is no damage on the inside surface of the housing.
2. **Inspect rotor.**
   1. Check that there is no damage on the outside of the rotor.
   2. Check that there is no looseness in the rotor and shaft and that the rotor rotate smoothly.
3. **Inspect bearings.** Check that the bearing is not rough or worn.

### Inspection of Air By-Pass Valve (ABV) and Air Control Valve (ACV) System

#### 1. Inspect air by-pass valve (ABV)

Apply a vacuum to the ABV and measure the vacuum when the valve opens.

**Partially open vacuum:** 105 – 165 mmHg (4.134 – 6.496 in.Hg, 13.00 – 21.99 kPa)

**Fully open vacuum:** 245 – 395 mmHg (9.646 – 15.551 in.Hg, 32.66 – 52.65 kPa)

If the vacuum is not within specification, replace the ABV.

#### 2. Inspect ABV VSV

1. Apply battery voltage across the terminals.
2. Check that air flows from pipe E to air filter.
3. Disconnect the battery terminals.
4. Check that air flows from pipe E to G.

If a problem is found, replace the VSV.

#### 3. Inspect ACV

1. Apply battery voltage across the terminals.
2. Check that air flows from pipe A to B and C.
3. Disconnect the battery terminals.
4. Check that air does not flow from pipe A to B or C.

If a problem is found, replace the ACV.

### Installation of Supercharger (bench reassembly)

*Reassembly of the supercharger unit itself. See [Disassembly of Supercharger](#disassembly-of-supercharger) (SC-9) for the component layout.*

#### 1. Install elbows

Using pliers and a hammer, tap in the elbow so that it faces the same way as in the illustration.

**Elbow protrusion:** 1 – 2 mm (0.039 – 0.079 in.) <!-- NEEDS REVIEW: OCR read "2 mm (0.039 - 0.079 in.)"; page image (SC-13) clearly shows the range "1 - 2 mm" — leading "1 -" restored from image -->

#### 2. Install union

1. Apply a light coat of sealant to the part of the union to be inserted into the rear plate.

   **Sealant:** Part No. 08833-00090, THREE BOND 1131, LOCTITE 518 or equivalent
2. Using a hammer, tap the union into place with a block of wood, etc., placed between the union and the hammer.

#### 3. Install rear plate

1. Remove any packing material and be careful not to drop oil on the contacting surfaces of the rear plate and housing.
2. Apply engine oil to four locations on the upper surface of the rotor.
3. Apply a light coat of sealant to the outer edge of the groove on the side matching the housing.

   **Sealant:** Part No. 08833-00090, THREE BOND 1131, LOCTITE 518 or equivalent
   > **CAUTION:** Do not apply the sealant too liberally or it will overflow the groove in the housing and be squeezed inside the housing.
   > **NOTE:** The groove in the housing is to prevent sealant being squeezed inside housing.
4. Install the rear plate as soon as the seal packing is applied.
5. Install and torque the two bolts.

   **Torque:** 50 kg-cm (43 in.-lb, 4.9 N·m)
6. Mount the supercharger in a soft jaw vice.
7. Secure the bolt and install the nut. Install the two nuts.

   **Torque:** 500 kg-cm (36 ft-lb, 49 N·m)

#### 4. Install rear cover

Install a new gasket and the rear cover with the eight bolts.

**Torque:** 50 kg-cm (43 in.-lb, 4.9 N·m)

#### 5. Install housing front cover

1. Remove the grease inside the housing front cover.
2. Pour supercharger grease into the housing front cover.

   **Grease:** Part No. 08887-80109 or equivalent

   **Grease capacity:** 2 g (0.09 oz)
3. Install a new gasket and the housing front cover with the two bolts and stud bolt.

   **Torque:** 50 kg-cm (43 in.-lb, 4.9 N·m)
4. Install the air pipe with the nut.

   **Torque:** 50 kg-cm (43 in.-lb, 4.9 N·m)
5. Connect the air hoses to the housing.

#### 6. Install clutch flange

Install the clutch flange with the five bolts.

**Torque:** 50 kg-cm (43 in.-lb, 4.9 N·m)

#### 7. Install clutch stator

1. Align the hole of the clutch flange with the protrusion of the clutch stator.
2. Using snap ring pliers, install the snap ring, facing the taper side toward the front.

#### 8. Install clutch pulley

1. Install the clutch pulley.
2. Using SST, install the ring nut.

   **SST 09814-22010**

   **Torque:** 250 kg-cm (18 ft-lb, 25 N·m)

#### 9. Install clutch hub

1. On the shaft install the shim used previously, then install the clutch hub.
2. Using SST, install and torque the nut.

   **SST 09504-00011**

   **Torque:** 200 kg-cm (14 ft-lb, 20 N·m)

#### 10. Inspect and adjust air gap of magnet clutch

1. Set up a dial gauge as shown in the illustration.
2. Place the matchmarks to ensure that the positions of the pulley and clutch hub remain unchanged.
3. Apply battery voltage between the terminals of the connector, and measure the value of movement of the clutch hub.
   > **NOTE:** Take measurements starting from the second time the clutch hub is operated.
4. Measure the other three locations using the same method. Use the average value of the four locations for the air gap value.

   **Standard air gap:** 0.35 – 0.65 mm (0.0138 – 0.0256 in.)

   If the air gap is not within specification, replace the shim.

**Adjusting shim thickness — mm (in.):**

| Shim thickness | Shim thickness |
| -------------- | -------------- |
| 0.1 (0.004) | 0.7 (0.028) |
| 0.3 (0.012) | 0.9 (0.035) |
| 0.5 (0.020) | 1.1 (0.043) |

> **CAUTION:** When measuring, check that the location marks for the pulley and clutch hub are in the correct position.
> **NOTE:** If the air gap is greater than specification, use a thinner shim. If the air gap is less than specifications, use a thicker shim.

#### 11. Install No. 2 air inlet duct

Install a new gasket and No. 2 air inlet duct with the three bolts and two nuts.

**Torque:** 95 kg-cm (82 in.-lb, 9.4 N·m)

#### 12. Fill with supercharger oil

1. Clean and install the magnet plug with a new gasket.
2. Fill the supercharger with new oil.

   **Supercharger oil:** Part No. 08885-80108 or equivalent

   **Oil capacity:** 130 cc (7.9 cu in.)

### Installation of Supercharger (on vehicle)

*Installing the reassembled supercharger unit back on the vehicle. See [Removal of Supercharger](#removal-of-supercharger) (SC-5) for the component layout.*

#### 1. Install supercharger

1. As shown in the illustration, insert the supercharger with the clutch hub uppermost.
   > **CAUTION:** The vehicle body is easily scratched, so use a cloth or rag to protect it.
2. Install the two stud bolts.

   **Torque:** 350 kg-cm (25 ft-lb, 34 N·m)
3. Fix the lower part of the supercharger in place by inserting the pivot bolt from the rear of the engine.
4. Install the supercharger by tightening the two nuts together with the air control valve.

   **Torque:**
   - Stud bolt side: 350 kg-cm (25 ft-lb, 34 N·m)
   - Pivot bolt side: 600 kg-cm (47 ft-lb, 64 N·m)
5. Connect the ACV and supercharger connectors.

#### 2. Install throttle body with air intake connector, No. 1 air inlet duct, and No. 1 air outlet duct

1. Push in the air hose to the No. 2 air inlet duct.
2. Install the four bolts holding the No. 1 inlet duct to the intake manifold.

   **Torque:** 190 kg-cm (14 ft-lb, 19 N·m)
3. Install a new gasket and the No. 1 air outlet duct with the three bolts and two nuts.

   **Torque:** 100 kg-cm (7 ft-lb, 10 N·m)

#### 3. Install air inlet duct stay

Install the air inlet duct stay with the two bolts.

**Torque:**
- Duct side: 220 kg-cm (16 ft-lb, 22 N·m)
- Block side: 400 kg-cm (29 ft-lb, 39 N·m)

#### 4. Tighten air hose clamp

#### 5. Connect No. 2 and No. 3 water by-pass hoses

#### 6. Install drive belt

See page MA-4 (Maintenance chapter).

#### 7. Install No. 1 intake air connector pipe with air hose

#### 8. Connect the following hoses

1. PCV hose
2. Brake booster hose
3. ACV hose
4. A/C idle up vacuum hose
5. Emission control vacuum hoses

#### 9. Connect accelerator cable (rod) and throttle cable

#### 10. Install air flow meter with No. 3 air cleaner hose

1. Install the air flow meter with No. 3 air cleaner hose with the three bolts and two clamps.
2. Install the EGR VSV with the bolt.
3. Connect the air flow meter connector.

#### 11. Install intercooler

Install the intercooler with four bolts and two clamps.

#### 12. Install VSV

#### 13. Install radiator reservoir tank

#### 14. Fill with engine coolant

#### 15. Connect cable to negative terminal of battery

---

## Supercharger Relay

### Inspection of Supercharger Relay

**Location:** Inside of the luggage compartment trim.

*(Figure: relay terminal layout, terminals numbered 1–4 — see page image p.174 / SC-19.)*

#### A. Inspect relay continuity

1. Using an ohmmeter, check that there is continuity between terminals 1 and 3.
2. Check that there is no continuity between terminal 2 and 4.
3. Check the continuity between terminals 1 and 4.
4. Reverse the polarity of the tester probes and repeat step 3.
5. Check that one shows continuity and the other shows no continuity.

If continuity is not as specified, replace the relay.

#### B. Inspect relay operation

1. Apply battery voltage across terminals 1 and 3.
2. Check that there is continuity between terminals 2 and 4.

If operation is not as specified, replace the relay.
