# HVAC (Heating, Ventilation, and Air Conditioning)

Honda S2000 service manual, PDF pp. 1409–1491 (printed section 21). Covers heating and air conditioning components, diagnostic procedures, refrigerant service, and A/C performance tests.

---

### Printed page 21-1

<a id="p1409"></a>
Source: [PDF p.1409](../page-images/p1409.png).

# HVAC (Heating, Ventilation, and Air Conditioning)

## Contents

- Special Tools 21-2

### Heating

- Component Location Index 21-3
- General Troubleshooting Information 21-4
- DTC Troubleshooting Index 21-6
- Symptom Troubleshooting Index 21-7
- System Description 21-8
- Circuit Diagram 21-9
- DTC Troubleshooting 21-10
- Recirculation Control Motor Circuit Troubleshooting 21-16
- Heater Control Power and Ground Circuit Troubleshooting 21-18
- Power Transistor Test 21-19
- Air Mix Control Motor Test 21-20
- Air Mix Control Motor Replacement 21-20
- Mode Control Motor Test 21-21
- Mode Control Motor Replacement 21-21
- Recirculation Control Motor Test 21-22
- Recirculation Control Motor Replacement 21-22
- Heater Control Panel Removal/Installation 21-23
- Blower Unit Removal/Installation 21-23
- Blower Unit Component Replacement 21-24
- Heater Unit/Core Replacement 21-24
- Dust and Pollen Filter Replacement 21-27
- Heater Valve Cable Adjustment 21-27

### Heating/Air Conditioning

- Component Location Index 21-29
- A/C Service Tips and Precautions 21-32
- A/C System Inspection 21-32
- A/C Refrigerant Oil Replacement 21-33
- A/C Line Replacement 21-34
- General Troubleshooting Information 21-35
- DTC Troubleshooting Index 21-36
- Symptom Troubleshooting Index 21-37
- System Description 21-38
- Circuit Diagram 21-40
- DTC Troubleshooting 21-42
- Recirculation Control Motor Circuit Troubleshooting 21-50
- HVAC Control Power and Ground Circuit Troubleshooting 21-51
- A/C Condenser Fan Circuit Troubleshooting 21-53
- Radiator and A/C Condenser Fan Common Circuit Troubleshooting 21-54
- A/C Compressor Clutch Circuit Troubleshooting 21-55
- A/C Pressure Switch Circuit Troubleshooting 21-58
- Evaporator Temperature Sensor Test 21-60
- HVAC Control Unit Removal/Installation 21-60
- Blower/Evaporator Unit Removal/Installation 21-61
- Blower/Evaporator Unit Component Replacement 21-62
- Expansion Valve Replacement 21-63
- Heater Unit/Core Replacement 21-63
- A/C Compressor Replacement 21-66
- A/C Compressor Clutch Check 21-68
- A/C Compressor Clutch Overhaul 21-69
- A/C Compressor Thermal Protector Replacement 21-71
- A/C Compressor Relief Valve Replacement 21-71
- A/C Condenser Replacement 21-72
- Refrigerant Recovery 21-73
- System Evacuation 21-74
- System Charging 21-75
- Refrigerant Leak Test 21-76
- A/C System Test 21-77

### Printed page 21-2

<a id="p1410"></a>
Source: [PDF p.1410](../page-images/p1410.png).

# Special Tools

| Ref. | Tool number | Description | Qty |
|---|---|---|---:|
| ① | 07SAZ-001000A | Backprobe Set | 2 |

### Printed page 21-3

<a id="p1411"></a>
Source: [PDF p.1411](../page-images/p1411.png).

# Heating Component Location Index (2008 model)

The under-hood fuse/relay box contains the blower motor relay. See its test on printed p. 22-48. Refer to the [source diagram](../page-images/p1411.png) for component position.

### Printed page 21-4

<a id="p1412"></a>
Source: [PDF p.1412](../page-images/p1412.png).

# Heating
## Component Location Index (cont'd)

### '08 model

| Component | Action | Page Reference |
| :--- | :--- | :--- |
|DUSTAND P O L L E N FILTER | Replacement | page 21-27 |
|HEATERVALVECABLE | Adjustment | page 21-27 |
|BLOWERUNIT | Removal/Installation | page 21-23 |
|BLOWERUNIT C O M P O N E N T | Replacement | page 21-24 |
| RECIRCULATION CONTROL MOTOR | Test | page 21-22 |
| RECIRCULATION CONTROL MOTOR | Replacement | page 21-22 |
|POWERTRANSISTOR | Test | page 21-19 |
|MODECONTROLMOTOR | Test | page 21-21 |
|MODECONTROLMOTOR | Replacement | page 21-21 |
| AIR MIX CONTROL MOTOR | Test | page 21-20 |
| AIR MIX CONTROL MOTOR | Replacement | page 21-20 |
|HEATERCONTROLPANEL | Removal/Installation | page 21-23 |

### Printed page 21-5

<a id="p1413"></a>
Source: [PDF p.1413](../page-images/p1413.png).

# General Troubleshooting Information

## How to Retrieve a DTC

The heater control panel has a self-diagnostic function. To run the self-diagnostic function, do the following:

1. Set the mode control dial on the Vent position.
2. Turn the ignition switch to ON (II).
3. Within 5 seconds after turning the ignition switch on, press the recirculation control switch the required number of times depending on the recirculation indicator status:
   - if the indicator is ON, press the recirculation control switch 5 times.
   - If the indicator is OFF, press the recirculation control switch 6 times.

The recirculation indicator will come on for 2 seconds, then blink the Diagnostic Trouble Code (DTC) to indicate a faulty component. If no DTCs are found, the indicator will not blink after the initial 2 seconds light.

### RECIRCULATION INDICATOR LIGHT

#### Example of DTC Indication Pattern (DTC 2)

The source timing diagram shows an initial 2-second indication and a DTC 2 blink pattern labeled 0.3-second and 1.5-second intervals. See the [source timing diagram](../page-images/p1413.png) for the pulse sequence.

#### Canceling the Self-diagnosis Function

4. Turn the ignition switch to LOCK (0) to cancel the self-diagnostic function. After completing repair work, run the self-diagnostic function again to make sure that there are no other malfunctions.

### Printed page 21-6

<a id="p1414"></a>
Source: [PDF p.1414](../page-images/p1414.png).

# Heating
## DTC Troubleshooting Index

### Recirculation Indicator Blinks

| DTC | Detection Item | Page |
| :--- | :--- | :--- |
| 1 | A problem in the air mix control motor circuit (see page 21-10) | 21-10 |
| 2 | A problem in the mode control motor circuit (see page 21-11) | 21-11 |
| 3 | A problem in the blower motor circuit (see page 21-13) | 21-13 |

* In case of multiple problems, the recirculation indicator will indicate only the DTC with the least number of blinks.
* In case of an intermittent failure, the heater control panel will store the DTC until the ignition switch is in LOCK (0).

### Printed page 21-7

<a id="p1415"></a>
Source: [PDF p.1415](../page-images/p1415.png).

# Symptom Troubleshooting Index

For electrical malfunctions which are indicated by the self-diagnostic system, refer to self-diagnostic function (see page 21-5).

## Recirculation control doors do not change between Fresh and Recirculate
**Recirculation Control Motor Circuit Troubleshooting** (see page 21-16)
*   Blown No. 20 (7.5 A) fuse in the under-dash fuse/relay box
*   Cleanliness and tightness of all connectors

## Blower and heater controls do not work
**Heater Control Power and Ground Circuit Troubleshooting** (see page 21-18)
*   Blown No. 56 (40 A) fuse in the main under-hood fuse/relay box, and No. 20 (7.5 A) fuse in the under-dash fuse/relay box
*   Poor ground at No. G201, G402
*   Cleanliness and tightness of all connectors

## Insufficient heating
1. Check the coolant level (see page 10-9)
2. Check the radiator cap (see page 10-6)
3. Check the coolant temperature
4. Check the operation of the air mix control motor and door (see page 21-20)
5. Check the operation of the heater valve (see page 21-27)
6. Check the blower motor for obstructions
7. Check for air leaks around the ducts and vents
8. Check the inlet heater hose temperature
*   If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, and a damaged or leaking water pump.
*   If it is HOT, check for restrictions in the heater core.
Back flush the heater core using standard commercially available equipment, or replace the heater core.

* Also check for a damaged cylinder head gasket.

### Printed page 21-8

<a id="p1416"></a>
Source: [PDF p.1416](../page-images/p1416.png).

# Heating
## System Description
### Heater control panel 30P connector

Wire side of female terminals

| Cavity | Wire color | Signal |
| :---: | :--- | :--- |
| 1 | PNK | AIR MIX COOL OUTPUT |
| 2 | PNK/BLU | AIR MIX HOT OUTPUT |
| 3 | YEL/BLU | MODE DEF OUTPUT |
| 4 | YEL/RED | MODE VENT OUTPUT |
| 5 | GRY | AIR MIX POTENTIAL + 5 V OUTPUT |
| 6 | PNK/BLK | AIR MIX POTENTIAL OUTPUT |
| 8 | YEL/GRN | MODE 2 OUTPUT |
| 9 | BRN/WHT | MODE 1 OUTPUT |
| 10 | LT GRN | SENSOR COMMON GROUND INPUT |
| 11 | BLU/RED | BLOWER FEEDBACK INPUT |
| 13 | BLU/YEL | POWER TRANSISTOR BASE OUTPUT |
| 15 | GRN/WHT | FRESH INPUT |
| 16 | GRN/YEL | RECIRCULATE INPUT |
| 21 | YEL | MODE 4 OUTPUT |
| 22 | BLK/WHT | MODE 3 OUTPUT |
| 23 | BLK/WHT | GAUGE ASSEMBLY OUTPUT |
| 26 | BLK | GROUND INPUT |
| 27 | RED | GAUGE ASSEMBLY OUTPUT |
| 28 | RED/BLK | TAILLIGHTS RELAY INPUT |
| 29 | WHT/RED | + B (Power) INPUT |
| 30 | BLK/YEL | IG2(Power) INPUT |

### Printed page 21-9

<a id="p1417"></a>
Source: [PDF p.1417](../page-images/p1417.png).

# Heating Circuit Diagram

The [source wiring diagram](../page-images/p1417.png) shows main under-hood fuses No. 41 (100 A), No. 42 (40 A), No. 54 (30 A), and No. 56 (40 A); under-dash fuses No. 25 and No. 20 (both 7.5 A); the blower motor relay, blower motor, power transistor, heater control panel 30P connector, air mix/mode/recirculation motors, grounds G201/G402, and ignition IG2 cut relay. Use the source image for circuit paths and wire colors.

### Printed page 21-10

<a id="p1418"></a>
Source: [PDF p.1418](../page-images/p1418.png).

# Heating
## DTC Troubleshooting
### DTC 1: A Problem in the Air Mix Control Motor Circuit

1. Disconnect the air mix control motor 7P connector.
2. Test the air mix control motor (see page 21-20).
   - Is the air mix control motor OK?
     - **YES** — Go to step 3.
     - **NO** — Go to step 7.

3. Disconnect the heater control panel 30P connector.
4. Check for continuity between body ground and the heater control panel 30P connector No. 1, 2, 5, 6, and 10 terminals individually.

**Is there continuity?**
- **YES** — Repair short to body ground in the wire(s) between the heater control panel and the air mix control motor.
- **NO** — Go to step 5.

5. Turn the ignition switch to ON (II), and measure the same terminals for voltage.

**Is there any voltage?**
- **YES** — Repair short to power in the wire(s) between the heater control panel and the air mix control motor. This short may also damage the heater control panel. Repair the short to power before replacing the heater control panel.
- **NO** — Go to step 6.

### Printed page 21-11

<a id="p1419"></a>
Source: [PDF p.1419](../page-images/p1419.png).

# DTC 1: Air Mix Control Motor Circuit (continued)

6. Turn ignition to LOCK (0). Check continuity from heater control panel 30P to air mix motor 7P:

| 30P terminal | 7P terminal |
|---:|---:|
| 1 | 2 |
| 2 | 1 |
| 5 | 5 |
| 6 | 3 |
| 10 | 7 |

If continuity is present, check both connectors for loose wires or poor connections. If sound, substitute a known-good heater control panel and recheck; replace the original panel if the symptom disappears. If continuity is absent, repair the open wire(s).

7. Remove the air mix control motor (p. 21-20).
8. Check the linkage and doors for smooth movement. If smooth, replace the motor; if they stick or bind, repair the linkage or doors.

# DTC 2: Mode Control Motor Circuit

1. Disconnect the mode control motor 7P connector.
2. Test the motor (p. 21-21). If good, continue to step 3; if faulty, go to step 7.
3. Disconnect the heater control panel 30P connector.
4. Check continuity from body ground to 30P terminals 3, 4, 8, 9, 10, 21, and 22 individually. If any has continuity, repair the short to body ground between the panel and mode motor. Otherwise continue to step 5.

### Printed page 21-12

<a id="p1420"></a>
Source: [PDF p.1420](../page-images/p1420.png).

# DTC 2: Mode Control Motor Circuit (continued)

5. Turn ignition to ON (II) and measure voltage at the same 30P terminals (3, 4, 8, 9, 10, 21, 22). If voltage is present, repair the short to power between the panel and mode motor **before** replacing the panel; the short may damage the panel. If absent, continue to step 6.
6. Turn ignition to LOCK (0). Check continuity from heater control panel 30P to mode motor 7P:

| 30P terminal | 7P terminal |
|---:|---:|
| 3 | 2 |
| 4 | 1 |
| 8 | 5 |
| 9 | 6 |
| 10 | 7 |
| 21 | 3 |
| 22 | 4 |

If continuity is present, check both connectors for loose wires or poor connections. If sound, substitute a known-good heater control panel and recheck; replace the original panel if the symptom disappears. If continuity is absent, repair the open wire(s).

### Printed page 21-13

<a id="p1421"></a>
Source: [PDF p.1421](../page-images/p1421.png).

# DTC 2: Mode Control Motor Circuit (continued)

7. Remove the mode control motor (p. 21-21).
8. Check the mode control linkage and doors for smooth movement. If smooth, replace the mode motor. If they stick or bind, repair the linkage or doors.

# DTC 3: Blower Motor Circuit

## Step 1
1. Check the No. 56(40 A) fuse in the main under-hood fuse/relay box, and the No. 20 (7.5 A) fuse in the under-dash fuse/relay box.

   Are the fuses OK?
   - **YES** — Go to step 2.
   - **NO** — Replace the fuse(s), and recheck.

## Step 2
2. Connect the No. 2 terminal of the blower motor 2P connector to body ground with a jumper wire.

   > **BLOWER MOTOR 2P CONNECTOR**
   > **JUMPER WIRE**
   > **BLU/BLK** (Wire side of female terminals)

## Step 3
3. Turn the ignition switch to ON (II).

   Does the blower motor run?
   - **YES** — Go to step 4.
   - **NO** — Go to step 17.

## Step 4
4. Turn the ignition switch to LOCK (0).
5. Disconnect the jumper wire.
6. Disconnect the power transistor 5P connector.

### Printed page 21-14

<a id="p1422"></a>
Source: [PDF p.1422](../page-images/p1422.png).

# DTC 3: Blower Motor Circuit (continued)

7. Check continuity between power transistor 5P terminal 5 and body ground. **YES:** go to step 8. **NO:** check for an open wire to ground; if sound, check ground G402.
8. Jumper power transistor 5P terminals 4 and 5.
9. Turn ignition to ON (II). If blower runs at high speed, continue to step 10. If not, repair the open wire between power transistor and blower motor.
10. Turn ignition to LOCK (0).
11. Disconnect the jumper.
12. Disconnect heater control panel 30P connector.
13. Check continuity from panel 30P terminals 11 and 13 individually to body ground. If continuity is present, repair the short to ground between panel and power transistor. If absent, continue to step 14.
14. Check continuity **30P 11 → power transistor 5P 1** and **30P 13 → 5P 3**. If both paths have continuity, continue to step 15. Otherwise repair the open wire(s).

### Printed page 21-15

<a id="p1423"></a>
Source: [PDF p.1423](../page-images/p1423.png).

# DTC 3: Blower Motor Circuit (continued)

## Step 15
Reconnect the heater control panel 30P connector.

## Step 16
Test the power transistor (see page 21-19).

**Is the power transistor OK?**

*   **YES**—Check for loose wires or poor connections at the heater control panel 30P connector, blower motor 2P connector and at the power transistor 5P connector. If the connections are good, substitute a known-good heater control panel, and recheck. If the symptom/indication goes away, replace the original heater control panel.
*   **NO**—Replace the power transistor.

## Step 17
Turn the ignition switch to LOCK (0).

## Step 18
Disconnect the jumper wire.

## Step 19
Disconnect the blower motor 2P connector.

## Step 20
Measure the voltage between the No. 1 terminal of the blower motor 2P connector and body ground.

**BLOWER MOTOR 2P CONNECTOR**
*   **BLU/WHT**: Wire side of female terminals

**Is there battery voltage?**

*   **YES**—Replace the blower motor.
*   **NO**—Go to step 21.

## Step 21
Turn the ignition switch to LOCK (0).

## Step 22
Remove the blower motor relay from the main under-hood fuse/relay box, and test it (see page 22-48).

**Is the relay OK?**

*   **YES**—Go to step 23.
*   **NO**—Replace the blower motor relay.

## Step 23
Measure the voltage between the No. 4 terminal of the blower motor relay 4P socket and body ground.

**BLOWER MOTOR RELAY 4P SOCKET**

**Is there battery voltage?**

*   **YES**—Go to step 24.
*   **NO**—Replace the main under-hood fuse/relay box.

## Step 24
Turn the ignition switch to ON (II).

## Step 25
Measure the voltage between the No. 1 terminal of the blower motor relay 4P socket and body ground.

**BLOWER MOTOR RELAY 4P SOCKET**
*   **BLK/YEL**: Wire side of female terminals

**Is there battery voltage?**

*   **YES**—Go to step 26.
*   **NO**—Repair open in the wire between the No. 20 (7.5 A) fuse in the under-dash fuse/relay box and the blower motor relay.

### Printed page 21-16

<a id="p1424"></a>
Source: [PDF p.1424](../page-images/p1424.png).

# Heating
## DTC Troubleshooting (cont'd)

**26.** Turn the ignition switch to LOCK (0).

**27.** Check for continuity between the No. 2 terminal of the blower motor relay 4P socket and body ground.

Is there continuity?

*   **YES**—Repair open in the BLU/WHT wire between the blower motor relay and the blower motor.
*   **NO**—Check for an open in the wire between the blower motor relay and body ground. If the wire is OK, check for poor ground at G201.

---

## Recirculation Control Motor Circuit Troubleshooting

**1.** Check the No. 20 (7.5 A) fuse in the under-dash fuse/relay box.

Is the fuse OK?

*   **YES**—Go to step 2.
*   **NO**—Replace the fuse, and recheck.

**2.** Disconnect the recirculation control motor 7P connector.

**3.** Turn the ignition switch to ON (II).

**4.** Measure the voltage between the No. 1 terminal of the recirculation control motor 7P connector and body ground.

Is there battery voltage?

*   **YES**—Go to step 5.
*   **NO**—Repair open in the wire between the No. 20 (7.5 A) fuse in the under-dash fuse/relay box and the recirculation control motor.

**5.** Turn the ignition switch to LOCK (0).

**6.** Test the recirculation control motor (see page 21-22).

Is the recirculation control motor OK?

*   **YES**—Go to step 7.
*   **NO**—Go to step 11.

**7.** Disconnect the heater control panel 30P connector.

### Printed page 21-17

<a id="p1425"></a>
Source: [PDF p.1425](../page-images/p1425.png).

# Recirculation Control Motor Circuit Troubleshooting (continued)

8. Check continuity between heater control panel 30P terminals 15 and 16 and body ground individually. **YES:** repair the short to body ground between panel and recirculation motor. **NO:** continue to step 9.
9. Turn ignition to ON (II), then measure voltage at the same terminals. **YES:** repair the short to power before replacing the panel; the short may damage it. **NO:** continue to step 10.
10. Turn ignition to LOCK (0), then check continuity **30P 15 → recirculation motor 7P 5** and **30P 16 → 7P 7**. **YES:** check both connectors, substitute a known-good heater control panel if connections are sound, and replace the original panel if the symptom disappears. **NO:** repair the open wire(s).
11. Remove the recirculation control motor (p. 21-22).
12. Check the linkage and doors. If they move smoothly, replace the motor. If they stick or bind, repair the linkage or doors.

### Printed page 21-18

<a id="p1426"></a>
Source: [PDF p.1426](../page-images/p1426.png).

# Heating
## Heater Control Power and Ground Circuit Troubleshooting

1. Check the No. 54 (30 A) fuse in the main under-hood fuse/relay box, and the No. 20 (7.5 A) and No. 25 (7.5 A) fuses in the under-dash fuse/relay box.

Are the fuses OK?
- **YES** — Go to step 2.
- **NO**—Replace the fuse(s), and recheck.

2. Disconnect the heater control panel 30P connector.

3. Turn the ignition switch to ON (II).

4. Measure the voltage between the No. 30 terminal of the heater control panel 30P connector and body ground.

**HEATER CONTROL PANEL 30P CONNECTOR**
Is there battery voltage ?
- **YES** — Go to step 5.
- **NO**—Repair open in the wire between the No. 20 (7.5 A) fuse in the under-dash fuse/relay box and the heater control panel.

5. Turn the ignition switch to LOCK (0).

6. Measure the voltage between the No. 29 terminal of the heater control panel 30P connector and body ground.

**HEATER CONTROL PANEL 30P CONNECTOR**
Is there battery voltage?
- **YES** — Go t o step 7.
- **NO**—Repair open in the wire between the No. 25 (7.5 A) fuse in the under-dash fuse/relay box and the heater control panel.

7. Check for continuity between the No. 26 terminal of the heater control panel 30P connector and body ground.

**HEATER CONTROL PANEL 30P CONNECTOR**
Is there continuity?
- **YES**—Check for loose wires or poor connections at the heater control panel 30P connector. If the connections are good, substitute a known-good heater control panel, and recheck. If the symptom indication goes away, replace the original heater control panel.
- **NO**—Check for an open in the wire between the heater control panel and body ground. If the wire is OK, check for poor ground at G402.

### Printed page 21-19

<a id="p1427"></a>
Source: [PDF p.1427](../page-images/p1427.png).

# Power Transistor Test

## Procedure
1. Disconnect the 5P connector from the power transistor.
2. Measure the resistance between the No. 1 and No. 4 terminals of the power transistor. It should be about **1.4—1.5 kΩ**.
   - If the resistance is within the specifications, go to step 3.
   - If the resistance is not within the specifications, replace the power transistor.

## Steps Continued
3. Carefully release the lock tab on the No. 3 terminal (BLU/YEL) (A) in the 5P connector, then remove the terminal and insulate it from body ground.
4. Reconnect the 5P connector to the power transistor.
5. Supply 12 V to the No. 3 cavity with a jumper wire.
6. Turn the ignition switch to ON (II), and check that the blower motor runs.
   - If the blower motor does not run, replace the power transistor.
     - **NOTE:** A faulty blower motor can cause the power transistor to fail. If the power transistor is replaced, also check the blower motor for binding, and replace it if necessary.
   - If the blower motor runs, the power transistor is OK.

## Safety Note
- Also check the blower motor. Power transistor failure can be caused by a defective blower motor.

### Printed page 21-20

<a id="p1428"></a>
Source: [PDF p.1428](../page-images/p1428.png).

# Heating
## Air Mix Control Motor Test

1. Disconnect the 7P connector from the air mix control motor.

**NOTICE:**
Incorrectly applying power and ground to the air mix control motor will damage it. Follow the instructions carefully.

2. Connect battery power to the No. 1 terminal of the air mix control motor, and ground the No. 2 terminal; the air mix control motor should run, and stop at Max Hot. If it doesn't, reverse the connections; the air mix control motor should run, and stop at Max Cool.

3. If the air mix control motor does not run in step 2, remove it, then check the air mix control linkage and doors for smooth movement.
*   If the linkage and doors move smoothly, replace the air mix control motor.
*   If the linkage or doors stick or bind, repair them as needed.
*   If the air mix control motor runs smoothly, go to step 4.



4. Measure the resistance between the No. 5 and No. 7 terminals. It should be between 4.2 to 7.8 kΩ.

5. Reconnect the air mix control motor 7P connector, then turn the ignition switch to ON (II).

6. Using the backprobe set, measure the voltage between the No. 3 and No. 7 terminals.
*   Max Cool: about 1 V
*   Max Hot: about 4 V

7. If either the resistance or voltage reading are not as specified, replace the air mix control motor.

---
## Air Mix Control Motor Replacement

1. Remove the audio unit (see page 22-288).

2. Remove the passenger's dashboard lower cover (see page 20-86).

3. Disconnect the 7P connector (A) from the air mix control motor (B). Remove the self-tapping screws and the air mix control motor from the heater unit.

4. Install the motor in the reverse order of removal. Make sure the pin on the motor is properly engaged with the linkage. After installation, make sure the motor runs smoothly.

### Printed page 21-21

<a id="p1429"></a>
Source: [PDF p.1429](../page-images/p1429.png).

# Mode Control Motor Test

## Step 1: Disconnect Connector
Disconnect the 7P connector from the mode control motor.

> **NOTICE:** Incorrectly applying power and ground to the mode control motor will damage it. Follow the instructions carefully.

## Step 2: Verify Operation
Connect battery power to the No. 1 terminal of the mode control motor, and ground the No. 2 terminal; the mode control motor should run smoothly, and stop at Vent. If it doesn't, reverse the connections; the mode control motor should run smoothly, and stop at Defrost. When the mode control motor stops running, disconnect battery power immediately.

See [source motor diagram](../page-images/p1429.png) for terminal positions.

## Step 3: Check Linkage if Motor Fails
If the motor does not run, remove it and check linkage and doors. If they move smoothly, replace the motor; if they stick or bind, repair them. If the motor runs, continue to step 4.

---

# Mode Control Motor Replacement

1. Set the mode control dial on DEF with the ignition switch to ON (II).
2. Remove the driver's heater outlet.
3. Disconnect the 7P connector (A) from the mode control motor (B). Remove the rods (C) from the mode control linkage (D). Remove the self-tapping screws and the mode control motor from the heater unit.

**Diagram Reference:** D (Linkage), A (Connector), B (Motor), C (Rods)

4. Install the motor in the reverse order of removal. Make sure the pin on the linkage is properly engaged with the motor. After installation, make sure the motor runs smoothly.


---

# Electrical Continuity Check

4. Use a digital multimeter with an output of 1 mA or less at the 20 kΩ range. With the mode control motor running as in step 2, check for continuity between the No. 7 terminal and the No. 3, 4, 5, and 6 terminals individually. There should be continuity for a moment at each terminal as the motor moves past each switch terminal.

5. If there is no continuity for a moment at each terminal, replace the mode control motor.

### Printed page 21-22

<a id="p1430"></a>
Source: [PDF p.1430](../page-images/p1430.png).

# Heating
## Recirculation Control Motor Test

1. Disconnect the 7P connector from the recirculation control motor.

**NOTICE**: Incorrectly applying power and ground to the recirculation control motor will damage it. Follow the instructions carefully.

2. Connect battery power to the No. 1 terminal of the recirculation control motor, and ground the No. 5 and No. 7 terminals; the recirculation control motor should run smoothly. To avoid damaging the recirculation control motor, do not reverse power and ground. Disconnect the No. 5 or No. 7 terminals from ground; the recirculation control motor should stop at Fresh (when the No. 7 terminal is disconnected) or Recirculate (when the No. 5 terminal is disconnected). Don't cycle the recirculation control motor for a long time.

See [source motor diagram](../page-images/p1430.png).

3. If the recirculation control motor does not run in step 2, remove it, then check the recirculation control linkage and doors for smooth movement.
*   If the linkage and doors move smoothly, replace the recirculation control motor.
*   If the linkage or doors stick or bind, repair them as needed.

## Recirculation Control Motor Replacement

1. Remove the passenger's dashboard lower cover (see page 20-86).
2. Remove the passenger's airbag (see page 23-166).
3. Remove the convertible top control unit (see page 22-242).
4. Disconnect the dashboard wire harness B connectors C201, C202, C203, and C451 (see page 22-24).
5. Disconnect the 7P connector (A) from the recirculation control motor (B). Remove the self-tapping screws and the recirculation control motor from the blower unit.
6. Install the motor in the reverse order of removal. Make sure the pin on the motor is properly engaged with the linkage. After installation, make sure the motor runs smoothly.

### Printed page 21-23

<a id="p1431"></a>
Source: [PDF p.1431](../page-images/p1431.png).

# Heater Control Panel Removal/Installation

1. Remove the instrument panel together with the heater control panel (see page 20-84).
2. Remove the self-tapping screws and the heater control panel (A) from the instrument panel (B).
3. Install the control panel in the reverse order of removal. After installation, operate the control panel controls to see whether it works properly.
4. Run the self-diagnostic function to confirm that there are no problems in the system (see page 21-5).

---

# Blower Unit Removal/Installation

1. Remove the passenger's dashboard lower cover and the right kick panel (see page 20-86).
2. Disconnect the dashboard wire harness connector from the passenger's door wire harness connector, then remove it. Remove the wire harness connectors and the convertible top control unit from the steering hanger beam.
3. Disconnect the connectors (A) from the blower motor, the power transistor and the recirculation control motor, then remove the wire harness clips (B). Remove the self-tapping screw, the mounting bolts, the mounting nuts and the blower unit (C).
4. Install in the reverse order of removal. Make sure there is no air leakage.

### Printed page 21-24

<a id="p1432"></a>
Source: [PDF p.1432](../page-images/p1432.png).

# Heating
## Blower Unit Component Replacement

**Note these items when overhauling the blower unit:**
*   The recirculation control motor (**A**), the power transistor (**B**) and the blower motor (**C**) can be replaced without removing the blower unit.
*   Before reassembly, make sure that the recirculation control doors and linkage move smoothly without binding.
*   After reassembly, make sure the recirculation control motor runs smoothly (see page 21-22).
*   Make sure that there is no air leakage.

## Heater Unit/Core Replacement

**SRS components are located in this area.** Review the **SRS component locations:**
*   '00-05 models (see page 23-11)
*   '06-08 models (see page 23-12)
*   and the precautions and procedures (see page 23-13) before doing repairs or service.

**Procedure:**
1. Make sure you have the anti-theft code for the audio system, then write down the audio preset.
2. Disconnect the negative cable from the battery.
3. Remove the heat shield of the exhaust manifold.
4. From under the hood, open the cable clamp (**A**), then disconnect the heater valve cable (**B**) from the heater valve arm (**C**). Turn the heater valve arm to the fully opened position as shown.
    *   [Diagram Label: A] (Cable Clamp)
    *   [Diagram Label: B] (Heater Valve Cable)
    *   [Diagram Label: C] (Heater Valve Arm)
5. When the engine is cool, drain the engine coolant from the radiator (see page 10-9).

### Printed page 21-25

<a id="p1433"></a>
Source: [PDF p.1433](../page-images/p1433.png).

# Page 1433 Transcription

## Section 6: Heater Valve Removal
- Remove the mounting bolt from the heater valve.
- Slide the clamps (**A**) back, then disconnect the inlet and outlet heater hoses (**B**) from the heater unit.
  - **Warning:** Engine coolant will run out when the hoses are disconnected; drain it into a clean drip pan. Be sure not to let coolant spill on the electrical parts or the painted surfaces. If any coolant spills, rinse it off immediately.

## Section 7: Heater Unit Removal
- Remove the mounting nut from the heater unit.
  - **Caution:** Take care not to damage or bend the fuel and brake lines, etc.
  - Fastener size: **8 × 1.25 mm**.
  - Torque specification: **13 N·m** (1.3 kgf·m, 9.4 lb-ft)

## Section 8: Dashboard Removal
- Remove the dashboard (see page 20-87).

## Section 9: Blower Unit Removal
- Remove the blower unit (see page 21-23).

## Section 10: Audio and Bracket Removal
- Remove the mounting bolts, the center brackets (**A**) and the audio brackets (**B**).
  - Torque specification: **9.8 N·m** (1.0 kgf·m, 7.2 lb-ft)

## Section 11: SRS Unit Removal
- Remove the SRS unit (see page 23-179).

## Section 12: Defroster Outlet and Wire Harness Removal
- Remove the self-tapping screws and the defroster outlet (**A**), then remove the wire harness clips (**B**).

### Printed page 21-26

<a id="p1434"></a>
Source: [PDF p.1434](../page-images/p1434.png).

# Heating
## Heater Unit/Core Replacement (cont'd)

**Step 13.** Disconnect the connectors (A) from the mode control motor and the air mix control motor, then remove the wire harness clip (B). Remove the mounting nuts, the mounting bolt and the heater unit (C).

*   **Torque Specification:** $6 \times 1.0 \text{ mm}$ fasteners: $9.8 \text{ N m}$ ($1.0 \text{ kgf m}$, $7.2 \text{ lbf-ft}$)

**Step 14.** Remove the self-tapping screw and the passenger's heater outlet (A), then remove the self-tapping screw and the clamp (B). Be careful not to bend the inlet and outlet pipes during the heater core (C) removal, and pull out the heater core.



**Step 15.** Install the heater core in the reverse order of removal.

**Step 16.** Install the heater unit in the reverse order of removal, and note these items:

*   Do not interchange the inlet and outlet heater hoses, and install the hose clamps securely.
*   Refill the cooling system with engine coolant (see page 10-9).
*   Adjust the heater valve cable (see page 21-27).
*   Make sure that there is no coolant leakage.
*   Make sure that there is no air leakage.
*   Enter the anti-theft code for the audio system, then enter the audio presets.

### Printed page 21-27

<a id="p1435"></a>
Source: [PDF p.1435](../page-images/p1435.png).

# Dust and Pollen Filter Replacement

1. Open the hood.
2. Remove clips (A) and hood seal (B); lift right side of cowl cover (C) and remove dust/pollen filter (D). Avoid damaging hood seal when removing clips.
3. Remove filter (A) from housing (B); replace the filter.
4. Install in reverse order.

# Heater Valve Cable Adjustment

1. Under hood, open cable clamp (A); detach heater valve cable (B) from heater valve arm (C).
2. Under dash, detach cable housing from clamp (A) and cable (B) from air mix linkage (C).
3. With both ends detached, ensure cable moves freely; replace it if binding.
4. Set temperature dial to Max Cool with ignition ON (II).
5. Attach cable to air mix linkage. Hold housing end against stop (D), then snap housing into cable clamp. See [source diagrams](../page-images/p1435.png).

### Printed page 21-28

<a id="p1436"></a>
Source: [PDF p.1436](../page-images/p1436.png).

6. From under the hood, turn the heater valve arm (A) to the fully closed position as shown, and hold it. Attach the heater valve cable (B) to the heater valve arm, and gently pull on the heater valve cable housing to take up any slack, then install the heater valve cable housing into the cable clamp (C).

### Printed page 21-29

<a id="p1437"></a>
Source: [PDF p.1437](../page-images/p1437.png).

# Heating/Air Conditioning
## Component Location Index

| Component | Description | Page Reference |
| :--- | :--- | :--- |
| DUST AND POLLEN FILTER | Replacement | page 21-27 |
| BLOWER/EVAPORATOR UNIT | Removal/Installation | page 21-61 |
| BLOWER/EVAPORATOR UNIT C O M P O N E N T | Replacement | page 21-62 |
| SERVICE VALVE (HIGH-PRESSURE SIDE) | | |
| EXPANSION VALVE | Replacement | page 21-63 |
| A/C CONDENSER | Replacement | page 21-72 |
| RECEIVER/DRYER DESICCANT | | |
| A/C COMPRESSOR | Replacement | page 21-66 |
| Clutch Check | | page 21-68 |
| Clutch Overhaul | | page 21-69 |
| Thermal Protector Check | | page 21-68 |
| Thermal Protector Replacement | | page 21-71 |
| Relief Valve Replacement | | page 21-71 |

*(cont'd)*

### Printed page 21-30

<a id="p1438"></a>
Source: [PDF p.1438](../page-images/p1438.png).

# Heating/Air Conditioning Component Location Index (continued)

The [source diagram](../page-images/p1438.png) locates the radiator fan, A/C condenser fan, A/C pressure switch, ECM, and main under-hood fuse/relay box. It identifies the blower motor relay, A/C condenser fan relay, radiator fan relay, and A/C compressor clutch relay in that box; relay tests are on printed p. 22-48.

### Printed page 21-31

<a id="p1439"></a>
Source: [PDF p.1439](../page-images/p1439.png).

# HVAC Control Unit

## Removal/Installation
**Reference:** Page 21-60

---

## Related Procedures

### Heater Unit / Core
- **Replacement:** Page 21-63

### Heater Valve Cable
- **Adjustment:** Page 21-27

### Blower / Evaporator Unit
- **Removal/Installation:** Page 21-61
- **Component Replacement:** Page 21-62

### Recirculation Control Motor
- **Test:** Page 21-22
- **Replacement:** Page 21-22

### Power Transistor
- **Test:** Page 21-19

### Air Mix Control Motor
- **Test:** Page 21-20
- **Replacement:** Page 21-20

### Evaporator Temperature Sensor
- **Test:** Page 21-60

### Mode Control Motor
- **Test:** Page 21-21
- **Replacement:** Page 21-21

---

### Printed page 21-32

<a id="p1440"></a>
Source: [PDF p.1440](../page-images/p1440.png).

# A/C Service Tips and Precautions

## WARNING
* Compressed air mixed with R-134a forms a combustible vapor.
* The vapor can burn or explode causing serious injury.
* Never use compressed air to pressure test R-134a service equipment or vehicle air conditioning systems.

## CAUTION
* Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.
* Be careful when connecting service equipment.
* Do not breathe refrigerant or vapor.

The air conditioning system uses HFC-134a (R-134a) refrigerant and polyalkyleneglycol (PAG) refrigerant oil, which are not compatible with CFC-12 (R-12) refrigerant and mineral oil. Do not use R-12 refrigerant or mineral oil in this system, and do not attempt to use R-12 servicing equipment; damage to the air conditioning system or your servicing equipment will result.

Use only service equipment that is U.L-listed and is certified to meet the requirements of SAE J2210 to remove R-134a from the air conditioning system.

If accidental system discharge occurs, ventilate the work area before resuming service.

R-134a service equipment or vehicle air conditioning systems should not be pressure tested or leak tested with compressed air.

Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

* Always disconnect the negative cable from the battery whenever replacing air conditioning parts.
* Keep moisture and dirt out of the system. When disconnecting any lines, plug or cap the fittings immediately; don't remove the caps or plugs until just before you reconnect each line.
* Before connecting any hose or line, apply a few drops of refrigerant oil to the O-ring.
* When tightening or loosening a fitting, use a second wrench to support the matching fitting.
* When discharging the system, use an R-134a refrigerant recovery/recycling/charging station; don't release refrigerant into the atmosphere.

## A/C System Inspection

Before troubleshooting any problem with the air conditioning system, do the following:

1. With the ignition switch in the LOCK (0), inspect the A/C components, pressure lines and hoses for stains that may indicate a refrigerant or a compressor oil leak.
2. Check the A/C condenser for material clogging the fins or for damage to the fins:
   * Carefully clean any material from the A/C condenser (A) fins with water and detergent.
   * Be sure to dry the A/C condenser completely.
3. Inspect the drive belt (see page 4-42).
4. Make sure no material is blocking the air flow to the A/C condenser.

### Printed page 21-33

<a id="p1441"></a>
Source: [PDF p.1441](../page-images/p1441.png).

# A/C System Inspection (continued)

5. Start engine and turn A/C on for a few minutes. Check operation at every blower setting except OFF; compressor clutch engagement (pressure plate rotates with pulley); radiator and condenser fans when clutch engages; and correct idle as A/C and clutch cycle.

# A/C Refrigerant Oil Replacement

Recommended PAG oil: **SP-10**. P/N 38897-P13-A01AH is 120 mL (4 fl oz); P/N 38899-P13-A01 is 40 mL (1⅓ fl oz). Add the following amounts when replacing parts:

| Replaced part/repair | Oil to add |
|---|---:|
| A/C condenser | 25 mL (⅚ fl oz) |
| Evaporator | 40 mL (1⅓ fl oz) |
| Line or hose | 10 mL (⅓ fl oz) |
| Receiver/dryer | 10 mL (⅓ fl oz) |
| Leakage repair | 25 mL (⅚ fl oz) |

For compressor replacement: drain the removed compressor, then drain **130 mL minus the volume recovered from the removed compressor** from the new compressor. Do not drain more than 50 mL from the new compressor, even if none was recovered from the old one. See [source oil-level diagram](../page-images/p1441.png).

Avoid contamination: never return dispensed oil to its container or mix refrigerant oils. Reseal the container immediately to prevent moisture absorption. Wash any oil off painted surfaces immediately.

### Printed page 21-34

<a id="p1442"></a>
Source: [PDF p.1442](../page-images/p1442.png).

# Page 1442: S2000 HVAC - A/C Line Replacement

## Torque Specifications

| Connection Path | Bolt Size | Torque (N-m) | Torque (kgf-m) | Torque (Ibf-ft) |
| :--- | :--- | :--- | :--- | :--- |
| Discharge hose to A/C compressor | 6 x 1.0 mm | 9.8 N-m | 1.0 kgf-m | 7.2 Ibf-ft |
| Discharge hose to A/C condenser | 6 x 1.0 mm | 9.8 N-m | 1.0 kgf-m | 7.2 Ibf-ft |
| A/C condenser line to A/C condenser | 6 x 1.0 mm | 9.8 N-m | 1.0 kgf-m | 7.2 Ibf-ft |
| A/C condenser line to receiver/dryer | 6 x 1.0 mm | 9.8 N-m | 1.0 kgf-m | 7.2 Ibf-ft |
| Receiver line A to receiver/dryer | 6 x 1.0 mm | 9.8 N-m | 1.0 kgf-m | 7.2 Ibf-ft |
| Receiver line A to receiver line B | - | 13 N·m | 1.3 kgf·m | 9.4 lbf-ft |
| Receiver line B and suction line to evaporator | 6 x 1.0 mm | 9.8 N-m | 1.0 kgf-m | 7.2 Ibf-ft |
| Suction hose to suction line | 6 x 1.0 mm | 9.8 N-m | 1.0 kgf-m | 7.2 Ibf-ft |
| Suction hose to A/C compressor | 6 x 1.0 mm | 9.8 N-m | 1.0 kgf-m | 7.2 Ibf-ft |
| A/C compressor to A/C compressor bracket | 10 x 1.25 mm | 44 N-m | 4.5 kgf-m | 33 Ibf-ft |
| A/C compressor bracket to engine block | 8 x 1.25 mm | 22 N-m | 2.2 kgf-m | 16 Ibf-ft |


See [source line diagram](../page-images/p1442.png) for numbered connection positions.

### Printed page 21-35

<a id="p1443"></a>
Source: [PDF p.1443](../page-images/p1443.png).

# Page 1443: S2000 HVAC Chapter

## General Troubleshooting Information

### How to Retrieve a DTC

The HVAC control unit has a self-diagnostic function. To run the self-diagnostic function, do the following:

1. Set the mode control dial on the Vent position.
2. Turn the ignition switch to ON (II).
3. Within 5 seconds after turning the ignition switch on, press the recirculation control switch the required number of times depending on the recirculation indicator status:
   - If the indicator is ON, press the recirculation control switch 5 times.
   - If the indicator is OFF, press the recirculation control switch 6 times.

The recirculation indicator will come on for 2 seconds, then blink the Diagnostic Trouble Code (DTC) to indicate a faulty component. If no DTCs are found, the indicator will not blink after the initial 2 seconds light.

**RECIRCULATION INDICATOR LIGHT**

#### Example of DTC Indication Pattern (DTC 2)

The [source timing diagram](../page-images/p1443.png) shows the initial 2-second indication and DTC blink intervals labeled 0.3 and 1.5 seconds.

### Canceling the Self-diagnostic Function

4. Turn the ignition switch to LOCK (0) to cancel the self-diagnostic function. After completing repair work, run the self-diagnostic function again to make sure that there are no other malfunctions.

### Printed page 21-36

<a id="p1444"></a>
Source: [PDF p.1444](../page-images/p1444.png).

# Heating/Air Conditioning
## DTC Troubleshooting Index

### DTC: Recirculation Indicator Blinks

| Detection Item | Page Reference |
| :--- | :--- |
| 1. A problem in the air mix control motor circuit | see page 21-42 |
| 2. A problem in the mode control motor circuit | see page 21-43 |
| 3. A problem in the blower motor circuit | see page 21-45 |
| 4. A problem in the evaporator temperature sensor circuit | see page 21-48 |

**Notes:**
*   In case of multiple problems, the recirculation indicator will indicate only the DTC with the least number of blinks.
*   In case of an intermittent failure, the heater control panel will store the DTC until the ignition switch to LOCK (0).

### Printed page 21-37

<a id="p1445"></a>
Source: [PDF p.1445](../page-images/p1445.png).

# Symptom Troubleshooting Index

## Recirculation control doors do not change between Fresh and Recirculate
*   **Diagnostic procedure:** Recirculation control motor circuit troubleshooting (see page 21-50)
*   **Also check for:**
    *   HVAC DTCs (see page 21-35)
    *   Blown No. 20 (7.5 A) fuse in the under-dash fuse/relay box
    *   Cleanliness and tightness of all connectors

## Blower, heater controls, and A/C do not work
*   **Diagnostic procedure:** HVAC control power and ground circuit troubleshooting (see page 21-51)
*   **Also check for:**
    *   HVAC DTCs (see page 21-35)
    *   Blown No. 54 (30 A) fuse in the main under-hood fuse/relay box, and No. 20 (7.5 A) and No. 25 (7.5 A) fuses in the under-dash fuse/relay box
    *   Poor ground at G402
    *   Cleanliness and tightness of all connectors

## The A/C condenser fan does not run at all (but radiator fan runs with the A/C on)
*   **Diagnostic procedure:** A/C condenser fan circuit troubleshooting (see page 21-53)
*   **Also check for:**
    *   HVAC DTCs (see page 21-35)
    *   Blown No. 58 (20 A) fuse in the main under-hood fuse/relay box, and No. 20 (7.5 A) fuse in the under-dash fuse/relay box
    *   Poor ground at G201
    *   Cleanliness and tightness of all connectors

## Both fans do not run with the A/C on (but the A/C compressor runs with the A/C on)
*   **Diagnostic procedure:** Radiator and A/C condenser fan common circuit troubleshooting (see page 21-54)
*   **Also check for:**
    *   HVAC DTCs (see page 21-35)
    *   Blown No. 57 (20 A) and No. 58 (20 A) fuses in the main under-hood fuse/relay box, and No. 20 (7.5 A) fuse in the under-dash fuse/relay box
    *   Poor ground at G201
    *   Cleanliness and tightness of all connectors

## The A/C compressor clutch does not engage (but both fans run with the A/C on)
*   **Diagnostic procedure:** A/C compressor clutch circuit troubleshooting (see page 21-55)
*   **Also check for:**
    *   HVAC DTCs (see page 21-35)
    *   Blown No. 58 (20 A) fuse in the main under-hood fuse/relay box, and No. 20 (7.5 A) fuse in the under-dash fuse/relay box
    *   Cleanliness and tightness of all connectors

## A/C system does not come on (both fans and the A/C compressor do not work); heater is OK
*   **Diagnostic procedure:** A/C pressure switch circuit troubleshooting (see page 21-58)
*   **Also check for:**
    *   HVAC DTCs (see page 21-35)
    *   Cleanliness and tightness of all connectors

### Printed page 21-38

<a id="p1446"></a>
Source: [PDF p.1446](../page-images/p1446.png).

# Heating/Air Conditioning

## System Description

The air conditioning system removes heat from the passenger compartment by transferring heat from the ambient air to the evaporator. The evaporator cools the air with the refrigerant that is circulating through the evaporator. The refrigerant expands in the evaporator, and the evaporator becomes very cold and absorbs the heat from the ambient air. The blower fan pushes air across the evaporator where the heat is absorbed, and then it blows the cool air into the passenger compartment.

### BLOWER FAN

### EXPANSION VALVE
*(Meters the required amount of refrigerant into the evaporator)*

### A/C PRESSURE SWITCH
When the refrigerant is below 196 kPa (2.0 kgf/cm², 28 psi) or above 3,140 kPa (32 kgf/cm², 455 psi), the A/C pressure switch opens the circuit to the A/C switch and stops the air conditioning to protect the A/C compressor.

### EVAPORATOR
*(Absorption of heat)*

### EVAPORATOR TEMPERATURE SENSOR

### RECEIVER/DRYER

### DESICCANT
*(Traps debris, and removes moisture)*

### A/C CONDENSER
*(Radiation of heat)*

### THERMAL PROTECTOR
*(Opens the A/C compressor clutch circuit when the compressor temperature becomes too high)*

### RELIEF VALVE
*(Relieves pressure at the A/C compressor when the pressure is too high)*

### A/C COMPRESSOR
*(Suction and compression)*

**Pressure States:**
- HIGH PRESSURE VAPOR
- HIGH PRESSURE LIQUID
- LOW PRESSURE LIQUID
- LOW PRESSURE VAPOR

---

This vehicle uses HFC-134a (R-134a) refrigerant which does not contain chlorofluorocarbons. Pay attention to the following service items:

*   Do not mix refrigerants CFC-12(R-12) and HFC-134a (R-134a). They are not compatible.
*   Use only the recommended polyalkyleneglycol (PAG) refrigerant oil (SP-10) designed for the R-134a A/C compressor. Intermixing the recommended (PAG) refrigerant oil with any other refrigerant oil will result in A/C compressor failure.
*   All A/C system parts (A/C compressor, discharge line, suction line, evaporator, A/C condenser, receiver/dryer, expansion valve, O-rings for joints) are designed for refrigerant R-134a. Do not exchange with R-12 parts.
*   Use a halogen gas leak detector designed for refrigerant R-134a.
*   R-12 and R-134a refrigerant servicing equipment are not interchangeable. Use only a recovery/recycling/charging station that is U.L-listed and is certified to meet the requirements of SAE J2210 to service R-134a air conditioning systems.
*   Always recover refrigerant R-134a with an approved recovery/recycling/charging station before disconnecting any A/C fitting.

### Printed page 21-39

<a id="p1447"></a>
Source: [PDF p.1447](../page-images/p1447.png).

# HVAC Control Unit Inputs and Outputs

30P connector, wire side of female terminals.

| Cavity | Wire | Signal |
|---:|---|---|
| 1 | PNK | Air mix cool output |
| 2 | PNK/BLU | Air mix hot output |
| 3 | YEL/BLU | Mode DEF output |
| 4 | YEL/RED | Mode VENT output |
| 5 | GRY | Air mix potential +5 V output |
| 6 | PNK/BLK | Air mix potential input |
| 7 | BRN | Evaporator temperature sensor input |
| 8 | YEL/GRN | Mode 2 input |
| 9 | BRN/WHT | Mode 1 input |
| 10 | LT GRN | Sensor common ground output |
| 11 | BLU/RED | Blower feedback input |
| 12 | BLU/WHT | A/C pressure switch output |
| 13 | BLU/YEL | Power transistor control output |
| 15 | GRN/WHT | Fresh output |
| 16 | GRN/YEL | Recirculate output |
| 21 | YEL | Mode 4 input |
| 22 | BLK/WHT | Mode 3 input |
| 23 | BLK/WHT | Gauge assembly output |
| 26 | BLK | Ground (G402) input |
| 27 | RED/BLK | Taillight relay input |
| 28 | RED | Gauge assembly output |
| 29 | WHT/RED | +B power input |
| 30 | BLK/YEL | IG2 power input |

### Printed page 21-40

<a id="p1448"></a>
Source: [PDF p.1448](../page-images/p1448.png).

# A/C Circuit Diagram (part 1)

The [source circuit diagram](../page-images/p1448.png) shows main under-hood fuse/relay box, battery, fuses No. 41 (100 A), 42 (40 A), 54 (30 A), 56 (40 A), 57 (20 A), and 58 (20 A), under-dash fuses No. 20 and 25 (both 7.5 A), IG2 cut relay, radiator and condenser fan relays/motors, compressor clutch relay, blower motor relay, A/C pressure switch, ECM, grounds G201/G301, and model-year variants. Use source for exact circuit paths.

### Printed page 21-41

<a id="p1449"></a>
Source: [PDF p.1449](../page-images/p1449.png).

# A/C Circuit Diagram (part 2)

The [source circuit diagram](../page-images/p1449.png) continues the A/C and HVAC wiring: HVAC control unit 30P, blower motor and power transistor, evaporator temperature sensor, air mix and mode motors, recirculation motor, gauge assembly, taillight relay, and ground G402. Model notes: *1 2000–2005, *2 2000–2007, *3 2006–2008, *4 2008. Use the source image for exact wire paths, colors, and connector cavities.

### Printed page 21-42

<a id="p1450"></a>
Source: [PDF p.1450](../page-images/p1450.png).

# Heating/Air Conditioning
## DTC Troubleshooting
### DTC 1: A Problem in the Air Mix Control - Motor Circuit

1. Disconnect the air mix control motor 7P connector.
2. Test the air mix control motor (see page 21-20).
   **Is the air mix control motor OK?**
   * YES — Go to step 3.
   * NO — Go to step 7.

3. Disconnect the HVAC control unit 30P connector.
4. Check for continuity between body ground and the HVAC control unit 30P connector No. 1, 2, 5, 6, and 10 terminals individually.

**Is there continuity?**
*   **YES**—Repair short to body ground in the wire(s) between the HVAC control unit and the air mix control motor.
*   **NO — Go to step 5.**

5. Turn the ignition switch to ON (II), and measure the same terminals for voltage.

**Is there any voltage?**
*   **YES**—Repair short to power in the wire(s) between the HVAC control unit and the air mix control motor.
    *Warning: This short may also damage the HVAC control unit. Repair the short to power before replacing the HVAC control unit.*
*   **NO — Go to step 6.**

### Printed page 21-43

<a id="p1451"></a>
Source: [PDF p.1451](../page-images/p1451.png).

# DTC 1: Air Mix Control Motor Circuit (continued)

6. Turn ignition to LOCK (0). Check continuity from HVAC control unit 30P to air mix motor 7P:

| 30P | 7P |
|---:|---:|
| 1 | 2 |
| 2 | 1 |
| 5 | 5 |
| 6 | 3 |
| 10 | 7 |

If continuity exists, inspect both connectors; if sound, substitute a known-good HVAC control unit and recheck. Replace original if symptom clears. Otherwise repair open wire(s).
7. Remove air mix motor (p. 21-20).
8. Check linkage and doors for smooth movement. If smooth, replace motor; if not, repair linkage or doors.

# DTC 2: Mode Control Motor Circuit

1. Disconnect mode motor 7P connector.
2. Test mode motor (p. 21-21). If good, step 3; if not, step 7.
3. Disconnect HVAC control unit 30P connector.
4. Check 30P terminals **3, 4, 8, 9, 10, 21, 22** individually for continuity to ground. If any has continuity, repair short to ground between unit and motor; otherwise step 5.

### Printed page 21-44

<a id="p1452"></a>
Source: [PDF p.1452](../page-images/p1452.png).

# DTC 2: Mode Control Motor Circuit (continued)

5. Ignition ON (II): measure voltage at the same 30P terminals (3, 4, 8, 9, 10, 21, 22). If voltage appears, repair short to power before replacing HVAC control unit; otherwise step 6.
6. Ignition LOCK (0): check continuity from HVAC control unit 30P to mode motor 7P:

| 30P | 7P |
|---:|---:|
| 3 | 2 |
| 4 | 1 |
| 8 | 5 |
| 9 | 6 |
| 10 | 7 |
| 21 | 3 |
| 22 | 4 |

If continuity exists, inspect both connectors; if sound, substitute known-good HVAC control unit and recheck. Replace original if symptom clears. Otherwise repair open wire(s).

### Printed page 21-45

<a id="p1453"></a>
Source: [PDF p.1453](../page-images/p1453.png).

# DTC 2: Mode Control Motor Circuit (continued)

7. Remove mode control motor (p. 21-21).
8. Check linkage and doors for smooth movement. If smooth, replace motor; otherwise repair linkage or doors.

# DTC 3:A Problem in the Blower Motor Circuit

## Step 1
1. Check the No. 56 (40 A) fuse in the main under-hood fuse/relay box, and the No. 20 (7.5 A) fuse in the under-dash fuse/relay box.

   Are the fuses OK?
   - **YES** — Go to step 2.
   - **NO** — Replace the fuse(s), and recheck.

## Step 2
2. Connect the No. 2 terminal of the blower motor 2P connector to body ground with a jumper wire.

   > **BLOWER MOTOR 2P CONNECTOR**
   > **JUMPER WIRE**
   > **BLU/BLK** (Wire side of female terminals)

## Step 3
3. Turn the ignition switch to ON (II).

   Does the blower motor run?
   - **YES** — Go to step 4.
   - **NO** — Go to step 17.

## Step 4
4. Turn the ignition switch to LOCK (0).
5. Disconnect the jumper wire.
6. Disconnect the power transistor 5P connector.

### Printed page 21-46

<a id="p1454"></a>
Source: [PDF p.1454](../page-images/p1454.png).

# DTC 3: Blower Motor Circuit (continued)

7. Check power transistor 5P terminal 5 to ground. **YES:** step 8. **NO:** check open wire and ground G402.
8. Jumper power transistor 5P terminals 4 and 5.
9. Ignition ON (II): if blower runs at high speed, step 10; otherwise repair open wire between transistor and blower.
10. Ignition LOCK (0).
11. Disconnect jumper.
12. Disconnect HVAC control unit 30P connector.
13. Check 30P terminals 11 and 13 individually to ground. If continuity exists, repair short to ground between unit and transistor; otherwise step 14.
14. Check continuity **30P 11 → transistor 5P 1** and **30P 13 → 5P 3**. If continuity exists, step 15; otherwise repair open wire(s).

### Printed page 21-47

<a id="p1455"></a>
Source: [PDF p.1455](../page-images/p1455.png).

# DTC 3: Blower Motor Circuit (continued)

15. Reconnect HVAC control unit 30P connector.
16. Test power transistor (p. 21-19). If good, check HVAC 30P, blower 2P, and transistor 5P connections; if sound, substitute known-good HVAC unit and replace original only if symptom clears. If transistor is faulty, replace it.
17. Disconnect jumper.
18. Disconnect blower motor 2P connector.
19. Measure voltage between blower 2P terminal 1 and ground. **Battery voltage:** replace blower motor. **No voltage:** step 20.
20. Ignition LOCK (0).
21. Remove blower relay from main under-hood fuse/relay box and test (p. 22-48). If good, step 22; if faulty, replace relay.
22. Measure voltage between blower relay 4P socket terminal 4 and ground. **Battery voltage:** step 23. **No voltage:** replace main under-hood fuse/relay box.
23. Ignition ON (II).
24. Measure voltage between blower relay 4P socket terminal 1 and ground. **Battery voltage:** step 25. **No voltage:** repair open wire from under-dash No. 20 (7.5 A) fuse to relay.

### Printed page 21-48

<a id="p1456"></a>
Source: [PDF p.1456](../page-images/p1456.png).

# DTC 3: Blower Motor Circuit (continued)

25. Ignition LOCK (0).
26. Check continuity from blower relay 4P socket terminal 2 to body ground. If continuity exists, repair open **BLU/WHT** wire between relay and blower. If absent, check ground wire and G201.

# DTC 4: Evaporator Temperature Sensor Circuit

1. Disconnect sensor 2P connector.
2. Measure resistance across sensor terminals 1 and 2. Compare with [source resistance/temperature graph](../page-images/p1456.png) (about 30 kΩ at 0 °C and 8 kΩ at 30 °C). If within graph specification, step 3; otherwise replace sensor.
3. Disconnect HVAC control unit 30P connector.

### Printed page 21-49

<a id="p1457"></a>
Source: [PDF p.1457](../page-images/p1457.png).

# DTC 4: Evaporator Temperature Sensor Circuit (continued)

4. Check HVAC control unit 30P terminal 7 to ground. If continuity exists, repair short to ground between unit and sensor; otherwise step 5.
5. Check continuity **HVAC 30P 7 → sensor 2P 2**. If present, step 6; otherwise repair open wire.
6. Check continuity **HVAC 30P 10 → sensor 2P 1**. If present, check connectors; if sound, substitute known-good HVAC unit and replace original only if symptom clears. If absent, repair open wire.

### Printed page 21-50

<a id="p1458"></a>
Source: [PDF p.1458](../page-images/p1458.png).

# Heating/Air Conditioning
## Recirculation Control Motor Circuit Troubleshooting

1. Check the No. 20 (7.5 A) fuse in the under-dash fuse/relay box.
   Is the fuse OK?
   - **YES** — Go to step 2.
   - **NO** — Replace the fuse, and recheck.

2. Disconnect the recirculation control motor 7P connector.
3. Turn the ignition switch to ON (II).
4. Measure the voltage between the No. 1 terminal of the recirculation control motor 7P connector and body ground.
   Is there battery voltage?
   - **YES** — Go to step 5.
   - **NO** — Repair open in the wire between the No. 20 (7.5 A) fuse in the under-dash fuse/relay box and the recirculation control motor.

5. Turn the ignition switch to LOCK (0).
6. Test the recirculation control motor (see page 21-22).
   Is the recirculation control motor OK?
   - **YES** — Go to step 7.
   - **NO** — Go to step 11.

7. Disconnect the HVAC control unit 30P connector.
8. Check for continuity between the No. 15 and No. 16 terminals of the HVAC control unit 30P connector and body ground individually.

   Is there continuity?
   - **YES** — Repair short to body ground in the wire(s) between the HVAC control unit and the recirculation control motor.
   - **NO** — Go to step 9.

9. Turn the ignition switch to ON (II), and measure the same terminals for voltage.

   Is there any voltage?
   - **YES** — Repair short to power in the wire(s) between the HVAC control unit and the recirculation control motor. This short may also damage the HVAC control unit. Repair the short to power before replacing the HVAC control unit.
   - **NO** — Go to step 10.

21-50

### Printed page 21-51

<a id="p1459"></a>
Source: [PDF p.1459](../page-images/p1459.png).

# Recirculation Control Motor Circuit (continued)

10. Ignition LOCK (0): check continuity **HVAC 30P 15 → recirculation motor 7P 5** and **30P 16 → 7P 7**. If present, inspect both connectors, then substitute known-good HVAC unit and replace original if symptom clears. If absent, repair open wire(s).
11. Remove recirculation motor (p. 21-22).
12. Check linkage and doors. If smooth, replace motor; otherwise repair linkage or doors.

# HVAC Control Power and Ground Circuit Troubleshooting

1. Check main under-hood No. 54 (30 A) and under-dash No. 20 and No. 25 (each 7.5 A) fuses. If good, step 2; otherwise replace and recheck.
2. Disconnect HVAC control unit 30P connector.
3. Ignition ON (II).
4. Measure voltage from 30P terminal 30 to ground. If battery voltage, step 5; otherwise repair open wire from No. 20 fuse to HVAC unit.
5. Ignition LOCK (0).

### Printed page 21-52

<a id="p1460"></a>
Source: [PDF p.1460](../page-images/p1460.png).

# HVAC Control Power and Ground Circuit (continued)

6. Measure voltage from HVAC 30P terminal 29 (WHT/RED) to ground. If battery voltage, step 7; otherwise repair open wire between under-dash No. 25 (7.5 A) fuse and HVAC unit.
7. Check continuity from 30P terminal 26 (BLK) to ground. If present, inspect connector; if sound, substitute known-good HVAC unit and replace original only if symptom clears. If absent, inspect open ground wire and ground G402.

### Printed page 21-53

<a id="p1461"></a>
Source: [PDF p.1461](../page-images/p1461.png).

# A/C Condenser Fan Circuit Troubleshooting

**NOTE:**
*   Do not use this troubleshooting procedure if the radiator fan and/or the A/C compressor is inoperative. Refer to the symptom troubleshooting.
*   Before performing symptom troubleshooting, check for powertrain DTCs: '00-05 models (see page 11-3); '06-08 models (see page 11-213).

1. Check the No. 58 (20 A) fuse in the main under-hood fuse/relay box, and the No. 20 (7.5 A) fuse in the under-dash fuse/relay box.

   Are the fuses OK?
   *   **YES** — Go to step 2.
   *   **NO** — Replace the fuse(s), and recheck.

2. Remove the A/C condenser fan relay from the main under-hood fuse/relay box, and test it (see page 22-48).

   Is the relay OK?
   *   **YES** — Go to step 3.
   *   **NO** — Replace the A/C condenser fan relay.

3. Measure the voltage between the No. 1 terminal of the A/C condenser fan relay 4P socket and body ground.

   Is there battery voltage?
   *   **YES** — Go to step 4.
   *   **NO** — Replace the main under-hood fuse/relay box.

4. Connect the No. 1 and No. 2 terminals of the A/C condenser fan relay 4P socket with a jumper wire.

   Does the A/C condenser fan run?
   *   **YES** — Go to step 5.
   *   **NO** — Go to step 8.

5. Disconnect the jumper wire.

6. Turn the ignition switch to ON (II).

7. Measure the voltage between the No. 3 terminal of the A/C condenser fan relay 4P socket and body ground.

   Is there battery voltage?
   *   **YES** — Replace the main under-hood fuse/relay box.
   *   **NO** — Repair open in the wire between the No. 20 (7.5 A) fuse in the under-dash fuse/relay box and the A/C condenser fan relay.

8. Disconnect the jumper wire.

### Printed page 21-54

<a id="p1462"></a>
Source: [PDF p.1462](../page-images/p1462.png).

# A/C Condenser Fan Circuit Troubleshooting (continued)

9. Disconnect condenser fan 2P connector.
10. Check continuity **fan relay 4P socket 2 → condenser fan 2P 2**. If present, step 11; otherwise repair open wire between relay and fan.
11. Check condenser fan 2P terminal 1 to ground. **No continuity:** check open ground wire and G201. The source scan does not show the YES branch for this step; refer to the [source page](../page-images/p1462.png) before replacing parts.

# Radiator and A/C Condenser Fan Common Circuit Troubleshooting

**Note:** Use this procedure only when both fans are inoperative but compressor operates. Check powertrain DTCs first ('00–05 p. 11-3; '06–08 p. 11-213).

1. Check main under-hood fuses No. 57 and 58 (both 20 A) and under-dash No. 20 (7.5 A). If sound, step 2; otherwise replace and recheck.
2. Remove condenser fan relay.
3. Ignition ON (II).
4. Measure voltage from condenser fan relay 4P socket terminal 3 to ground (BLK/YEL). The decision branch continues on the next page.
5. Ignition LOCK (0).

### Printed page 21-55

<a id="p1463"></a>
Source: [PDF p.1463](../page-images/p1463.png).

# Radiator and A/C Condenser Fan Common Circuit (continued)

6. Reinstall condenser fan relay.
7. Set A/C switch OFF.
8. Ignition ON (II).
9. Backprobe voltage to ground with ECM connected: **2000–2005:** connector A 32P terminal 20; **2006–2008:** connector E 31P terminal 12. If battery voltage, inspect connector; if sound, substitute known-good ECM and replace original only if symptom clears (p. 11-115 or 11-389 respectively). If no voltage, repair open wire among radiator fan relay, condenser fan relay, and ECM.

# A/C Compressor Clutch Circuit Troubleshooting

**Note:** Use this procedure when fans run but clutch does not. Check powertrain DTCs ('00–05 p. 11-3; '06–08 p. 11-213).

1. Check main under-hood fuse No. 58 (20 A) and under-dash No. 20 (7.5 A). If sound, step 2; otherwise replace and recheck.
2. At idle, HDS PGM-FI Data List should show ECT sensor 1 **169–194 °F (76–90 °C)**, TP sensor about 0.5 V, RPM >800, A/C switch ON, A/C clutch ON. If any out of range, troubleshoot that value; otherwise step 3.
3. Remove and test compressor clutch relay (p. 22-48). If sound, step 4; otherwise replace relay.

### Printed page 21-56

<a id="p1464"></a>
Source: [PDF p.1464](../page-images/p1464.png).

# A/C Compressor Clutch Circuit (continued)

4. Measure voltage from compressor clutch relay 4P socket terminal 1 to ground. **Battery voltage:** step 5. **No voltage:** replace main under-hood fuse/relay box.
5. Jumper relay socket terminals 1 and 2. If clutch clicks, step 6; otherwise step 14.
6. Disconnect jumper.
7. Ignition ON (II).
8. Measure voltage from relay socket terminal 4 to ground. **Battery voltage:** step 9. **No voltage:** repair open wire from under-dash No. 20 (7.5 A) fuse to relay.
9. Ignition LOCK (0).
10. Reinstall compressor clutch relay.
11. Set A/C switch OFF.
12. Ignition ON (II).

### Printed page 21-57

<a id="p1465"></a>
Source: [PDF p.1465](../page-images/p1465.png).

# A/C Compressor Clutch Circuit (continued)

13. With ECM connected, backprobe voltage to ground: **2000–2005:** ECM A 32P terminal 17; **2006–2008:** ECM E 31P terminal 18. **Battery voltage:** inspect ECM connector; if sound, substitute known-good ECM and replace original only if symptom clears (p. 11-115 / 11-389). **No voltage:** repair open wire between compressor clutch relay and ECM.
14. Disconnect jumper.
15. Disconnect compressor clutch 1P connector.
16. Check continuity **clutch relay 4P socket 2 → clutch 1P terminal 1**. If present, check clutch clearance, thermal protector, and field coil (p. 21-68). If absent, repair open wire between relay and clutch.

### Printed page 21-58

<a id="p1466"></a>
Source: [PDF p.1466](../page-images/p1466.png).

# A/C Pressure Switch Circuit Troubleshooting

**Note:** Use when condenser fan, radiator fan, and compressor are all inoperative but heater works. Check powertrain DTCs first ('00–05 p. 11-3; '06–08 p. 11-213).

1. Disconnect pressure switch 2P connector.
2. Ignition ON (II).
3. Measure pressure switch 2P terminal 2 to ground. **About 5 V:** step 4. **Otherwise:** step 15.
4. Ignition LOCK (0).
5. Check continuity between pressure switch terminals 1 and 2. **YES:** step 6. **NO:** step 17.
6. Reconnect pressure switch 2P connector.
7. Disconnect HVAC control unit 30P connector.
8. Ignition ON (II).
9. Measure HVAC 30P terminal 12 to ground. **About 5 V:** step 10. **Otherwise:** repair open wire between HVAC unit and pressure switch.

### Printed page 21-59

<a id="p1467"></a>
Source: [PDF p.1467](../page-images/p1467.png).

# A/C Pressure Switch Circuit (continued)

10. Ignition LOCK (0).
11. Measure resistance across HVAC 30P terminals 7 and 10. **Less than 24 kΩ:** step 12. **Otherwise:** repair high resistance in evaporator temperature circuit.
12. Reconnect HVAC 30P.
13. Ignition ON (II).
14. Check blower at several speeds. **All speeds work:** inspect HVAC 30P and pressure switch 2P connectors; if sound, substitute known-good HVAC unit and replace original only if symptom clears. **Otherwise:** repair blower circuit.
15. Ensure A/C switch OFF.
16. With ECM connected, backprobe voltage to ground: **2000–2005:** ECM A 32P terminal 27; **2006–2008:** ECM E 31P terminal 28. **About 5 V:** repair open wire between ECM and pressure switch. **Otherwise:** inspect ECM connector; if sound, substitute known-good ECM and replace original only if symptom clears (p. 11-115 / 11-389).
17. Check A/C system pressure. If within specification, replace pressure switch; otherwise repair pressure problem.

### Printed page 21-60

<a id="p1468"></a>
Source: [PDF p.1468](../page-images/p1468.png).

# Evaporator Temperature Sensor Test

1. Remove evaporator core and sensor (p. 21-62).
2. Dip sensor in ice water and measure resistance across terminals.
3. Pour warm water on sensor and check for resistance change.
4. Compare readings with [source resistance/temperature graph](../page-images/p1468.png).
5. If out of specification, replace sensor (p. 21-62).

# HVAC Control Unit Removal/Installation

1. Remove instrument panel with HVAC unit (p. 20-84).
2. Remove self-tapping screws and unit (A) from panel (B).
3. Install in reverse order, then operate controls.
4. Run self-diagnostic function (p. 21-35) to confirm no problems.

### Printed page 21-61

<a id="p1469"></a>
Source: [PDF p.1469](../page-images/p1469.png).

# Blower/Evaporator Unit Removal/Installation

1. Recover the refrigerant with a recovery/recycling/charging station (see page 21-73).
2. Make sure you have the anti-theft code for the audio system, then write down the audio presets.
3. Remove the battery.
4. Pull out the grommets, then carefully separate the upper grommet (A) from the lower grommet (B) by releasing the locktabs (C).
5. Remove the bolt, then disconnect the suction line (A) and the receiver line (B) from the blower/evaporator unit. Plug or cap the lines immediately after disconnecting them to avoid moisture and dust contamination.
Fastener: 6 × 1.0 mm; torque
9.8 N-m (1.0 kgf·m, 7.2 lbf-ft)
6. Remove the passenger's dashboard lower cover (see page 20-86) and the right kick panel (see page 20-71).
7. Disconnect the dashboard wire harness connector from the passenger's door wire harness connector, then remove it. Remove the wire harness connectors and the convertible top control unit from the steering hanger beam.
8. Disconnect the connectors (A) from the blower motor, the power transistor, the evaporator sensor, and the recirculation control motor, then remove the wire harness clips (B). Remove the drain hose (C), the self-tapping screw, the mounting bolts, the mounting nuts, and the blower/evaporator unit (D).
9. Install the unit in the reverse order of removal, and note these items:
• If you're installing a new blower/evaporator unit, add refrigerant oil (SP-10) (see page 21-33).
• Replace the O-rings with new ones at each fitting, and apply a thin coat of refrigerant oil before installing them. Be sure to use the correct O-rings for HFC-134a (R-134a) to avoid leakage.
• Immediately after using the oil, reinstall the cap on the container, and seal it to avoid moisture absorption.
• Do not spill the refrigerant oil on the vehicle; it may damage the paint. If the refrigerant oil contacts the paint, wash it off immediately.
• Make sure that there is no air leakage.
• Charge the system (see page 21-75).
• Do the ECM idle learn procedure: '00-05 models (see page 11-140); '06-08 models (see page 11-462).
• Enter the anti-theft code for the audio system, then enter the audio presets.

### Printed page 21-62

<a id="p1470"></a>
Source: [PDF p.1470](../page-images/p1470.png).

# Heating/Air Conditioning
## Blower/Evaporator Unit Component Replacement

**Note these items when overhauling the blower/evaporator unit:**

*   The recirculation control motor (**A**), the power transistor (**B**), and the blower motor (**C**) can be replaced without removing the blower/evaporator unit.
*   If you're installing a new evaporator core (**D**), add refrigerant oil (**SP-10**) (see page 21-33).
*   Replace the O-rings with new ones at each fitting and apply a thin coat of refrigerant oil before installing them.
    *   Be sure to use the correct O-rings for HFC-134a (R-134a) to avoid leakage.
*   Immediately after using the oil, reinstall the cap on the container, and seal it to avoid moisture absorption.
*   Reinstall the evaporator temperature sensor (**E**) in its original location.
*   Before reassembly, make sure that the recirculation control linkage and doors move smoothly.
*   After reassembly, make sure the recirculation control motor runs smoothly (see page 21-22).
*   Make sure no air is leaking from the upper housing (**F**) and the lower housing (**G**) fitting.

**Diagram Labels:**
*   **A**: Recirculation control motor
*   **B**: Power transistor
*   **C**: Blower motor
*   **D**: Evaporator core
*   **E**: Evaporator temperature sensor
*   **F**: Upper housing
*   **G**: Lower housing

### Printed page 21-63

<a id="p1471"></a>
Source: [PDF p.1471](../page-images/p1471.png).

# Expansion Valve Replacement

1. Remove the blower/evaporator unit (see page 21-61).
2. Remove the evaporator core (see page 21-62).
3. Remove the bolts (A).
4. Remove the outer seal (B) and expansion valve (C).
5. Install the expansion valve in the reverse order of removal and note these items:
   - If you're installing a new expansion valve, add refrigerant oil (SP-10) (see page 21-33).
   - Replace the O-rings with new ones at each fitting, and apply a thin coat of refrigerant oil before installing them. Be sure to use the correct O-rings for HFC-134a (R-134a) to avoid leakage.
   - Immediately after using the oil, reinstall the cap on the container, and seal it to avoid moisture absorption.
   - Do not spill the refrigerant oil on the vehicle; it may damage the paint; if the refrigerant oil contacts the paint, wash it off immediately.
   - Make sure that there is no air leakage.
   - Charge the system (see page 21-75).

# Heater Unit/Core Replacement

SRS components are located in this area. Review the SRS component locations: '00-05 models (see page 23-11), '06-08 models (see page 23-12) and the precautions and procedures (see page 23-13) before doing repairs or service.

1. Make sure you have the anti-theft code for the audio system, then write down the audio presets.
2. Disconnect the negative cable from the battery.
3. Remove the heat shield of the exhaust manifold (see step 23 on page 6-29).
4. From under the hood, open the cable clamp (A), then disconnect the heater valve cable (B) from the heater valve arm (C). Turn the heater valve arm to the fully opened position as shown.
5. When the engine is cool, drain the engine coolant from the radiator (see page 10-9).

### Printed page 21-64

<a id="p1472"></a>
Source: [PDF p.1472](../page-images/p1472.png).

# Heating/Air Conditioning
## Heater Unit/Core Replacement (cont'd)

### Step 6
Remove the mounting bolt from the heater valve.
Slide the hose clamps (A) back, then disconnect the inlet heater hose (B) and the outlet heater hose (C) from the heater unit. Engine coolant will run out when the hoses are disconnected; drain it into a clean drip pan. Be sure not to let coolant spill on the electrical parts or the painted surfaces. If any coolant spills, rinse it off immediately.

*   **Torque Specification:** 6 x 1.0 mm, 9.8 N-m (1.0 kgf-m, 7.2 Ib-ft)

### Step 7
Remove the mounting nut from the heater unit.
Take care not to damage or bend the fuel lines, the brake lines, etc..

*   **Torque Specification:** 8 x 1.25 mm, 13 N-m (1.3 kgf-m, 9.4 Ib-ft)

### Step 8
Remove the dashboard (see page 20-87).

### Step 9
Remove the blower/evaporator unit (see page 21-61).

### Step 10
Remove the mounting bolts, the center brackets (A), and the audio brackets (B).

*   **Torque Specification:** 8 x 1.25 mm, 22 N-m (2.2 kgf-m, 16 Ib-ft)
*   **Torque Specification:** 6 x 1.0 mm, 9.8 N-m (1.0 kgf-m, 7.2 Ib-ft)
*   **Torque Specification:** 8 x 1.25 mm, 22 N-m (2.2 kgf-m, 16 Ib-ft)

### Step 11
Remove the SRS unit (see page 23-179).

### Step 12
Remove the self-tapping screws and the defroster outlet (A), then remove the wire harness clips (B).

### Printed page 21-65

<a id="p1473"></a>
Source: [PDF p.1473](../page-images/p1473.png).

# Heater Unit/Core Replacement (continued)

13. Disconnect mode and air mix motor connectors (A); release harness clip (B); remove mounting nuts, bolt, and heater unit (C).
14. Remove passenger heater outlet (A), then clamp (B). Avoid bending inlet/outlet pipes and pull out heater core (C).
15. Install heater core in reverse order.
16. Install heater unit in reverse order. Keep inlet and outlet hoses in their proper positions and clamp securely. Refill coolant (p. 10-9), adjust heater valve cable (p. 21-27), check for coolant and air leaks, see blower/evaporator installation (p. 21-61) for A/C work, perform ECM idle learn ('00–05 p. 11-140; '06–08 p. 11-462), and restore audio code/presets.

### Printed page 21-66

<a id="p1474"></a>
Source: [PDF p.1474](../page-images/p1474.png).

# Heating/Air Conditioning
## A/C Compressor Replacement

1. If the A/C compressor is marginally operable, run the engine at idle speed, and let the air conditioning work for a few minutes, then shut the engine off.
2. Make sure you have the anti-theft code for the audio system, then write down the audio presets.
3. Disconnect the negative cable from the battery.
4. Recover the refrigerant with a recovery/recycling/charging station (see page 21-73).
5. Remove the air cleaner housing (see page 6-25).
6. Remove the alternator (see page 4-45).
7. Remove the nuts, then disconnect the suction line (A) and the discharge line (B) from the A/C compressor. Plug or cap the lines immediately after disconnecting them to avoid moisture and dust contamination.
8. Disconnect the A / C compressor clutch connector, then remove the mounting bolts and the A/C compressor.
   - **Torque specification:** 10 x 1.25 mm, 44 N-m (4.5 kgf.m, 33 lbf ft)
9. If necessary, remove the mounting bolts and the A/C compressor bracket.

### Printed page 21-67

<a id="p1475"></a>
Source: [PDF p.1475](../page-images/p1475.png).

# Page 1475: S2000 HVAC - Installation of A/C Compressor

## 10. Install the A/C compressor in the reverse order of removal, and note these items:

*   If you're installing a new A/C compressor, you must calculate the amount of refrigerant oil to be removed from it (see page 21-33).
*   Replace the O-rings with new ones at each fitting, and apply a thin coat of refrigerant oil before installing them. Be sure to use the correct O-rings for HFC-134a (R-134a) to avoid leakage.
*   Use refrigerant oil (SP-10) for HFC-134a KEIHIN spiral type A/C compressor only.
*   To avoid contamination, do not return the oil to the container once dispensed, and never mix it with other refrigerant oils.
*   Immediately after using the oil, reinstall the cap on the container, and seal it to avoid moisture absorption.
*   Do not spill the refrigerant oil on the vehicle; it may damage the paint. If the refrigerant oil contacts the paint, wash it off immediately.
*   Charge the system (see page 21-75).
*   Do the ECM idle learn procedure: '00-05 models (see page 11-140); '06-08 models (see page 11-462).
*   Enter the anti-theft code for the audio system, then enter the audio presets.

### Printed page 21-68

<a id="p1476"></a>
Source: [PDF p.1476](../page-images/p1476.png).

# Heating/Air Conditioning
## A/C Compressor Clutch Check

1. Check the armature plate for discoloration, peeling, or other damage. If there is damage, replace the clutch set (see page 21-69).

2. Check the rotor pulley bearing play and drag by rotating the rotor pulley by hand. Replace the clutch set with a new one if it is noisy or has excessive play/drag (see page 21-69).

3. Measure the clearance between the rotor pulley (A) and the armature plate (B) all the way around. If the clearance is not within specified limits, remove the armature plate (see page 21-69) and add or remove shims as needed to increase or decrease clearance.

**Clearance:** 0.35—0.65 mm (0.014±0.026 in.)

> **NOTE:** The shims are available in four thicknesses: 0.1 mm, 0.2 mm, 0.4 mm, and 0.5 mm.

[Source clearance and electrical diagrams](../page-images/p1476.png)
*Figure A indicates rotor pulley (A) and armature plate (B)*

4. Release the field coil connector from the holder, then disconnect it. Check the thermal protector for continuity. If there is no continuity, replace the thermal protector (see page 21-71).

> **NOTE:** The thermal protector will have no continuity above 252 to 262 °F (122 to 128 °C). When the temperature drops below 241 to 219 °F (116 to 104 °C), the thermal protector will have continuity.

5. Check resistance of the field coil. If resistance is not within specifications, replace the coil (see page 21-69).

**Field Coil Resistance:** 3.05—3.35 Ω at 68 °F (20 °C)

### Printed page 21-69

<a id="p1477"></a>
Source: [PDF p.1477](../page-images/p1477.png).

# A/C Compressor Clutch Overhaul

## Special Tools Required
*   A/C clutch holder, Robinair 10204 or Kent-Moore J37872, or Honda Tool and Equipment KMT-J33939, commercially available

### Step 1
Remove the center nut (A) while holding the armature plate with a commercially available A/C clutch holder (B).

### Step 2
Remove the armature plate (A) and shim(s) (B), taking care not to lose the shim(s). If the clutch needs adjustment, increase or decrease the number and thickness of shims as necessary, then reinstall the armature plate, and recheck its clearance (see page 21-68).

> **NOTE:** The shims are available in four thicknesses: 0.1 mm, 0.2 mm, 0.4 mm, and 0.5 mm.

### Step 3
If you are replacing the field coil, remove the snap ring (A) with snap ring pliers, then remove the rotor pulley (B). Be careful not to damage the pulley and A/C compressor.

### Step 4
Remove the bolt and holder (A), then disconnect the field coil connector (B). Loosen the clamp screw (C) to free the field coil wire. Remove the snap ring (D) with snap ring pliers, then remove the field coil (E). Be careful not to damage the field coil and A/C compressor.

*(cont'd)*

### Printed page 21-70

<a id="p1478"></a>
Source: [PDF p.1478](../page-images/p1478.png).

# A/C Compressor Clutch Overhaul (cont'd)

## 5. Reassemble the clutch in the reverse order of disassembly, and note these items:

*   Install the field coil with the wire side facing down, and align the boss on the A/C field coil with the hole in the A/C compressor.
*   Clean the rotor pulley and A/C compressor sliding surfaces with contact cleaner or other non-petroleum solvent.
*   Install new snap rings, note the installation direction, and make sure they are fully seated in the groove.
*   Make sure that the rotor pulley turns smoothly after it's reassembled.
*   Route and clamp the wires properly or they can be damaged by the rotor pulley.

### Printed page 21-71

<a id="p1479"></a>
Source: [PDF p.1479](../page-images/p1479.png).

# A/C Compressor Thermal Protector Replacement

1. Remove the bolt, the ground terminal (A), and the holder (B). Disconnect the field coil connector (C), then remove the thermal protector (D).
   - **Torque:** 7.4 N m (0.75 kgf m, 5 lbf-ft)

2. Replace the thermal protector (A) with a new one, and apply silicone sealant (B) to the bottom of the thermal protector.

3. Install the thermal protector in the reverse order of removal.

---

# A/C Compressor Relief Valve Replacement

**NOTE:** If the A/C compressor relief valve released refrigerant to the atmosphere, determine and correct the cause of the excessive system pressure, then replace the relief valve.

1. Recover the refrigerant with a recovery/recycling/charging station (see page 21-73).

2. Remove the relief valve (A), and the O-ring (B). Plug the opening to keep foreign matter from entering the system and the A/C compressor oil from running out.

3. Clean the mating surfaces.

4. Replace the O-ring with a new one at the relief valve, and apply a thin coat of refrigerant oil before installing it.

5. Remove the plug, and install and tighten the relief valve.

6. Charge the system (see page 21-75).

### Printed page 21-72

<a id="p1480"></a>
Source: [PDF p.1480](../page-images/p1480.png).

# Heating/Air Conditioning
## A/C Condenser Replacement

1. Recover the refrigerant with a recovery/recycling/charging station (see page 21-73).
2. Remove the air cleaner housing (see page 6-25).
3. Remove the bolts, then remove the upper mount brackets from the radiator.
   - **Torque:** 6 × 1.0 mm
   - **Value:** 9.8 N-m (1.0 kgf·m , 7.2 lbf-ft)
4. Remove the bolts, then disconnect the discharge line (A) and the A/C condenser line (B) from the A/C condenser. Plug or cap the lines immediately after disconnecting them to avoid moisture and dust contamination.
   - **Torque:** 6 × 1.0 mm
   - **Value:** 9.8 N-m (1.0 kgf·m , 7.2 lbf-ft)
5. Remove the bolts and the upper mount brackets (A), then remove the A/C condenser (B) by lifting it up.
   > **Warning:** Be careful not to damage the radiator or the A/C condenser fins when removing the A/C condenser.
   - **Labels:** A, B
6. Install the A/C condenser in the reverse order of removal, and note these items:
   - If you're installing a new A/C condenser, add refrigerant oil (SP-10) (see page 21-33).
   - Replace the O-rings with new ones at each fitting, and apply a thin coat of refrigerant oil before installing them. Be sure to use the correct O-rings for HFC-134a (R-134a) to avoid leakage.
   - Immediately after using the oil, reinstall the cap on the container, and seal it to avoid moisture absorption.
   - Do not spill the refrigerant oil on the vehicle; it may damage the paint. If the refrigerant oil contacts the paint, wash it off immediately.
   - Be careful not to damage the radiator or the A/C condenser fins when installing the A/C condenser.
   - Charge the system (see page 21-75).

### Printed page 21-73

<a id="p1481"></a>
Source: [PDF p.1481](../page-images/p1481.png).

# Refrigerant Recovery

**CAUTION**
*   Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.
*   Be careful when connecting service equipment.
*   Do not breathe refrigerant or vapor.

1.  Connect an R-134a refrigerant recovery/recycling/charging station (A) to the high-pressure service port (B) and the low-pressure service port (C), as shown, following the equipment manufacturer's instructions.
2.  Measure the amount of refrigerant oil removed from the A/C system after the recovery process is completed. Be sure to put the same amount of new refrigerant oil back into the A/C system before charging.

Use only service equipment that is U.L-listed and is certified to meet the requirements of SAE J2210 to remove HFC-134a (R-134a) from the air conditioning system.

If accidental system discharge occurs, ventilate the work area before resuming service.

Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

### Printed page 21-74

<a id="p1482"></a>
Source: [PDF p.1482](../page-images/p1482.png).

# Heating/Air Conditioning
## System Evacuation

**CAUTION**
*   Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.
*   Be careful when connecting service equipment.
*   Do not breathe refrigerant or vapor.

Use only service equipment that is U.L-listed and is certified to meet the requirements of SAE J2210 to remove HFC-134a (R-134a) from the air conditioning system.

If accidental system discharge occurs, ventilate the work area before resuming service.

Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

1.  When an A/C system has been opened to the atmosphere, such as during installation or repair, it must be evacuated using an R-134a refrigerant recovery/recycling/charging station (If the system has been open for several days, the receiver/dryer should be replaced, and the system should be evacuated for several hours.)
2.  Connect an R-134a refrigerant recovery/recycling/charging station (A) to the high-pressure service port (B) and the low-pressure service port (C) as shown, following the equipment manufacturer's instructions. Evacuate the system.
3.  If the low-pressure does not reach more than 93.3 kPa (700 mmHg, 27.6 in.Hg) within 15 minutes, there is probably a leak in the system. Partially charge the system, and check for leaks (see step 3 on page 21-76).

### Printed page 21-75

<a id="p1483"></a>
Source: [PDF p.1483](../page-images/p1483.png).

# System Charging

> **CAUTION**
> Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat. Be careful when connecting service equipment. Do not breathe refrigerant or vapor.
> Use only service equipment that is U.L.-listed and is certified to meet the requirements of SAE J2210 to remove HFC-134a (R-134a) from the air conditioning system.
> If accidental system discharge occurs, ventilate the work area before resuming service. Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

1. Connect a R-134a refrigerant recovery/recycling/charging station (A) to the high-pressure service port (B) and the low-pressure service port (C), as shown, following the equipment manufacturer's instructions.
2. Evacuate the system (see page 21-74).
3. Add the same amount of new refrigerant oil to the system that was removed during recovery. Use only SP-10 refrigerant oil.
4. Charge the system with the specified amount of R-134a refrigerant. Do not overcharge the system; the A/C compressor will be damaged.

Select the appropriate units of measure for your refrigerant charging station.

**Refrigerant Capacity:**
*   550 to 600 g
*   0.55 to 0.60 kg
*   1.2 to 1.3 lbs
*   19.4 to 21.2 oz

5. Check for refrigerant leaks (see page 21-76).
6. Check for system performance (see page 21-78).

### Printed page 21-76

<a id="p1484"></a>
Source: [PDF p.1484](../page-images/p1484.png).

# Heating/Air Conditioning
## Refrigerant Leak Test
### Special Tools Required
*   Leak detector
*   Honda Tool and Equipment YGK-H-10PM (commercially available)

---

**WARNING**
*   Compressed air mixed with R-134a forms a combustible vapor.
*   The vapor can burn or explode causing serious injury.
*   Never use compressed air to pressure test R-134a service equipment or vehicle air conditioning systems.

**CAUTION**
*   Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.
*   Be careful when connecting service equipment.
*   Do not breathe refrigerant or vapor.

Use only service equipment that is U.L.-listed and is certified to meet the requirements of SAE J2210 to remove HFC-134a (R-134a) from the air conditioning system.

If accidental system discharge occurs, ventilate the work area before resuming service.

R-134a service equipment or vehicle air conditioning systems should not be pressure tested or leak tested with compressed air.

Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

1.  Connect an R-134a refrigerant recovery/recycling/charging station (A) to the high-pressure service port (B) and the low-pressure service port (C), as shown, following the equipment manufacturer's instructions.
2.  Open the high pressure valve to charge the system to the specified capacity, then close the supply valve, and remove the charging station fittings.
    *   Select the appropriate units of measurement for your refrigerant charging station.
    *   **Refrigerant Capacity:**
        *   550 to 600 g
        *   0.55 to 0.60 kg
        *   1.2 to 1.3 lbs
        *   19.4 to 21.2 oz
3.  Check the system for leaks using an R-134a refrigerant leak detector with an accuracy of 14 g (0.5 oz) per year or better.
4.  If you find leaks that require the system to be opened (to repair or replace hoses, fittings, etc.), recover refrigerant from the system.
5.  After checking and repairing leaks, the system must be evacuated.

### Printed page 21-77

<a id="p1485"></a>
Source: [PDF p.1485](../page-images/p1485.png).

# A/C System Test — Pressure Test

The [source diagnostic table](../page-images/p1485.png) groups symptoms, causes, and remedies. The first test-result row prints “20 °F (20 °C)” for the driver's/passenger's vent difference; those units conflict, so verify against the source before using that threshold.

| Test result / related symptom | Probable cause | Remedy |
|---|---|---|
| Vent temperatures differ; poor A/C, both pressures low | Low refrigerant charge | Recover, evacuate, recharge to specified amount (pp. 21-73, 21-75). |
| Vent temperatures differ; poor A/C, both pressures low | Air mix door inoperable | Repair or replace. |
| High discharge pressure; after stop pressure quickly falls to ~196 kPa then gradually | Air in system | Recover, evacuate, recharge. |
| High discharge pressure; reduced condenser airflow | Clogged condenser/radiator fins or fan malfunction | Clean fins; check voltage, fan RPM, and direction. |
| High discharge pressure; condenser line excessively hot | Restricted refrigerant flow | Replace restricted lines. |
| Low discharge pressure; pressures quickly balance after stop, low side higher than normal | Faulty compressor discharge valve or seal | Replace compressor. |
| Low discharge pressure; expansion valve outlet not frosted, low gauge in vacuum | Faulty expansion valve or moisture | Replace valve or recover/evacuate/recharge, respectively. |
| Low suction pressure; valve not frosted, low line not cold, gauge in vacuum | Frozen/faulty expansion valve | Recover/evacuate/recharge for moisture; replace faulty valve. |
| Low suction pressure; discharge temperature low, airflow restricted | Frozen evaporator | Run fan with compressor off, then check evaporator sensor. |
| Low suction pressure; expansion valve frosted | Clogged expansion valve | Clean or replace. |
| Low suction pressure; receiver/dryer outlet cool, inlet warm | Clogged receiver/dryer | Replace. |
| High suction pressure; low hose/check joint cooler than around evaporator | Expansion valve open too long | Repair or replace. |
| High suction pressure; condenser water-cooling lowers pressure | Excess refrigerant | Recover, evacuate, recharge. |
| High suction pressure; high/low sides equalize immediately after stop, gauges fluctuate running | Faulty gasket, high-pressure valve, or particle in valve | Replace compressor. |
| Both pressures high; reduced condenser airflow | Clogged fins or fan malfunction | Clean fins; check fan voltage, RPM, direction. |
| Both pressures low; low hose/metal ends cooler than evaporator | Clogged or kinked low-pressure hose | Repair or replace. |
| Both pressures low; expansion valve much cooler than receiver/dryer | Clogged high-pressure line | Repair or replace. |
| Refrigerant leak; dirty clutch | Compressor shaft seal leaking | Replace compressor. |
| Refrigerant leak; dirty compressor bolt(s) | Leak around bolts | Tighten bolts or replace compressor. |
| Refrigerant leak; gasket wet with oil | Gasket leaking | Replace compressor. |
| Refrigerant leak; dirty A/C fitting | Leaking O-ring | Clean fitting, replace O-ring. |

### Printed page 21-78

<a id="p1486"></a>
Source: [PDF p.1486](../page-images/p1486.png).

# Heating/Air Conditioning
## A/C System Test (cont'd)
### Performance Test

**WARNING**
Compressed air mixed with R-134a forms a combustible vapor.
The vapor can burn or explode causing serious injury.
Never use compressed air to pressure test R-134a service equipment or vehicle air conditioning systems.

**CAUTION**
* Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.
* Be careful when connecting service equipment.
* Do not breathe refrigerant or vapor.

The performance test will help determine if the air conditioner system is operating within specifications.
Use only service equipment that is U.L.-listed and is certified to meet the requirements of SAE J2210 to remove HFC-134a (R-134a) from the air conditioning system.
If accidental system discharge occurs, ventilate the work area before resuming service.
R-134a service equipment or vehicle air conditioning systems should not be pressure tested or leak tested with compressed air.
Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

1. Connect an R-134a refrigerant recovery/recycling/charging station to the high-pressure service port and the low-pressure service port, following the equipment manufacturer's instructions.
2. Determine the relative humidity and air temperature.
3. Remove the passenger's dashboard lower cover (see page 20-86).
4. Insert a thermometer (A) in the center vent, and place another thermometer (B) near the blower unit.

**5. Test conditions:**
* Avoid direct sunlight, put the top up.
* Open the hood.
* Open the front doors.
* Set the temperature control dial on Max Cool, the mode control dial on Vent, and the recirculation control switch on Recirculate.
* Turn the A/C switch on and the fan switch on Max.
* Run the engine speed at 1,500 rpm.
* No driver or passengers in vehicle.

**6. After running the air conditioning for 10 minutes under the above test conditions, read the delivery temperature from the thermometer in the center vent, the intake temperature near the blower unit, and the high and low system pressure from the A/C gauges.**

### Printed page 21-79

<a id="p1487"></a>
Source: [PDF p.1487](../page-images/p1487.png).

# A/C Performance Test — Vent Temperature Chart

7. Mark vent delivery temperature on the vertical axis and ambient intake temperature on the bottom axis. Draw horizontal and vertical lines to intersect. The intersection should fall within the shaded region near the measured humidity level (about 10% tolerance); outside readings call for further inspection. Use the [source vent/ambient chart](../page-images/p1487.png) for the actual bounds; it covers roughly 60–120 °F ambient, 32–92 °F vent temperature, and 20–80% humidity.

### Printed page 21-80

<a id="p1488"></a>
Source: [PDF p.1488](../page-images/p1488.png).

# A/C Performance Test — High-Side Pressure Chart

8. Mark high-side discharge pressure on the vertical axis and ambient intake temperature on the bottom axis; draw lines to intersect. Compare with the shaded region for measured humidity (about 10% tolerance); outside readings call for further inspection. Use the [source high-side pressure chart](../page-images/p1488.png) for the actual bounds. The source chart spans 0–450 psi (0–3103 kPa), 60–120 °F ambient, and labels 20–80% humidity.

### Printed page 21-81

<a id="p1489"></a>
Source: [PDF p.1489](../page-images/p1489.png).

# A/C Performance Test — Low-Side Pressure Chart

9. Mark low-side suction pressure on the vertical axis and ambient intake temperature on the bottom axis; draw lines to intersect. Compare with the shaded region for measured humidity (about 10% tolerance); outside readings call for further inspection. Use the [source low-side pressure chart](../page-images/p1489.png) for the actual bounds. The source chart spans 0–100 psi (0–689 kPa), 60–120 °F ambient, and labels 20–80% humidity.

### Printed page 21-82

<a id="p1490"></a>
Source: [PDF p.1490](../page-images/p1490.png).

# Blank source scan

This PDF page has no legible manual content. The source image is a black scan artifact; no procedure is transcribed.

### Printed page 21-83

<a id="p1491"></a>
Source: [PDF p.1491](../page-images/p1491.png).

# Page 1491

## S2000 HVAC Chapter: Supplemental Restraint System (SRS) Safety and Service Warnings

### Critical Safety Notice
To avoid rendering the SRS inoperative, which could lead to personal injury or death in the event of a severe frontal collision, all SRS service work should be done by an authorized Honda dealer.

Improper service procedures, including incorrect removal and installation of the SRS , could lead to personal injury caused by unintentional activation of the airbags and seat belt tensioners.

### Operational Restrictions
Do not bump or impact the SRS unit, or front impact sensors when the ignition switch is ON (II), or for at least 3 minutes after the ignition switch is turned OFF; otherwise, the system may fail in a collision, or airbags may deploy.

### Identification and Circuit Handling
SRS electrical connectors are identified by yellow color coding. Related components are located in the steering column, console, dashboard, dashboard lower panel, in the dashboard above the glove box. Do not use electrical test equipment on these circuits.
