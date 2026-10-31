# Body Electrical (Part B)

Honda S2000 service manual, PDF pp. 1589–1685 (printed section 22, pp. 22-97–22-193). Covers gauge diagnostics, lighting, power sockets, horns, trunk opener, power mirrors, wipers/washers, and the start of immobilizer diagnostics.

---

### Printed page 22-97

<a id="p1589"></a>
Source: [PDF p.1589](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1589.png).

# Page 1589: S2000 Body Electrical

## Step 8
Measure the voltage between gauge assembly connector B (30P) No. 7 terminal and body ground.

**Gauge assembly connector B (30P), No. 7 (BLU/WHT).** See the source connector view for terminal orientation: ![Gauge assembly connector B](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1589.png)

**Decision Path:**
Does voltage pulse from 0 to about 5 V?
*   **YES**—Check connections, and if necessary, replace the printed circuit board.
*   **NO**—Go to step 9.

## Step 9
Turn the ignition switch OFF.

## Step 10
Disconnect the 3P connector from the output shaft (countershaft) speed sensor.

## Step 11
Turn the ignition switch ON (II).

## Step 12
Measure the voltage between the output shaft (countershaft) speed sensor 3P connector No. 2 terminal and body ground.

**Decision Path:**
Is there about 5 V?
*   **YES**—Replace the output shaft (countershaft) speed sensor.
*   **NO**—Repair a short to ground or open in the BLU/WHT wire.

---

## Resetting the Maintenance Required Indicator

### How to Reset
Push and hold the trip button, turn the ignition switch ON (II), and continue holding the trip button for more than 10 seconds.

**Blinking Pattern:**
| Mileage Range | Metric Equivalent | Behavior |
| :--- | :--- | :--- |
| 5,900 to 6,100 | 9,440 to 9,760 km | Blinks for 10 seconds when the ignition switch is turned ON (II). |
| 7,400 to 7,600 | 11,840 to 12,160 km | Comes on and stays on while the ignition switch is ON (II). |

*Page Reference: 22-97*

---

### Printed page 22-98

<a id="p1590"></a>
Source: [PDF p.1590](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1590.png).

# Tachometer Circuit Troubleshooting

**'00-03 models**

> **NOTE:** If the MIL is on, troubleshoot the PGM-FI problem first.

1. Remove the gauge assembly (see page 22-89).
2. Disconnect gauge assembly connector C (20P) and ECM connector A (32P).
3. Check for continuity between gauge assembly connector C (20P) No. 5 terminal and ECM connector A (32P) No. 19 terminal.

**Gauge assembly connector C (20P), No. 5 (BLU), and ECM connector A (32P), No. 19.** See [source connector views](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1590.png) for terminal orientation.

**Is there continuity?**
- **YES** — Go to step 4.
- **NO** — Repair an open in the BLU wire between the gauge assembly and the ECM.

4. Disconnect EPS control unit connector B (14P).
5. Check for continuity between gauge assembly connector C (20P) No. 5 terminal and body ground.

**Gauge assembly connector C (20P), No. 5 (BLU), and ECM connector A (32P), No. 19.** See [source connector views](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1590.png) for terminal orientation.

**Is there continuity?**
- **YES** — Repair a short to ground in the BLU wire between the gauge assembly, the EPS control unit and the ECM.
- **NO** — Go to step 6.

6. Reconnect gauge assembly connector C (20P), EPS control unit connector B (14P) and ECM connector A (32P).
7. Check the EPS system for DTC 22 or 23.

**Is DTC 22 or 23 present?**
- **YES** — Go to the EPS system Troubleshooting. If OK, substitute a known-good ECM and retest the circuit. If OK, replace the ECM.
- **NO** — Check for continuity between the gauge assembly connector A14 terminal and the EPS control unit connector B12 terminal, and the gauge assembly connector C5 terminal and the EPS control unit connector B5 terminal. If OK, replace the main printed circuit board in the gauge assembly.

*Page Reference: 22-98*

---

### Printed page 22-99

<a id="p1591"></a>
Source: [PDF p.1591](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1591.png).

# Tachometer Circuit Troubleshooting — 2004–2005 models

**NOTE:** If the MIL is on, troubleshoot the PGM-FI problem first.

1. Remove the gauge assembly (see page 22-89).
2. Disconnect gauge assembly connector B (30P) and ECM connector A (32P).
3. Check for continuity between gauge assembly connector B (30P) No. 3 terminal and ECM connector A (32P) No. 19 terminal.

**Gauge assembly connector B (30P), No. 3 (BLU), and ECM connector A (32P), No. 19.** See [source connector views](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1591.png).

**Is there continuity?**
- **YES:** Go to step 4.
- **NO:** Repair an open in the BLU wire between the gauge assembly and the ECM.

4. Disconnect EPS control unit connector B (14P).
5. Check for continuity between gauge assembly connector B (30P) No. 3 terminal and body ground.

**Gauge assembly connector B (30P), No. 3 (BLU).** See [source connector view](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1591.png).

**Is there continuity?**
- **YES:** Repair a short to ground in the BLU wire between the gauge assembly, the EPS control unit and the ECM.
- **NO:** Go to step 6.

6. Reconnect gauge assembly connector B (30P), EPS control unit connector B (14P) and ECM connector A (32P).
7. Check the EPS system for DTC 22 or 23.

**Is DTC 22 or 23 present?**
- **YES:** Go to the EPS system Troubleshooting. If OK, substitute a known-good ECM and retest the circuit. If OK, replace the ECM.
- **NO:** Check for continuity between the gauge assembly connector B21 terminal and the EPS control unit connector B12 terminal, and the gauge assembly connector B3 terminal and the EPS control unit connector B5 terminal. If OK, replace the main printed circuit board in the gauge assembly.

**Source Page:** 22-99

---

### Printed page 22-100

<a id="p1592"></a>
Source: [PDF p.1592](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1592.png).

# Tachometer Circuit Troubleshooting (continued) — 2006–2008 models

**Note:** If the MIL is on, troubleshoot the PGM-FI problem first.

1. Remove the gauge assembly (see page 22-89).
2. Disconnect gauge assembly connector B (30P).
3. Jump the SCS line with the HDS, then disconnect ECM connector E (31P).
4. Check for continuity between gauge assembly connector B (30P) No. 3 and ECM connector E (31P) No. 25. Both test points are on the BLU wire; see the [source connector views](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1592.png).
   - **YES:** Go to step 5.
   - **NO:** Repair an open in the BLU wire between the gauge assembly and ECM.
5. Disconnect EPS control unit connector B (14P).
6. Check for continuity between gauge assembly connector B (30P) No. 3 and body ground.
   - **YES:** Repair a short to ground in the BLU wire between the gauge assembly, EPS control unit, and ECM.
   - **NO:** Go to step 7.
7. Reconnect gauge assembly connector B (30P), EPS control unit connector B (14P), and ECM connector A (32P).
8. Check the EPS system for DTC 22 or 23.
   - **YES:** Go to EPS system troubleshooting. If that system is OK, substitute a known-good ECM and retest. If the circuit is then OK, replace the ECM.
   - **NO:** Check continuity between gauge assembly B21 and EPS control unit B12, and between gauge assembly B3 and EPS control unit B5. If both paths are OK, replace the main printed circuit board in the gauge assembly.

The source page names ECM connector **E (31P)** for the test in step 4 but **A (32P)** for reconnection in step 7; this inconsistency is present in the scan.

---

### Printed page 22-101

<a id="p1593"></a>
Source: [PDF p.1593](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1593.png).

# Coolant Temperature Gauge Circuit Troubleshooting

**'00-03 models**

1. Check for DTCs with the HDS.
   Is DTC P0116, P0117, or P0118 Indicated?
   - **YES** — G o to the ECM DTC Troubleshooting.
   - **NO** — Go to step 2.

2. Remove the gauge assembly (see page 22-89).

3. Disconnect gauge assembly connector C (20P) and ECM connector A (32P).

4. Check for continuity between gauge assembly connector C (20P) No. 7 terminal and ECM connector A (32P) No. 1 terminal.

   **Connector views:** Gauge assembly C (20P), No. 7, and ECM A (32P), No. 1; see [source image](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1593.png).

   Is there continuity?
   - **YES** — Go to step 5.
   - **NO** — Repair an open in the YEL/GRN wire between the gauge assembly and the ECM.

5. Check for continuity between gauge assembly connector C (20P) No. 7 terminal and body ground.

   **Connector view:** Gauge assembly C (20P), No. 7 (YEL/GRN); see [source image](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1593.png).

   Is there continuity?
   - **YES** — Check the output from the ECM first, if OK, repair a short to ground in the YEL/GRN wire between the gauge assembly and the ECM . B
   - **NO** — Check connections. If OK, substitute a known-good gauge assembly. If the problem goes away, replace the main printed circuit board in the gauge assembly. •

22-101

---

### Printed page 22-102

<a id="p1594"></a>
Source: [PDF p.1594](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1594.png).

# Gauges
## Coolant Temperature Gauge Circuit Troubleshooting (cont'd)
### '04-05 models

1. Check for DTCs with the HDS.
   - Is DTC P0116, P0117, or P0118 indicated?
     - **YES** — Go to the ECM DTC Troubleshooting.
     - **NO** — Go to step 2.

2. Remove the gauge assembly (see page 22-89).

3. Disconnect gauge assembly connector B (30P) and ECM connector A (32P).

4. Check for continuity between gauge assembly connector B (30P) No. 5 terminal and ECM connector A (32P) No. 1 terminal.

   **Connector views:** Gauge assembly B (30P), No. 5, and ECM A (32P), No. 1; see [source image](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1594.png).

   - Is there continuity?
     - **YES** — Go to step 5.
     - **NO** — Repair an open in the YEL/GRN wire between the gauge assembly and the ECM.

5. Check for continuity between gauge assembly connector B (30P) No. 5 terminal and body ground.

   **Connector view:** Gauge assembly B (30P), No. 5 (YEL/GRN); see [source image](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1594.png).

   - Is there continuity?
     - **YES** — Check the output from the ECM first; if OK, repair a short to ground in the YEL/GRN wire between the gauge assembly and the ECM.
     - **NO** — Check connections; if OK, substitute a known-good gauge assembly. If the problem goes away, replace the main printed circuit board in the gauge assembly.

*Page Reference: 22-102*

---

### Printed page 22-103

<a id="p1595"></a>
Source: [PDF p.1595](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1595.png).

# Reminder Systems — Component Location Index

![Reminder system component locations](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1595.png)

- Driver’s seat belt buckle switch: on the driver’s seat belt buckle.
- Driver’s door switch: at the driver’s door opening.
- Gauge assembly: bulb replacement on pp.22-56 (2000–2003), 22-57 (2004–2005), 22-58 (2006–2007), and 22-59 (2008); replacement on p.22-89.
- Ignition key switch: test on p.22-232.
- Parking brake switch: test on p.19-12.

---

### Printed page 22-104

<a id="p1596"></a>
Source: [PDF p.1596](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1596.png).

# Reminder Systems — Circuit Diagram, 2000–2003 models

![2000–2003 reminder systems circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1596.png)

The diagram shows the battery, main under-hood fuses No. 41 (100 A), No. 42 (40 A), and No. 54 (30 A), and gauge assembly fuse No. 23 (10 A). The gauge assembly includes the seat belt reminder indicator (1.12 W), LCD display, beeper driver, odometer/trip switch, and mph/km/h switch. Inputs include the driver’s door switch (closed when door open), driver’s seat belt buckle switch (closed when unbuckled), and ignition key switch (closed when key inserted). Grounds shown: G601, G501, and G401. Follow the source diagram for actual wire paths and terminal associations.

---

### Printed page 22-105

<a id="p1597"></a>
Source: [PDF p.1597](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1597.png).

# Reminder Systems — Circuit Diagram, 2004–2008 models

![2004–2008 reminder systems circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1597.png)

The diagram shows the battery, main under-hood fuses No. 41 (100 A), No. 42 (40 A), and No. 54 (30 A), ignition switch, under-dash fuses No. 25 (7.5 A), No. 5 (7.5 A), and No. 23 (10 A), and gauge assembly. The gauge assembly includes the seat belt reminder indicator (1.12 W), LCD display, CPU, beeper, dash lights brightness controller, odometer/trip switch, mph/km/h switch, and clock switch. Inputs include the driver’s door, seat belt buckle, parking brake, and ignition key switches. Grounds shown: G601, G501, and G401. Follow the source diagram for actual wire paths and connector pin associations.

---

### Printed page 22-106

<a id="p1598"></a>
Source: [PDF p.1598](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1598.png).

# Reminder Systems — System Input Test, 2000–2003 models

1. Remove the gauge assembly (see page 22-89).
2. Inspect all connectors and socket terminals for good contact. Repair bent, loose, or corroded terminals and recheck the system. If the terminals look OK, proceed to step 3 on the next page.

![Gauge assembly connector A (14P), B (12P), and C (20P) terminal views](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1598.png)

The connector views are from the wire side of the female terminals. Use the source image for pin locations and wire colors; the OCR does not preserve their spatial associations reliably.

---

### Printed page 22-107

<a id="p1599"></a>
Source: [PDF p.1599](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1599.png).

# Reminder Systems — System Input Test (continued), 2000–2003 models

3. With the connectors connected, back-probe the connectors and perform these input tests. If a test fails, correct its cause and retest. If every test passes, replace the faulty gauge assembly.

| Cavity; wire | Condition | Desired result | Possible causes if result differs |
|---|---|---|---|
| B4; YEL | Ignition ON (II) | Battery voltage to ground | No. 5 (7.5 A) under-dash fuse blown; open wire |
| B5; WHT/RED | All conditions | Battery voltage to ground | No. 25 (7.5 A) under-dash fuse blown; open wire |
| B3; RED/BLK | Combination light switch ON | Battery voltage to ground | No. 23 (10 A) under-dash fuse blown; faulty taillight relay; faulty combination light switch; open wire |
| B8; BLK | All conditions | Less than 0.5 V to ground | Poor G501 ground; open wire |
| C2; RED/WHT | Key inserted | Less than 1 V to ground | Faulty ignition key switch; poor G401 ground; open wire |
| C2; RED/WHT | Key removed | 5 V or more to ground | Faulty ignition switch; short to ground |
| A1; BLU/RED | Ignition ON (II), driver belt unbuckled | Less than 1 V to ground | Faulty buckle switch; poor G601 ground; open wire |
| A1; BLU/RED | Ignition ON (II), driver belt buckled | 5 V or more to ground | Faulty buckle switch; short to ground |
| B6; GRN | Driver’s door open | Less than 1 V to ground | Faulty driver’s door switch; open wire |
| B6; GRN | Driver’s door closed | 5 V or more to ground | Faulty driver’s door switch; short to ground |
| B4; YEL | Ignition ON (II), trip reset pressed | Beeper sounds | Faulty beeper; poor G501 ground; open wire; faulty gauge assembly |
| B5; WHT/RED | Ignition ON (II), trip reset pressed | Beeper sounds | Same four causes as preceding row |
| B8; BLK | Ignition ON (II), trip reset pressed | Beeper sounds | Same four causes as preceding row |

---

### Printed page 22-108

<a id="p1600"></a>
Source: [PDF p.1600](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1600.png).

# Reminder Systems — System Input Test (continued), 2004–2008 models

1. Remove the gauge assembly (see page 22-89).
2. Inspect the connectors and socket terminals for good contact. Repair bent, loose, or corroded terminals and recheck the system. If the terminals look OK, proceed to step 3 on the next page.

![Gauge assembly connector A (22P) and B (30P) terminal views](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1600.png)

The connector views are from the wire side of the female terminals. Use the source image for pin locations and wire colors; the OCR does not preserve their spatial associations reliably.

---

### Printed page 22-109

<a id="p1601"></a>
Source: [PDF p.1601](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1601.png).

# Reminder Systems — System Input Test (continued), 2004–2008 models

3. With the connectors connected, back-probe the connectors and perform these input tests.

*   If any test indicates a problem, find and correct the cause, then recheck the system.
*   If all the input tests prove OK, the gauge assembly is faulty; replace it.

| Cavity | Wire Test Condition | Test: Desired Result | Possible Cause if Desired Result is not Obtained |
| :--- | :--- | :--- | :--- |
| **A9** | YEL<br>Ignition switch ON (II) | Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 5 (7.5 A) fuse in the under-dash fuse/relay box<br>• An open in the wire |
| **A10** | WHT/RED<br>Under all conditions | Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 25 (7.5 A) fuse in the under-dash fuse/relay box<br>• An open in the wire |
| **A8** | RED/BLK<br>Combination light switch ON | Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 23 (10 A) fuse in the under-dash fuse/relay box<br>• Faulty taillight relay<br>• Faulty combination light switch<br>• An open in the wire |
| **A17** | BLK<br>Under all conditions | Measure the voltage to ground:<br>There should be less than 1 V. | • Poor ground (G501)<br>• An open in the wire |
| **B6** | RED/WHT<br>Ignition key is inserted into the ignition switch | Measure the voltage to ground:<br>There should be less than 1 V. | • Faulty ignition key switch<br>• Poor ground (G401)<br>• An open in the wire |
| **B6** | RED/WHT<br>Ignition key not in ignition | Measure the voltage to ground:<br>There should be 5 V or more. | • Faulty ignition switch<br>• A short to ground in the wire |
| **B4** | BLU/RED<br>Ignition switch ON (II) and driver's seat belt unbuckled | Measure the voltage to ground:<br>There should be less than 1 V. | • Faulty driver's seat belt buckle switch<br>• Poor ground (G601)<br>• An open in the wire |
| **B4** | BLU/RED<br>Ignition switch ON (II) and driver's seat belt buckled | Measure the voltage to ground:<br>There should be 5 V or more. | • Faulty driver's seat belt buckle switch<br>• A short to ground in the wire |
| **B23** | GRN/WHT<br>Ignition switch ON (II) and parking brake lever pulled | Measure the voltage to ground:<br>There should be less than 1 V. | • Poor ground<br>• Faulty parking brake switch<br>• An open in the wire |
| **B23** | GRN/WHT<br>Ignition switch ON (II) and parking brake lever released | Measure the voltage to ground:<br>There should be battery voltage. | • Faulty parking brake switch<br>• A short to ground in the wire |
| **A14** | GRN<br>Driver's door open | Measure the voltage to ground:<br>There should be less than 1 V. | • Faulty driver's door switch<br>• An open in the wire |
| **A14** | GRN<br>Driver's door closed | Measure the voltage to ground:<br>There should be 5 V or more. | • Faulty driver's door switch<br>• A short to ground in the wire |
| **A9** | YEL<br>Ignition switch ON (II) and trip reset button pressed | Check the beeper operation:<br>The beeper should come on. | • Faulty beeper<br>• Poor ground (G501)<br>• An open in the wire<br>• Faulty gauge assembly |
| **A10** | WHT/RED<br>Ignition switch ON (II) and trip reset button pressed | Check the beeper operation:<br>The beeper should come on. | • Faulty beeper<br>• Poor ground (G501)<br>• An open in the wire<br>• Faulty gauge assembly |
| **A17** | BLK<br>Ignition switch ON (II) and trip reset button pressed | Check the beeper operation:<br>The beeper should come on. | • Faulty beeper<br>• Poor ground (G501)<br>• An open in the wire<br>• Faulty gauge assembly |

---

### Printed page 22-110

<a id="p1602"></a>
Source: [PDF p.1602](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1602.png).

# Exterior Lights — Component Location Index

![Exterior front light component locations](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1602.png)

- Headlight relay 1 (right) and headlight relay 2 (left): main under-hood fuse/relay box; test on p.22-48.
- Headlights: HID troubleshooting p.22-133; HID bulb removal p.22-136; bulb replacement p.22-138; headlight replacement p.22-139; adjustment p.22-140.
- HID unit: replacement p.22-138.
- Back-up light switch: test and replacement p.13-4.
- Side turn signal light: replacement p.22-141.
- Front parking/side marker/turn signal lights: bulb replacement p.22-138; replacement p.22-139.

---

### Printed page 22-111

<a id="p1603"></a>
Source: [PDF p.1603](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1603.png).

# Exterior Lights — Component Location Index (continued)

![Exterior rear light component locations](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1603.png)

- Side marker light: shown at the rear side of the car.
- Taillight assembly, back-up light, and turn signal light: replacement p.22-142.
- High mount brake light: replacement p.22-143.
- License plate light: replacement p.22-143.

---

### Printed page 22-112

<a id="p1604"></a>
Source: [PDF p.1604](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1604.png).

# Exterior Lights — Component Location Index (continued)

![Exterior light controls and relays](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1604.png)

- Dash lights brightness controller: input test pp.22-155 (2000–2003), 22-157 (2004–2008).
- High beam indicator: bulb locations pp.22-56 (2000–2003), 22-57 (2004–2005), 22-58 (2006–2007), 22-59 (2008).
- DRL indicator, except 2000–2005 USA models: bulb locations on the same four year-specific pages.
- Daytime running lights subcontrol unit, 2006–2008 USA models: input test p.22-131.
- Daytime running lights control unit, except 2000–2005 USA models: input test p.22-127.
- High beam cut relay, except 2000–2005 USA models: test p.22-48.
- Combination light switch: test/replacement p.22-126.
- IG2 cut relay and taillight relay: tests p.22-48.
- Under-dash fuse/relay box: shown in the inset.

---

### Printed page 22-113

<a id="p1605"></a>
Source: [PDF p.1605](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1605.png).

# Exterior Lights — Circuit Diagram, 2000–2003 USA models

![Exterior lights circuit diagram, 2000–2003 USA models](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1605.png)

Shows battery; under-hood fuses No. 41 (100 A), No. 45 (20 A), No. 43 (20 A), and No. 54 (30 A); headlight relays 1 and 2; under-dash fuse No. 23 (10 A) and taillight relay; combination light switch; HID low beams (35 W), high beams (55 W), high-beam indicator (1.12 W), parking, side marker, taillights, and license plate light. Follow the diagram for actual wire paths, connectors, and grounds.

---

### Printed page 22-114

<a id="p1606"></a>
Source: [PDF p.1606](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1606.png).

# Exterior Lights — Circuit Diagram, 2004–2005 USA models

![Exterior lights circuit diagram, 2004–2005 USA models](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1606.png)

Shows battery; under-hood fuses No. 41 (100 A), No. 45 (20 A), No. 43 (20 A), and No. 54 (30 A); headlight relays 1 and 2; under-dash fuse No. 23 (10 A) and taillight relay; combination light switch; HID low beams (35 W), high beams (55 W), high-beam indicator (1.12 W), front parking/side marker lamps (5 W), rear side marker and taillight LED arrays, and license plate light (5 W). Follow the diagram for actual wire paths, connectors, and grounds.

---

### Printed page 22-115

<a id="p1607"></a>
Source: [PDF p.1607](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1607.png).

# Exterior Lights — Circuit Diagram, 2006–2008 USA models (part 1)

![Exterior lights circuit diagram, 2006–2008 USA models, part 1](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1607.png)

Shows battery; main under-hood fuse/relay box with fuses No. 41 (100 A), No. 42 (40 A), No. 54 (30 A), No. 45 (20 A), and No. 43 (20 A); headlight relays 1 and 2; daytime running lights control unit; HID low beams (35 W), high beams (55 W), and gauge high-beam indicator (1.12 W). Connection labels A–E continue on subsequent diagram pages. Follow the image for exact connections.

---

### Printed page 22-116

<a id="p1608"></a>
Source: [PDF p.1608](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1608.png).

# Exterior Lights — Circuit Diagram, 2006–2008 USA models (part 2)

![Exterior lights circuit diagram, 2006–2008 USA models, part 2](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1608.png)

Continues connection labels A–E from the preceding page. Shows ignition switch, engine start and clutch interlock switches, IG2 cut relay, under-dash fuses No. 23 (10 A), No. 27 (10 A), and No. 19 (7.5 A), high-beam cut relay, daytime running lights control and subcontrol units, DRL indicator, parking brake switch, and ground points G402 and G401. Follow the diagram for connector pins and wire paths.

---

### Printed page 22-117

<a id="p1609"></a>
Source: [PDF p.1609](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1609.png).

# Exterior Lights — Circuit Diagram, 2006–2008 USA models (part 3)

![Exterior lights circuit diagram, 2006–2008 USA models, part 3](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1609.png)

Continues the taillight relay circuit in the under-dash fuse/relay box and combination light switch. The diagram includes front parking/side marker lights (5 W), rear side marker and taillight LED arrays, license plate light (5 W), and grounds G401, G301, G201, and G602. Follow the source image for wiring and terminal associations.

---

### Printed page 22-118

<a id="p1610"></a>
Source: [PDF p.1610](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1610.png).

# Exterior Lights — Circuit Diagram, 2000–2003 Canada models (part 1)

![Exterior lights circuit diagram, 2000–2003 Canada models, part 1](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1610.png)

Shows battery; under-hood fuses No. 41 (100 A), No. 42 (40 A), No. 54 (30 A), No. 45 (20 A), and No. 43 (20 A); headlight relays 1 and 2; under-dash fuse No. 27 (10 A); daytime running lights control unit and DRL indicator; parking brake switch; HID low beams (35 W), high beams (55 W), and gauge high-beam indicator (1.12 W). The circuit continues on the next page. Follow the image for exact wiring.

---

### Printed page 22-119

<a id="p1611"></a>
Source: [PDF p.1611](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1611.png).

# Exterior Lights — Circuit Diagram, 2000–2003 Canada models (part 2)

![2000–2003 Canada exterior lights circuit, part 2](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1611.png)

Continues the daytime running lights circuit from p.22-118. Shows the ignition switch, engine start switch, clutch interlock switch, IG2 cut relay, under-dash fuses No. 23 (10 A) and No. 19 (7.5 A), high-beam cut relay, taillight relay, daytime running lights control unit, combination light switch, brake fluid level switch, and exterior parking, side marker, taillights, and license plate light. Follow the source diagram for actual wire paths and terminal associations.

---

### Printed page 22-120

<a id="p1612"></a>
Source: [PDF p.1612](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1612.png).

# Exterior Lights — Circuit Diagram, 2004–2005 Canada models (part 1)

![2004–2005 Canada exterior lights circuit, part 1](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1612.png)

Shows battery; under-hood fuses No. 41 (100 A), No. 42 (40 A), No. 54 (30 A), No. 45 (20 A), and No. 43 (20 A); headlight relays 1 and 2; under-dash fuse No. 27 (10 A); daytime running lights control unit and indicator; parking brake switch; HID low beams (35 W), high beams (55 W), and gauge high-beam indicator (1.12 W). Circuit continues on the next page; use the source image for wiring.

---

### Printed page 22-121

<a id="p1613"></a>
Source: [PDF p.1613](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1613.png).

# Exterior Lights — Circuit Diagram, 2004–2005 Canada models (part 2)

![2004–2005 Canada exterior lights circuit, part 2](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1613.png)

Continues the daytime running lights circuit from p.22-120. Shows the ignition switch, engine start and clutch interlock switches, IG2 cut relay, under-dash fuses No. 23 (10 A) and No. 19 (7.5 A), high-beam cut relay, taillight relay, daytime running lights control unit, combination light switch, brake fluid level switch, front parking/side marker lights, rear side marker and taillight LED arrays, and license plate light. Follow the source diagram for actual wiring.

---

### Printed page 22-122

<a id="p1614"></a>
Source: [PDF p.1614](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1614.png).

# Exterior Lights — Circuit Diagram, 2006–2008 Canada models (part 1)

![2006–2008 Canada exterior lights circuit, part 1](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1614.png)

Shows battery; under-hood fuses No. 41 (100 A), No. 42 (40 A), No. 54 (30 A), No. 45 (20 A), and No. 43 (20 A); headlight relays 1 and 2; under-dash fuse No. 27 (10 A); daytime running lights control unit and indicator; parking brake switch; HID low beams (35 W), high beams (55 W), and gauge high-beam indicator (1.12 W). Circuit continues on the next page; use the source image for wiring.

---

### Printed page 22-123

<a id="p1615"></a>
Source: [PDF p.1615](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1615.png).

# Exterior Lights — Circuit Diagram, 2006–2008 Canada models (part 2)

![2006–2008 Canada exterior lights circuit, part 2](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1615.png)

Continues the daytime running lights circuit from p.22-122. Shows the ignition switch, engine start and clutch interlock switches, IG2 cut relay, under-dash fuses No. 23 (10 A) and No. 19 (7.5 A), high-beam cut relay, taillight relay, daytime running lights control unit, combination light switch, front parking/side marker lights, rear side marker and taillight LED arrays, and license plate light. Follow the source diagram for actual wiring.

---

### Printed page 22-124

<a id="p1616"></a>
Source: [PDF p.1616](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1616.png).

# Exterior Lights — Back-up and Brake Light Circuit Diagrams

![Back-up lights and 2000–2003 brake lights circuit diagrams](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1616.png)

**Back-up lights:** The diagram shows battery, under-hood fuses No. 41 (100 A) and No. 42 (40 A), ignition switch, under-dash fuse No. 5 (7.5 A), back-up light switch on the transmission housing (closed in R), left and right back-up bulbs (21 W each), and ground G602.

**Brake lights, 2000–2003:** The diagram shows under-hood fuse No. 47 (10 A for 2000–2001; 15 A for 2002–2003), brake pedal position switch (closed when pedal pressed), high-mount LED brake light, left and right brake lights (21 W each), and branches to ABS modulator-control unit, ECM, and cruise control unit. Follow the image for wire paths.

---

### Printed page 22-125

<a id="p1617"></a>
Source: [PDF p.1617](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1617.png).

# Exterior Lights — Brake Light Circuit Diagram, 2004–2008 models

![2004–2008 brake lights circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1617.png)

Shows battery, under-hood fuse No. 47 (15 A), brake pedal position switch (closed when pedal pressed), high-mount LED brake light, left and right LED brake light arrays, and branches to ABS modulator-control unit (2004–2005), VSA modulator-control unit (2006–2008), ECM, and cruise control unit (2004–2005). Follow the source image for exact wiring and year-specific connections.

---

### Printed page 22-126

<a id="p1618"></a>
Source: [PDF p.1618](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1618.png).

# Exterior Lights — Combination Light Switch Test/Replacement

1. Remove the steering column covers (see page 17-9).
2. Disconnect 16P connector **A** from combination light switch **B**.
3. Remove the two screws and pull out the switch.
4. Inspect connector terminals for good contact. Repair bent, loose, or corroded terminals and recheck. If terminals look OK, test continuity in every listed switch position using the source tables. Replace the switch if continuity differs.

![Combination light switch connector and continuity tables](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1618.png)

The source image contains separate headlight/passing and turn-signal continuity tables. The OCR does not preserve the connected-terminal lines, so use the image for the exact terminal pairs.

---

### Printed page 22-127

<a id="p1619"></a>
Source: [PDF p.1619](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1619.png).

# Daytime Running Lights Control Unit Input Test — Canada models

1. Disconnect 14P connector **A** from daytime running lights control unit **B**.
2. Inspect connector and socket terminals for good contact. Repair bent, loose, or corroded terminals and recheck the system. If terminals look OK, proceed to step 3 on the next page.

![DRL control unit and 14P connector, wire side of female terminals](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1619.png)

The GRN/RED terminal marked with an asterisk applies to 2000–2005 models. Use the image for exact terminal numbers and wire colors.

---

### Printed page 22-128

<a id="p1620"></a>
Source: [PDF p.1620](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1620.png).

# Daytime Running Lights Control Unit Input Test (continued) — Canada models

3. Make these input tests at the connector.

• If any test indicates a problem, find and correct the cause, then recheck the system.

• If all the input tests prove OK, the control unit must be faulty; replace it.

| Cavity | Wire | Condition and desired result | Possible causes if result differs |
| :--- | :--- | :--- | :--- |
| 2*2 | RED/BLU | Under all conditions<br>Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 54 (30 A) fuse in the main under-hood fuse/relay box<br>• Blown No. 27 (10 A) fuse in the under-dash fuse/relay box<br>• An open in the wire |
| 12*2 | YEL/BLK | Ignition switch ON (II)<br>Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 19 (7.5 A) fuse in the under-dash fuse/relay box<br>• Faulty IG2 cut relay<br>• An open in the wire |
| 4*2 | BLK | Under all conditions<br>Measure the voltage to ground:<br>There should be less than 0.5 V. | • Poor ground (G402)<br>• An open in the wire |
| 7*2 | BLK | Under all conditions<br>Measure the voltage to ground:<br>There should be less than 0.5 V. | • Poor ground (G402)<br>• An open in the wire |
| 3 | RED/YEL | Combination light switch ON (headlights)<br>Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 45 (20 A) fuse in the main under-hood fuse/relay box<br>• Faulty headlight relay 2<br>• Faulty combination light switch<br>• Faulty diode<br>• Poor ground (G401)<br>• An open in the wire |
| 5 | RED/WHT | Combination light switch ON (headlights)<br>Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 43 (20 A) fuse in the main under-hood fuse/relay box<br>• Faulty headlight relay 1<br>• Faulty combination light switch<br>• Faulty diode<br>• Poor ground (G401)<br>• An open in the wire |
| 1 | RED/WHT | Combination light switch ON (headlights), and dimmer switch in HIGH<br>Connect a jumper wire between No. 3 and No. 1 terminals:<br>Left headlight (HIGH) and high beam indicator should come on. | • Blown bulb<br>• Faulty high beam cut relay<br>• Faulty combination light switch<br>• Faulty diode<br>• Poor ground (G401)<br>• An open in the wire |
| 11 | RED/ORN | Combination light switch ON (headlights), and dimmer switch in HIGH<br>Connect a jumper wire between No. 5 and No. 11 terminals:<br>Right headlight (HIGH) should come on. | • Blown bulb<br>• Faulty high beam cut relay<br>• Faulty combination light switch<br>• Faulty diode<br>• Poor ground (G401)<br>• An open in the wire |
| 10 | RED/BLU | Combination light switch ON (headlights), and dimmer switch in HIGH<br>Check for continuity to ground:<br>There should be continuity. | • Faulty high beam cut relay<br>• Faulty combination light switch<br>• Faulty diode<br>• Poor ground (G401)<br>• An open in the wire |
| 6 | GRN/WHT | Parking brake lever pulled<br>Check for continuity to ground:<br>There should be continuity. | • Faulty parking brake switch<br>• An open in the wire |
| 8 | BLU/RED | Under all conditions<br>Measure the voltage to ground:<br>There should be battery voltage. | • Faulty headlight relays<br>• Faulty diode<br>• An open in the wire |
| 9 | BLU/WHT | Ignition switch ON (II)<br>Attach to ground:<br>The DRL indicator should come on. | • Blown No. 5 (7.5 A) fuse in the under-dash fuse/relay box<br>• Blown bulb<br>• An open in the wire |
| 13*1 | GRN/RED | Ignition switch ON (II)<br>Attach to ground:<br>The brake system indicator should come on. | • Blown No. 5 (7.5 A) fuse in the under-dash fuse/relay box<br>• Blown bulb<br>• An open in the wire |

*¹ 2000–2005 models. *² Reconnect the connector for this test. See the [source table](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1620.png) for switch icons and exact terminal layout.

---

### Printed page 22-129

<a id="p1621"></a>
Source: [PDF p.1621](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1621.png).

# Daytime Running Lights Control Unit Input Test — 2006–2008 USA models

1. Disconnect 14P connector **A** from daytime running lights control unit **B**.
2. Inspect connector and socket terminals for good contact. Repair bent, loose, or corroded terminals and recheck the system. If terminals look OK, proceed to step 3 on the next page.

![DRL control unit and 14P connector, 2006–2008 USA](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1621.png)

Use the image for exact terminal numbers and wire colors. The Qwen draft treated wire color letter fragments as pin identifiers.

---

### Printed page 22-130

<a id="p1622"></a>
Source: [PDF p.1622](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1622.png).

# Daytime Running Lights Control Unit Input Test (continued) — 2006–2008 USA models

### 3. Make these input tests at the connector.

*   If any test indicates a problem, find and correct the cause, then recheck the system.
*   If all the input tests prove OK, the control unit must be faulty; replace it.

| Cavity and wire | Condition and desired result | Possible causes if result differs |
| :--- | :--- | :--- |
| **12*** YEL/BLK | Ignition switch ON (II)<br>Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 19 (7.5 A) fuse in the under-dash fuse/relay box<br>• Faulty IG2 cut relay<br>• An open in the wire |
| **4*** BLK | Under all conditions<br>Measure the voltage to ground:<br>There should be less than 0.5 V. | • Poor ground (G402)<br>• An open in the wire |
| **7*** BLK | Under all conditions<br>Measure the voltage to ground:<br>There should be less than 0.5 V. | • Poor ground (G402)<br>• An open in the wire |
| **3*** RED/YEL | Combination light switch ON (headlights)<br>Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 45 (20 A) fuse in the main under-hood fuse/relay box<br>• Faulty headlight relay 2<br>• Faulty combination light switch<br>• Faulty diode<br>• Poor ground (G401)<br>• An open in the wire |
| **5** RED/WHT | Combination light switch ON (headlights)<br>Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 43 (20 A) fuse in the main under-hood fuse/relay box<br>• Faulty headlight relay 1<br>• Faulty combination light switch<br>• Faulty diode<br>• Poor ground (G401)<br>• An open in the wire |
| **1** RED/WHT | Combination light switch ON (headlights), and dimmer switch in HIGH<br>Connect a jumper wire between No. 3 and No. 1 terminals:<br>Left headlight (HIGH) and high beam indicator should come on. | • Blown bulb<br>• Faulty high beam cut relay<br>• Faulty combination light switch<br>• Faulty diode<br>• Poor ground (G401)<br>• An open in the wire |
| **11** RED/ORN | Combination light switch ON (headlights), and dimmer switch in HIGH<br>Connect a jumper wire between No. 5 and No. 11 terminals:<br>Right headlight (HIGH) should come on. | • Blown bulb<br>• Faulty high beam cut relay<br>• Faulty combination light switch<br>• Faulty diode<br>• Poor ground (G401)<br>• An open in the wire |
| **2** WHT | Ignition switch ON (II), and parking brake lever released<br>Measure the voltage to ground:<br>There should be about 6.5 V. | • Faulty daytime running lights subcontrol unit<br>• An open in the wire |
| **6** GRN/WHT | Parking brake lever pulled<br>Check for continuity to ground:<br>There should be continuity. | • Faulty parking brake switch<br>• An open in the wire |
| **8** BLU/RED | Under all conditions<br>Measure the voltage to ground:<br>There should be battery voltage. | • Faulty headlight relays<br>• Faulty diode<br>• An open in the wire |

* Reconnect the connector for starred cavities. See the [source table](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1622.png) for switch icons and exact layout.

22-130

---

### Printed page 22-131

<a id="p1623"></a>
Source: [PDF p.1623](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1623.png).

# Daytime Running Lights Subcontrol Unit Input Test — 2006–2008 USA models

1. Disconnect 14P connector **A** from daytime running lights subcontrol unit **B**.
2. Inspect connector and socket terminals for good contact. Repair bent, loose, or corroded terminals and recheck the system. If terminals look OK, proceed to step 3 on the next page.

![DRL subcontrol unit and 14P connector, wire side of female terminals](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1623.png)

Use the image for exact terminal numbers and wire colors. The source includes RED/BLU; the Qwen draft incorrectly listed RED/BLK.

---

### Printed page 22-132

<a id="p1624"></a>
Source: [PDF p.1624](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1624.png).

# Daytime Running Lights Subcontrol Unit Input Test (continued) — 2006–2008 USA models

3. Make these input tests at the connector.

• If any test indicates a problem, find and correct the cause, then recheck the system.
• If all the input tests prove OK, the control unit must be faulty; replace it.

| Cavity | Wire Test condition | Test: Desired result | Possible cause if desired result is not obtained |
| :--- | :--- | :--- | :--- |
| 14* | RED/BLU<br>Under all conditions | Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 54 (30 A) fuse in the main under-hood fuse/relay box<br>• Blown No. 27 (10 A) fuse in the under-dash fuse/relay box<br>• An open in the wire |
| 1* | YEL/BLK<br>Ignition switch ON (II) | Measure the voltage to ground:<br>There should be battery voltage. | • Blown No. 19 (7.5 A) fuse in the under-dash fuse/relay box<br>• Faulty IG2 cut relay<br>• An open in the wire |
| 8*, 9* | BLK<br>Under all conditions | Measure the voltage to ground:<br>There should be less than 0.5 V. | • Poor ground (G401)<br>• An open in the wire |
| 12 | BLU/RED<br>Under all conditions | Measure the voltage to ground:<br>There should be battery voltage. | • Faulty headlight relays<br>• Faulty diode<br>• An open in the wire |
| 3 | BLU/WHT<br>Ignition switch ON (II) | Attach to ground:<br>The DRL indicator should come on. | • Blown No. 5 (7.5 A) fuse in the under-dash fuse/relay box<br>• Blown bulb<br>• An open in the wire |
| 4 | RED/BLU<br>Combination light switch ON (headlights), and dimmer switch in HIGH | Check for continuity to ground:<br>There should be continuity. | • Faulty high beam cut relay<br>• Faulty combination light switch<br>• Poor ground (G401)<br>• An open in the wire |
| 5 | GRN/WHT<br>Ignition switch ON (II), and parking brake lever pulled | Measure the voltage to ground:<br>There should be less than 1 V. | • Faulty parking brake switch<br>• An open in the wire |
| 5 | GRN/WHT<br>Ignition switch ON (II), and parking brake lever released | Measure the voltage to ground:<br>There should be battery voltage. | • Blown bulb<br>• Faulty parking brake switch<br>• Short to ground |
| 7* | WHT<br>Ignition switch ON (II), and parking brake lever released | Measure the voltage between the daytime running lights control unit No. 2 terminal and ground:<br>There should be about 6.5 V. | • Faulty daytime running lights control unit<br>• Short to ground |

* Reconnect the connector for starred cavities. See the [source table](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1624.png) for switch icons and exact layout.

**Source Page:** 22-132

---

### Printed page 22-133

<a id="p1625"></a>
Source: [PDF p.1625](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1625.png).

# HID Lamp System Troubleshooting

**WARNING**
A transient high tension (25,000 V) occurs at the bulb sockets or the high intensity discharge (HID) lamps when the combination light switch is turned ON, it may cause serious electrical shock or electrocution if you do not observe the cautions below.

**CAUTION**
*   Never turn on the combination light switch before fitting the HID bulbs to their bulb sockets and completing the reassembly of the headlight assembly.
*   Do not service the headlights assembly in wet conditions, such as rain or snow, near a sprinkler system, or when your hands are wet to prevent electrocution.
*   Do not touch the surface of the HID bulbs with your bare hands and do not stain it with any oils and fats.
*   Do not disassemble the inverter unit and the igniter unit.
*   Do not turn on the HID bulb by using a power source other than the battery mounted on your vehicle.

**Special Tools Required**
HID bulb test light 07AAJ-S3MA100

1. Check the No. 45 (20 A) and No. 43 (20 A) fuses in the main under-hood fuse/relay box.
Are the fuses OK ?
YES—Go to step 2.
NO—Replace the fuse(s), and recheck.

2. Make sure you have the anti-theft code for the audio system, then write down the audio presets.

3. Turn the combination light switch OFF.

4. Disconnect the negative battery cable.

5. Remove the socket from the HID bulb (see page 22-136).

6. Check for corrosion (A) and traces of electrical arcing (B) at the socket mating part.
![HID bulb socket inspection points A and B](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1625.png)

Is the socket corroded or burnt?
YES—Go to step 7.
NO—Replace the socket, and recheck.

**Source inconsistency:** The scan asks whether the socket is corroded or burnt, then says **YES—Go to step 7** and **NO—Replace the socket**. Those branches appear reversed, but are reproduced as printed.

---

### Printed page 22-134

<a id="p1626"></a>
Source: [PDF p.1626](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1626.png).

# Exterior Lights
## HID Lamp System Troubleshooting (cont'd)

7. Connect the HID bulb test light (A) to the socket (B).
07AAJ-S3MA100
8. Reconnect the battery negative cable.
9. Turn the combination light (headlight) switch ON.
Does the bulb In the test light come on?
- **YES**—Replace the original HID bulb (see page 22-136).
- **NO**—Go to step 10.

10. Turn the combination light (headlight) switch OFF.
11. Disconnect the battery negative cable.
12. Remove the HID bulb test light from the bulb socket.
13. Reconnect the battery negative cable.
14. Disconnect the HID unit 2P connector.
15. Turn the combination light (headlight) switch ON.
16. Check for continuity between the HID unit 2P connector No. 1 terminal and body ground.

### HID unit 2P connector
[View connector orientation in source](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1626.png).

- **Is there continuity?**
  - **YES**—Go to step 17.
  - **NO**—Repair an open in the wire between the HID unit and body ground. If the wire is OK, check for poor ground at G201 (right)/G301 (left) ('00-03 models) or G501 ('04-08 models).

> **NOTE**: After the repair is complete, enter the anti-theft code for the audio system, then enter the audio presets, and set the clock.

**Page Reference**: 22-134

---

### Printed page 22-135

<a id="p1627"></a>
Source: [PDF p.1627](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1627.png).

# HID Lamp System Troubleshooting (continued)

17. Measure voltage between HID unit 2P connector No. 2 and body ground. For the left headlight this is RED/YEL; for the right headlight RED/WHT. See the [source connector view](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1627.png).
    - **Battery voltage:** Substitute a known-good HID unit and recheck. If the symptom disappears, replace the original unit (see p.22-138).
    - **No battery voltage:** Go to step 18.
18. Disconnect main under-hood fuse/relay box connector A (18P).
19. Check continuity from fuse/relay box connector A No. 3 (left) or No. 4 (right) to HID unit 2P connector No. 2. See the [source connector views](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1627.png).
    - **Continuity:** Replace the main under-hood fuse/relay box (see p.22-46).
    - **No continuity:** Repair the open wire between the fuse/relay box and HID unit.

After repair, enter the audio anti-theft code and presets, and set the clock.

---

### Printed page 22-136

<a id="p1628"></a>
Source: [PDF p.1628](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1628.png).

# Exterior Lights
## HID Bulb Removal

### WARNING
A transient high tension (25,000 V) occurs at the bulb sockets of the high intensity discharge (HID) lamps when the combination light switch is turned ON. It may cause serious electrical shock or electrocution if you do not observe the cautions below.

### CAUTION
*   Never turn on the combination light switch before fitting the HID bulbs to their bulb sockets and completing the reassembly of the headlight assembly.
*   Do not service the headlights assembly in wet conditions, such as rain or snow, near a sprinkler system, or when your hands are wet to prevent electrocution.
*   Do not touch the surface of the HID bulbs with your bare hands and do not stain it with any oils and fats.
*   Do not disassemble the inverter unit and the igniter unit.
*   Do not turn on the HID bulb by using a power source other than the battery mounted in your vehicle.

1.  Make sure you have the anti-theft code for the audio system, then write down the audio presets.
2.  Turn the ignition switch OFF.
3.  Turn the combination light switch OFF.
4.  Disconnect the battery negative cable.
5.  Remove the front part of the inner fender as necessary (see page 20-126).
6.  Disconnect 2P connector (A) from the inverter unit.
7.  Remove the TORX bolt using a tamper-proof TORX T25 bit.
8.  Turn the cover (B) 45° counterclockwise to remove it from the headlight assembly.

[See source illustration for connector A and cover B](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1628.png).

---

### Printed page 22-137

<a id="p1629"></a>
Source: [PDF p.1629](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1629.png).

# HID Bulb Removal (continued)

9. Pull retaining spring **A** away from bulb **B**, then remove socket and bulb **C**.
10. Turn the bulb **45° counterclockwise** to remove it from the socket.
11. Install the new bulb in reverse order of removal.
12. After reconnecting the battery, enter the audio anti-theft code and presets, and set the clock.

![HID bulb retaining spring and socket removal](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1629.png)

---

### Printed page 22-138

<a id="p1630"></a>
Source: [PDF p.1630](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1630.png).

# Exterior Lights
## HID Unit Replacement

1. Make sure you have the anti-theft code for the audio system, then write down the audio presets.
2. Turn the ignition switch OFF.
3. Turn the combination light switch OFF.
4. Disconnect the battery negative cable, then disconnect the positive cable.
5. Remove the headlight assembly (see page 22-139).
6. Remove the socket from the HID bulb (see page 22-136).
7. Remove the three mounting screws and the HID unit.
8. Install in the reverse order of removal.
9. Enter the anti-theft code for the audio system, then enter the audio presets, and set the clock.

## Bulb Replacement
### Headlight

1. Disconnect the 3P connector (A) from the headlight.
   - **Headlight (high beam):** 55 W
2. Remove the rubber cover (B).
3. Pull the retaining spring (C) away from the bulb (D), then remove the bulb.
4. Install a new bulb in the reverse order of removal.
   Make sure the tabs on the bulb align with the notches in the headlight.

[See source illustration for HID unit and high-beam bulb fasteners](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1630.png).

---

### Printed page 22-139

<a id="p1631"></a>
Source: [PDF p.1631](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1631.png).

# Front Turn Signal, Parking, and Side Marker Bulb Replacement

1. Remove the inner fender (see p.20-126).
2. Disconnect connectors **A** from the lights. Front turn signal: **21 W**; front parking (2000–2003): **5 W**; front parking/side marker (2004–2008): **5 W**.
3. Turn bulb sockets **B** 45° counterclockwise to remove them from the headlight housing.
4. Install new bulbs in reverse order.

## Headlight Replacement

**Caution:** Headlights and attaching hardware become very hot during use. Let them cool before touching them.

1. Remove the front bumper: p.20-104 for 2000–2003, p.20-105 for 2004–2008, or p.20-106 for CR models.
2. Remove the front part of the inner fender as necessary (p.20-126).
3. Disconnect connectors **A** from the headlights.
4. Remove four bolts and corner upper beam **B**. High beam: **55 W**; low beam: **35 W**; front turn signal: **21 W**; front parking (2000–2003): **5 W**; parking/side marker (2004–2008): **5 W**.
5. Remove four more bolts and the headlight assembly.
6. Install in reverse order.
7. Adjust headlights to local requirements (p.22-140).

[See source for component locations and bolt positions](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1631.png).

---

### Printed page 22-140

<a id="p1632"></a>
Source: [PDF p.1632](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1632.png).

# Exterior Lights
## Headlight Adjustment

-*CAUTION**
Headlights become very hot during use; do not touch them or any attaching hardware immediately after they have been turned off.
Before adjusting the headlights:
- Park the vehicle on a level surface.
- Make sure the tire pressures are correct.
- The driver or someone who weighs the same should sit in the driver's seat.
>
1. Clean the outer lens so that you can see the center of the headlights (A).
2. Park the vehicle 25 ft (7.5 m) away from a wall or a screen (A).
>
> ![Vehicle 25 ft (7.5 m) from aiming screen](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1632.png)
3. Open the hood.

**Source Reference:** Page 22-140

---

### Printed page 22-141

<a id="p1633"></a>
Source: [PDF p.1633](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1633.png).

# Headlight Adjustment (continued)

## Low Beam Adjustment
4. Turn the low beams on.
5. Determine if the headlights are aimed properly.
**Vertical adjustment:**
Measure the height of the headlights (A). The lights should reflect **52 mm (2.1 in.)** below headlight height (B).
6. If necessary, adjust the headlights to local requirements by turning the vertical adjuster (A).

## Side Turn Signal Light Replacement
1. Push the side turn signal light (A) forward, then remove it from the fender.
2. Disconnect the **2P connector (B)** from the light.
**Side Turn Signal Light Bulb:** 5 W

[See source image for beam height and vertical adjuster](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1633.png).

---

### Printed page 22-142

<a id="p1634"></a>
Source: [PDF p.1634](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1634.png).

# Taillight Replacement

1. Open the trunk lid and pull back the trunk trim panel (p.20-77).
2. Disconnect connectors **A** from the taillight. For 2000–2003 models: brake/taillight **21/5 W**, back-up **21 W**, turn signal **21 W**, side marker **5 W**. For 2004–2008 models: brake/taillight and side marker are **LED**; back-up and turn signal are **21 W** each.
3. Remove four mounting nuts **B**, then pull out the taillight.
4. Check the gasket; replace it if distorted or permanently compressed.
5. Install in reverse order.
6. Run water over the taillight to check for leaks.

## Taillight/Brake Light LED Replacement — 2004–2008 models

1. Remove the taillight (p.22-142).
2. Remove two screws and cover **A**.
3. Remove two screws **A** and TORX screw **B**, then pull out LED unit **C**.
4. Check the gasket; replace it if distorted or permanently compressed.
5. Install the new unit in reverse order. The source calls it a “bulb” in this last step.

![Taillight and LED unit removal](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1634.png)

---

### Printed page 22-143

<a id="p1635"></a>
Source: [PDF p.1635](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1635.png).

# High Mount Brake Light Replacement

1. Open the trunk lid.
2. Disconnect 2P connector **A** from high mount brake light **B**.
3. Remove five mounting nuts and pull out the light.
4. Install in reverse order.
5. Run water over the light to check for leaks.

## License Plate Light Replacement

1. Remove the license plate light assembly and disconnect its 2P connector. Bulb rating: **5 W**.
2. Remove the lens and replace the bulb.

![High mount brake light and license plate light removal](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1635.png)

---

### Printed page 22-144

<a id="p1636"></a>
Source: [PDF p.1636](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1636.png).

# Exterior Lights
## Brake Pedal Position Switch Test

### 2000–2005 models
1. Disconnect the brake pedal position switch connector, and remove the switch.
2. Check for continuity between the No. 1 and the No. 4 terminals of the brake pedal position switch connector. There should be continuity when the button (A) is pressed, and no continuity when the button is released.
   - See [source connector view](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1636.png) for terminal orientation.
3. Check for continuity between the No. 2 and the No. 3 terminals. There should be continuity when the button is released, and no continuity when the button is pressed.
4. If the brake pedal position switch is faulty, replace it.
5. Install the brake pedal position switch, and adjust it (see page 19-6).

### 2006–2008 models
1. Disconnect the brake pedal position switch connector, and remove the switch.
2. Check for continuity between the No. 1 and the No. 2 terminals of the brake pedal position switch connector. There should be continuity when the button (A) is pressed, and no continuity when the button is released.
   - See [source connector view](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1636.png); this model uses the terminal side of **female** terminals.
3. Check for continuity between the No. 3 and the No. 4 terminals. There should be continuity when the button is released, and no continuity when the button is pressed.
4. If the brake pedal position switch is faulty, replace it.
5. Install the brake pedal position switch, and adjust it (see page 19-6).

**Page Reference**: 22-144

---

### Printed page 22-145

<a id="p1637"></a>
Source: [PDF p.1637](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1637.png).

# Turn Signal/Hazard Warning Lights — Component Location Index

The location illustration identifies the turn signal indicators, combination switch (turn signal switch; see p. 22-126), hazard warning switch (test/replacement, p. 22-148), turn signal/hazard relay (input test, p. 22-147), and under-dash fuse/relay box. See the [source location drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1637.png) for physical positions.

---

### Printed page 22-146

<a id="p1638"></a>
Source: [PDF p.1638](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1638.png).

# Turn Signal/Hazard Warning Lights — Circuit Diagram

Use the [source circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1638.png) for wire colors, connectors, switch paths, and grounds. It covers the battery, main under-hood and under-dash fuse/relay boxes, ignition and turn signal switches, hazard warning switch, turn signal/hazard relay, turn indicators in the gauge assembly, and front, side, and rear turn signal lights. Fuses shown include under-hood No. 41 (100 A), No. 42 (40 A), No. 49 (10 A), and under-dash No. 7 (7.5 A) and No. 23 (10 A).

---

### Printed page 22-147

<a id="p1639"></a>
Source: [PDF p.1639](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1639.png).

# Turn Signal/Hazard Relay Input Test

1. Remove the turn signal/hazard relay from the under-dash fuse/relay box.
2. Inspect the connector and socket terminals. Repair bent, loose, or corroded terminals and recheck the system. If they look OK, continue.
3. Perform the following input tests at the fuse/relay box. Correct any failed input and recheck. If all inputs pass, replace the faulty relay.

| Cavity | Test condition | Desired result | Possible cause if result differs |
| --- | --- | --- | --- |
| 3 | All conditions | Voltage to ground below 0.5 V | Poor ground G401; open wire |
| 2 | Ignition switch ON (II) | Battery voltage to ground | Under-dash fuse No. 7 (7.5 A) blown; faulty hazard switch; open wire |
| 2 | Hazard switch ON; ignition OFF | Battery voltage to ground | Under-hood fuse No. 49 (10 A) blown; faulty hazard switch; open wire |
| 1 | Hazard switch ON; connect terminals No. 1 and No. 2 | Hazard lights illuminate | Poor ground G201, G301, G501, or G602; faulty hazard or turn signal switch; open wire |
| 1 | Ignition ON (II); connect terminals No. 1 and No. 2; turn signal switch left or right | Corresponding turn signal lights illuminate | Poor ground G201, G301, G501, or G602; faulty hazard or turn signal switch; open wire |

---

### Printed page 22-148

<a id="p1640"></a>
Source: [PDF p.1640](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1640.png).

# Hazard Warning Switch Test/Replacement

1. Remove the center console (see p. 20-80).
2. Disconnect the 10P connector from the hazard warning switch.
3. Remove the two screws and the switch.
4. Check continuity between the terminals in each switch position using the [source continuity table and terminal drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1640.png).
5. If continuity differs from the table, replace the illumination bulb or switch.

---

### Printed page 22-149

<a id="p1641"></a>
Source: [PDF p.1641](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1641.png).

# Interior Lights — Component Location Index

The [source location drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1641.png) identifies the ceiling light/spotlights (test p. 22-151), driver's and passenger's door switches, trunk light (test p. 22-152), and trunk lid latch switch (test p. 22-152). Use the drawing for physical locations.

---

### Printed page 22-150

<a id="p1642"></a>
Source: [PDF p.1642](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1642.png).

# Interior Lights — Circuit Diagram

Use the [source circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1642.png) for connector pins, wire colors, grounds, and year-specific paths. It includes battery power through main under-hood fuses No. 41 (100 A) and No. 54 (30 A), under-dash fuse No. 24 (7.5 A), gauge assembly, keyless door lock control unit, driver's and passenger's door switches, ceiling light/spotlights (two 5 W lamps), trunk light (5 W), trunk indicator, and trunk lid latch switch. The diagram distinguishes 2000–2003 (`*1`) and 2004–2008 (`*2`) models.

---

### Printed page 22-151

<a id="p1643"></a>
Source: [PDF p.1643](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1643.png).

# Ceiling Light/Spotlight Test

1. Turn the ceiling light/spotlight switch OFF.
2. Pry off the lens. The ceiling light/spotlight bulb is 5 W.
3. Remove the two screws and the ceiling light/spotlight housing.
4. Disconnect the 4P connector from the housing.
5. Check continuity between terminals in each switch position using the [source table](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1643.png), including the body-ground contact.
6. If continuity differs from the table, replace the bulbs or light.

---

### Printed page 22-152

<a id="p1644"></a>
Source: [PDF p.1644](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1644.png).

# Interior Lights — Trunk Light Test

1. Open the trunk lid.
2. Pry out the trunk light assembly. The trunk light bulb is 5 W.
3. Disconnect the 2P connector from the housing.
4. Open the trunk light cover.
5. Check continuity between terminals No. 1 and No. 2.
6. If there is no continuity, replace the bulb or light.

## Trunk Lid Latch Switch Test

1. Open the trunk lid.
2. Disconnect the 3P connector from the trunk lid latch. View the terminal drawing from the male terminal side in the [source scan](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1644.png).
3. Check continuity between terminals No. 2 and No. 3: continuity with the trunk lid **open**, no continuity with it **closed**.
4. If continuity differs, replace the trunk lid latch.

---

### Printed page 22-153

<a id="p1645"></a>
Source: [PDF p.1645](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1645.png).

# Dash Lights Brightness Controller — Circuit Diagram (2000–2003 models)

Use the [source diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1645.png) for exact wires, fuses, connector cavities, and grounds. It shows battery and ignition feeds through the main under-hood and under-dash fuse/relay boxes; the gauge assembly with brightness controller, CPU, and driving circuit; the taillight relay and combination light switch; and the heater control panel, hazard, convertible top, audio remote, cruise control main, and rear window defogger switch lights. The rear window defogger switch light is marked for 2002–2003 models.

---

### Printed page 22-154

<a id="p1646"></a>
Source: [PDF p.1646](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1646.png).

# Dash Lights Brightness Controller — Circuit Diagram (2004–2008 models)

Use the [source diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1646.png) for exact connections. This version includes the gauge assembly brightness controller, taillight relay and combination light switch, audio remote switch light and audio unit, convertible top, cruise control main, hazard, heater control, passenger airbag cutoff indicator illumination, rear window defogger, and VSA OFF switch lights. Power passes through main under-hood fuses No. 41 (100 A), No. 54 (30 A), and No. 42 (40 A), and under-dash fuses No. 23 (10 A), No. 25 (7.5 A), and No. 5 (7.5 A).

---

### Printed page 22-155

<a id="p1647"></a>
Source: [PDF p.1647](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1647.png).

# Dash Lights Brightness Controller — Controller Input Test (2000–2003 models)

1. Remove the gauge assembly (see p. 22-89).
2. Inspect connector B (12P) terminals for good contact. Repair bent, loose, or corroded terminals and recheck. If terminals are sound, continue to step 3 on p. 22-156.

The [connector drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1647.png) is viewed from the wire side of the female terminals. It identifies B3 RED/BLK, B4 YEL, B5 WHT/RED, B8 and B9 BLK, and B10 RED.

---

### Printed page 22-156

<a id="p1648"></a>
Source: [PDF p.1648](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1648.png).

# Controller Input Test (2000–2003 models, continued)

3. Reconnect the connectors to the gauge assembly.
4. Back probe the connector and make the input tests below. Correct any failed input and recheck. If all pass, replace the faulty controller switch board or main printed circuit board in the gauge assembly.

| Cavity | Wire | Test condition | Desired result | Possible cause if result differs |
| --- | --- | --- | --- | --- |
| B3 | RED/BLK | Combination light switch ON (parking or headlights) | Battery voltage to ground | Under-dash fuse No. 23 (10 A) blown; taillight relay or combination light switch faulty; poor ground G401; open wire |
| B4 | YEL | Ignition ON (II) | Battery voltage to ground | Under-dash fuse No. 5 (7.5 A) blown; open wire |
| B5 | WHT/RED | All conditions | Battery voltage to ground | Under-dash fuse No. 25 (7.5 A) blown; open wire |
| B8 | BLK | All conditions | Less than 0.5 V to ground | Poor ground G501; open wire |
| B9 | BLK | All conditions | Less than 0.5 V to ground | Poor ground G501; open wire |
| B10 | RED | Combination light switch ON (parking or headlights) | Connect to ground: dash lights illuminate at full brightness | Open wire |

The switch positions are depicted as symbols in the [source table](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1648.png).

---

### Printed page 22-157

<a id="p1649"></a>
Source: [PDF p.1649](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1649.png).

# Controller Input Test (2004–2008 models)

1. Remove the gauge assembly (see p. 22-89).
2. Inspect connector A (22P) terminals for good contact. Repair bent, loose, or corroded terminals and recheck. If terminals are sound, continue to step 3 on p. 22-158.

The [connector drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1649.png) is viewed from the wire side of the female terminals. Test cavities are A8 RED/BLK, A9 YEL, A10 WHT/RED, A17 and A18 BLK, and A19 RED.

---

### Printed page 22-158

<a id="p1650"></a>
Source: [PDF p.1650](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1650.png).

# Controller Input Test (2004–2008 models, continued)

3. Reconnect the connectors to the gauge assembly.
4. Back probe the connector and make the input tests below. Correct any failed input and recheck. If all pass, replace the faulty controller switch board or main printed circuit board in the gauge assembly.

| Cavity | Wire | Test condition | Desired result | Possible cause if result differs |
| --- | --- | --- | --- | --- |
| A8 | RED/BLK | Combination light switch ON (parking or headlights) | Battery voltage to ground | Under-dash fuse No. 23 (10 A) blown; taillight relay or combination light switch faulty; poor ground G401; open wire |
| A9 | YEL | Ignition ON (II) | Battery voltage to ground | Under-dash fuse No. 5 (7.5 A) blown; open wire |
| A10 | WHT/RED | All conditions | Battery voltage to ground | Under-dash fuse No. 25 (7.5 A) blown; open wire |
| A17 | BLK | All conditions | Less than 0.5 V to ground | Poor ground G501; open wire |
| A18 | BLK | All conditions | Less than 0.5 V to ground | Poor ground G501; open wire |
| A19 | RED | Combination light switch ON (parking or headlights) | Connect to ground: dash lights illuminate at full brightness | Open wire |

The switch positions are depicted as symbols in the [source table](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1650.png).

---

### Printed page 22-159

<a id="p1651"></a>
Source: [PDF p.1651](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1651.png).

# Accessory Power Sockets — Component Location Index

The [source location drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1651.png) identifies the accessory power socket in the rear console (test/replacement, p. 22-161), ACC cut relay (test, p. 22-48), and accessory power socket relay on the CR model (test, p. 22-48).

---

### Printed page 22-160

<a id="p1652"></a>
Source: [PDF p.1652](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1652.png).

# Accessory Power Sockets — Circuit Diagram

Use the [source circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1652.png) for actual wire routing, connectors, relay contacts, and grounds. It shows the ignition switch, main under-hood and under-dash fuse/relay boxes, ACC cut and IG2 cut relays, starter cut relay, CR-model clutch interlock switch and accessory power socket relay, under-dash fuse No. 9 (10 A), accessory power socket, and ground G601. `*1` identifies the CR model; `*2` identifies other models.

---

### Printed page 22-161

<a id="p1653"></a>
Source: [PDF p.1653](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1653.png).

# Accessory Power Socket Test/Replacement

1. Remove the rear console (see p. 20-82).
2. Disconnect the 2P connector.
3. Inspect connector terminals for good contact. Repair bent, loose, or corroded terminals and recheck. If sound, continue.
4. Turn the ignition switch to ACC (I) and measure voltage between terminals No. 1 and No. 2. Battery voltage should be present. If absent, check under-dash fuse No. 9 (10 A), main under-hood fuse No. 53 (20 A, CR model), ACC cut relay, accessory power socket relay (CR model), grounds G601 and G401 (G401 on CR model), and an open wire.
5. Remove the housing and socket.

The connector drawing is viewed from the wire side of the female terminals.

---

### Printed page 22-162

<a id="p1654"></a>
Source: [PDF p.1654](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1654.png).

# Horns — Component Location Index

The [source location drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1654.png) identifies the low horn (2000–2008), high horn (2002–2008), horn relay in the main under-hood fuse/relay box, horn switch, and cable reel. Horn test/replacement is p. 22-164; horn switch test p. 22-165; relay test p. 22-48; cable reel replacement pp. 23-173–174 by model year.

---

### Printed page 22-163

<a id="p1655"></a>
Source: [PDF p.1655](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1655.png).

# Horns — Circuit Diagram

Use the [source circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1655.png) for routing, connector cavities, and grounds. Battery power passes through main under-hood fuse No. 47: 10 A on 2000–2001 models and 15 A on 2002–2008 models. The diagram includes horn relay, cable reel and horn switch, keyless door lock control unit, low horn on all models, and high horn on 2002–2008 models. Cruise switch connections differ by model year.

---

### Printed page 22-164

<a id="p1656"></a>
Source: [PDF p.1656](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1656.png).

# Horn Test/Replacement

1. Remove the front bumper: see p. 20-104 for 2000–2003, p. 20-105 for 2004–2008, or p. 20-106 for CR models.
2. Open the hood (2002–2008 models).
3. Disconnect the 1P connector and remove the horn.
4. Apply battery power to the horn terminal and ground the bracket. The horn should sound.
5. If it does not sound, replace it.

---

### Printed page 22-165

<a id="p1657"></a>
Source: [PDF p.1657](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1657.png).

# Horn Switch Test

1. Remove the steering column upper and lower covers (see p. 17-9).
2. Disconnect dashboard wire harness B 4P connector from the cable reel.
3. Check continuity between cable reel terminal No. 2 and body ground. There should be continuity with the horn switch pushed and none with it released. If continuity is present as specified, the switch is OK. Otherwise continue.
4. Remove the driver's airbag (see p. 23-164).
5. Check continuity between cable reel terminal No. 2 and the horn switch positive terminal. If none, replace the cable reel (2000–2005: p. 23-173; 2006–2008: p. 23-174) and recheck. If continuity is present, replace the horn switch.

---

### Printed page 22-166

<a id="p1658"></a>
Source: [PDF p.1658](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1658.png).

# Trunk Lid Opener — Component Location Index

The [source location drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1658.png) shows the trunk lid opener switch in the rear console (test p. 22-168) and the trunk lid opener solenoid/latch switch at the trunk latch (solenoid test p. 22-168; latch switch test p. 22-152).

---

### Printed page 22-167

<a id="p1659"></a>
Source: [PDF p.1659](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1659.png).

# Trunk Lid Opener — Circuit Diagram

Use the [source circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1659.png) for wire paths and connector positions. It covers main under-hood fuses No. 41 (100 A) and No. 54 (30 A), under-dash fuse No. 26 (15 A), keyless door lock control unit, trunk lid opener switch, trunk lid opener solenoid/latch switch, trunk indicator and trunk light, and ground G601.

---

### Printed page 22-168

<a id="p1660"></a>
Source: [PDF p.1660](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1660.png).

# Trunk Lid Opener Switch Test

1. Remove the rear console (see p. 20-82).
2. Disconnect the 2P connector from the switch.
3. Check continuity between terminals No. 1 and No. 2. There should be continuity when pushed and none when released.
4. Replace the switch if continuity differs.

## Trunk Lid Opener Solenoid Test

1. Open the trunk lid.
2. Disconnect the 3P connector from the trunk lid latch, viewing the male terminal side as shown in the [source scan](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1660.png).
3. For the UNLOCK test, momentarily apply battery **positive** to terminal No. 1 and **ground** to terminal No. 2. Do not hold battery voltage on the solenoid.
4. Replace the solenoid if it does not operate.

---

### Printed page 22-169

<a id="p1661"></a>
Source: [PDF p.1661](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1661.png).

# Power Mirrors — Component Location Index

The [source location drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1661.png) identifies the power mirror switch on the driver's door (test p. 22-172) and both power mirrors (function test p. 22-171, actuator test p. 22-172, mirror replacement p. 20-22, actuator replacement p. 22-173).

---

### Printed page 22-170

<a id="p1662"></a>
Source: [PDF p.1662](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1662.png).

# Power Mirrors — Circuit Diagram

Use the [source circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1662.png) for the mirror switch contacts and both mirror actuator motor polarities. It shows the battery, main under-hood fuses No. 41 (100 A) and No. 42 (40 A), ignition switch, IG2 cut relay, under-dash fuse No. 19 (7.5 A), power mirror switch, left and right mirrors, and ground G501.

---

### Printed page 22-171

<a id="p1663"></a>
Source: [PDF p.1663](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1663.png).

# Power Mirrors — Function Test

1. Remove the driver's door panel (see p. 20-5).
2. Disconnect the 10P connector from the power mirror switch and inspect its terminals. If sound, continue. Use the [source connector drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1663.png) for cavity orientation and wire colors.
3. Choose the test: both mirrors inoperative → step 4; left only → step 6; right only → step 7.
4. Reconnect the 10P connector. With ignition ON (II), measure between terminal No. 9 and body ground while selecting either mirror and holding the control in any direction. Battery voltage should be present. If absent, check under-dash fuse No. 19 (7.5 A) and the YEL/BLK wire. If present, continue.
5. Check terminal No. 10 to body ground while selecting either mirror and operating the control. The printed procedure says to check continuity but gives a voltage criterion of less than 1 V. It then says “no more than 1 V” indicates an open BLK wire or poor ground G501, while “less than 1 V” proceeds to individual tests. These statements conflict in the source; verify the circuit and measurement method before acting on this branch.
6. For the left mirror, jumper terminal No. 9 to No. 7 and ground No. 5 (or No. 4) with ignition ON (II). It should tilt down (or swing left). If not, check the GRN/WHT (or RED) wire, then the actuator. If neither movement works, repair the RED/YEL wire. If it works, check the switch.
7. For the right mirror, jumper terminal No. 9 to No. 6 and ground No. 5 (or No. 3) with ignition ON (II). It should tilt down (or swing left). If not, check the GRN/WHT (or BLU/WHT) wire, then the actuator. If neither movement works, repair the RED/BLU wire. If it works, check the switch.

---

### Printed page 22-172

<a id="p1664"></a>
Source: [PDF p.1664](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1664.png).

# Power Mirrors — Switch and Actuator Tests

## Power Mirror Switch Test

1. Remove the driver's door panel (see p. 20-5).
2. Disconnect the 10P connector from the power mirror switch.
3. Check continuity for each left and right switch position using the [source continuity matrix](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1664.png). The matrix includes UP, DOWN, LEFT, RIGHT, and OFF for each side.
4. Replace the switch if continuity differs.

## Power Mirror Actuator Test

1. Remove the door panel (see p. 20-5).
2. Disconnect the 3P connector from the power mirror. View terminals from the male terminal side.
3. Apply power (+) and ground (−) according to the source table:

| Movement | Terminal 1 | Terminal 2 | Terminal 3 |
| --- | --- | --- | --- |
| Tilt up | — | − | + |
| Tilt down | — | + | − |
| Swing left | − | + | — |
| Swing right | + | − | — |

4. Replace the mirror actuator if it fails to operate properly.

---

### Printed page 22-173

<a id="p1665"></a>
Source: [PDF p.1665](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1665.png).

# Power Mirror Actuator Replacement

1. Remove the power mirror from the door (see p. 20-22).
2. Record terminal positions and wire colors.
3. Cut the wire harness.
4. Carefully pull out the bottom edge of the mirror holder by hand.
5. Separate the holder from the actuator by slowly pulling them apart.
6. Remove the screws and actuator from the housing.
7. Route the new actuator harness through the mirror housing and install the actuator in reverse order.
8. Insert terminals into the connector in the original arrangement. From the male terminal side, both left and right connectors have **1 YEL, 2 BRN, 3 BLU**; see the [source drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1665.png).
9. Reassemble in reverse order. Take care not to break the mirror holder when attaching it to the actuator.
10. Operate the mirror and check for smooth actuator movement.

---

### Printed page 22-174

<a id="p1666"></a>
Source: [PDF p.1666](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1666.png).

# Wipers/Washers

## Component Location Index

| Component | Description | Page Reference |
| :--- | :--- | :--- |
| WINDSHIELD WASHER TUBE | Replacement | page 22-186 |
| WINDSHIELD WIPER ARMS and LINKAGE | Replacement | page 22-185 |
| WIPER/WASHER SWITCH | Test/Replacement | page 22-182 |
| INTERMITTENT WIPER RELAY ('00-01 models) | Test | page 22-48 |
| INTERMITTENT WIPER CIRCUIT (In the gauge assembly) | Input Test | page 22-180 |
| INTERMITTENT WIPER RELAY ('02-08 models) | Test | page 22-48 |
| WINDSHIELD WIPER MOTOR | Test, Replacement | page 22-183, 22-185 |
| WASHER RESERVOIR | Replacement | page 22-184 |
| WINDSHIELD WASHER MOTOR | Test | page 22-183 |

---

### Printed page 22-175

<a id="p1667"></a>
Source: [PDF p.1667](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1667.png).

# Wipers/Washers — Unreadable Source Page

This printed page 22-175 contains no readable manual content in the available scan; a black rectangular artifact obscures the center. See the [source page image](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1667.png). No technical procedure is inferred.

---

### Printed page 22-176

<a id="p1668"></a>
Source: [PDF p.1668](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1668.png).

# Wipers/Washers — Circuit Diagram (2000–2003 models)

Use the [source circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1668.png) for switch contacts, wire routing, relay pins, connectors, and grounds. It shows main under-hood fuses No. 41 (100 A), No. 42 (40 A), No. 54 (30 A); under-dash fuses No. 5 (7.5 A), No. 8 (20 A), No. 12 (15 A), No. 13 (7.5 A); the windshield wiper/washer switch, intermittent wiper relay, wiper and washer motors, and grounds G201, G301, and G401. Bracketed relay terminal numbers apply to 2002–2003 models.

---

### Printed page 22-177

<a id="p1669"></a>
Source: [PDF p.1669](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1669.png).

# Wipers/Washers — Circuit Diagram (gauge assembly, 2000–2003 models)

The [source diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1669.png) continues the 2000–2003 circuit in the gauge assembly. It identifies the wiper/washer driving circuit, CPU, voltage feed, under-dash fuses No. 5 and No. 25 (both 7.5 A), gauge connector cavities, and ground G501. Use the image for exact wiring.

---

### Printed page 22-178

<a id="p1670"></a>
Source: [PDF p.1670](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1670.png).

# Wipers/Washers — Circuit Diagram (2004–2008 models)

Use the [source circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1670.png) for switch contacts, relay pins, connectors, and grounds. It shows main under-hood fuses No. 41 (100 A), No. 42 (40 A), and No. 54 (30 A); under-dash fuses No. 5 (7.5 A), No. 8 (20 A), No. 12 (15 A), and No. 13 (7.5 A); the windshield wiper/washer switch, intermittent wiper relay, wiper and washer motors, and grounds G201, G301, and G401.

---

### Printed page 22-179

<a id="p1671"></a>
Source: [PDF p.1671](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1671.png).

# Wipers/Washers — Circuit Diagram (gauge assembly, 2004–2008 models)

The [source diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1671.png) continues the 2004–2008 circuit through the gauge assembly wiper/washer driving circuit, CPU, and voltage feed. It shows under-dash fuses No. 5 and No. 25 (both 7.5 A), connector cavities A9, A10, A17, A18 and B12, B16–B18, and ground G501. Use the diagram for exact wire routing.

---

### Printed page 22-180

<a id="p1672"></a>
Source: [PDF p.1672](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1672.png).

# Wipers/Washers — Intermittent Wiper Circuit Input Test (2000–2003 models)

1. Remove the gauge assembly (see p. 22-89).
2. Inspect all connectors and socket terminals. Repair bent, loose, or corroded terminals and recheck. Otherwise continue. Use the [source connector drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1672.png) for cavity orientation (wire side of female terminals).
3. Reconnect the gauge assembly.
4. Test at the connector. Correct failed inputs and recheck; if all pass, replace the faulty gauge assembly.

| Cavity | Wire | Condition | Desired result | Possible cause if result differs |
| --- | --- | --- | --- | --- |
| B4 | YEL | Ignition ON (II) | Battery voltage to ground | Under-dash fuse No. 5 (7.5 A) blown; open wire |
| B5 | WHT/RED | All conditions | Battery voltage to ground | Main under-hood fuse No. 54 (30 A) or under-dash fuse No. 25 (7.5 A) blown; open wire |
| B8 and B9 | BLK | All conditions | Less than 0.5 V to ground | Poor ground G501; open wire |
| B11 | GRN | Ignition ON (II) | Battery voltage to ground | Under-dash fuse No. 8 (20 A) blown; intermittent wiper relay faulty; open wire |
| C11 | BLU/ORN | Ignition ON (II), wiper switch OFF (parked) | Battery voltage to ground | Under-dash fuse No. 13 (7.5 A) blown; wiper motor faulty; open wire |
| C12 | BLU/BLK | Ignition ON (II), wiper switch INT | Battery voltage to ground | Under-dash fuse No. 12 (15 A) blown; wiper switch faulty; open wire |
| C13 | WHT/BLK | Ignition ON (II), washer switch ON | Battery voltage to ground | Under-dash fuse No. 12 (15 A) blown; washer switch faulty; open wire |

---

### Printed page 22-181

<a id="p1673"></a>
Source: [PDF p.1673](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1673.png).

# Wipers/Washers — Intermittent Wiper Circuit Input Test (2004–2008 models)

1. Remove the gauge assembly (see p. 22-89).
2. Inspect all connectors and socket terminals. Repair bent, loose, or corroded terminals and recheck. Otherwise continue. Use the [source connector drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1673.png) for cavity orientation (wire side of female terminals).
3. Reconnect the gauge assembly.
4. Test at the connector. Correct failed inputs and recheck; if all pass, replace the faulty gauge assembly.

| Cavity | Wire | Condition | Desired result | Possible cause if result differs |
| --- | --- | --- | --- | --- |
| A9 | YEL | Ignition ON (II) | Battery voltage to ground | Under-dash fuse No. 5 (7.5 A) blown; open wire |
| A10 | WHT/RED | All conditions | Battery voltage to ground | Main under-hood fuse No. 54 (30 A) or under-dash fuse No. 25 (7.5 A) blown; open wire |
| A17 and A18 | BLK | All conditions | Less than 0.5 V to ground | Poor ground G501; open wire |
| B12 | GRN | Ignition ON (II) | Battery voltage to ground | Under-dash fuse No. 8 (20 A) blown; intermittent wiper relay faulty; open wire |
| B16 | BLU/ORN | Ignition ON (II), wiper switch OFF (parked) | Battery voltage to ground | Under-dash fuse No. 13 (7.5 A) blown; wiper motor faulty; open wire |
| B17 | BLU/BLK | Ignition ON (II), wiper switch INT | Battery voltage to ground | Under-dash fuse No. 12 (15 A) blown; wiper switch faulty; open wire |
| B18 | WHT/BLK | Ignition ON (II), washer switch ON | Battery voltage to ground | Under-dash fuse No. 12 (15 A) blown; washer switch faulty; open wire |

---

### Printed page 22-182

<a id="p1674"></a>
Source: [PDF p.1674](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1674.png).

# Wiper/Washer Switch Test/Replacement

1. Lower the steering column and remove its covers (see p. 17-9).
2. Disconnect the 14P connector from the wiper/washer switch.
3. Remove two screws and pull out the switch.
4. Check continuity in each switch position. Replace the switch if it differs from the [source continuity table](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1674.png): OFF joins 12–11; INT joins 14–13 and 12–11; LO joins 4–11; HI and MIST ON join 5–4; washer ON joins 6–14. Use the source drawing to identify connector cavities.

---

### Printed page 22-183

<a id="p1675"></a>
Source: [PDF p.1675](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1675.png).

# Wiper Motor Test

1. Open the hood; remove wiper arm cap nuts and arms (see p. 22-185).
2. Remove the hood seal and cowl cover (p. 22-185).
3. Disconnect the wiper motor 5P connector.
4. Apply battery power (+) to terminal No. 4. For low speed ground terminal No. 2; for high speed ground terminal No. 1. Replace the motor if it fails to run smoothly. See the [source terminal drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1675.png).
5. Power No. 4 and ground No. 2 and No. 3. Connect an analog voltmeter between No. 4 (+) and No. 5 (−). The pointer should swing when the park switch contacts; otherwise replace the motor.

## Washer Motor Test

1. Remove the right inner fender (p. 20-126).
2. Disconnect the washer motor 2P connector.
3. Apply battery power to terminal No. 1 and ground to No. 2.
4. Replace the motor if it does not run smoothly.

---

### Printed page 22-184

<a id="p1676"></a>
Source: [PDF p.1676](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1676.png).

# Washer Reservoir Replacement

1. Pull away the right inner fender (p. 20-126).
2. Disconnect the washer tube and washer motor 2P connector.
3. Remove bolts; separate and remove the filler neck from the reservoir. The diagram specifies 6 × 1.0 mm fasteners at **9.8 N·m (1.0 kgf·m, 7.2 lbf·ft)** for both USA and Canada models.
4. Remove the reservoir.
5. Install in reverse order and check washer motor operation. See the [source illustrations](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1676.png) for the two model layouts.

Reservoir capacity: USA **2.5 L (2.6 US qt)**; Canada **6.0 L (6.3 US qt)**.

---

### Printed page 22-185

<a id="p1677"></a>
Source: [PDF p.1677](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1677.png).

# Wiper Motor Replacement

1. Open the hood; remove the cap nuts and wiper arms. Arm nut torque on installation: **18 N·m (1.8 kgf·m, 13 lbf·ft)** for 10 × 1.25 mm fasteners.
2. Remove the hood seal and cowl cover.
3. Disconnect the 5P connector from the wiper motor.
4. Remove the bolts and windshield wiper linkage assembly. Illustrated 6 × 1.0 mm linkage fasteners: **9.8 N·m (1.0 kgf·m, 7.2 lbf·ft)**.
5. Remove the three mounting bolts and nut joining the motor to the linkage. The [source illustration](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1677.png) gives **8 N·m (0.8 kgf·m, 6 lbf·ft)** for 6 × 1.0 mm bolts and **15 N·m (1.5 kgf·m, 11 lbf·ft)** for the 8 × 1.25 mm nut.
6. Reinstall in reverse order. Grease moving parts; turn the switch ON then OFF to park the shafts before replacing the arms; replace damaged clips; check motor operation.

---

### Printed page 22-186

<a id="p1678"></a>
Source: [PDF p.1678](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1678.png).

# Washer Tube Replacement

1. Remove the front bumper and right inner fender (see p. 20-126).
2. Remove the washer nozzles and clips, then remove the tube.
3. Reinstall in reverse order without pinching the tube; check windshield washer operation.

---

### Printed page 22-187

<a id="p1679"></a>
Source: [PDF p.1679](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1679.png).

# Immobilizer System — Component Location Index

The [source location drawing](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1679.png) identifies the gauge immobilizer indicator (bulb locations pp. 22-56–59 by model year), ECM, immobilizer receiver unit (2000–2005; troubleshooting p. 22-194), immobilizer control unit-receiver (2006–2008; troubleshooting 2006–2007 p. 22-200, 2008 p. 22-206), IMOES unit (2008; input test/replacement p. 22-215), and transponder in the master/valet ignition keys. Receiver replacement is p. 22-217.

---

### Printed page 22-188

<a id="p1680"></a>
Source: [PDF p.1680](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1680.png).

# Immobilizer System — System Description (2000–2005 models)

The **type II** immobilizer disables the vehicle unless a recognized ignition key is used. It consists of a key transponder, immobilizer receiver unit, indicator, and ECM. The black master key operates ignition, doors, trunk, and center console; the gray valet key operates ignition and doors.

At ignition ON (II), the receiver powers the key transponder. The transponder sends a coded signal through the receiver to the ECM. The system stores up to six key codes.

For an ECM rewrite, the dealer needs the vehicle, all master and valet keys, and current HDS software. A key not learned during the rewrite will no longer start the engine, except T5 keys duplicated with the Ilco Code Key Duplicator. One new key may be added without reprogramming all keys by following the HDS IMMOBI menu.

---

### Printed page 22-189

<a id="p1681"></a>
Source: [PDF p.1681](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1681.png).

# Immobilizer System — Indicator and Parts (2000–2005 models)

A recognized key makes the indicator light for about 2 seconds, then go out. After ignition OFF it blinks about 5 seconds and goes out. An unrecognized key or code makes it light about 2 seconds then blink until ignition OFF. Metal objects, key fobs, other immobilizer keys, and transponders can interfere; remove the key from the key ring when investigating an intermittent problem.

| Problem | Part set | HDS required? |
| --- | --- | --- |
| Lost master/valet key or additional key needed | Blank key | Yes* |
| All master and valet keys lost | Two or three blank keys | Yes |
| Immobilizer receiver unit faulty | Immobilizer receiver unit | No |
| ECM faulty | ECM | Yes |
| Ignition switch faulty | Ignition switch; master and valet keys; rekey all lock cylinders | Yes |
| Door key cylinder broken | Door key cylinder; rekey that cylinder | No |

\* Duplicate keys can be made with the Ilco Code Key Duplicator. See the [source table](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1681.png).

---

### Printed page 22-190

<a id="p1682"></a>
Source: [PDF p.1682](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1682.png).

# Immobilizer System — System Description (2006–2008 models)

The type IV immobilizer requires a programmed ignition key. It includes the key transponder, immobilizer control unit-receiver, indicator, ECM, and on the 2008 model the IMOES unit.

For 2006–2007, at ignition ON (II) the receiver powers the transponder, which returns a rolling code embedded in the receiver rather than the ECM. An HDS handshake is required for ECM repair/replacement; all keys are required for control unit-receiver repair/replacement.

For 2008, the receiver sends the code to the IMOES unit, which confirms it and signals the ECM to supply the fuel pump circuit. HDS communication agreement is required after ECM or IMOES replacement. When replacing the control unit-receiver, register every key to the new unit with HDS; unregistered keys will not start the vehicle.

---

### Printed page 22-191

<a id="p1683"></a>
Source: [PDF p.1683](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1683.png).

# Immobilizer System — Indicator Blinking Pattern (2006–2008 models)

With a programmed key, the indicator lights for about **2 seconds** after ignition ON (II), then goes out. Following ignition OFF, it blinks at about **1 Hz for 5 seconds** and goes out. With an unrecognized key/code it lights for about **2 seconds**, then blinks at about **1 Hz until ignition OFF**. See the [source timing diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1683.png).

---

### Printed page 22-192

<a id="p1684"></a>
Source: [PDF p.1684](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1684.png).

# Immobilizer System — Circuit Diagram (2000–2005 models)

Use the [source circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1684.png) for exact wire paths, connector cavities, fuses, relay contacts, and grounds. It shows main under-hood fuses No. 41 (100 A), No. 54 (30 A), No. 46 (15 A); under-dash fuse No. 25 (7.5 A); PGM-FI main relay, fuel pump, immobilizer receiver and indicator (1.12 W), ECM, and grounds G101 and G601. `*1` denotes 2004–2005; `*2` denotes 2000–2003.

---

### Printed page 22-193

<a id="p1685"></a>
Source: [PDF p.1685](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1685.png).

# Immobilizer System — Circuit Diagram (2006–2008 models)

Use the [source circuit diagram](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1685.png) for exact wire paths and connector cavities. It shows the battery through main under-hood fuses No. 41 (100 A), No. 54 (30 A), and No. 42 (40 A); under-dash fuses No. 2 (15 A) and No. 25 (7.5 A); immobilizer control unit-receiver, ECM, gauge indicator (1.12 W), keyless door lock control unit, data link connector, ignition key and parking brake switches, and the **2008-only IMOES unit**. Ground identifiers include G401 and G101.
