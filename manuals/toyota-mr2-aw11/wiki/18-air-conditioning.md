# Air Conditioning System

Covers the R-12 air conditioning system on the Toyota MR2 (AW11) with the **4A-GE** and
supercharged **4A-GZE** engines. Torque values are given as `kg-cm (ft-lb, N·m)`.

> **CAUTION:** The refrigerant in this system is **R-12**. Observe all
> [Precautions](#precautions) before opening any part of the refrigeration circuit.

## General Description

### Refrigeration cycle

1. The compressor discharges high-temperature, high-pressure refrigerant that contains
   the heat absorbed from the evaporator plus the heat created by the compressor in a
   discharge stroke.
2. This gaseous refrigerant flows into the condenser. In the condenser, the gaseous
   refrigerant condenses into liquid refrigerant.
3. This liquid refrigerant flows into the receiver, which stores and filters the liquid
   refrigerant until the evaporator requires the refrigerant.
4. By the (expansion) valve, the liquid refrigerant changes into a low-temperature,
   low-pressure liquid and gaseous mixture.
5. This cold, foggy refrigerant flows to the evaporator. Vaporizing the liquid in the
   evaporator, the heat from the warm air stream passing through the evaporator core is
   transferred to the refrigerant. All the liquid changes into gaseous refrigerant in the
   evaporator, and only heat-laden gaseous refrigerant is drawn into the compressor. Then
   the process is repeated.

*(Figure: refrigeration cycle schematic — compressor, condenser, receiver, expansion
valve, evaporator — see page image p.940.)*

### Principle of the A/C electrical circuit

The magnetic clutch is fed through the ignition switch, circuit breaker, heater relay,
A/C fuse, and A/C switch, and is controlled by the A/C amplifier together with the blower
switch/motor, VSV, thermistor (TEMP), and — on the **4A-GZE engine only** — a revolution
detecting sensor (RPM).

*(Figure: A/C electrical circuit block diagram — see page image p.941.)*

### How the magnetic clutch is energized

The general process by which the magnetic clutch is energized:

1. Ignition switch **ON**.
2. Blower switch **ON** → heater relay **ON** (blower motor **RUN**).
3. A/C switch **ON** → A/C amplifier **ON** (A/C amplifier main power supply).
4. Dual pressure switch **ON**: refrigerant pressure between **2.1 kg/cm² (30 psi, 206 kPa)**
   and less than **27 kg/cm² (384 psi, 2648 kPa)**.
5. Thermistor supplies the temperature of the evaporator to the A/C amplifier.
6. VSV **ON** → engine idle-up.
7. A/C amplifier turns on the magnetic clutch.

The revolution detecting sensor supplies the RPM of the compressor to the A/C amplifier.
If the compressor is not locked, the magnetic clutch is continuously energized.

## Air Conditioning System Circuit

The wiring differs between engines. Key components on both: air flow control switch, air
flow control servo motor, A/C amplifier, radiator fan motor, water temperature sensor,
pressure switch, radiator fan relay, and fan main relay. The **4A-GZE** circuit adds
idle-up (for electrical load) and cancellation (M/T only).

- *(Figure: A/C system circuit — 4A-GE engine — see page image p.942.)*
- *(Figure: A/C system circuit — 4A-GZE engine — see page image p.943.)*
- *(Figure: connector layouts, 4A-GE and 4A-GZE — see page image p.944.)*

## System Components

*(Figure: system component layout — VSV, receiver, pressure switch, suction hose/tube,
discharge hose, high- and low-pressure charging valves, liquid tubes, and cooling unit —
see page image p.945.)*

## Precautions

1. When handling refrigerant (R-12), observe the following:
   - Always wear eye protection.
   - Keep the refrigerant container (service drum) below 40°C (104°F).
   - Do not handle refrigerant in an enclosed area where there is an open flame.
   - Discharge refrigerant slowly when purging the system.
   - Be careful that the liquid refrigerant does not get on your skin.
2. If liquid refrigerant gets in the eyes or on the skin:
   - Do not rub eyes or skin.
   - Wash the area with a lot of cool water.
   - Apply clean petroleum jelly to the skin.
   - Rush to a physician or hospital for immediate professional treatment.
   - Do not attempt to treat yourself.
3. When tubing:
   - Apply a few drops of compressor oil onto the O-ring fittings.
   - Tighten the nut using two wrenches to avoid twisting the tube.
   - Tighten the O-ring fitting to the specified torque.

### Torque specification for O-ring fittings and bolted-type fitting

| Fitting size            | Torque                       |
| ----------------------- | ---------------------------- |
| 0.31 in. tube           | 135 kg-cm (10 ft-lb, 13 N·m) |
| 0.50 in. tube           | 235 kg-cm (17 ft-lb, 23 N·m) |
| 0.62 in. tube           | 325 kg-cm (24 ft-lb, 32 N·m) |
| Bolted type (for compressor) | 250 kg-cm (18 ft-lb, 25 N·m) |

## Special Tools and Equipment

| Tool                         | SST No.     | Use                                         |
| ---------------------------- | ----------- | ------------------------------------------- |
| Manifold gauge set           | 07710-58011 | To evacuate and charge system               |
| Ohmmeter                     | —           | To perform electrical diagnosis             |
| Voltage meter                | —           | To perform electrical diagnosis             |
| Ammeter                      | —           | To perform electrical diagnosis             |
| Magnetic clutch tool set     | 07110-77011 | Includes the following 8 tools              |
| Pressure plate remover       | 07112-71010 | To remove pressure plate                    |
| Snap ring pliers             | 07114-84020 | To remove and install rotor and stator      |
| Key remover                  | 07112-45021 | To remove key                               |
| Shaft plate remover          | 07112-15010 | To remove shaft plate                       |
| Shaft seal remover           | 07114-15010 | To remove and install shaft seal            |
| Hexagon wrench set           | 07110-61050 | To remove and install service valve and front housing |
| Shaft plate installing tool  | 07112-25010 | To install shaft plate                      |
| Key press tool               | 07114-45010 | To install key                              |

## Troubleshooting

| Problem                              | Possible cause                    | Remedy                          | Page       |
| ------------------------------------ | --------------------------------- | ------------------------------- | ---------- |
| No blower operation                  | Blown fuse                        | Replace                         | AC-4, 5    |
|                                      | Defective blower motor            | Check and repair                |            |
|                                      | Defective blower relay            | Check operation                 | AC-4, 5    |
|                                      | Defective blower switch           | Check for short or open circuit | BE-35      |
|                                      | Blown blower resistor             | Replace                         | BE-36      |
|                                      | Defective wiring connection       | Check and repair                | AC-4, 5    |
| No blower control                    | Blown blower resistor             | Replace                         |            |
|                                      | Defective blower switch           | Check for short or open circuit | BE-35      |
|                                      | Defective servo motor             | Check operation                 | BE-37      |
|                                      | Defective blower control relay    | Check operation                 | AC-4, 5    |
|                                      | Defective system amplifier        | Replace amplifier and recheck   |            |
|                                      | Defective A/C amplifier           | Check operation                 | AC-41, 42  |
|                                      | Defective wiring connection       | Check and repair                | AC-4, 5    |
| Interior temperature does not drop   | Blown fuse                        | Replace                         |            |
|                                      | Defective magnetic clutch         | Check and repair                | AC-15      |
|                                      | Defective compressor              | Check and repair                | AC-15      |
|                                      | Defective pressure switch         | Replace                         | AC-35      |
|                                      | Insufficient refrigerant in system | Check discharge refrigeration system | AC-14 |
|                                      | Defective A/C switch              | Check for short or open circuit | AC-40      |
|                                      | Defective servo motor             | Check operation                 | BE-37      |
|                                      | Defective system amplifier        | Replace amplifier and recheck   |            |
|                                      | Defective A/C amplifier           | Check operation                 | AC-41, 42  |
|                                      | Defective wiring connection       | Check and repair                | AC-4, 5    |
|                                      | Defective water valve             | Check for leak and repair       |            |
| Interior temperature does not rise   | Defective water valve             | Check operation                 |            |
|                                      | Defective servo motor             | Check operation                 | BE-37      |
|                                      | Defective system amplifier        | Replace amplifier and recheck   |            |
|                                      | Defective A/C amplifier           | Check operation                 | AC-41, 42  |
|                                      | Defective wiring connection       | Check and repair                | AC-4, 5    |
| Unstable operation (fluctuating)     | Defective servo motor             | Check operation                 | BE-37      |
|                                      | Defective system amplifier        | Replace amplifier and recheck   |            |
|                                      | Defective A/C amplifier           | Check operation                 | AC-41, 42  |
|                                      | Defective wiring connection       | Check and repair                | AC-4, 5    |

### Checking of refrigeration system with manifold gauge

Locate the trouble using a manifold gauge. Read the manifold gauge pressure under the
following established conditions:

- Temperature at the air inlet is 30 – 35°C (86 – 95°F)
- Engine running at 2,000 rpm
- Blower speed set at high
- Temperature control lever set at cool

> **NOTE:** The gauge indications may vary slightly due to ambient temperature conditions.

**Normally functioning refrigeration system — gauge reading:**

| Side               | Reading                                            |
| ------------------ | -------------------------------------------------- |
| Low pressure side  | 1.5 – 2.0 kg/cm² (21 – 28 psi, 147 – 196 kPa)      |
| High pressure side | 14.5 – 15.0 kg/cm² (206 – 213 psi, 1422 – 1471 kPa) |

Each pointer of the manifold gauge points to the **A** position.

*(Figure: manifold gauge dial with lettered pointer positions A–F, D' — see page image
p.948.)*

**Fault diagnosis by pointer position:**

| No. | Trouble                                                                    | Condition                                          | Pointer position |
| --- | -------------------------------------------------------------------------- | -------------------------------------------------- | ---------------- |
| 1   | Moisture present in refrigerant system                                     | Periodically cools and then fails to cool          | Between A and B  |
| 2   | Insufficient refrigerant                                                   | Insufficient cooling                               | C                |
| 3   | Poor circulation of refrigerant                                            | Insufficient cooling                               | C                |
| 4   | Refrigerant overcharge or insufficient cooling of condenser                | Does not cool sufficiently                         | D                |
| 5   | Expansion valve improperly mounted / heat sensing tube defective (opens too wide) | Insufficient cooling                        | D                |
| 6   | Air present in refrigeration system                                        | Does not cool sufficiently                         | Low is D, High is D' |
| 7   | Refrigerant does not circulate                                             | Does not cool (cools from time to time in some cases) | E             |
| 8   | Insufficient compressor                                                    | Does not cool                                      | F                |

**Detailed diagnosis (probable cause → diagnosis → remedy):**

| No. | Symptom seen in refrigeration system | Probable cause | Diagnosis | Remedy |
| --- | ------------------------------------ | -------------- | --------- | ------ |
| 1 | During operation, pressure at low pressure side sometimes becomes a vacuum and sometimes normal | Moisture entered in refrigeration system; freezes at expansion valve orifice and temporarily stops cycle, but normal state is restored after a time when the ice melts | Drier in oversaturated state; moisture in refrigeration system freezes at expansion valve orifice and blocks circulation of refrigerant | (1) Replace receiver and drier; (2) remove moisture in cycle through repeated vacuum purging; (3) charge refrigerant to proper amount |
| 2 | Pressure low at both low and high pressure sides; bubbles seen in sight glass; insufficient cooling performance | Gas leakage at some place in refrigeration system | Insufficient refrigerant in system; refrigerant leaking | (1) Check with leak detector and repair; (2) charge refrigerant to proper amount |
| 3 | Pressure low at both low and high pressure sides; frost on tubes from receiver to unit | Refrigerant flow obstructed by dirt in receiver | Receiver clogged | Replace receiver |
| 4 | Pressure too high at both low and high pressure sides | Unable to develop sufficient performance due to excessive refrigerant in system; condenser cooling insufficient | Excessive refrigerant in cycle → refrigerant overcharged; condenser cooling insufficient → condenser fins clogged or fan motor faulty | (1) Clean condenser; (2) check fan motor operation; (3) if (1) and (2) are normal, check refrigerant amount. **NOTE:** Vent out refrigerant through gauge manifold low pressure side by gradually opening valve. |
| 5 | Pressure too high at both low and high pressure sides; frost or large amount of dew on piping at low pressure side | Trouble in expansion valve or heat sensing tube not installed correctly; refrigerant flow out | Excessive refrigerant in low pressure piping; expansion valve opened too wide | (1) Check heat sensing tube installed condition; (2) if (1) is normal, test expansion valve in unit — replace if defective |
| 6 | Pressure too high at both low and high pressure sides | Air entered refrigeration system | Air present in refrigeration system; insufficient vacuum purging | (1) Replace receiver and drier; (2) check compressor oil to see if dirty or insufficient; (3) vacuum purge and charge new refrigerant |
| 7 | Vacuum indicated at low pressure side, very low pressure indicated at high pressure side; frost or dew seen on piping before and after receiver and drier or expansion valve | Refrigerant flow obstructed by moisture or dirt in refrigerant freezing or adhering to expansion valve orifice; refrigerant flow obstructed by gas leakage from expansion valve heat sensing tube | Expansion valve orifice clogged; refrigerant does not flow | Allow to stand for some time and then restart operation to determine if trouble is caused by moisture or dirt. If caused by moisture, refer to Step 2 above. If caused by dirt, remove expansion valve and clean off dirt by blowing with air; if unable to remove dirt, replace valve. Vacuum purge and charge new refrigerant to proper amount. For gas leakage from heat sensing tube, replace expansion valve. |
| 8 | Pressure too high at low pressure side; pressure too low at high pressure side | Internal leak in compressor | Compression defective; valve leaking or broken sliding parts (piston, cylinder, gasket, etc.) broken | Repair or replace compressor |

> **NOTE (at No. 6):** These gauge indications are shown when the refrigeration system has
> been opened and the refrigerant charged without vacuum purging.

## On-Vehicle Inspection

1. **Check condenser fins for blockage or damage.** If the fins are clogged, clean them
   with pressurized water.
   > **CAUTION:** Be careful not to damage the fins.
2. **Check drive belt tension.** Using a belt tension gauge, check the drive belt.
   - Belt tension gauge: Nippondenso BTG-20 (95506-00020) or Borroughs No. BT-33-73F

   | Engine        | New belt   | Used belt  |
   | ------------- | ---------- | ---------- |
   | 4A-GE engine  | 132 ± 10 lb | 88 ± 10 lb |
   | 4A-GZE engine | 165 ± 10 lb | 82 ± 15 lb |

   > **NOTE:**
   > - "New belt" refers to a belt that has been used less than 5 minutes on a running engine.
   > - "Used belt" refers to a belt that has been used on a running engine for 5 minutes or more.
3. **Start engine.**
4. **Turn on A/C switch.** Check that the A/C operates at each position of the blower switch.
5. **Check magnetic clutch operation.**
6. **Check that idle increases.** When the magnetic clutch engages, engine revolution
   should increase.
   - Standard idle-up rpm: **900 – 1,000 rpm**
7. **Check condenser fan motor rotates.**
8. **Check amount of refrigerant.** If you can see bubbles in the sight glass, additional
   refrigerant is needed. (See [Checking of refrigerant charge](#checking-of-refrigerant-charge).)
9. **If no or insufficient cooling, inspect for leakage.** Using a gas leak detector,
   inspect each component of the refrigeration system.

## Refrigeration System

### Checking of refrigerant charge

1. **Run engine at approx. 2000 rpm.**
2. **Operate air conditioner at maximum cooling for a few minutes.**
3. **Check amount of refrigerant.** Observe the sight glass on the receiver.

| Item | Symptom                                                         | Amount of refrigerant       | Remedy                                                          |
| ---- | -------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------- |
| 1    | Bubbles present in sight glass                                  | Insufficient                | Check for leak with gas leak detector                          |
| 2    | No bubbles present in sight glass                              | Empty, proper or too much   | Refer to items 3 and 4                                         |
| 3    | No temperature difference between compressor inlet and outlet  | Empty or nearly empty       | Evacuate and charge system. Then check for leak with gas leak detector |
| 4    | Temperature between compressor inlet and outlet is noticeably different | Proper or too much | Refer to items 5 and 6                                         |
| 5    | Immediately after the air conditioner is turned off, refrigerant in sight glass stays clear | Too much | Discharge the excess refrigerant to specified amount |
| 6    | When the air conditioner is turned off, refrigerant foams and then stays clear | Proper       | —                                                              |

### Installation of manifold gauge set

> **NOTE:** Fittings for attaching the manifold gauge set are located on the suction tube
> charging valve and liquid tube charging valve.

1. **Close both hand valves of the manifold gauge set.**
2. **Install charging hoses of gauge set to charging valves.** Connect the low pressure
   hose to the low pressure charging valve and the high pressure hose to the high pressure
   charging valve. Tighten the hose nuts by hand.
   > **NOTE:** Do not apply compressor oil to the seat of the connection.

## Compressor

### On-vehicle inspection

1. **Install manifold gauge set.** (See [Installation of manifold gauge set](#installation-of-manifold-gauge-set).)
2. **Run engine at fast idle.**
3. **Check compressor for the following:**
   - High pressure gauge reading is not lower and low pressure gauge reading is not higher
     than normal.
   - Metallic sound.
   - Leakage from shaft seal.

   If any of the above is not satisfactory, repair the compressor.
4. **Check magnetic clutch.**
   - Inspect the pressure plate and the rotor for signs of oil.
   - Check the clutch bearings for noise and leaking grease.
   - Using an ohmmeter, measure the resistance of the stator coil between the clutch lead
     wire and ground.
     - Standard resistance: **3.7 ± 0.2 Ω at 20°C (68°F)**

     If resistance is not as specified, replace the coil.
   - Connect the positive (+) lead from the battery to the terminal, and check that the
     magnetic clutch is energized. If the magnetic clutch does not energize, replace the coil.
     > **CAUTION:** Do not short the positive (+) lead wire harness to the vehicle when
     > applying battery voltage.
5. **Revolution detecting sensor (4A-GZE engine only).** Using an ohmmeter, measure the
   resistance between the two terminals of the sensor.
   - Standard resistance: **100 – 130 Ω at 20°C (68°F)**

   If resistance is not as specified, replace the revolution detecting sensor.

**Compressor mounting torques (both engines):**

| Location                     | Torque            |
| ---------------------------- | ----------------- |
| Bracket bolts (upper)        | 375 kg-cm (28, 36) |
| Bracket bolts                | 450 kg-cm (32, 43) |
| Compressor mounting bolt     | 280 kg-cm (20, 27) |

*(Torque triples are `kg-cm (ft-lb, N·m)`. Figures: 4A-GE p.954, 4A-GZE p.954.)*

### Removal of compressor

1. **Run engine at idle with air conditioning on for 10 minutes.**
2. **Stop the engine.**
3. **Disconnect negative cable from battery.**
4. **Remove battery.**
5. **Disconnect clutch lead wire from wiring harness.**
6. **Discharge refrigerant from refrigeration system.**
7. **Disconnect two hoses from compressor.**
   > **NOTE:** Cap the open fitting immediately to keep moisture out of the system.
8. **Remove compressor.**
   - Loosen the drive belt.
   - Remove the compressor mounting bolts and the compressor.

*(Figures: magnetic clutch/compressor exploded views, 4A-GE p.955 and 4A-GZE p.956 — show
pressure plate, rotor, rotor bearing, stator, snap ring, shim, and non-reusable parts.)*

### Disassembly of magnetic clutch

1. **Remove pressure plate.**
   - Using SST and a socket, remove the shaft nut. **SST 07110-77011**
   - Using SST and a socket, remove the pressure plate. **SST 07112-71010**
   - Remove the shims from the shaft.
2. **Remove rotor.**
   - Using SST, remove the snap ring. **SST 07114-84020**
   - Using a plastic hammer, tap the rotor off the shaft.
     > **CAUTION:** Be careful not to damage the pulley when tapping on the rotor.
3. **Remove stator.**
   - Disconnect the stator lead wires from the compressor housing.
   - Using SST, remove the snap ring. Remove the stator. **SST 07114-84020**
4. **Remove rotor bearings.**
   > **NOTE:** Press out the bearings only if they are to be replaced.
   - Remove the bearing snap ring from the rotor.
   - Using SST, press out the two bearings. **SST 07110-77011**
5. **Inspect pressure plate and rotor.**
   - Inspect the pressure plate and rotor surfaces for wear and scoring. Replace if necessary.
   - Check the rotor bearings for wear and leakage of grease. Replace if necessary.

### Disassembly of compressor

*(Figures: compressor cylinder block / O-ring / revolution detecting sensor, 4A-GE p.957
and 4A-GZE p.957.)*

1. **Remove felt.**
2. **Remove snap ring.** Using SST, remove the snap ring. **SST 07114-84020**
3. **Remove key.** Remove the key from the shaft. **SST 07112-45021**
4. **Apply compressor oil to inner bore.** Apply compressor oil to the inner bore of the
   compressor.
5. **Remove shaft plate.**
   - Insert SST against the shaft. Then push the holder ring downward. **SST 07112-15010**
   - Pull up the remover bar and remove the shaft plate.
6. **Remove shaft seal.** Insert SST against the shaft, and turn it to the right while
   pressing on the remover. Then remove the shaft seal. **SST 07114-15010**
7. **Remove service valve.**
   - Using SST, remove the bolts holding the service valve. **SST 07110-61050**
   - Remove the O-ring from the service valve and discard it.
8. **Drain compressor oil into measuring flask.** Measure the quantity of drained oil
   because the same amount should be replaced later.
9. **Remove revolution detecting sensor (4A-GZE engine only).**
10. **Remove front housing.**
    - Using SST, remove the five through bolts. **SST 07110-61050**
      > **NOTE:** Do not reuse the five washers.
    - Using a screwdriver, remove the front housing.
      > **CAUTION:** Be careful not to scratch the sealing surface of the front housing.
11. **Remove front valve plate.** Remove the two pins from the front housing. Discard the pins.
12. **Remove rear housing.** Using a screwdriver, remove the rear housing.
    > **CAUTION:** Be careful not to scratch the sealing surface of the rear housing.
13. **Remove front and rear O-rings from cylinder block.** Discard the O-rings.

### Assembly of compressor

1. **Install rear valve plate on rear cylinder.**
   - Install two pins in the rear cylinder.
   - Lubricate a new O-ring with compressor oil. Install the O-ring in the rear cylinder.
   - Install the rear suction valve over the pins on the rear cylinder.
     > **NOTE:** The front and rear suction valves are identical.
   - Install the rear valve plate together with the discharge valve over the pins on the
     rear cylinder.
     > **NOTE:** The rear valve plate is marked with an "R."
   - Lubricate the new gasket with compressor oil. Install the gasket on the valve plate.
2. **Install rear housing on rear cylinder.**
3. **Install front valve plate on front cylinder.**
   - Install the two pins in the front cylinder.
   - Lubricate a new O-ring with compressor oil. Install the O-ring in the front housing.
   - Install the front suction valve over the pins on the front cylinder.
   - Install the front valve plate together with the discharge valve over the pins on the
     front cylinder.
     > **NOTE:** The front valve plate is marked with an "F."
   - Lubricate the new gasket with compressor oil. Install the gasket on the valve plate.
4. **Install front housing on front cylinder and tighten five through bolts.** Using SST
   and torque wrench, gradually tighten the five through bolts in two or three passes.
   - **SST 07110-61050**
   - Torque: **260 kg-cm (19 ft-lb, 25 N·m)**
5. **Install shaft seal.**
   - Fit the shaft seal onto SST. **SST 07114-15010**
   - Apply oil to the bore. Insert SST, and turn it counterclockwise while lightly pressing
     in. Then pull up the SST. **SST 07114-15010**
6. **Install shaft plate.**
   - Put in the shaft plate.
   - Press in SST. **SST 07112-25010**
7. **Install key in shaft groove.** Using SST and plastic hammer, tap the key lightly.
   Place the felt inside the bore. **SST 07114-45010**
8. **Install revolution detecting sensor (4A-GZE engine only).**
9. **Pour compressor oil into compressor.** Add the same quantity plus 20 cc of oil into
   the compressor.
   - Compressor oil: **DENSOIL 6 SUNISO No. 5GS** <!-- NEEDS REVIEW: printed as one line; likely two acceptable oils, "DENSO OIL 6" or "SUNISO No. 5GS" — verify separator -->
10. **Install service valve.**
    - Lubricate new O-rings with compressor oil. Install the O-rings in the service valve.
    - Install the service valve on the compressor. Using SST and torque wrench, tighten the
      bolts. **SST 07110-61050**
    - Torque: **260 kg-cm (19 ft-lb, 25 N·m)**
11. **Check shaft starting torque.**
    - Torque: **30 kg-cm (26 in.-lb, 2.9 N·m) or less**

### Assembly of magnetic clutch

1. **Install two bearings in rotor.**
   - Using SST, press a shield ring and two new bearings into the rotor boss until fully
     seated. **SST 07110-77011**
   - Install the bearing snap ring into the rotor groove.
2. **Install stator.**
   - Install the stator on the compressor.
   - Using SST, install the new snap ring. **SST 07114-84020**
   - Connect the stator lead wires to the compressor housing.
3. **Install rotor.**
   - Install the rotor on the compressor shaft.
   - Using SST, install the new snap ring. **SST 07114-84020**
4. **Install pressure plate.**
   - Adjust the clearance between the pressure plate and rotor by putting shims on the
     compressor shaft.
     - Standard clearance: **0.4 – 0.7 mm (0.016 – 0.028 in.)**

     If the clearance is not within tolerance, add or reduce the number of shims to obtain
     the standard clearance.
   - Using SST and torque wrench, install the shaft nut. **SST 07110-77011**
     - Torque: **165 kg-cm (12 ft-lb, 16 N·m)**
5. **Check clearance of magnetic clutch.** Using thickness gauge, check the clearance
   between the pressure plate and rotor.
   - Standard clearance: **0.6 – 1.0 mm (0.024 – 0.039 in.)**

   If the clearance is not within standard clearance, adjust using the shims to obtain the
   standard clearance.

### Performance test of compressor

1. **Perform gas leakage test.**
   - Install the inspection service valve on the service valve.
     > **NOTE:** Use only a TOYOTA-supplied inspection service valve for the gas leakage test.
     - Part No. Suction side: **88376-17020**
     - Part No. Discharge side: **88376-22020**
   - Charge the compressor with refrigerant through the charge valve until the pressure is
     **3 kg/cm² (43 psi, 294 kPa)**.
   - Using a gas leak detector, check the compressor for leaks. If leaks are found, check
     and replace the compressor.
2. **Evacuate compressor and charge with refrigerant.** Make sure the caps are tight and
   the compressor is free from moisture and contamination.
   > **NOTE:** When storing a compressor for an extended period, charge the compressor with
   > refrigerant or dry nitrogen gas to prevent corrosion.

### Installation of compressor

1. **Install compressor with four mounting bolts.**
   - Torque: **280 kg-cm (20 ft-lb, 27 N·m)**
2. **Install drive belt.**
   - Install the drive belt to the pulley.
   - Tighten the belt with adjusting bolts. Using a belt tension gauge, check the drive
     belt tension.
   - Belt tension gauge: Nippondenso BTG-20 (95506-00020) or Borroughs No. BT-33-73F

   | Engine        | New belt   | Used belt   |
   | ------------- | ---------- | ----------- |
   | 4A-GE engine  | 132 ± 10 lb | 88 ± 10 lb <!-- NEEDS REVIEW: OCR read "88 10 lb"; page image (p.951) shows "88 ± 10 lb" — ± confirmed --> |
   | 4A-GZE engine | 165 ± 10 lb | 82 ± 15 lb |

   > **NOTE:**
   > - "New belt" refers to a belt that has been used less than 5 minutes on a running engine.
   > - "Used belt" refers to a belt that has been used on a running engine for 5 minutes or more.
3. **Connect two hoses to compressor.**
   - Discharge line: **250 kg-cm (18 ft-lb, 25 N·m)**
   - Suction line: **250 kg-cm (18 ft-lb, 25 N·m)**
4. **Connect clutch lead wire to wiring harness.**
5. **Place battery.**
6. **Connect cables to battery.**
7. **Evacuate air from air conditioning system.**
8. **Charge air conditioning system with refrigerant and check for gas leakage.**
   - Specified amount: **600 – 750 g (1.3 – 1.7 lb)**

## Receiver

### On-vehicle inspection

**Check sight glass, fusible plug and fitting for leakage.** Use a gas leak detector.
Repair as necessary.

### Removal of receiver

1. **Discharge refrigeration system.**
2. **Remove spare tire and trim cover.**
3. **Disconnect two liquid tubes from receiver.**
   > **NOTE:** Cap the open fittings immediately to keep moisture out of the system.
4. **Remove receiver from receiver holder.**

### Installation of receiver

1. **Install receiver in receiver holder.**
   > **NOTE:** Do not remove the blind plugs until connecting the liquid tubes to the receiver.
2. **Connect two liquid tubes to receiver.**
   - Torque: **135 kg-cm (10 ft-lb, 13 N·m)**
3. **Install trim cover and spare tire.**
4. **If receiver was replaced, add compressor oil to compressor.** Add **20 cc (0.7 fl.oz.)**.
5. **Evacuate air from air conditioning system.**
6. **Charge air conditioning system with refrigerant and check for gas leakage.**
   - Specified amount: **600 – 750 g (1.3 – 1.7 lb)**

## Condenser

### On-vehicle inspection

1. **Check condenser fins for blockage or damage.** If the fins are clogged, wash them
   with water and dry with compressed air.
   > **CAUTION:** Be careful not to damage the fins.

   If the fins are bent, straighten them with a screwdriver or pliers.
2. **Check condenser fittings for leakage.** Repair as necessary.

### Removal of condenser

1. **Discharge refrigeration system.**
2. **Remove front grille and front under cover.**
3. **Remove two upper condenser bolts.**
4. **Remove two upper radiator bolts.** After removing the bolts, lean the radiator back.
5. **Disconnect discharge tube and discharge tube clamp from condenser inlet fitting.**
6. **Disconnect liquid tube and liquid tube clamp from condenser outlet fitting.**
   > **NOTE:** Cap the open fittings immediately to keep moisture out of the system.
7. **Remove condenser.** Remove the two lower condenser nuts and condenser.

### Installation of condenser

1. **Install condenser.** Install the two lower condenser nuts, making sure the rubber
   cushions fit on the mounting flanges correctly.
2. **Connect liquid tube, discharge tube and two clamps to condenser.**
   - Liquid tube: **135 kg-cm (10 ft-lb, 13 N·m)**
   - Discharge tube: **185 kg-cm (13 ft-lb, 18 N·m)**
3. **Install two upper condenser bolts.**
4. **Install two upper radiator bolts.**
5. **Install front grille and under cover.**
6. **If condenser was replaced, add compressor oil to compressor.** Add **40 – 50 cc
   (1.4 – 1.7 fl.oz.)**.
7. **Evacuate air from air conditioning system.**
8. **Charge air conditioning system with refrigerant and check for gas leakage.**
   - Specified amount: **600 – 750 g (1.3 – 1.7 lb)**

## Condenser Fan Motor

### Inspection of fan motors

1. **Inspect fan motors.**
   - Disconnect the 2-P connector of the fan motor.
   - Using the wire harness, apply battery voltage to the connector.
   - Confirm smooth rotation of the motor within the specified current flow.
     - Standard current: **6.7 ± 0.7 A**

     If current is not as specified, replace the motor.
2. **Check fan motors operation.**
   > **NOTE:** The fan motors operate at two speeds depending on the water temperature and
   > the A/C switch.

   | A/C switch  | Magnetic clutch | Water temperature                                                          | Fan motor speed |
   | ----------- | --------------- | -------------------------------------------------------------------------- | --------------- |
   | OFF or ON   | OFF             | 85°C (185°F) or below                                                      | OFF             |
   | OFF or ON   | OFF             | 85 to 90°C (185 to 194°F)                                                  | LO              |
   | OFF or ON   | OFF             | 90°C (194°F) or above                                                      | HI              |
   | ON          | ON              | 90°C (194°F) or below                                                      | LO              |
   | ON          | ON              | 90°C (194°F) or above, or the refrigerant pressure is over 15.5 kg/cm² (220 psi, 1,520 kPa) | HI |

   > *(Example) A/C switch: ON, magnetic clutch: ON, water temperature: 90°C (194°F) or
   > below → fan motor speed: LO.*

*(Figure: condenser fan motor circuit — AM2 FL 10A, HEAD FL 60A, fan main relay, RDI FAN
fuse 30A, CDS FAN fuse 30A, radiator fan relay, A/C fan relay No. 2 and No. 3, water
temperature sensor, amplifier, high pressure switch, compressor — see page image p.970.)*

## A/C Relays

### Inspection of relays

Inspect relay continuity as follows (○—○ indicates continuity between the two terminals).

**A/C Fan Relay No. 3** (terminals 1, 2, 3, 4):

| Condition                                   | Continuity between |
| ------------------------------------------- | ------------------ |
| No voltage applied                          | 1 – 3              |
| Apply battery voltage to terminals 1 and 3  | 2 – 4              |

**A/C Fan Relay No. 2** (terminals 1, 2, 3, 4, 5):

| Condition                                        | Continuity between       |
| ------------------------------------------------ | ------------------------ |
| No voltage applied                               | 2 – 3; 4 – 5 (via diode, 4→5) |
| Apply battery voltage to terminals 4 (+) and 5 (−) | 1 – 3                  |

**Idle-up Relay** (terminals 1, 2, 3, 4):

| Condition                                   | Continuity between |
| ------------------------------------------- | ------------------ |
| No voltage applied                          | 1 – 2; 3 – 4       |
| Apply battery voltage to terminals 1 and 2  | (no continuity)    |

If continuity is not as specified, replace the relay.

## Pressure Switch

(See [System Components](#system-components).)

### On-vehicle inspection

1. **Disconnect connector of pressure switch.**
2. **Inspect pressure switch.**
   - Install the manifold gauge set.
   - Observe the gauge reading.
   - Check the continuity between the two terminals of the pressure switch as shown below.

**Dual pressure switch** (low- and high-pressure protection):

| Switching point           | State                    |
| ------------------------- | ------------------------ |
| Low side — below 2.1 kg/cm² (30 psi, 206 kPa) | OFF (no continuity) |
| Low side — at 2.35 kg/cm² (33 psi, 230 kPa)   | ON (continuity)     |
| High side — at 21 kg/cm² (299 psi, 2050 kPa) <!-- NEEDS REVIEW: page image (p.972) shows "205 kPa"; physically 21 kg/cm² ≈ 2059 kPa, so a digit appears dropped — verify against a cleaner scan --> | ON (continuity) |
| High side — above 27 kg/cm² (384 psi, 2648 kPa) | OFF (no continuity) |

**Pressure switch** (condenser fan HI trigger):

| Switching point                                | State                |
| ---------------------------------------------- | -------------------- |
| At/above 15.5 kg/cm² (220 psi, 1520 kPa)       | ON (continuity)      |
| Below 12.5 kg/cm² (178 psi, 1226 kPa)          | OFF (no continuity)  |

If defective, replace the pressure switch.

3. **Connect connector of pressure switch.**

## Water Temperature Sensor

### Inspection of temperature sensor

Using an ohmmeter, measure the resistance of the water temperature sensor.

| Water temperature | Resistance      |
| ----------------- | --------------- |
| 85°C (185°F)      | approx. 1.35 kΩ |
| 90°C (194°F)      | approx. 1.19 kΩ |
| 95°C (203°F)      | approx. 1.05 kΩ |

## Cooling Unit

(See [System Components](#system-components).)

### On-vehicle inspection of expansion valve

1. **Check quantity of refrigerant during refrigeration cycle.**
2. **Install manifold gauge set.** (See [Installation of manifold gauge set](#installation-of-manifold-gauge-set).)
3. **Run engine.** Run the engine at 2,000 rpm for at least 5 minutes.
4. **Check expansion valve.** If the expansion valve is clogged, the low pressure reading
   will drop to **0 kg/cm² (0 psi, 0 kPa)**; otherwise it is OK.

### Removal of cooling unit

1. **Disconnect negative cable from battery.**
2. **Discharge refrigeration system.**
3. **Disconnect suction tube from cooling unit outlet fitting.**
4. **Disconnect liquid tube from cooling unit inlet fitting.**
   > **NOTE:** Cap the open fittings immediately to keep moisture out of the system.
5. **Remove grommets from inlet and outlet fittings.**
6. **Remove glove box and under cover.**
7. **Disconnect connectors.**
8. **Remove cooling unit.** Remove two nuts and four screws.

### Disassembly of cooling unit

1. **Remove lower and upper unit cases.**
   - Disconnect connectors.
   - Remove four clips.
   - Remove four screws.
   - Remove upper unit case.
   - Remove thermistor with thermistor holder.
   - Remove lower unit case.
2. **Remove expansion valve.**
   - Disconnect the liquid tube from the inlet fitting of the expansion valve.
   - Remove the packing and heat sensing tube from the suction tube of the evaporator.
   - Remove the expansion valve.

### Evaporator — inspection

1. **Check evaporator fins for blockage.** If the fins are clogged, clean them with
   compressed air.
   > **CAUTION:** Never use water to clean the evaporator.
2. **Check fittings for cracks or scratches.** Repair as necessary.

### Assembly of cooling unit

**Install components on evaporator:**

1. Connect the expansion valve to the inlet fitting of the evaporator. Torque the nut.
   - Torque: **235 kg-cm (17 ft-lb, 23 N·m)**
   > **NOTE:** Be sure that the O-rings are positioned on the tube fitting.
2. Install the holder to the suction tube with the heat sensing tube.
3. Connect the liquid tube to the inlet fitting of the expansion valve. Torque the nut.
   - Torque: **135 kg-cm (10 ft-lb, 13 N·m)**
4. Install lower unit case to the evaporator.
5. Install thermistor to the evaporator.
6. Install upper unit case.
7. Install four screws.
8. Install four clips.
9. Connect connectors.

### Installation of cooling unit

1. **Install cooling unit.** Install the cooling unit with two nuts and four screws.
2. **Connect connectors.**
3. **Install glove box and under cover.**
4. **Install grommets on inlet and outlet fittings.**
5. **Connect liquid tube to cooling unit inlet fitting.** Torque the nut.
   - Torque: **135 kg-cm (10 ft-lb, 13 N·m)**
6. **Connect suction tube to cooling unit outlet fitting.** Torque the nut.
   - Torque: **325 kg-cm (24 ft-lb, 32 N·m)**
7. **If evaporator was replaced, add compressor oil to compressor.** Add **40 – 50 cc
   (1.4 – 1.7 fl.oz.)**.
8. **Connect negative cable to battery.**
9. **Evacuate air from air conditioning system.**
10. **Charge air conditioning system with refrigerant and check for gas leakage.**
    - Specified amount: **600 – 750 g (1.3 – 1.7 lb)**

## Refrigerant Lines

(See [System Components](#system-components).)

### On-vehicle inspection

1. **Inspect hoses and tubes for leakage.** Use a gas leak detector. Replace if necessary.
2. **Check that hose and tube clamps are not loose.** Tighten or replace as necessary.

### Replacement of refrigerant lines

1. **Discharge refrigeration system.**
2. **Replace faulty tube or hose.**
   > **NOTE:** Cap the open fittings immediately to keep moisture out of the system.
3. **Tightening torque for O-ring.** (See [Torque specification for O-ring fittings and
   bolted-type fitting](#torque-specification-for-o-ring-fittings-and-bolted-type-fitting).)
4. **Evacuate air from air conditioning system.**
5. **Charge air conditioning system with refrigerant and check for gas leakage.**
   - Specified amount: **600 – 750 g (1.3 – 1.7 lb)**

## Thermistor

### On-vehicle inspection

1. **Disconnect negative battery cable.**
2. **Remove glove box.**
3. **Check resistance of thermistor.** Measure the resistance between terminals.
   - Standard resistance: **1500 Ω at 25°C (77°F)**

   If resistance is not as specified, replace the thermistor.

### Removal and inspection of thermistor

1. **Remove and disassemble cooling unit.** (See [Disassembly of cooling unit](#disassembly-of-cooling-unit).)
2. **Remove thermistor from evaporator.**
3. **Check thermistor operation.**
   - Place the thermistor in cold water. While varying the temperature of the water,
     measure the resistance at the connector and, at the same time, measure the temperature
     of the water with a thermometer.
   - Compare the two readings on the chart.

   If the intersection is not between the two lines, replace the thermistor.

*(Figure: thermistor resistance-vs-temperature chart, resistance approx. 3,500 – 5,500 Ω
over −1 to 5°C (30 to 40°F) — see page image p.977.)*

### Installation of thermistor

1. **Install thermistor to evaporator.**
2. **Assemble and install cooling unit.**

## A/C Switch

(See [System Components](#system-components).)

### Inspection of switch

**Inspect switch continuity.** Inspect continuity between the terminals (4, 2, 10, 15).

| Switch position | Continuity between terminals                          |
| --------------- | ----------------------------------------------------- |
| A/C             | 4 – 15; 4 – 2 and 2 – 15 (through panel-illumination bulbs and a resistor) |
| ECONO           | 2 – 10 (through bulb/resistor); 10 – 15               |

<!-- NEEDS REVIEW: the A/C switch continuity chart (page image p.977) mixes plain continuity dots with illumination-bulb and resistor symbols; the terminal-pair continuity above is a best-effort reading of those symbols and should be verified against a cleaner scan or the wiring diagram (chapter BE). -->

If continuity is not as specified, replace the switch.

## Air Conditioner Amplifier

### Inspection of amplifier

**Inspect amplifier circuit.** Disconnect the amplifier and inspect the connector on the
wire harness side as shown in the charts below.

Test conditions:
1. Ignition switch: ON
2. Temperature control lever: MAX COOL
3. Blower switch: HI

**4A-GE E/G model** (connectors K-13-1, H-1-1):

| Check for  | Tester connection | Condition                     | Specified value             |
| ---------- | ----------------- | ----------------------------- | --------------------------- |
| Continuity | 10 – Ground       | —                             | Continuity                  |
| Voltage    | 2 – 10            | Turn A/C switch on            | Battery voltage             |
| Voltage    | 2 – 10            | Turn A/C switch off           | No voltage                  |
| Voltage    | 14 – 10           | Turn ECONO switch on          | Battery voltage             |
| Voltage    | 14 – 10           | Turn ECONO switch off         | No voltage                  |
| Voltage    | 4 – 10            | Turn ignition switch on       | Battery voltage             |
| Voltage    | 4 – 10            | Turn ignition switch off      | No voltage                  |
| Voltage    | 6 – 10            | Turn ignition switch on       | Battery voltage             |
| Voltage    | 6 – 10            | Turn ignition switch off      | No voltage                  |
| Voltage    | 1 – 10            | Turn ignition switch on       | Battery voltage             |
| Voltage    | 1 – 10            | Turn ignition switch off      | No voltage                  |
| Voltage    | 8 – 10            | Turn ignition switch on       | Battery voltage             |
| Voltage    | 8 – 10            | Turn ignition switch off      | No voltage                  |
| Voltage    | 13 – 10           | Start the engine              | Approx. 10 to 14 V          |
| Voltage    | 13 – 10           | Stop the engine               | No voltage                  |
| Continuity | 5 – Ground        | —                             | Continuity                  |
| Continuity | 7 – Ground        | —                             | Continuity                  |
| Resistance | 12 – 11           | —                             | Approx. 1.5 kΩ at 25°C (77°F) |
| Resistance | 9 – 3             | —                             | Approx. 4.5 kΩ              |

**4A-GZE E/G model** (connector K-17-1):

| Check for  | Tester connection | Condition                     | Specified value             |
| ---------- | ----------------- | ----------------------------- | --------------------------- |
| Continuity | 13 – Ground       | —                             | Continuity                  |
| Voltage    | 3 – 13            | Turn A/C switch on            | Battery voltage             |
| Voltage    | 3 – 13            | Turn A/C switch off           | No voltage                  |
| Voltage    | 8 – 13            | Turn A/C switch on            | Battery voltage             |
| Voltage    | 8 – 13            | Turn A/C switch off           | No voltage                  |
| Voltage    | 3 – 13            | Turn ECONO switch on          | Battery voltage             |
| Voltage    | 3 – 13            | Turn ECONO switch off         | No voltage                  |
| Voltage    | 16 – 13           | Turn ECONO switch on          | Battery voltage             |
| Voltage    | 16 – 13           | Turn ECONO switch off         | No voltage                  |
| Voltage    | 2 – 13            | Turn ignition switch on       | Battery voltage             |
| Voltage    | 2 – 13            | Turn ignition switch off      | No voltage                  |
| Voltage    | 5 – 13            | Turn ignition switch on       | Battery voltage             |
| Voltage    | 5 – 13            | Turn ignition switch off      | No voltage                  |
| Voltage    | 9 – 13            | Turn ignition switch on       | Battery voltage             |
| Voltage    | 9 – 13            | Turn ignition switch off      | No voltage                  |
| Voltage    | 14 – 13           | Turn ignition switch on       | Battery voltage             |
| Voltage    | 14 – 13           | Turn ignition switch off      | No voltage                  |
| Voltage    | 6 – 13            | Start the engine              | Approx. 10 to 14 V          |
| Voltage    | 6 – 13            | Stop the engine               | No voltage                  |
| Continuity | 15 – Ground       | —                             | Continuity                  |
| Continuity | 11 – Ground       | —                             | Continuity                  |
| Continuity | 4 – Ground        | —                             | Continuity                  |
| Continuity | 10 – Ground       | —                             | Continuity                  |
| Resistance | 17 – 7            | —                             | Approx. 1.5 kΩ at 25°C (77°F) |
| Resistance | 1 – 13            | —                             | Approx. 4.5 kΩ              |

If the circuit is correct, replace the amplifier.

## Vacuum Switching Valve (VSV)

(See [System Components](#system-components).)

### Inspection of VSV

1. **Remove VSV.**
2. **Check vacuum circuit continuity.**
   - Blow into pipe "A" and check that air does **not** come out of pipe "B".
   - Apply battery voltage (12 V) between terminals No. 1 and No. 2.
   - Blow into pipe "A" and check that air **comes** out of pipe "B".

   If a problem is found, replace the VSV.
