# Emissions Control Systems

*Toyota Corolla (FWD, 1984–1992) Haynes Repair Manual — Chapter 6, section code `EC` · printed pages 6-1 to 6-18 · source PDF pages 154–171. Covers 4A-C, 4A-F, 4A-FE and 4A-GE engines, Federal and California emissions configurations, both carbureted and EFI (fuel-injected) models.*

> Diagnostic trouble codes (DTC) in this manual are read by counting flashes of the **Check Engine light** (the "Check Engine" light here is the **Malfunction Indicator Lamp, MIL**, per SAE J1930 — not the maintenance-reminder SRI). See the [glossary](../../../../../glossary.md) for DTC/MIL conventions and OCR misread patterns (Ω→"2", l→i, h→li, rn→m) used when cross-checking this chapter against the scanned pages.

---

**[PDF p.154]**
## 1. General Information (PDF p.154) <a id="p154"></a>

To minimize pollution of the atmosphere from incompletely burned and evaporating gases and to maintain good driveability and fuel economy, a number of emission control systems are used on these vehicles. They include:

- **Positive Crankcase Ventilation (PCV) system** — reduces hydrocarbons from crankcase blow-by
- **Evaporative Emission Control (EVAP) system** — reduces evaporative hydrocarbons
- **Feedback carburetor system** (some models) — reduces hydrocarbons and carbon monoxide by regulating the operating conditions of the engine
- **Exhaust Gas Recirculation (EGR) system** — reduces oxides of nitrogen (NOx) emissions
- **Catalytic converter** — reduces hydrocarbons, carbon monoxide and oxides of nitrogen
- **Electronic Fuel Injection (EFI) system** (some models) — reduces all exhaust emissions by regulating the operating conditions of the engine

The **Vehicle Emissions Control Information (VECI) label**, located in the engine compartment, contains emissions specifications, setting procedures, and a vacuum hose schematic with emissions components identified. Always check the VECI label on the specific vehicle for up-to-date information — the illustrations in this chapter may not exactly match the system installed, due to running production changes.

<!-- DIAGRAM CANDIDATE: p.159-160 — fig. 1.6, Vehicle Emission Control Information (VECI) label -->

Before assuming an emissions control system is malfunctioning, check the fuel and ignition systems carefully (see [Fuel and Exhaust Systems](04-fuel-and-exhaust-systems.md) and [Engine Electrical Systems](05-engine-electrical-systems.md)). The diagnosis of some emission control devices requires specialized tools, equipment and training — if checking/servicing becomes too difficult, consult a dealer service department. The most frequent cause of emissions problems is simply a loose or broken electrical connector or vacuum hose — always check those first.

Pay close attention to the precautions in this chapter (Section 2) — illustrations of the various systems may not exactly match the system on any one vehicle because of year-to-year and running production changes.

### Typical emissions control system component locations (illustrations)

The manual illustrates component locations for each model-year/engine/emissions configuration. Parts lists that are legible as text in the source are transcribed below; illustrations that are pure line-art with no accompanying parts list are flagged as diagram candidates.

**Fig. 1.1a — 1984 and 1985 Federal models (PDF p.154) <a id="p154"></a>**

| # | Component | # | Component |
| - | --------- | - | --------- |
| 1 | Distributor | 13 | Auxiliary acceleration pump |
| 2 | Check valve | 14 | Air suction valve |
| 3 | Thermo switch | 15 | Check valve |
| 4 | Thermostatic vacuum switching valve | 16 | Delay valve |
| 5 | Jet | 17 | Electric air bleed control valve |
| 6 | Choke breaker | 18 | High altitude compensation valve |
| 7 | Hot air intake diaphragm | 19 | Vacuum switch (A) |
| 8 | Vacuum switching valve | 20 | Vacuum switch (B) |
| 9 | Charcoal canister | 21 | Vacuum switching valve |
| 10 | Outer vent control valve | 22 | Throttle positioner |
| 11 | EGR valve | 23 | Choke opener |
| 12 | EGR vacuum modulator | 24 | Hot idle compensator |

<!-- DIAGRAM CANDIDATE: p.154 — fig. 1.1a, exploded emissions component-location diagram, 1984-85 Federal models -->

**Fig. 1.1b — 1984 and 1985 California models (PDF p.155) <a id="p155"></a>**

| # | Component | # | Component |
| - | --------- | - | --------- |
| 1 | Distributor | 12 | Auxiliary acceleration pump |
| 2 | Thermo switch | 13 | Air suction valve (reed valve) |
| 3 | Thermostatic vacuum switching valve | 14 | Air suction valve |
| 4 | Jet | 15 | Check valve |
| 5 | Choke breaker | 16 | Delay valve |
| 6 | Hot air intake diaphragm | 17 | Electric air bleed control valve |
| 7 | Vacuum switching valve | 18 | Vacuum switch (A) |
| 8 | Charcoal canister | 19 | Vacuum switch (B) |
| 9 | Outer vent control valve | 20 | Vacuum switching valve |
| 10 | EGR valve | 21 | Throttle positioner |
| 11 | EGR vacuum modulator | 22 | Choke opener |
| — | — | 23 | Hot idle compensator |

<!-- DIAGRAM CANDIDATE: p.155 — fig. 1.1b, exploded emissions component-location diagram, 1984-85 California models -->

**Fig. 1.1c — 1986 and 1987 carbureted Federal models (PDF p.156) <a id="p156"></a>**

Components (unnumbered list in source, order as printed): Distributor (1986 hoses shown, 1987 similar), Check valve, Thermo switch, Thermostatic vacuum switching valve, Jet, Choke breaker, Hot air intake diaphragm, Vacuum switching valve, Charcoal canister, Outer vent control valve, EGR valve, EGR vacuum modulator, Auxiliary acceleration pump, Air suction valve, Check valve, Delay valve, Electric air bleed control valve, High altitude compensation valve, Throttle positioner switch, Vacuum switch, Vacuum switching valve, Throttle positioner, Choke opener, Hot idle compensator.

<!-- DIAGRAM CANDIDATE: p.156 — fig. 1.1c, exploded emissions component-location diagram, 1986-87 carbureted Federal models -->

**Fig. 1.1d — 1986 and 1987 carbureted California models (PDF p.157) <a id="p157"></a>**

| # | Component | # | Component |
| - | --------- | - | --------- |
| 1 | Distributor | 12 | Auxiliary acceleration pump |
| 2 | Thermo switch | 13 | Air suction valve (reed valve) |
| 3 | Thermostatic vacuum switching valve | 14 | Air suction valve (shut-off valve) |
| 4 | Jet | 15 | Check valve |
| 5 | Choke breaker | 16 | Delay valve |
| 6 | Hot air intake diaphragm | 17 | Electric air bleed control valve |
| 7 | Vacuum switching valve | 18 | Throttle positioner |
| 8 | Charcoal canister | 19 | Vacuum switch |
| 9 | Outer vent control valve | 20 | Vacuum switching valve |
| 10 | EGR valve | 21 | Throttle positioner |
| 11 | EGR vacuum modulator | 22 | Choke opener |
| — | — | 23 | Hot idle compensator |

<!-- DIAGRAM CANDIDATE: p.157 — fig. 1.1d, exploded emissions component-location diagram, 1986-87 carbureted California models -->

**Fig. 1.1e — 1987 through 1989 4A-GE engine models (PDF p.158) <a id="p158"></a>**

| # | Component | # | Component |
| - | --------- | - | --------- |
| 1 | EGR vacuum modulator | 8 | Fuel vapor canister |
| 2 | Diaphragm (for T-VIS) | 9 | Bimetal vacuum switching valve (for EGR) |
| 3 | Vacuum switching valve | 10 | EGR valve |
| 4 | Vacuum tank | 11 | Bimetal vacuum switching valve (for evaporative emissions control system) |
| 5 | Exhaust oxygen sensor | 12 | EGR temperature switch (California only) |
| 6 | Check valve | — | — |
| 7 | Dashpot (with vacuum transmitting valve) | — | — |

<!-- DIAGRAM CANDIDATE: p.158 — fig. 1.1e, exploded emissions component-location diagram, 1987-89 4A-GE engine models -->

**Figs. 1.1f–1.1k — later component-location diagrams (PDF p.158–160)**

The remaining component-location illustrations in this section are pure diagrams with component names as image labels only (no separate numbered parts list in the source text): EGR vacuum modulator, VSV (for EGR), EGR gas temperature sensor (California), oxygen sensor, BVSV (for EVAP), charcoal canister, and similar components, labeled directly on the drawing rather than via a numbered legend.

<!-- DIAGRAM CANDIDATE: p.158 — fig. 1.1f, component locations, 1990 and later 4A-GE engine models -->
<!-- DIAGRAM CANDIDATE: p.158-159 — fig. 1.1g, component locations, 1988-89 Federal 4A-F engine models -->
<!-- DIAGRAM CANDIDATE: p.159 — fig. 1.1i, component locations, 1989 4A-FE engine models -->
<!-- DIAGRAM CANDIDATE: p.159 — fig. 1.1j, component locations, 1990 and later Federal 4A-FE engine models -->
<!-- DIAGRAM CANDIDATE: p.160 — fig. 1.1k, component locations, 1990 and later California 4A-FE engine models -->

> The manual notes: *"The illustrations of the various systems may not exactly match the system installed on your vehicle because of changes made by the manufacturer during production or from year-to-year."*

---

**[PDF p.159]**
## 2. Electronic Control System — Description and Precautions (PDF p.159) <a id="p159"></a>

### Description

The electronic control system controls the fuel injection system or feedback carburetor system by means of a microcomputer known as the **Electronic Control Unit (ECU)**. The system used with fuel injection on these vehicles is called the **Toyota Computer Control System (TCCS)**.

The ECU receives signals from various sensors which monitor changing engine operating conditions — intake air volume, intake air temperature, coolant temperature, engine rpm, acceleration/deceleration, exhaust oxygen content, etc. These signals are used by the ECU to determine the correct injector duration or the air/fuel mixture in the carburetor.

The system is analogous to the central nervous system in the human body: sensors ("nerve endings") constantly relay signals to the ECU ("brain"), which processes the data and, if necessary, sends a command to change the operating parameters of the engine ("body"). Example: an oxygen sensor in the exhaust manifold constantly monitors exhaust oxygen content and signals the ECU. If the mixture is incorrect, the ECU commands the fuel injection system or feedback carburetor to change the air/fuel mixture. This happens continuously, in a fraction of a second, while the engine runs — maintaining a constantly correct air/fuel ratio regardless of driving conditions.

In the event of a sensor malfunction, a backup circuit takes over to provide driveability until the problem is identified and fixed.

### Precautions

> **CAUTION:**
> a. Always disconnect power (ignition switch off, or disconnect the battery terminals) before removing TCCS wiring connectors.
> b. When installing a battery, be particularly careful to avoid reversing the positive and negative battery cables.
> c. Do not subject EFI, emissions-related components, feedback carburetor components, or the ECU to severe impact during removal or installation.
> d. Do not be careless during troubleshooting — even slight terminal contact can invalidate a test procedure and damage a transistor circuit.
> e. Never attempt to work on the ECU or open the ECU cover. The ECU is protected by a government-mandated extended warranty that will be nullified if tampered with or damaged. Remanufactured ECUs are available in some cases; the core must be clean and dry to be accepted for exchange credit.
> f. If inspecting electronic control system components during rainy weather, make sure water does not enter any part. When washing the engine compartment, do not spray these parts or their connectors with water.

---

## 3. Diagnosis System — General Information and Obtaining Code Output (PDF p.159–162)

> **Note:** Only 1987 and later fuel-injected models and 1988 and later California carbureted models are equipped with a diagnosis system.

### General information

The ECU contains a built-in self-diagnosis system which detects and identifies malfunctions occurring in the network. When the ECU detects a problem, three things happen: the Check Engine light (MIL) comes on, the trouble is identified, and a diagnostic code is recorded and stored. The ECU stores the failure code assigned to the specific problem area until the diagnosis system is cancelled by removing the stop fuse with the ignition switch off.

The Check Engine warning light, on the instrument panel, comes on when the ignition switch is turned On and the engine is not running. When the engine starts, the light should go out. If it remains on, the diagnosis system has detected a malfunction.

### Obtaining diagnosis code output

1. Verify the battery voltage is above **11 volts**, the throttle is fully closed, the transaxle is in Neutral, the accessory switches are off, and the engine is at normal operating temperature.
2. Turn the ignition switch to On. Do not start the engine.
3. On 1987 models, use a jumper wire to bridge both terminals of the service connector located near the windshield wiper motor.
   <!-- DIAGRAM CANDIDATE: p.160 — fig. 3.3a, check engine connector location and jumper-wire bridging, 1987 models -->
   On 1988 and later models, use a jumper wire to bridge terminals **T** and **E1** of the service connector (located in the engine compartment).
   <!-- DIAGRAM CANDIDATE: p.160 — fig. 3.3b, service connector terminals T/E1 location, 1988 and later models -->
4. Read the diagnosis code as indicated by the number of flashes of the Check Engine light on the dash (see the DTC tables below). Normal system operation is indicated by **Code No. 1** (no malfunctions) for all models — the light blinks once every few seconds.
5. If there are malfunctions, their corresponding trouble codes are stored and the light blinks the requisite number of times for each code. Multiple stored codes display in numerical order, lowest to highest, with a pause between each. After the largest-numbered code, there is a longer pause and the sequence repeats.
6. Watch carefully for the interval between the end of one code and the start of the next, or you will miscount the blinks. The interval length varies with model year.

### Clearing a diagnostic code

7. After the malfunctioning component has been repaired/replaced, remove the **15A stop fuse** for at least ten seconds with the ignition switch off (the lower the temperature, the longer the fuse must stay out). Fuse location varies with model year.
8. Codes can also be cleared by disconnecting the battery negative terminal cable, but this also cancels other memory systems (clock, theft-resistant radio on 1990-and-later models).
9. If a diagnostic code is not cleared, it remains stored by the ECU and will appear alongside any new codes in the event of future trouble.
10. Before removing the battery terminal to work on engine components, first check whether a diagnostic code has been recorded.

### 1987 Trouble Codes

| Code | Flash pattern | Circuit or system | Diagnosis | Trouble area |
| ---- | -------------- | ------------------ | --------- | ------------- |
| Code 1 | 1 Flash, Pause, 1 Flash | Normal | This appears when none of the other codes are identified | — |
| Code 2 | 2 Flashes, Pause, 2 Flashes | Air flow meter signal | Open circuit in Vc, Vs, Vb or E2 | Air flow meter circuit; Air flow meter; ECU |
| Code 3 | 3 Flashes, Pause, 3 Flashes | Ignition signal | No signal from igniter four times in a row | Ignition circuit (+B, IGf); Igniter; ECU |
| Code 4 | 4 Flashes, Pause, 4 Flashes | Coolant temperature sensor circuit | Open or short circuit in the coolant temperature sensor or circuit | Coolant temperature sensor circuit; Coolant temperature sensor; ECU |
| Code 5 | 5 Flashes, Pause, 5 Flashes | Oxygen sensor signal | Open circuit in oxygen sensor signal (lean indication only) | Oxygen sensor circuit; Oxygen sensor; ECU |
| Code 6 | 6 Flashes, Pause, 6 Flashes | RPM signal | No Ne or G signal to ECU within several seconds after engine is cranked | Distributor circuit; Distributor–Igniter; Starter signal circuit; ECU |
| Code 7 | 7 Flashes, Pause, 7 Flashes | Throttle position sensor signal | Open or short circuit in throttle position sensor signal | Throttle position sensor circuit; Throttle position sensor; ECU |
| Code 8 | 8 Flashes, Pause, 8 Flashes | Intake air temperature sensor signal | Open or short circuit in intake air temperature sensor | Air temperature sensor circuit; ECU |
| Code 9 | (not used) | — | — | — |
| Code 10 | 10 Flashes, Pause, 10 Flashes | Starter signal | No STA signal to ECU when vehicle is stopped and engine is running at more than 800 rpm | Starter relay circuit; IG switch circuit (starter); IG switch–ECU |
| Code 11 | 11 Flashes, Pause, 11 Flashes | Switch signal | Air conditioner switch ON, idle switch OFF, or shift position D range (automatic only) during diagnostic check | Air conditioner switch; ECU; Idle switch; Neutral switch (automatic only) |

### 1988 and Later Trouble Codes

| Code | Flash pattern | Circuit or system | Diagnosis | Trouble area |
| ---- | -------------- | ------------------ | --------- | ------------- |
| Code 1 | 1 Flash, Pause, 1 Flash | Normal | This appears when none of the other codes are identified | — |
| Code 12 | 1 flash, Pause, 2 flashes | RPM signal | No "Ne" signal to the ECU within 2 seconds after the engine is cranked; no "G" signal to the ECU two times in succession when engine speed is between 500 rpm and 4000 rpm | Distributor circuit; Distributor; Starter signal circuit; Igniter circuit; Igniter; ECU |
| Code 13 (EFI only) | 1 flash, Pause, 3 flashes | RPM signal | No "Ne" signal to the ECU when the engine speed is above 1500 rpm | Distributor circuit; Distributor; ECU |
| Code 14 (EFI only) | 1 flash, Pause, 4 flashes | Ignition signal | No "IGF" signal to the ECU 4 times in succession | Igniter circuit; Igniter; ECU |
| Code 21* | 2 Flashes, Pause, 1 Flash | Oxygen sensor | Problem in the oxygen sensor circuit | Oxygen sensor circuit; ECU |
| Code 22 | 2 Flashes, Pause, 2 Flashes | Coolant temperature | Open or short in the temperature sensor circuit | Coolant temperature sensor circuit; Coolant temperature sensor; ECU |
| Code 24 (EFI only) | 2 Flashes, Pause, 4 Flashes | Intake air temperature sensor | Open or short in the intake air temperature (THA) circuit | Intake air temperature sensor circuit; Intake air temperature sensor; ECU |
| Code 25* | 2 Flashes, Pause, 5 Flashes | Air/fuel ratio lean malfunction | The air/fuel ratio feedback compensation valve or adaptive control valve remains at the upper (lean) or lower (rich) limit for a certain period of time | Injector circuit; Injector; Oxygen sensor circuit; Oxygen sensor; ECU; Fuel line pressure; Air leak; Air-flow meter; Air intake system; Ignition system; EBCV circuit (carburetor only); EBCV (carburetor only) |
| Code 26* | 2 Flashes, Pause, 6 Flashes | Air/fuel ratio rich malfunction | The air/fuel ratio is overly rich | Injector; Injector circuit; Oxygen sensor circuit; Oxygen sensor; Fuel line pressure; Mass air-flow meter; Cold start injector; EBCV circuit (carburetor only); EBCV hose (carburetor only); EBCV (carburetor only); ECU |
| Code 27 | 2 Flashes, Pause, 7 Flashes | Sub-oxygen sensor (California 4A-GE engine models only) | Open or shorted circuit | Sub-oxygen sensor circuit; Sub oxygen sensor; ECU |
| Code 31 | 3 Flashes, Pause, 1 Flash | Vacuum sensor (4A-F, 4A-FE engine only) | Open or short circuit | Vacuum sensor circuit; Vacuum sensor; No vacuum to sensor |
| Code 31 | 3 Flashes, Pause, 1 Flash | Air flow meter (4A-GE engine only) | Open or short circuit | Mass air flow circuit; Mass air flow meter; ECU |
| Code 41 | 4 Flashes, Pause, 1 Flash | Throttle position sensor (EFI) or throttle switch | Open or short in the throttle position sensor circuit | Throttle position sensor or switch; Throttle position sensor or switch circuit; ECU |
| Code 42 (EFI only) | 4 Flashes, Pause, 2 Flashes | Vehicle speed sensor | No "SPD" signal for 5 seconds when the engine speed is above 2800 rpm | Vehicle speed sensor circuit; Vehicle speed sensor; ECU |
| Code 43 (EFI only) | 4 Flashes, Pause, 3 Flashes | Starter signal | No "STA" signal to the ECU until engine speed reaches 800 rpm with the vehicle not moving | Starter signal circuit; Ignition switch; Main relay–ECU |
| Code 51 (EFI only) | 5 Flashes, Pause, 1 Flash | A/C switch signal | Air conditioner switch on, idle switch off during diagnosis check | A/C switch circuit; A/C switch; A/C amplifier; Throttle position sensor circuit; Throttle position sensor; ECU |
| Code 52 | 5 Flashes, Pause, 2 Flashes | Knock sensor (1990 and later 4A-GE engines only) | Open or short circuit | Knock sensor circuit; Knock sensor; ECU |
| Code 53 | 5 Flashes, Pause, 3 Flashes | Knock control (1990 and later 4A-GE engines only) | ECU | ECU connectors; ECU |
| Code 71* | 7 Flashes, Pause, 1 Flash | EGR (California 4A-GE engine only) is too low <!-- NOTE: source misprint, not OCR — confirmed against the p.162 page image, printed exactly as "EGR (California 4A-GE is too low engine only)" in the "Circuit or system" column, with "is too low" oddly nested inside the parenthetical. The "Diagnosis" column ("EGR gas temperature signal") suggests the intended meaning is "EGR gas temperature is too low (California 4A-GE engine only)" — but transcribed here exactly as printed, not corrected. --> | EGR gas temperature signal | EGR system (EGR valve, hoses, etc.); EGR gas temperature sensor circuit; EGR gas temperature sensor; Vacuum switching valve for the EGR circuit; ECU |
| Code 72 (carb only) | — | Fuel cut solenoid signal | Open circuit in fuel cut solenoid signal (FCS) | Fuel cut solenoid circuit; Fuel cut solenoid; ECU |

\* On 1991 models, the vehicle must be driven, shut off and driven again to set code 21 (depending on the cause of the code) and codes 25, 26 and 71.

<!-- NOTE: OCR read "Code 2 Г" for the oxygen-sensor code above the coolant-temperature code; page image p.161 (not p.162 as originally cited — that code is in the "1988 AND LATER" table on the preceding page) clearly shows "Code 21*" — corrected from image. -->
<!-- NOTE: OCR read "Code 71-" (hyphen); page image p.162 clearly shows "Code 71*" — corrected from image, consistent with the footnote listing "codes 25, 26 and 71" as asterisked. -->

---

## 4. Information Sensors (PDF p.162–164)

> **Note:** Most of the components in this section are protected by a Federally-mandated extended warranty — see a dealer for details. It makes little sense to check or replace these parts yourself while still under warranty; once the warranty expires, the checks/replacement procedures below can save money.

### Oxygen sensor (all models)

The oxygen sensor is located in the exhaust manifold. It detects the concentration of oxygen in the exhaust gases. On some models, a second oxygen sensor is located in the catalytic converter — this sensor rechecks the emission level after the exhaust gases pass through the converter and feeds the results back to the main oxygen sensor so the air/fuel ratio is maintained as precisely as possible.

An open or shorted oxygen sensor circuit will set a **Code 21** or **Code 27**.

To replace an oxygen sensor: follow its wire back to the electrical connector and disconnect it, remove the oxygen sensor nuts or bolts, and remove the sensor. Reverse the removal steps to install the new sensor.

<!-- DIAGRAM CANDIDATE: p.163 — fig. 4.3, oxygen sensor mounting location on exhaust manifold (viewed from below) -->

**Carbureted models:** see [Feedback carburetor system](#8-feedback-carburetor-system-pdf-p168170), Section 8, for information on the feedback carburetor system.

### Coolant temperature sensor (fuel-injected models)

The coolant temperature sensor is a thermistor (a resistor whose resistance value varies with temperature). A failure in the coolant sensor or circuit will set a **Code 22**. The sensor is located in the thermostat housing or behind the distributor housing.

To check: unplug the electrical connector and use an ohmmeter to measure the resistance between the two terminals, then compare the reading to the resistance-vs-temperature graph.

<!-- DIAGRAM CANDIDATE: p.163 — figs. 4.6a/4.6b, coolant temperature sensor test setup and resistance-vs-temperature graph -->

If the indicated resistance is not as specified, replace the sensor. Use Teflon tape or thread sealant on the threads of the new sensor to prevent leaks.

### Intake Air Temperature (THA) sensor

The manifold air temperature (THA) sensor, located in the side of the air cleaner housing, is a thermistor that constantly measures the temperature of air entering the intake manifold. The ECU uses this reading to adjust the fuel quantity. A failure in the THA sensor or circuit will set a **Code 24**. Diagnosis of the THA sensor should be left to a dealer service department.

### Air Flow Meter (AFM) — 4A-GE engines

The air flow meter, located near the battery, measures the amount of air passing through it. The ECU uses this to control fuel delivery — a large air quantity indicates acceleration, a small quantity indicates deceleration or idle. A failure in the sensor or circuit will set a **Code 31**. Diagnosis of the AFM should be left to a dealer service department.

<!-- DIAGRAM CANDIDATE: p.164 — fig. 4.9, air flow meter location -->

### Vacuum (Manifold Absolute Pressure — MAP) sensor — 4A-FE engines

The vacuum sensor, also called a Manifold Absolute Pressure (MAP) sensor, monitors intake manifold pressure changes resulting from changes in engine load and speed, converting the reading into a voltage signal. The ECU uses the MAP sensor to control fuel delivery and ignition timing. Other than checking for vacuum, hose connection, or electrical connector problems, the only service possible is unit replacement should diagnosis show the sensor faulty.

<!-- DIAGRAM CANDIDATE: p.164 — fig. 4.10, MAP sensor location -->

### Throttle Position Sensor (TPS)

The TPS is located on the throttle body (4A-GE shown, 4A-FE similar). By monitoring the TPS output voltage, the ECU determines fuel delivery based on throttle valve angle (driver demand). A failure in the TPS sensor or circuit will set a **Code 41**. TPS diagnosis or replacement requires special tools and test equipment and should be done by a dealer service department.

<!-- DIAGRAM CANDIDATE: p.164 — fig. 4.12, throttle position sensor mounting on the throttle body -->

### Park/Neutral switch (automatic transaxle-equipped models only)

The Park/Neutral switch, on the automatic transaxle, indicates to the ECU when the transaxle is in Park or Neutral. The ECU uses this to control the fuel injectors and the ISC solenoid valve.

### Air conditioner (A/C) signal

The A/C amplifier supplies a signal to the ECU when the air conditioning is turned on, allowing the ECU to adjust engine speed for the additional load. A **Code 51** will set if this signal is not present. Diagnosis should be left to a dealer service department.

### Vehicle Speed Sensor (VSS)

The VSS consists of a lead switch and magnet built into the speedometer. As the magnet turns with the speedometer cable, its magnetic force switches the lead switch on and off; this pulsing voltage signal is sent to the ECU and converted into miles per hour. A failure sets a **Code 42**. Diagnosis and repair should be left to a dealer service department.

### Crank angle sensor

Located in the distributor; consists of a signal generator and signal rotor. As the signal rotor turns, a pulsing AC voltage is generated in the pick-up coil and sent to the ECU, which uses it to calculate engine speed and as one of the signals to control various devices.

### Engine start signal

Sent from the engine starter circuit. Receiving it, the ECU detects that the engine is cranking and uses it as one of the signals to control the fuel injectors.

### Electronic Spark Control (ESC) system

Two major components: the ESC module (part of the ECU) and the ESC knock sensor, mounted in the engine block near the cylinders. The knock sensor detects abnormal detonation; the ESC module receives that information and signals the ECU, which adjusts timing to reduce detonation. A failure sets **Code 52** or **Code 53**. Repair of this system should be left to a dealer service department.

---

## 5. Evaporative Emission Control (EVAP) System (PDF p.164–165)

This system is designed to trap and store fuel that evaporates from the fuel tank, carburetor and intake manifold, which would otherwise enter the atmosphere as hydrocarbon (HC) emissions.

The EVAP system consists of a charcoal-filled canister, hoses connecting the canister to the fuel tank, and a thermo switch or an ECU-controlled purge valve.

<!-- DIAGRAM CANDIDATE: p.165 — fig. 5.2b, typical EVAP system for 4A-GE engine models -->
<!-- DIAGRAM CANDIDATE: p.165 — fig. 5.2c, typical EVAP system for 4A-FE engine models -->

Fuel vapors are transferred from the fuel tank and carburetor to the canister, where they're stored while the engine isn't running. When the engine runs, the fuel vapors are purged from the canister by intake air flow and consumed in normal combustion.

On some models, the ECU operates a solenoid valve controlling vacuum to the purge valve in the charcoal canister. Under cold engine conditions the ECU turns the solenoid on, closing the valve; the ECU turns it off and allows purge when the engine is warm. On some models a bi-metal thermo switch controls canister purge instead.

### Checking

- Poor idle, stalling and poor driveability can be caused by an inoperative purge valve, a damaged canister, split/cracked hoses, or hoses connected to the wrong fittings. Check the fuel filler cap for a damaged or deformed gasket (see [Tune-up and Routine Maintenance](01-tune-up-and-routine-maintenance.md)).
- Evidence of fuel loss or fuel odor can be caused by liquid fuel leaking from fuel lines, a cracked/damaged canister, an inoperative purge valve, or disconnected/misrouted/kinked/deteriorated/damaged vapor or control hoses.
- Inspect every hose attached to the canister, along its entire length, for kinks, leaks and cracks. Repair or replace as necessary.
- Inspect the canister; if cracked or damaged, replace it.
- Look for fuel leaking from the bottom of the canister — if found, replace the canister and check the hoses and hose routing.
- Further testing should be left to a dealer service department.

### Charcoal canister replacement

1. Detach the negative cable from the battery.
2. Unplug the solenoid electrical connector(s), if equipped.
3. Clearly label, then detach the vacuum hoses from the canister.
4. Remove the canister mounting bolts and lift it out of the vehicle.
5. Installation is the reverse of removal.

<!-- DIAGRAM CANDIDATE: p.165 — fig. 5.13, charcoal canister removal — hose locations and mounting bracket pinch screw -->

---

## 6. Exhaust Gas Recirculation (EGR) System (PDF p.165–167)

To reduce oxides of nitrogen (NOx) emissions, some of the exhaust gases are recirculated through the EGR valve to the intake manifold, lowering combustion temperatures.

### Carbureted models

The EGR system consists of the EGR valve, EGR vacuum modulator, a check valve and a thermovalve. The EGR valve, operated by ported vacuum, recirculates gases in accordance with engine load (intake air volume); there is no recirculation at idle. The vacuum signal is ported above the throttle valve idle position. During cold engine operation, the thermovalve opens, bleeding off ported vacuum and keeping the EGR valve closed. When engine coolant temperature exceeds the thermovalve's set temperature, it closes and ported vacuum is applied to the EGR valve. The EGR vacuum modulator controls the EGR valve by controlling the vacuum signal to it with an atmospheric bleed; the bleed is controlled by the amount of exhaust pressure acting on the bottom of the EGR vacuum modulator.

<!-- DIAGRAM CANDIDATE: p.166 — fig. 6.2, typical EGR system diagram, carbureted models (EGR valve, EGR vacuum modulator, check valve, EGR port, EGR "R" port, pressure chamber, thermostatic vacuum switching valve, jet) -->

### Fuel-injected models

The EGR system consists of the EGR valve, the EGR modulator, a vacuum switching valve, the Electronic Control Module (ECU) and various sensors. The ECU memory is programmed to produce the ideal EGR valve lift for each operating condition.

<!-- DIAGRAM CANDIDATE: p.166 — fig. 6.3, typical EGR system diagram, fuel-injected models (EGR valve, EGR vacuum modulator, EGR vacuum switching valve, MAP sensor, distributor) -->

### Checking EGR valve

1. Start the engine and allow it to idle.
2. Detach the vacuum hose from the EGR valve and attach a hand vacuum pump in its place.
3. Apply vacuum to the EGR valve. Vacuum should remain steady and the engine should run poorly or stall.
   - If the vacuum doesn't remain steady and the engine doesn't run poorly, replace the EGR valve and recheck it.
   - If the vacuum remains steady but the engine doesn't run poorly, remove the EGR valve and check the valve and the intake manifold for blockage. Clean or replace parts as necessary and recheck.

### EGR vacuum modulator valve

1. Remove the valve (see [EGR valve](#component-replacement) below).
2. Pull the cover off and check the filters.
3. Clean them with compressed air, reinstall the cover and the modulator.

<!-- DIAGRAM CANDIDATE: p.166 — figs. 6.8a/6.8b, EGR vacuum modulator filter removal and cleaning -->

### EGR system

Any further checking of the EGR system requires special tools and test equipment. Take the vehicle to a dealer service department for checking.

### Component replacement

**EGR valve.** Disconnect the threaded fitting that attaches the EGR pipe to the EGR valve, remove the two EGR valve mounting bolts or nuts, remove the EGR valve from the intake manifold and check it for sticking and heavy carbon deposits. If the valve is sticking or clogged with deposits, clean or replace it.

<!-- DIAGRAM CANDIDATE: p.167 — fig. 6.11, EGR valve mounting on the intake manifold (4A-C engine model shown, others similar) -->

**EGR vacuum modulator valve.** Label and disconnect the vacuum hoses and remove the EGR vacuum modulator from its bracket. Installation is the reverse of removal.

<!-- DIAGRAM CANDIDATE: p.167 — fig. 6.13, EGR vacuum modulator valve location on a carbureted model -->

---

## 7. Positive Crankcase Ventilation (PCV) System (PDF p.167–168)

To reduce hydrocarbon (HC) emissions, crankcase blow-by gas is routed to the intake manifold for combustion in the cylinders.

**Carbureted models:** the main components of the PCV system are the PCV valve, a fresh-air filtered inlet, and the vacuum hoses connecting these components with the engine. To maintain idle quality, the PCV valve restricts flow when intake manifold vacuum is high. Under abnormal operating conditions, the system allows excess blow-by gases to flow back through the crankcase vent tube into the air cleaner to be consumed by normal combustion. Checking and replacement of the PCV valve on carbureted models is covered in [Tune-up and Routine Maintenance](01-tune-up-and-routine-maintenance.md).

<!-- DIAGRAM CANDIDATE: p.167 — fig. 7.1a, PCV system, carbureted models (4A-C shown, 4A-F similar) -->
<!-- DIAGRAM CANDIDATE: p.167 — fig. 7.1b, PCV system used on [4A-GE — caption truncated in source] -->

**4A-GE engine models:** the system consists only of a PCV hose between the valve cover and the intake manifold.

**4A-FE engine models:** the PCV system consists of a PCV valve and two hoses.

<!-- DIAGRAM CANDIDATE: p.168 — fig. 7.1c, PCV system, 4A-FE engine models (PCV hose, PCV valve, air cleaner, blow-by gas / fresh air flow paths) -->

---

## 8. Feedback Carburetor System (PDF p.168–170)

> **Note:** The feedback carburetor system and all related components are covered by a Federally mandated extended warranty. Check with a dealer service department before replacing or repairing system components at your own expense.

The feedback carburetor (FBC) system maintains the air/fuel ratio at the desired **14.7-to-1** ratio during normal operation. The system is designed to operate somewhat richer than desired, setting up the rich limit of system operation. When leaner operation is desired, the ECU commands air to be bled into the carburetor's main metering system and into the carburetor primary bore, giving a lean operating condition.

The various sub-systems and components of the feedback system are discussed below; checking and component replacement information is provided where possible.

- **Evaporative Emission Control (EVAP) system** — see [Section 5](#5-evaporative-emission-control-evap-system-pdf-p164165).
- **Feedback control system** — see [Fuel and Exhaust Systems](04-fuel-and-exhaust-systems.md).

### Deceleration Fuel Cut system

During deceleration, this system cuts off part of the fuel flow in the idle circuit of the carburetor to prevent overheating and afterburning in the exhaust system. The fuel cut solenoid is kept energized by the ECU whenever the engine is running, except when the throttle is closed with the engine speed above **2290 rpm**.

To check the system:

1. Hook up a tachometer per the manufacturer's instructions and start the engine.
2. Disconnect the throttle position switch connector, raise the engine speed to **2300 rpm**, and make sure the engine speed is fluctuating.
   > **CAUTION:** Perform this step quickly to prevent overheating the catalytic converter.
3. With the speed still at 2300 rpm, reconnect the connector and check that engine operation returns to normal.
4. If no problems are found, the system is okay. Any further checks or repairs should be left to a dealer service department.

<!-- DIAGRAM CANDIDATE: p.168 — fig. 8.7, disconnecting the throttle position switch connector -->

### Cold Mixture Heater (CMH) system

The CMH system reduces cold engine emissions and improves driveability during engine warm-up. The intake manifold is heated during cold engine operation to accelerate vaporization of liquid fuel. The ECU turns the CMH on and off according to engine coolant temperature.

1. To check: locate the connector, unplug it, and using an ohmmeter, measure the resistance between the terminals.
   - **Resistance: 0.5 – 2.0 Ω**
   - If not within specification, replace the heater. Any further checks should be done by a dealer service department or other repair shop.
2. To replace: first remove the carburetor (see [Fuel and Exhaust Systems](04-fuel-and-exhaust-systems.md)).
3. Unplug the cold mixture heater connector, remove the PCV hose, and lift the heater from the intake manifold.
4. Installation is the reverse of removal.

<!-- DIAGRAM CANDIDATE: p.169 — fig. 8.13, cold mixture heater removal from the intake manifold -->

### Positive Crankcase Ventilation (PCV) system

See [Section 7](#7-positive-crankcase-ventilation-pcv-system-pdf-p167168) for information on this system.

### Throttle Positioner (TP)

To reduce HC and CO emissions, the throttle positioner opens the throttle valve slightly when decelerating, keeping the air/fuel ratio from becoming excessively rich when the throttle valve is quickly closed. The TP also increases idle speed when power steering fluid pressure exceeds a preset value and when a large electrical load is placed on the electrical system. Any checks or repairs should be left to a dealer service department.

### Exhaust Gas Recirculation (EGR) system

See [Section 6](#6-exhaust-gas-recirculation-egr-system-pdf-p165167) for information on this system.

### Catalytic Converter

See [Section 9](#9-catalytic-converter-pdf-p170171) for further information.

### Air Suction (AS) system

Additional oxygen is needed to aid the oxidation of HC and CO in the catalytic converter. The air suction valve is a simple reed-type valve that opens when vacuum is present in the exhaust system; when open, oxygen-rich air is drawn into the exhaust to aid the converter's oxidation process.

To check the system: first check the hoses and fittings for cracks, kinks, damage or loose connections. Remove the air cleaner top cover.

- **Federal models:** with the engine idling, check that a burbling noise is heard from the air suction valve inlet. Any further checks or repairs should be left to a dealer service department.
- **California models:** disconnect and plug the shut-off valve vacuum hose. Start the engine, unplug and reconnect the hose, and listen for a burbling noise from the air suction valve inlet — it should occur within **2 to 6 seconds**. Any further checks or repairs should be left to a dealer service department.

<!-- DIAGRAM CANDIDATE: p.170 — fig. 8.21a, listening point for burbling noise at the air suction valve inlet -->
<!-- DIAGRAM CANDIDATE: p.170 — fig. 8.21b, AS shut-off valve vacuum hose disconnect point, California models -->

### High Altitude Compensation (HAC) system (Federal models only)

As altitude increases, air density decreases, making the air/fuel mixture richer. The HAC system ensures the proper air/fuel mixture by supplying additional air to the primary and high-speed circuit of the carburetor, and also advances ignition timing to improve driveability at high altitudes.

To check: first inspect all hoses for cracks, kinks, damage or loose connections. Check and clean the air filter in the HAC valve. Any further checks or repairs should be left to a dealer service department.

<!-- DIAGRAM CANDIDATE: p.170 — fig. 8.24, HAC cover and filter removal -->

### Thermostatic Air Cleaner (TAC) system

This system directs hot air to the carburetor in cold weather to improve driveability and prevent carburetor icing in extremely cold weather. See [Tune-up and Routine Maintenance](01-tune-up-and-routine-maintenance.md) for the TAC system check.

### Hot Idle Compensation (HIC) system

The HIC system allows additional air to enter the intake manifold to maintain proper air/fuel mixture during high temperatures at idle.

To check: remove the HIC valve from the air cleaner housing.

- With the temperature **above 72°F**, check operation of the valve by placing a finger over the atmospheric port and blowing into the port for the HIC diaphragm. Air should flow from the port normally connected to the carburetor.
- At temperatures **below 72°F**, carry out a similar air flow test: place a finger over the port normally connected to the carburetor, blow through the port for the HIC diaphragm, and make sure air does not pass out of the atmospheric port.

<!-- DIAGRAM CANDIDATE: p.170 — fig. 8.28, HIC valve vacuum hose labeling and mounting screws -->

**Typical HIC valve ports** (fig. 8.29):

| # | Port |
| - | ---- |
| 1 | Carburetor port |
| 2 | Hot air intake diaphragm port |
| 3 | Atmosphere port |

### Automatic Choke

The automatic choke system temporarily supplies a rich air/fuel mixture to the engine by closing the choke valve when the engine is cold, and automatically opens the choke as the engine warms up. See [Tune-up and Routine Maintenance](01-tune-up-and-routine-maintenance.md) for the choke check procedure. Any further checks or repairs should be left to a dealer service department.

### Auxiliary Acceleration Pump (AAP)

When accelerating with a cold engine, the main acceleration pump's capacity is insufficient. The AAP system compensates by forcing more fuel into the acceleration nozzle for better cold-engine performance. A thermostatic control valve controls the AAP system; after the engine is warmed up, the valve lets the main acceleration pump take over. Any checks or repairs should be left to a dealer service department.

### Heat Control Valve

When the engine is cold, the heat control valve improves fuel vaporization for better driveability by quickly heating the intake manifold. Once the engine has warmed up, the valve helps keep the intake manifold at the proper temperature. The valve is located in the exhaust manifold and can be seen best from under the vehicle.

Check the heat control valve when the engine is cold: the counterweight should be in its **upper** position. After warm-up, check that the counterweight is in its **lower** position. If the valve is stuck, apply penetrating oil to the shaft to free it.

<!-- DIAGRAM CANDIDATE: p.170 — fig. 8.34, heat control valve counterweight positions (cold vs. warm) -->

---

## 9. Catalytic Converter (PDF p.170–171)

> **Note:** Because of a federally mandated extended warranty covering emissions-related components such as the catalytic converter, check with a dealer service department before replacing the converter at your own expense.

### General description

To reduce hydrocarbon (HC), carbon monoxide (CO) and oxides of nitrogen (NOx) emissions, all vehicles are equipped with a three-way catalyst system, which oxidizes and reduces these chemicals, converting a large percentage of them into harmless nitrogen, carbon dioxide and water.

### Checking

1. Periodically inspect the catalytic-converter-to-exhaust-pipe mating flanges and bolts. Make sure there are no loose bolts and no leaks between the flanges.
2. Look for dents in or damage to the catalytic converter protector/shield. If any part of the protector is damaged or dented enough to touch the converter, repair or replace it.
3. Inspect the heat insulator for damage. Make sure there is adequate clearance between the heat insulator and the catalytic converter.

<!-- DIAGRAM CANDIDATE: p.171 — figs. 9.3/9.4, catalytic converter shield and heat insulator inspection points (underbody-mounted converters) -->

### Replacement

To replace the catalytic converter, refer to [Fuel and Exhaust Systems](04-fuel-and-exhaust-systems.md).
