# EFI System and Emission Control (Part 1)

*Toyota MR2 (AW11) 1988 factory service manual — source PDF pages 175–260. Covers the
Emission Control Systems section (manual pages EC-1 to EC-22) and the first part of the
EFI System section (manual pages FI-1 to FI-64), for the **4A-GE** and **4A-GZE**
(supercharged) engines. The Fuel System component procedures continue in
Part 2.*

> **NOTE (from manual):** For emission-system troubleshooting see the Engine Mechanical
> troubleshooting (manual page EM-2). For inspection and repair of the EFI system itself,
> refer to the EFI section below.

---

## Emission Control Systems

### System Purpose

| System | Abbreviation | Purpose |
| ------ | ------------ | ------- |
| Positive crankcase ventilation | PCV | Reduces blow-by gas (HC) |
| Fuel evaporative emission control | EVAP | Reduces evaporative HC |
| Dash pot | DP | Reduces HC and CO |
| Exhaust gas recirculation | EGR | Reduces NOx |
| Three-way catalyst | TWC | Reduces HC, CO and NOx |
| Electronic fuel injection\* | EFI | Regulates all engine conditions for reduction of exhaust emissions |

> \* For inspection and repair of the EFI system, refer to the [EFI System](#efi-system)
> section.

### Component Layout and Schematic Drawing

*(Figure: emission-control component layout and vacuum schematic, 4A-GE — EGR vacuum
modulator, EGR gas temp. sensor (Calif. only), BVSV (for EVAP), BVSV (for EGR), VSV,
vacuum tank, diaphragm (for T-VIS), check valve, charcoal canister, DP, EGR valve, oxygen
sensor, TWC — see page images p.177 (EC-3).)*

*(Figure: emission-control component layout and vacuum schematic, 4A-GZE — EGR vacuum
modulator, EGR gas temp. sensor (Calif. only), charcoal canister, EGR valve — see page
image p.178 (EC-4).)*

### Positive Crankcase Ventilation (PCV) System

To reduce HC emissions, crankcase blow-by gas (HC) is routed to the intake manifold for
combustion in the cylinders.

*(Figure: PCV hose routing, 4A-GE and 4A-GZE — blow-by gas and fresh-air flow paths —
see page image p.179 (EC-5).)*

#### Inspection of PCV hoses and connections

1. **Visually inspect hoses, connections and gaskets.** Check for cracks, leaks or damage.

### Fuel Evaporative Emission Control (EVAP) System

To reduce HC emissions, evaporated fuel from the fuel tank is routed through the charcoal
canister to the intake manifold for combustion in the cylinders.

*(Figure: EVAP system — check valve, BVSV, purge port, canister check valves (1)(2)(3),
check valve in cap, charcoal canister, fuel tank — see page image p.180 (EC-6).)*

#### System operation

| Coolant temp. | BVSV | Throttle valve opening | Canister check valve (1) | Canister check valve (2) | Canister check valve (3) | Check valve in cap | Evaporated fuel (HC) |
| ------------- | ---- | ---------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------ | -------------------- |
| Below 35°C (95°F) | CLOSED | — | — | — | — | — | HC from tank is absorbed into the canister. |
| Above 54°C (129°F) | OPEN | Positioned below purge port | CLOSED | — | — | — | HC from tank is absorbed into the canister. |
| Above 54°C (129°F) | OPEN | Positioned above purge port | OPEN | — | — | — | HC from canister is led into air intake manifold. |
| High pressure in tank | — | — | — | OPEN | CLOSED | CLOSED | HC from tank is absorbed into the canister. |
| High vacuum in tank | — | — | — | CLOSED | OPEN | OPEN | Air is led into the fuel tank. |

#### Inspection of fuel vapor lines, fuel tank and tank cap

1. **Visually inspect lines and connections.** Look for loose connections, kinks or damage.
2. **Visually inspect fuel tank.** Look for deformation, cracks or fuel leakage.
3. **Visually inspect fuel tank cap.** Look for a damaged or deformed gasket and cap. If
   necessary, repair or replace the cap.

#### Inspection of charcoal canister

1. **Remove charcoal canister.**
2. **Visually inspect charcoal canister case.** Look for cracks or damage.
3. **Check for clogged filter and stuck check valve.**
   1. Using low pressure compressed air, blow into the tank pipe and check that air flows
      without resistance from the other pipes.
   2. Blow into the purge pipe and check that air does not flow from the other pipes.

   > If a problem is found, replace the charcoal canister.
4. **Clean filter in canister.** Clean the filter by blowing **3 kg/cm² (43 psi, 294 kPa)**
   of air into the tank pipe while holding the other upper canister pipe closed.

   > **NOTE:**
   > - Do not attempt to wash the canister.
   > - No activated carbon should come out.
5. **Install charcoal canister.**

#### Inspection of BVSV

**Check BVSV by blowing air into pipe:**

1. Drain the coolant from the cylinder block into a suitable container.
2. Remove the BVSV.
3. Cool the BVSV to **below 35°C (95°F)** with cool water.
4. Blow air into a pipe and check that the BVSV is **closed**.
5. Heat the BVSV to **above 54°C (129°F)** with hot water.
6. Blow air into a pipe and check that the BVSV is **open**.

   > If a problem is found, replace the BVSV.
7. Apply liquid sealer to the threads of the BVSV and reinstall.
8. Fill the cylinder block with coolant.

### Dash Pot (DP) System

*(4A-GE only)*

To reduce HC and CO emissions, when decelerating the dash pot opens the throttle valve
slightly more than at idle. This causes the air-fuel mixture to burn completely.

*(Figure: DP diaphragm on throttle body; VTV and filter operation in normal driving vs.
deceleration — see page image p.182 (EC-8).)*

#### System operation

| Condition | Diaphragm | VTV | Throttle valve |
| --------- | --------- | --- | -------------- |
| Idling | Pushed in by return force of throttle valve | CLOSED | Idle speed position |
| Normal driving | Pushed out by diaphragm spring | OPEN | High speed position |
| Deceleration | Pushed in by return force of throttle valve | CLOSED | Slightly opens and then slowly closes to idle position |

#### Inspection of DP system

1. **Warm up and stop engine.** Allow the engine to reach normal operating temperature.
2. **Check idling speed and adjust, if necessary.**
3. **Remove cap, filter and separater from DP.**
4. **Check DP setting speed.**
   1. Race the engine at **2,500 rpm** for a few seconds.
   2. Plug the VTV hole with your finger.
   3. Release the throttle valve.
   4. Check that the DP is set.

   > **DP setting speed: 1,800 rpm** (w/ cooling fan OFF)
   >
   > If not at specified, adjust with the DP adjusting screw.
5. **Reinstall DP separater, filter and cap.**
6. **Check VTV operation.** Race the engine at **2,500 rpm** for a few seconds, release
   the throttle valve and check that the engine returns to idle in a few seconds.

### Exhaust Gas Recirculation (EGR) System (4A-GE)

To reduce NOx emissions, part of the exhaust gases are recirculated through the EGR valve
to the intake manifold to lower the maximum combustion temperature.

*(Figure: EGR system layout and vacuum diagrams (1)–(4), 4A-GE — EGR vacuum modulator,
EGR valve, EGR gas temp. sensor (Calif. only), VSV, vacuum tank, check valve, BVSV,
distributor, pressure chamber from exhaust manifold — see page images p.184–185
(EC-10, EC-11).)*

#### System operation

| Coolant temp. | BVSV | Engine rpm | VSV | Throttle valve opening angle | Pressure in EGR valve pressure chamber | EGR vacuum modulator | EGR valve | Exhaust gas |
| ------------- | ---- | ---------- | --- | ---------------------------- | -------------------------------------- | -------------------- | --------- | ----------- |
| Below 35°C (95°F) | CLOSED | — | — | — | — | — | CLOSED | Not recirculated |
| Above 54°C (129°F) | OPEN | Below 4,350 rpm | ON | Positioned below E port | — | — | CLOSED | Not recirculated |
| Above 54°C (129°F) | OPEN | Below 4,350 rpm | ON | Positioned between E port and R port | (1) LOW \* | OPENS passage to atmosphere | CLOSED | Not recirculated |
| Above 54°C (129°F) | OPEN | Below 4,350 rpm | ON | Positioned between E port and R port | (2) HIGH \* | CLOSES passage to atmosphere | OPEN | Recirculated |
| Above 54°C (129°F) | OPEN | Below 4,350 rpm | ON | Positioned above R port | (3) HIGH \*\* | CLOSES passage to atmosphere | OPEN | Recirculated (increase) |
| Above 54°C (129°F) | OPEN | Above 4,350 rpm | (4) OFF | — | — | — | CLOSED | Not recirculated |

> \* At (1)/(2) the exhaust pressure constantly alternates between low and high.
> Pressure increase → modulator closes → EGR valve opens → pressure drops → EGR valve
> closes → modulator opens.
>
> \*\* When the throttle valve is positioned above the R port, the EGR vacuum modulator
> will close the atmosphere passage and open the EGR valve to increase the EGR gas, even
> if the exhaust pressure is insufficiently low.

#### Inspection of EGR system

1. **Check and clean filters in EGR vacuum modulator.**
   1. Check the filter for contamination or damage.
   2. Using compressed air, clean the filters.
2. **Preparation.** Using a 3-way connector, connect a vacuum gauge to the hose between
   the EGR valve and EGR vacuum modulator.
3. **Check seating of EGR valve.** Start the engine and check that the engine starts and
   runs at idle.
4. **Check BVSV with cold engine.**
   1. The coolant temperature should be below **35°C (95°F)**.
   2. Check that the vacuum gauge indicates zero at **3,500 rpm**.
5. **Check BVSV, VSV and EGR vacuum modulator with hot engine.**
   1. Warm up the engine.
   2. Check that the vacuum gauge indicates low vacuum at **3,500 rpm**.
   3. Check that the vacuum gauge indication is zero at **5,000 rpm**.
   4. Disconnect the vacuum hose from R port of the EGR vacuum modulator and connect R
      port directly to the intake manifold with another hose.
   5. Check that the vacuum gauge indicates high vacuum at **3,500 rpm**.

      > **NOTE:** As a large amount of EGR gas enters, the engine will misfire slightly.
   6. Disconnect the vacuum gauge and reconnect the vacuum hoses to the proper locations.
6. **Check EGR valve.**
   1. Apply vacuum directly to the EGR valve with the engine idling.
   2. Check that the engine runs rough or dies.
   3. Reconnect the vacuum hoses to the proper location.

   > If no problem is found with this inspection, the system is okay; otherwise inspect
   > each part.

#### Inspection of EGR valve

1. **Remove EGR valve.** Check the valve for sticking and heavy carbon deposits. If a
   problem is found, replace it.
2. **Reinstall EGR valve with a new gasket.**

#### Inspection of EGR vacuum modulator

**Check EGR vacuum modulator operation:**

1. Disconnect the vacuum hoses from ports P, Q and R of the EGR vacuum modulator.
2. Block ports P and R with your finger.
3. Blow air into port Q. Check that the air passes through to the air filter side freely.
4. Start the engine and maintain an engine speed of **3,500 rpm**.
5. Repeat the above test. Check that there is a strong resistance to air flow.
6. Reconnect the vacuum hoses to the proper locations.

#### Inspection of BVSV (EGR)

**Check BVSV by blowing air into pipe:**

1. Drain the coolant from the cylinder block into a suitable container.
2. Remove the BVSV.
3. Cool the BVSV to **below 35°C (95°F)** with cool water.
4. Blow air into the pipe and check that the BVSV is **closed**.
5. Heat the BVSV to **above 54°C (129°F)** with hot water.
6. Blow air into the pipe and check that the BVSV is **open**.

   > If a problem is found, replace the BVSV.
7. Apply liquid sealer to the threads of the BVSV and reinstall.
8. Fill the cylinder block with coolant.

#### Inspection of VSV (EGR)

1. **Check vacuum circuit continuity in VSV by blowing air into pipe.**
   1. Connect the VSV terminals to the battery terminals as illustrated.
   2. Blow into pipe E and check that air comes out of pipe F.
   3. Disconnect the battery.
   4. Blow into pipe E and check that air comes out of air filter.

   > If a problem is found, repair or replace the VSV.
2. **Check for short circuit.** Using an ohmmeter, check that there is no continuity
   between the terminal and the VSV body. If there is continuity, replace the VSV.
3. **Check for open circuit.** Using an ohmmeter, measure the resistance between the
   terminals as shown.

   > **Specified resistance: 33 – 39 Ω at 20°C (68°F)**
   >
   > If resistance is not within specification, replace the VSV.

#### Inspection of check valve (EGR)

**Check valve by blowing air into each pipe:**

1. Check that air flows from the orange pipe to the black pipe.
2. Check that air does not flow from the black pipe to the orange pipe.

> If a problem is found, replace the check valve.

### Exhaust Gas Recirculation (EGR) System (4A-GZE)

To reduce NOx emissions, part of the exhaust gases are recirculated through the EGR valve
to the intake manifold to lower the maximum combustion temperature.

*(Figure: EGR system layout and vacuum diagrams (1)–(3), 4A-GZE — EGR vacuum modulator,
EGR gas temp. sensor (Calif. only), E port, R port, VSV, distributor, EGR valve — see
page images p.190–191 (EC-16, EC-17).)*

#### System operation

| Coolant temp. | Engine rpm | Intake air volume | VSV | Throttle valve opening angle | Pressure in EGR valve pressure chamber | EGR vacuum modulator | EGR valve | Exhaust gas |
| ------------- | ---------- | ----------------- | --- | ---------------------------- | -------------------------------------- | -------------------- | --------- | ----------- |
| M/T Below 44°C (111°F); A/T Below 35°C (95°F) | — | — | OFF | — | — | — | CLOSED | Not recirculated |
| M/T Above 50°C (122°F); A/T Above 40°C (104°F) | Above 4,200 rpm | — | OFF | — | — | — | CLOSED | Not recirculated |
| M/T Above 50°C (122°F); A/T Above 40°C (104°F) | Blow 3,800 rpm <!-- NEEDS REVIEW: source prints "Blow 3,800 rpm"; 300-dpi page image confirms "Blow", but by parallel with the 4A-GE table ("Below 4,350 rpm") this is almost certainly an original-manual typo for "Below 3,800 rpm" --> | LOW | OFF | — | — | — | CLOSED | Not recirculated |
| M/T Above 50°C (122°F); A/T Above 40°C (104°F) | Blow 3,800 rpm | HIGH | ON | Positioned below E port | — | — | CLOSED | Not recirculated |
| M/T Above 50°C (122°F); A/T Above 40°C (104°F) | Blow 3,800 rpm | HIGH | ON | Positioned between E port and R port | (1) LOW \* | OPENS passage to atmosphere | CLOSED | Not recirculated |
| M/T Above 50°C (122°F); A/T Above 40°C (104°F) | Blow 3,800 rpm | HIGH | ON | Positioned between E port and R port | (2) HIGH \* | CLOSES passage to atmosphere | OPEN | Recirculated |
| M/T Above 50°C (122°F); A/T Above 40°C (104°F) | Blow 3,800 rpm | HIGH | ON | Positioned above R port | (3) HIGH \*\* | CLOSES passage to atmosphere | OPEN | Recirculated (increase) |

> \* At (1)/(2) the exhaust pressure constantly alternates between low and high.
> Pressure increase → modulator closes → EGR valve opens → pressure drops → EGR valve
> closes → modulator opens.
>
> \*\* When the throttle valve is positioned above the R port, the EGR vacuum modulator
> will close the atmosphere passage and open the EGR valve to increase the EGR gas, even
> if the exhaust pressure is insufficiently low.

#### Inspection of EGR system

1. **Check and clean filter in EGR vacuum modulator.**
   1. Check the filter for contamination or damage.
   2. Using compressed air, clean the filter.
2. **Preparation.** Using a 3-way connector, connect a vacuum gauge to the hose between
   the EGR valve and EGR vacuum modulator.
3. **Check seating of EGR valve.** Start the engine and check that the engine starts and
   runs at idle.
4. **Check VSV with cold engine.**
   1. (M/T) The coolant temperature should be below **44°C (111°F)**.
   2. (A/T) The coolant temperature should be below **35°C (95°F)**.
   3. Check that the vacuum gauge indicates zero at **3,500 rpm**.
5. **Check VSV and EGR vacuum modulator with hot engine.**
   1. Warm up the engine.
   2. Check that the vacuum gauge indicates low vacuum at **3,500 rpm**.
   3. Check that the vacuum gauge indication is zero at **5,000 rpm**.
   4. Disconnect the vacuum hose from R port of the EGR vacuum modulator and connect R
      port directly to the intake manifold with another hose.
   5. Check that the vacuum gauge indicates high vacuum at **3,500 rpm**.

      > **NOTE:** As a large amount of EGR gas enters, the engine will misfire slightly.
   6. Disconnect the vacuum gauge and reconnect the vacuum hoses to the proper locations.
6. **Check EGR valve.**
   1. Apply vacuum directly to the EGR valve with the engine idling.
   2. Check that the engine runs rough or dies.
   3. Reconnect the vacuum hoses to the proper location.

   > If no problem is found with this inspection, the system is okay; otherwise inspect
   > each part.

#### Inspection of EGR valve

1. **Remove EGR valve.** Check the valve for sticking and heavy carbon deposits. If a
   problem is found, replace it.
2. **Reinstall EGR valve with a new gasket.**

#### Inspection of EGR vacuum modulator

**Check EGR vacuum modulator operation:**

1. Disconnect the vacuum hoses from ports P, Q and R of the EGR vacuum modulator.
2. Block ports P and R with your finger.
3. Blow air into port Q. Check that the air passes through to the air filter side freely.
4. Start the engine and maintain an engine speed of **3,500 rpm**.
5. Repeat the above test. Check that there is a strong resistance to air flow.
6. Reconnect the vacuum hoses to the proper locations.

#### Inspection of VSV (EGR)

1. **Check vacuum circuit continuity in VSV by blowing air into pipe.**
   1. Connect the VSV terminals to the battery terminals as illustrated.
   2. Blow into pipe E and check that air comes out of pipe F.
   3. Disconnect the battery.
   4. Blow into pipe E and check that air comes out of air filter.

   > If a problem is found, repair or replace the VSV.
2. **Check for short circuit.** Using an ohmmeter, check that there is no continuity
   between the terminal and the VSV body. If there is continuity, replace the VSV.
3. **Check for open circuit.** Using an ohmmeter, measure the resistance between the
   terminals as shown.

   > **Specified resistance: 33 – 39 Ω at 20°C (68°F)**
   >
   > If resistance is not within specification, replace the VSV.

#### Inspection of water temperature sensor

See EFI System — Water Temperature Sensor (manual page FI-116; in Part 2).

#### Inspection of air flow meter

See EFI System — Air Flow Meter (manual page FI-94; in Part 2).

### Three-Way Catalyst (TWC) System

To reduce HC, CO and NOx emissions, they are oxidized, reduced and converted to nitrogen
(N₂), carbon dioxide (CO₂) and water (H₂O) by the catalyst.

*(Figure: TWC system location — see page image p.196 (EC-21).)*

| Exhaust port | TWC | Exhaust gas |
| ------------ | --- | ----------- |
| HC, CO, and NOx | → Oxidation and reduction → | CO₂, H₂O, N₂ |

#### Inspection of exhaust pipe assembly

1. **Check connections for looseness or damage.**
2. **Check clamps for weakness, cracks or damage.**

#### Inspection of catalytic converter

**Check for dents or damage:** If any part of protector is damaged or dented to the extent
that it contacts the catalyst, repair or replace.

#### Inspection of heat insulator

1. **Check heat insulator for damage.**
2. **Check for adequate clearance between catalytic converter and heat insulator.**

#### Replacement of catalytic converter

1. **Remove converter.**
   1. Jack up the vehicle.
   2. Check that the converter is cool.
   3. Remove the converter protector.
   4. Remove the bolts at the front and rear of the converter.
   5. Remove the converter and gaskets.
2. **Install converter.**
   1. Place new gaskets on the front and rear exhaust pipes, and connect the converter to
      the exhaust pipes.
   2. Install the converter protector.
   3. Tighten the bolts.

      > **Torque:**
      > - Catalyst – Exhaust pipe: **440 kg-cm (32 ft-lb, 43 N·m)**
      > - Protector – Bracket: **195 kg-cm (14 ft-lb, 19 N·m)**
   4. Reinstall the bracket bolts and tighten them.

---

## EFI System

### Description

The EFI system is composed of 3 basic subsystems: Fuel Induction, Air Induction and
Electronic Control.

*(Figure: EFI system component overview, 4A-GE and 4A-GZE — ignition switch, "CHECK ENGINE"
warning light, battery, fuel tank, fuel pulsation damper (4A-GZE), oxygen sensor, air temp.
sensor (inlet air temp.), auxiliary air valve, throttle position sensor, control valve
(T-VIS), start injector time switch, water temp. sensor, EGR gas temp. sensor, neutral
start switch (A/T), check connector (T-E1) — see page images p.197–199 (FI-2 to FI-4).)*

#### Fuel system

An electric fuel pump supplies sufficient fuel, under a constant pressure, to the
injectors. These injectors inject a metered quantity of fuel into the intake manifold in
accordance with signals from the ECU (Electronic Control Unit).

#### Air induction system

The air induction system provides sufficient air for engine operation.

#### Electronic control system

The 4A-GE and 4A-GZE engine is equipped with a Toyota Computer Control System (TCCS) which
centrally controls the EFI, ESA, Diagnosis systems, etc. by means of an Electronic Control
Unit (ECU — formerly EFI computer) employing a microcomputer.

By the ECU, the TCCS controls the following functions:

1. **Electronic Fuel Injection (EFI).** The ECU receives signals from various sensors
   indicating changing engine operating conditions such as: intake air volume, intake air
   temperature, coolant temperature, engine rpm, acceleration/deceleration, exhaust oxygen
   content, etc. These signals are utilized by the ECU to determine the injection duration
   necessary for an optimum air-fuel ratio.
2. **Electronic Spark Advance (ESA).** The ECU is programmed with data for optimum ignition
   timing under any and all operating conditions. Using data provided by sensors which
   monitor various engine functions (rpm, A/C signal, coolant temperature, etc.), the
   microcomputer (ECU) triggers the spark at precisely the right instant. (See IG section.)
3. **Diagnosis.** The ECU detects any malfunctions or abnormalities in the sensor network
   and lights a "CHECK ENGINE" warning light on the instrument panel. At the same time, the
   trouble is identified and a diagnostic code is recorded by the ECU. The diagnostic code
   can be read by the number of blinks of the "CHECK ENGINE" warning light when terminals T
   and E1 are short-circuited. There are 13 (Calif.) or 14 (Ex. Calif.) different diagnostic
   codes, including "normal operation." (See [Diagnostic Codes](#diagnostic-codes-4a-ge).)
4. **Fail-Safe Function.** In the event of a sensor malfunction, a back-up circuit will take
   over to provide minimal drivability. Simultaneously the "CHECK ENGINE" warning light is
   activated.

### Precautions

1. Before working on the fuel system, disconnect the negative terminal from the battery.

   > **NOTE:** Any diagnosis code retained by the computer will be erased when the battery
   > terminal is removed. Therefore read the diagnosis before removing the battery terminal.
2. Do not smoke or work near an open flame when working on the fuel system.
3. Keep gasoline off rubber or leather parts.

### Inspection Precautions

#### Maintenance precautions

1. **Insure correct engine tune-up.**
2. **Precautions when connecting gauge.**
   1. Connect the tachometer (+) terminal to the ignition coil (−) terminal.
   2. Use the battery as the power source for the timing light, tachometer, etc.
3. **In event of engine misfire the following precautions should be taken.**
   1. Insure proper connection of battery terminals, etc.
   2. Handle high-tension cords carefully.
   3. After repair work, insure that the ignition coil terminals and all other ignition
      system lines are reconnected securely. When cleaning the engine compartment, be
      especially careful to protect the electrical system from water.
4. **Precautions when handling oxygen sensor.**
   1. Do not allow oxygen sensor to drop or hit against an object.
   2. Do not allow water to come into contact with the sensor or attempt to cool it.

#### If car is equipped with mobile radio system (HAM, CB, etc.)

The ECU has been designed so that it will not be affected by outside interference. However,
if your vehicle is equipped with a CB radio transceiver, etc. (even one with about 10 W
output), it may, at times, have an effect upon ECU operation, especially if the antenna and
feeder are installed nearby. Therefore, observe the following precautions:

1. Install the antenna as far as possible from the ECU. The ECU is located at the trunk
   center, so the antenna should be installed on the front or rear side of the vehicle.
2. Keep the antenna feeder as far away as possible from the ECU wires — at least
   **20 cm (7.87 in.)** — and do not wind them together.
3. Insure that the feeder and antenna are properly adjusted.
4. Do not equip your vehicle with a powerful mobile radio system.

#### Air induction system

1. Make sure that the oil dipstick, oil filler cap, PCV hose, etc. are all securely fitted,
   otherwise the engine may run out of tune.
2. Disconnection, looseness or cracks in the parts of the air intake system between the air
   flow meter and cylinder head will allow air suction and cause the engine to run out of
   tune.

#### Electronic control system

1. Before removing EFI wiring connectors, terminals, etc., first disconnect the power by
   either turning OFF the ignition switch or disconnecting the battery terminals.
2. When installing a battery, be especially careful not to incorrectly connect the positive
   and negative cables.
3. Do not permit parts to receive a severe impact during removal or installation. Handle
   all EFI parts carefully, especially the ECU.
4. Do not be careless during troubleshooting as there are numerous transistor circuits and
   even slight terminal contact can cause further troubles.
5. Do not open the ECU cover.
6. When inspecting during rainy weather, take care to prevent entry of water. Also, when
   washing the engine compartment, prevent water from getting on the EFI parts and wiring
   connectors.
7. Parts should be replaced as an assembly.
8. Care is required when pulling out and inserting wiring connectors.
   1. Release the lock and pull out the connector, pulling on the connectors.
   2. Fully insert the connector and insure that it is locked.
9. When inspecting a connector with a circuit tester:
   1. Carefully take out the water-proofing rubber if it is a water-proof type connector.
   2. Insert the tester probe into the connector from the wiring side when checking the
      continuity, amperage or voltage.
   3. Do not apply unnecessary force to the terminal.
   4. After checking, install the water-proofing rubber on the connector securely.
10. Use SST for inspection or test of the injector, cold start injector or its wiring
    connector.

    > **SST 09842-30050 (A), 09842-30060 (B) (4A-GZE) and 09842-30070 (C) (4A-GE)**

#### Fuel system

1. When disconnecting the high fuel pressure line, a large amount of gasoline will spill
   out so observe the following procedure.
   1. Put a container under the connection.
   2. Slowly loosen the connection.
   3. Disconnect the connection.
   4. Plug the connection with a rubber plug.
2. When connecting the flare nut or union bolt on the high pressure pipe union, observe the
   following procedure:

   **(Union bolt type)**
   1. Always use a new gasket.
   2. First tighten the union bolt by hand.
   3. Then tighten the bolt to the specified torque.

      > **Torque: 300 kg-cm (22 ft-lb, 29 N·m)**

   **(Flare nut type)**
   1. Apply a thin coat of oil to the flare and tighten the flare nut.
   2. Then using SST, tighten the nut to the specified torque.

      > **Torque: 310 kg-cm (22 ft-lb, 30 N·m)**
      >
      > **NOTE:** Use a torque wrench with a fulcrum length of **30 cm (11.81 in.)**.
3. Observe the following precautions when removing and installing the injectors.
   1. Never reuse an O-ring.
   2. When placing an O-ring on the injector, use care not to damage it in any way.
   3. Lubricate the O-ring with spindle oil or gasoline before installing — never use
      engine, gear or brake oil.
4. Install the injector to the delivery pipe and cylinder head as shown in the figure.
5. Confirm that there are no fuel leaks after performing any maintenance on the fuel system.
   1. With engine stopped, turn the ignition switch to ON.
   2. Short circuit the fuel pump check terminals (FP – +B) in the check connector.

      > **NOTE:** The check connector is located near the resonator (4A-GE) or intercooler
      > (4A-GZE).
   3. When the fuel return hose is pinched, the pressure within the high pressure line will
      rise to about **4 kg/cm² (57 psi, 392 kPa)**. In this state, check to see that there
      are no leaks from any part of the fuel system.

      > **CAUTION:** Always pinch the hose. Avoid bending as it may cause the hose to crack.

### Troubleshooting

#### Troubleshooting hints

1. Engine troubles are usually not caused by the EFI system. When troubleshooting, always
   first check the condition of the other systems:
   - **Electronic source** — battery, fusible links, fuses
   - **Body ground**
   - **Fuel supply** — fuel leakage, fuel filter, fuel pump
   - **Ignition system** — spark plugs, high-tension cords, distributor, igniter and
     ignition coil
   - **Air induction system** — vacuum leaks
   - **Others** — ignition timing (ESA system), idle speed, etc.
2. The most frequent cause of problems is simply a bad contact in wiring connectors. Always
   make sure that connections are secure. When inspecting the connector, pay particular
   attention to the following points:
   1. Check to see that the terminals are not bent.
   2. Check to see that the connector is pushed in completely and locked.
   3. Check to see that there is no signal change when the connector is slightly tapped or
      wiggled.
3. Sufficiently troubleshoot for other causes before replacing the ECU, as the ECU is of
   high quality and is expensive.
4. Use a volt/ohmmeter with high impedance (**10 kΩ/V minimum**) for troubleshooting of the
   electrical circuit. (See [Diagnosis System](#diagnosis-system), manual page FI-26.)

#### Troubleshooting procedures

Each symptom is a diagnostic tree. Work down the **Check** column in order: if a check is
**OK**, proceed to the next check; if a check is **BAD / NO**, inspect the listed trouble
areas in the "Inspect if BAD/NO" column.

##### Symptom — Difficult to start or no start (engine will not crank or cranks slowly)

| Step | Check | Inspect if BAD / NO |
| ---- | ----- | ------------------- |
| 1 | Check electric source | 1. Battery — (1) connection, (2) gravity / drive belt / charging system, (3) voltage. 2. Fusible link |
| 2 | Check starting system | 1. Ignition switch. 2. Clutch (M/T) or neutral start switch (A/T). 3. Starter relay. 4. Starter. 5. Wiring/connection |

##### Symptom — Difficult to start or no start (cranks OK)

| Step | Check | Inspect if BAD / NO (or malfunction) |
| ---- | ----- | ------------------------------------ |
| 1 | Check diagnosis system — check for output of diagnosis code (see FI-21) | Diagnosis code(s) — see [Diagnostic Codes](#diagnostic-codes-4a-ge) (FI-24 to 27) |
| 2 | Check for vacuum leaks in air induction system | 1. Oil filler cap. 2. Oil level gauge. 3. Hose connections. 4. PCV hose. 5. EGR system — EGR valve stays open |
| 3 | Check ignition spark — unplug connectors of injector and start injector time switch; hold spark plug cord 8–10 mm (0.31–0.39 in.) from engine block while cranking; a strong spark should be noted | 1. High-tension cords. 2. Distributor. 3. Ignition coil, igniter |
| 4 | Check ignition timing — short terminals T and E1 of check connector; STD: **10° BTDC @ idling** (w/ short-circuited T and E1) | Ignition timing — adjust (see IG-11) |
| 5 | Check fuel supply to injector — (1) short terminals FP and +B of check connector; (2) fuel pressure at fuel return hose can be felt (see FI-65 or 68) | 1. Fuel line — leakage / deformation. 2. Fuse. 3. Circuit opening relay (FI-111). 4. Fuel pump (FI-64). 5. Fuel filter. 6. Fuel pressure regulator (FI-78 or 79) |
| 6 | Check fuel pump switch in air flow meter — check continuity between terminals Fc and E1 while measuring plate of air flow meter is open | Air flow meter (FI-94) |
| 7 | Check spark plugs — plug gap **1.1 mm (0.043 in.)**; also check compression and valve clearance if necessary (see EM-14) | 1. Spark plug. 2. Compression pressure — limit (at 250 rpm): 4A-GE **10.0 kg/cm² (142 psi, 981 kPa)**, 4A-GZE **8.5 kg/cm² (120 psi, 834 kPa)**. 3. Valve clearance (cold) STD: IN **0.15–0.25 mm (0.006–0.010 in.)**, EX **0.20–0.30 mm (0.008–0.012 in.)**. — If plugs WET: 1. injector(s) shorted or leaking; 2. injector wiring between resistor and ECU shorted; 3. cold start injector leakage (FI-73); 4. start injector time switch (FI-115) |
| 8 | Check auxiliary air valve (4A-GE) (FI-108) | 1. Air valve. 2. Water hoses |
| 9 | Check ISC valve (4A-GZE) (FI-106) | 1. ISC valve. 2. Wiring connection (FI-60). 3. A/C switch |
| 10 | Check EFI electronic circuit using volt/ohmmeter (FI-33 or 48) | 1. Wiring connection. 2. Power to computer (ECU) — (1) fusible links, (2) fuses, (3) EFI main relay. 3. Air flow meter. 4. Water temperature sensor. 5. Air temperature sensor (in air flow meter). 6. Injection signal circuit — (1) injector wiring, (2) computer (ECU), (3) resistor (4A-GZE) |

##### Symptom — Engine often stalls

| Step | Check | Inspect if BAD / NO |
| ---- | ----- | ------------------- |
| 1 | Check diagnosis system (FI-21) | Diagnostic code(s) (FI-24 to 27) |
| 2 | Check for vacuum leaks in air intake line | 1. Oil filler cap. 2. Oil level gauge. 3. Hose connections. 4. PCV hose. 5. EGR system — EGR valve stays open |
| 3 | Check fuel supply to injector — (1) short terminals FP and +B of service connector; (2) fuel pressure can be felt at fuel hose of fuel filter (see FI-65 or 68) | 1. Fuel line — leakage / deformation. 2. Fuse. 3. Circuit opening relay (FI-111). 4. Fuel pump (FI-64). 5. Fuel filter. 6. Fuel pressure regulator (FI-78 or 79) |
| 4 | Check air filter element | Element — clean or replace |
| 5 | Check idle speed — STD: **800 rpm** | Idle speed — adjust (4A-GE); ISC system (4A-GZE) |
| 6 | Check ignition timing — short T and E1; STD: **10° BTDC @ idling** (w/ short-circuited T–E1) | Ignition timing — adjust (IG-11) |
| 7 | Check spark plugs — plug gap **1.1 mm (0.043 in.)**; check compression/valve clearance if necessary (EM-14) | 1. Spark plug. 2. Compression pressure — limit (at 250 rpm): 4A-GE **10.0 kg/cm² (142 psi, 981 kPa)**, 4A-GZE **8.5 kg/cm² (120 psi, 834 kPa)**. 3. Valve clearance (cold) STD: IN **0.15–0.25 mm (0.006–0.010 in.)**, EX **0.20–0.30 mm (0.008–0.012 in.)** |
| 8 | Check cold start injector (FI-73) | 1. Cold start injector. 2. Start injector time switch (FI-115) |
| 9 | Check auxiliary air valve (4A-GE) (FI-108) | 1. Air valve. 2. Water hoses |
| 10 | Check ISC valve (4A-GZE) (FI-106) | 1. ISC valve. 2. Wiring connection (FI-60). 3. A/C switch |
| 11 | Check fuel pressure (FI-65 or 68) | 1. Fuel pump (FI-64). 2. Fuel filter. 3. Fuel pressure regulator (FI-78 or 79) |
| 12 | Check injectors (FI-80) | Injection condition |
| 13 | Check EFI electronic circuit using volt/ohmmeter (FI-33 or 48) | 1. Wiring connection. 2. Power to computer (ECU) — (1) fusible links, (2) fuses, (3) EFI main relay. 3. Air flow meter. 4. Water temperature sensor. 5. Air temperature sensor (in air flow meter). 6. Injection signal circuit — (1) injector wiring, (2) computer (ECU), (3) resistor (4A-GZE) |

##### Symptom — Engine sometimes stalls

| Step | Check | Inspect if BAD / NO |
| ---- | ----- | ------------------- |
| 1 | Check diagnosis system (FI-21) | Diagnostic code(s) (FI-24 to 27) |
| 2 | Check air flow meter (FI-94) | Air flow meter |
| 3 | Check wiring connectors and relays — check that there is a signal change when the connector or relay is slightly tapped or wiggled | 1. Connector. 2. EFI main relay (FI-110). 3. Circuit opening relay (FI-111) |

##### Symptom — Rough idling and/or missing

| Step | Check | Inspect if BAD / NO |
| ---- | ----- | ------------------- |
| 1 | Check diagnosis system (FI-21) | Diagnostic code(s) (FI-24 to 27) |
| 2 | Check for vacuum leaks in air intake line | 1. Oil filler cap. 2. Oil level gauge. 3. Hose connections. 4. PCV hose. 5. EGR system — EGR valve stays open |
| 3 | Check air filter element | Element — clean or replace |
| 4 | Check idle speed — STD: **800 rpm** | Idle speed — adjust (4A-GE); ISC system (4A-GZE) |
| 5 | Check ignition timing — short T and E1; STD: **10° BTDC @ idling** (w/ short-circuited T–E1) | Ignition timing — adjust (IG-11) |
| 6 | Check spark plugs — plug gap **1.1 mm (0.043 in.)**; check compression/valve clearance if necessary (EM-14) | 1. Spark plug. 2. Compression pressure — limit (at 250 rpm): 4A-GE **10.0 kg/cm² (142 psi, 981 kPa)**, 4A-GZE **8.5 kg/cm² (120 psi, 834 kPa)**. 3. Valve clearance (cold) STD: IN **0.15–0.25 mm (0.006–0.010 in.)**, EX **0.20–0.30 mm (0.008–0.012 in.)** |
| 7 | Check air control valve (4A-GE) — check that the air control valve is closed | 1. VSV for air control valve. 2. Vacuum leaks |
| 8 | Check ISC valve (4A-GZE) (FI-106) | 1. ISC valve. 2. Wiring connection (FI-60). 3. A/C switch |
| 9 | Check cold start injector (FI-73) | 1. Cold start injector. 2. Start injector time switch (FI-115) |
| 10 | Check fuel pressure (FI-65 or 68) | 1. Fuel pump (FI-64). 2. Fuel filter. 3. Fuel pressure regulator (FI-78 or 79) |
| 11 | Check injectors (FI-80) | Injection condition |
| 12 | Check EFI electronic circuit using volt/ohmmeter (FI-33 or 48) | 1. Wiring connection. 2. Power to computer (ECU) — (1) fusible link, (2) fuses, (3) EFI main relay. 3. Air flow meter. 4. Water temperature sensor. 5. Air temperature sensor (in air flow meter). 6. Injection signal circuit — (1) injector wirings, (2) computer (ECU), (3) resistor (4A-GZE). 7. Oxygen sensor |

##### Symptom — High engine idle speed (no drop)

| Step | Check | Inspect if BAD / NO |
| ---- | ----- | ------------------- |
| 1 | Check accelerator linkage | Linkage — stuck dash pot system |
| 2 | Check auxiliary air valve (4A-GE) (FI-108) | 1. Air valve. 2. Water hoses |
| 3 | Check ISC valve (4A-GZE) (FI-106) | 1. ISC valve. 2. Wiring connection (FI-60). 3. A/C switch |
| 4 | Check air conditioner idle-up circuit | Air valve for air conditioner — leakage; VSV for air conditioner — leakage |
| 5 | Check diagnosis system (FI-21) | Diagnosis code(s) (FI-24 to 27) |
| 6 | Check throttle position sensor (FI-98) | Throttle body |
| 7 | Check fuel pressure (FI-65 or 68) | Fuel pressure regulator — high pressure |
| 8 | Check cold start injector (FI-73) | Cold start injector — leakage |
| 9 | Check injectors (FI-80) | Injectors — leakage, injection quality |
| 10 | Check EFI electronic circuit using volt/ohmmeter (FI-33 or 48) | 1. Wiring connection. 2. Power to computer (ECU) — (1) fusible links, (2) fuses, (3) EFI main relay. 3. Air flow meter. 4. Water temperature sensor. 5. Air temperature sensor (in air flow meter). 6. Injection signal circuit — (1) injector wiring, (2) computer (ECU), (3) resistor (4A-GZE) |

##### Symptom — Engine backfires (lean fuel mixture)

| Step | Check | Inspect if BAD / NO |
| ---- | ----- | ------------------- |
| 1 | Check diagnosis system (FI-21) | Diagnosis code(s) (FI-24 to 27) |
| 2 | Check for vacuum leaks in air intake line | 1. Oil filler cap. 2. Oil level gauge. 3. Hose connections. 4. PCV hoses. 5. EGR system — EGR valve stays open |
| 3 | Check ignition timing — short T and E1; STD: **10° BTDC @ idling** (w/ short-circuited T–E1) | Ignition timing — adjust (IG-11) |
| 4 | Check idle speed — STD: **800 rpm** | Idle speed — adjust (4A-GE); ISC system (4A-GZE) |
| 5 | Check cold start injector (FI-73) | 1. Cold start injector. 2. Start injector time switch (FI-115) |
| 6 | Check fuel pressure (FI-65 or 68) | 1. Fuel pump (FI-64). 2. Fuel filter. 3. Fuel pressure regulator (FI-78 or 79) |
| 7 | Check injectors (FI-80) | Injectors — clogged |
| 8 | Check EFI electronic circuit using volt/ohmmeter (FI-33 or 48) | 1. Wiring connection. 2. Power to computer (ECU) — (1) fusible links, (2) fuses, (3) EFI main relay. 3. Air flow meter. 4. Water temperature sensor. 5. Air temperature sensor (in air flow meter). 6. Throttle position sensor. 7. Injection signal circuit — (1) injector wirings, (2) computer (ECU), (3) fuel cut signal, (4) resistor (4A-GZE). 8. Oxygen sensor |

##### Symptom — Muffler explosion (after fire) — rich fuel mixture / misfire

| Step | Check | Inspect if BAD / NO |
| ---- | ----- | ------------------- |
| 1 | Check diagnosis system (FI-21) | Diagnosis code(s) (FI-24 to 27) |
| 2 | Check ignition timing — short T and E1; STD: **10° BTDC @ idling** (w/ short-circuited T–E1) | Ignition timing — adjust (IG-11) |
| 3 | Check idle speed — STD: **800 rpm** | Idle speed — adjust (4A-GE); ISC system (4A-GZE) |
| 4 | Check cold start injector (FI-115) | 1. Cold start injector. 2. Start injector time switch (FI-115) |
| 5 | Check fuel pressure (FI-65 or 68) | Fuel pressure regulator |
| 6 | Check injectors (FI-80) | Injectors — leakage |
| 7 | Check spark plugs — plug gap **1.1 mm (0.043 in.)**; check compression/valve clearance if necessary (EM-14) | 1. Spark plug. 2. Compression pressure — limit (at 250 rpm): 4A-GE **10.0 kg/cm² (142 psi, 981 kPa)**, 4A-GZE **8.5 kg/cm² (120 psi, 834 kPa)**. 3. Valve clearance (cold) STD: IN **0.15–0.25 mm (0.006–0.010 in.)**, EX **0.20–0.30 mm (0.008–0.012 in.)** |
| 8 | Check EFI electronic circuit using volt/ohmmeter (FI-33 or 48) | 1. Throttle position sensor. 2. Injection signal — (1) injector wiring, (2) fuel cut RPM (FI-128), (3) computer (ECU), (4) resistor (4A-GZE). 3. Oxygen sensor |

##### Symptom — Engine hesitates and/or poor acceleration

| Step | Check | Inspect if BAD / NO |
| ---- | ----- | ------------------- |
| 1 | Check clutch or brake | 1. Clutch — slips. 2. Brakes — drag |
| 2 | Check for vacuum leaks in air intake line | 1. Oil filler cap. 2. Oil level gauge. 3. Hose connections. 4. PCV hose. 5. EGR system — EGR valve stays open |
| 3 | Check air filter element | Element — clean or replace |
| 4 | Check diagnosis system (FI-21) | Diagnosis code(s) (FI-24 to 27) |
| 5 | Check ignition spark — unplug connectors of injector and start injection time switch; hold spark plug 8–10 mm (0.31–0.39 in.) from engine block while cranking; a strong spark should be noted | 1. High-tension cords. 2. Distributor. 3. Ignition coil, igniter |
| 6 | Check ignition timing — short T and E1; STD: **10° BTDC @ idling** (w/ short-circuited T–E1) | Ignition timing — adjust (IG-11) |
| 7 | Check fuel pressure (FI-65 or 68) | 1. Fuel pump (FI-64). 2. Fuel filter. 3. Fuel pressure regulator (FI-78 or 79) |
| 8 | Check injectors (FI-80) | Injection condition |
| 9 | Check spark plugs — plug gap **1.1 mm (0.043 in.)**; check compression/valve clearance if necessary (EM-14) | 1. Spark plug. 2. Compression pressure — limit (at 250 rpm): 4A-GE **10.0 kg/cm² (142 psi, 981 kPa)**, 4A-GZE **8.5 kg/cm² (120 psi, 834 kPa)**. 3. Valve clearance (cold) STD: IN **0.15–0.25 mm (0.006–0.010 in.)**, EX **0.20–0.30 mm (0.008–0.012 in.)** |
| 10 | Check air control valve (4A-GE) — check if air control valve is open with engine running at **4,350 rpm** or above | VSV for air control valve |
| 11 | Check EFI electronic circuit using volt/ohmmeter (FI-33 or 48) | 1. Wiring connection. 2. Power to computer (ECU) — (1) fusible link, (2) fuses, (3) EFI main relay. 3. Air flow meter. 4. Water temp. sensor. 5. Air temp. sensor (in air flow meter). 6. Throttle position sensor. 7. Injection signal circuit — (1) injector wirings, (2) computer (ECU), (3) resistor (4A-GZE) |

### Diagnosis System

#### Description

The ECU contains a built-in self-diagnosis system by which troubles with the engine signal
network are detected and indicated by a "CHECK ENGINE" warning light on the instrument
panel flashing. By analyzing various signals as shown in the code tables below, the
Electronic Control Unit (ECU) detects system malfunctions which are related to the various
operating parameter sensors or to actuators. The ECU stores the failure code associated
with the detected failure until the diagnosis system is cleared by removing the AM2 fuse
with the ignition switch off.

A "CHECK ENGINE" warning light on the instrument panel informs the driver that a
malfunction has been detected. The light goes out automatically when the malfunction has
been cleared.

#### "CHECK ENGINE" warning light check

1. The "CHECK ENGINE" warning light will come on when the ignition switch is placed at ON
   and the engine is not running.
2. When the engine is started, the "CHECK ENGINE" warning light should go out. If the light
   remains on, the diagnosis system has detected a malfunction or abnormality in the system.

#### Output of diagnostic codes

To obtain an output of diagnostic codes, proceed as follows:

1. Initial conditions:
   1. Battery voltage above **11 volts**
   2. Throttle valve fully closed (throttle position sensor IDL points closed)
   3. Transmission in neutral position
   4. Accessory switches OFF
   5. Engine at normal operating temperature
2. Turn the ignition switch to ON. Do not start the engine.
3. Using a service wire, short terminals T and E1 of the check connector.

   > **NOTE:** The check connector is located near the resonator (4A-GE) or intercooler
   > (4A-GZE).
4. Read the diagnosis code as indicated by the number of flashes of the "CHECK ENGINE"
   warning light:
   1. **Normal system operation** — the light will blink once every 0.5 seconds.
   2. **Malfunction code indication** — the light will blink a number of times equal to the
      malfunction code as follows:
      - Between the first digit and second digit: **1.5 seconds**
      - Between code and code: **2.5 seconds**
      - Between all malfunction codes: **4.5 seconds**

      The diagnostic code series will be repeated as long as the check connector terminals T
      and E1 are shorted.

      > **NOTE:** In the event of a number of trouble codes, indication will begin from the
      > smaller value and continue in order to the larger.
5. After the diagnosis check, remove the service wire.

#### Cancelling diagnostic code

1. After repair of the trouble area, the diagnosis code retained in memory by the ECU must
   be cancelled out by removing the fuse **AM2 (7.5A)** — located in the engine compartment
   No. 2 relay box — for **10 seconds or more**, depending on ambient temperature (the lower
   the temperature, the longer the fuse must be left out) with the ignition switch off.

   > **NOTE:**
   > - Cancellation can also be done by removing the battery negative (−) terminal, but in
   >   this case, other memory systems (clock, etc.) will also be cancelled out.
   > - If the diagnosis code is not cancelled out, it will be retained by the ECU and
   >   appear along with a new code in the event of future trouble.
   > - If it is necessary to work on engine components requiring removal of the battery
   >   terminal, a check must first be made to see if a diagnostic code has been recorded.
2. After cancellation, perform a road test to confirm that a "normal" code is now read on
   the "CHECK ENGINE" warning light. If the same diagnosis code appears, it indicates that
   the trouble area has not been repaired thoroughly.

#### Diagnostic Codes (4A-GE)

The "number of blinks" of the "CHECK ENGINE" warning light corresponds to the code number
(e.g. code 21 = two blinks, pause, one blink). Codes are listed in the manual's order.

| Code No. | System | Diagnosis | Trouble area | See page |
| -------- | ------ | --------- | ------------ | -------- |
| — | Normal | This appears when none of the other codes are identified. | — | — |
| 12 | RPM Signal | No "Ne" signal to ECU within 2 seconds after engine has been cranked. No "G" signal to ECU 2 times in succession when engine speed is between 500 rpm and 4,000 rpm. | Distributor circuit; Distributor; Starter signal circuit; Igniter circuit; Igniter; ECU | — |
| 13 | RPM Signal | No "Ne" signal to ECU when the engine speed is above 1,500 rpm. | Distributor circuit; Distributor; ECU | — |
| 14 | Ignition Signal | No "IGf" signal to ECU 4 times in succession. | Igniter circuit; Igniter; Igniter and ignition coil circuit; Igniter and ignition coil; ECU | FI-44 |
| 21 | Oxygen Sensor Signal | Detection of oxygen sensor deterioration. | Oxygen sensor circuit; Oxygen sensor; ECU | FI-46 |
| 21 | Oxygen Sensor Heater | Open or short circuit in oxygen sensor heater. | Oxygen sensor heater circuit; Oxygen sensor heater; ECU | FI-46 |
| 22 | Water Temp. Sensor Signal | Open or short circuit in water temp. sensor signal (THW). | Water temp. sensor circuit; Water temp. sensor; ECU | FI-42 |
| 24 | Intake Air Temp. Sensor Signal | Open or short circuit in intake air temp. sensor signal (THA). | Intake air temp. sensor circuit; Intake air temp. sensor; ECU | FI-41 |
| 25 | Air-fuel Ratio Lean Malfunction | When air-fuel ratio feedback compensation value or adaptive control value continues at the upper (lean) or lower (rich) limit renewed for a certain period of time. | Injection circuit; Injector; Oxygen sensor circuit; Oxygen sensor; ECU; Fuel line pressure; Air leak; Air flow meter; Ignition system | FI-46 |
| 26 | Air-fuel Ratio Rich Malfunction | (See code 25.) | Injector circuit; Injector; Oxygen sensor circuit; Oxygen sensor; Fuel line pressure; Air flow meter; Cold start injector; ECU | FI-46 |
| 31 | Air-flow Meter Signal | Short circuit between VC and VB, VC and E2, or VS and VC. | Air flow meter circuit; Air flow meter; ECU | FI-38 |
| 41 | Throttle Position Sensor Signal | Open or short circuit in throttle position signal. | Throttle position sensor circuit; Throttle position sensor; ECU | FI-36 |
| 42 | Vehicle Speed Sensor Signal | No "SPD" signal for 5 seconds when engine speed is above 2,500 rpm. | Vehicle speed sensor circuit; Vehicle speed sensor; ECU | — |
| 43 | Starter Signal | No "STA" signal to ECU until engine speed reaches 800 rpm with vehicle not moving. | IG switch circuit; IG switch; ECU | FI-43 |
| 71\* | EGR System Malfunction | EGR gas temp. below predetermined level during EGR control. | EGR system (EGR valve, EGR hose, etc.); EGR gas temp. sensor circuit; EGR gas temp. sensor; VSV for EGR; VSV for EGR circuit; ECU | FI-47 |
| 51 | Switch Signal | Air conditioner switch ON, idle switch OFF, or A/T shift position other than "P" or "N" range during diagnosis check. | A/C switch circuit; A/C switch; A/C amplifier; Throttle position sensor circuit; Throttle position sensor; ECU | FI-45 |

> \* Code 71 is for California.

#### Diagnostic Codes (4A-GZE)

| Code No. | System | Diagnosis | Trouble area | See page |
| -------- | ------ | --------- | ------------ | -------- |
| — | Normal | This appears when none of the other codes are identified. | — | — |
| 11 | ECU (+B) | Momentary interruption in power supply to ECU. | Ignition switch circuit; Ignition switch; Main relay circuit; Main relay; ECU | FI-49 |
| 12 | RPM Signal | No "Ne" or "G" signal to ECU within 2 seconds after engine has been cranked. | Distributor circuit; Distributor; ECU; Starter signal circuit | — |
| 13 | RPM Signal | No "Ne" signal to ECU when engine speed is above 1,000 rpm. | Distributor circuit; Distributor; ECU | — |
| 14 | Ignition Signal | No "IGf" signal to ECU 8–11 times in succession. | Igniter and ignition coil circuit; Igniter and ignition coil; ECU | FI-59 |
| 21 | Oxygen Sensor | Detection of oxygen sensor deterioration. | Oxygen sensor circuit; Oxygen sensor; ECU | FI-62 |
| 21 | Oxygen Sensor Heater | Open or short circuit in oxygen sensor heater. | Oxygen sensor heater circuit; Oxygen sensor heater; ECU | FI-62 |
| 22 | Water Temp. Sensor Signal | Open or short circuit in water temp. sensor signal. | Water temp. sensor circuit; Water temp. sensor; ECU | FI-57 |
| 24 | Intake Air Temp. Sensor Signal | Open or short circuit in intake air temp. sensor signal. | Intake air temp. sensor circuit; Intake air temp. sensor; ECU | FI-56 |
| 25 | Air-fuel Ratio Lean Malfunction | When air-fuel ratio feedback compensation value or adaptive control value continues at the upper (lean) or lower (rich) limit renewed for a certain period of time. | Injector circuit; Injector; Oxygen sensor circuit; Oxygen sensor; ECU; Air leak; Fuel line pressure; Air flow meter | FI-62 |
| 26 | Air-fuel Ratio Rich Malfunction | (See code 25.) | Injector circuit; Injector; Oxygen sensor circuit; Oxygen sensor; Fuel line pressure; Air flow meter; ECU | FI-62 |
| 31 | Air-flow Meter Signal | Open circuit in VC signal or short circuit between VS and E2 when idle contacts are closed. | Air flow meter circuit; Air flow meter; ECU | FI-53 |
| 32 | Air-flow Meter Signal | Open circuit in E2 or short circuit between VC and VS. | Air flow meter circuit; Air-flow meter; ECU | — |
| 41 | Throttle Position Sensor Signal | Open or short circuit in throttle position sensor signal. | Throttle position sensor circuit; Throttle position sensor | FI-51 |
| 42 | Vehicle Speed Sensor Signal | No "SPD" signal for 8 seconds when engine speed is between 2,300 rpm and 5,000 rpm and coolant temp. is below 80°C (176°F) except when racing the engine. | Vehicle speed sensor circuit; Vehicle speed sensor; ECU | — |
| 43 | Starter Signal | No "STA" signal to ECU until engine speed reaches 800 rpm with vehicle not moving. | IG switch circuit; IG switch; ECU | FI-58 |
| 52 | Knock Sensor Signal | Open or short circuit in knock sensor signal. | Knock sensor circuit; Knock sensor; ECU | — |
| 53 | Knock Control Signal in ECU | Knock control in ECU faulty. | ECU | — |
| 71\* | EGR System Malfunction | EGR gas temp. below predetermined level during EGR operation. | EGR system (EGR valve, EGR hose, etc.); EGR gas temp. sensor circuit; EGR gas temp. sensor; VSV for EGR; VSV for EGR circuit; ECU | FI-63 |
| 51 | Switch Signal | Air conditioner switch ON, idle switch OFF, or A/T shift position other than "P" or "N" range during diagnosis check. | A/C switch circuit; A/C switch; A/C amplifier; Throttle position sensor circuit; Throttle position sensor; ECU | FI-61 |

> \* Code 71 is for California.

#### Inspection of diagnosis circuit

*(Figure: diagnosis circuit — EFI main relay, fuse EFI (15A), ignition switch fuses (AM1,
IG1, TURN, GAG 7.5A), fusible link 1.25B, "CHECK ENGINE" warning light, battery, check
connector, ECU terminals +B, B1, W, T, E1 — see page image p.219 (FI-28).)*

| Step | Check | Result | Action / Go to |
| ---- | ----- | ------ | -------------- |
| 1 | Does "CHECK ENGINE" warning light come on when ignition switch is at ON? | YES | System normal |
| 1 | Does "CHECK ENGINE" warning light come on when ignition switch is at ON? | NO | Go to 2 |
| 2 | Does "CHECK ENGINE" light come on when ECU terminal W is grounded to the body? | YES | Check wiring between ECU terminal E and body ground. If OK → try another ECU. If BAD → repair or replace |
| 2 | Does "CHECK ENGINE" light come on when ECU terminal W is grounded to the body? | NO | Check bulb, fuse and wiring between ECU and ignition switch. If BAD → repair or replace |
| 3 | Does "CHECK ENGINE" warning light go OFF when the engine is started? | YES | System normal — cancel out diagnosis code (if any recorded) |
| 3 | Does "CHECK ENGINE" warning light go OFF when the engine is started? | NO | A malfunction is present — read and repair the diagnostic code, then cancel it out |

### Troubleshooting with Volt/Ohmmeter (4A-GE)

#### Preparation of troubleshooting

1. Remove the rear luggage compartment trim.
2. Remove the ECU with the wire harness.

#### EFI system check procedure

> **NOTE:**
> 1. The EFI circuit can be checked by measuring the resistance and voltage at the wiring
>    connectors of the ECU.
> 2. Perform all voltage measurements with the connectors connected.
> 3. Verify that the battery voltage is **11 V or above** when the ignition switch is at ON.

Using a voltmeter with high impedance (**10 kΩ/V minimum**), measure the voltage at each
terminal of the wiring connector.

> **NOTE:** If there is any problem, see
> [Troubleshooting EFI Electronic Circuit with Volt/Ohmmeter (4A-GE)](#troubleshooting-efi-electronic-circuit-with-voltohmmeter-4a-ge).

##### ECU connector terminals (4A-GE)

| Symbol | Terminal | Symbol | Terminal |
| ------ | -------- | ------ | -------- |
| E01 | Engine ground (Power) | GS\* | Engine revolution sensor |
| E02 | Engine ground (Power) | VCC | Throttle position sensor |
| No. 10 | No. 3, 4 injector | THG\*\* | EGR temperature sensor |
| No. 20 | No. 1, 2 injector | L3\* | ECT computer |
| STA | Starter switch | ECT\* | ECT computer |
| IGT | Igniter | L1\* | ECT computer |
| VF | Service connector | L2\* | ECT computer |
| E1 | Engine ground | VC | Air flow meter |
| NSW\* | Neutral start switch | E21 | Sensor ground |
| S/TH | VSV (T-VIS) | VS | Air flow meter |
| FPU | VSV (FPU) | STP | Stop light switch |
| V-ISC | VSV (ISC) | THA | Inlet air temperature sensor |
| W | Warning light | SPD | Speedometer sensor |
| HT | Oxygen sensor heater | BATT | Battery |
| T | Service connector | +B1 | EFI main relay |
| IDL | Throttle position sensor | +B | EFI main relay |
| A/C | A/C magnet clutch | NE | Engine revolution sensor |
| IGF | Igniter | THW | Water temperature sensor |
| E2 | Sensor ground | VTA | Throttle position sensor |
| G⊖ (Gc3) | Engine revolution sensor | OX | Oxygen sensor |

> \* For A/T. \*\* For Calif.

#### Voltage at ECU wiring connectors (4A-GE)

| No. | Terminals | STD voltage (V) | Condition | See page |
| --- | --------- | --------------- | --------- | -------- |
| 1 | +B1 / +B – E1 | 10 – 14 | Ignition S/W ON | FI-34 |
| 2 | BATT – E1 | 10 – 14 | — | FI-35 |
| 3 | IDL – E2 | 10 – 14 | Ignition S/W ON, throttle valve open | FI-36 |
| 3 | VTA – E2 | 0.1 – 1.0 | Ignition S/W ON, throttle valve fully closed | FI-36 |
| 3 | VTA – E2 | 4 – 5 | Ignition S/W ON, throttle valve fully open | FI-36 |
| 3 | VCC – E2 | 4 – 6 | — | FI-36 |
| 4 | +B1 – E2 | 10 – 14 | Ignition S/W ON | FI-38 |
| 4 | VC – E2 | 6 – 10 | Ignition S/W ON | FI-38 |
| 4 | VS – E2 | 2 – 5.5 | Ignition S/W ON, measuring plate fully closed | FI-38 |
| 4 | VS – E2 | 6 – 9 | Ignition S/W ON, measuring plate fully open | FI-38 |
| 4 | VS – E2 | 2 – 8 | Idling | FI-38 |
| 5 | No. 10 – E01 / No. 20 – E02 | 9 – 14 | Ignition S/W ON | FI-39 |
| 6 | W – E1 | 9 – 14 | No trouble ("CHECK ENGINE" warning light off) and engine running | FI-40 |
| 7 | THA – E2 | 1 – 3 | Ignition S/W ON, intake air temperature 20°C (68°F) | FI-41 |
| 8 | THW – E2 | 0.1 – 1.0 | Ignition S/W ON, coolant temperature 80°C (176°F) | FI-42 |
| 9 | STA – E1 | 6 – 14 | Ignition S/W ST position and press on the clutch pedal (M/T) | FI-43 |
| 10 | IGT – E1 | 0.7 – 1.0 | Idling | FI-44 |
| 11 | A/C – E1 | 5 – 14 | Air conditioning ON | FI-45 |

### Troubleshooting with Volt/Ohmmeter (4A-GZE)

#### Preparation of troubleshooting

1. Remove the rear luggage compartment trim.
2. Remove the ECU with the wire harness.

#### EFI system check procedure

> **NOTE:**
> 1. The EFI circuit can be checked by measuring the resistance and voltage at the wiring
>    connectors of the ECU.
> 2. Perform all voltage measurements with the connectors connected.
> 3. Verify that the battery voltage is **11 V or above** when the ignition switch is at ON.

Using a voltmeter with high impedance (**10 kΩ/V minimum**), measure the voltage at each
terminal of the wiring connector.

> **NOTE:** If there is any problem, see
> [Troubleshooting EFI Electronic Circuit with Volt/Ohmmeter (4A-GZE)](#troubleshooting-efi-electronic-circuit-with-voltohmmeter-4a-gze).

##### ECU connector terminals (4A-GZE)

| Symbol | Terminal | Symbol | Terminal |
| ------ | -------- | ------ | -------- |
| E01 | Engine ground (Power) | E22 | Sensor ground |
| E02 | Engine ground (Power) | VSV2 | VSV (Air bleed) |
| RSC | ISC valve | L1\* | ECT computer |
| RSO | ISC valve | L3\* | ECT computer |
| STA | Starter switch | L2\* | ECT computer |
| IGT | Igniter | ECT1\* | ECT computer |
| EGR | EGR valve | TIL | Super charger |
| G2 | Engine revolution sensor | A/C | A/C magnet clutch |
| VTA | Throttle position sensor | SPD | Speedometer sensor |
| NE | Engine revolution sensor | W | Warning light |
| IDL | Throttle position sensor | STP | Stop light |
| VSV3 | VSV (Air by-pass) | KNK | Knock sensor |
| HT | Oxygen sensor heater | VC | Air flow meter |
| IGF | Igniter | VS | Air flow meter |
| OX | Oxygen sensor | THG\* | EGR temperature sensor |
| THW | Water temperature sensor | BATT | Battery |
| E2 | Sensor ground | +B | EFI main relay |
| R/P | Fuel control switch | +B1 | EFI main relay |
| THA | Inlet air temperature sensor | ELS2 | Accessory switch |

> \* For A/T / For Calif. as applicable.

#### Voltage at ECU wiring connectors (4A-GZE)

| No. | Terminals | STD voltage (V) | Condition | See page |
| --- | --------- | --------------- | --------- | -------- |
| 1 | +B1 / +B – E1 | 10 – 14 | Ignition S/W ON | FI-49 |
| 2 | BATT – E1 | 10 – 14 | — | FI-50 |
| 3 | IDL – E2 | M/T 4 – 5; A/T 10 – 14 | Throttle valve open | FI-51 |
| 3 | VTA – E2 | 0.1 – 1.0 | Ignition S/W ON, throttle valve fully closed | FI-51 |
| 3 | VTA – E2 | 4 – 5 | Ignition S/W ON, throttle valve fully open | FI-51 |
| 3 | VC – E2 | 4 – 6 | — | FI-51 |
| 4 | VC – E2 | 4 – 6 | — | FI-53 |
| 4 | VS – E2 | 4 – 5 | Ignition S/W ON, measuring plate fully closed | FI-53 |
| 4 | VS – E2 | 0.02 – 0.5 | Ignition S/W ON, measuring plate fully open | FI-53 |
| 4 | VS – E2 | 2 – 4 | Idling | FI-53 |
| 5 | No. 10 – E01 / No. 20 – E02 | 9 – 14 | Ignition S/W ON | FI-54 |
| 6 | W – E1 | 9 – 14 | No trouble ("CHECK ENGINE" warning light off) and engine running | FI-55 |
| 7 | THA – E2 | 1 – 3 | Ignition S/W ON, intake air temperature 20°C (68°F) | FI-56 |
| 8 | THW – E2 | 0.1 – 1.0 | Ignition S/W ON, coolant temperature 80°C (176°F) | FI-57 |
| 9 | STA – E1 | 6 – 14 | Ignition S/W ST position and press on the clutch pedal (M/T) | FI-58 |
| 10 | IGT – E1 | 0.7 – 1.0 | Idling | FI-59 |
| 11 | RSC / RSO – E1 | 9 – 14 | Ignition S/W ON | FI-60 |
| 12 | A/C – E1 | 5 – 14 | Air conditioning ON | FI-61 |

### Troubleshooting EFI Electronic Circuit with Volt/Ohmmeter (4A-GE)

> **NOTE:** The following troubleshooting procedures are designed for inspection of each
> separate system, and therefore the actual procedure may vary somewhat. However,
> troubleshooting should be performed by referring to the inspection methods described in
> this manual. Before beginning inspection, it is best to first make a simple check of the
> fuses, fusible links and the condition of the connectors.
>
> The following troubleshooting procedures are based on the supposition that the trouble
> lies in either a short or open circuit in a component outside the computer or a short
> circuit within the computer. If engine trouble occurs even though proper operating
> voltage is detected in the computer connector, then the computer is faulty and should be
> replaced.

*(Figure: location of fuses and fusible links — Junction Block No. 2, EFI 15A, EFI main
relay, injector relay, fusible link 1.25B — see page image p.229 (FI-33).)*

In each flow below, work down the **Check** column: follow the OK branch or the NG (NO/BAD)
branch as indicated.

#### No. 1 — +B1 / +B – E1

**Trouble:** No voltage · **Condition:** Ignition switch ON · **STD voltage: 10 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals +B1 or +B and E1? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminals +B1 or +B and body ground? (IG S/W ON) | Check wiring between ECU terminal E1 and body ground; if BAD, repair or replace | Go to 3 |
| 3 | Check fuse, fusible link and wiring harness | — | Repair or replace |

#### No. 2 — BATT – E1

**Trouble:** No voltage · **Condition:** — · **STD voltage: 10 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals BATT and E1? | System OK | Go to 2 |
| 2 | Voltage between ECU terminal BATT and body ground? | Check wiring between ECU terminal E1 and body ground; if BAD, repair or replace | Go to 3 |
| 3 | Check fuse, fusible links and wiring harness | — | Repair |

#### No. 3 — IDL / VTA / VCC – E2

**Trouble:** No voltage · **Condition:** Ignition switch ON · **STD voltage:** IDL–E2 (throttle
valve open) 10 – 14 V; VTA–E2 (throttle fully closed) 0.1 – 1.0 V; VTA–E2 (throttle fully
open) 4 – 5 V; VCC–E2 4 – 6 V

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Specified voltage at the terminal under test and E2? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal +B1 or +B and body ground? (IG S/W ON) | Go to 3 | Refer to No. 1 (FI-34) — if that path bad, repair/replace; check wiring ECU E1 to body ground |
| 3 | Check throttle position sensor (FI-98) | Check wiring between ECU and throttle position sensor; if OK, try another ECU; if BAD, repair or replace wiring | Repair or replace throttle position sensor |

#### No. 4 — +B1 / VC / VS – E2

**Trouble:** No voltage · **Condition:** Ignition switch ON (or idling) · **STD voltage:**
+B1–E2 10 – 14 V; VC–E2 6 – 10 V; VS–E2 (measuring plate fully closed) 2 – 5.5 V; VS–E2
(measuring plate fully open) 6 – 9 V; VS–E2 (idling) 2 – 8 V

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 (+B1–E2) | Voltage between computer terminals +B1 and E2? (IG S/W ON) | System OK | Go to 2 |
| 2 (+B1–E2) | Voltage between computer terminal +B and body ground? (IG S/W ON) | Try another computer | Refer to No. 1 (FI-34) |
| 1 (VC/VS–E2) | Specified voltage at computer terminals VC and VS? (IG S/W ON) | System OK | Go to 2 |
| 2 (VC/VS–E2) | Voltage between computer terminals +B1 and E2? (IG S/W ON) | Check air flow meter (FI-94); if BAD, check wiring between computer and air flow meter | Refer to No. 1 (FI-34) |

#### No. 5 — No. 10 – E01 / No. 20 – E02

**Trouble:** No voltage · **Condition:** Ignition switch ON · **STD voltage: 9 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals No. 10 and/or No. 20 and E01 and/or E02? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal No. 10 and/or No. 20 and body ground? | Go to 3 | Check fuse, fusible link, ignition switch and starter relay; if BAD, repair or replace |
| 3 | Check resistance of magnetic coil in each injector — **STD resistance: approx. 13.8 Ω** | Check wiring between ECU terminal No. 10 and/or No. 20 and battery; if BAD, repair or replace | Replace injector |
| (2, alt.) | Check wiring between ECU terminal E01 and/or E02 and body ground | Try another ECU | Repair or replace |

#### No. 6 — W – E1

**Trouble:** No voltage · **Condition:** No trouble (check engine warning light off) and engine
running · **STD voltage: 9 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals W and E1? (idling) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal W and body ground? | Go to 3 | Check wiring between ECU terminal E1 and body ground; if OK try another ECU, if BAD repair or replace |
| 3 | Check fuse and check engine warning light | Check wiring between ECU terminal W and fuse (if fuse blows again); if BAD, repair or replace | Repair or replace |

#### No. 7 — THA – E2

**Trouble:** No voltage · **Condition:** Ignition switch ON, intake air temperature 20°C (68°F)
· **STD voltage: 1 – 3 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Specified voltage between ECU terminals THA and E2? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal +B1 or +B and body ground? (IG S/W ON) | Check wiring between ECU and air temperature sensor; if OK, try another ECU; if BAD, repair or replace wiring | Refer to No. 1 (FI-34) |

#### No. 8 — THW – E2

**Trouble:** No voltage · **Condition:** Ignition switch ON, coolant temperature 80°C (176°F) ·
**STD voltage: 0.1 – 1.0 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Specified voltage between ECU terminals THW and E2? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal +B1 or +B and body ground? (IG S/W ON) | Go to 3 | Refer to No. 1 (FI-34) |
| 3 | Check water temp. sensor | Check wiring between ECU and sensor; if OK try another ECU, if BAD repair or replace wiring | Replace water temp. sensor |

#### No. 9 — STA – E1

**Trouble:** No voltage · **Condition:** Ignition switch ST position · **STD voltage: 6 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals STA and E1? (IG S/W ON) | System OK | Go to 2 |
| 2 | Check starter operation | Check wiring between ECU and starter terminal 50; if BAD, repair or replace | Go to 3 |
| 3 | Check fusible link, battery, wiring, ignition switch, starter relay and clutch start switch | Go to 4 | Repair or replace |
| 4 | Voltage at STA (50) terminal of starter? (IG S/W ST) — **STD voltage: 6 – 14 V** | Check starter | Check wiring between ignition switch ST terminal and starter STA (50) terminal |
| (alt.) | Check wiring between ECU terminal E1 and body ground | — | Repair or replace |

#### No. 10 — IGT – E1

**Trouble:** No voltage · **Condition:** Idling · **STD voltage: 0.7 – 1.0 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminal IGT and E1? (idling) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal IGT and body ground? (idling) | Go to 3 | Refer to No. 1 (FI-34); check wiring ECU E1 to body ground, if BAD repair or replace |
| 3 | Check wiring between ECU and distributor | Go to 4 | Repair or replace |
| 4 | Check distributor | Go to 5 | Replace |
| 5 | Check wiring between ECU and igniter | Go to 6 | Repair or replace |
| 6 | Check igniter (IG-4) | Try another ECU | Repair or replace |

#### No. 11 — A/C – E1

**Trouble:** No voltage · **Condition:** Air conditioning ON · **STD voltage: 5 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals A/C and E1? (air conditioning ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal A/C and body ground? | Check wiring between ECU E1 and body ground; if OK try another ECU, if BAD repair or replace | Go to 3 |
| 3 | Check compressor running | Check wiring between ECU terminal A/C and amplifier; if BAD, repair or replace | Go to 4 |
| 4 | Voltage between amplifier terminal and body ground? | Check wiring between amplifier and ECU or compressor; if BAD, repair or replace | Repair or replace |

#### Oxygen sensor circuit (VF)

*(Figure: oxygen sensor / oxygen sensor heater circuit at check connector and ECU terminals
VF, T, OX, HT, E1 — see page image p.242 (FI-46).)*

The VF check verifies air-fuel feedback. If there is no voltage between ECU terminals VF and
E1, check for air leaking into the air intake system and inspect/repair or replace per the
flow; a normal result indicates the system is normal. (Rich malfunction only applies to
part of this flow.)

#### EGR gas temperature sensor circuit (THG) — California

**Condition:** Engine running at 2,000 rpm

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals THG and E2? (engine running at 2,000 rpm) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal +B or +B1 and body ground? (IG S/W ON) | Go to 3 | Refer to No. 1 (FI-34) |
| 3 | Check wiring between ECU terminal E1 and body ground | Check EGR system | if BAD, repair or replace |
| 4 | Check EGR gas temp. sensor | Check wiring between ECU and EGR gas temp. sensor; if OK try another ECU, if BAD repair or replace | Replace EGR gas temp. sensor |

### Troubleshooting EFI Electronic Circuit with Volt/Ohmmeter (4A-GZE)

> **NOTE:** The following troubleshooting procedures are designed for inspection of each
> separate system, and therefore the actual procedure may vary somewhat. However,
> troubleshooting should be performed by referring to the inspection methods described in
> this manual. Before beginning inspection, it is best to first make a simple check of the
> fuses, fusible links and the condition of the connectors.
>
> The following troubleshooting procedures are based on the supposition that the trouble
> lies in either a short or open circuit in a component outside the computer or a short
> circuit within the computer. If engine trouble occurs even though proper operating
> voltage is detected in the computer connector, then the computer is faulty and should be
> replaced.

*(Figure: location of fuses and fusible links — Junction Block No. 2, EFI 15A, EFI main
relay, injector relay, fusible link 1.25B — see page image p.245 (FI-48).)*

#### No. 1 — +B1 / +B – E1

**Trouble:** No voltage · **Condition:** Ignition switch ON · **STD voltage: 10 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals +B1 or +B and E1? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminals +B1 or +B and body ground? (IG S/W ON) | Check wiring between ECU terminal E1 and body ground; if BAD, repair or replace | Go to 3 |
| 3 | Check fuse, fusible link and wiring harness | Go to 4 | Repair or replace |
| 4 | Check EFI main relay | — | Replace |

#### No. 2 — BATT – E1

**Trouble:** No voltage · **Condition:** — · **STD voltage: 10 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals BATT and E1? | System OK | Go to 2 |
| 2 | Voltage between ECU terminal BATT and body ground? | Check wiring between ECU terminal E1 and body ground; if BAD, repair or replace | Go to 3 |
| 3 | Check fuse, fusible links and wiring harness | — | Repair |

#### No. 3 — IDL / VTA / VC – E2

**Trouble:** No voltage · **Condition:** Ignition switch ON · **STD voltage:** IDL–E2 (throttle
valve open) M/T 4 – 5 V, A/T 10 – 14 V; VTA–E2 (throttle fully closed) 0.1 – 1.0 V; VTA–E2
(throttle fully open) 4 – 5 V; VC–E2 4 – 6 V

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Specified voltage at the terminal under test and E2? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal +B1 or +B and body ground? (IG S/W ON) | Go to 3 | Refer to No. 1 (FI-49); check wiring ECU E1 to body ground, if BAD repair or replace |
| 3 | Check throttle position sensor (FI-98) | Check wiring between ECU and throttle position sensor; if OK try another ECU, if BAD repair or replace | Repair or replace throttle position sensor |

*(For the VC–E2 branch: if step 2 is OK, check throttle position sensor; if BAD, repair or
replace; if step 2 is NO, refer to No. 1 (FI-49).)*

#### No. 4 — VC / VS – E2

**Trouble:** No voltage · **Condition:** Ignition switch ON (or idling) · **STD voltage:** VC–E2
4 – 6 V; VS–E2 (measuring plate fully closed) 4 – 5 V; VS–E2 (measuring plate fully open)
0.02 – 0.5 V; VS–E2 (idling) 2 – 4 V

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Specified voltage at ECU terminals VC or VS and E2? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal +B or +B1 and body ground? (IG S/W ON) | Go to 3 | Refer to No. 1 (FI-49) |
| 3 | Check wiring between ECU terminal E1 and body ground | Go to 4 | Repair or replace |
| 4 | Check air flow meter (FI-94) | Check wiring between ECU and air flow meter; if OK try another ECU, if BAD repair or replace | Repair or replace air flow meter |

#### No. 5 — No. 10 – E01 / No. 20 – E02

**Trouble:** No voltage · **Condition:** Ignition switch ON · **STD voltage: 9 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between computer terminal No. 10 and/or No. 20 and E01 and/or E02? (IG S/W ON) | System OK | Go to 2 |
| 2 | Specified voltage between resistor terminal (+) and body ground? — **STD voltage: 9 – 14 V** | Go to 3 | Check fuse, fusible link, injector relay and ignition switch; if BAD, repair or replace |
| 3 | Specified voltage between resistor terminal (−) and body ground? — **STD voltage: 9 – 14 V** | Go to 4 | Replace resistor |
| 4 | Check resistance of the magnetic coil in each injector — **STD resistance: approx. 2.9 Ω** | Check wiring between ECU and resistor | Replace injector |

#### No. 6 — W – E1

**Trouble:** No voltage · **Condition:** No trouble ("CHECK ENGINE" warning light off) and
engine running · **STD voltage: 9 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals W and E1? (idling) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal W and body ground? | Go to 3 | Check wiring between ECU terminal E1 and body ground; if OK try another ECU, if BAD repair or replace |
| 3 | Check GAUGE fuse (7.5 A) and "CHECK ENGINE" warning light | Check wiring between ECU terminal W and fuse (if fuse blows again); if BAD, repair or replace | Repair or replace |

#### No. 7 — THA – E2

**Trouble:** No voltage · **Condition:** Ignition switch ON, intake air temperature 20°C (68°F)
· **STD voltage: 1 – 3 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Specified voltage between ECU terminals THA and E2? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal +B1 or +B and body ground? (IG S/W ON) | Go to 3 | Refer to No. 1 (FI-49) |
| 3 | Check air temp. sensor | Check wiring between ECU and air temperature sensor; if OK try another ECU, if BAD repair or replace wiring | Replace air temp. sensor |

#### No. 8 — THW – E2

**Trouble:** No voltage · **Condition:** Ignition switch ON, coolant temperature 80°C (176°F) ·
**STD voltage: 0.1 – 1.0 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Specified voltage between ECU terminals THW and E2? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal +B1 or +B and body ground? (IG S/W ON) | Check water temp. sensor and wiring between ECU and sensor; if OK try another ECU, if BAD repair or replace wiring | Refer to No. 1 (FI-49) |

#### No. 9 — STA – E1

**Trouble:** No voltage · **Condition:** Ignition switch ST position · **STD voltage: 6 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals STA and E1? (IG S/W ON) | System OK | Go to 2 |
| 2 | Check starter operation | Check wiring between ECU and starter terminal 50; if BAD, repair or replace | Go to 3 |
| 3 | Check fusible link, battery, wiring, ignition switch, starter relay and clutch start switch | Go to 4 | Repair or replace |
| 4 | Voltage at STA (50) terminal of starter? (IG S/W ST) — **STD voltage: 6 – 14 V** | Check starter | Check wiring between ignition switch ST terminal and starter STA (50) terminal |
| (alt.) | Check wiring between ECU terminal E1 and body ground | — | Repair or replace |

#### No. 10 — IGT – E1

**Trouble:** No voltage · **Condition:** Idling · **STD voltage: 0.7 – 1.0 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminal IGT and E1? (idling) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal IGT and body ground? (idling) | Go to 3 | Refer to No. 1 (FI-49); check wiring ECU E1 to body ground, if BAD repair or replace |
| 3 | Check wiring between ECU and distributor | Go to 4 | Repair or replace |
| 4 | Check distributor | Go to 5 | Replace |
| 5 | Check wiring between ECU and igniter | Go to 6 | Repair or replace |
| 6 | Check igniter (IG-4) | Try another ECU | Repair or replace |

#### No. 11 — RSC / RSO (ISC1 / ISC2) – E1

**Trouble:** No voltage · **Condition:** Ignition switch ON · **STD voltage: 9 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminal RSC or RSO and E1? (IG S/W ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminals +B or +B1 and body ground? (IG S/W ON) | Go to 3 | Refer to No. 1 (FI-49) |
| 3 | Check resistance between ISC valve terminals +B and ISC1 or ISC2 — **STD resistance: 16.0 – 17.0 Ω** | Check wiring between ECU and ISC valve; if OK try another ECU, if BAD repair or replace wiring | Replace ISC valve |

#### No. 12 — A/C – E1

**Trouble:** No voltage · **Condition:** Air conditioning ON · **STD voltage: 5 – 14 V**

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals A/C and E1? (air conditioning ON) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal A/C and body ground? | Check wiring between ECU E1 and body ground; if OK try another ECU, if BAD repair or replace | Go to 3 |
| 3 | Check compressor running | Check wiring between ECU terminal A/C and amplifier; if BAD, repair or replace | Go to 4 |
| 4 | Voltage between amplifier terminal and body ground? | Check wiring between amplifier and ECU or compressor; if BAD, repair or replace | Repair or replace |

#### Oxygen sensor circuit (VF)

*(Figure: oxygen sensor / oxygen sensor heater circuit at check connector and ECU terminals
VF, T, OX, HT, E1 — see page image p.257 (FI-62).)*

The VF check verifies air-fuel feedback: work down the OK branches; a normal result at the
end indicates the system is normal, otherwise repair wiring. (The final "rich malfunction
only" note applies to that branch.)

#### EGR gas temperature sensor circuit (THG) — California

**Condition:** Engine running at 2,000 rpm

| Step | Check | OK | NG |
| ---- | ----- | -- | -- |
| 1 | Voltage between ECU terminals THG and E2? (engine running at 2,000 rpm) | System OK | Go to 2 |
| 2 | Voltage between ECU terminal +B or +B1 and body ground? (IG S/W ON) | Go to 3 | Refer to No. 1 (FI-49) |
| 3 | Check wiring between ECU terminal E1 and body ground | Check EGR system | if BAD, repair or replace |
| 4 | Check EGR gas temp. sensor | Check wiring between ECU and EGR gas temp. sensor; if OK try another ECU, if BAD repair or replace | Replace EGR gas temp. sensor |

### Fuel System

*This section begins the Fuel System component procedures, which continue in
[Part 2](05b-efi-system-and-emission-control-part-2.md).*

#### Fuel Pump

*(Figure: fuel pump cutaway — check valve, relief valve, brush, armature, magnet, impeller,
casing, outlet, inlet — and fuel pump circuit: EFI main relay, circuit opening relay,
fusible link 1.25B, fuel pump switch (in air flow meter), starter relay, clutch (M/T) or
neutral (A/T) start switch, check connector (FP, +B), fuel pump — see page image p.260
(FI-64).)*

*(Fuel Pump removal, inspection, and installation procedures continue in Part 2.)*
