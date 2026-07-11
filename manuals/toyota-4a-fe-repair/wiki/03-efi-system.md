# EFI System (4A-FE / 4A-GE)

*Section code: `FI` | PDF pages 76-169 of `Toyota-4A-FE-4A-GE-engine-repair-manual-OCR.pdf` | 94 pages*

> Faithful transcription by image-verified parallel agents. This is the largest section and
> the most heavily **4A-FE / 4A-GE interleaved** — subsections are engine-tagged as the
> manual tags them (e.g. "w/ air flow meter" vs "w/o air flow meter", TWC vs non-TWC).
> Every numeric spec was checked against the page image. This scan is abridged — the FI
> section-page codes skip in places (missing pages), flagged inline. See
> [llm-instructions.md](llm-instructions.md).

## In this chapter

- [SYSTEM DESCRIPTION](#p76) — [PDF p.76]
- [TROUBLESHOOTING (symptom tables)](#p90) — [PDF p.90]
- [FUSES / EFI SYSTEM CHECK](#p104) — [PDF p.104]
- [TROUBLESHOOTING WITH VOLT/OHMMETER](#p118) — [PDF p.118]
- [FUEL SYSTEM (pump, injectors)](#p124) — [PDF p.124]
- [AIR INDUCTION / AUXILIARY AIR VALVE](#p146) — [PDF p.146]
- [ELECTRONIC CONTROL / SENSORS / OXYGEN SENSOR / ECU](#p152) — [PDF p.152]

---
<a id="p76"></a>
**[PDF p.76]** — FI-1 — EFI SYSTEM (section contents)

# EFI SYSTEM

| Section | Page |
|---|---|
| SYSTEM DESCRIPTION | FI-2 |
| PRECAUTIONS | FI-8 |
| INSPECTION PRECAUTIONS | FI-8 |
| TROUBLESHOOTING | FI-14 |
| DIAGNOSIS SYSTEM | FI-25 |
| TROUBLESHOOTING WITH VOLT/OHMMETER | FI-34 |
| FUEL SYSTEM | FI-94 |
| &nbsp;&nbsp;Fuel Pump | FI-94 |
| &nbsp;&nbsp;Cold Start Injector | FI-105 |
| &nbsp;&nbsp;Fuel Pressure Regulator | FI-109 |
| &nbsp;&nbsp;Injectors | FI-111 |
| AIR INDUCTION SYSTEM | FI-120 |
| &nbsp;&nbsp;Air Flow Meter (w/ Air Flow Meter) | FI-120 |
| &nbsp;&nbsp;Throttle Body (4A-FE) | FI-122 |
| &nbsp;&nbsp;Auxiliary Air Valve | FI-131 |
| ELECTRONIC CONTROL SYSTEM | FI-133 |
| &nbsp;&nbsp;Location of Electronic Control Parts | FI-133 |
| &nbsp;&nbsp;EFI Main Relay | FI-134 |
| &nbsp;&nbsp;Circuit Opening Relay | FI-135 |
| &nbsp;&nbsp;Start Injector Time Switch | FI-137 |
| &nbsp;&nbsp;Water Temperature Sensor | FI-138 |
| &nbsp;&nbsp;Intake Air Temperature Sensor (w/o Air Flow Meter) | FI-139 |
| &nbsp;&nbsp;Vacuum Sensor (w/o Air Flow Meter) (Manifold Absolute Pressure Sensor) | FI-140 |
| &nbsp;&nbsp;Variable Resistor (w/o TWC) | FI-142 |
| &nbsp;&nbsp;Oxygen Sensor (w/ TWC) | FI-145 |
| &nbsp;&nbsp;Engine ECU | FI-147 |
| &nbsp;&nbsp;Fuel Cut RPM | FI-153 |
| &nbsp;&nbsp;Fuel Pressure Control System (4A-GE Europe) | FI-154 |
| &nbsp;&nbsp;Idle-up System (w/ Air Flow Meter) | FI-156 |
| &nbsp;&nbsp;Idle Speed Control (ISC) Valve (4A-FE) | FI-158 |

---
<a id="p77"></a>
**[PDF p.77]** — FI-2 — EFI SYSTEM — System Description

# SYSTEM DESCRIPTION

**4A-FE (2WD, w/o EGR System)** — system schematic diagram

*(image only — see [PDF p.77])* Labeled components: "CHECK ENGINE" Warning Light, Battery, ECU, Ignition Switch, Starter, Circuit Opening Relay, Fuel Pump, Fuel Tank, A/C, Variable Resistor, Speed Sensor, Throttle Position Sensor, Vacuum Sensor, Fuel Pressure Regulator, IIA, Injector, Cold Start Injector, ISC Valve, Air Valve, Intake Air Temp. Sensor, Water Temp. Sensor, Start Injector Time Switch.

---
<a id="p78"></a>
**[PDF p.78]** — FI-3 — EFI SYSTEM — System Description

# SYSTEM DESCRIPTION (Cont'd)

**4A-FE (2WD, w/ EGR System)** — system schematic diagram

*(image only — see [PDF p.78])* Labeled components: "CHECK ENGINE" Warning Light, Battery, ECU, Ignition Switch, Starter, Circuit Opening Relay, Fuel Pump, Charcoal Canister, Fuel Tank, A/C, Fuel Control Switch, Speed Sensor, Throttle Position Sensor, Vacuum Sensor, VSV (EGR), EGR Vacuum Modulator, EGR Valve, Fuel Pressure Regulator, Injector, IIA, ISC Valve, Air Valve, Intake Air Temp. Sensor, Oxygen Sensor, TWC, Cold Start Injector, Water Temp. Sensor, BVSV, Start Injector Time Switch.

> **Scan gap:** pages FI-4 to FI-6 are missing from this scan.

---
<a id="p79"></a>
**[PDF p.79]** — FI-7 — EFI SYSTEM — System Description

The EFI system is composed of three basic subsystems: Fuel, Air Induction and Electronic Control System.

## FUEL SYSTEM

Fuel is supplied under constant pressure to the EFI injectors by an electric fuel pump. The injectors inject a metered quantity of fuel into the intake ports in accordance with signals from the ECU (Electronic Control Unit).

## AIR INDUCTION SYSTEM

The air induction system provides sufficient air for engine operation.

## ELECTRONIC CONTROL SYSTEM

4A-FE, 4A-GE engines are equipped with a Toyota Computer Control System (TCCS) which centrally controls the EFI, ESA, Diagnosis systems, etc. by means of an Electronic Control Unit (ECU-formerly EFI computer) employing a microcomputer.

The ECU, the TCCS controls the following functions:

1. **Electronic Fuel Injection (EFI)**

   The ECU receives signals from various sensors indicating changing engine operating conditions such as:
   - Intake manifold absolute pressure (w/o Air flow meter)
   - Intake air volume (w/ Air flow meter)
   - Intake air temperature
   - Coolant temperature
   - Engine rpm
   - Throttle valve opening valve
   - Exhaust oxygen content (w/ TWC) etc.

   These signals are utilized by the ECU to determine the injection duration necessary for an optimum air-fuel ratio.

2. **Electronic Spark Advance (ESA)**

   The ECU is programmed with data for optimum ignition timing under any and all operating conditions. Using data provided by sensors which monitor various engine functions (rpm, coolant temperature, etc.), the microcomputer (ECU) triggers the spark at precisely the right instant. (See IG section)

3. **Diagnosis**

   The ECU detects any malfunctions or abnormalties in the sensor network and lights a "CHECK ENGINE" warning light on the instrument panel. At the same time, the trouble is identified and a diagnostic code is recorded by the ECU. The diagnostic code can be read by the number of blinks of the check engine warning light when terminals TE1 and E1 are connected. The diagnostic codes are refered to the later page. (See pages FI-28 to 31)

4. **Fail-Safe Function**

   In the event of the sensor malfanctioning, a back-up circuit will take over to provide minimal driveability, and the "CHECK ENGINE" warning light will illuminate.

---
<a id="p80"></a>
**[PDF p.80]** — FI-8 — EFI SYSTEM — Precautions, Inspection Precaution

# PRECAUTIONS

1. Before working on the fuel system, disconnect the negative (−) terminal from the battery.

   > **HINT:** Any diagnostic code retained by the computer will be cleared when the battery terminal is removed. Therefore, if necessary, read the diagnosis before removing the battery terminal.

2. (w/ AIRBAG) Work must be started after approx. **20 seconds** or longer from the time the ignition switch is turned to the "LOCK" position and the negative (−) terminal cable is disconnected from the battery.

3. When working on the fuel system, do not smoke or work near any fire hazard.

4. Keep gasoline off rubber or leather parts.

# INSPECTION PRECAUTIONS

## MAINTENANCE PRECAUTIONS

1. **CHECK CORRECT ENGINE TUNE-UP**

2. **PRECAUTIONS WHEN CONNECTING GAUGE**

   a. Connect the tachometer test probe to the IG ⊝ terminal of the check connector.

   LOCATION: See page FI-133

   b. Use the battery as the power source for the timing light, tachometer, etc.

   *(image — Tachometer, Check Connector, IG ⊝, Battery. Also 4A-FE CORRECT / WRONG probe-connection illustration.)*

3. **IN EVENT OF ENGINE MISFIRE, THE CATALYTIC VERTER MAY OVERHEAT. THEREFORE, THE FOLLOWING PRECAUTIONS SHOULD BE TAKEN**

   a. Check proper connection of battery terminals, etc.

   b. Handle high-tension cords carefully.

   c. After repair work, check that all ignition system wirings are reconnected securely.

   d. When cleaning the engine compartment, be especially careful to protect the electrical system from water.

4. **PRECAUTIONS WHEN HANDLING OXYGEN SENSOR**

   a. Do not allow the oxygen sensor to receive any physical impact or shocks.

   b. Do not allow water to come into contact with the sensor.

> **Scan gap:** page FI-9 is missing from this scan.

---
<a id="p81"></a>
**[PDF p.81]** — FI-10 — EFI SYSTEM — Inspection Precaution

## ELECTRONIC CONTROL SYSTEM

1. Before removing EFI wiring connectors, terminals, etc., first disconnect power by either turning OFF the ignition switch or disconnecting the battery terminals.

2. When installing the battery, be especially careful not to incorrectly connect the positive (+) and negative (−) cables.

3. Do not permit parts to touch during removal or installation. Handle all EFI parts carefully and, in particular, the ECU.

4. Take great care during troubleshooting as there are numerous transistor circuits and even slight terminal contact can cause further troubles.

5. Do not open the ECU cover.

6. When inspecting during rainy weather, take care to prevent entry of water. Also, when washing the engine compartment, prevent water from getting on the EFI parts and wiring connectors.

7. Parts should be replaced as an assembly.

8. Care is required when pulling out and inserting wiring connectors.

   a. To pull the connector out, release the lock and pull on the connector. *(image: Lock, Lock Spring)*

   b. Fully insert the connector and check that it is locked. *(image: Lock)*

9. When inspecting a connector with a volt/ohmmeter.

   a. Carefully move away the water-proofing rubber if it is a water-proof type connector.

---
<a id="p82"></a>
**[PDF p.82]** — FI-11 — EFI SYSTEM — Inspection Precautions

(continued: item 9, When inspecting a connector with a volt/ohmmeter)

   b. Insert the tester probe into the connector from wiring side when checking the continuity, amperage or voltage.

   c. Do not apply unnecessary force to the terminal.

   d. After the check, securely install the water-proofing rubber on the connector.

10. Use SST for inspection or test of the injector, cold start injector or their wiring connectors.

    **SST 09842-30055 (A)** and **09842-30070 (B)**

## FUEL SYSTEM

1. When disconnecting the flare nut or union bolt on the high pressure pipe union, observe the following procedure.

   a. Put a container under the connection.

   b. Slowly loosen the connection.

   c. Disconnect the connection.

   d. Plug the connection with a rubber plug.

2. When connecting the flare nut or union bolt on the high pressure pipe union, observe the following procedure.

   **(Union bolt type)**
   a. Always use a new gasket.
   b. Hand tighten the union bolt.
   c. Torque the bolt to the specified torque.

   **(Flare nut type)**
   a. Apply a thin coat of oil to the flare and tighten the flare nut.
   b. Then using SST, torque the unit to the specified torque.

   **SST 09631-22020**

   **Torque: 310 kg-cm (22 ft-lb, 30 N·m)**

   > **HINT:** Use a torque wrench with a fulcrum length of **30 cm (11.81 in.)**.

---
<a id="p83"></a>
**[PDF p.83]** — FI-12 — EFI SYSTEM — Inspection Precautions

3. Take the following precautions when removing and installing the injectors. **(4A-FE, Ex. Australia)**

   a. Never reuse the O-ring.

   b. When placing an O-ring on the injector, use care not to damage it in any way.

   c. Lubricate the O-ring with spindle oil or gasoline before installing. Never use engine, gear or brake oil.

   *(image: 4A-FE (Ex. Australia) — O-Ring, Grommet, Delivery Pipe, Injector; CORRECT / WRONG installation)*

4. Install the injector to the delivery pipe and cylinder head as shown in the figure. **(4A-FE, Ex. Australia)**

   *(image: Delivery Pipe, O-Ring, Grommet, Injector, Insulator, Cylinder Head)*

5. Confirm that there are no fuel leaks after performing maintenance on the fuel system.

   a. With engine stopped, turn the ignition switch ON.

   b. Using SST, connect terminals +B and FP of the check connector.

   **SST 09843-18020**

   LOCATION: See page FI-133

   *(image: Check Connector — FP, +B; SST)*

---
<a id="p84"></a>
**[PDF p.84]** — FI-13 — EFI SYSTEM — Inspection Precautions

(continued: item 5, confirm no fuel leaks)

   c. When the fuel return hose is pinched, the pressure within high pressure line will rise to approx. **4 kg/cm² (57 psi, 392 kPa)**. In this state, check to see that there are no leaks from any part of the fuel system.

   > **NOTICE:** Always pinch the hose. Avoid bending the hose as it may cause the hose to crack.

   *(image: 4A-FE — Return Hose)*

   d. Remove SST from the check connector.

   **SST 09843-18020**

   *(image: SST)*

---
<a id="p85"></a>
**[PDF p.85]** — FI-14 — EFI SYSTEM — Troubleshooting

# TROUBLESHOOTING

## TROUBLESHOOTING HINTS

1. Engine trouble are usually not caused by the EFI system. When troubleshooting, always firstly check the condition of the other systems.

   a. Electronic source
      - Battery
      - Fusible links
      - Fuses

   b. Body ground

   c. Fuel supply
      - Fuel leakage
      - Fuel filter
      - Fuel pump

   d. Ignition system
      - Spark plugs
      - High-tension cords
      - IIA or Distributor
      - Ignition coil
      - Igniter

   e. Air induction system
      - Vacuum leaks

   f. Emission control system
      - PCV system
      - EGR system (w/ EGR system)

   g. Others
      - Ignition timing
      - Idle speed
      - etc.

2. The most frequent cause of problems is simply a bad contact in wiring connectors. Always check that connections are secure. When inspecting the connector, pay particular attention to the following points:

   a. Check to see that the terminals are not bent.

   b. Check to see that the connector is pushed in completely and locked.

   c. Check to see that there is no signal change when the connector is slightly tapped or wiggled.

3. Sufficiently troubleshooting for other causes before replacing the ECU, as the ECU is high quality and expensive.

*(images: Lock connector; connector wiggle test)*

---
<a id="p86"></a>
**[PDF p.86]** — FI-15 — EFI SYSTEM — Troubleshooting

4. Use a volt/ohmmeter with high impedance (**10 kΩ/V minimum**) for troubleshooting of the electrical circuit. (See page FI-34)

*(image: Digital Type and Analog Type volt/ohmmeter)*

## TROUBLESHOOTING PROCEDURES

### SYMPTOM — DIFFICULT TO START OR NO START (ENGINE WILL NOT CRANK OR CRANKS SLOWLY)

| Check | Result | If BAD → Suspect |
|---|---|---|
| CHECK ELECTRIC SOURCE | BAD → | 1. Battery — (1) Connection, (2) Gravity–Drive belt–charging system, (3) Voltage. 2. Fusible link |
| ↓ OK — CHECK STARTING SYSTEM | BAD → | 1. Ignition switch. 2. Starter. 3. Neutral start switch (A/T). 4. Wiring/Connection |

### SYMPTOM — DIFFICULT TO START OR NO START (CRANKS OK)

| Check | Result | If bad → Suspect |
|---|---|---|
| CHECK DIAGNOSIS SYSTEM — Check for output of diagnosis code. (See page FI-25) | Malfunction code(s) → | Diagnosis code(s): 4A-FE (See page FI-28); 4A-GE (See page FI-29) |
| ↓ Normal code — CHECK FOR VACUUM LEAKS IN AIR INTAKE LINE | BAD → | 1. Oil dipstick. 2. Hose connection(s). 3. PCV hose(s). 4. EGR system — EGR valve stays open |
| ↓ OK — CHECK IGNITION SPARK — 4A-FE (See page IG-6); 4A-GE (See page IG-10) | BAD → | 1. High-tension cords. 2. IIA, Distributor. 3. Ignition coil, igniter |
| ↓ OK — CHECK IGNITION TIMING — 1. Short terminals TE1 and E1 of the check connector. 2. Check ignition timing. **Standard: 10° BTDC @ idle** | NO → | Ignition timing — Adjust: 4A-FE (See page EM-20); 4A-GE (See page EM-28) |
| ↓ OK | | CONTINUED ON PAGE FI-16 |

---
<a id="p87"></a>
**[PDF p.87]** — FI-16 — EFI SYSTEM — Troubleshooting

*(CONTINUED FROM PAGE FI-15)*

| Check | Result | If bad → Suspect |
|---|---|---|
| CHECK FUEL SUPPLY TO INJECTOR — 1. Fuel in tank. 2. Fuel pressure in fuel line: (1) Connect terminals +B and FP of the check connector. (2) Fuel pressure at fuel hose of fuel filter can be felt. (See page FI-95) | BAD → | 1. Fuel line — Leakage — deformation. 2. Fuse. 3. Circuit opening relay (See page FI-135). 4. Fuel pump (See page FI-94). 5. Fuel filter. 6. Fuel pressure regulator (See page FI-109) |
| ↓ OK — (w/ AIR FLOW METER) CHECK FUEL PUMP SWITCH IN AIR FLOW METER — Check continuity between terminals FC and E1 while measuring plate of air flow meter is open. | BAD → | Air flow meter (See page FI-120) |
| ↓ OK — CHECK SPARK PLUGS — **Standard: 0.8 mm (0.031 in.)** HINT: Check compression pressure and valve clearance if necessary. | NO → | 1. Spark plugs. 2. Compression pressure — **Minimum: 10.0 kg/cm² (142 psi, 981 kPa) at 250 rpm**. 3. Valve clearance (Cold) — **Standard: IN 0.15 − 0.25 mm (0.006 − 0.010 in.); EX 0.20 − 0.30 mm (0.008 − 0.0012 in.)** |
| (same CHECK SPARK PLUGS step) | BAD / ALL Plugs WET → | 1. Injectors — shorted or leaking. 2. Injector wiring — short circuited. 3. Cold start injector — leakage (See page FI-105). 4. Start injector time switch (See page FI-137) |
| ↓ OK — CHECK AUXILIARY AIR VALVE (See page FI-130) | BAD → | 1. Auxiliary air valve. 2. Water by-pass hose(s). 3. Air hose(s) |
| ↓ OK — CHECK INTAKE VALVE | BAD → | Intake valve — carbon deposits |
| ↓ OK — CHECK EFI ELECTRONIC CIRCUIT USING VOLT/OHMMETER (See page FI-34) | BAD → | 1. Wiring connection(s). 2. Power to ECU: (1) Fusible link(s), (2) Fuse(s), (3) EFI main relay. 3. Air flow meter (w/ Air flow meter). 4. Vacuum sensor (w/o Air flow meter). 5. Water temp. sensor. 6. Intake air temp. sensor. 7. Injection signal circuit: (1) Injector wiring, (2) ECU |

<!-- NEEDS REVIEW: EX valve clearance upper bound printed as "0.30 mm (0.008 − 0.0012 in.)"; the in. value "0.0012" is a manual typo for "0.012" but transcribed as printed on the image. -->

---
<a id="p88"></a>
**[PDF p.88]** — FI-17 — EFI SYSTEM — Troubleshooting

### SYMPTOM — ENGINE OFTEN STALLS

| Check | Result | If bad → Suspect |
|---|---|---|
| CHECK DIAGNOSIS SYSTEM — Check for output of diagnostic code. (See page FI-25) | Malfunction code(s) → | Diagnostic code(s): 4A-FE (See page FI-28); 4A-GE (See page FI-29) |
| ↓ Normal code — CHECK FOR VACUUM LEAKS IN AIR INTAKE LINE | BAD → | 1. Oil dipstick. 2. Hose connection(s). 3. PCV hose(s). 4. EGR system — EGR valve stays open |
| ↓ OK — CHECK FUEL SUPPLY TO INJECTOR — 1. Fuel in tank. 2. Fuel pressure in fuel line: (1) Connect terminals +B and FP of the check connector. (2) Fuel pressure at fuel hose of fuel filter. (See page FI-95) | BAD → | 1. Fuel line — leakage — deformation. 2. Fuse(s). 3. Circuit opening relay (See page FI-135). 4. Fuel pump (See page FI-94). 5. Fuel filter. 6. Fuel pressure regulator (See page FI-109) |
| ↓ OK — CHECK AIR FILTER ELEMENT | BAD → | Element — Clean or replace |
| ↓ OK — CHECK IDLE SPEED (AND IDLE CO CONCENTRATION) — **Standard: 800 rpm** | NO → | Idle speed — Adjust: 4A-FE (See pages EM-22, 23); 4A-GE (See pages EM-30, 31) |
| ↓ OK — CHECK IGNITION TIMING — 1. Connect terminals TE1 and E1 of the check connector. 2. Check ignition timing. **Standard: 10° BTDC @ idle** | NO → | Ignition timing — Adjust: 4A-FE (See page EM-20); 4A-FE (See page EM-28) |
| ↓ OK — CHECK SPARK PLUGS — **Standard: 0.8 mm (0.031 in.)** HINT: Check compression pressure and valve clearance if necessary. | NO → | 1. Spark plugs. 2. Compression pressure — **Minimum: 10.0 kg/cm² (142 psi, 981 kPa) at 250 rpm**. 3. Valve clearance (Cold) — **Standard: IN 0.15 − 0.25 mm (0.006 − 0.010 in.); EX 0.20 − 0.30 mm (0.008 − 0.012 in.)** |
| ↓ OK — CHECK COLD START INJECTOR (See page FI-105) | BAD → | 1. Cold start injector. 2. Start injector time switch (See page FI-137) |
| ↓ OK | | CONTINUED ON PAGE FI-18 |

<!-- NEEDS REVIEW: Ignition-timing "Adjust" box lists "4A-FE (See page EM-20)" then "4A-FE (See page EM-28)"; the second is printed 4A-FE on the image but is almost certainly 4A-GE (cf. FI-15 which reads 4A-GE / EM-28). Transcribed as printed. -->

---
<a id="p89"></a>
**[PDF p.89]** — FI-18 — EFI SYSTEM — Troubleshooting

*(CONTINUED FROM PAGE FI-17)*

| Check | Result | If bad → Suspect |
|---|---|---|
| CHECK AUXILIARY AIR VALVE (See page FI-131) | BAD → | 1. Auxiliary air valve. 2. Water hose(s). 3. Air hose(s) |
| ↓ OK — CHECK FUEL PRESSURE (See page FI-97) | BAD → | 1. Fuel pump (See page FI-94). 2. Fuel filter. 3. Fuel pressure regulator (See page FI-109) |
| ↓ OK — CHECK INJECTORS (See page FI-111) | BAD → | Injection condition |
| ↓ OK — CHECK EFI ELECTRONIC CIRCUIT USING VOLT/OHMMETER (See page FI-34) | BAD → | 1. Wiring connections. 2. Power to ECU: (1) Fusible link(s), (2) Fuse(s), (3) EFI main relay. 3. Air flow meter (w/ Air flow meter). 4. Vacuum sensor (w/o Air flow meter). 5. Water temp. sensor. 6. Intake air temp. sensor. 7. Injection signal circuit: (1) Injector wiring, (2) ECU |

### SYMPTOM — ENGINE SOMETIMES STALLS

| Check | Result | If bad → Suspect |
|---|---|---|
| CHECK DIAGNOSTIC SYSTEM — Check for output of diagnostic code. (See page FI-25) | Malfunction code(s) → | Diagnostic cord(s): 4A-FE (See page FI-28) |
| ↓ Normal code — (w/ AIR FLOW METER) CHECK AIR FLOW METER (See page FI-120) | BAD → | Air flow meter |
| ↓ OK — (w/o AIR FLOW METER) CHECK VACUUM SENSOR (See page FI-140) | BAD → | Vacuum sensor |
| ↓ OK — CHECK WIRING CONNECTORS AND RELAYS — Check that there is a signal change when the connector or relay is slightly tapped or wiggled. | BAD → | 1. Connectors. 2. EFI main relay (See page FI-134). 3. Circuit opening relay (See page FI-135) |
---
<a id="p90"></a>
**[PDF p.90]** — EFI SYSTEM — Troubleshooting — FI-19

## SYMPTOM — ROUGH IDLING AND/OR MISSING

*Diagnostic flowchart. Unless a branch is shown, an **OK / Normal** result proceeds down to the next check.*

| Check | Branch | Trouble area / action |
|---|---|---|
| **CHECK DIAGNOSIS SYSTEM** — Check for output of diagnostic code. (See page FI-25) | Malfunction code(s) | Diagnostic code(s) — **4A-FE** (See page FI-28) |
| ↳ Normal code → continue | | |
| **CHECK FOR VACUUM LEAKS IN AIR INTAKE LINE** | BAD | 1. Oil dipstick 2. Hose connection(s) 3. PCV hose(s) 4. EGR system — EGR valve stays open |
| **CHECK AIR FILTER ELEMENT** | BAD | Element — Clean or replace |
| **CHECK IDLE SPEED (AND IDLE CO CONCENTRATION)** — Standard: **800 rpm** | NO | Idle speed — Adjust — **4A-FE** (See pages EM-22, 23); **4A-GE** (See pages EM-30, 31) |
| **CHECK IGNITION TIMING** — 1. Connect terminals TE1 and E1 of the check connector. 2. Check ignition timing. Standard: **10° BTDC @ idle** | NO | Ignition timing — Adjust — **4A-FE** (See page EM-20); **4A-GE** (See page EM-28) |
| **CHECK SPARK PLUGS** — Standard: **0.8 mm (0.031 in.)** > **HINT:** Check compression pressure and valve clearance if necessary. | NO | 1. Spark plugs 2. Compression pressure — Minimum: **10.0 kg/cm² (142 psi, 981 kPa)** at **250 rpm** 3. Valve clearance (Cold) — Standard: IN **0.15 – 0.25 mm (0.006 – 0.010 in.)**, EX **0.20 – 0.30 mm (0.008 – 0.012 in.)** |
| **CHECK COLD START INJECTOR** (See page FI-105) | BAD | 1. Cold start injector 2. Start injector time switch (See page FI-137) |
| **CHECK FUEL PRESSURE** (See page FI-97) | BAD | 1. Fuel pump (See page FI-94) 2. Fuel filter 3. Fuel pressure regulator (See page FI-109) |

OK → **CONTINUED ON PAGE FI-20**

---
<a id="p91"></a>
**[PDF p.91]** — EFI SYSTEM — Troubleshooting — FI-20

**CONTINUED FROM PAGE FI-19** (OK)

*Unless a branch is shown, an **OK** result proceeds down to the next check.*

| Check | Branch | Trouble area / action |
|---|---|---|
| **CHECK INJECTORS** (See page FI-111) | BAD | Injection condition |
| **CHECK EFI ELECTRONIC CIRCUIT USING VOLT/OHMMETER** (See page FI-34) | BAD | 1. Wiring connections 2. Power to ECU — (1) Fusible link(s) (2) Fuse(s) (3) EFI main relay 3. Air flow meter (w/ Air flow meter) 4. Vacuum sensor (w/o Air flow meter) 5. Water temp. sensor 6. Intake air temp. sensor 7. Injection signal circuit — (1) Injector wiring (2) ECU 8. Oxygen sensor (w/ TWC) |
| **(w/o TWC) CHECK VARIABLE RESISTOR** (See page FI-142) | BAD | Variable resistor |

## SYMPTOM — HIGH ENGINE IDLE SPEED (NO DROP)

| Check | Branch | Trouble area / action |
|---|---|---|
| **CHECK ACCELERATOR LINKAGE** | BAD | Linkage — Stuck |
| **CHECK AUXILIARY AIR VALVE** (See page FI-131) | BAD | Auxiliary air valve — Always open |
| **(4A-FE) CHECK ISC VALVE** (See page FI-158) | BAD | 1. ISC valve 2. Air pipe(s) 3. Air hose(s) |
| **CHECK FOR VACUUM LEAKS IN AIR INTAKE LINE** | BAD | 1. Oil dipstick 2. Hose connection(s) 3. PCV hose(s) 4. EGR system — EGR valve stays open 5. Brake booster line 6. Throttle valve adjusting (open stick) |
| **CHECK AIR CONDITIONER IDLE-UP CIRCUIT** | BAD | Air valve for air conditioner — Leakage |
| **CHECK DIAGNOSIS SYSTEM** — Check for output of diagnostic code. (See page FI-25) | Malfunction code(s) | Diagnostic code(s) — **4A-FE** (See page FI-28) |
| ↳ Normal code → continue | | |
| **CHECK THROTTLE POSITION SENSOR** (See page FI-123) | BAD | Throttle body |

OK → **CONTINUED ON PAGE FI-21**

---
<a id="p92"></a>
**[PDF p.92]** — EFI SYSTEM — Troubleshooting — FI-21

**CONTINUED FROM PAGE FI-20** (OK)

*(continuation of SYMPTOM — HIGH ENGINE IDLE SPEED (NO DROP))*

| Check | Branch | Trouble area / action |
|---|---|---|
| **CHECK FUEL PRESSURE** (See page FI-97) | BAD | Fuel pressure regulator — High pressure |
| **CHECK COLD START INJECTOR** (See page FI-105) | BAD | Cold start injector — Linkage |
| **CHECK INJECTORS** (See page FI-111) | BAD | Injectors — Leakage, Injection quantity |
| **CHECK EFI ELECTRONIC CIRCUIT USING VOLT/OHMMETER** (See page FI-34) | BAD | 1. Wiring connection 2. Power to ECU — (1) Fusible link(s) (2) Fuse(s) (3) EFI main relay 3. Air flow meter (w/ Air flow meter) 4. Vacuum sensor (w/o Air flow meter) 5. Water temp. sensor 6. Intake air temp. sensor 7. Injection signal circuit — (1) Injector wiring (2) ECU |

## SYMPTOM — ENGINE BACKFIRES-Lean Fuel Mixture

| Check | Branch | Trouble area / action |
|---|---|---|
| **CHECK DIAGNOSIS SYSTEM** — Check for output of diagnostic code. (See page FI-25) | Malfunction code(s) | Diagnostic code(s) — **4A-FE** (See page FI-28) |
| ↳ Normal code → continue | | |
| **CHECK FOR VACUUM LEAKS IN AIR INTAKE LINE** | BAD | 1. Oil dipstick 2. Hose connection(s) 3. PCV hose(s) 4. EGR system — EGR valve stays open |
| **CHECK IGNITION TIMING** — 1. Connect terminals TE1 and E1 of the check connector. 2. Check ignition timing. Standard: **10° BTDC @ idle** | NO | Ignition timing — Adjust — **4A-FE** (See page EM-20) |
| **CHECK IDLE SPEED (AND IDLE CO CONCENTRATION)** — Standard: **800 rpm** | NO | 1. Idle speed — Adjust — **4A-FE** (See pages EM-22, 23) 2. Idle CO concentration — Adjust |

OK → **CONTINUED ON PAGE FI-22**

---
<a id="p93"></a>
**[PDF p.93]** — EFI SYSTEM — Troubleshooting — FI-22

**CONTINUED FROM PAGE FI-21** (OK)

*(continuation of SYMPTOM — ENGINE BACKFIRES-Lean Fuel Mixture)*

| Check | Branch | Trouble area / action |
|---|---|---|
| **CHECK COLD START INJECTOR** (See page FI-105) | BAD | 1. Cold start injector 2. Start injector time switch (See page FI-137) |
| **CHECK FUEL PRESSURE** (See page FI-97) | BAD | 1. Fuel pump (See page FI-94) 2. Fuel filter 3. Fuel pressure regulator (See page FI-109) |
| **CHECK INJECTORS** (See page FI-111) | BAD | Injectors — Clogged |
| **CHECK EFI ELECTRONIC CIRCUIT USING VOLT/OHMMETER** (See page FI-34) | BAD | 1. Wiring connections 2. Power to ECU — (1) Fusible link(s) (2) Fuse(s) (3) EFI main relay 3. Air flow meter (w/ Air flow meter) 4. Vacuum sensor (w/o Air flow meter) 5. Water temp. sensor 6. Intake air temp. sensor 7. Throttle position sensor 8. Injection signal circuit — (1) Injector wiring (2) Fuel cut RPM (See page FI-153) (3) ECU 9. Oxygen sensor (w/ TWC) |
| **(w/o TWC) CHECK VARIABLE RESISTOR** (See page FI-142) | BAD | Variable resistor |

## SYMPTOM — MUFFLER EXPLOSION (AFTER FIRE)-Rich Fuel Mixture-Misfire

| Check | Branch | Trouble area / action |
|---|---|---|
| **CHECK DIAGNOSIS SYSTEM** — Check for output of diagnostic code. (See page FI-25) | Malfunction code(s) | Diagnostic code(s) — **4A-FE** (See page FI-28) |
| ↳ Normal → continue | | |
| **CHECK IGNITION TIMING** — 1. Connect terminals TE1 and E1 of the check connector. 2. Check ignition timing. Standard: **10° BTDC @ idle** | NO | Ignition timing — Adjust — **4A-FE** (See page EM-20) |

OK → **CONTINUED ON PAGE FI-23**

---
<a id="p94"></a>
**[PDF p.94]** — EFI SYSTEM — Troubleshooting — FI-23

**CONTINUED FROM PAGE FI-22** (OK)

*(continuation of SYMPTOM — MUFFLER EXPLOSION (AFTER FIRE)-Rich Fuel Mixture-Misfire)*

| Check | Branch | Trouble area / action |
|---|---|---|
| **CHECK IDLE SPEED (AND IDLE CO CONCENTRATION)** — Standard: **800 rpm** | NO | 1. Idle speed — Adjust — **4A-FE** (See pages EM-22, 23) 2. Idle CO concentration — Adjust |
| **CHECK COLD START INJECTOR** (See page FI-105) | BAD | 1. Cold start injector 2. Start injector time switch. (See page FI-137) |
| **CHECK FUEL PRESSURE** (See page FI-97) | BAD | Fuel pressure regulator |
| **CHECK THROTTLE POSITION SENSOR** — **4A-FE** (See page FI-123); **4A-GE** (See page FI-127) | BAD | Throttle body |
| **CHECK INJECTORS** (See page FI-111) | BAD | Injectors — Leakage |
| **CHECK SPARK PLUGS** — Standard: **0.8 mm (0.031 in.)** > **HINT:** Check compression pressure and valve clearance if necessary. | NO | 1. Spark plugs 2. Compression pressure — Minimum: **10.0 kg/cm² (142 psi, 981 kPa)** at **250 rpm** 3. Valve clearance (Cold) — Standard: IN **0.15 – 0.25 mm (0.006 – 0.010 in.)**, EX **0.20 – 0.30 mm (0.008 – 0.012 in.)** |
| **CHECK EFI ELECTRONIC CIRCUIT USING VOLT/OHMMETER** (See page FI-34) | BAD | 1. Throttle position sensor 2. Injection signal circuit — (1) Injector wiring (2) Fuel cut RPM (See page FI-153) (3) ECU 3. Oxygen sensor (w/ TWC) |

## SYMPTOM — ENGINE HESITATES AND/OR POOR ACCELERATION

| Check | Branch | Trouble area / action |
|---|---|---|
| **CHECK CLUTCH OR BRAKES** | BAD | 1. Clutch — Slips 2. Brakes — Drag |
| **CHECK FOR VACUUM LEAKS IN AIR INTAKE LINE** | BAD | 1. Oil dipstick 2. Hose connection(s) 3. PCV hose(s) 4. EGR system — EGR valve stays open |

OK → **CONTINUED ON PAGE FI-24**

---
<a id="p95"></a>
**[PDF p.95]** — EFI SYSTEM — Troubleshooting — FI-24

**CONTINUED FROM PAGE FI-23** (OK)

*(continuation of SYMPTOM — ENGINE HESITATES AND/OR POOR ACCELERATION)*

| Check | Branch | Trouble area / action |
|---|---|---|
| **CHECK AIR FILTER ELEMENT** | BAD | Element — Clean or replace |
| **CHECK DIAGNOSIS SYSTEM** — Check for output of diagnostic code. (See page FI-25) | Malfunction code(s) | Diagnostic code(s) — **4A-FE** (See page FI-28) |
| ↳ Normal code → continue | | |
| **CHECK IGNITION SPARK** — **4A-FE** (See page IG-6); **4A-GE** (See page IG-10) | BAD | 1. High-tension cord(s) 2. IIA or Distributor 3. Ignition coil, igniter |
| **CHECK IGNITION TIMING** — 1. Connect terminals TE1 and E1 of the check connector. 2. Check ignition timing. Standard: **10° BTDC @ idle** | NO | Ignition timing — Adjust — **4A-FE** (See page EM-20) |
| **CHECK FUEL PRESSURE** (See page FI-97) | BAD | 1. Fuel pump (See page FI-94) 2. Fuel filter 3. Fuel pressure regulator (See page FI-109) |
| **CHECK INJECTORS** (See page FI-111) | BAD | Injection condition |
| **CHECK SPARK PLUGS** — Standard: **0.8 mm (0.031 in.)** > **HINT:** Check compression pressure and valve clearance if necessary. | BAD | 1. Spark plugs 2. Compression pressure — Minimum: **10.0 kg/cm² (142 psi, 981 kPa)** at **250 rpm** 3. Valve clearance (Cold) — Standard: IN **0.15 – 0.25 mm (0.006 – 0.010 in.)**, EX **0.20 – 0.30 mm (0.008 – 0.012 in.)** |
| **CHECK INTAKE VALVE** | BAD | Intake valve — corbon [carbon] deposits |
| **CHECK EFI ELECTRONIC CIRCUIT USING VOLT/OHMMETER** (See page FI-34) | NO | 1. Wiring connections 2. Power to ECU — (1) Fusible link(s) (2) Fuse(s) (3) EFI main relay 3. Air flow meter (w/ Air flow meter) 4. Vacuum sensor (w/o Air flow meter) 5. Water temp. sensor 6. Intake air temp. sensor 7. Throttle position sensor 8. Injector signal circuit — (1) Injector wiring (2) ECU |

---
<a id="p96"></a>
**[PDF p.96]** — EFI SYSTEM — Diagnosis System — FI-25

# DIAGNOSIS SYSTEM

## DESCRIPTION

The ECU contains a built-in self-diagnosis system by which troubles with the engine signal network are detected and a "CHECK ENGINE" warning light on the instrument panel flashes.

By analyzing various signals as shown in the later table (See pages FI-28 to 31) the ECU detects system malfunctions which are related to the various operating parameter sensors or actuator. The ECU stores the failure code associated with the detected failure until the diagnosis system is cleared by removing the fuse stop 15A (AE) or EFI 15A (AT) with the ignition switch OFF.

The "CHECK ENGINE" Warning light on the instrument panel informs the driver that a malfunction has been detected.

The light goes out automatically when the malfunction has been cleared.

## CHECK ENGINE WARNING LIGHT CHECK

1. The "CHECK ENGINE" warning light will come on when the ignition switch is placed at ON and the engine is not running.
2. When the engine is started, the "CHECK ENGINE" warning light should go out.
   If the light remains on, the diagnosis system has detected a malfunction or abnormality in the system.

*(image only — see [PDF p.96]: "CHECK ENGINE" warning light symbol)*

## OUTPUT OF DIAGNOSTIC CODES

To obtain an output of diagnostic codes, proceed as follow:

1. Initial conditions
   a. Battery voltage **11 V** or more
   b. Throttle valve fully closed (throttle position sensor IDL points closed)
   c. Transmission in neutral position
   d. Accessories switched OFF
2. Turn the ignition switch to ON. Do not start the engine.
3. Using SST, connect terminals TE1 and E1 of the check connector.
   SST **09843-18020**
   LOCATION: See page FI-133

*(diagram: check connector with E1 and TE1 terminals; SST jumper)*

---
<a id="p97"></a>
**[PDF p.97]** — EFI SYSTEM — Diagnosis System — FI-26

4. Read the diagnostic code as indicated by the number of flashed of the "CHECK ENGINE" warning light.

*(image only — see [PDF p.97]: "CHECK ENGINE" warning light flashing symbol)*

Diagnostic Codes (See pages FI-28 to 31)

a. **Normal System Operation (no malfunction)**
   - The light will alternately blink ON and OFF at **0.25 second** intervals.

   *(timing diagram "No malfunction": ON/OFF square wave, **0.25 seconds** on and **0.25 seconds** off)*

b. **Malfunction Code Indication**
   - In the event of a malfunction, the light will blink every **0.5 seconds**. The first number of blinks will equal the first digit of a 2-digit diagnostic code and, after a **1.5 second** pause, the 2nd number of blinks will equal the 2nd digit. If there are two or more codes, there will be a **2.5 second** pause between each code.
   - After all the codes have been output, there will be a **4.5 second** pause and they will all be repeated as long as the terminals TE1 and E1 of the check connector are connected.

   *(timing diagram "Code No. 13 and No. 21": pulse groups separated by **1.5**, **2.5**, **4.5** (seconds))*

> **HINT:** In the event of a number of trouble codes, indication will begin from the smaller value and continue to the larger.

5. After the diagnosis check, remove SST from the check connector.
   SST **09843-18020**

*(diagram: SST jumper being removed from check connector)*

---
<a id="p98"></a>
**[PDF p.98]** — EFI SYSTEM — Diagnosis System — FI-27

## CANCELLING DIAGNOSTIC CODE

1. After repair of trouble area, the diagnostic code retained in memory by the ECU must be cancelled out by removing the fuse STOP 15A (AE) or EFI 15A (AT), located in the engine compartment relay box, for **10 seconds** or more, depending on ambient temperature (the lower the temperature, the longer the fuse must be left out) with the ignition switch OFF.

   > **HINT:**
   > - Cancellation can also be done by removing the battery negative (⊖) terminal, but in this case, other memory systems (clock, etc.) will also be cancelled out.
   > - If the diagnostic code is not cancelled out, it will be retained by the ECU and appear along with a new code in the event of future trouble.
   > - If it is necessary to work on engine components requiring removal of the battery terminal, a check must first be made to see if a diagnostic code is has been recorded.

2. After cancellation, do the road test of the vehicle the vehicle to check that a normal code is now read on the "CHECK ENGINE" warning light.
   If the same diagnostic code appears, it indicates that the trouble area has not been repaired thoroughly.

*(images: fuse locations — AE92, 95: STOP 15A; AT171: EFI 15A; AT180: EFI 15A)*

## DIAGNOSIS INDICATION

1. Including "normal", the ECU is programmed with the following diagnostic codes.
2. If two or more malfunctions are present at the same time, the lowest-numbered diagnostic code will be displayed first.
3. All detected diagnostic codes, except code No.51, will be retained in memory by the ECU from the time of detection until cancelled out.
4. Once the malfunction is corrected, the "CHECK ENGINE" warning light on the instrument panel will go out but the diagnostic code(s) will remain stored in ECU memory (except for code No.51).

---
<a id="p99"></a>
**[PDF p.99]** — EFI SYSTEM — Diagnosis System — FI-28

## DIAGNOSTIC CODES (4A-FE)

| Code No. | System | Diagnosis | Trouble area | See page |
|---|---|---|---|---|
| – | Normal | This appears when none of the other codes are identified | – | – |
| 12 | PRM Signal | No "NE" or "G" signal to ECU within 2 seconds after the engine is cranked. | • Distributor (IIA) circuit • Distributor (IIA) • Starter signal circuit • Igniter circuit • Igniter • ECU | IG-4 |
| 13 | RPM Signal | No "NE" signal to ECU When the engine speed is above **1,000 rpm**. | • Distributor (IIA) circuit • Distributor (IIA) • Igniter circuit • Igniter • ECU | IG-4 |
| 14 | Ignition Signal | No "IGF" signal to ECU 4 times in succession. | • Igniter circuit • Igniter • ECU | FI-48 / FI-62 |
| *21 | Oxygen Sensor Heater | During air-fuel ratio feedback correction, voltage output from the oxygen sensor does not exceed a set value on the lean side and the rich side continuously for a centain [certain] period. | • Oxygen sensor circuit • Oxygen sensor | FI-50 / FI-64 |
| *21 (cont'd) | Oxygen Sensor Heater | Open or short circuit in oxygen sensor heater (HT). | • Oxygen sensor heater circuit • Oxygen sensor heater • ECU | FI-50 / FI-64 |
| 22 | Water Temp. Sensor | Open or short circuit in water temp. sensor signal (THW). | • Water temp. sensor circuit • Water temp. sensor • ECU | FI-46 / FI-60 |
| 24 | Intake air Temp. Sensor Signal | Open or short circuit in intake air temp. sensor signal (THA). | • Intake air temp. sensor circuit • Intake air temp. sensor • ECU | FI-45 / FI-59 |
| *25 | Air-fuel Ratio Lean Malfunction | When air-fuel ratio feedback correction value cotinues [continues] at the upper (lean) limit for a certain period of time. | • Oxygen sensor circuit • Oxygen sensor • ECU | FI-50 / FI-64 |
| *26 | Air-fuel Ratio Rich Malfunction | (same as *25 — shares the "When air-fuel ratio feedback correction value continues at the upper (lean) limit for a certain period of time" diagnosis) | • Oxygen sensor circuit • Oxygen sensor • ECU | FI-50 / FI-64 |

**\*: w/ EGR System only**

> **HINT:** The "Number of blinks / CHECK ENGINE" column of this table is an image showing the flash pattern for each code and is not transcribed numerically.

---
<a id="p100"></a>
**[PDF p.100]** — EFI SYSTEM — Diagnosis System — FI-29

## DIAGNOSTIC CODES (4A-FE) (Cont'd)

| Code No. | System | Diagnosis | Trouble area | See page |
|---|---|---|---|---|
| 31 | Vacuum Sensor Signal | Open or short circuit intake manifold pressure signal (PIM). | • Vacuum sensor circuit • Vacuum sensor • ECU | FI-44 / FI-58 |
| 41 | Throttle Position Sensor Signal | The "IDL" and "PSW" signals are output simultaneously for several seconds. | • Throttle position sensor circuit • Throttle position sensor • ECU | FI-41 / FI-55 |
| 42 | Vehicle Speed Sensor Signal | No "SPD" signal for **8 seconds** when engine speed is between **2,600 rpm** and **4,500 rpm** and coolant temp. is below **80°C (176°F)** except when racing the engine. | • Vehicle speed sensor circuit • Vehicle speed sensor • ECU | – |
| 43 | Starter Signal | No "STA" signal to ECU until engine speed reaches **800 rpm** with vehicle not moving. | • IG switch circuit • IG switch, main relay circuit • ECU | FI-47 / FI-61 |
| 51 | Switch Condition Signal | No "IDL" signal, "NSW" signal or "A/C" signal to ECU, with the check terminals E1 and TE1 connected. | • A/C switch circuit • A/C switch • A/C amplifier • Neutral start switch circuit • Neutral start switch • Accelerator pedal and cable • Throttle position sensor circuit • Throttle position sensor • ECU | FI-49 / FI-63 |

## DIAGNOSTIC CODES (4A-GE)

| Code No. | System | Diagnosis | Trouble area | See page |
|---|---|---|---|---|
| – | Normal | This appears when none of the other codes are identified. | – | – |
| 12 | PRM Signal | **(w/o Air Flow Meter)** No "NE" or "G" signal to ECU within 2 seconds after engine has been cranked. **(w/ Air Flow Meter)** • No "NE" signal to ECU within 2 seconds after the engine is cranked. • Ne "G" signal to ECU 4 times in succession when engine speed is between **500 rpm** and **4,000 rpm**. | • Distributor circuit • Distributor • Starter signal circuit • ECU | IG-5 |

> **Scan gap:** pages FI-30 to FI-31 are missing from this scan.

---
<a id="p101"></a>
**[PDF p.101]** — EFI SYSTEM — Diagnosis System — FI-32

## INSPECTION OF DIAGNOSIS CIRCUIT

*(Wiring schematics — two variants. Values as labeled.)*

**AE variant:**
- FL MAIN **0.85R** — Fuse EFI **15A** — EFI Main Relay → ECU **+B**, **+B1**
- FL AM2 **30A**; FL ALT **100A**; FL AM1 **40A**
- Ignition Switch (AM2/AM1 → IG2/IG1) — Fuse IGN **10A** — Fuse GAUGE **7.5A** → "CHECK ENGINE" Warning Light → ECU **W**
- Fuse STOP **15A** → ECU **BATT**
- Battery
- Check Connector (terminals TE1, E1) → ECU **T**, **E1**

**AT variant:**
- Fuse EFI **15A** → ECU **BATT**
- FL MAIN **2.0L**: (AT171) FL ALT **80A**, FL AM1 **60A**; (AT180) FL ALT **100A**, FL AM1 **40A**
- FL AM2 **30A**
- Ignition Switch (AM2/AM1 → IG2/IG1) — Fuse IGN **7.5A** — EFI Main Relay → ECU **+B**, **+B1**
- Fuse GAUGE **7.5A (AT171)** / **15A (AT180)** → "CHECK ENGINE" Warning Light → ECU **W**
- Battery
- Check Connector (terminals TE1, E1) → ECU **T**, **E1**

---
<a id="p102"></a>
**[PDF p.102]** — EFI SYSTEM — Diagnosis System — FI-33

*Diagnostic flowchart for the diagnosis-circuit inspection.*

**1.**

| Step | Question | Result | Next / action |
|---|---|---|---|
| 1a | Does "CHECK ENGINE" warning light come on when ignition switch is at ON? | YES | System Normal. |
| | | NO | → step 1b |
| 1b | Does "CHECK ENGINE" warning light come on when ECU terminal W is grounded to the body? | YES | Check wiring between ECU terminal E1 and body ground. → OK: Try another ECU. → BAD: Repair or replace. |
| | | NO | Check bulb, fuse and wiring between ECU and ignition switch. → BAD: Repair or replace. |

**2.**

| Step | Question | Result | Next / action |
|---|---|---|---|
| 2a | Does "CHECK ENGINE" warning light go off when the engine is started? | YES | System Normal. |
| | | NO | → step 2b |
| 2b | Check wiring between ECU and "CHECK ENGINE" warning light. | BAD | Repair. |
| | | NO (OK) | → step 2c |
| 2c | Is there diagnostic code output when check connector terminals TE1 and E1 connected? | NO | Check wiring between ECU terminal TE1 and check connector terminal TE1, and ECU terminal E1 and check connector terminal E1. → OK: Try another ECU. |
| | | YES | → step 2d |
| 2d | Does "CHECK ENGINE" warning light go out after repair according to malfunction code? | NO | Further repair required. |
| | | YES | System OK → Cancel out diagnostic code. |

---
<a id="p103"></a>
**[PDF p.103]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-34

# TROUBLESHOOTING WITH VOLT/OHMMETER

> **HINT:** The following troubleshooting procedures are designed for inspection of each separate system, therefore the procedure may vary somewhat. However, troubleshooting should be performed refering to the inspection methods described in this manual.
> Before beginning inspection, it is best to first make a simple check of the fuses, fusible links and the condition of the connectors.

The following troubleshooting procedures are based on the supposition that the trouble lies in either a short or open circuit in a component outside the computer or short circuit within the computer.

If engine trouble occurs even through proper operating voltage is detected in the computer connector, then it can be assumed that the ECU is faulty and should be replaced.

## LOCATION OF FUSES AND FUSIBLE LINKS

**AE** *(diagram of vehicle with fuse/fusible-link locations; LHD variant shown at right)*

Labeled fuses and fusible links:
- Fuse IGN **10A**
- Fuse GAUGE **7.5A**
- Fuse STOP **15A**
- Fuse EFI **15A**
- FL AM2 **30A**
- FL AM1 **40A**
- FL ALT **100A**
---
<a id="p104"></a>
**[PDF p.104]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-35

## LOCATION OF FUSES AND FUSIBLE LINKS (Cont'd)

**AT171**

*(image only — see [PDF p.104])* Vehicle front view with two fuse/relay block diagrams:
- Instrument-panel fuse block: **Fuse IGN 7.5A**, **Fuse GAUGE 7.5A**
- Engine-compartment relay block: **FL ALT 80A**, **FL AM2 30A**, **FL AM1 60A**, **Fuse EFI 15A**

**AT180**

*(image only — see [PDF p.104])* Engine-compartment and instrument-panel blocks:
- Engine-compartment relay block: **FL ALT 100A**, **FL AM1 40A**, **FL AM2 30A**, **Fuse EFI 15A**
- Instrument-panel fuse block (RHD / LHD): **Fuse IGN 7.5A**, **Fuse GAUGE 15A**

---
<a id="p105"></a>
**[PDF p.105]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-36

## EFI SYSTEM CHECK PROCEDURE

### PREPARATION

a. Disconnect the connectors from the ECU.
b. Remove the locks shown in the illustration so that the tester probe(s) can easily come in.

> **NOTICE:** Pay attention to sections "A" and "B" in the illustration which can be easily broken.

c. Reconnect the connectors to the ECU.

> **HINT:**
> - Perform all voltage measurements with the connectors connected.
> - Verify that the battery voltage is **11 V** or above when the ignition switch is ON.

Using a voltmeter with high-impedance (**10 kΩ/V** minimum), measure the voltage at each terminal of the wiring connectors.

*(images only — see [PDF p.105]: ECU connector showing locks "A" and "B"; voltmeter connected to ECU terminals E1, +B1, +B)*

---
<a id="p106"></a>
**[PDF p.106]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-37

## Terminals of ECU (4A-FE 2WD)

| Symbol | Terminal Name | Symbol | Terminal Name |
|---|---|---|---|
| E01 | POWER GROUND | PSW | THROTTLE POSITION SENSOR |
| E02 | POWER GROUND | THW | WATER TEMP. SENSOR |
| No.10 | INJECTOR | E2 | SENSOR GROUND |
| No.20 | INJECTOR | *³ NSW | NEUTRAL START SWITCH |
| STA | STARTER MAGNETIC SWITCH | *¹ HT | OXYGEN SENSOR |
| E1 | ECU GROUND | EGR | VSV (EGR) |
| *¹ OX | OXYGEN SENSOR | V-ISC | VSV (ISC VALVE) |
| *² VAF | VARIABLE RESISTOR | T | CHECK CONNECTOR |
| G ⊖ | DISTRIBUTOR | VF | CHECK CONNECTOR |
| E21 | SENSOR GROUND | *¹ ACT | A/C AMPLIFIER |
| G1 | DISTRIBUTOR | SPD | SPEED SENSOR |
| NE | DISTRIBUTOR | FC | CIRCUIT OPENING RELAY |
| IGF | IGNITER | A/C | A/C COMPRESSOR |
| IGT | IGNITER | *¹ R/P | FUEL CONTROL SWITCH |
| IDL | THROTTLE POSITION SENSOR | BATT | BATTERY |
| THA | INTAKE AIR TEMP. SENSOR | W | CHECK ENGINE WARNING LIGHT |
| VCC | VACUUM SENSOR | +B1 | EFI MAIN RELAY |
| PIM | VACUUM SENSOR | +B | EFI MAIN RELAY |

*¹ : w/ EGR System, *² : w/o EGR System, *³ : A/T

**ECU Terminals** *(connector pin-layout diagram)*

Top row: E01 | No.10 | STA | OX/VAF | G⊖ | G1 | IGF | IGT | THA | PIM | THW | NSW | EGR | ‖ | T | ACT | – | – | FC | R/P | BATT | +B1

Bottom row: E02 | No.20 | E1 | – | E21 | NE | – | IDL | VCC | PSW | E2 | HT | V-ISC | ‖ | VF | – | – | SPD | A/C | – | W | +B

---
<a id="p107"></a>
**[PDF p.107]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-38

## Voltage at ECU wiring connectors (4A-FE 2WD)

| No. | Terminals | STD voltage (V) | Condition | | See page |
|---|---|---|---|---|---|
| 1 | +B / +B1 – E1 | 10 – 14 | Ignition SW ON | | FI-39 |
| 2 | BATT – E1 | 10 – 14 | — | | FI-40 |
| 3 | IDL – E2 | 4.5 – 5.5 | Ignition SW ON | Throttle valve open | FI-41 |
| 3 | PSW – E2 | 4.5 – 5.5 | Ignition SW ON | Throttle valve fully closed | FI-41 |
| 4 | No.10 – E01 / No.20 – E02 | 10 – 14 | Ignition SW ON | | FI-42 |
| 5 | W – E1 | 10 – 14 | No trouble ("CHECK ENGINE" warning light off) and engine running | | FI-43 |
| 6 | PIM – E2 | 3.3 – 3.9 | Ignition SW ON | | FI-44 |
| 6 | VCC – E2 | 4.5 – 5.5 | Ignition SW ON | | FI-44 |
| 7 | THA – E2 | 2.0 – 2.5 | Ignition SW ON | Intake air temp. 20°C (68°F) | FI-45 |
| 8 | THW – E2 | 0.4 – 0.7 | Ignition SW ON | Coolant temp. 80°C (176°F) | FI-46 |
| 9 | STA – E1 | 6 – 14 | Cranking | | FI-47 |
| 10 | IGT – E1 | 0.7 – 1.0 | Idling | | FI-48 |
| 11 | A/C – E1 | 5 – 14 | Air conditioning ON | | FI-49 |

**ECU Terminals** *(connector pin-layout diagram, same as FI-37)*

Top row: E01 | No.10 | STA | OX/VAF | G⊖ | G1 | IGF | IGT | THA | PIM | THW | NSW | EGR | ‖ | T | ACT | – | – | FC | R/P | BATT | +B1

Bottom row: E02 | No.20 | E1 | – | E21 | NE | – | IDL | VCC | PSW | E2 | HT | V-ISC | ‖ | VF | – | – | SPD | A/C | – | W | +B

---
<a id="p108"></a>
**[PDF p.108]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-39

| No. | Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|---|
| 1 | +B / +B1 – E1 | No voltage | IG SW ON | **10 – 14 V** |

*(circuit diagram — see [PDF p.108])* Battery → **FL MAIN 2.0L (AT)** / **FL MAIN 0.85R (AE)** and **FL AM2 30A** → Ignition Switch (AM2 → IG2) → **Fuse IGN 7.5A (AE) / 10A (AT)**; also **Fuse EFI 15A** → EFI Main Relay → ECU terminals +B and +B1; ECU E1 to ground.

**Diagnostic flowchart:**

| Step | Check | Result → Next |
|---|---|---|
| ① | There is no voltage between ECU terminals +B (+B1) and E1. (IG SW ON) | → ② |
| ② | Check that there is voltage between ECU terminal +B (+B1) and body ground. (IG SW ON) | OK → ③ ; NO → check fuses/fusible links & ignition switch |
| ③ | Check wiring between ECU terminal E1 and body ground. | OK → Try another ECU ; BAD → Repair or replace |
| — | Check fuses, fusible links and ignition switch. | BAD → Repair or replace ; OK → next |
| — | Check EFI main relay. (See page FI-134) | BAD → Replace ; OK → next |
| — | Check wiring between EFI main relay and battery. | BAD → Repair or replace |

*(inset images: ① voltmeter at ECU +B/+B1/E1; ② voltmeter at ECU +B1/+B and body ground; ③ ohmmeter at ECU E1)*

---
<a id="p109"></a>
**[PDF p.109]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-40

| No. | Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|---|
| 2 | BATT – E1 | No voltage | — | **10 – 14 V** |

*(circuit diagram — see [PDF p.109])* Battery → **FL ALT 100A (AE) / FL MAIN 2.0 L (AT)** → **Fuse STOP 15A (AE) / EFI 15A (AT)** → ECU terminal BATT; ECU E1 to ground.

**Diagnostic flowchart:**

| Step | Check | Result → Next |
|---|---|---|
| ① | There is no voltage between ECU terminals BATT and E1. | → ② |
| ② | Check that there is voltage between ECU terminal BATT and body ground. | OK → ③ ; NO → check fuse & fusible link |
| ③ | Check wiring between ECU terminal E1 and body ground. | OK → Try another ECU ; BAD → Repair or replace |
| — | Check fuse and fusible link. | BAD → Replace ; OK → next |
| — | Check wiring between ECU terminal and battery. | BAD → Repair or replace |

*(inset images: ① voltmeter at ECU BATT/E1; ② voltmeter at ECU BATT and body ground; ③ ohmmeter at ECU E1)*

---
<a id="p110"></a>
**[PDF p.110]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-41

| No. | Terminals | Trouble | Condition | | STD voltage |
|---|---|---|---|---|---|
| 3 | IDL – E2 | No voltage | IG SW ON | Throttle valve open | **4.5 – 5.5 V** |
| 3 | PSW – E2 | No voltage | IG SW ON | Throttle valve fully closed | **4.5 – 5.5 V** |

*(circuit diagram — see [PDF p.110])* Throttle Position Sensor terminals IDL, E2, PSW → ECU terminals +B (+B1), IDL, E2, PSW; ECU E1 to ground.

**Diagnostic flowchart:**

| Step | Check | Result → Next |
|---|---|---|
| ① | There is no voltage between ECU terminals IDL and E2. (IG SW ON) (Throttle valve open) | → ② |
| ② | Check that there is voltage between ECU terminal +B (+B1) and body ground. (IG SW ON) | OK → check wiring between ECU terminal E1 and body ground ; NO → Refer to +B – E1 trouble section (No.1) (See page FI-39) |
| — (E1 wiring) | Check wiring between ECU terminal E1 and body ground. | OK → Try another ECU ; BAD → Repair or replace |
| — (No.1 ref) | Refer to +B – E1 trouble section (No.1) (See page FI-39) | BAD → Repair or replace ; OK → ③ |
| ③ | Check throttle position sensor. (See page FI-123) | BAD → Repair or replace throttle position sensor ; OK → Check wiring between ECU and throttle position sensor |
| — | Check wiring between ECU and throttle position sensor. | OK → Try another ECU ; BAD → Repair or replace |

*(inset images: ① voltmeter at ECU IDL/E2/PSW; ② voltmeter at ECU +B1/+B; ③ ohmmeter at throttle position sensor PSW/E2/IDL)*

---
<a id="p111"></a>
**[PDF p.111]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-42

| No. | Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|---|
| 4 | No.10 – E01 / No.20 – E02 | No voltage | IG SW ON | **10 – 14 V** |

*(circuit diagram — see [PDF p.111])* Battery → **FL MAIN 2.0L (AT/AE)** and **FL AM2 30A** → Ignition Switch (AM2 → IG2) → four Injectors → ECU terminals No.10, No.20, E01, E02.

**Diagnostic flowchart:**

| Step | Check | Result → Next |
|---|---|---|
| ① | There is no voltage between ECU terminals No.10 and/or No.20 and E01 and/or E02. (IG SW ON) | → ② |
| ② | Check that there is voltage between ECU terminal No.10 and/or No.20 and body ground. | OK → ③ (E01/E02 wiring) ; NO → check fuse, fusible link, ignition switch |
| — (E01/E02) | Check wiring between ECU terminal E01 and/or E02 and body ground. | OK → Try another ECU ; BAD → Repair or replace |
| — | Check fuse, fusible link, ignition switch. | BAD → Repair or replace ; OK → next |
| ③ | Check resistance of magnetic coil in each injector. **STD resistance: Approx. 13.8 Ω** | OK → Check wiring between ECU terminal No.10 and/or No.20 and battery ; BAD → Replace injector |
| — | Check wiring between ECU terminal No.10 and/or No.20 and battery. | BAD → Repair or replace |

*(inset images: ① voltmeter at ECU No.10/No.20; ② voltmeter at ECU No.10/No.20 and E02/E01; ③ ohmmeter at injector)*

---
<a id="p112"></a>
**[PDF p.112]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-43

| No. | Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|---|
| 5 | W – E1 | No voltage | No trouble ("CHECK ENGINE" warning light off) and engine running. | **10 – 14 V** |

*(circuit diagram — see [PDF p.112])* From Ignition Switch (IG1) → **Fuse GAUGE 7.5A (AE, AT171) / 15A (AT180)** → "CHECK ENGINE" Warning Light (in Combination Meter) → ECU terminal W; ECU E1 to ground.

**Diagnostic flowchart:**

| Step | Check | Result → Next |
|---|---|---|
| ① | There is no voltage between ECU terminals W and E1. (Idling) | → ② |
| ② | Check that there is voltage between ECU terminal W and body ground. | OK → ③ ; NO → check GAUGE fuse & "CHECK ENGINE" warning light |
| ③ | Check wiring between ECU terminal E1 and body ground. | OK → Try another ECU ; BAD → Repair or replace |
| — | Check GAUGE fuse and "CHECK ENGINE" warning light. | OK → check wiring between ECU terminal W and fuse ; BAD → Repair or replace (if fuse blows again → check wiring between ECU terminal W and fuse) |
| — | Check wiring between ECU terminal W and fuse. | BAD → Repair or replace |

*(inset images: ① voltmeter at ECU E1/W; ② voltmeter at ECU W; ③ ohmmeter at ECU E1)*

---
<a id="p113"></a>
**[PDF p.113]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-44

| No. | Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|---|
| 6 | PIM – E2 | No voltage | IG SW ON | **3.3 – 3.9 V** |
| 6 | VCC – E2 | No voltage | IG SW ON | **4.5 – 5.5 V** |

*(circuit diagram — see [PDF p.113])* Vacuum Sensor (Manifold Absolute Pressure Sensor) terminals E2, PIM, VCC → ECU terminals E2, PIM, VCC; ECU E1 to ground.

**Diagnostic flowchart:**

| Step | Check | Result → Next |
|---|---|---|
| ① | There is no voltage between ECU terminals PIM or VCC and E2. (IG SW ON) | → ② |
| ② | Check that there is voltage between ECU terminal +B (+B1) and body ground. (IG SW ON) | NO (left) → ③ (E1 wiring) ; NO (right) → Refer to +B – E1 trouble section (No.1) (See page FI-39) |
| ③ | Check wiring between ECU terminal E1 and body ground. | OK → Check vacuum sensor (See page FI-140) ; BAD → Repair or replace |
| — | Check vacuum sensor. (See page FI-140) | BAD → Replace vacuum sensor ; OK → Check wiring between ECU and vacuum sensor |
| — | Check wiring between ECU and vacuum sensor. | OK → Try another ECU ; BAD → Repair or replace |

*(inset images: ① voltmeter at ECU VCC/PIM/E2; ② voltmeter at ECU +B1/+B; ③ ohmmeter at ECU E1)*

---
<a id="p114"></a>
**[PDF p.114]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-45

| No. | Terminals | Trouble | Condition | | STD voltage |
|---|---|---|---|---|---|
| 7 | THA – E2 | No voltage | IG SW ON | Intake air temperature 20°C (68°F) | **2.0 – 2.5 V** |

*(circuit diagram — see [PDF p.114])* Intake Air Temp. Sensor terminals THA, E2 → ECU terminals +B (+B1), THA, E2; ECU E1 to ground.

**Diagnostic flowchart:**

| Step | Check | Result → Next |
|---|---|---|
| ① | There is no voltage between ECU terminals THA and E2. (IG SW ON) | → ② |
| ② | Check that there is voltage between ECU terminal +B (+B1) and body ground. (IG SW ON) | OK → Check wiring between ECU terminal E1 and body ground ; NO → Refer to +B – E1 trouble section (No.1) (See page FI-39) |
| — (E1 wiring) | Check wiring between ECU terminal E1 and body ground. | OK → ③ ; BAD → Repair or replace |
| ③ | Check intake air temp. sensor. (See page FI-139) | BAD → Replace intake air temp. sensor ; OK → Check wiring between ECU and intake air temp. sensor |
| — | Check wiring between ECU and intake air temp. sensor. | OK → Try another ECU ; BAD → Repair or replace wiring |

*(inset images: ① voltmeter at ECU THA/E2; ② voltmeter at ECU +B1/+B; ③ ohmmeter at intake air temp. sensor)*

---
<a id="p115"></a>
**[PDF p.115]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-46

| No. | Terminals | Trouble | Condition | | STD voltage |
|---|---|---|---|---|---|
| 8 | THW – E2 | No voltage | IG SW ON | Coolant temperature 80°C (176°F) | **0.4 – 0.7 V** |

*(circuit diagram — see [PDF p.115])* Water Temp. Sensor terminals THW, E2 → ECU terminals +B (+B1), THW, E2; ECU E1 to ground.

**Diagnostic flowchart:**

| Step | Check | Result → Next |
|---|---|---|
| ① | There is no voltage between ECU terminals THW and E2. (IG SW ON) | → ② |
| ② | Check that there is voltage between ECU terminal +B (+B1) and body ground. (IG SW ON) | OK → Check wiring between ECU terminal E1 and body ground ; NO → Refer to +B – E1 trouble section (No.1) (See page FI-39) |
| — (E1 wiring) | Check wiring between ECU terminal E1 and body ground. | OK → ③ ; BAD → Repair or replace |
| ③ | Check water temp. sensor. (See page FI-138) | BAD → Replace water temp. sensor ; OK → Check wiring between ECU and water temp. sensor |
| — | Check wiring between ECU and water temp. sensor. | OK → Try another ECU ; BAD → Repair or replace |

*(inset images: ① voltmeter at ECU THW/E2; ② voltmeter at ECU +B1/+B; ③ ohmmeter at water temp. sensor)*

---
<a id="p116"></a>
**[PDF p.116]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-47

| No. | Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|---|
| 9 | STA – E1 | No voltage | Cranking | **6 – 14 V** |

*(circuit diagram — see [PDF p.116])* Battery → **FL MAIN 2.0L (AT/AE)**, **FL ALT 100A (AE, AT180) / 80A (AT171)**, **FL AM1 40A (AE, AT180) / 60A (AT171)** → Ignition Switch (AM1 → ST1) → Neutral Start Switch (A/T) / direct (M/T) → ECU terminal STA and Starter STA (Terminal 50); also To Circuit Opening Relay; ECU E1 to ground.

**Diagnostic flowchart:**

| Step | Check | Result → Next |
|---|---|---|
| ① | There is no voltage between ECU terminals STA and E1. (IG SW START) | → Check starter operation |
| — | Check starter operation. | OK → Check wiring between ECU terminal STA and ignition switch terminal ST1 ; BAD → ② |
| — | Check wiring between ECU terminal STA and ignition switch terminal ST1. | OK → next ; BAD → Replace replace. <!-- NEEDS REVIEW: printed "Replace replace." likely "Repair or replace." --> |
| ② | Check wiring between ECU terminal E1 and body ground. | OK → Try another ECU ; BAD → Repair or replace |
| — | Check fusible link, battery, wiring and ignition switch. | BAD → Repair or replace ; OK → ③ |
| ③ | Check that there is voltage at STA (50) terminal of starter. (IG SW START) **STD voltage: 6 – 14 V** | OK → Check starter ; NO → Check wiring between ignition switch terminal ST1 and starter terminal STA (50) |

*(inset images: ① voltmeter at ECU STA/E1; ② ohmmeter at ECU E1; ③ voltmeter at Starter STA (Terminal 50))*

---
<a id="p117"></a>
**[PDF p.117]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-48

| No. | Terminals | Trouble | Condition | STD voltage |
|---|---|---|---|---|
| 10 | IGT – E1 | No voltage | Idling | **0.7 – 1.0 V** |

*(circuit diagram — see [PDF p.117])* Battery → **FL MAIN 2.0L (AT/AE)** and **FL AM2 30A** → Ignition Switch (AM2 → IG2) → IIA (igniter/distributor) → ECU terminals IGT and IGF; ECU E1 to ground.

**Diagnostic flowchart:**

| Step | Check | Result → Next |
|---|---|---|
| ① | There is no voltage between ECU terminals IGT and E1. (Idling) | → ② |
| ② | Check that there is voltage between ECU terminal IGT and body ground. (Idling) | OK → ③ ; NO → check fusible links & ignition switch |
| ③ | Check wiring between ECU terminal E1 and body ground. | OK → Try another ECU ; BAD → Repair or replace |
| — | Check fusible links and ignition switch. | BAD → Repair or replace ; OK → next |
| — | Check IIA. (See page IG-8) | BAD → Repair or replace ; OK → next |
| — | Check wiring between ECU and battery. | BAD → Repair or replace ; OK → next |
| — | Check igniter. (See page IG-6) | BAD → Repair or replace |

*(inset images: ① voltmeter at ECU IGT/E1; ② voltmeter at ECU IGT; ③ ohmmeter at ECU E1)*
---
<a id="p118"></a>
**[PDF p.118]** — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter — FI-49

**Troubleshooting table (row 11)**

| No. | Terminals | Trouble | Condition | STD voltage |
|-----|-----------|---------|-----------|-------------|
| 11 | A/C – E1 | No voltage | Air conditioning ON | **5 – 14 V** |

*(Circuit diagram — image only, see [PDF p.118]: To A/C Amplifier and A/C Compressor wired to ECU terminals A/C and E1.)*

**Diagnostic flowchart** — ① There is no voltage between ECU terminals A/C and E1. (Air conditioning ON)

| Step | Check | Result | Next |
|------|-------|--------|------|
| ② | Check that there is voltage between ECU terminal A/C and body ground. | OK | Go to ③ |
| ② | (as above) | NO | Go to "Check compressor running." |
| ③ | Check wiring between ECU terminal E1 and body ground. | OK | Try another ECU. |
| ③ | (as above) | BAD | Repair or replace. |
| — | Check compressor running. | OK | Check wiring between ECU terminal A/C and Amplifier. → BAD → Repair or replace. |
| — | Check compressor running. | NO | Check that there is voltage between amplifier terminal and body ground. |
| — | Check that there is voltage between amplifier terminal and body ground. | BAD | Repair or replace. |
| — | (as above) | OK | Check wiring between amplifier and ECU or compressor. → BAD → Repair or replace. |

*(Left-column meter hookup illustrations ①②③ — image only: ① Voltmeter across ECU terminals E1 and A/C; ② Voltmeter from ECU terminal A/C; ③ Ohmmeter from ECU terminal E1.)*

---
<a id="p119"></a>
**[PDF p.119]** — FI-50 — EFI SYSTEM — Troubleshooting with Volt/Ohmmeter

*(Circuit diagram — image only, see [PDF p.119]: From EFI Main Relay, Oxygen Sensor, Oxygen Sensor Heater (w/ EGR system), Check Connector terminals VF1/TE1/E1 → ECU terminals VF, T, OX, HT, E1.)*

**Diagnostic flowchart** — ① There is no voltage between ECU terminals VF and E1.

| Step | Check | Result | Next |
|------|-------|--------|------|
| — | Check that there is voltage between ECU terminal VF and body ground. | OK | Check wiring between ECU terminal E1 and body ground. |
| — | (as above) | NO | Go to "Is air leaking into air intake system?" |
| — | Check wiring between ECU terminal E1 and body ground. | OK | Try another ECU. |
| — | (as above) | BAD | Repair or replace. |
| — | Is air leaking into air intake system? | BAD | Repair air leak. |
| — | (as above) | OK | Check spark plugs. |
| — | Check spark plugs. | BAD | Repair or replace. |
| — | (as above) | OK | Check distributor and ignition system. |
| — | Check distributor and ignition system. | BAD | Repair or replace. |
| — | (as above) | OK | Check fuel pressure. |
| — | Check fuel pressure. | BAD | Repair or replace. |
| — | (as above) | OK | Check injector. |
| — | Check injector. | BAD | Repair or replace. |
| — | (as above) | OK | Check cold start injector.* |
| — | Check cold start injector.* | BAD | Repair or replace. |
| — | (as above) | OK | Check vacuum sensor. |
| — | Check vacuum sensor. | BAD | Repair or replace. |
| — | (as above) | OK | ② Check operation of oxygen sensor. |
| ② | Check operation of oxygen sensor. | OK | System normal. |
| ② | (as above) | BAD | Check wiring between oxygen sensor and ECU connector. |
| — | Check wiring between oxygen sensor and ECU connector. | BAD | Repair wiring. |
| — | (as above) | OK | Replace oxygen sensor. |

> *Rich malfunction only

*(Left-column illustrations ①② — image only: ① Voltmeter across ECU terminals E1 and VF; ② SST at Check Connector terminals E1/TE1, Voltmeter across E1/TE1/VF1.)*

---
<a id="p120"></a>
**[PDF p.120]** — FI-94 — EFI SYSTEM — Fuel System

> **Scan gap:** pages FI-51 to FI-93 are missing from this scan.

## FUEL SYSTEM
### Fuel Pump

*(Cutaway diagram — image only, see [PDF p.120]: Fuel pump internals — OUTLET, Check Valve, Relief Valve, Bearing, Armature, Magnet, Bearing, Impeller, INLET; and impeller/casing turbine view — OUTLET, INLET, Casing, Impeller.)*

*(Fuel pump circuit diagram — image only, see [PDF p.120]. Key labelled values:)*

| Component | Rating |
|-----------|--------|
| Fuse EFI | **15A** |
| Fuse IGN | **10A (AE)**, **7.5A (AT)** |
| FL MAIN | **0.85R** |
| FL AM2 | **30A** |
| FL AM1 | **40A (AE, AT180)**, **60A (AT171)** |
| FL ALT | **100A (AE, AT180)**, **80A (AT171)** |
| FL MAIN | **2.0L** |

Circuit elements shown: EFI Main Relay, Ignition Switch (AM2/IG2, AM1/ST1), Battery, Circuit Opening Relay (+B, FP, STA, E1, FC), Check Connector (+B, FP), Fuel Pump, Fuel Pump Switch (Air Flow Meter), Neutral Start Switch, To ECU (w/o Air Flow Meter).

---
<a id="p121"></a>
**[PDF p.121]** — FI-95 — EFI SYSTEM — Fuel System

## ON-VEHICLE INSPECTION

1. **CHECK FUEL PUMP OPERATION**
   a. Turn the ignition to ON.
      > **HINT:** Do not start the engine.
   b. Using SST, connect terminals +B and FP of the check connector.
      SST **09843-18020**
      LOCATION: See page FI-133
   c. Check that there is pressure in the hose from the fuel filter.
      > **HINT:** At this time, you will hear fuel return noise from the pressure regulator.
   d. Remove SST from the check connector.
      SST **09843-18020**
   e. Turn the ignition switch to OFF.

   If there is no pressure, check the following parts:
   - Fusible links
   - Fuses
   - EFI main relay
   - Circuit opening relay
   - Fuel pump
   - ECU
   - Wiring connections

2. **INSPECT FUEL PRESSURE**
   a. Check that the battery voltage is above **12 V**.
   b. Disconnect the cable from the negative ( – ) terminal of the battery.
   c. Disconnect the wiring connector from the cold start injector.

*(Left-column illustrations — image only: Check Connector with SST across FP/+B; fuel filter hose check; SST at connector; 4A-FE Cold Start Injector Connector location views.)*

---
<a id="p122"></a>
**[PDF p.122]** — FI-96 — EFI SYSTEM — Fuel System

(continued — INSPECT FUEL PRESSURE)

   d. Put a suitable container or shop towel under cold start injector pipe.
   e. Slowly loosen the union bolts of the cold start injector pipe and remove the bolts, cold start injector pipe and four gaskets.
   f. Drain the fuel from the delivery pipe.
   g. Install SST (pressure gauge) to the delivery pipe with new two gasket and union bolt.
      SST **09268-45012**
      **Torque: 4A-FE — 180 kg-cm (13 ft-lb, 18 N·m)**
   h. Wipe off any splattered gasoline.
   i. Reconnect the battery negative ( – ) cable.
   j. Using SST, connect terminals +B and FP of the check connector.
      SST **09843-18020**
      LOCATION: See page FI-133

*(Left-column illustrations — image only: SST pressure-gauge installation on delivery pipe, shown for **4A-FE** and **4A-GE**; Check Connector with SST across FP/+B.)*

---
<a id="p123"></a>
**[PDF p.123]** — FI-97 — EFI SYSTEM — Fuel System

(continued — INSPECT FUEL PRESSURE)

   k. Turn the ignition switch ON.
   l. Measure the fuel pressure.
      **Fuel pressure: 2.7 – 3.1 kg/cm² (38 – 44 psi, 265 – 304 kPa)**

   If pressure is high, replace the fuel pressure regulator.

   If pressure is low, check the following parts:
   - Fuel hoses and connection
   - Fuel pump
   - Fuel filter
   - Fuel pressure regulator

   m. Remove SST from the check connector.
      SST **09843-18020**
   n. Start the engine.
   o. Disconnect the vacuum sensing hose from the fuel pressure regulator, and plug the hose end.
   p. Measure the fuel pressure at idling.
      **Fuel pressure: 2.7 – 3.1 kg/cm² (38 – 44 psi, 265 – 304 kPa)**

<!-- NEEDS REVIEW: OCR text rendered kPa low value as "266"; page image confirms 265. -->

*(Left-column illustrations — image only: SST pressure gauge for **4A-FE** and **4A-GE**; SST at check connector.)*

---
<a id="p124"></a>
**[PDF p.124]** — FI-98 — EFI SYSTEM — Fuel System

(continued — INSPECT FUEL PRESSURE)

   q. Reconnect the vacuum sensing hose to the fuel pressure regulator.
   r. Measure the fuel pressure at idling.
      **Fuel pressure: 2.1 – 2.6 kg/cm² (30 – 37 psi, 206 – 255 kPa)**

   If pressure is not as specified, check the vacuum sensing hose and fuel pressure regulator.

   s. Stop the engine. Check that the fuel pressure remains **1.5 kg/cm² (21 psi, 147 kPa)** or more for 5 minutes after the engine is turned off.

   If pressure is not as specified, check the fuel pump, pressure regulator and/or injector.

   t. After checking fuel pressure, disconnect the battery negative ( – ) cable and carefully remove the SST to prevent gasoline from splashing.
      SST **09268-45012**
   u. Install the cold start injector pipe with four new gaskets and two union bolts.
      **Torque: 4A-FE — 180 kg-cm (13 ft-lb, 18 N·m)**
   v. Reconnect the cold start injector connector.
   w. Reconnect the cable to the negative ( – ) terminal of the battery.
   x. Check for fuel leakage. (See page FI-12)

*(Left-column illustrations — image only: SST pressure-gauge "Reconnect" views for **4A-FE** and **4A-GE**.)*

---
<a id="p125"></a>
**[PDF p.125]** — FI-105 — EFI SYSTEM — Fuel System

> **Scan gap:** pages FI-99 to FI-104 are missing from this scan.

## Cold Start Injector (4A-FE)

*(Cutaway diagram — image only, see [PDF p.125]: Solenoid Coil, Spring, INJECTION, INLET, Plunger, Strainer. Circuit: Ignition Switch, STI, Cold Start Injector (STA/STJ), Start Injector Time Switch (STJ/STA), Solenoid Coil, Point, +B.)*

### ON-VEHICLE INSPECTION
**INSPECT RESISTANCE OF COLD START INJECTOR**
   a. Disconnect the cold start injector connector.
   b. Using an ohmmeter, measure the resistance between the terminals.
      **Resistance: 4A-FE — 3 – 5 Ω**

   If the resistance is not as specified, replace the injector.

   c. Reconnect the cold start injector connector.

### REMOVAL OF COLD START INJECTOR (4A-FE)
1. **DISCONNECT CABLE FROM NEGATIVE TERMINAL OF BATTERY**
2. **DISCONNECT COLD START INJECTOR CONNECTOR**
3. **REMOVE COLD START INJECTOR PIPE**
   a. Put a suitable container or shop towel under the injector pipe.
   b. Remove the two union bolts, four gaskets and injector pipe.
      > **HINT:** Slowly loosen the union bolts.

*(Left-column illustrations — image only, **4A-FE**: Ohmmeter across cold start injector terminals; injector pipe removal.)*

---
<a id="p126"></a>
**[PDF p.126]** — FI-106 — EFI SYSTEM — Fuel System

4. **REMOVE COLD START INJECTOR**
   Remove the two bolts, cold start injector and gasket.

### INSPECTION OF COLD START INJECTOR
1. **INSPECT INJECTION OF COLD START INJECTOR**
   > **CAUTION:** Keep clear of sparks during the test.
   a. Install SST (two unions) to the injector and delivery pipe with new gaskets and the union bolts.
      SST **09268-41045 (09268-41080)**
   b. Connect SST (hose) to the union.
      SST **09268-41045**
   c. Connect SST (wire) to the injector.
      SST **09842-30055**
   d. Put a container under the injector.
   e. Reconnect the battery negative ( – ) cable.
   f. Turn the ignition switch ON.
      > **NOTICE:** Do not start the engine.

*(Left-column illustrations — image only, **4A-FE**: injector removal; SST assembly — Union Bolt, New Gasket, SST(Union), SST(Hose), SST(Wire).)*

---
<a id="p127"></a>
**[PDF p.127]** — FI-107 — EFI SYSTEM — Fuel System

   g. Using SST, connect terminals +B and FP of the check connector.
      SST **09843-18020**
   h. Connect the test probes of the SST (wire) to the battery, and check that the spray is as shown.
      SST **09842-30055**
      > **NOTICE:** Perform this check within the shortest possible time.

2. **INSPECT LEAKAGE**
   a. In the condition above, disconnect the test probes of SST (wire) from the battery and check fuel leakage from the injector.
      SST **09842-30055**
      **Fuel drop: One drop or less per minute**
   b. Disconnect the battery negative ( – ) cable.
   c. Remove SST.
      SST **09268-41045 (09268-41080)** and **09842-30055**, **09843-18020**

*(Left-column illustrations — image only: Check Connector with SST across FP/+B; **4A-FE** SST(Wire) "Connect" to battery; **4A-FE** SST(Wire) "Disconnect" from battery.)*

---
<a id="p128"></a>
**[PDF p.128]** — FI-108 — EFI SYSTEM — Fuel System

### INSTALLATION OF COLD START INJECTOR
1. **INSTALL COLD START INJECTOR**
   Install a new gasket and the injector with the two bolts.
   **Torque: 4A-FE — 95 kg-cm (82 in.-lb, 9.3 N·m)**

2. **INSTALL COLD START INJECTOR PIPE**
   Install the injector pipe with four new gaskets and the two union bolts.
   **Torque: 4A-FE — 180 kg-cm (13 ft-lb, 18 N·m)**

3. **CONNECT COLD START INJECTOR CONNECTOR**
4. **CONNECT CABLE TO NEGATIVE TERMINAL OF BATTERY**
5. **CHECK FOR FUEL LEAKAGE** (See page FI-12)

*(Left-column illustrations — image only, **4A-FE**: cold start injector installation; injector pipe installation.)*

---
<a id="p129"></a>
**[PDF p.129]** — FI-109 — EFI SYSTEM — Fuel System

## Fuel Pressure Regulator (4A-FE)

*(Diagrams — image only, see [PDF p.129], **4A-FE**: Cutaway — Spring, Diaphragm, Check Valve, FROM DELIVERY PIPE, TO RETURN HOSE. Installed view — Vacuum Sensing Hose, Fuel Pressure Regulator, Fuel Return Hose.)*

### ON-VEHICLE INSPECTION
**INSPECT FUEL PRESSURE** (See page FI-95)

### REMOVAL OF FUEL PRESSURE REGULATOR
1. **DISCONNECT VACUUM SENSING HOSE**
2. **DISCONNECT FUEL RETURN HOSE**

*(Lower-left illustration — image only, **4A-FE**: fuel pressure regulator in place.)*

---
<a id="p130"></a>
**[PDF p.130]** — FI-110 — EFI SYSTEM — Fuel System

3. **REMOVE FUEL PRESSURE REGULATOR**
   a. Remove the two bolts, and pull out the pressure regulator.
   b. Remove the O-ring from the pressure regulator.

### INSTALLATION OF FUEL PRESSURE REGULATOR
1. **INSTALL FUEL PRESSURE REGULATOR**
   a. Apply a light coat of gasoline to a new O-ring, and install it to the pressure regulator.
   b. Install the pressure regulator with the two bolts.
      **Torque: 4A-FE — 95 kg-cm (82 in-lb, 9.3 N·m)**

2. **CONNECT FUEL RETURN HOSE**
3. **CONNECT VACUUM SENSING HOSE**
4. **CHECK FOR FUEL LEAKAGE** (See page FI-12)

*(Left-column illustrations — image only, **4A-FE**: regulator removal; O-ring orientation on Delivery Pipe showing WRONG vs CORRECT installation.)*

---
<a id="p131"></a>
**[PDF p.131]** — FI-111 — EFI SYSTEM — Fuel System

## Injector (4A-FE (2WD))

*(Cutaway diagram — image only, see [PDF p.131]: Needle Valve, Solenoid Coil, Connector Terminal, INJECTION, INLET.)*

### ON-VEHICLE INSPECTION
1. **INSPECT INJECTOR OPERATION**
   Check operation sound from each injector.
   a. With the engine running or cranking, use a sound scope to check that there is normal operating noise in proportion to engine rpm.

*(Lower-left illustration — image only, **4A-FE**: Sound Scope applied to injectors on delivery pipe.)*
---
<a id="p132"></a>
**[PDF p.132]** — EFI SYSTEM — Fuel System (FI-112)

*(Continuation of injector operation check — 4A-FE)*

(b) If you have no sound scope, you can check the injector transmission operation with your finger. **(4A-FE)**

If no sound or an unusual sound is heard, check the wiring connector, injector or injector signal from the ECU.

*(image only — see [PDF p.132]: 4A-FE, checking injector transmission with finger)*

### 2. INSPECT INJECTOR RESISTANCE (4A-FE)

*(image only — see [PDF p.132]: 4A-FE, ohmmeter across injector terminals)*

a. Disconnect the injector connector.
b. Using an ohmmeter, measure the resistance between the terminals.

**Resistance: Approx. 13.8 Ω**

If the resistance is not as specified, replace the injector.

c. Reconnect the injector connector.

---
<a id="p133"></a>
**[PDF p.133]** — EFI SYSTEM — Fuel System (FI-113)

## REMOVAL OF INJECTORS

1. DISCONNECT CABLE FROM NEGATIVE TERMINAL OF BATTERY
2. REMOVE COLD START INJECTOR PIPE (See step 3 page FI-105)
3. DISCONNECT VACUUM SENSING HOSE FROM FUEL PRESSURE REGULATOR
4. DISCONNECT INJECTOR CONNECTORS
5. DISCONNECT HOSE FROM FUEL RETURN PIPE
6. DISCONNECT FUEL INLET HOSE FROM DELIVERY PIPE
   a. **(4A-FE)** Remove the inlet pipe mount bolt.
   b. Remove the union bolt and two gaskets, and disconnect the inlet hose from the delivery pipe.
7. **(4A-FE 4WD)** REMOVE EGR VACUUM MODULATOR (See step 6 page EM-60)

*(image only — see [PDF p.133]: 4A-FE (Australia), fuel inlet hose / union bolt area)*

---
<a id="p134"></a>
**[PDF p.134]** — EFI SYSTEM — Fuel System (FI-114)

### 8. REMOVE DELIVERY PIPE AND INJECTORS

a. **(4A-FE)** Remove the two bolts and delivery pipe together with the four injectors.

> **NOTICE:** Be careful not to drop the injector, when removing the delivery pipe.

b. **(4A-FE)** Remove the four insulators and two spacers from the cylinder head.
c. Pull out the four injectors from the delivery pipe.

*(image only — see [PDF p.134]: 4A-FE (Ex. Australia), delivery pipe removal)*

## INSPECTION OF INJECTORS

### 1. INSPECT INJECTOR INJECTION

> **CAUTION:** Keep clear of sparks during the test.

*(image only — see [PDF p.134]: 4A-FE, SST setup — Pressure Regulator (From Vehicle), SST (Hose), SST (Union), SST (Clamp), Injector, Fuel Filter (On Vehicle))*

---
<a id="p135"></a>
**[PDF p.135]** — EFI SYSTEM — Fuel System (FI-115)

a. Disconnect the fuel inlet hose from the fuel filter outlet.
b. Connect SST (union and hose) to the fuel filter outlet with new gaskets and the union bolt.

**SST 09268-41045 (90405-09015)**

> **HINT:** Use the vehicle's fuel filter.

c. Remove the pressure regulator from the delivery pipe, and connect the fuel hose to pressure regulator.
d. Install a new O-ring to the pressure regulator.
e. Connect the SST (hose) to the pressure regulator with SST (union) and two bolts.

**SST 09268-41045 (09268-41090)**

f. Install the grommet and a new O-ring to the injector.
g. Connect SST (union and hose) to the injector, and hold the injector and union with SST (clamp).

**SST 09268-41045**

h. Put the injector into the graduated cylinder.

> **HINT:** Install the suitable vinyl hose onto the injector to prevent gasoline from splashing out.

i. Reconnect the battery negative ( − ) cable.
j. Turn the ignition switch ON.

> **NOTICE:** Do not start the engine.

*(image only — see [PDF p.135]: top — SST (Union), Union Bolt, New Gasket, Fuel Filter, Fuel Hose, SST (Hose); middle — 4A-FE Pressure Regulator with SST (Hose) and SST (Union); bottom — SST (Hose), SST (Union), O-ring, SST (Clamp), Vinyl Tube)*

---
<a id="p136"></a>
**[PDF p.136]** — EFI SYSTEM — Fuel System (FI-116)

k. Using SST, connect terminals +B and FP of the check connector.

**SST 09843-18020**

**LOCATION:** See page FI-133

*(image only — see [PDF p.136]: Check Connector, FP and +B terminals, SST)*

l. Connect SST (wire) to the injector and battery for 15 seconds, and measure the injection volume with a graduated cylinder. Test each injector two or three times.

**SST 09842-30070**

**Volume:**
**4A-FE 40 − 50cc (2.4 − 3.1 cu in.) per 15sec.**

**Difference between each injector: 5cc (0.3 cu in.) or less**

If the injection volume is not as specified, replace the injector.

### 2. INSPECT LEAKAGE

a. In the condition above, disconnect the test probes of SST (wire) from the battery and check the fuel leakage from the injector.

**SST 09842-30070**

**Fuel drop: One drop or less per minute.**

b. Disconnect the battery negative ( − ) cable.
c. Remove SST and the service wire.

**SST 09268-41045**

## INSTALLATION OF INJECTORS

### 1. INSTALL INJECTORS AND DELIVERY PIPE

a. Install a new grommet to the injector.
b. Apply a light coat of gasoline to a new O-ring and install it to the injector.

*(image only — see [PDF p.136]: 4A-FE (2WD) injector; SST wire/battery injection test; injector with O-ring and Grommet)*

---
<a id="p137"></a>
**[PDF p.137]** — EFI SYSTEM — Fuel System (FI-117)

c. While turning the injector left and right, install it to the delivery pipe. Install the four injectors.
d. **(4A-FE)** Place the four insulators and two spacers in position on the cylinder head.
   **(4A-GE)** Place the four insulators and three spacers in position on the cylinder head.
e. Place the injectors together with the delivery pipe in position on the cylinder head.
f. Check that the injectors rotate smoothly.

> **HINT:** If injectors do not rotate smoothly, the probable cause is incorrect installation of O-rings. Replace the O-ring.

g. Position the injector connector upward.

*(image only — see [PDF p.137]: 4A-FE (Ex. Australia) O-Ring CORRECT/WRONG seating on Injector/Delivery Pipe/Grommet; 4A-FE Spacer/Insulator placement on cylinder head; 4A-FE injector connector Upward)*

---
<a id="p138"></a>
**[PDF p.138]** — EFI SYSTEM — Fuel System (FI-118)

h. **(4A-FE)** Install and torque the two bolts.
   **(4A-GE)** Install and torque the three bolts.

**Torque: 4A-FE 150 kg-cm (11 ft-lb, 15 N·m)**

*(image only — see [PDF p.138]: 4A-FE (Ex. Australia), delivery pipe bolt tightening)*

---
<a id="p139"></a>
**[PDF p.139]** — EFI SYSTEM — Fuel System (FI-119)

### 3. CONNECT FUEL INLET HOSE TO DELIVERY PIPE

a. Connect the inlet hose with two new gaskets and the union bolt.

**Torque: 300 kg-cm (22 ft-lb, 29 N·m)**

4. CONNECT FUEL RETURN HOSE
5. CONNECT INJECTOR CONNECTORS
6. CONNECT VACUUM SENSING HOSE
7. INSTALL COLD START INJECTOR PIPE (See step 2 page FI-108)
8. CONNECT CABLE TO NEGATIVE TERMINAL OF BATTERY
9. CHECK FOR FUEL LEAKAGE (See page FI-12)

*(image only — see [PDF p.139]: 4A-FE (Ex. Australia), inlet hose / union bolt connection)*

---
<a id="p140"></a>
**[PDF p.140]** — EFI SYSTEM — Air Induction System (FI-122)

> **Scan gap:** pages FI-120 to FI-121 are missing from this scan.

## Throttle Body (4A-FE)

*(image only — see [PDF p.140]: Throttle Position Sensor detail — Power Point, Moving Point, Guide Cam, Idle Point, Power Point; connector terminals PSW, E2, IDL)*

## ON-VEHICLE CHECK

### 1. CHECK THROTTLE BODY

a. Check that the throttle linkage moves smoothly.
b. Check the vacuum at each port.
   - Start and warm up the engine.
   - Check the vacuum with your finger.

| Port | Throttle Valve Opening |
|------|------------------------|
| P *1 | Positioned more than P port. |
| E *2 | Positioned more than E port. |
| R *2 | Positioned more than R port. |

- \*1: With fuel evaporative emission control system
- \*2: With exhaust gas recirculation system

*(image only — see [PDF p.140]: 2WD (w/ EGR SYSTEM) port locations E, R, P)*

---
<a id="p141"></a>
**[PDF p.141]** — EFI SYSTEM — Air Induction System (FI-123)

### 2. INSPECT THROTTLE POSITION SENSOR

a. Disconnect the sensor connector.
b. Insert a feeler gauge between the throttle stop screw and stop lever.
c. Using an ohmmeter, measure the resistance between each terminal.

If the resistance is not as specified, adjust or replace the throttle position sensor.

| Clearance between lever and stop screw | IDL − E2 | PSW − E2 | IDL − PSW |
|----------------------------------------|----------|----------|-----------|
| **0.60 mm (0.0236 in.)** | Continuity | No continuity | No continuity |
| **0.80 mm (0.0316 in.)** | No continuity | No continuity | No continuity |
| Throttle valve fully opened position | No continuity | Continuity | No continuity |

d. Reconnect the sensor connector.

*(image only — see [PDF p.141]: 0.60 or 0.80 mm feeler gauge with ohmmeter across PSW/E2/IDL terminals)*

## REMOVAL OF THROTTLE BODY

1. DISCONNECT CABLE FROM NEGATIVE TERMINAL OF BATTERY
2. DRAIN ENGINE COOLANT
3. DISCONNECT ACCELERATOR CABLE
4. **(A/T)** DISCONNECT THROTTLE CABLE
5. DISCONNECT AIR CLEANER HOSE
6. REMOVE CABLE BRACKET FROM THROTTLE BODY
7. DISCONNECT THROTTLE POSITION SENSOR CONNECTOR
8. DISCONNECT FOLLOWING HOSES:
   a. No.2 water by-pass hose from the air valve.
   b. PCV hose from the throttle body.
   c. Vacuum hose(s) from the port(s).
9. REMOVE THROTTLE BODY
   a. Remove the two bolts and nuts, and disconnect the throttle body and gasket.
   b. Disconnect the No.1 water by-pass hose, and remove the throttle body.

---
<a id="p142"></a>
**[PDF p.142]** — EFI SYSTEM — Air Induction System (FI-124)

## INSPECTION OF THROTTLE BODY

### 1. CLEAN THROTTLE BODY

a. Using a soft brush and carburetor cleaner, clean the cast parts.
b. Using compressed air, clean all the passages and apertures.

> **NOTICE:** To prevent deterioration, do not clean the throttle position sensor.

### 2. INSPECT THROTTLE BODY VALVE

Check that there is no clearance between the throttle stop screw and throttle lever when the throttle valve is fully closed.

*(image only — see [PDF p.142]: "No Clearance" at throttle stop screw)*

### 3. INSPECT THROTTLE POSITION SENSOR

a. Make an angle gauge as shown in the figure.
b. Set throttle valve opening angle to the specifications below from the vertical position (incl. throttle valve fully closed angle **6°**).

**Throttle valve opening angle:**
- **M/T 73° or 79°**
- **A/T 63° or 69°**

*(angle-gauge diagram — see [PDF p.142]:)*
- M/T gauge: **For 79°** (11°) — **50 mm (1.97 in.)** — **For 73°** (17°)
- A/T gauge: **For 69°** (21°) — **50 mm (1.97 in.)** — **For 63°** (27°)
- Fully Closed Angle **6°**, Throttle Valve Opening Angle, Angle Gauge

---
<a id="p143"></a>
**[PDF p.143]** — EFI SYSTEM — Air Induction System (FI-125)

c. Using an ohmmeter, check the continuity between each of the terminals.

| Throttle valve opening angle (M/T) | Throttle valve opening angle (A/T) | IDL − E2 | PSW − E2 | IDL − PSW |
|-----------------------------------|-----------------------------------|----------|----------|-----------|
| **73° from vertical** | **63° from vertical** | No continuity | No continuity | No continuity |
| **79° from vertical** | **69° from vertical** | No continuity | Continuity | No continuity |
| **Less than 7.5 from vertical** | | Continuity | No continuity | No continuity |

<!-- NEEDS REVIEW: "Less than 7.5 from vertical" printed without a degree symbol/unit in the image; kept as-is. -->

### 4. IF NECESSARY, ADJUST THROTTLE POSITION SENSOR

a. Loosen the two set screws of the sensor.
b. Insert a **0.70 mm (0.028 in.)** feeler gauge, between the throttle stop screw and stop lever.
c. Connect the test probe of an ohmmeter to the terminals IDL and E2 of the sensor.
d. Gradually turn the sensor counterclockwise until the ohmmeter deflects, and secure it with the two screws.
e. Recheck the continuity between terminals IDL and E2.

| Clearance between lever and stop screw | Continuity (IDL − E2) |
|----------------------------------------|-----------------------|
| **0.60 mm (0.024 in.)** | Continuity |
| **0.80 mm (0.032 in.)** | No continuity |

*(image only — see [PDF p.143]: ohmmeter across PSW/E2/IDL; screwdriver turning sensor; 0.70 mm feeler gauge with ohmmeter; 0.60 or 0.80 mm feeler gauge with ohmmeter)*

---
<a id="p144"></a>
**[PDF p.144]** — EFI SYSTEM — Air Induction System (FI-126)

## INSTALLATION OF THROTTLE BODY

### 1. INSTALL THROTTLE BODY

a. Connect No.1 water by-pass hose.
b. Install a new gasket and the throttle body with the two bolts and nuts.

**Torque: 220 kg-cm (16 ft-lb, 22 N·m)**

### 2. CONNECT FOLLOWING HOSES:

a. No.2 water by-pass hose.
b. PCV hose to the throttle body.
c. Vacuum hose(s) to the port(s).

3. CONNECT THROTTLE POSITION SENSOR CONNECTOR
4. INSTALL CABLE BRACKET TO THROTTLE BODY
5. CONNECT AIR CLEANER HOSE
6. **(A/T)** CONNECT THROTTLE CABLE, AND ADJUST IT
7. CONNECT ACCELERATOR CABLE, AND ADJUST IT
8. CONNECT CABLE TO NEGATIVE TERMINAL OF BATTERY
9. FILL WITH ENGINE COOLANT (See page CO-6)

*(image only — see [PDF p.144]: throttle body installation)*

---
<a id="p145"></a>
**[PDF p.145]** — EFI SYSTEM — Air Induction System (FI-131)

> **Scan gap:** pages FI-127 to FI-130 are missing from this scan.

## Auxiliary Air Valve

*(cutaway diagram — see [PDF p.145]: Idle Speed Adjusting Screw, Throttle Body, Throttle Valve, FROM AIR CLEANER → TO MANIFOLD, Auxiliary Air Valve, Valve, Coolant)*

## ON-VEHICLE INSPECTION

### INSPECT AIR VALVE OPERATION

**(w/o Air Flow Meter)**

a. Remove the air cleaner hose.
b. Check the engine rpm by closing the air port on the throttle body.

At low temp. (Coolant temp.: below **80°C (176°F)**)
- The engine RPM should drop.

After warm-up
- Check that engine RPM does not drop more than **100 rpm**.

c. Install the air cleaner hose.

If operation is not as specified, replace the air valve.

**(w/ Air Flow Meter)**

Check the engine rpm by fully screwing in the idle speed adjusting screw.

At low temp. (Coolant temp.: below **80°C (176°F)**)
- When the idle speed adjusting screw is in, the engine rpm should drop.

After warm-up
- When the idle speed adjusting screw is in, the engine rpm should drop below idle speed duel stop.

If operation is not as specified, replace the air valve.

*(image only — see [PDF p.145]: 4A-FE, Air Port on throttle body)*
---
<a id="p146"></a>
**[PDF p.146]** — EFI SYSTEM — Air Induction System (FI-132)

## REMOVAL OF AUXILIARY AIR VALVE

*(image only — see [PDF p.146]: **4A-FE** air valve removal from throttle body)*

1. **REMOVE THROTTLE BODY**
   4A-FE (See page FI-123)

2. **REMOVE AIR VALVE FROM THROTTLE BODY**
   - (4A-FE) Remove the three screws, air valve, gasket and O-ring.
   - (4A-GE) Remove the five screws, air valve, gasket and O-ring.

## INSTALLATION OF AIR VALVE

*(image only — see [PDF p.146]: **4A-FE** exploded view — New Gasket, New O-Ring, throttle body)*

1. **INSTALL AIR VALVE TO THROTTLE BODY**
   a. Place new gasket and O-ring on the throttle body.
   b. (4A-FE) Install the air valve with the three screws.
      (4A-GE) Install the air valve with the five screws.

2. **INSTALL THROTTLE BODY**
   4A-FE (See page FI-126)

---
<a id="p147"></a>
**[PDF p.147]** — EFI SYSTEM — Electronic Control System (FI-133)

# ELECTRONIC CONTROL SYSTEM
## Location of Electronic Control Parts (4A-FE)

*(image only — see [PDF p.147]: labeled engine layout diagram)* Component callouts:
- Vacuum Sensor
- Circuit Opening Relay (AT180) / (AT171) / (AE)
- ECU
- ISC Valve (2WD)
- ISC Valve (4WD)
- Variable Resistor (w/o TWC)
- Check Connector (AT) / (AE)
- Water Temp. Sensor
- Start Injector Time Switch
- Oxygen Sensor (w/ TWC)
- Intake Air Temp. Sensor
- EFI Main Relay (AE)
- EFI Main Relay (AT)

---
<a id="p148"></a>
**[PDF p.148]** — EFI SYSTEM — Electronic Control System (FI-134)

## EFI Main Relay

*(circuit diagram — see [PDF p.148])* Wiring detail:
- (AT) **FL MAIN 0.85R** / (AE) — to Fuse EFI **15A** — to EFI Main Relay — to ECU **+B**
- Ignition Switch: AM2 → IG2 — Fuse IGN **10A (AE)**, **7.5A (AT)** — to ECU **+B1**
- FL MAIN **2.0L** (AT), (AE) — FL AM2 **30A** — Battery — ECU **E1**

### INSPECTION OF EFI MAIN RELAY (AE)

1. **INSPECT RELAY CONTINUITY**
   a. Using an ohmmeter, check that there is continuity between terminals 1 and 2.
   b. Check that there is no continuity between terminals 3 and 4.

   If continuity is not as specified, replace the relay.

2. **INSPECT RELAY OPERATION**
   a. Apply battery voltage across terminals 1 and 2.
   b. Using an ohmmeter, check that there is continuity between terminals 3 and 4.

   If operation is not as specified, replace the relay.

### INSPECTION OF EFI MAIN RELAY (AT)

1. **INSPECT RELAY CONTINUITY**
   a. Using an ohmmeter, check that there is continuity between terminals 1 and 3.
   b. Check that there is no continuity between terminals 2 and 4.

   If continuity is not as specified, replace the relay.

---
<a id="p149"></a>
**[PDF p.149]** — EFI SYSTEM — Electronic Control System (FI-135)

### INSPECTION OF EFI MAIN RELAY (AT) *(continued)*

2. **INSPECT RELAY OPERATION**
   a. Apply battery voltage across terminals 1 and 3.
   b. Using an ohmmeter, check that there is continuity between terminals 2 and 4.

   If operation is not as specified, replace the relay.

## Circuit Opening Relay

*(circuit diagram — see [PDF p.149])* Wiring detail:
- From Ignition Switch (ST1) → To ECU (STA)
- To ECU (+B); To EFI Main Relay; terminals +B, STA, FP, FC, E1
- Check Connector (+B, FP)
- Fuel Pump (M) — (w/o Air Flow Meter): To ECU (FC); (w/ Air Flow Meter): Fuel Pump Switch

### INSPECTION OF CIRCUIT OPENING RELAY (w/o Air Flow Meter)

1. **INSPECT RELAY CONTINUITY**
   a. Using an ohmmeter, check that there is continuity between terminals STA and E1.
   b. Check that there is continuity between terminals +B and FC.
   c. Check that there is no continuity between terminals +B and FP.

   If continuity is not as specified, replace the relay.

2. **INSPECT RELAY OPERATION**
   a. Apply battery voltage across terminals STA and E1.
   b. Using an ohmmeter, check that there is continuity between terminals +B and FP.

---
<a id="p150"></a>
**[PDF p.150]** — EFI SYSTEM — Electronic Control System (FI-136)

### INSPECTION OF CIRCUIT OPENING RELAY (w/o Air Flow Meter) *(continued)*

2. **INSPECT RELAY OPERATION** *(continued)*
   c. Apply battery voltage across terminals +B and FC.
   d. Check that there is continuity between terminals +B and FP.

   If operation is not as specified, replace the relay.

### INSPECTION OF CIRCUIT OPENING RELAY (w/ Air Flow Meter)

1. **INSPECT RELAY CONTINUITY**
   a. Using an ohmmeter, check that there is continuity between terminals STA and E1.
   b. Check that there is continuity between terminals +B and FC.
   c. Check that there is no continuity between terminals +B and FP.

   If continuity is not as specified, replace the relay.

2. **INSPECT RELAY OPERATION**
   a. Apply battery voltage across terminals STA and E1.
   b. Using an ohmmeter, check that there is continuity between terminals +B and FP.
   c. Apply battery voltage across terminals +B and FC.
   d. Check that there is continuity between terminals +B and FP.

   If operation is not as specified, replace the relay.

---
<a id="p151"></a>
**[PDF p.151]** — EFI SYSTEM — Electronic Control System (FI-137)

## Start Injector Time Switch

*(circuit diagram — see [PDF p.151])* Wiring detail:
- From Ignition Switch (ST1) → To ECU (STA)
- Terminals STA, STJ; Start Injector Time Switch

### INSPECTION OF START INJECTOR TIME SWITCH (4A-FE)

**INSPECT START INJECTOR TIME SWITCH**

Using an ohmmeter, measure the resistance between each terminal.

**Resistance:**

| Terminals | Resistance |
|---|---|
| STA – STJ | **20 – 40 Ω** below 30°C (86°F) |
| STA – STJ | **40 – 60 Ω** above 40°C (104°F) |
| STA – Ground | **20 – 80 Ω** |

If the resistance is not as specified, replace the switch.

---
<a id="p152"></a>
**[PDF p.152]** — EFI SYSTEM — Electronic Control System (FI-138)

## Water Temperature Sensor

*(characteristic graph — see [PDF p.152])* WATER TEMP. SENSOR: RESISTANCE **kΩ** (vertical axis, log scale from **0.2** to **40**) vs. TEMPERATURE °C (°F) horizontal axis **−20 (−4)** to **120 (248)**. Thermistor. Curve band descends from approx. **20 kΩ** at −20°C to below **0.2 kΩ** at 120°C.

Axis tick labels:
- RESISTANCE kΩ: 40, 20, 10, 8, 6, 4, 2, 1, 0.8, 0.6, 0.4, 0.2
- TEMPERATURE °C: −20, 0, 20, 40, 60, 80, 100, 120
- TEMPERATURE (°F): (−4)(32)(68)(104)(140)(176)(212)(248)

### INSPECTION OF WATER TEMPERATURE SENSOR (4A-FE)

**INSPECT WATER TEMPERATURE SENSOR**

Using an ohmmeter, measure the resistance between the terminals.

**Resistance: Refer to the chart above**

If the resistance is not as specified, replace the sensor.

---
<a id="p153"></a>
**[PDF p.153]** — EFI SYSTEM — Electronic Control System (FI-139)

## Intake Air Temperature Sensor (w/o Air Flow Meter)

*(characteristic graph — see [PDF p.153])* INTAKE AIR TEMP. SENSOR: RESISTANCE **kΩ** (vertical axis, log scale from **0.2** to **40**) vs. TEMPERATURE °C (°F) horizontal axis **−20 (−4)** to **120 (248)**. Thermistor. Curve band descends from approx. **20 kΩ** at −20°C to below **0.2 kΩ** at 120°C.

Axis tick labels:
- RESISTANCE kΩ: 40, 20, 10, 8, 6, 4, 2, 1, 0.8, 0.6, 0.4, 0.2
- TEMPERATURE °C: −20, 0, 20, 40, 60, 80, 100, 120
- TEMPERATURE (°F): (−4)(32)(68)(104)(140)(176)(212)(248)

### INSPECTION OF INTAKE AIR TEMPERATURE SENSOR (4A-FE)

**INSPECT RESISTANCE OF INTAKE AIR TEMPERATURE SENSOR**

Using an ohmmeter, measure the resistance between the terminals.

**Resistance: Refer to the chart above**

If the resistance is not as specified, replace the sensor.

---
<a id="p154"></a>
**[PDF p.154]** — EFI SYSTEM — Electronic Control System (FI-140)

## Vacuum Sensor (w/o Air Flow Meter) (Manifold Absolute Pressure Sensor)

*(cutaway diagrams — see [PDF p.154])*
- **Type A**: Vacuum Chamber, Terminal, Filter, FROM INTAKE MANIFOLD
- **Type B**: Vacuum Chamber, Terminal, Filter, FROM INTAKE MANIFOLD
- Wiring: Vacuum Sensor (Manifold Absolute Pressure Sensor) terminals E2, PIM, VCC → ECU terminals E2, PIM, VCC, E1

### INSPECTION OF VACUUM SENSOR

1. **INSPECT POWER SOURCE VOLTAGE OF VACUUM SENSOR**
   a. Disconnect the vacuum sensor connector.
   b. Turn the ignition switch ON.
   c. Using a voltmeter, measure the voltage between terminals VCC and E2 of the vacuum sensor connector.

   **Voltage: 4 – 6 V**

2. **INSPECT POWER OUTPUT OF VACUUM SENSOR**
   a. Turn the ignition switch ON.
   b. Disconnect the vacuum hose of the intake manifold side.

---
<a id="p155"></a>
**[PDF p.155]** — EFI SYSTEM — Electronic Control System (FI-141)

### INSPECTION OF VACUUM SENSOR *(continued)* — 4A-FE (2WD)

2. **INSPECT POWER OUTPUT OF VACUUM SENSOR** *(continued)*
   c. Connect a voltmeter to terminals PIM and E2 of the ECU, and measure and record the output voltage under ambient atmospheric pressure.
   d. Apply vacuum to the vacuum sensor in **100 mmHg (3.94 in.Hg, 13.3 kPa)** segments to **500 mmHg (19.69 in.Hg, 66.7 kPa)**.
   e. Measure voltage drop from step (c) above for each segment.

**Voltage drop:**

| Applied Vacuum mmHg (in.Hg, kPa) | 100 (3.94, 13.3) | 200 (7.87, 26.7) | 300 (11.81, 40.0) | 400 (15.75, 53.3) | 500 (19.69, 66.7) |
|---|---|---|---|---|---|
| Voltage drop V | **0.3–0.5** | **0.7–0.9** | **1.1–1.3** | **1.5–1.7** | **1.9–2.1** |

> **HINT:** The bottom of this page carries handwritten owner's field notes (not part of the printed manual), transcribed here for completeness:
> `4AFE - AT171`
> - E2 · VCC — 4.98 V
> - E2 – PIM — 3.62 V
> - −0.1 bar — 3.23 V
> - −0.2 bar — 2.88 V
> - −0.3 bar — 2.57 V
> - −0.4 bar — 2.28 V
> - −0.5 bar — 1.92 V
> - −0.6 bar — 1.61 V
> - −0.7 bar — 1.38 V
> - −0.8 bar — 1.13 V
> - −0.9 bar — 0.85 V
> <!-- NEEDS REVIEW: handwritten, some digits (e.g. AT171 code, 1.38 V) partly illegible -->

---
<a id="p156"></a>
**[PDF p.156]** — EFI SYSTEM — Electronic Control System (FI-142)

## Variable Resistor (w/o TWC)

*(circuit diagram — see [PDF p.156])* Wiring detail: Variable Resistor terminals VCC, VAF, E2 → ECU terminals +B (+B), VCC, VAF, E2.

### INSPECTION OF VARIABLE RESISTOR (4A-FE)

1. **INSPECT VOLTAGE OF VARIABLE RESISTOR**
   a. Using a voltmeter, measure the voltage between ECU terminals VCC and E2.

   **Voltage: 4 – 6 V**

---
<a id="p157"></a>
**[PDF p.157]** — EFI SYSTEM — Electronic Control System (FI-143)

### INSPECTION OF VARIABLE RESISTOR (4A-FE) *(continued)*

1. **INSPECT VOLTAGE OF VARIABLE RESISTOR** *(continued)*
   b. Measure the voltage between ECU terminals VAF and E2 while slowly turning idle mixture adjusting screw first fully counterclockwise, and then fully clockwise.
   c. Check that the voltage changes smoothly from **0 V** to approx. **5 V**.

2. **INSPECT RESISTANCE OF VARIABLE RESISTOR**
   a. Disconnect the variable resistor connector.
   b. Using an ohmmeter, measure the resistance between the terminals VCC and E2.

   **Resistance: 4 – 6 kΩ**

*(images — see [PDF p.157]: 4A-FE idle mixture adjusting screw; voltmeter across ECU terminals VAF/E2; ohmmeter across E2/VCC)*

---
<a id="p158"></a>
**[PDF p.158]** — EFI SYSTEM — Electronic Control System (FI-144)

### INSPECTION OF VARIABLE RESISTOR (4A-FE) *(continued)*

2. **INSPECT RESISTANCE OF VARIABLE RESISTOR** *(continued)*
   c. Turn the idle mixture adjusting screw fully counterclockwise.
   d. Connect an ohmmeter to terminals VAF and E2. Turn the adjusting screw fully clockwise and check that the resistance value changes from approx. **5 kΩ** to **0 Ω** accordingly.

*(image — see [PDF p.158]: 4A-FE ohmmeter connected to terminals E2/VAF at variable resistor)*
---
<a id="p159"></a>
**[PDF p.159]** — EFI SYSTEM — Electronic Control System — FI-145

## Oxygen Sensor (w/ TWC)

### INSPECTION OF OXYGEN SENSOR

*(Diagram: Voltmeter connected to check-connector terminals VF1 and E1 — see [PDF p.159].)*

1. **WARM UP ENGINE**

   Allow the engine to reach normal operating temperature.

2. **INSPECT FEEDBACK VOLTAGE (VF)**

   Connect the positive (+) probe of a voltmeter to terminal VF1 of the check connector, and negative (−) probe to terminal E1. Perform the test as follows:

**Diagnostic flowchart (continues on FI-146):**

- **A.** Warm up the oxygen sensor with the engine at **2,500 rpm** for approx. **90 seconds**.
- **B.** Using SST, connect terminals TE1 and E1 of the check connector.
  - SST **09843-18020**
  - And maintain engine speed at **2,500 rpm**.
- **C.** Check the number of times the voltmeter needle fluctuates in **10 seconds**.
  - **4A-FE — 8 times or more** → **Normal**
  - **Zero** → **Replace the ECU.** → *"Zero again"* after replacing the oxygen sensor (loops back)
  - **4A-FE — Less than 8 times** → go to **D.**
- **D.** Warm up the oxygen sensor with the engine at **2,500 rpm** for approx. **90 seconds**. And maintain engine at **2,500 rpm**.
- **E.** Check the number of times the voltmeter needle fluctuates in **10 seconds**.
  - **6 times or more** → **Normal**
  - **Zero** → (continues to path ④ / ③ on FI-146)
  - **4A-FE — Less than 8 times** / **4A-GE — Less than 6 times** → go to **F.**
- **F.** Disconnect terminals TE1 and E1 of the check connector. And maintain engine speed at **2,500 rpm**.
- **G.** Measure voltage between terminals VF1 and E1.
  - **More than 0 V** → path **①** (continues on FI-146)
  - **0 V** → **Read and record diagnostic codes.** (See pages FI-28 to 31)
    - **Normal code and code 21** → path **②** (continues on FI-146)
    - **Malfunction code(s) (Ex. code 21)** → **Repair the relevant diagnostic code.**

Exit paths carried to next page: **①  ②  ③  ④**

**CONTINUED ON PAGE FI-146**

---
<a id="p160"></a>
**[PDF p.160]** — FI-146 — EFI SYSTEM — Electronic Control System

**CONTINUED FROM PAGE FI-145**

Diagnostic flowchart, continued (entry paths **①  ②  ③  ④**):

- **Path ③** → **Read and record diagnostic codes.** (See pages FI-28 to 31)
  - **Malfunction code(s) (Ex. code 21)** → **Repair the relevant diagnostic code.**
  - **Normal code and code 21** → Disconnect terminals TE1 and E1 of the check connector. And maintain engine at **2,500 rpm**.
    - → Measure voltage between terminals VF1 and E1.
      - **0 V** → join **Path ②** below (Disconnect the PCV hose.)
      - **5 V** → join **Path ④** below (water temp. sensor sequence)
- **Path ② (0 V branch)** → **Disconnect the PCV hose.**
  - → Measure voltage between terminals VF1 and E1.
    - **More than 0 V** → **Repair (Over rich)**
- **Path ④ (5 V branch)** → Disconnect the water temp. sensor connector and connect resistor with a resistance of **4 − 8 kΩ** or another coded water temp. sensor.
  - → Connect terminals TE1 and E1 of the check connector.
  - → Warm up the oxygen sensor with the engine at **2,500 rpm** for approx. **90 seconds**. And maintain engine speed at **2,500 rpm**.
  - → Measure voltage between terminals VF1 and E1.
    - **0 V** → **Replace the oxygen sensor.**
    - **5 V** → **Repair (Over lean)**
- **Path ①** → **Replace the oxygen sensor.**

---
<a id="p161"></a>
**[PDF p.161]** — EFI SYSTEM — Electronic Control System — FI-147

3. **INSPECT HEATER COIL RESISTANCE OF OXYGEN SENSOR**

   Using an ohmmeter, measure the resistance between the terminals +B and HT.

   **Resistance: 5.1 − 6.3 Ω**

   If the resistance is not as specified, replace the sensor.

   *(Diagram: ohmmeter across oxygen-sensor terminals +B and HT — see [PDF p.161].)*

## Engine ECU

### INSPECTION OF ECU

> **HINT:** The EFI circuit can be checked by measuring the resistance and voltage at the wiring connectors of the ECU.

1. **PREPARATION** (See page FI-36)

2. **INSPECT VOLTAGE OF ENGINE ECU**

   Check the voltage between each terminal of the wiring connectors.
   - Turn the ignition switch ON.
   - Measure the voltage at each terminal

   > **HINT:**
   > - Perform all voltage measurements with the connectors connected.
   > - Verify that the battery voltage is **11 V or more** when the ignition switch is ON position.

   *(Diagram: voltmeter probing ECU connector terminals +B1, +B, E1 — see [PDF p.161].)*

---
<a id="p162"></a>
**[PDF p.162]** — FI-148 — EFI SYSTEM — Electronic Control System

### Voltage at ECU Wiring Connectors (4A-FE)

| Terminals | Condition | STD voltage (V) |
|---|---|---|
| +B − E1 | Ignition SW ON | 10 − 14 |
| +B1 − E1 | Ignition SW ON | 10 − 14 |
| BATT − E1 | − | 10 − 14 |
| IDL − E2 | Ignition SW ON — Throttle valve open | 4.5 − 5.5 |
| PSW − E2 | Ignition SW ON — Throttle valve fully closed | 4.5 − 5.5 |
| No.10 − E01 | Ignition SW ON | 10 − 14 |
| No.20 − E02 | Ignition SW ON | 10 − 14 |
| W − E1 | Ignition SW ON | 0 |
| W − E1 | No trouble ("CHECK ENGINE" light off) and engine running | 10 − 14 |
| PIM − E2 | Ignition SW ON | 3.3 − 3.9 |
| VCC − E2 | Ignition SW ON | 4.5 − 5.5 |
| THA − E2 | Ignition SW ON — Intake air temperature 20°C (68°F) | 2.0 − 2.5 |
| THW − E2 | Ignition SW ON — Coolant temperature 80°C (176°F) | 0.4 − 0.7 |
| STA − E1 | Cranking | 6 − 14 |
| IGT − E1 | Idling | 0.7 − 1.0 |
| A/C − E1 | Ignition SW ON — A/C switch ON | 5 − 14 |
| A/C − E1 | Ignition SW ON — A/C switch OFF | 0 |
| T − E1 | Ignition SW ON — Check connector TE1 − E1 not connect | 10 − 14 |
| T − E1 | Ignition SW ON — Check connector TE1 − E1 connect | 0 |

**ECU Terminals (2WD)** — connector pinout (top row / bottom row):

Left connector block:

| top | EO1 | No.10 | STA | OX / VAF | G(−) | G1 | IGF | IGT | THA | PIM | THW | NSW | EGR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **bottom** | EO2 | No.20 | E1 | − | E21 | NE | − | IDL | VCC | PSW | E2 | HT | V-ISC |

Right connector block:

| top | T | ACT | − | − | FC | R/P | BATT | +B1 |
|---|---|---|---|---|---|---|---|---|
| **bottom** | VF | − | − | SPD | A/C | − | W | +B |

> **HINT:** The "OX / VAF" cell is a diagonal-split terminal (OX upper / VAF lower).

---
<a id="p163"></a>
**[PDF p.163]** — EFI SYSTEM — Electronic Control System — FI-149

### Voltage at ECU Wiring Connectors (4A-GE w/o Air Flow Meter)

| Terminals | Condition | STD voltage (V) |
|---|---|---|
| +B / +B1 − E1 | Ignition SW ON | 10 − 14 |
| BATT − E1 | − | 10 − 14 |
| IDL − E2 | Ignition SW ON — Throttle valve open | 4.5 − 5.5 |
| VTA − E2 | Ignition SW ON — Throttle valve fully closed | 0.5 or less |
| VTA − E2 | Ignition SW ON — Throttle valve fully open | 3.5 − 5.5 |
| VCC − E2 | Ignition SW ON — − | 4.5 − 5.5 |
| IGT − E1 | Idling | 0.7 − 1.0 |
| STA − E2 | Cranking | 6 − 14 |
| No.10 − E01 | Ignition SW ON | 10 − 14 |
| No.20 − E02 | Ignition SW ON | 10 − 14 |
| W − E1 | No trouble ("CHECK ENGINE" warning light off) and engine running | 10 − 14 |
| PIM − E2 | Ignition SW ON | 3.3 − 3.9 |
| VCC − E2 | Ignition SW ON | 4.5 − 5.5 |
| THA − E2 | Ignition SW ON — Intake air temp. 20°C (68°F) | 2.0 − 2.8 |
| THW − E2 | Ignition SW ON — Coolant temp. 80°C (176°F) | 0.4 − 0.7 |
| A/C − E1 | Ignition SW ON — Air conditioning ON | 10 − 14 |
| T − E1 | Ignition SW ON — Check connector TE1 − E1 not connect | 10 − 14 |
| T − E1 | Ignition SW ON — Check connector TE1 − E1 connect | 0.5 or less |

**ECU Terminals** — connector pinout (top row / bottom row):

Left connector block:

| top | EO1 | No.10 | − | − | V-ISC | − | − | − | G2 | Ne | IGF | STA | FPU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **bottom** | EO2 | No.20 | E1 | − | IGT | − | − | − | G1 | G(−) | − | − | − |

Middle connector block:

| top | VF | − | VAF | − | THW | THA | PIM | − |
|---|---|---|---|---|---|---|---|---|
| **bottom** | E21 | T | KNK | − | IDL | VCC | VTA | E2 |

Right connector block:

| top | − | ELS1 | FC | SEL | BATT | +B1 |
|---|---|---|---|---|---|---|
| **bottom** | ELS2 | SPD | A/C | − | W | +B |

---
<a id="p164"></a>
**[PDF p.164]** — EFI SYSTEM — Electronic Control System — FI-151

> **Scan gap:** page FI-150 is missing from this scan.

2. **INSPECT RESISTANCE OF ECU**

   > **NOTICE:**
   > - Do not touch the ECU terminals.
   > - The tester probe should be inserted into the wiring connector from the wiring side.

   Check the resistance between each terminal of the wiring connectors.
   - Disconnect the connectors from the ECU.
   - Measure the resistance at each terminal.

   *(Diagram: ohmmeter probing ECU wiring terminals IDL, E2 — see [PDF p.164].)*

### Resistance of ECU Wiring Connectors (4A-FE)

| Terminals | Condition | Resistance (Ω) |
|---|---|---|
| IDL − E2 | Throttle valve open | Infinity |
| IDL − E2 | Throttle valve fully closed | 0 |
| PSW − E2 | Throttle valve fully open | 0 |
| PSW − E2 | Throttle valve fully closed | Infinity |
| THA − E2 | Intake temperature 20°C (68°F) | 2,000 − 3,000 |
| THW − E2 | Coolant temperature 80°C (176°F) | 200 − 400 |
| G1 − G(−) | − | 140 − 180 |
| NE − G(−) | − | 140 − 180 |

**ECU Terminals (2WD)** — connector pinout (top row / bottom row):

Left connector block:

| top | EO1 | No.10 | − | OX / VAF | G(−) | G1 | IGF | IGT | THA | PIM | THW | NSW | EGR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **bottom** | EO2 | No.20 | − | − | E21 | NE | − | IDL | VCC | PSW | E2 | HT | V-ISC |

Right connector block:

| top | T | ACT | − | − | FC | R/P | BATT | +B1 |
|---|---|---|---|---|---|---|---|---|
| **bottom** | VF | − | − | SPD | A/C | − | W | +B |

---
<a id="p165"></a>
**[PDF p.165]** — EFI SYSTEM — Electronic Control System — FI-153

> **Scan gap:** page FI-152 is missing from this scan.

## Fuel Cut RPM (4A-FE)

*(Diagram: 4A-FE throttle-position-sensor connector, terminals E2 and IDL; tachometer — see [PDF p.165].)*

### INSPECTION OF FUEL CUT RPM

(a) Start and warm up the engine.

(b) Disconnect the connector from the throttle position sensor.

(c) Connect circuit terminals IDL and E2 on the wiring connector side.

(d) Gradually raise the engine rpm and check that there is fluctuation between the fuel cut and fuel return points.

> **HINT:**
> - The vehicle should be stopped.
> - Accessories switched off.

**Fuel cut rpm:**

| Engine | Fuel cut rpm |
|---|---|
| 4A-FE w/o TWC | **1,700 rpm** |
| 4A-FE w/ TWC | **1,900 rpm** |

**Fuel return rpm:**

| Engine | Fuel return rpm |
|---|---|
| 4A-FE w/o TWC | **1,200 rpm** |
| 4A-FE w/ TWC | **1,200 rpm** |

---
<a id="p166"></a>
**[PDF p.166]** — FI-156 — EFI SYSTEM — Electronic Control System

> **Scan gap:** pages FI-154 to FI-155 are missing from this scan.

## Idle-up System (w/ Air Flow Meter)

**Circuit diagram (see [PDF p.166]):** Battery → Fusible Link **AM1 40A** → Ignition Switch (AM1 → ST1) → ECU terminal **STA**; Fusible Link **ALT 100A**; VSV (coil) → ECU terminal **V-ISC**; ECU terminal **E1** (ground).

### INSPECTION OF IDLE-UP SYSTEM

1. **INSPECTION BATTERY VOLTAGE OF IDLE-UP VSV**

   (a) All accessories switched off.

   (b) Using a voltmeter, check that it indicates battery voltage during cranking and for ten seconds after starting.

2. **INSPECT IDLE-UP VSV**

   **A. Inspect VSV for open circuit**

   Using an ohmmeter, check that there is continuity between the terminals.

   **Resistance (Cold): 37 − 44 Ω**

   If there is no continuity, replace the VSV.

   **B. Inspect VSV for ground**

   Using an ohmmeter, check that there is no continuity between each terminal and the body.

   If there is continuity, replace the VSV.

   *(Diagrams: voltmeter check, ohmmeter continuity, ohmmeter no-continuity to body — see [PDF p.166].)*

---
<a id="p167"></a>
**[PDF p.167]** — EFI SYSTEM — Electronic Control System — FI-157

**C. Inspect VSV operation**

(a) Check that air flows from pipe E to pipe F.

(b) Apply battery voltage across the terminals.

(c) Check that air flows from pipe E to pipe F.

If operation is not as specified, replace the VSV.

*(Diagrams: VSV pipes E and F with air-flow test, and battery voltage applied across VSV terminals — see [PDF p.167].)*

<!-- NEEDS REVIEW: steps (a) and (c) both read "air flows from pipe E to pipe F" as printed; one is expected to be the no-voltage condition. Kept verbatim per image. -->

---
<a id="p168"></a>
**[PDF p.168]** — FI-158 — EFI SYSTEM — Electronic Control System

## Idle Speed Control (ISC) Valve (4A-FE)

**Circuit diagram (see [PDF p.168]):** Battery → Fusible Links **FL ALT 100A (AE, AT180) / 80A (AT171)**, **FL MAIN 2.0L**, **FL AM1 40A (AE, AT180) / 60A (AT171)** → Ignition Switch (AM1 → ST1) → Neutral Start Switch (A/T) / (M/T) → ECU terminal **STA**; **+B (+B1)**; From EFI Main Relay → **ISC Valve** coil → ECU terminal **V-ISC**; ECU terminal **E1** (ground).

### INSPECTION OF ISC VALVE

**INSPECT ISC VALVE**

**A. Inspect ISC Valve for open circuit** *(2WD)*

Using an ohmmeter, check that there is continuity between the terminals.

**Resistance: 2WD 30 − 33 Ω**

If there is no continuity, replace the ISC valve.

**B. Inspect ISC valve for ground** *(2WD)*

Using an ohmmeter, check that there is no continuity between each terminal and body.

If there is continuity, replace the ISC valve.

*(Diagrams: 2WD ISC valve ohmmeter continuity and no-continuity-to-body tests — see [PDF p.168].)*

---
<a id="p169"></a>
**[PDF p.169]** — EFI SYSTEM — Electronic Control System — FI-159

**C. Inspect ISC valve operation** *(2WD)*

(a) Check that air does not flow from pipes E to F.

(b) Apply battery voltage across the terminals.

(c) Check that air flows pipes E to F.

If operation is not as specified, replace the ISC valve.

*(Diagrams: 2WD ISC valve — no voltage: air in at E, "No Air" at F; battery voltage applied: air flows E to F — see [PDF p.169].)*
