# Automatic Transaxle (A240E / A241E) — Part 1

*Section code: `AT` | PDF pages 519–592 of `prepared.pdf` | Covers A240E (4A-GE) and A241E (4A-GZE) Electronic Controlled Transaxles (ECT). Torque is printed as `kg-cm (ft-lb, N·m)`.*

This is Part 1 of the Automatic Transaxle chapter. It covers system description, troubleshooting, the operating mechanism, the automatic shift diagrams, on-vehicle repair, transaxle removal, torque converter, oil pump, transmission disassembly, and the start of component-group work (oil pump and direct clutch). Component-group inspection/assembly and transmission reassembly continue in [Part 2](12b-automatic-transmission-a240e-a241e-part-2.md).

## Chapter contents (manual page codes)

| Section | Manual page |
|---|---|
| System Description | AT-2 |
| Troubleshooting | AT-2 |
| — Basic Troubleshooting | AT-2 |
| — General Troubleshooting | AT-3 |
| — Preliminary Check | AT-5 |
| — Manual Shifting Test | AT-7 |
| — Stall Test | AT-8 |
| — Time Lag Test | AT-9 |
| — Hydraulic Test | AT-10 |
| — Road Test | AT-11 |
| — Electronic Control System | AT-15 |
| Operating Mechanism for Each Gear | AT-30 |
| Automatic Shift Diagram (A240E/4A-GE) | AT-31 |
| Automatic Shift Diagram (A241E/4A-GZE) | AT-34 |
| On-Vehicle Repair | AT-37 |
| Removal of Transaxle | AT-44 |
| Torque Converter | AT-48 |
| Oil Pump | AT-48 |
| Disassembly of Transmission | AT-50 |
| Component Group Disassembly, Inspection and Assembly | AT-70 |
| — Oil Pump | AT-71 |
| — Direct Clutch | AT-74 |
| — Forward Clutch | AT-77 |
| — No.1 One-way Clutch and Sun Gear | AT-80 |
| — No.2 One-way Clutch and Rear Planetary Gear | AT-82 |
| — First and Reverse Brake Piston | AT-84 |
| — Intermediate Shaft | AT-86 |
| — Counter Shaft | AT-88 |
| — Valve Body | AT-96 |
| Assembly of Transmission | AT-112 |
| Differential | AT-134 |
| Installation of Transaxle | AT-144 |

## System Description

The transaxle for A240E and A241E, also called Electronic Controlled Transaxle (ECT), differs from the oil-pressure-control-type transaxle in that it is controlled by a microcomputer. Accordingly, troubleshooting procedures differ also.

Trouble occurring in the ECT can stem from one of three sources: the engine, the ECT electronic control unit, or the transaxle itself. Before troubleshooting, determine in which of these three sources the problem lies, and begin troubleshooting with the simplest operation, gradually working up in order of difficulty.

## Troubleshooting

### Basic Troubleshooting

Before troubleshooting an ECT, first determine whether the problem is electrical or mechanical. Use the basic troubleshooting flow below. If the cause is already known, using this basic chart together with the [General Troubleshooting](#general-troubleshooting) chart should speed the procedure.

| Step | Check | Result | Next action |
|---|---|---|---|
| 1 | Preliminary Check (see AT-5) | OK | Go to step 2 |
| 1 | Preliminary Check (see AT-5) | Bad | Repair or replace |
| 2 | Read Diagnostic Code (see AT-23) | OK | Go to step 3 |
| 2 | Read Diagnostic Code (see AT-23) | Bad | Repair or replace |
| 3 | Manual Shifting Test (see AT-7) | OK | Electrical Control System Check → repair or replace |
| 3 | Manual Shifting Test (see AT-7) | Bad | Stall Test, Time Lag Test and Hydraulic Test → repair transmission |

### General Troubleshooting

Page references in the last column are the manual's own `AT-` page codes.

| Problem | Possible cause | Remedy | Page |
|---|---|---|---|
| Fluid discolored or smells burnt | Fluid contaminated | Replace fluid | AT-5 |
| | Torque converter faulty | Replace torque converter | AT-48 |
| | Transmission faulty | Disassemble and inspect transmission | AT-50 |
| Vehicle does not move in any forward range or reverse | Control cable out of adjustment | Adjust control cable | AT-6 |
| | Valve body or primary regulator faulty | Inspect valve body | AT-96 |
| | Parking lock pawl faulty | Inspect parking lock pawl | AT-66 |
| | Torque converter faulty | Replace torque converter | AT-48 |
| | Oil pump intake screen blocked | Clean screen | — |
| | Transmission faulty | Disassemble and inspect transmission | AT-50 |
| Shift lever position incorrect | Control cable out of adjustment | Adjust control cable | AT-6 |
| | Manual valve and lever faulty | Inspect valve body | AT-96 |
| | Transmission faulty | Disassemble and inspect transmission | AT-50 |
| Harsh engagement into any drive range | Throttle cable out of adjustment | Adjust throttle cable | AT-6 |
| | Valve body or primary regulator faulty | Inspect valve body | AT-96 |
| | Transmission faulty | Disassemble and inspect transmission | AT-50 |
| Delayed 1-2, 2-3 or 3-OD up-shift, or down-shifts from OD-3 or 3-2 and shifts back to 4 or 3 | Throttle cable out of adjustment | Adjust throttle cable | AT-6 |
| | Valve body faulty | Inspect valve body | AT-96 |
| | Solenoid valve faulty | Inspect solenoid valve | AT-27 |
| Slips on 1-2, 2-3 or 3-OD up-shift, or slips or shudders on acceleration | Control cable out of adjustment | Adjust control cable | AT-6 |
| | Throttle cable out of adjustment | Adjust throttle cable | AT-6 |
| | Valve body faulty | Inspect valve body | AT-96 |
| | Solenoid valve faulty | Inspect solenoid valve | AT-17 <!-- NEEDS REVIEW: page image confirms "AT-17" as printed, but every other "Inspect solenoid valve" row points to AT-27; likely an original manual typo — transcribed as printed --> |
| | Transmission faulty | Disassemble and inspect transmission | AT-50 |
| Vehicle does not hold in P range | Control cable out of adjustment | Adjust control cable | AT-6 |
| | Parking lock pawl cam and spring faulty | Inspect cam and spring | AT-66 |
| Drag, binding or tie-up on 1-2, 2-3 or 3-OD up-shift | Control cable out of adjustment | Adjust control cable | AT-6 |
| | Valve body faulty | Inspect valve body | AT-96 |
| | Transmission faulty | Disassemble and inspect transmission | AT-50 |
| No lock-up in 2nd, 3rd or OD | Electronic control faulty | Inspect electronic control | AT-15 |
| | Valve body faulty | Inspect valve body | AT-96 |
| | Solenoid valve faulty | Inspect solenoid valve | AT-27 |
| | Transmission faulty | Disassemble and inspect transmission | AT-50 |
| Harsh down-shift | Throttle cable out of adjustment | Adjust throttle cable | AT-6 |
| | Valve body faulty | Inspect valve body | AT-96 |
| | Transmission faulty | Disassemble and inspect transmission | AT-50 |
| No down-shift when coasting | Valve body faulty | Inspect valve body | AT-96 |
| | Solenoid valve faulty | Inspect solenoid valve | AT-27 |
| | Electronic control faulty | Inspect electronic control | AT-15 |
| Down-shift occurs too quickly or too late while coasting | Throttle cable out of adjustment | Adjust throttle cable | AT-6 |
| | Valve body faulty | Inspect valve body | AT-96 |
| | Transmission faulty | Disassemble and inspect transmission | AT-50 |
| | Solenoid valve faulty | Inspect solenoid valve | AT-27 |
| | Electronic control faulty | Inspect electronic control | AT-15 |
| No OD-3, 3-2 or 2-1 kick-down | Throttle cable out of adjustment | Adjust throttle cable | AT-6 |
| | Solenoid valve faulty | Inspect solenoid valve | AT-96 <!-- NEEDS REVIEW: page image confirms "AT-96" as printed, but the "Inspect solenoid valve" remedy points to AT-27 elsewhere; likely an original manual typo — transcribed as printed --> |
| | Electronic control faulty | Inspect electronic control | AT-15 |
| | Valve body faulty | Inspect valve body | AT-96 |
| No engine braking in 2 or L range | Solenoid valve faulty | Inspect solenoid valve | AT-27 |
| | Electronic control faulty | Inspect electronic control | AT-15 |
| | Valve body faulty | Inspect valve body | AT-96 |
| | Transmission faulty | Disassemble and inspect transmission | AT-50 |

### Preliminary Check

1. **CHECK FLUID LEVEL**
   > **NOTE:** The vehicle must have been driven so that the engine and transmission are at normal operating temperature (fluid temperature: 70 – 80°C or 158 – 176°F).
   1. Park the vehicle on a level surface, set the parking brake.
   2. With the engine idling, shift the selector into each gear from P range to L range and return to P range.
   3. Pull out the transmission dipstick and wipe it clean.
   4. Push it back fully into the tube.
   5. Pull it out and check that the fluid level is in the HOT range. If the level is at the low side of either range, add fluid.
   - Fluid type: **ATF DEXRON® II**
   > **CAUTION:** Do not overfill.
2. **CHECK FLUID CONDITION**
   - If the fluid smells burnt or is black, replace it.
3. **REPLACE ATF**
   > **CAUTION:** Do not overfill.
   1. Remove the drain plug and drain the fluid.
   2. Reinstall the drain plug securely.
   3. With the engine OFF, add new fluid through the filler tube. **SST 09043-38100**
   - Fluid: **ATF DEXRON® II**
   - Capacity:

   | Application | Capacity |
   |---|---|
   | A240E/4A-GE | 7.2 liters (7.6 US qts, 6.3 Imp. qts) |
   | A241E/4A-GZE | 7.9 liters (8.4 US qts, 7.0 Imp. qts) |
   | Drain and refill (reference) | 3.1 liters (3.3 US qts, 2.7 Imp. qts) |

   4. Start the engine and shift the selector into all positions from P through L and then shift into P.
   5. With the engine idling, check the fluid level. Add fluid up to the "COOL" level on the dipstick.
   6. Check the fluid level with the normal fluid temperature (70 – 80°C or 158 – 176°F) and add as necessary.
   > **CAUTION:** Do not overfill.
4. **INSPECT AND ADJUST THROTTLE CABLE**
   1. Depress the accelerator pedal all the way and check that the throttle valve opens fully.
      > **NOTE:** If the valve does not open fully, adjust the accelerator link.
   2. Fully depress the accelerator.
   3. Loosen the adjustment nuts.
   4. Adjust the cable housing so that the distance between the end of the boot and stopper on the cable is the standard.
      - Standard boot and cable stopper distance: **0 – 1 mm (0 – 0.04 in.)**
   5. Tighten the adjusting nuts.
   6. Recheck the adjustments.
5. **ADJUST CONTROL CABLE**
   1. Loosen the swivel nut on manual shift lever.
   2. Push the manual lever fully toward the right side of the vehicle.
   3. Return the lever two notches to NEUTRAL position.
   4. Set the shift lever to N.
   5. While holding the lever lightly toward the R range side, tighten the swivel nut.
6. **ADJUST NEUTRAL START SWITCH**
   - If the engine will start with the shift selector in any range other than N or P range, adjustment is required.
   1. Loosen the neutral start switch bolts and set the shift selector to the N range.
   2. Align the groove and neutral basic line.
   3. Hold in position and tighten the bolts.
      - Torque: **55 kg-cm (48 in.-lb, 5.4 N·m)**
7. **INSPECT IDLE SPEED (N RANGE)**
   - Idle speed: **800 rpm**

### Manual Shifting Test

> **NOTE:** With this test, it can be determined whether the trouble lies within the electrical circuit or is a mechanical problem in the transmission.

1. **DISCONNECT ECT COMPUTER CONNECTOR**
   1. Remove the luggage compartment panel.
   2. With the engine OFF, disconnect the ECT connector.
2. **INSPECT MANUAL DRIVING OPERATION**
   - Check that the shift and gear positions correspond with the table below.

   | Shift position | D range | 2 range | L range | R range | P range |
   |---|---|---|---|---|---|
   | Gear position | OD | 3rd | 1st | Reverse | Pawl Lock |

   - If the L, 2 and D range gear positions are difficult to distinguish, do not perform the following road test.
     1. While driving, shift through the L, 2 and D ranges and back up again. Check that the gear change corresponds to the gear position.
     2. While driving, shift through the D, 2 and L ranges and back down again. Check that the gear change corresponds to the gear position.
   - If any abnormality is found in the above tests, do not perform the stall, time lag or gear change tests.
3. **CONNECT ECT COMPUTER CONNECTOR**
   1. Connect the ECT computer connector.
   2. Install the center cluster.

### Stall Test

The object of this test is to check the overall performance of the transmission and engine by measuring the maximum engine speeds in D and R ranges.

> **CAUTION:**
> - Perform the test at normal operating fluid temperature (50 – 80°C or 122 – 176°F).
> - Do not continuously run this test longer than 5 seconds.

**MEASURE STALL SPEED**

1. Chock the front and rear wheels.
2. Mount an engine tachometer.
3. Fully apply the parking brake.
4. Step down strongly on the brake pedal with your left foot.
5. Start the engine.
6. Shift into D range. Step all the way down on the accelerator pedal with your right foot. Quickly read the highest engine rpm at this time.
   - Stall speed:

   | Application | Stall speed |
   |---|---|
   | A240E/4A-GE | 2,150 ± 150 rpm |
   | A241E/4A-GZE | 2,650 ± 150 rpm |

7. Perform the same test in R range.

**EVALUATION**

- If the engine speed is the same for both ranges but lower than specified value:
  - Engine output may be insufficient.
  - Stator one-way clutch is not operating properly.
- If the stall speed in D range is higher than specified:
  - Line pressure too low
  - Forward clutch slipping
  - One-way clutch No. 2 not operating properly
  - UD one-way clutch not operating properly
- If the stall speed in R range is higher than specified:
  - Line pressure too low
  - Direct clutch slipping
  - First and reverse brake slipping
  - UD brake slipping
- If the stall speed in R and D ranges is higher than specified:
  - Line pressure too low
  - Improper fluid level
  - UD brake slipping

### Time Lag Test

If the shift lever is shifted while the engine is idling, there will be a certain time elapse or lag before the shock can be felt. This is used for checking the condition of the OD clutch, forward clutch, direct clutch and first and reverse brake.

> **CAUTION:**
> - Perform the test at normal operating fluid temperature (50 – 80°C or 122 – 176°F).
> - Be sure to allow one minute interval between tests.
> - Make three measurements and take the average value.

**MEASURE TIME LAG**

1. Fully apply the parking brake.
2. Start the engine and check the idle speed.
   - Idling speed: **800 rpm**
3. Shift the shift lever from N to D range. Using a stop watch, measure the time it takes from shifting the lever until the shock is felt.
   - Time lag (N → D): **Less than 1.2 seconds**
4. In the same manner, measure the time lag for N → R.
   - Time lag (N → R): **Less than 1.5 seconds**

**EVALUATION**

- If N → D time lag is longer than specified:
  - Line pressure too low
  - Forward clutch worn
  - No. 2 and UD one-way clutch not operating properly
- If N → R time lag is longer than specified:
  - Line pressure too low
  - Direct clutch worn
  - First and reverse brake worn
  - UD brake worn

### Hydraulic Test

1. **PREPARATION**
   1. Warm up the transmission fluid.
   2. Remove the transmission case test plug and mount the hydraulic pressure gauge.
      - **SST 09992-00094** Oil pressure gauge
   > **CAUTION:** Perform the test at normal operating fluid temperature (50 – 80°C or 122 – 176°F).
2. **MEASURE LINE PRESSURE**
   1. Fully apply the parking brake and chock the four wheels.
   2. Start the engine and check the idling rpm.
   3. Shift into D range, step down strongly on the brake pedal with your left foot and, while manipulating the accelerator pedal with the right foot, measure the line pressure at the engine speeds specified in the table.
   4. In the same manner, perform the test in R range.
   5. If the measured pressures are not up to specified values, recheck the throttle cable adjustment and retest.

**Line pressure — kg/cm² (psi, kPa):**

| Engine / ATM | D range — Idling | D range — Stall | R range — Idling | R range — Stall |
|---|---|---|---|---|
| A240E/4A-GE | 3.7 – 4.3 (53 – 61, 363 – 422) | 9.2 – 10.7 (131 – 152, 902 – 1,049) | 5.4 – 7.2 (77 – 102, 530 – 706) | 14.4 – 16.8 (205 – 239, 1,412 – 1,648) |
| A241E/4A-GZE | 3.7 – 4.3 (53 – 61, 363 – 422) | 9.2 – 10.7 (131 – 152, 902 – 1,049) | 6.3 – 8.1 (90 – 115, 618 – 794) | 15.9 – 19.3 (226 – 274, 1,559 – 1,893) |

**EVALUATION**

- If the measured values at all ranges are higher than specified:
  - Throttle cable out of adjustment
  - Throttle valve defective
  - Regulator valve defective
- If the measured values at all ranges are lower than specified:
  - Throttle cable out of adjustment
  - Throttle valve defective
  - Regulator valve defective
  - Oil pump defective
  - UD one-way clutch not operating properly
- If pressure is low in D range only:
  - D range circuit fluid leakage
  - Forward clutch defective
  - UD one-way clutch not operating properly
- If pressure is low in R range only:
  - R range circuit fluid leakage
  - Direct clutch defective
  - First and reverse brake defective
  - UD one-way clutch not operating properly

### Road Test

> **CAUTION:** Perform the test at normal operating fluid temperature (50 – 80°C or 122 – 176°F).

1. **D RANGE TEST IN NORM AND PWR PATTERN RANGES**
   - Shift into the D range and hold accelerator pedal constant at 50% and 100% throttle valve opening positions. Push in one of the pattern selection buttons with the OD switch ON and check the following:
   1. 1-2, 2-3, 3-OD and lock-up up-shifts should take place, and shift points should conform to those shown in the automatic shift diagram.
      > **NOTE:**
      > 1. There is no OD up-shift when coolant temperature is below 50°C (122°F).
      > 2. There is no lock-up when the vehicle speed is 10 km/h (6 mph) less than the set cruise control speed.

      **EVALUATION**
      1. If there is no 1 → 2 up-shift: No. 2 solenoid is stuck; 1-2 shift valve is stuck.
      2. If there is no 2 → 3 up-shift: No. 1 solenoid is stuck; 2-3 shift valve is stuck.
      3. If there is no 3 → OD up-shift (throttle valve opening 1/2): 3-OD shift valve is stuck.
      4. If the shift point is defective: throttle valve, 1-2 shift valve, 2-3 shift valve, 3-OD shift valve, etc., are defective.
      5. If the lock-up is defective: No. 3 solenoid is stuck; lock-up relay valve is stuck.
   2. In the same manner, check the shock and the slip at 1-2, 2-3 and 3-OD up-shifts.
      > **EVALUATION** — If the shock is severe: line pressure is too high; accumulator is defective; check ball is defective.
   3. Run in the OD gear of the D range and, with the lock-up in operation, check for abnormal noise and vibration.
      > **NOTE:** Check for cause of abnormal noise and vibration must be made with extreme care as they could also be due to unbalance in the drive shaft, differential, tire, torque converter, etc., or insufficient bending rigidity, etc., in the power train.
   4. While running in the D range 2nd, 3rd gears and OD, check to see that the possible kick-down vehicle speed limits for 2-1, 3-2, OD-3 and OD-2 kick-downs conform to those indicated on the automatic shift diagram.
   5. Check for abnormal shock and slip at kick-down.
   6. While running about 80 km/h (50 mph) in the D range OD gear, shift into the 2 and L ranges and check the engine braking effect at each of these ranges.
      > **EVALUATION**
      > 1. If there is no engine braking effect at the 2 range: **3rd Gear** — second brake is defective; **2nd Gear** — second brake and second coast brake are defective.
      > 2. If there is no engine braking effect at the L range: **2nd Gear** — second brake and second coast brake are defective; **1st Gear** — first and reverse brake are defective.
   7. While running in the D range, release your foot from the accelerator pedal and shift into the L range. Then check to see if OD-3, 3-2 and 2-1 down-shift points conform to those indicated on the automatic shift diagram.
2. **INSPECT LOCK-UP MECHANISM**
   1. Connect a voltmeter to service connector terminals ECT and E1.
   2. Select the normal pattern.
   3. Drive at around 50 km/h (31 mph) to where 7, 5 or 3 volts appears on the voltmeter (this is the lock-up range).
   4. Depress the accelerator pedal and read the tachometer. If there is a big jump in engine rpm there is no lock-up.
3. **2 RANGE TEST**
   - Shift into the 2 range and, while driving with the accelerator pedal held constant at specified point (throttle valve opening 50% and 100%), push in one of the pattern selectors, check on the following points.
   1. At each of the above throttle openings, check to see that 1 → 2 up-shift takes place and also that the shift points conform to those shown on the automatic shift diagram.
      > **NOTE:**
      > - To prevent overrun, the transmission shifts up into 3rd gear at around 130 km/h (81 mph).
      > - In range 2, there will be no lock-up to 2nd gear.
   2. While running in the 2 range, 2nd gear, release the accelerator pedal and check the engine braking effect.
   3. Check for abnormal noise at acceleration and deceleration, and for shock at up-shift and down-shift.
4. **L RANGE TEST**
   1. While running above 80 km/h (50 mph) in the D or 2 range, release your foot from the accelerator pedal and shift into L range. Then check to see that the 2-1 down-shift point conforms to 52 km/h (32 mph).
   2. While running in the L range, check to see that there is no up-shift to 2nd gear.
      > **NOTE:** To prevent overrun, the transmission up-shifts into 2nd gear at around 75 km/h (47 mph).
   3. While running in the L range, release the accelerator pedal and check the engine braking effect.
   4. Check for abnormal noise at acceleration and deceleration.
5. **R RANGE TEST**
   - Shift into the R range and, while starting at full throttle, check for slipping.
6. **P RANGE TEST**
   - Stop the vehicle on a gradient (more than 5°) and after shifting into the P range, release the parking brake. Then check to see that the parking lock pawl holds the vehicle in place.

*(Figure: ECT electronic control system wiring diagram — see page image p.534, source page AT-15/AT-16.)*

### Troubleshooting of Electronic Control System

> **NOTE:**
> - If diagnostic code Nos. 42, 61, 62 or 63 occur, the overdrive indicator light will begin to blink immediately to warn the driver. However, an impact or shock may cause the blinking to stop; but the code will still be retained in the ECT computer memory until canceled out.
> - There is no warning for diagnostic code No. 64.
> - In the event of a simultaneous malfunction of both No. 1 and No. 2 speed sensors, no diagnostic code will appear and the fail-safe system will not function. However, when driving in the D range, the transmission will not up-shift from first gear, regardless of the vehicle speed.

#### Trouble No. 1 — Blinking overdrive indicator light (while driving)

| Step | Check | Result | Next action / Conclusion |
|---|---|---|---|
| 1 | Read diagnostic code (see AT-23) | Code Nos. 42, 61 | Faulty speed sensor circuit; faulty speed sensor |
| 1 | Read diagnostic code (see AT-23) | Code Nos. 62, 63, 64 | Go to step 2 |
| 2 | Disconnect ECT computer connector and check there is 11 – 15 Ω between connector terminals S1, S2, SL – GND | No | Faulty solenoid circuit; faulty solenoid |
| 2 | (as above) | Yes | Try another ECT computer |

#### Trouble No. 2 — No shifting

Warm up engine — Coolant temp: 80°C (176°F); ATF temp: 50 – 80°C (122 – 176°F).

| Step | Check | Result | Next action / Conclusion |
|---|---|---|---|
| 1 | Read diagnostic code (see AT-23) | Malfunction code(s) | Proceed to Trouble No. 1 (AT-17) |
| 1 | (as above) | Normal code | Go to step 2 |
| 2 | Connect a voltmeter to service connector terminals ECT and E1. Does terminal ECT voltage vary with changes in throttle opening? | Yes | Go to step 4 |
| 2 | (as above) | No | Go to step 3 |
| 3 | Is voltage between ECT computer terminals BK and GND as follows? (0V: brake pedal released; 12V: brake pedal depressed) | No | Brake signal faulty |
| 3 | (as above) | Yes | Computer power source and ground faulty; throttle position signal faulty; terminal ECT wire open or short |
| 4 | Disconnect ECT computer connector and road test. Does the transmission operate in the respective gear when in the following ranges while driving? (D range → Overdrive; 2 range → 3rd gear; L range → 1st gear) | No | Transmission faulty |
| 4 | (as above) | Yes | Continue to step 5 (page AT-19) |
| 5 | Connect ECT computer connector and road test. Does terminal ECT voltage rise from 0V to 7V in sequence? | 0 → 7V | Transmission faulty; solenoid faulty |
| 5 | (as above) | 0 → 5V | Proceed to Trouble No. 4 (AT-21) |
| 5 | (as above) | 0 → 3V | Go to step 6 |
| 5 | (as above) | 0V | Go to step 7 |
| 6 | Are there 12V between ECT computer terminals 2 – GND when in the D range? | Yes | Neutral start switch circuit faulty; neutral start switch faulty |
| 6 | (as above) | No | Try another ECT computer |
| 7 | Are there 12V between ECT computer terminals L – GND when in the D range? | Yes | Neutral start switch circuit faulty; neutral start switch faulty |
| 7 | (as above) | No | Try another ECT computer |

#### Trouble No. 3 — Shift point too high or too low

Warm up engine — Coolant temp: 80°C (176°F); ATF temp: 50 – 80°C (122 – 176°F).

| Step | Check | Result | Next action / Conclusion |
|---|---|---|---|
| 1 | Read diagnostic code (see AT-23) | Malfunction code(s) | Proceed to Trouble No. 1 (AT-17) |
| 1 | (as above) | Normal code | Go to step 2 |
| 2 | Connect a voltmeter to service connector terminals ECT and E1. Does terminal ECT voltage vary with changes in throttle opening? | Yes | Go to step 4 |
| 2 | (as above) | No | Go to step 3 |
| 3 | Is voltage between ECT computer terminals BK and GND as follows? (0V: brake pedal released; 12V: brake pedal depressed) | No | Brake signal faulty |
| 3 | (as above) | Yes | Computer power source and ground faulty; throttle position signal faulty; terminal ECT wire open or short |
| 4 | Check voltage between ECT computer terminals PWR and GND. (Power pattern: 12V; Normal pattern: 1V) | OK | Faulty ECT computer; faulty transmission |
| 4 | (as above) | No | Faulty pattern select switch system |

#### Trouble No. 4 — No up-shift to overdrive (after warm-up)

| Step | Check | Result | Next action / Conclusion |
|---|---|---|---|
| 1 | Road test while shifting manually with ECT computer connector pulled out. Is there overdrive up-shift in the D range when shifting from L to 2 to D? | No | Faulty transmission |
| 1 | (as above) | Yes | Go to step 2 |
| 2 | Connect ECT computer connector, and while driving does terminal ECT voltage rise from 0V to 7V in sequence? | 0 → 7V | Faulty transmission; faulty solenoid |
| 2 | (as above) | 0 → 5V | Go to step 5 |
| 2 | (as above) | 0 → 3V | Go to step 4 |
| 2 | (as above) | 0V | Go to step 3 |
| 3 | Are there 12V between ECT computer terminals L and GND when in the D range? | No | Try another ECT computer |
| 3 | (as above) | Yes | Faulty neutral start switch circuit; faulty neutral start switch |
| 4 | Are there 12V between ECT computer terminals 2 and GND when in D range? | Yes | Faulty neutral start switch circuit; faulty neutral start switch |
| 4 | (as above) | No | Try another ECT computer |
| 5 | Is voltage between terminals OD2 and GND as follows? (OD switch turn ON: 12V; OD switch turn OFF: 0V) | No | Faulty OD switch harness; faulty OD switch; OD off light open |
| 5 | (as above) | Yes (check OD cutout signal) | Go to step 6 |
| 6 | Is voltage between terminals OD1 and GND as follows? Approx. 5V (Denso) or 12V (Aisin) — coolant temp. above 50°C or 122°F | Yes | Try another ECT computer |
| 6 | (as above) | No (check OD cutout signal) | Go to step 7 |
| 7 | Is voltage between ECT computer terminals OD1 and GND normal with the cruise control computer connector pulled out? | Yes | Faulty cruise control computer |
| 7 | (as above) | No | Faulty engine ECU (short circuit in ECT wire harness or EFI water temp. sensor bad) |

#### Trouble No. 5 — No lock-up (after warm-up)

Warm up engine — Coolant temp.: 80°C (176°F); ATF temp.: 50 – 80°C (122 – 176°F).

| Step | Check | Result | Next action / Conclusion |
|---|---|---|---|
| 1 | Read diagnostic code (see AT-23) | Malfunction code(s) | Proceed to Trouble No. 1 (AT-17) |
| 1 | (as above) | Normal code | Go to step 2 |
| 2 | Road test. Connect a voltmeter to service connector terminals ECT and E1. Is there 7, 5 or 3V in the lock-up range while driving? | Yes | Lock-up solenoid stuck; faulty transmission; faulty lock-up mechanism |
| 2 | (as above) | No | Go to step 3 |
| 3 | Is voltage between ECT computer BK and GND terminals as follows? (Brake pedal depressed: 12V; brake pedal released: 0V) | No | Faulty brake signal |
| 3 | (as above) | Yes | Faulty computer power source and ground; faulty throttle position signal |

### Read of Diagnostic Code

1. **TURN IGNITION SWITCH AND OD SWITCH TO ON**
   - Do not start engine.
   > **NOTE:** Warning and diagnostic code can be read only when the overdrive switch is ON. If OFF, the overdrive light will light continuously and will not blink.
2. **SHORT DG TERMINAL CIRCUIT**
   - Using a service wire, short the terminals ECT and E1.
3. **READ DIAGNOSTIC CODE**
   - Read the diagnostic code as indicated by the number of times the OD "OFF" light flashes.
4. **DIAGNOSTIC CODE**
   1. If the system is operating normally, the light will blink for 0.25 seconds every 0.5 seconds.
   2. In the event of a malfunction, the light will blink for 0.5 seconds every 1.0 seconds. The number of blinks will equal the first number and, after 1.5 second pause, the second number of the two-digit diagnostic code. If there are two or more codes, there will be a 2.5 second pause between each.
   > **NOTE:** In the event of several trouble codes occurring simultaneously, indication will begin from the smaller value and continue to the larger.
   3. Remove the service wire from the DG terminal.

**Diagnostic Code** *(light pattern is a pulse-train waveform per code — see page image p.542):*

| Code No. | Diagnosis System |
|---|---|
| 42 | Defective No. 1 speed sensor (in combination meter) — severed wire harness or short circuit |
| 61 | Defective No. 2 speed sensor (in ATM) — severed wire harness or short circuit |
| 62 | Severed No. 1 solenoid or short circuit — severed wire harness or short circuit |
| 63 | Severed No. 2 solenoid or short circuit — severed wire harness or short circuit |
| 64 | Severed lock-up solenoid or short circuit — severed wire harness or short circuit |

> **NOTE:** If codes 62, 63 and 64 appear, there is an electrical malfunction in the solenoid. Causes due to mechanical failure, such as a stuck switch, will not appear.

### Cancel Out Diagnostic Code

1. After repair of the trouble area, the diagnostic code retained in memory by the ECT computer must be canceled by removing the fuse AM2 (7.5A) for 10 seconds or more, depending on ambient temperature (the lower the temperature, the longer the fuse must be left out) with the ignition switch off.
   > **NOTE:**
   > - Cancellation can also be done by removing the battery negative (–) terminal, but in this case other memory systems (clock, radio ETR, etc.) will also be cancelled out.
   > - The diagnostic code can also be cancelled out by disconnecting the ECT computer connector.
   > - If the diagnostic code is not cancelled out, it will be retained by the ECT computer and appear along with a new code in event of future trouble.
2. After cancellation, perform a road test to confirm that a "normal code" is now read on the OD "OFF" light.

### Inspect Terminal ECT Voltage

1. **INSPECT THROTTLE POSITION SENSOR SIGNAL**
   1. Turn the ignition switch to ON. Do not start the engine.
   2. Connect a voltmeter to the terminals ECT and E1 of the service connector.
   3. While slowly depressing the accelerator pedal, check that terminal ECT voltage rises in sequence.
   - If the voltage is in proportion to the throttle opening angle and does not change, there is a malfunction with the throttle position sensor or circuit.
2. **INSPECT BRAKE SIGNAL**
   1. Depress the accelerator pedal until the terminal ECT indicates 8V.
   2. Depress the brake pedal and check the voltage reading from the terminal ECT.
      - Brake pedal depressed: **0V**
      - Brake pedal released: **8V**
   - If not as indicated, there is a malfunction in either the stop light switch or circuit.
3. **INSPECT EACH UP SHIFT POSITION**
   1. Warm up the engine. Coolant temperature: **80°C (176°F)**
   2. Turn the OD switch to "ON".
   3. Place the pattern select switch in "Normal" and the shift selector into the D range.
   4. During a road test (above 10 km/h or 6 mph) check that voltage at the terminal ECT is as indicated below for each up-shift position.
   5. If the voltage rises from 0V to 7V in the sequence shown, the control system is okay.
   6. The voltage could rise anywhere between 0V – 8V before the vehicle reaches 10 km/h (6 mph); the voltmeter indicates the current gear.
      > **NOTE:** Determine the gear position by a light shock or change in engine rpm when shifting.

   | Terminal ECT (V) | Gear position |
   |---|---|
   | 0 | 1st |
   | 2 | 2nd |
   | 3 | 2nd Lock-up |
   | 4 | 3rd |
   | 5 | 3rd Lock-up |
   | 6 | OD |
   | 7 | OD Lock-up |

### Inspection of Electronic Control Components

1. **INSPECT VOLTAGE OF ECT COMPUTER CONNECTOR**
   1. Remove the luggage compartment panel.
   2. Turn on the ignition switch.
   3. Measure the voltage at each terminal.

In the tables below, "←" means the AISIN-type value is the same as the DENSO-type value in the same row.

| Terminal | Measuring condition | DENSO type computer — Voltage (V) | AISIN type computer — Voltage (V) |
|---|---|---|---|
| L1 – GND | Throttle valve fully closed | 5 | 12 |
| L1 – GND | Throttle valve fully closed to fully open | 5 to 0 | 12 to 0 |
| L1 – GND | Throttle valve fully open | 0 | ← |
| L2 – GND | Throttle valve fully closed | 5 | 12 |
| L2 – GND | Throttle valve fully closed to fully open | 5 to 0 to 5 | 12 to 0 to 12 |
| L2 – GND | Throttle valve fully open | 5 | 12 |
| L3 – GND | Throttle valve fully closed | 5 | 12 |
| L3 – GND | Throttle valve fully closed to fully open | 5 to 0 to 5 to 0 to 5 | 12 to 0 to 12 to 0 to 12 |
| L3 – GND | Throttle valve fully open | 5 | 12 |
| IDL – GND | Throttle valve fully closed | 0 | ← |
| IDL – GND | Throttle valve opening above 1.5° | 12 | ← |
| SP1 – GND | Standing still (Cruise control OFF) | 5 or 0 | 12 or 0 |
| SP1 – GND | Vehicle moving (Cruise control OFF) | 2.5 | 6 |
| BR – GND | When brake pedal is depressed | 12 | ← |
| BR – GND | When brake pedal is not depressed | 0 | ← |
| 2 – GND | 2 range | 10 – 16 | ← |
| 2 – GND | Except 2 range | 0 – 2 | ← |
| L – GND | L range | 10 – 16 | ← |
| L – GND | Except L range | 0 – 2 | ← |
| N – GND | N range | 10 – 16 | ← |
| N – GND | Except N range | 0 – 2 | ← |
| S1 – GND | — | 12 | ← |
| S2, SL – GND | — | 0 | ← |
| OD1 – GND | Coolant temp. below 50°C (122°F) | 0 | ← |
| OD1 – GND | Coolant temp. above 50°C (122°F) | 5 | 12 |
| OD2 – GND | OD main switch turned ON | 12 | 12 |
| OD2 – GND | OD main switch turned OFF | 0 | ← |
| IG – GND | Ignition switch ON | 12 | ← |
| SP2 – GND | Standing still | 5 or 0 | ← |
| SP2 – GND | Vehicle moving | 4 | ← |
| PWR – GND | PWR pattern | 12 | ← |
| PWR – GND | NORM pattern | 0 to 2 | ← |
| +B – GND | — | 12 | ← |

2. **INSPECT SOLENOID**
   1. Disconnect the connector from the ECT computer.
   2. Measure the resistance between S1, S2, SL and ground.
      - STD: **11 – 15 Ω**
   3. Apply battery voltage to the solenoid. Check that an operation noise can be heard from the solenoid.
   > **NOTE:** If there is foreign matter in the solenoid valve, there will be no fluid control even with solenoid operation.
3. **INSPECT NEUTRAL START SWITCH**
   - Inspect that there is continuity between terminals L–C, 2–C and N–C.

   | Shift position | Continuity |
   |---|---|
   | N range | N – C |
   | 2 range | 2 – C |
   | L range | L – C |

4. **INSPECT THROTTLE POSITION SENSOR**
   - Using an ohmmeter, check the resistance between each terminal.

   | Terminal | Throttle valve condition | Resistance (kΩ) |
   |---|---|---|
   | IDL – E2 | Fully closed | 0 – 0.1 |
   | IDL – E2 | Open | Infinity |
   | Vc – E2 | — | 3 – 7 |
   | VTA – E2 | Fully closed | 0.2 – 0.8 |
   | VTA – E2 | Fully open | 3.3 – 10 |

5. **INSPECT SPEED SENSOR IN ATM**
   1. Jack up a rear wheel on one side.
   2. Connect an ohmmeter between the terminals.
   3. Spin the wheel and check that the meter needle deflects from 0 to ∞ Ω.
6. **INSPECT SPEED SENSOR IN COMBINATION METER**
   1. Remove the combination meter.
   2. Connect an ohmmeter between the terminals SPD and GND.
   3. Revolve the meter shaft and check that the meter needle repeatedly deflects from 0 to ∞ Ω.
7. **INSPECT PATTERN SELECTION SWITCH**
   - Inspect that there is continuity between 5 and each terminal.
   > **NOTE:** As there are diodes inside, be careful of the tester probe polarity.

   | Position | Continuity |
   |---|---|
   | NORM | 5 – 4 |
   | PWR | 5 – 3 |

8. **INSPECT OD SWITCH**
   - Inspect that there is continuity between terminals 1 and 3.

   | Position | Continuity |
   |---|---|
   | ON | 1 – 3 |
   | OFF | No continuity |

9. **INSPECT LOCK-UP MECHANISM**
   1. Warm up the coolant and ATF.
   2. Connect a voltmeter to the service connector terminals ECT and E1.
   3. Turn the OD switch ON.
   4. Select the normal pattern.
   5. Drive at around 50 km/h (31 mph) to where 7, 5 or 3 volts appears on the voltmeter (this is the lock-up range).
   6. Depress the accelerator pedal and read the tachometer. If there is a big jump in engine rpm there is no lock-up.
10. **INSPECT BRAKE SIGNAL**
    - Check that the brake light comes on when the brake pedal is depressed.

## Operating Mechanism for Each Gear

### 1. Transmission System

Clutch/brake application per gear (○ = operating). Columns C1–C3 are clutches; B1–B4 are brakes; F1–F3 are one-way clutches.

| Shift lever position | Gear position | C1 | C2 | C3 | B1 | B2 | B3 | B4 | F1 | F2 | F3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P | Parking | | | | | | | ○ | | | |
| R | Reverse | | ○ | | | | ○ | ○ | | | |
| N | Neutral | | | | | | | ○ | | | |
| D | 1st | ○ | | | | | | ○ | | ○ | ○ |
| D | 2nd | ○ | | | | ○ | | ○ | ○ | | ○ |
| D | 3rd | ○ | ○ | | | ○ | | ○ | | | ○ |
| D | OD | ○ | ○ | ○ | | ○ | | | | | |
| 2 | 1st | ○ | | | | | | ○ | | ○ | ○ |
| 2 | 2nd | ○ | | | ○ | ○ | | ○ | ○ | | ○ |
| 2 | 3rd | ○ | ○ | | | ○ | | ○ | | | ○ |
| L | 1st | ○ | | | | | ○ | ○ | | ○ | ○ |
| L | 2nd | ○ | | | ○ | ○ | | ○ | ○ | | ○ |

### 2. Solenoid System

Possible gear positions in accordance with solenoid operating conditions. Legend: `( )` = no fail-safe function; `x` = malfunctions.

| Range | Normal — No.1 | Normal — No.2 | Normal — Gear | No.1 Solenoid malfunctioning — No.1 | No.1 — No.2 | No.1 — Gear | No.2 Solenoid malfunctioning — No.1 | No.2 — No.2 | No.2 — Gear | Both Solenoids malfunctioning — No.1 | Both — No.2 | Both — Gear |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D range | ON | OFF | 1st | x | ON (OFF) | 3rd (OD) | ON | x | 1st | x | x | OD |
| D range | ON | ON | 2nd | x | ON | 3rd | OFF (ON) | x | OD (1st) | x | x | OD |
| D range | OFF | ON | 3rd | x | ON | 3rd | OFF | x | OD | x | x | OD |
| D range | OFF | OFF | OD | x | OFF | OD | OFF | x | OD | x | x | OD |
| 2 range | ON | OFF | 1st | x | ON (OFF) | 3rd (OD) | ON | x | 1st | x | x | 3rd |
| 2 range | ON | ON | 2nd | x | ON | 3rd | OFF (ON) | x | 3rd (1st) | x | x | 3rd |
| 2 range | OFF | ON | 3rd | x | ON | 3rd | OFF | x | 3rd | x | x | 3rd |
| L range | ON | OFF | 1st | x | OFF | 1st | ON | x | 1st | x | x | 1st |
| L range | ON | ON | 2nd | x | ON | 2nd | ON | x | 1st | x | x | 1st |

## Automatic Shift Diagram (A240E/4A-GE)

Shift-point speeds in km/h (mph). Bracketed columns `[3→OD]` and `[OD→3]` are for the **fully closed** throttle condition; all other columns are for **fully open** throttle.

| Range | Pattern | 1→2 | 2→3 | 3→OD | [3→OD] | [OD→3] | OD→3 | 3→2 | 2→1 |
|---|---|---|---|---|---|---|---|---|---|
| D range | NORM | 48–53 (30–33) | 93–101 (58–63) | 146–155 (91–96) | 31–35 (19–22) | 20–24 (12–15) | 137–146 (85–91) | 87–95 (54–59) | 43–47 (27–29) |
| D range | PWR | 60–65 (37–40) | 109–117 (68–73) | 177–187 (110–116) | 47–51 (29–32) | 20–24 (12–15) | 169–178 (105–111) | 103–111 (64–69) | 43–47 (27–29) |
| 2 range | NORM / PWR | 60–65 (37–40) | — | — | — | — | — | — | 43–47 (27–29) |
| L range | NORM / PWR | — | — | — | — | — | — | — | 50–54 (31–34) |

**Lock-up (throttle valve opening 5%) — km/h (mph).** `*` = O/D main switch OFF.

| Range | Pattern | Lock-up ON — 2nd | Lock-up ON — 3rd | Lock-up ON — OD | Lock-up OFF — 2nd | Lock-up OFF — 3rd | Lock-up OFF — OD |
|---|---|---|---|---|---|---|---|
| D range | NORM | — | *64–69 (40–43) | 67–72 (42–45) | — | *50–54 (31–34) | 61–66 (38–41) |
| D range | PWR | — | *83–91 (52–57) | 78–83 (48–52) | — | *73–78 (45–48) | 66–70 (41–44) |

> **NOTE:**
> 1. There is no lock-up in the 2 and L ranges.
> 2. In the following cases, the lock-up will be released regardless of the lock-up pattern:
>    - When the throttle is completely closed.
>    - When the brake light switch is ON.

*(Figures: D range NORM/PWR, 2 range NORM/PWR and L range NORM/PWR shift-point graphs — see page images p.550–551, source pages AT-32/AT-33.)*

## Automatic Shift Diagram (A241E/4A-GZE)

Shift-point speeds in km/h (mph). Bracketed columns `[3→OD]` and `[OD→3]` are for the **fully closed** throttle condition; all other columns are for **fully open** throttle.

| Range | Pattern | 1→2 | 2→3 | 3→OD | [3→OD] | [OD→3] | OD→3 | 3→2 | 2→1 |
|---|---|---|---|---|---|---|---|---|---|
| D range | NORM | 46–50 (29–31) | 88–96 (55–60) | 132–140 (82–87) | 30–35 (19–22) | 19–23 (12–14) | 126–134 (78–83) | 82–90 (51–56) | 42–46 (26–29) |
| D range | PWR | 51–56 (32–35) | 95–103 (59–64) | 150–159 (93–99) | 40–46 (25–29) | 19–23 (12–14) | 143–152 (89–94) | 89–97 (55–60) | 42–46 (26–29) |
| 2 range | NORM / PWR | 51–56 (32–35) | — | — | — | — | — | — | 42–46 (26–29) |
| L range | NORM / PWR | — | — | — | — | — | — | — | 46–50 (29–31) |

**Lock-up (throttle valve opening 5%) — km/h (mph).** `*` = O/D main switch OFF.

| Range | Pattern | Lock-up ON — 2nd | Lock-up ON — 3rd | Lock-up ON — OD | Lock-up OFF — 2nd | Lock-up OFF — 3rd | Lock-up OFF — OD |
|---|---|---|---|---|---|---|---|
| D range | NORM | — | *66–70 (41–43) | 54–59 (34–37) | — | *60–65 (37–40) | 51–56 (32–35) |
| D range | PWR | — | *103–112 (64–70) | 81–89 (50–55) | — | *95–103 (59–64) | 77–82 (48–51) |

> **NOTE:**
> 1. There is no lock-up in the 2 and L ranges.
> 2. In the following cases, the lock-up will be released regardless of the lock-up pattern:
>    - When the throttle is completely closed.
>    - When the brake light switch is ON.

*(Figures: D range NORM/PWR, 2 range NORM/PWR and L range NORM/PWR shift-point graphs — see page images p.554–556, source pages AT-35/AT-36.)*

## On-Vehicle Repair

### Removal of Speed Sensor

1. **(A241E/4A-GZE) REMOVE INTERCOOLER** — Disconnect the two hose clamps, and remove the four bolts and intercooler.
2. **REMOVE AIR FLOW METER AND AIR CLEANER HOSE**
3. **DISCONNECT SPEED SENSOR CONNECTOR**
4. **REMOVE RETAINING PLATE**
5. **REMOVE SPEED SENSOR AND O-RING**

### Inspection of Speed Sensor

**INSPECT SPEED SENSOR**

1. Connect an ohmmeter between the terminals.
2. Bring a magnet close to then away from the sensor tip and check that the meter needle deflects from 0 to ∞ Ω.

### Installation of Speed Sensor

1. **INSTALL AND COAT NEW O-RING WITH ATF**
2. **INSTALL SPEED SENSOR**
3. **INSTALL RETAINING PLATE**
4. **CONNECT SPEED SENSOR CONNECTOR**
5. **INSTALL AIR FLOW METER AND AIR CLEANER HOSE**
6. **(A241E/4A-GZE) INSTALL INTERCOOLER** — Connect the two hose clamps, and install the four bolts and intercooler.

### Removal of Throttle Cable

1. **DISCONNECT THROTTLE CABLE**
   1. Disconnect the cable housing from the bracket.
   2. Disconnect the cable from the throttle linkage.
   3. Disconnect the cable from the clamps.
2. **REMOVE NEUTRAL START SWITCH**
   1. Remove the clips, and disconnect the transmission control cable from manual shift lever.
   2. Remove the manual shift lever.
   3. Remove the neutral start switch.
3. **REMOVE VALVE BODY** (see [Removal of Valve Body](#removal-of-valve-body))
4. **PULL THROTTLE CABLE OUT OF TRANSMISSION CASE**
   1. Remove the bolt and retaining plate.
   2. Pull the cable out of the transmission case.

### Installation of Throttle Cable

1. **INSTALL CABLE IN TRANSMISSION CASE**
   1. Be sure to push it in all the way.
   2. Install the retaining plate and one bolt.
2. **INSTALL VALVE BODY** (see [Installation of Valve Body](#installation-of-valve-body))
3. **IF THROTTLE CABLE IS NEW, STAKE STOPPER TO INNER CABLE**
   1. Bend the cable so there is a radius of about 200 mm (7.87 in.).
   2. Pull the inner cable lightly until a slight resistance is felt, and hold it.
   3. Stake the stopper 0.8 – 1.5 mm (0.031 – 0.059 in.) from the outer cable as shown.
4. **CONNECT THROTTLE CABLE**
   1. Connect the cable to the throttle linkage.
   2. Connect the cable housing to the bracket.
   3. Connect the cable to the clamps.
5. **ADJUST THROTTLE CABLE** (see [Preliminary Check, step 4](#preliminary-check))
6. **INSTALL NEUTRAL START SWITCH**
   1. Install the neutral start switch.
   2. Install the manual shift lever.
   3. Adjust the neutral start switch (see [Preliminary Check, step 6](#preliminary-check)).
   4. Connect the transmission control cable.
7. **TEST DRIVE VEHICLE**

### Removal of Valve Body

1. **CLEAN TRANSMISSION EXTERIOR** — To help prevent contamination, clean the exterior of the transmission.
2. **DRAIN TRANSMISSION FLUID** — Remove the drain plug and drain the fluid into a suitable container.
3. **REMOVE OIL PAN, AND GASKET**
   > **CAUTION:** Some fluid will remain in the oil pan.
   - Remove all pan bolts, and carefully remove the pan assembly. Discard the gasket.
4. **REMOVE OIL STRAINER** — Remove the three bolts, and the oil strainer.
   > **CAUTION:** Be careful as some oil will come out with the filter.
5. **REMOVE APPLY TUBE BRACKET**
6. **REMOVE TUBE CLAMP**
7. **REMOVE OIL TUBES** — Pry up both tube ends with a large screwdriver and remove the five tubes.
8. **DISCONNECT SOLENOID CONNECTORS**
9. **REMOVE MANUAL DETENT SPRING**
10. **REMOVE VALVE BODY**
    1. Remove the twelve bolts.
    2. Disconnect the throttle cable from the cam.
    3. Disconnect the manual valve connecting rod and remove the valve body.
11. **REMOVE SECOND BRAKE APPLY GASKET**

**DISASSEMBLY OF VALVE BODY** — see [Valve Body](12b-automatic-transmission-a240e-a241e-part-2.md) (AT-96, Part 2).

### Installation of Valve Body

1. **INSTALL SECOND BRAKE APPLY GASKET**
2. **PLACE VALVE BODY ON TRANSMISSION**
   1. Connect the manual valve connecting rod.
   2. While holding the cam down with your hand, slip the cable end into the slot.
   3. Bring valve body into place.
   > **CAUTION:** Be careful not to entangle the solenoid wire.
3. **INSTALL BOLTS IN VALVE BODY**
   > **NOTE:** Each bolt length (mm) is indicated in the figure. Finger tighten all the bolts first. Then tighten them with a torque wrench.
   - Torque: **100 kg-cm (7 ft-lb, 10 N·m)**
4. **CONNECT SOLENOID WIRING**
5. **INSTALL DETENT SPRING**
   1. Finger tighten the bolt first. Then tighten it.
      - Torque: **100 kg-cm (7 ft-lb, 10 N·m)**
   2. Check that the manual valve lever is in contact with the center of the roller at the tip of the detent spring.
6. **INSTALL OIL TUBES** — Tap the tubes into the positions indicated in the figure with a plastic hammer.
   > **CAUTION:** Be careful not to bend or damage the tubes.
7. **INSTALL TUBE CLAMP**
8. **INSTALL APPLY TUBE BRACKET** — Each bolt length (mm) is indicated in the figure.
9. **INSTALL OIL STRAINER** — Each bolt length (mm) is indicated in the figure.
   - Torque: **100 kg-cm (7 ft-lb, 10 N·m)**
10. **INSTALL MAGNETS IN PAN AND INSTALL OIL PAN WITH NEW GASKET**
    > **CAUTION:** Make sure that the magnets do not interfere with the oil tubes.
    - Torque: **50 kg-cm (43 in.-lb, 4.9 N·m)**
11. **INSTALL DRAIN PLUG WITH NEW GASKET** — **SST 09043-38100**
    - Torque: **175 kg-cm (13 ft-lb, 17 N·m)**
12. **FILL TRANSMISSION WITH ATF** — Add only about two liters of ATF.
    > **CAUTION:** Do not overfill.
    - Fluid type: **ATF DEXRON® II**
13. **CHECK FLUID LEVEL** (see [Preliminary Check](#preliminary-check))

## Removal of Transaxle

1. **(A241E/4A-GZE) REMOVE INTERCOOLER** — Disconnect the two hose clamps, and remove the four bolts and intercooler.
2. **DISCONNECT NEGATIVE BATTERY TERMINAL**
3. **REMOVE AIR FLOW METER AND AIR CLEANER HOSE**
4. **DISCONNECT SPEED SENSOR CONNECTOR**
5. **DISCONNECT THROTTLE CABLE FROM THROTTLE LINKAGE AND BRACKET**
6. **REMOVE WATER INLET SET BOLTS AND DISCONNECT GROUND STRAP**
7. **REMOVE TRANSMISSION MOUNTING SET BOLT**
8. **RAISE VEHICLE AND DRAIN TRANSAXLE**
9. **REMOVE REAR LH WHEEL**
10. **REMOVE ENGINE UNDER COVER**
11. **DISCONNECT SPEEDOMETER CABLE**
12. **DISCONNECT OIL COOLER HOSES**
13. **DISCONNECT CONTROL CABLE**
    1. Remove the clip.
    2. Remove the retainer.
    3. Disconnect the control cable.
14. **REMOVE CONTROL CABLE BRACKET**
15. **DISCONNECT THE THREE CONNECTORS** — Disconnect the two neutral start switch connectors and the solenoid connector.
16. **REMOVE STARTER MOTOR SET BOLTS**
17. **REMOVE EXHAUST PIPE**
18. **REMOVE STIFFENER PLATE**
19. **REMOVE ENGINE REAR END PLATE**
20. **REMOVE TORQUE CONVERTER MOUNTING BOLTS**
    1. Turn the crankshaft to gain access to each bolt.
    2. Hold the crankshaft pulley bolt with a wrench, remove the six bolts.
21. **REMOVE DRIVE SHAFTS** (See page RA-14)
22. **HOLD ENGINE AND TRANSAXLE WITH TWO JACKS, OR A CHAIN BLOCK AND JACK**
23. **REMOVE TRANSMISSION MOUNTING SET BOLTS**
24. **DISCONNECT FRONT AND REAR MOUNTING**
25. **REMOVE TRANSAXLE HOUSING MOUNTING BOLTS** — Lower the rear end of the transaxle, remove the mounting bolts.
26. **REMOVE TRANSAXLE ASSEMBLY FROM ENGINE** — Making sure that neither the throttle cable nor wire harnesses snag inside the engine compartment, moving the transaxle back and forth, left and right, remove the transaxle from the engine.
27. **REMOVE TORQUE CONVERTER FROM TRANSAXLE**

## Torque Converter

**CLEAN TORQUE CONVERTER**

If the transmission is contaminated, the torque converter and transmission cooler should be thoroughly flushed with Toyota Transmission Cleaner.

**INSPECTION OF TORQUE CONVERTER**

1. **INSERT SST IN END OF TORQUE CONVERTER**
   1. Insert a turning tool in the inner race of the one-way clutch.
   2. Install the stopper so that it fits in the notch of the converter hub and outer race of the one-way clutch.
   - **SST 09350-32013 (09351-32010, 09351-32020)**
2. **TEST ONE-WAY CLUTCH** — With the torque converter positioned upward, the clutch should lock when turned counterclockwise, and should rotate freely and smoothly clockwise. Less than **25 kg-cm (22 in.-lb, 2.5 N·m)** of torque should be required to rotate the clutch. If necessary, clean the converter and retest the clutch. Replace the converter if the clutch still fails the test.
3. **MEASURE TORQUE CONVERTER SLEEVE RUNOUT**
   1. Temporarily mount the torque converter to the drive plate. Set up a dial indicator.
      - Torque: **280 kg-cm (20 ft-lb, 27 N·m)**
      - Runout: **0.30 mm (0.0118 in.) or less**
   - If runout exceeds 0.30 mm (0.0118 in.), try to correct it by reorienting the installation of the converter. If excessive runout cannot be corrected, replace the torque converter.
   > **NOTE:** Mark the position of the converter to ensure correct installation.
   2. Remove the torque converter.
4. **MEASURE DRIVE PLATE RUNOUT AND INSPECT RING GEAR** — Set up a dial indicator and measure the drive plate runout. If runout exceeds 0.20 mm (0.0079 in.) or if the ring gear is damaged, replace the drive plate. If installing a new drive plate, note the orientation of the spacers and tighten the bolts.
   - Torque: **650 kg-cm (47 ft-lb, 64 N·m)**
   - Runout: **0.20 mm (0.0079 in.) or less**

## Oil Pump

### Replacement of Oil Seal

1. **REMOVE OIL SEAL WITH SST** — **SST 09350-32013 (09308-10010)**
2. **INSTALL NEW OIL SEAL**
   1. Apply MP grease to the oil seal lip.
   2. Drive in the oil seal with SST. — **SST 09350-32013 (09351-32140)**

### Replacement of O-Ring

1. **REMOVE OIL PUMP**
   1. Position the transmission with the oil pump facing upward.
   2. Remove the seven bolts.
   3. Pull up the oil pump to where the O-ring can be removed with SST. — **SST 09350-32013 (09351-32061)**
   4. Temporarily install the bolt.
2. **REMOVE O-RING**
3. **INSTALL NEW O-RING**
4. **INSTALL OIL PUMP MOUNTING BOLT** — Tighten the seven bolts uniformly and a little at a time.
   - Torque: **250 kg-cm (18 ft-lb, 25 N·m)**

## Disassembly of Transmission

### Components

*(Figure: Transmission exploded view — sensor rotor/adaptor, speed sensor, sensor cover, transmission housing, governor driven gear, thrust washer, transaxle case, throttle cable, transmission dipstick, oil filler tube, solenoid wire, manual shift lever, neutral start switch, valve body, spring plate, manual valve, detent spring, oil pan/gasket, magnet, oil tube/bracket, brake apply rod, oil seal ring, accumulator pistons/O-rings/covers, B4 accumulator piston, oil gallery cover/gasket/screw/bolt, plate — see page image p.568, source page AT-50.)*

Torque callouts embedded in the exploded view:

| Fastener | Torque |
|---|---|
| Neutral start switch | 70 kg-cm (61 in.-lb, 6.9 N·m) |
| Drain plug | 175 kg-cm (13 ft-lb, 17 N·m) |

Diagram legend: `kg-cm (ft-lb, N·m)` = specified torque; `+` = non-reusable part; `*` = precoated part.

*(Figures: Components (Cont'd) — forward clutch, direct clutch, oil pump thrust washer, bearings, thrust washers, snap rings, 2nd brake drum/gasket, rear planetary ring gear, piston return spring, flange, plate/disc (A241E), parking lock pawl, lock pawl shaft, manual valve shaft/oil seal, manual valve lever, retaining spring, differential drive pinion and output flange, outer races, UD one-way clutch, needle bearing, return spring, O-ring — see page images p.569–570, source pages AT-51/AT-52.)*

### Separate Basic Subassembly

1. **REMOVE THE TWO OIL COOLER PIPES**
2. **REMOVE TRANSMISSION DIPSTICK AND FILLER TUBE**
3. **REMOVE MANUAL SHIFT LEVER**
4. **REMOVE NEUTRAL START SWITCH**
5. **REMOVE THROTTLE CABLE RETAINING PLATE**
6. **REMOVE SOLENOID WIRE RETAINING PLATE**
7. **REMOVE SPEED SENSOR AND SENSOR ROTOR**
   1. Remove the retaining plate and speed sensor.
   2. Remove the two bolts and sensor cover.
   3. Remove the sensor rotor.
   4. Remove the sensor rotor adaptor.
8. **REMOVE PAN AND GASKET**
   1. Remove the eighteen bolts.
   2. Remove the pan by lifting the transmission case.
   > **CAUTION:** Do not turn the transmission over as it will contaminate the valve body with the foreign materials in the bottom of the pan.
   3. Place the transmission on wooden blocks to prevent damage to the pipe.
9. **EXAMINE PARTICLES IN PAN** — Remove the magnet and use it to collect any steel chips. Look carefully at the chips and particles in the pan and on the magnet to anticipate what type of wear you will find in the transmission:
   - Steel (magnetic) ... bearing, gear and plate wear
   - Brass (non-magnetic) ... bushing wear
10. **TURN TRANSMISSION OVER AND REMOVE OIL TUBE BRACKET**
11. **REMOVE OIL STRAINER**
12. **REMOVE OIL TUBES**
    1. Remove the tube clamp bolt.
    2. Pry up both tube ends with a large screwdriver and remove the five tubes.
13. **REMOVE MANUAL DETENT SPRING**
14. **DISCONNECT SOLENOID CONNECTORS**
15. **REMOVE VALVE BODY**
    1. Remove the twelve bolts.
    2. Disconnect the throttle cable from the cam.
    3. Disconnect the manual valve connecting rod from the manual valve lever and remove the valve body.
16. **REMOVE THROTTLE CABLE FROM CASE**
17. **REMOVE SOLENOID WIRE**
18. **REMOVE SECOND BRAKE APPLY GASKET**
19. **REMOVE C3 ACCUMULATOR PISTON AND SPRING** — Using low-pressure compressed air (1 kg/cm², 14 psi or 98 kPa), pop out the piston into a rag. Force air into the hole shown and remove the piston and spring.
20. **REMOVE ACCUMULATOR PISTONS AND SPRINGS**
    1. Loosen the five bolts one turn at a time until the spring tension is released.
    2. Remove the cover and the gasket.
    3. Remove the piston and spring for C1.
    4. Using low-pressure compressed air (1 kg/cm², 14 psi or 98 kPa), pop out piston B2 and C2 into a rag. Force air into the hole shown and remove the piston and springs.
21. **MEASURE PISTON STROKE OF SECOND COAST BRAKE**
    1. Apply a small amount of paint to the piston rod at the point it meets the case as shown in the illustration.
    2. Using SST, measure the piston stroke applying and releasing the compressed air (4 – 8 kg/cm², 57 – 114 psi or 392 – 785 kPa) as shown. — **SST 09240-00020**
       - Piston stroke: **1.5 – 3.0 mm (0.059 – 0.118 in.)**
    - If the piston stroke exceeds the limit, replace the piston rod or brake band.
22. **REMOVE SECOND COAST BRAKE PISTON**
    1. Remove the snap ring.
    2. Remove the cover.
    3. Remove the piston and the outer return spring.
23. **REMOVE OIL PUMP**
    1. Remove the six bolts.
    2. Using SST, pull out the oil pump. — **SST 09350-32013 (09351-32061)**
24. **REMOVE OIL PUMP**
25. **WATCH FOR RACE AND BEARING BEHIND OIL PUMP**
26. **REMOVE DIRECT CLUTCH**
27. **REMOVE FORWARD CLUTCH**
28. **WATCH FOR RACES AND BEARINGS**
29. **REMOVE SECOND COAST BRAKE BAND**
    1. Push the pin with a small screwdriver and remove it from the bolt hole of the oil pump mounting.
    2. Remove the brake band.
30. **REMOVE FRONT PLANETARY RING GEAR WITH BEARING AND RACE**
31. **WATCH FOR RACE AND BEARING ON RING GEAR**
32. **REMOVE FRONT PLANETARY GEAR WITH RACE**
33. **WATCH FOR RACES AND BEARING ON FRONT PLANETARY GEAR**
34. **REMOVE SUN GEAR, SUN GEAR INPUT DRUM AND THRUST WASHER**
35. **REMOVE SECOND BRAKE HUB AND NO.1 ONE-WAY CLUTCH**
36. **REMOVE SECOND COAST BRAKE BAND GUIDE**
37. **REMOVE SNAP RING HOLDING SECOND BRAKE DRUM TO CASE**
38. **REMOVE SECOND BRAKE DRUM** — If the brake drum is difficult to remove, lightly tap it with a wooden block.
39. **REMOVE SECOND BRAKE PISTON RETURN SPRING**
40. **REMOVE PLATES, DISCS, AND FLANGE**
41. **BLOW OUT PISTON WITH COMPRESSED AIR** — Use compressed air to remove the piston.
    > **NOTE:** Hold the piston so it is not horizontal, and blow with the gun slightly away from the oil hole.
42. **REMOVE SECOND BRAKE DRUM SEAL** — Using needle nose pliers, pull out the second brake drum seal.
43. **REMOVE SNAP RING HOLDING NO. 2 ONE-WAY CLUTCH OUTER RACE TO CASE**
44. **REMOVE NO. 2 ONE-WAY CLUTCH AND REAR PLANETARY GEAR WITH THRUST WASHERS**
45. **WATCH FOR THRUST WASHERS OF PLANETARY CARRIER ON BOTH SIDES**
46. **REMOVE REAR PLANETARY RING GEAR AND BEARING**
47. **WATCH FOR RACES AND BEARING ON RING GEAR**
48. **REMOVE SNAP RING HOLDING FLANGE TO CASE**
49. **REMOVE FLANGES, PLATES AND DISCS**
50. **TURN TRANSMISSION CASE AROUND**
51. **REMOVE THE THIRTEEN BOLTS HOLDING TRANSAXLE REAR COVER TO TRANSMISSION CASE**
52. **REMOVE TRANSAXLE REAR COVER AND INTERMEDIATE SHAFT**
    1. Tap on the circumference of the cover with a plastic hammer to remove the cover from the transmission case.
    2. Remove the intermediate shaft if it remains in the transmission.
53. **REMOVE SNAP RING** <!-- NEEDS REVIEW: OCR numbered steps 53–56 as "63, 64, 66, 66"; page image (AT-63) confirms the correct sequence is 53, 54, 55, 56 — corrected from image -->
54. **REMOVE TRANSAXLE HOUSING** — Remove the bolts and transaxle housing.
    > **NOTE:** A240E ... eighteen bolts; A241E ... nineteen bolts
55. **REMOVE DIFFERENTIAL**
56. **REMOVE GOVERNOR DRIVEN GEAR**
    1. Remove the governor driven gear.
    2. Remove the thrust washer.
57. **REMOVE OIL SEALS** — Remove the two oil seals.
58. **REMOVE COUNTER SHAFT LOCK NUTS**
    1. Using a chisel and hammer, unstake the counter shaft lock nut on both sides.
    2. Using SST, remove the lock nut of the driven gear side. — **SST 09330-00021 and 09350-32013 (09351-32031)**
    3. Using SST to hold the driven gear, remove the lock nut on the other side. — **SST 09330-00021 and 09350-32013 (09351-32031, 09351-32170)**
59. **REMOVE COUNTER DRIVEN GEAR** — Using SST, remove the driven gear. — **SST 09350-32013 (09351-32061)**
60. **REMOVE THRUST NEEDLE BEARING**
61. **REMOVE COUNTER SHAFT ASSEMBLY AND ANTI-RATTLE CLIP**
62. **REMOVE THRUST BEARING WITH RACE**
63. **REMOVE UNDERDRIVE CLUTCH DRUM**
64. **REMOVE SNAP RING**
    > **CAUTION:** The snap ring is cushioned by a return spring, so when removing be careful that it does not fly off.
65. **REMOVE FLANGE, PLATES AND DISCS**
66. **REMOVE BRAKE RETURN SPRING**
67. **REMOVE UNDERDRIVE BRAKE PISTON** — Using low-pressure compressed air (1 kg/cm², 14 psi or 98 kPa), pop out the brake piston into a rag. Force air into the hole shown and remove the brake piston.
68. **REMOVE PARKING LOCK PAWL STOPPER PLATE, TORSION SPRING AND SPRING GUIDE**
69. **REMOVE PAWL SHAFT CLAMP**
70. **REMOVE PARKING LOCK PAWL SHAFT AND LOCK PAWL**
71. **REMOVE PARKING LOCK SLEEVE**
72. **REMOVE CAM GUIDE BRACKET**
73. **REMOVE MANUAL VALVE SHAFT SPACER** — Unstake the spacer and remove it.
74. **REMOVE PIN** — Using a punch and hammer, drive out the pin.
75. **REMOVE MANUAL VALVE SHAFT AND LEVER**
    1. Remove the retaining spring.
    2. Slide out the manual valve shaft and remove the manual valve lever and washer.
76. **IF NECESSARY, REPLACE OIL SEAL OF MANUAL SHAFT**
    1. Remove the oil seal with a punch.
    2. Drive in a new oil seal.
    3. Apply MP grease to the oil seal lip.
77. **REMOVE OIL SEAL RINGS**
78. **REMOVE OIL GALLERY COVER AND GASKET**
    1. Remove the three screws and six bolts.
    2. Remove the gallery cover and gasket.
79. **REMOVE B4 ACCUMULATOR PISTON AND SPRING**
80. **REMOVE BEARING** — Using SST, remove the bearing. — **SST 09308-00010**
81. **REMOVE THE FOUR OIL TUBE CLAMPS**
82. **REMOVE OIL TUBES WITH SCREWDRIVER**
83. **REMOVE OIL TUBE APPLY COVER AND GASKET**
84. **REMOVE BEARING**
    1. Remove the bearing stopper.
    2. Using SST, remove the bearing. — **SST 09308-00010**

## Component Group Disassembly, Inspection and Assembly

The instructions here are organized so that you work on only one component group at a time. This will help avoid confusion of similar-looking parts from different subassemblies being on your workbench at the same time. As much as possible, complete the inspection, repair and assembly before proceeding to the next component group. If a component group cannot be assembled because parts are being ordered, be sure to keep all parts of that group in a separate container while proceeding with disassembly, inspection, repair and assembly of other component groups. The component groups are inspected and repaired from the converter housing side.

- Recommended ATF: **DEXRON® II**

> **GENERAL CLEANING NOTES:**
> 1. All disassembled parts should be washed clean and the fluid passages and holes blown through with compressed air to make sure that they are not clogged.
> 2. The recommended automatic transmission fluid or kerosene should be used for cleaning.
> 3. When using compressed air to dry parts, keep face away to avoid spraying ATF or kerosene in your face.

> **PARTS ARRANGEMENT:**
> 1. After cleaning, the parts should be arranged in proper order to allow performing inspection, repairs, and reassembly with efficiency.
> 2. When disassembling a valve body, be sure to keep each valve together with the corresponding spring.
> 3. New brakes and clutches that are to be used for replacement must be soaked in transmission fluid for at least two hours before assembly.

> **GENERAL ASSEMBLY:**
> 1. All oil seal rings, clutch discs, clutch plates, rotating parts, and sliding surfaces should be coated with transmission fluid prior to reassembly.
> 2. All gaskets and rubber O-rings should be replaced.
> 3. Make sure that the ends of a snap ring are not aligned with one of the cutouts and are installed in the groove correctly.
> 4. If a worn bushing is to be replaced, the subassembly containing that bushing must be replaced.
> 5. Check thrust bearings and races for wear or damage. Replace if necessary.
> 6. Use petroleum jelly to keep parts in place.

### Oil Pump

*(Figure: Oil pump exploded view — pump body, driven gear, drive gear, O-ring, oil seal ring — see page image p.585, source page AT-71. Legend: `+` = non-reusable part.)*

**DISASSEMBLY OF OIL PUMP**

1. **REMOVE RACE FROM STATOR SHAFT**
2. **REMOVE O-RING FROM PUMP BODY**
3. **REMOVE TWO OIL SEAL RINGS FROM BACK OF STATOR SHAFT**
4. **REMOVE THRUST WASHER OF CLUTCH DRUM FROM STATOR SHAFT**
5. **REMOVE STATOR SHAFT** — Remove the eleven bolts and the stator shaft. Identify the top and bottom. Keep gears in assembly order.

**INSPECTION OF OIL PUMP**

1. **CHECK BODY CLEARANCE OF DRIVEN GEAR** — Push the driven gear to one side of the body. Using a feeler gauge, measure the clearance.
   - Standard body clearance: **0.07 – 0.15 mm (0.0028 – 0.0059 in.)**
   - Maximum body clearance: **0.3 mm (0.012 in.)**
   - If the body clearance is greater than the maximum, replace the drive gear, driven gear or pump body.
2. **CHECK TIP CLEARANCE OF BOTH GEARS** — Measure between the gear teeth and the crescent-shaped part of the pump body.
   - Standard tip clearance: **0.11 – 0.14 mm (0.0043 – 0.0055 in.)**
   - Maximum tip clearance: **0.3 mm (0.012 in.)**
   - If the tip clearance is greater than the maximum, replace the drive gear, driven gear or pump body.
3. **CHECK SIDE CLEARANCE OF BOTH GEARS** — Using a steel straightedge and a feeler gauge, measure the side clearance of both gears.
   - Standard side clearance: **0.02 – 0.05 mm (0.0008 – 0.0020 in.)**
   - Maximum side clearance: **0.1 mm (0.004 in.)**
   - If the side clearance is greater than the maximum, replace the drive gear, driven gear or pump body.
4. **INSPECT FRONT OIL SEAL** — Check for wear, damage or cracks.
5. **IF NECESSARY, REPLACE FRONT OIL SEAL**
   1. Pry off the oil seal with a screwdriver.
   2. Using SST and a hammer, install a new oil seal. The seal end should be flush with the outer edge of the pump body. — **SST 09350-32013 (09351-32140)**

**ASSEMBLY OF OIL PUMP** *(see Oil pump exploded view above)*

1. **INSTALL DRIVEN GEAR AND DRIVE GEAR** — Make sure the top of the gears are facing upward.
2. **INSTALL STATOR SHAFT ONTO PUMP BODY** — Align the stator shaft with each bolt hole.
3. **TIGHTEN ELEVEN BOLTS**
   - Torque: **100 kg-cm (7 ft-lb, 10 N·m)**
4. **INSTALL THRUST WASHER**
   1. Coat the thrust washer with petroleum jelly.
   2. Align the tab of the washer with the hollow of the pump body.
5. **INSTALL THE TWO OIL SEAL RINGS ON OIL PUMP**
   > **CAUTION:** Do not spread the ring ends too much.
   > **NOTE:** After installing the oil seal rings, check that they move smoothly.
6. **CHECK PUMP DRIVE GEAR ROTATION** — Turn the drive gear with two screwdrivers and make sure that it rotates smoothly.
7. **INSTALL NEW O-RING**
8. **INSTALL RACE ONTO STATOR SHAFT**

### Direct Clutch

*(Figure: Direct clutch exploded view — direct clutch drum, O-ring, piston, piston return spring, snap ring, flange, disc, snap ring — see page image p.592, source page AT-74. Legend: `+` = non-reusable part.)*

**DISASSEMBLY OF DIRECT CLUTCH**

1. **REMOVE SNAP RING FROM CLUTCH DRUM**
2. **REMOVE FLANGE, DISCS AND PLATES**
3. **COMPRESS PISTON RETURN SPRING AND REMOVE SNAP RING** — Place SST on the spring retainer and compress the spring with a press. Using a screwdriver, remove the snap ring. — **SST 09350-32013 (09351-32070)**
4. **REMOVE PISTON RETURN SPRING**

*(Direct clutch inspection and assembly continue in [Part 2](12b-automatic-transmission-a240e-a241e-part-2.md).)*
