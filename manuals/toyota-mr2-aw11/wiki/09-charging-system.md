# Charging System

*Toyota MR2 (AW11) 1988 factory service manual — Charging System (section code `CH`, source pages 387–402). Covers the 4A-GE and 4A-GZE (supercharged) alternators and the engine main relay.*

## In this chapter

- [Precautions](#precautions)
- [Troubleshooting](#troubleshooting)
- [On-Vehicle Inspection](#on-vehicle-inspection)
- [Alternator](#alternator)
  - [Components](#components)
  - [Removal](#removal-of-alternator)
  - [Disassembly](#disassembly-of-alternator)
  - [Inspection and Repair](#inspection-and-repair-of-alternator)
  - [Assembly](#assembly-of-alternator)
  - [Installation](#installation-of-alternator)
- [Engine Main Relay](#engine-main-relay)

---

## Precautions

1. Check that the battery cables are connected to the correct terminals.
2. Disconnect the battery cables when the battery is given a quick charge.
3. Do not perform tests with a high voltage insulation resistance tester.
4. Never disconnect the battery while the engine is running.

---

## Troubleshooting

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| Discharge warning light does not light with ignition ON and engine off | Fuse blown | Check CHARGE, AM₂ and ENGINE fuses | |
| | Light burned out | Replace light | |
| | Wiring connection loose | Tighten loose connections | |
| | Engine main relay faulty | Check relay | CH-14 <!-- NEEDS REVIEW: manual prints "CH-14" here, but the Engine Main Relay section is at CH-16 (per this chapter's contents page and the section header); page image p.388 clearly shows "CH-14" — transcribed as printed; source appears internally inconsistent --> |
| | IC regulator faulty | Replace IC regulator | CH-7 |
| Discharge warning light does not go out with engine running (battery requires frequent recharging) | Drive belt loose or worn | Adjust or replace drive belt | CH-4 |
| | Battery cables loose, corroded or worn | Repair or replace cables | |
| | Fuse blown | Check "CHARGE" fuse | |
| | Fusible link blown | Replace fusible link | CH-3 |
| | IC regulator or alternator faulty | Check charging system | CH-5 |
| | Wiring faulty | Repair wiring | |

---

## On-Vehicle Inspection

### 1. Check battery specific gravity and electrolyte level

1. Check the specific gravity of each cell.

   **Standard specific gravity (when fully charged at 20°C / 68°F):** 1.25 – 1.27

   If not within specifications, charge the battery.
2. Check the electrolyte quantity of each cell. If insufficient, refill with distilled (or purified) water.

### 2. Check battery terminals and fusible link

1. Check that the battery terminals are not loose or corroded.
2. Check the fusible links for continuity.

### 3. Check fuses for continuity

- ENGINE fuse (10 A)
- CHARGE fuse (5 A)
- AM₂ (7.5 A)

### 4. Inspect alternator drive belt

1. Visually check the belt for separation of the adhesive rubber above and below the core, core separation from the belt side, severed core, separation of the rib from the adhesive rubber, cracking or separation of the ribs, torn or worn ribs or cracks in the inner ridges of the ribs.

   If necessary, replace the drive belt.
2. Using a belt tension gauge, check the drive belt tension.

   **Belt tension gauge:** Nippondenso BTG-20 (95506-00020), or Borroughs No. BT-33-73F

   | Belt | Drive belt tension |
   | ---- | ------------------ |
   | New belt | 175 ± 5 lb |
   | Used belt | 115 ± 20 lb |

   If necessary, adjust the drive belt tension.

> **NOTE:**
> - "New belt" refers to a belt which has been used less than 5 minutes on a running engine.
> - "Used belt" refers to a belt which has been used on a running engine for 5 minutes or more.
> - After installing the drive belt, check that it fits properly in the ribbed grooves.

### 5. Visually check alternator wiring and listen for abnormal noises

1. Check that the wiring is in good condition.
2. Check that there are no abnormal noises from the alternator while the engine is running.

### 6. Check discharge warning light circuit

1. Warm up the engine and then turn it off.
2. Turn off all accessories.
3. Turn the ignition switch to "ON." Check that the discharge warning light is lit.
4. Start the engine. Check that the light goes out.

If the light does not come on and go off as specified, troubleshoot the warning light circuit.

### 7. Check charging circuit without load

> **NOTE:** If a battery/alternator tester is available, connect the tester to the charging circuit as per the manufacturer's instructions.

1. If a tester is not available, connect a voltmeter and ammeter to the charging circuit as follows:
   - Disconnect the wire from terminal "B" of the alternator and connect it to the negative terminal of the ammeter.
   - Connect the test lead from the positive terminal of the ammeter to terminal "B" of the alternator.
   - Connect the positive lead of the voltmeter to terminal "B" of the alternator.
   - Connect the negative lead of the voltmeter to ground.
2. Check the charging circuit as follows: with the engine running from idling to 2,000 rpm, check the reading on the ammeter and voltmeter.

   **Standard amperage:** Less than 10 A

   **Standard voltage:**

   | Engine | Standard voltage | Temperature |
   | ------ | ---------------- | ----------- |
   | 4A-GE | 13.9 – 15.1 V | 25°C (77°F) |
   | 4A-GE | 13.5 – 14.3 V | 115°C (239°F) |
   | 4A-GZE | 13.7 – 14.8 V | 25°C (77°F) |
   | 4A-GZE | 13.2 – 14.0 V | 115°C (239°F) |

   - If the voltage reading is greater than standard, replace the IC regulator.
   - If the voltage reading is less than standard, check the IC regulator and alternator as follows: with terminal "F" grounded, start the engine and check the voltage reading of terminal "B".
   - If the voltage reading is greater than standard, replace the IC regulator.
   - If the voltage reading is less than standard, check the alternator.

### 8. Check charging circuit with load

1. With the engine running at 2,000 rpm, turn on the high beam headlights and place the heater fan control switch at "HI."
2. Check the reading on the ammeter.

   **Standard amperage:** More than 30 A

If the ammeter reading is less than 30 A, repair the alternator (see [Alternator](#alternator)).

> **NOTE:** If the battery is fully charged, sometimes the indication will be less than 30 A.

---

## Alternator

### Components

*(Figure: 4A-GE alternator exploded view — see page image p.392. Labeled parts: Pulley, Drive End Frame, Front Bearing, Bearing Retainer, Rotor, Rear Bearing, Rear Bearing Cover, Rubber Insulator, Terminal Insulator, Brush Holder, Spring, Brush, IC Regulator, Rectifier Holder, Rear End Frame, Rear End Cover.)*

*(Figure: 4A-GZE alternator exploded view — see page image p.392. Labeled parts: Pulley, Drive End Frame, Front Bearing, Retainer, Rotor, Rear Bearing, Rear Cover Plate, Spring, Brush, Brush Holder, Rectifier Holder, Rear End Frame, Rear Wire, Rear End Cover, Rear Cover.)*

### Removal of Alternator

1. **Disconnect cable from negative terminal of battery.**
2. **Disconnect wire from alternator.**
   1. Disconnect the connector from the alternator.
   2. Remove the nut and wire from the alternator.
3. **Remove alternator drive belt.** Loosen the alternator pivot nut, bolt and adjusting lock bolts, and remove the drive belt.
4. **Remove alternator.**
   1. Remove the pivot nut, bolt and adjusting lock bolts.
   2. Remove the alternator.

### Disassembly of Alternator

*(See [Components](#components).)*

1. **(4A-GZE) Rear cover plate.**
   1. Remove the nut and terminal insulator.
   2. Remove the three nuts and cover plate.
   3. Remove the two bolts.
2. **Remove rear end cover.**
   1. (4A-GE) Remove the nut and terminal insulator.
   2. Remove the three nuts and end cover.
3. **Remove brush holder and IC regulator (4A-GE) or rear wire (4A-GZE).**
   - (4A-GE) Remove the five screws, brush holder and IC regulator.
   - (4A-GZE) Remove the five screws, brush holder and rear wire. <!-- NEEDS REVIEW: OCR/original read "read wire"; taken as "rear wire" to match the 4A-GZE component list and heading -->
4. **Remove rectifier holder.** Remove the four screws, rectifier holder and rubber insulators.
5. **Remove pulley.**
   1. Hold SST A with a torque wrench and tighten SST B clockwise to the specified torque.

      **SST** 09820-63010

      **Torque:** 400 kg-cm (29 ft-lb, 39 N·m)
   2. Confirm that SST A is secured to the pulley shaft.
   3. As shown in the figure, grip SST C in a vise and then install the alternator to SST C.
   4. To loosen the pulley nut, turn SST A in the direction shown in the figure.

      > **CAUTION:** To prevent damage to the rotor shaft, do not loosen the pulley nut more than one-half of a turn.
   5. Remove the alternator from SST C.
   6. Turn SST B and remove all SSTs.
   7. Remove the pulley nut and the pulley.
6. **Remove rear end frame.**
   1. Remove the four nuts.
   2. Using SST, remove the rear end frame.

      **SST** 09286-46011
7. **Remove rotor from drive end frame.**

### Inspection and Repair of Alternator

#### Rotor

1. **Inspect rotor for open circuit.** Using an ohmmeter, check for continuity between the slip rings.

   **Standard resistance:** Less than 3 Ω <!-- NEEDS REVIEW: OCR read "3 0"; page image p.395 clearly shows "3 Ω" — corrected from image -->

   If there is no continuity, replace the rotor.
2. **Inspect rotor for ground.** Using an ohmmeter, check that there is no continuity between the slip ring and rotor. If there is continuity, replace the rotor.
3. **Inspect slip rings.**
   1. Check that the slip rings are not rough or scored. If rough or scored, replace the rotor.
   2. Using calipers, measure the slip ring diameter.

      **Standard diameter:** 14.2 – 14.4 mm (0.559 – 0.567 in.)

      **Minimum diameter:** 12.8 mm (0.504 in.)

      If the diameter of the slip ring is less than the minimum, replace the rotor.

#### Stator

1. **Inspect stator for open circuit.** Using an ohmmeter, check all leads for continuity. If there is no continuity, replace the drive end frame assembly.
2. **Inspect that stator is not grounded.** Using an ohmmeter, check that there is no continuity between the coil leads and drive end frame. If there is continuity, replace the drive end frame assembly.

#### Brush and Brush Holder

1. **Measure exposed brush length.** Using a scale, measure the exposed brush length.

   **Standard exposed length:** 10.5 mm (0.413 in.)

   **Minimum exposed length:** 1.5 mm (0.059 in.)

   If the brush length is less than the minimum, replace the brush.
2. **If necessary, replace brush.**
   1. Unsolder and remove the brush and the spring.
   2. Put the brush wire through the spring and insert the brush holder.
   3. Solder the wire to the brush holder as shown.

      **Standard exposed length:** 10.5 mm (0.413 in.)
   4. Check that the brush moves smoothly in the brush holder.
   5. Cut off the excess wire.

#### Rectifier

1. **Inspect positive side rectifier.**
   1. Using an ohmmeter, connect one tester probe to the positive stud and the other to each rectifier terminal.
   2. Reverse the polarity of the tester probes and repeat step 1.
   3. Check that one shows continuity and the other shows no continuity.

      If not, replace the rectifier holder.
2. **Inspect negative side rectifier.**
   1. Connect one tester probe to each rectifier terminal and the other to each rectifier negative terminal.
   2. Reverse the polarity of the tester probes.
   3. Check that one shows continuity and the other shows no continuity.

      If not, replace the rectifier holder.

#### Bearings

1. **Inspect front bearing.** Check that the bearing is not rough or worn.
2. **If necessary, replace front bearing.**
   1. Remove the four screws and bearing retainer.
   2. Using a press and socket wrench, press out the front bearing.
   3. Using SST and a press, press the front bearing into the drive end frame.

      **SST** 09608-20012 (09608-00030)
   4. Install the bearing retainer with the four screws.
3. **Inspect rear bearing.** Check that the bearing is not rough or worn.
4. **If necessary, replace rear bearing.**
   1. Using SST, remove the rear bearing cover and cover.

      **SST** 09820-00021

      > **CAUTION:** Be careful not to damage the fan.
   2. Using SST and a press, press in a new bearing and the bearing cover.

      **SST** 09285-76010

### Assembly of Alternator

*(See [Components](#components).)*

1. **Install rotor to drive end frame.**
2. **Install rear end frame.**
   1. Using a plastic hammer, lightly tap the rear end frame on the drive end frame.
   2. Install the four nuts.
3. **Install pulley.**
   1. Install the pulley to the rotor shaft by tightening the pulley nut by hand.
   2. Hold SST A with a torque wrench and tighten SST B clockwise to the specified torque.

      **SST** 09820-63010

      **Torque:** 400 kg-cm (29 ft-lb, 39 N·m)
   3. Confirm that SST A is secured to the pulley shaft.
   4. As shown in the figure, grip SST C in a vise and then install the alternator to SST C.
   5. To torque the pulley nut, turn SST A in the direction shown in the figure.

      **Torque:** 1,125 kg-cm (81 ft-lb, 110 N·m)
   6. Turn SST B and remove all SSTs.
4. **Install rectifier holder.**
   1. Install the four rubber insulators on the lead wires.
   2. Install the rectifier with four screws.
5. **(4A-GE) Install brush holder and IC regulator.**
   1. Place the brush holder cover to the brush holder.
   2. Install the IC regulator and brush holder to the rear end frame horizontally as shown in the figure.

      > **NOTE:** Make sure the brush holder's cover doesn't slip to one side during installation.
   3. Install and tighten the three screws.

      > **NOTE:** Make sure the gap between the brush holder and connector is at least 1 mm (0.04 in.).
6. **(4A-GZE) Install brush holder and rear wire.** <!-- NEEDS REVIEW: draft heading truncated ("INSTALL BRUSH HOLDER AND"); completed as "rear wire" to mirror the 4A-GZE disassembly step and component list -->
   1. Place the brush holder cover to the brush holder.
   2. Install the rear wire and brush holder to the rear end frame horizontally as shown in the figure.

      > **NOTE:** Make sure the brush holder's cover doesn't slip to one side during installation.
7. **Install rear end cover.**
   1. Install the end cover with the three nuts.
   2. Install the terminal insulator with the nut.
8. **Make sure rotor rotates smoothly.**

### Installation of Alternator

1. **Install alternator.** Mount the alternator on the engine bracket with the pivot nut, bolt and adjusting lock bolts. Do not tighten the bolts.
2. **Connect wiring to alternator.**
   1. Connect the wire to the alternator and install the nut.
   2. Connect the connector to the alternator.
3. **Connect negative cable to battery.**
4. **Install alternator drive belt.**
   1. Install the drive belt.
   2. Using a belt tension gauge, check the drive belt tension.

      **Belt tension gauge:** Nippondenso BTG-20 (95506-00020), or Borroughs No. BT-33-73F

      | Belt | Drive belt tension |
      | ---- | ------------------ |
      | New belt | 175 ± 5 lb |
      | Used belt | 115 ± 20 lb |

      > **NOTE:**
      > - "New belt" refers to a belt which has been used less than 5 minutes on a running engine.
      > - "Used belt" refers to a belt which has been used on a running engine for 5 minutes or more.
      > - After installing the drive belt, check that it fits properly in the ribbed grooves.
   3. Tighten the pivot bolt.

---

## Engine Main Relay

### Inspection of Engine Main Relay

> **NOTE:** The relay is located in the No. 2 junction block of the engine compartment.

**Inspect relay continuity**

1. Using an ohmmeter, check that there is continuity between terminals 1 and 2.
2. Check that there is continuity between terminals 3 and 5.
3. Check that there is no continuity between terminals 3 and 4.

If continuity is not as specified, replace the relay.

**Inspect relay operation**

1. Apply battery voltage across terminals 1 and 2.
2. Using an ohmmeter, check that there is continuity between terminals 3 and 4.
3. Check that there is no continuity between terminals 3 and 5.

If operation is not as described, replace the relay.
