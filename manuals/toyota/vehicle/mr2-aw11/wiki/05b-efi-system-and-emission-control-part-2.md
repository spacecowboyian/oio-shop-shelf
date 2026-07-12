# EFI System and Emission Control (Part 2)

*Toyota MR2 (AW11) 1988 Factory Service Manual — section codes `FI` (pages Fl-66 to Fl-128) and `CO` (pages CO-1 to CO-21) · source PDF pages 261–345 · covers 4A-GE and 4A-GZE.*

> Torque values are printed as `kg-cm (ft-lb, N·m)` (small values as `kg-cm (in.-lb, N·m)`), transcribed exactly as in the manual.

> This part of the manual continues from [EFI System and Emission Control (Part 1)](05a-efi-system-and-emission-control-part-1.md) and, on its final pages (CO-1 to CO-21), begins the **Cooling System** section — included here because it falls within this file's source page range. Cross-references such as "See page Fl-8" or "See pages Fl-24 to 27" point to Part 1.

---

<a id="p261"></a>
## Fuel System

<a id="p261"></a>
### Fuel Pump and Fuel Pressure — On-Vehicle Inspection (4A-GE)

#### 1. Check fuel pump operation

1. Turn the ignition switch ON.
   > **NOTE:** Do not start the engine.
2. Short the terminals **Fp** and **+B** of the check connector.
   > **NOTE:** The check connector is located near the resonator.
3. Check that there is pressure in the pressure regulator fuel return hose.
   > **NOTE:** At this time, you will hear fuel return noise from the pressure regulator.
4. Remove the service wire.
5. Turn the ignition switch OFF.

If there is no pressure, check the following parts:
- Fusible link (1.25B)
- Fuse (EFI 15A, AM2 7.5A)
- EFI main relay
- Circuit opening relay
- Fuel pump
- Wiring connections

#### 2. Check fuel pressure

1. Check that battery voltage is above 12 volts.
2. Disconnect the battery ground cable.
3. Disconnect the wiring connector from the cold start injector.
4. Place a suitable container or shop towel under the cold start injector pipe.
5. Slowly loosen the union bolt of the cold start injector pipe and remove the bolt and two gaskets from the delivery pipe.
6. Drain the fuel in the delivery pipe.
7. Install a gasket, SST, another gasket and union bolt to the delivery pipe as shown in the figure.
   - **SST 09268-45012**
8. Wipe off any splattered gasoline.
9. Reconnect the battery cable.
10. Short the terminals **Fp** and **+B** of the check connector.
    > **NOTE:** The check connector is located near the resonator.
11. Turn on the ignition switch.
12. Measure the fuel pressure.
    - **Fuel pressure: 2.7 – 3.1 kg/cm² (38 – 44 psi, 265 – 304 kPa)**
    - If high, replace the pressure regulator.
    - If low, check the following parts: fuel hoses and connection, fuel pump, fuel filter, pressure regulator.
13. Remove the service wire from the check connector.
14. Start the engine.
15. Disconnect the vacuum sensing hose from the pressure regulator and plug it.
16. Measure the fuel pressure at idling.
    - **Fuel pressure: 2.7 – 3.1 kg/cm² (38 – 44 psi, 265 – 304 kPa)**
17. Reconnect the vacuum sensing hose to the pressure regulator.
18. Measure the fuel pressure at idling after 90 seconds.
    - **Fuel pressure: 2.1 – 2.3 kg/cm² (30 – 33 psi, 206 – 226 kPa)**
    - If no pressure, check the vacuum sensing hose and pressure regulator.
19. Stop the engine. Check that the fuel pressure remains above **1.5 kg/cm² (21 psi, 147 kPa)** for 5 minutes after the engine is turned off.
    - If not within specification, check the fuel pump, pressure regulator and/or injectors.
20. After checking fuel pressure, disconnect the battery ground cable and carefully remove the SST to prevent gasoline from splashing.
21. Using new gaskets, reconnect the cold start injector hose to the delivery pipe.
22. Connect the wiring connector to the cold start injector.
23. Check for fuel leakage.

<a id="p264"></a>
### Fuel Pump and Fuel Pressure — On-Vehicle Inspection (4A-GZE)

#### 1. Check fuel pump operation

1. Turn the ignition switch ON.
   > **NOTE:** Do not start the engine.
2. Short the terminals **Fp** and **+B** of the check connector.
   > **NOTE:** The check connector is located near the intercooler.
3. Check that there is pressure in the pressure regulator fuel return hose.
   > **NOTE:** At this time, you will hear fuel return noise from the pressure regulator.
4. Remove the service wire.
5. Turn the ignition switch OFF.

If there is no pressure, check the following parts:
- Fusible link (1.25B)
- Fuse (EFI 15A, AM2 7.5A)
- EFI main relay
- Circuit opening relay
- Fuel pump
- Wiring connections

#### 2. Check fuel pressure

1. Check that battery voltage is above 12 volts.
2. Disconnect the battery ground cable.
3. Disconnect the wiring connector from the cold start injector.
4. Place a suitable container or shop towel under the cold start injector pipe.
5. Slowly loosen the union bolt of the cold start injector pipe and remove the bolt and two gaskets from the delivery pipe.
6. Drain the fuel in the delivery pipe.
7. Install a gasket, SST, another gasket and union bolt to the delivery pipe as shown in the figure.
   - **SST 09268-45012**
8. Wipe off any splattered gasoline.
9. Reconnect the battery cable.
10. Short the terminals **Fp** and **+B** of the check connector.
    > **NOTE:** The check connector is located near the intercooler.
11. Turn on the ignition switch.
12. Measure the fuel pressure.
    - **Fuel pressure: 2.3 – 2.8 kg/cm² (33 – 40 psi, 265 – 304 kPa)** <!-- NEEDS REVIEW: the kPa figure (265–304) is inconsistent with 2.3–2.8 kg/cm² and 33–40 psi (both ≈ 226–275 kPa); page image p.265 confirms the manual itself prints "265 – 304 kPa" here, apparently copied from the 4A-GE spec — verify against another source. -->
    - If high, replace the pressure regulator.
    - If low, check the following parts: fuel hoses and connection, fuel pump, fuel filter, pressure regulator.
13. Remove the service wire from the check connector.
14. Start the engine.
15. Disconnect the vacuum sensing hose from the pressure regulator and plug it.
16. Measure the fuel pressure at idling.
    - **Fuel pressure: 2.3 – 2.8 kg/cm² (33 – 40 psi, 265 – 304 kPa)** <!-- NEEDS REVIEW: same kPa inconsistency as step 12 above; page image confirms the manual prints "265 – 304 kPa". -->
17. Reconnect the vacuum sensing hose to the pressure regulator.
18. Measure the fuel pressure at idling after 90 seconds.
    - **Fuel pressure: 1.4 – 1.9 kg/cm² (20 – 27 psi, 137 – 186 kPa)**
    - If no pressure, check the vacuum sensing hose and pressure regulator.
19. Stop the engine. Check that the fuel pressure remains above **1.5 kg/cm² (21 psi, 147 kPa)** for 5 minutes after the engine is turned off.
    - If not within specification, check the fuel pump, pressure regulator and/or injectors.
20. After checking fuel pressure, disconnect the battery ground cable and carefully remove the SST to prevent gasoline from splashing.
21. Using new gaskets, reconnect the cold start injector hose to the delivery pipe.
22. Connect the wiring connector to the cold start injector.
23. Check for fuel leakage.

<a id="p267"></a>
### Fuel Pump — Removal

> **WARNING:** Do not smoke or work near an open flame when working on the fuel pump.

1. Drain gasoline from fuel tank.
2. Remove fuel tank.
3. Remove fuel pump bracket from fuel tank.
   1. Remove the clamp bolt from the fuel tank.
   2. Remove the five bolts.
   3. Pull out the fuel pump bracket.
4. Remove fuel pump from fuel pump bracket.
   1. Remove the two nuts and disconnect the wires from the fuel pump.
   2. Pull off the lower side of the fuel pump from the bracket.
   3. Remove the fuel pump from the fuel hose.
5. Remove fuel pump filter from fuel pump.
   1. Remove the rubber cushion.
   2. Remove the clip and pull out the filter.

*Components: Fuel Hose, Fuel Pump, Fuel Pump Bracket, Fuel Pump Filter, Clip, Rubber Cushion. (Figure — see page image p.267.)*

<a id="p268"></a>
### Fuel Pump — Installation

1. Install fuel pump filter to fuel pump.
2. Install fuel pump to fuel pump bracket.
   1. Insert the outlet port of the fuel pump into the fuel hose.
   2. Install the rubber cushion to the lower side of the fuel pump.
   3. Push the lower side of the fuel pump together with the rubber cushion into the fuel pump bracket.
3. Install fuel pump bracket.
   1. Place the bracket with a new gasket on the fuel tank.
   2. Install and torque the five screws.
      - **Torque: 20 – 60 kg-cm (18 – 52 in.-lb, 2.0 – 5.8 N·m)**
   3. Install the clamp bolt to the fuel tank.
4. Install fuel tank.
   1. Apply a thin coat of oil to the flare and tighten the flare nut.
   2. Then using SST, tighten the nut to the specified torque.
      - **SST 09631-22020**
      - **Torque: 310 kg-cm (22 ft-lb, 30 N·m)**
      > **NOTE:** Use a torque wrench with a fulcrum length of 30 cm (11.81 in.). Because of the SST offset, the torque wrench itself should read **350 kg-cm (25 ft-lb, 34 N·m)** at this fulcrum length (as shown in the figure) to achieve the specified 310 kg-cm at the union.
      > **CAUTION:**
      > - Tighten the fuel tank mounting bolts, etc. to the specified torque.
      > - Push in the pipe and insert-type hose to the specified position, and install the clip to the specified location.
      > - If reusing the hose, reinstall the clip to the original location.
5. Refill gasoline.

*Pipe/hose clip fit dimensions: pipe-to-clip 2 – 7 mm (0.08 – 0.28 in.); hose end 0 – 3 mm (0 – 0.12 in.). (Figure — see page image p.268.)*

<a id="p269"></a>
### Cold Start Injector

*Wiring: solenoid coil fed from ignition switch (AM2 / ST2) through fuse AM2 7.5A, start switch, starter relay, and — for M/T, the clutch switch; for A/T, neutral start switch. (Figure — see page image p.271.)*

#### On-vehicle inspection — Measure resistance of cold start injector

1. Disconnect the cold start injector connector.
2. Using an ohmmeter, check the resistance of the injector.

| Engine | Resistance |
| ------ | ---------- |
| 4A-GE  | 3 – 5 Ω    |
| 4A-GZE | 2 – 4 Ω    |

3. Connect the cold start injector connector.

#### Removal of cold start injector

1. Disconnect cable from negative terminal of battery.
2. Disconnect cold start injector connector.
3. Remove cold start injector pipe.
   1. Put a suitable container or shop towel under the cold start injector pipe.
   2. Remove the two union bolts and the cold start injector pipe with the gaskets.
      > **NOTE:** Slowly loosen the union bolts.
4. Remove cold start injector.
   - Remove the two bolts and cold start injector with the gasket.

#### Inspection of cold start injector — Check injection

1. Install the gasket, SST (two unions), another gasket and two union bolts to the delivery pipe and injector.
   - **SST 09268-41045**
2. Connect the SST (hose) from the unions.
3. Connect the SST (wire) to the injector.
   - **SST 09842-30050**
   > **WARNING:** Position the injector as far away from the battery as possible.
4. Put a container under the injector.
5. Turn the ignition switch ON.
   > **NOTE:** Do not start the engine.
6. Short terminals **Fp** and **+B** of the check connector with a service wire.
7. Connect the test probes of the SST to the battery and check that the fuel spray is as shown.
   - **SST 09842-30050**
   > **CAUTION:** Perform this check within the shortest possible time.
8. Disconnect the test probes from the battery and check that there is less than one drop of fuel per minute from the injector.
9. After checking, remove SST and restore the following parts to their original condition:
   - Fuel pump check connector
   - Ignition switch OFF
   - Cold start injector
   - Injector wiring

#### Installation of cold start injector (4A-GE)

1. Install cold start injector.
   - Place on a new gasket and install the cold start injector with the two bolts.
   - **Torque: 75 kg-cm (65 in.-lb, 7.4 N·m)**
2. Install cold start injector pipe.
   - Using new gaskets, connect the cold start injector pipe to the delivery pipe and cold start injector. Install the union bolts.
   - **Torque: 180 kg-cm (13 ft-lb, 18 N·m)**
3. Connect cold start injector connector.
4. Connect cable to negative terminal of battery.
5. Check for fuel leakage.

<a id="p274"></a>
### Pressure Regulator (4A-GE)

*Ports: FROM DELIVERY PIPE; TO RETURN PIPE. (Figure — see page image p.278.)*

- **On-vehicle inspection — Check fuel pressure:** See [Fuel System — Check Fuel Pressure (4A-GE)](#2-check-fuel-pressure), manual page Fl-40 (in [Part 1](05a-efi-system-and-emission-control-part-1.md)).

#### Removal of pressure regulator

1. Disconnect vacuum sensing hose from pressure regulator.
2. Disconnect fuel pipe from pressure regulator.
   1. Put a suitable container or shop towel under the pressure regulator.
   2. Remove the flare nut and fuel pipe.
3. Remove pressure regulator.
   - Remove the two bolts and pull out the pressure regulator from the delivery pipe.

#### Installation of pressure regulator

1. Install pressure regulator.
   - Install a new O-ring and the pressure regulator, and torque the two bolts.
   - **Torque: 75 kg-cm (65 in.-lb, 7.4 N·m)**
2. Connect fuel pipe.
   - **Torque: 300 kg-cm (22 ft-lb, 29 N·m)**
3. Connect vacuum sensing hose.
4. Check for fuel leakage (see manual page Fl-8, in [Part 1](05a-efi-system-and-emission-control-part-1.md)).

<a id="p275"></a>
### Pressure Regulator (4A-GZE)

*Ports: FROM DELIVERY PIPE; TO RETURN PIPE. (Figure — see page image p.279.)*

- **On-vehicle inspection — Check fuel pressure:** See [Fuel Pressure — On-Vehicle Inspection (4A-GZE)](#fuel-pump-and-fuel-pressure-on-vehicle-inspection-4a-gze), manual page Fl-65.

#### Removal of pressure regulator

1. Disconnect vacuum sensing hose from pressure regulator.
2. Disconnect fuel pipe from pressure regulator.
   1. Put a suitable container or shop towel under the pressure regulator.
   2. Remove the union bolt, two gaskets and disconnect the fuel pipe.
3. Remove pressure regulator.
   - Remove the two bolts and pull out the pressure regulator from the delivery pipe.

#### Installation of pressure regulator

1. Install pressure regulator.
   - Install a new O-ring and the pressure regulator, and torque the two bolts.
   - **Torque: 75 kg-cm (65 in.-lb, 7.4 N·m)**
2. Connect fuel hose.
   - Install two new gaskets, fuel hose and union bolt.
   - **Torque: 150 kg-cm (11 ft-lb, 15 N·m)**
3. Connect vacuum sensing hose.
4. Check for fuel leakage (see manual page Fl-8, in [Part 1](05a-efi-system-and-emission-control-part-1.md)).

<a id="p276"></a>
### Injector

#### On-vehicle inspection

**1. Check injector operation** — check the operating sound from each injector.

1. With the engine running or cranking, use a sound scope to check that there is normal operating noise in proportion to engine rpm.
2. If you have no sound scope, you can check the injector transmission operation with your finger.

If no sound or an unusual sound is heard, check the wiring connector, injector, resistor or injection signal from the computer.

**2. Measure resistance of injector**

1. Disconnect the injector connector.
2. Using an ohmmeter, check the resistance of both terminals.

| Engine | Resistance    |
| ------ | ------------- |
| 4A-GE  | Approx. 13.8 Ω |
| 4A-GZE | Approx. 2.9 Ω |

#### Removal of injector (4A-GE)

1. Disconnect cable from negative terminal of battery.
2. Disconnect the following hoses:
   1. PCV hose from cylinder head cover.
   2. Vacuum sensing hose from pressure regulator.
3. Remove pressure regulator (see [Pressure Regulator (4A-GE)](#pressure-regulator-4a-ge), manual page Fl-78).
4. Remove cold start injection pipe (see step 3 of [Removal of cold start injector](#removal-of-cold-start-injector), manual page Fl-74).
5. Disconnect fuel pipe.
   1. Remove the inlet pipe mounting bolt.
   2. Remove the union bolt, two gaskets and fuel pipe.
6. Disconnect injector connectors.
7. Remove delivery pipe.
   1. Remove the three bolts, and then remove the delivery pipe with the injectors.
      > **NOTE:** When removing the delivery pipe, be careful not to drop the injectors.
   2. Remove the four insulators and three collars from the cylinder head.
8. Remove injectors.
   - Pull out the injectors from the delivery pipe.

#### Removal of injector (4A-GZE)

1. Disconnect cable from negative terminal of battery.
2. Remove throttle body (see [Throttle Body — Removal (4A-GZE)](#removal-of-throttle-body), manual page Fl-99).
3. Disconnect cold start injector pipe.
   1. Disconnect the cold start injector connector.
   2. Remove the union bolt and two gaskets, and disconnect the fuel pipe.
4. Loosen air outlet duct.
   - Loosen the two bolts, two nuts of air outlet duct.
5. Remove accelerator cable bracket.
6. Disconnect injector connectors.
7. Disconnect fuel return pipe.
   1. Remove the clamp bolt, union bolt and two gaskets, and disconnect the fuel pipe.
   2. Disconnect the vacuum hose from pressure regulator.
8. Disconnect EGR vacuum hose from modulator.
9. Remove vacuum pipe.
   - Remove the three clamp bolts and vacuum pipe.
10. Remove pressure regulator (see [Pressure Regulator (4A-GZE)](#pressure-regulator-4a-gze), manual page Fl-79).
11. Remove fuel inlet pipe.
    1. Remove the clamp bolt.
    2. Remove the pulsation damper and two gaskets, and disconnect the fuel inlet pipe from the delivery pipe.
12. Remove delivery pipe.
    1. Remove the three bolts, and then remove the delivery pipe with the injectors.
       > **NOTE:** When removing the delivery pipe, be careful not to drop the injectors.
    2. Remove the four insulators and three collars from the cylinder head.
13. Remove injectors.
    - Pull out the injectors from the delivery pipe.
    > **CAUTION:** When replacing the injector, replace it with one having the same-colored painted mark. Colors: blue, yellow, black, white.

> Steps 8–13 above are numbered 8, 9, 10, 8, 9, 10 across two pages in the source (manual pages Fl-82 and Fl-83); renumbered here as a single continuous sequence.

#### Inspection of injector (4A-GE) — Test injection of injectors

> **WARNING:** Keep clear of sparks during the test.

1. Disconnect the fuel hose from the fuel filter outlet.
2. Connect SST (union) to the fuel filter outlet.
   - **SST 09268-41045**
   > **NOTE:** Use the vehicle's fuel filter.
3. Install SST (union) to the removed pressure regulator.
   - **SST 09268-41045**
4. Install SST (union) to the injector and hold the injector and union with SST (clamp).
   - **SST 09268-41045**
5. Put the injector into the graduated cylinder.
   > **NOTE:** Install a suitable vinyl tube onto the injector to prevent gasoline from splashing out.
6. Connect the battery cable.
7. Turn the ignition switch ON.
   > **NOTE:** Do not start the engine.
8. Using a service wire, short terminals **Fp** and **+B** of the check connector.
   > **NOTE:** The fuel pump will operate. The check connector is located near the resonator.
9. Connect SST (resistor wire) to the injector and battery for 15 seconds and measure the injection volume with a graduated cylinder. Test each injector two or three times. If not within specified volume, replace the injector.
   - **SST 09842-30070**
   - **Volume: 45 – 55 cc/15 sec. (2.7 – 3.4 cu in.)**
   - **Difference between each injector: Less than 5 cc (0.3 cu in.)**

**Check leakage**

1. In the condition above, disconnect SST from the battery and check for fuel leakage from the injector nozzle.
   - **SST 09842-30070**
   - **Fuel drop: Less than one fuel drop of fuel per minute**
2. Disconnect the battery cable.
3. Remove the SST and disconnect the service wire from the terminals **Fp** and **+B**.
   - **SST 09268-41045**

#### Inspection of injector (4A-GZE) — Test injection of injectors

> **WARNING:** Keep clear of sparks during the test.

1. Disconnect the fuel hose from the fuel filter outlet.
2. Connect SST (union) to the fuel filter outlet.
   - **SST 09268-41045**
   > **NOTE:** Use the vehicle's fuel filter.
3. Install SST (union) to the removed pressure regulator.
   - **SST 09268-41045**
4. Install SST (union) to the injector and hold the injector and union with SST (clamp).
   - **SST 09268-41045**
5. Put the injector into the graduated cylinder.
   > **NOTE:** Install a suitable vinyl tube onto the injector to prevent gasoline from splashing out.
6. Connect the battery cable.
7. Turn the ignition switch ON.
   > **NOTE:** Do not start the engine.
8. Using a service wire, short terminals **Fp** and **+B** of the check connector.
   > **NOTE:** The fuel pump will operate. The check connector is located near the intercooler.
9. Connect SST (resistor wire) to the injector and battery for 15 seconds and measure the injection volume with a graduated cylinder. Test each injector two or three times. If not within specified volume, replace the injector.
   - **SST 09842-30060**
   - **Volume: 80 – 100 cc/15 sec. (4.9 – 6.1 cu in.)**
   - **Difference between each injector: Less than 5 cc (0.3 cu in.)**

**Check leakage**

1. In the condition above, disconnect SST from the battery and check for fuel leakage from the injector nozzle.
   - **SST 09842-30060**
   - **Fuel drop: Less than one fuel drop of fuel per minute**
2. Disconnect the battery cable.
3. Remove the SST and disconnect the service wire from the terminals **Fp** and **+B**.
   - **SST 09268-41045**

#### Installation of injectors (4A-GE)

1. Install injectors into delivery pipe.
   1. Replace the O-ring onto the injector.
   2. Apply a thin coat of gasoline to the O-rings and install the injectors into the delivery pipe.
   3. Make sure that the injectors rotate smoothly.
      > **NOTE:** If the injectors do not rotate smoothly, the probable cause is incorrect installation of O-rings. Replace the O-rings.
2. Install delivery pipe with injectors.
   1. Install the four insulators into the injector hole of the cylinder head.
   2. Install the three collars on the delivery pipe mounting hole of the cylinder head.
   3. Place the injectors together with the delivery pipe on the cylinder head.
   4. Make sure that the injectors rotate smoothly.
   5. Install the three thinner spacers and bolts. Torque the bolts.
      - **Torque: 175 kg-cm (13 ft-lb, 17 N·m)** <!-- NEEDS REVIEW: OCR read "176"; page image p.285 clearly shows "175" — corrected from image. -->
3. Connect injector connectors.
4. Connect fuel inlet pipe.
   1. Place the fuel inlet pipe with two new gaskets on the delivery pipe.
   2. Install and torque the union bolt.
      - **Torque: 300 kg-cm (22 ft-lb, 29 N·m)**
5. Install cold start injection pipe (see step 3 of [Installation of cold start injector](#installation-of-cold-start-injector-4a-ge), manual page Fl-74).
6. Install pressure regulator (see [Pressure Regulator (4A-GE)](#pressure-regulator-4a-ge), manual page Fl-78).
7. Connect the following hoses:
   1. PCV hose to the cylinder head cover.
   2. Vacuum sensing hose to the pressure regulator.
8. Connect cable to negative terminal of battery.
9. Check for fuel leakage (see manual page Fl-8, in [Part 1](05a-efi-system-and-emission-control-part-1.md)).

> The source numbers the last four steps 6, 6, 7, 8, 9 (a duplicated "6"); renumbered here 5–9.

#### Installation of injectors (4A-GZE)

1. Install injectors into delivery pipe.
   1. Replace the O-ring onto the injector.
   2. Apply a thin coat of gasoline to the O-rings and install the injectors into the delivery pipe.
   3. Make sure that the injectors rotate smoothly.
      > **NOTE:** If the injectors do not rotate smoothly, the probable cause is incorrect installation of O-rings. Replace the O-rings.
2. Install delivery pipe with injectors.
   1. Install the four insulators into the injector hole of the cylinder head.
   2. Install the three collars on the delivery pipe mounting hole of the cylinder head.
   3. Place the injectors together with the delivery pipe on the cylinder head.
   4. Make sure that the injectors rotate smoothly.
   5. Install the three thinner spacers and bolts. Torque the bolts.
      - **Torque: 175 kg-cm (13 ft-lb, 17 N·m)**
3. Install fuel inlet pipe.
   1. Place the fuel pipe with two new gaskets on the delivery pipe.
   2. Install and torque the union bolt.
      - **Torque: 300 kg-cm (22 ft-lb, 29 N·m)**
   3. Install the clamp bolt.
4. Install pressure regulator (see [Pressure Regulator (4A-GZE)](#pressure-regulator-4a-gze), manual page Fl-79).
5. Install vacuum pipe.
   - Install the vacuum pipe and three clamp bolts.
6. Connect EGR vacuum hose to modulator.
7. Connect fuel return pipe.
   1. Connect the vacuum hose to the pressure regulator.
   2. Place the fuel pipe with two new gaskets on the pressure regulator.
   3. Install and torque the union bolt.
   4. Install the clamp bolt.
8. Connect injector connectors.
9. Install accelerator cable bracket.
10. Install air outlet duct.
    - Tighten the two bolts and two nuts of air outlet duct.
    - **Torque: 100 kg-cm (7 ft-lb, 10 N·m)**
11. Connect cold start injector pipe.
    1. Place the fuel pipe and two new gaskets.
    2. Install and torque the union bolt.
       - **Torque: 150 kg-cm (11 ft-lb, 15 N·m)**
    3. Connect the cold start injector connector.
12. Install throttle body (see [Throttle Body — Installation (4A-GZE)](#installation-of-throttle-body), manual page Fl-104).
13. Connect cable to negative terminal of battery.

<a id="p289"></a>
### Fuel Tank and Line

#### Components — specified torque

Torque values shown in `kg-cm (ft-lb, N·m)`, read from the components diagram (page image p.289):

| Fastener | Torque |
| -------- | ------ |
| Fuel pump (to bracket) | 35 (30 in.-lb, 3.4) |
| Fuel sender gauge | 15 (13 in.-lb, 1.3) |
| No. 1 Fuel Tank Cushion | 130 (9, 13) |
| No. 3 Fuel Tank Cushion | 35 (30 in.-lb, 3.4) |
| No. 1 Left / No. 2 Right Fuel Tank Band | 140 (10, 14) |
| No. 2 Left Fuel Tank Band | 145 (10, 14) |
| No. 1 Left Fuel Tank Band (specified torque) | 195 (14, 19) |

*Components include: Fuel Pump, Fuel Sender Gauge, No. 1/No. 2/No. 3 Fuel Tank Cushions, Fuel Evaporative Separator, Fuel Tank Cap, Fuel Tank Inlet Pipe, Fuel Tank Bands (No. 1/No. 2, Left/Right), gaskets (non-reusable). (Figure — see page image p.289.)*

#### Precautions

1. Always use new gaskets when replacing the fuel tank or component part.
2. When re-installing, be sure to include the rubber protectors on the upper surfaces of the fuel tank and tank band.
3. Apply the proper torque to all parts tightened.

#### Inspect fuel lines and connections

1. Inspect the fuel lines for cracks or leakage, and all connections for deformation.
2. Inspect the fuel tank vapor vent system hoses and connections for looseness, kinks or damage.
3. Inspect the fuel tank for deformation, cracks, fuel leakage or tank band looseness.
4. Inspect the filler neck for damage or fuel leakage.
5. Hose and tube connections are as shown in the illustration.

If a problem is found, repair or replace the parts as necessary.

*Pipe/hose clip fit dimensions: pipe-to-clip 2 – 7 mm (0.08 – 0.28 in.); hose end 0 – 3 mm (0 – 0.12 in.).*

---

<a id="p290"></a>
## Air Induction System

<a id="p290"></a>
### Air Flow Meter

*Internal parts: Potentiometer, Damping Chamber, Compensation Plate, Return Spring, Air Temp. Sensor, Measuring Plate, Air By-pass Passage. (Figure — see page image p.290.)*

#### On-vehicle inspection — Measure resistance of air flow meter

1. Disconnect the wiring connector from the air flow meter.
2. Using an ohmmeter, measure the resistance between each terminal.

| Terminals | 4A-GE (Resistance) | 4A-GZE (Resistance) | Temperature |
| --------- | ------------------ | ------------------- | ----------- |
| E2 – Vs   | 20 – 3,000 Ω       | 20 – 1,200 Ω        | — |
| E2 – Vc   | 100 – 300 Ω        | 200 – 400 Ω         | — |
| E2 – VB   | 200 – 400 Ω        | —                   | — |
| E2 – THA  | 10 – 20 kΩ         | —                   | −20°C (−4°F) |
| E2 – THA  | 4 – 7 kΩ           | —                   | 0°C (32°F) |
| E2 – THA  | 2 – 3 kΩ           | —                   | 20°C (68°F) |
| E2 – THA  | 0.9 – 1.3 kΩ       | —                   | 40°C (104°F) |
| E2 – THA  | 0.4 – 0.7 kΩ       | —                   | 60°C (140°F) |
| E1 – Fc   | Infinity           | —                   | — |

If not within specification, replace the air flow meter.

#### Removal of air flow meter

1. Remove resonator (4A-GE) or intercooler (4A-GZE).
2. Disconnect air flow meter connector.
3. Disconnect air cleaner hoses from air flow meter.
4. Remove air flow meter.
   - Remove the three bolts and air flow meter.

#### Inspection of air flow meter — Measure resistance of air flow meter

Using an ohmmeter, measure the resistance between each terminal by moving the measuring plate.

| Terminals | 4A-GE (Resistance) | 4A-GZE (Resistance) | Measuring plate opening |
| --------- | ------------------ | ------------------- | ----------------------- |
| E1 – Fc   | Infinity           | —                   | Fully closed |
| E1 – Fc   | Zero               | —                   | Other than closed |
| E2 – Vs   | 20 – 400 Ω         | 200 – 600 Ω         | Fully closed |
| E2 – Vs   | 20 – 3,000 Ω       | 20 – 1,200 Ω        | Fully open |

> **NOTE:** Resistance between terminals E2 and Vs will change in a wave pattern as the measuring plate slowly opens.

#### Installation of air flow meter

1. Install air flow meter.
2. Connect air cleaner hoses to air flow meter.
3. Connect air flow meter connector.
4. Install resonator (4A-GE) or intercooler (4A-GZE).

<a id="p293"></a>
### Throttle Body

*Throttle Position Sensor mounts on the throttle body (both 4A-GE and 4A-GZE). (Figure — see page image p.293.)*

#### On-vehicle check

**1. Check throttle body**

1. Check that the throttle linkage moves smoothly.
2. Check the vacuum at port "N."
   - Start the engine.
   - Check the vacuum with your finger.

**2. Check throttle position sensor** — check the resistance between the terminals.

- Unplug the connector from the sensor.
- Insert a thickness gauge between the throttle stop screw and stop lever.
- Using an ohmmeter, check the resistance between each terminal.

**4A-GE**

| Clearance between lever and stop screw | Between terminals | Resistance |
| -------------------------------------- | ----------------- | ---------- |
| 0 mm (0 in.)                           | VTA – E2          | 0.2 – 0.8 kΩ |
| 0.35 mm (0.0138 in.)                   | IDL – E2          | 2.3 kΩ or less |
| 0.59 mm (0.0232 in.)                   | IDL – E2          | Infinity |
| Throttle valve fully opened position   | VTA – E2          | 3.3 – 10 kΩ |
| —                                      | Vcc – E2          | 3 – 7 kΩ |

**4A-GZE**

| Clearance between lever and stop screw | Between terminals | Resistance |
| -------------------------------------- | ----------------- | ---------- |
| 0 mm (0 in.)                           | VTA – E2          | 0.2 – 0.8 kΩ |
| 0.40 mm (0.0157 in.)                   | IDL – E2          | 2.3 kΩ or less |
| 0.65 mm (0.0256 in.)                   | IDL – E2          | Infinity |
| Throttle valve fully opened position   | VTA – E2          | 3.3 – 10 kΩ |
| —                                      | Vcc – E2          | 3 – 7 kΩ |

#### Removal of throttle body

**(4A-GE)**

1. Drain coolant from throttle body.
2. Remove air cleaner hose No. 1.
3. Disconnect throttle position sensor connector.
4. Disconnect water and vacuum hoses.
5. Remove accelerator return spring.
6. Disconnect accelerator cable.
7. Remove throttle body.
   - Remove the two bolts, two nuts and the throttle body with the gasket.

**(4A-GZE)**

1. Drain coolant from throttle body.
2. Disconnect the following connectors:
   1. Throttle position sensor connector
   2. ISC valve connector
3. Disconnect the following hoses:
   1. Air cleaner hose
   2. Charcoal canister hose
   3. ABV vacuum hose
   4. PCV hose
   5. EGR vacuum hose
4. Disconnect throttle cable.
5. Disconnect throttle cable (A/T).
6. Remove intake air connector.
   - Remove the two bolts, nuts, air connector and gasket.
7. Disconnect two water by-pass hoses.
8. Remove throttle body.
   - Remove the two bolts, two nuts and the throttle body with the gasket.

#### Inspection of throttle body

**1. Clean throttle body before inspection**

1. Wash and clean the cast parts with a soft brush and carburetor cleaner.
2. Using compressed air, blow all passages and apertures in the throttle body.
   > **CAUTION:** To prevent deterioration, do not clean the throttle position sensor and dash pot.

**2. Check throttle valve** — check that there is no clearance between the throttle stop screw and throttle lever when the throttle valve is fully closed.

**3. Check throttle position sensor** — see [On-vehicle check, step 2](#on-vehicle-check) (manual page Fl-98).

**4. If necessary, adjust throttle position sensor**

1. Loosen the two screws of the sensor.
2. Insert a thickness gauge between the throttle stop screw and lever, and connect the ohmmeter to terminals **IDL** and **E2**. Gradually turn the sensor clockwise until the ohmmeter deflects, and secure the sensor with two screws.
   - **(4A-GE)** thickness gauge: **0.47 mm (0.0185 in.)**
   - **(4A-GZE)** thickness gauge: **0.53 mm (0.0209 in.)**
3. Using a thickness gauge, recheck the continuity between terminals **IDL** and **E2**.

**(4A-GE)**

| Clearance between lever and stop screw | Continuity (IDL – E2) |
| -------------------------------------- | --------------------- |
| 0.35 mm (0.0138 in.)                   | Continuity |
| 0.59 mm (0.0232 in.)                   | No continuity |

**(4A-GZE)**

| Clearance between lever and stop screw | Continuity (IDL – E2) |
| -------------------------------------- | --------------------- |
| 0.40 mm (0.0157 in.)                   | Continuity |
| 0.65 mm (0.0256 in.)                   | No continuity |

#### Disassembly of throttle body

**(4A-GE)**

1. Remove throttle position sensor.
   - Remove the two screws and sensor.
2. Remove air valve.
   - Remove the five screws, air valve, gasket and O-ring.
3. Remove dash pot.

**(4A-GZE)**

1. Remove throttle position sensor.
   - Remove the two screws and sensor.
2. Remove ISC valve.
   - Remove the four screws and ISC valve with the gasket.

#### Assembly of throttle body

**(4A-GE)**

1. Install dash pot.
2. Install air valve.
   1. Place the gasket and O-ring on the throttle body.
   2. Install the air valve with five screws.
3. Install throttle position sensor.
   1. Check that the throttle valve is fully closed.
   2. Place the sensor on the throttle body as shown in the figure.
   3. Turn the sensor clockwise, and temporarily install the two screws.
4. Adjust throttle position sensor (see step 4 of [Inspection of throttle body](#inspection-of-throttle-body), manual page Fl-100).

**(4A-GZE)**

1. Install ISC valve.
   - Install a new gasket, ISC valve and four screws.
2. Install throttle position sensor.
   1. Check that the throttle valve is fully closed.
   2. Place the sensor on the throttle body as shown in the figure.
   3. Turn the sensor clockwise, and temporarily install the two screws.
3. Adjust throttle position sensor (see step 4 of [Inspection of throttle body](#inspection-of-throttle-body), manual page Fl-100).

#### Installation of throttle body

**(4A-GE)**

1. Install throttle body.
   - Place on a new gasket and install the throttle body with two bolts and two nuts.
   - **Torque: 220 kg-cm (16 ft-lb, 22 N·m)**
2. Connect accelerator cable.
3. Install accelerator return spring.
4. Connect water and vacuum hoses.
5. Connect throttle position sensor connector.
6. Install air cleaner hose No. 1.
7. Refill with coolant.

**(4A-GZE)**

1. Install throttle body.
   - Place on a new gasket and install the throttle body with two bolts and two nuts.
   - **Torque: 220 kg-cm (16 ft-lb, 22 N·m)**
2. Connect two water by-pass hoses.
3. Install intake air connector.
   - Place on a new gasket and install with two bolts and two nuts.
   - **Torque: 100 kg-cm (7 ft-lb, 10 N·m)**
4. Connect throttle cable (A/T).
5. Connect accelerator cable.
6. Connect the following hoses:
   1. PCV hose
   2. ABV vacuum hose
   3. Charcoal canister hose
   4. Air cleaner hose
   5. EGR vacuum hose
7. Connect the following connectors:
   1. ISC valve connector
   2. Throttle position sensor connector
8. Refill with coolant.

<a id="p302"></a>
### Idle Speed Control (ISC) Valve (4A-GZE)

*Internal parts: Coil, Valve Assy, Bimetal, Valve; ports OUT / IN. (Figure — see page image p.302.)*

#### On-vehicle inspection — Inspect resistance of ISC valve

1. Disconnect the ISC valve connector.
2. Using an ohmmeter, measure the resistance between each terminal.

| Terminals   | Resistance |
| ----------- | ---------- |
| ISC1 – +B   | 16 – 17 Ω  |
| ISC2 – +B   | 16 – 17 Ω  | <!-- NEEDS REVIEW: OCR read "16 – 11 Ω"; page image p.302 clearly shows "16 – 17 Ω" — corrected from image. -->

#### Removal of ISC valve

1. Drain coolant from throttle body.
2. Disconnect ISC valve connector.
3. Disconnect two water by-pass hoses.
4. Remove ISC valve (see [Disassembly of throttle body (4A-GZE)](#disassembly-of-throttle-body), manual page Fl-102).

#### Inspect operation of ISC valve

1. Apply battery voltage: connect the positive terminal to **+B** terminal and the negative terminal to **ISC1** terminal. Check that the valve moves toward the closed position.
2. Apply battery voltage: connect the positive terminal to **+B** terminal and the negative terminal to **ISC2** terminal. Check that the valve moves toward the open position.

#### Installation of ISC valve

1. Install ISC valve (see [Assembly of throttle body (4A-GZE)](#assembly-of-throttle-body), manual page Fl-103).
2. Connect two water by-pass hoses.
3. Connect ISC valve connector.
4. Refill with coolant.

<a id="p304"></a>
### Auxiliary Air Valve (4A-GE)

*Auxiliary air valve routes coolant. (Figure — see page image p.304.)*

#### On-vehicle inspection — Check operation of auxiliary air valve

Check the engine rpm by fully screwing in the idle speed adjusting screw.

- At low temp. (coolant temp. below 80°C or 176°F): when the idle speed adjusting screw is in, the engine rpm should drop.
- After warm-up: when the idle speed adjusting screw is in, the engine rpm should drop below 600 rpm or stop.

#### Removal of auxiliary air valve

1. Remove throttle body (see [Throttle Body — Removal (4A-GE)](#removal-of-throttle-body), manual page Fl-99).
2. Remove air valve (see step 2 of [Disassembly of throttle body (4A-GE)](#disassembly-of-throttle-body), manual page Fl-102).

#### Installation of auxiliary air valve

1. Install air valve (see step 2 of [Assembly of throttle body (4A-GE)](#assembly-of-throttle-body), manual page Fl-103).
2. Install throttle body (see [Throttle Body — Installation (4A-GE)](#installation-of-throttle-body), manual page Fl-104).

---

<a id="p305"></a>
## Electronic Control System

<a id="p305"></a>
### Location of Electronic Control Parts

Parts include: EFI Main Relay, Circuit Opening Relay, Solenoid Resistor (4A-GZE). *(Figure — see page image p.305.)*

<a id="p306"></a>
### EFI Main Relay

*Circuit: battery → fusible link (1.25B) → ignition switch and fuse AM2 7.5A → main relay → ECU. (Figure — see page image p.306.)*

#### Inspection of EFI main relays

**1. Check operation of main relays** — turn the ignition switch ON. At this time an operation noise will occur from the relay.

**2. Inspect relay continuity**

1. Check that there is continuity between terminals 1 and 3.
2. Check that there is no continuity between terminals 2 and 4.
3. Check that there is no continuity between terminals 3 and 4.

If continuity is not as specified, replace the relay.

**3. Inspect relay operation**

1. Apply battery voltage across terminals 1 and 3.
2. Check that there is continuity between terminals 2 and 4.

If operation is not as specified, replace the relay.

<a id="p307"></a>
### Circuit Opening Relay

*Circuit connects: Starter Relay, ECU (STA, +B), EFI Main Relay (B), Check Connector, Fuel Pump Switch, Fuel Pump (Fp, Fc terminals). (Figure — see page image p.307.)*

#### Inspection of circuit opening relay

**1. Check circuit opening relay operation**

1. Remove the rear luggage compartment trim.
2. Remove the circuit opening relay with the wiring.
3. Using a voltmeter, check that the meter indicates voltage at terminal **FP** during engine cranking and running.

**2. Inspect relay continuity**

1. Using an ohmmeter, check that there is continuity between terminals **STA** and **E1**.
2. Check that there is continuity between terminals **B** and **Fc**.
3. Check that there is no continuity between terminals **B** and **FP**.

If continuity is not as specified, replace the relay.

**3. Inspect relay operation**

1. Apply battery voltage across terminals **STA** and **E1**.
2. Using an ohmmeter, check that there is continuity between terminals **B** and **FP**.
3. Apply battery voltage across terminals **B** and **Fc**.
4. Check that there is continuity between terminals **B** and **FP**.

If operation is not as specified, replace the relay.

<a id="p309"></a>
### Solenoid Resistor (4A-GZE) and Injector Relay

*Circuit (4A-GE and 4A-GZE): battery → fusible link (1.25B) → ignition switch / fuse AM2 7.5A → (4A-GZE) solenoid resistor → injectors (No. 10, No. 20) → ECU (E01, E02). (Figure — see page image p.309.)*

#### Inspection of solenoid resistor (4A-GZE) — Measure resistance of solenoid resistor

Using an ohmmeter, measure the resistance between **+B** and other terminals (e.g. No. 10, No. 20).

- **Resistance: 3 Ω each**

#### Inspect injector relay

> **NOTE:** The injector relay is located in the No. 2 junction block.

**Inspect relay continuity**

1. Check that there is continuity between terminals 1 and 3.
2. Check that there is no continuity between terminals 2 and 4.
3. Check that there is no continuity between terminals 3 and 4.

If continuity is not as specified, replace the relay.

**Inspect relay operation**

1. Apply battery voltage across terminals 1 and 3.
2. Check that there is continuity between terminals 2 and 4.

If operation is not as specified, replace the relay.

<a id="p311"></a>
### Start Injector Time Switch

*Circuit: Starter Relay — ECU (STA); switch has STA and STJ terminals with internal coils and a bimetal contact. (Figure — see page image p.311.)*

#### Inspection of start injector time switch — Measure resistance

1. Disconnect the connector.
2. Using an ohmmeter, measure the resistance between each terminal.

| Between terminals | Resistance (Ω) | Coolant temp. |
| ----------------- | -------------- | ------------- |
| STA – STJ         | 20 – 40        | Below 30°C (95°F) | <!-- NEEDS REVIEW: 30°C = 86°F, not 95°F; page image p.311 confirms the manual prints "Below 30°C (95°F)" and "Above 40°C (95°F)" (same °F for both temps) — likely an original-manual error. -->
| STA – STJ         | 40 – 60        | Above 40°C (95°F) | <!-- NEEDS REVIEW: 40°C = 104°F, not 95°F; see note above — page image confirms the manual prints 95°F. -->
| STA – Ground      | 20 – 80        | — |

<a id="p312"></a>
### Water Temperature Sensor

The sensor is a thermistor; resistance decreases as temperature rises.

#### Inspection of water temperature sensor — Measure resistance

1. Disconnect the connector.
2. Using an ohmmeter, measure the resistance between both terminals.

- **Resistance: Refer to chart.**

*Resistance-vs-temperature curve spans approx. 20 kΩ at −20°C (−4°F) down to below 0.2 kΩ at 120°C (248°F). (Graph — see page image p.312.)*

<a id="p313"></a>
### EGR Gas Temperature Sensor (For California)

*Thermistor sensor mounted on the EGR valve; wired to ECU terminals +B, THG, E2, E1. (Figure — see page image p.313.)*

#### Inspection of EGR gas temperature sensor

Using an ohmmeter, measure the resistance between the terminals.

| Resistance | Temperature |
| ---------- | ----------- |
| 69.40 – 88.50 kΩ | 50°C (112°F) | <!-- NEEDS REVIEW: 50°C = 122°F, not 112°F; page image p.313 confirms the manual prints "50°C (112°F)" — likely an original-manual error. -->
| 11.89 – 14.37 kΩ | 100°C (212°F) |
| 2.79 – 3.59 kΩ   | 150°C (302°F) |

If the resistance is not as specified, replace the sensor.

<a id="p314"></a>
### High Temperature Line Pressure Up System

*Uses the Air Temp. Sensor (in air flow meter), Water Temp. Sensor, a fuel pressure VSV, and the circuit opening relay (STA). (Figure — see page image p.314.)*

#### Inspection of high temperature line pressure up system

1. Inspect water temperature sensor (see [Water Temperature Sensor](#water-temperature-sensor), manual page Fl-116).
2. Inspect air temperature sensor (see [Air Flow Meter](#air-flow-meter), manual page Fl-94).
3. Inspect fuel pressure VSV.
   1. Check that air does not flow from pipe E to pipe F.
   2. Apply battery voltage across the terminals.
   3. Check that air flows from pipe E to pipe F.
   - If operation is not as specified, replace the VSV.

<a id="p315"></a>
### Idle-up System

*Circuit: battery → fusible link → VSV (idle-up) → ECU (V-ISC). (Figure — see page image p.315.)*

#### Inspection of VSV (idle-up)

**1. Measure battery voltage of VSV**

1. All accessories switched OFF.
2. Using a voltmeter, check that the meter indicates battery voltage during cranking and for ten seconds after starting.

**2. Inspect VSV operation**

1. Remove the VSV.
2. Connect the VSV terminals to the battery terminals as illustrated.
3. Blow into pipe E and check that air comes out of pipe F.
4. Disconnect the battery terminals.
5. Closed VSV.

If a problem is found, replace the VSV.

<a id="p316"></a>
### Oxygen Sensor

#### Inspection of feedback voltage (VF)

1. Warm up the engine.
2. Connect the positive (+) lead of a voltmeter to terminal **VF** of the check connector and negative (−) lead to terminal **E1**.

The manual's diagnostic flowchart (manual pages Fl-120 to Fl-121) is reproduced below as a step-table (per methodology Rule 3). Connector labels ①–④ in the original correspond to the branch targets noted in "Go to." *(Original flowchart — see page images p.316–p.317.)*

| Step | Check / Action | Result | Go to |
| ---- | -------------- | ------ | ----- |
| 1 | Warm up the oxygen sensor with the engine at 2,500 rpm for approx. 90 seconds. Short terminals T and E1 of the check connector and maintain 2,500 rpm. Check the number of times the voltmeter needle fluctuates in 10 seconds. | 8 times or more | **Normal** (end) |
| 1 | (as above) | Zero | Replace the oxygen sensor, then the ECU |
| 1 | (as above) | Less than 8 times | 2 |
| 2 | Warm up the oxygen sensor again at 2,500 rpm for approx. 90 seconds; maintain 2,500 rpm. Check the number of fluctuations in 10 seconds. | 8 times or more | 5 (connector ③) |
| 2 | (as above) | Zero | 7 (connector ④) |
| 2 | (as above) | Less than 8 times | 3 |
| 3 | Unshort terminals T and E1; maintain 2,500 rpm. Measure voltage between terminals VF and E1. | More than 0 V | Replace the oxygen sensor (connector ①) |
| 3 | (as above) | 0 V | 4 |
| 4 | Read and record diagnostic codes. | Malfunction code(s) (ex. code 21) | Repair the relevant diagnostic code |
| 4 | (as above) | Normal code and code 21 | 6 (connector ②) |
| 5 | Read and record diagnostic codes (see manual pages Fl-24 to 27, in Part 1). | Malfunction code(s) (ex. code 21) | Repair the relevant diagnostic code |
| 5 | (as above) → Normal code and code 21 → Unshort T and E1, maintain 2,500 rpm, then measure voltage VF – E1. | 0 V | 6 (connector ②) |
| 5 | (as above, VF – E1) | 5 V | 7 (connector ④) |
| 6 | Disconnect the PCV hose. Measure voltage between terminals VF and E1. | 0 V | Replace the oxygen sensor |
| 6 | (as above) | More than 0 V | **Repair (Over rich)** |
| 7 | Disconnect the water temp. sensor connector and connect a resistor of 4 – 8 kΩ (or another coded water temp. sensor). Short terminals T and E1. Warm up the oxygen sensor at 2,500 rpm for approx. 90 seconds; maintain 2,500 rpm. Measure voltage between terminals VF and E1. | 0 V | Replace the oxygen sensor |
| 7 | (as above) | 5 V | **Repair (Over lean)** |

#### Inspect heater coil resistance of oxygen sensor

Using an ohmmeter, measure the resistance between the terminals **+B** and **HT**.

- **Resistance: 5.1 – 6.3 Ω**

If the resistance is not as specified, replace the sensor.

<a id="p319"></a>
### Electronic Controlled Unit (ECU)

#### Inspection of ECU

**1. Measure voltage of ECU**

> **NOTE:** The EFI circuit can be checked by measuring the resistance and voltage at the wiring connectors of the ECU.

Check the voltages at the wiring connectors:
- Remove the rear luggage compartment trim.
- Turn the ignition switch ON.
- Measure the voltage at each terminal.

> **NOTE:**
> 1. Perform all voltage measurements with the connectors connected.
> 2. Verify that the battery voltage is 11 V or above when the ignition switch is ON.

##### Connectors of ECU (4A-GE)

*(`*1` = For A/T; `*2` = For Calif. The physical pin layout is a two-row connector diagram — see page image p.319.)*

| Symbol | Terminal |
| ------ | -------- |
| E01 | Engine ground (Power) |
| E02 | Engine ground (Power) |
| No. 10 | No. 3, 4 injector |
| No. 20 | No. 1, 2 injector |
| STA | Starter switch |
| IG | Igniter |
| VF | Service connector |
| E1 | Engine ground |
| `*1` NSW | Neutral Start Switch |
| S/TH | VSV (T-VIS) |
| FPU | VSV (FPU) |
| V-ISC | VSV (ISC) |
| W | Warning light |
| HT | Oxygen sensor heater |
| T | Service connector |
| TSW | Water temperature switch |
| IDL | Throttle position sensor |
| A/C | A/C Magnet clutch |
| IGF | Igniter |
| E2 | Sensor ground |
| G⊖ | Engine revolution sensor |
| OX | Oxygen sensor |
| G⊕ | Engine revolution sensor |
| VCC | Throttle position sensor |
| `*2` THG | EGR temperature sensor |
| VTA | Throttle position sensor |
| NE | Engine revolution sensor |
| THW | Water temp. sensor |
| `*1` L3 | ECT computer |
| `*1` ECT | ECT computer |
| `*1` L1 | ECT computer |
| `*1` L2 | ECT computer |
| VC | Air flow meter |
| E21 | Sensor ground |
| VS | Air flow meter |
| STP | Stop light switch |
| THA | Inlet air temp. sensor |
| SPD | Speedometer sensor |
| BATT | Battery |
| +B1 | EFI main relay |
| +B | EFI main relay |

##### Voltage at ECU Wiring Connectors (4A-GE)

*(`*` = For A/T)*

| Terminals | STD voltage (V) | Condition | |
| --------- | --------------- | --------- | --- |
| BATT – E1 | — (see note) | — | |
| +B – E1   | 10 – 14 | Ignition S/W ON | |
| +B1 – E1  | 10 – 14 | Ignition S/W ON | |
| IDL – E1  | 10 – 14 | Ignition S/W ON | Throttle valve open |
| VTA – E2  | 0.1 – 1.0 | Ignition S/W ON | Throttle valve fully closed |
| VTA – E2  | 4 – 5 | Ignition S/W ON | Throttle valve fully open |
| VCC – E2  | 4 – 6 | Ignition S/W ON | — |
| VC – E2   | 6 – 10 | Ignition S/W ON | — |
| VS – E2   | 2 – 5.5 | Ignition S/W ON | Measuring plate fully closed |
| VS – E2   | 6 – 9 | Ignition S/W ON | Measuring plate fully open |
| VS – E2   | 2 – 8 | Idling | — |
| THA – E2  | 1 – 3 | Ignition S/W ON | Intake air temperature 20°C (68°F) |
| THW – E2  | 0.1 – 1.0 | Ignition S/W ON | Coolant temperature 80°C (176°F) |
| STA – E1  | 6 – 14 | Ignition S/W ST position and press on the clutch pedal (M/T) | |
| No. 10 – E01 / No. 20 – E02 | 9 – 14 | Ignition S/W ON | |
| IGT – E1  | 0.7 – 1.0 | Idling | |
| T – E1    | 10 – 14 | Ignition S/W ON | Service connector T ↔ E1 not short |
| T – E1    | 0.5 or less | Ignition S/W ON | Service connector T ↔ E1 short |
| A/C – E1  | 5 – 14 | Ignition S/W ON | A/C switch ON |
| A/C – E1  | 0.5 or less | Ignition S/W ON | A/C switch OFF |
| W – E1    | 0.5 or less | Ignition S/W ON | |
| W – E1    | 9 – 14 | Engine start | |
| S/TH – E1 | 0 – 2 | Idling | |
| S/TH – E1 | 10 – 14 | More than 4,350 rpm | |
| `*` NSW – E1 | 0 | Ignition S/W ON | Shift position P or N range |
| `*` NSW – E1 | 10 – 14 | Ignition S/W ON | Ex. P or N range |
| `*` NSW – E1 | 6 – 11 | Cranking | |

> **NOTE:** The BATT – E1 standard-voltage cell is blank in the source (no value given).

##### Connectors of ECU (4A-GZE)

*(`*1` = For A/T; `*2` = For Calif. The physical pin layout is a two-row connector diagram — see page image p.321.)*

| Symbol | Terminal |
| ------ | -------- |
| E01 | Engine ground (Power) |
| E02 | Engine ground (Power) |
| RSC | ISC valve |
| RSO | ISC valve |
| STA | Starter switch |
| IGT | Igniter |
| EGR | EGR valve |
| E1 | Engine ground |
| `*1` NSW | Neutral start switch |
| SMC | Super charger relay |
| No. 10 | No. 3, 4 injector |
| No. 20 | No. 1, 2 injector |
| G⊖ | Engine revolution sensor |
| VF | Service connector |
| G1 | Engine revolution sensor |
| T | Service connector |
| G2 | Engine revolution sensor |
| VTA | Throttle position sensor |
| NE | Engine revolution sensor |
| IDL | Throttle position sensor |
| VSV3 | VSV (Air bypass) |
| HT | Oxygen sensor heater |
| IGF | Igniter |
| OX | Oxygen sensor |
| THW | Water temperature sensor |
| E2 | Sensor ground |
| R/P | Fuel control switch |
| E22 | Sensor ground |
| VSV2 | VSV (Air bleed) |
| `*1` L1 | ECT computer |
| `*1` L3 | ECT computer |
| `*1` L2 | ECT computer |
| ECT1 | ECT computer |
| TIL | Super charger indicator lamp |
| A/C | A/C Magnet clutch |
| SPD | Speedometer sensor |
| W | Warning light |
| ELS1 | Stop light |
| FPU | VSV (FPU) |
| THA | Inlet air temp. sensor |
| KNK | Knock sensor |
| VS | Air flow meter |
| VC | Air flow meter |
| `*2` THG | EGR temperature sensor |
| BATT | Battery |
| +B | EFI main relay |
| ELS2 | Accessory switch |
| +B1 | EFI main relay |

##### Voltage at ECU Wiring Connectors (4A-GZE)

*(`*` = For A/T)*

| Terminals | STD voltage (V) | Condition | |
| --------- | --------------- | --------- | --- |
| BATT – E1 | — (see note) | — | |
| +B1 – E1 / +B – E1 | 10 – 14 | Ignition S/W ON | |
| IDL – E2  | M/T 4 – 5; A/T 10 – 14 | Ignition S/W ON | Throttle valve open |
| VTA – E2  | 0.1 – 1.0 | Ignition S/W ON | Throttle valve fully closed |
| VTA – E2  | 4 – 5 | Ignition S/W ON | Throttle valve fully open |
| VC – E2   | 4 – 6 | | — |
| VS – E2   | 4 – 5 | Ignition S/W ON | Measuring plate fully closed |
| VS – E2   | 0.02 – 0.5 | Ignition S/W ON | Measuring plate fully open |
| VS – E2   | 2 – 4 | | Idling |
| THA – E2  | 1 – 3 | Ignition S/W ON | Intake air temperature 20°C (68°F) |
| THW – E2  | 0.1 – 1.0 | Ignition S/W ON | Coolant temperature 80°C (176°F) |
| STA – E1  | 6 – 14 | Ignition S/W ST position and press on the clutch pedal (M/T) | |
| No. 10 – E01 / No. 20 – E02 | 9 – 14 | Ignition S/W ON | |
| IGT – E1  | 0.7 – 1.0 | Idling | |
| T – E1    | 10 – 14 | Ignition S/W ON | Service connector T ↔ E1 not short |
| T – E1    | 0.5 or less | Ignition S/W ON | Service connector T ↔ E1 short |
| A/C – E1  | 5 – 14 | Ignition S/W ON | A/C switch ON |
| A/C – E1  | 0.5 or less | Ignition S/W ON | A/C switch OFF |
| W – E1    | 0.5 or less | Ignition S/W ON | |
| W – E1    | 9 – 14 | Engine start | |
| RSC – E1 / RSO – E1 | 9 – 14 | Ignition S/W ON | |
| `*` NSW – E1 | 0 | Ignition S/W ON | Shift position P or N range |
| `*` NSW – E1 | 10 – 14 | Ignition S/W ON | Ex. P or N range |
| `*` NSW – E1 | 6 – 11 | Cranking | |

> **NOTE:** The BATT – E1 standard-voltage cell is blank in the source (no value given).

**2. Measure resistance of ECU**

> **CAUTION:**
> 1. Do not touch the ECU terminals.
> 2. The tester probe should be inserted into the wiring connector from the wiring side.

Check the resistance between each terminal of the wiring connector:
- Remove the rear luggage compartment trim.
- Unplug the wiring connectors from the ECU.
- Measure the resistance between each terminal of the wiring connectors.

##### Resistances at ECU Wiring Connectors (4A-GE)

| Terminals | Condition | Resistance |
| --------- | --------- | ---------- |
| IDL – E2  | Throttle valve open | Infinity |
| IDL – E2  | Throttle valve fully closed | 2.3 kΩ or less |
| VTA – E2  | Throttle valve fully open | 3.3 – 10 kΩ |
| VTA – E2  | Throttle valve fully closed | 0.2 – 0.8 kΩ |
| VC – E2   | — | 100 – 300 Ω |
| VS – E2   | Measuring plate fully closed | 20 – 400 Ω |
| VS – E2   | Measuring plate fully open | 20 – 3,000 Ω |
| VCC – E2  | — | 3 – 7 kΩ |
| THA – E2  | Intake air temperature 20°C (68°F) | 2 – 3 kΩ |
| THW – E2  | Coolant temperature 80°C (176°F) | 0.2 – 0.4 kΩ |
| G⊕ – G⊖   | — | 140 – 180 Ω |

##### Resistances at ECU Wiring Connectors (4A-GZE)

| Terminals | Condition | Resistance |
| --------- | --------- | ---------- |
| IDL – E2  | Throttle valve open | Infinity |
| IDL – E2  | Throttle valve fully closed | 2.3 kΩ or less |
| VTA – E2  | Throttle valve fully open | 3.3 – 10 kΩ |
| VTA – E2  | Throttle valve fully closed | 0.2 – 0.8 kΩ |
| VS – E2   | Measuring plate fully closed | 200 – 600 Ω |
| VS – E2   | Measuring plate fully open | 20 – 1,200 Ω |
| THA – E2  | Intake air temperature 20°C (68°F) | 2 – 3 kΩ |
| THW – E2  | Coolant temperature 80°C (176°F) | 0.2 – 0.4 kΩ |
| G1 – G⊖, G2 – G⊖, NE – G⊖ | — | 140 – 180 Ω |

<a id="p324"></a>
### Fuel Cut RPM

#### Inspection of fuel cut RPM

1. Start and warm up the engine.
2. Disconnect the throttle position sensor connector from the throttle position sensor.
3. Short circuit terminals **IDL** and **E2** on the wire connector side.
4. Gradually raise the engine rpm and check that there is fluctuation between the fuel cut and fuel return points.
   > **NOTE:** The vehicle should be stopped.

- **Fuel cut rpm: 1,600 rpm (A/C OFF); 1,900 rpm (A/C ON)**
- **Fuel return rpm: 1,200 rpm (A/C OFF); 1,500 rpm (A/C ON)**

---

<a id="p325"></a>
## Cooling System

*Section code `CO`, source PDF pages 324–345.*

<a id="p325"></a>
### In this section

- [Troubleshooting](#troubleshooting) — CO-2
- [Check of Engine Coolant](#check-of-engine-coolant) — CO-2
- [Replacement of Engine Coolant](#replacement-of-engine-coolant) — CO-3
- [Water Pump](#water-pump) — CO-6
- [Thermostat](#thermostat) — CO-10
- [Radiator](#radiator) — CO-11
- [Electric Cooling Fan (Radiator)](#electric-cooling-fan-radiator) — CO-13
- [Electric Cooling Fan (Engine Compartment)](#electric-cooling-fan-engine-compartment) — CO-17

<a id="p326"></a>
### Troubleshooting

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| Engine overheats | Check coolant | Replenish coolant | CO-3 |
| | Water pump drive belt loose or missing | Adjust or replace belt | CO-9 |
| | Dirt, leaves or insects on radiator | Clean radiator | |
| | Hoses, water pump, thermostat housing, radiator, heater, core plugs or head gasket leakage | Repair as necessary | |
| | Thermostat faulty | Check thermostat | CO-10 |
| | Ignition timing retarded | Set timing | |
| | Electric cooling system faulty | Inspect electric cooling system | CO-13 |
| | Radiator hose plugged or rotted | Replace hose | |
| | Water pump faulty | Replace water pump | CO-6 |
| | Radiator plugged faulty | Check radiator | CO-11 |
| | Cylinder head or block cracked or plugged | Repair as necessary | |

> **NOTE:** The thermostat on the A series engine is equipped with a by-pass valve. Therefore, if the engine tends to overheat, removal of the thermostat will an adversely effect, cooling efficiency. *(Transcribed as printed; the sentence is grammatically garbled in the source.)*

<a id="p326"></a>
### Check of Engine Coolant

**1. Check coolant level** — the coolant level should be between the LOW and FULL lines. If low, check for leakage and add coolant up to the FULL line.

**2. Check coolant quality** — there should not be any excessive deposits of rust or scales around the radiator cap (water filler cap) or radiator filler hole, and the coolant should also be free from oil. Replace the coolant if excessively dirty.

<a id="p327"></a>
### Replacement of Engine Coolant

*Cooling circuit parts: Radiator Cap (water filler cap), Water Inlet Air Bleeder Valve, Heater Air Bleeder, Radiator Drain Cock, Radiator Pipe Drain Cock. (Figure — see page image p.327.)*

#### Drainage of engine coolant

1. Remove spare tire and luggage compartment trim.
2. Remove service hose.
3. Remove No. 1 fuel tank protector.
4. Set heater control lever to MAX HOT.
5. Remove water filler cap.
6. Drain coolant.
   1. Connect the service hose to the drain cock.
   2. Drain the coolant from the radiator and engine drain cocks.
   3. Drain the coolant from the two radiator pipe's cocks.

#### Replacement of engine coolant

1. Close drain cocks.
   - Tighten the radiator drain cock and torque the engine and radiator pipes drain cocks.
   - **Torque: Radiator pipe 170 kg-cm (12 ft-lb, 17 N·m)**
   - **Torque: Engine 130 kg-cm (9 ft-lb, 13 N·m)**
2. Connect service hoses.
   1. Connect the service hoses to the radiator and heater air bleeder valves.
   2. Suspend the opposite end of the hose connected to the radiator to the hood stay.
   3. Suspend the opposite end of the hose connected to the heater air bleeder valve to the windshield washer tube.
      > **NOTE:** Do not close-off or pinch any of the tubes.
3. Refill with coolant.
   > **NOTE:** Use a good brand of ethylene-glycol base coolant, mixed according to the manufacturer's directions.
   1. Open the water inlet, radiator and heater air bleeder valves about three turns.
   2. Pour the coolant into the water filler.
   3. When the coolant begins to come out of the engine air bleeder valve, stop pouring and close the air drain valve.
   4. Again, pour coolant into the water filler hole until it is full.
   5. Check that the coolant levels in the suspended tubes come up to the level of the water filler nozzle.
      - If the coolant level in either tube does not come up to filler nozzle level, check the tube for folds or obstructions. Repeat steps (d) and (e) above.
      - **Total capacity:**
        - **M/T with heater: 12.2 liters (12.9 US qts, 10.7 Imp. qts)**
        - **M/T others: 12.4 liters (13.1 US qts, 10.9 Imp. qts)**
        - **A/T: 12.9 liters (13.6 US qts, 11.4 Imp. qts)**
   6. Close the radiator and heater air bleeder valves.
   7. Disconnect the service hoses.
      > **NOTE:** When removing the service hoses, place a rag beneath the valve to catch any dripping coolant.
   8. Fasten the radiator cap (water filler cap) to the first stop point.
      > **NOTE:** Do not tighten the radiator cap completely (to the second stop point).
   9. Start the engine and run at fast idle for about 3 minutes, and then turn it off.
      - If the level of the radiator filler hole falls, add coolant as before. Then repeat steps (h) and (i) above.
   10. Completely tighten the radiator cap.
   11. Fill coolant into the reservoir tank up to the "FULL" mark.
4. Install No. 1 fuel tank protector.
5. Install service hose.
   > **NOTE:** Thoroughly flush out remaining coolant in hoses.
6. Start engine and check for leaks.
7. Install front luggage compartment trim and spare tire.

<a id="p330"></a>
### Water Pump

*Components: Water Pump Assembly, O-ring (non-reusable), Water Pump Pulley. (Figure — see page image p.331.)*

#### Removal of water pump

1. Drain coolant (see [Replacement of Engine Coolant](#replacement-of-engine-coolant), manual page CO-3).
2. If vehicle has air conditioning, remove compressor drive belt and idle pulley.
3. Remove alternator drive belt.
   1. Loosen the water pump pulley bolts.
   2. Loosen the lock bolt and pivot nut.
   3. Move the alternator fully right, and remove the drive belt.
4. Remove water pump pulley.
   - Remove the four bolts and pump pulley.
5. Remove water inlet pipe.
   1. Disconnect the water inlet and water by-pass hoses from the inlet pipe.
   2. Remove the two nuts and clamp bolts.
   3. Remove the water inlet pipe and O-ring.
6. Remove oil dipstick guide and dipstick.
   - Remove the mounting bolt and pull out the oil dipstick guide and dipstick.
   > **NOTE:** After pulling out the oil dipstick guide, be sure to plug the oil pump body hole.
7. Remove No. 3 and No. 2 timing belt covers and gaskets.
8. Remove water pump.
   - Remove the three bolts and water pump.
   > **CAUTION:** Be careful not to get coolant on the timing belt.

#### Installation of water pump

1. Install water pump.
   - Place the water pump O-ring on the block and install the pump with three bolts. Torque the bolts.
   - **Torque: 150 kg-cm (11 ft-lb, 15 N·m)**
2. Install No. 2 and No. 3 timing belt covers with gaskets.
3. Install oil dipstick guide and dipstick.
   1. Install a new O-ring on the oil dipstick guide.
   2. Apply small amount of engine oil to O-ring.
   3. Push in the oil dipstick guide with the O-ring.
   4. Install the mounting bolt.
4. Install inlet pipe.
   1. Install the inlet pipe and a new O-ring to the water pump with the two nuts.
   2. Install the inlet pipe clamp bolt.
   3. Connect the water inlet and water by-pass hoses to the inlet pipe.
5. Install water pump pulley and alternator drive belt.
   1. Install the water pump pulley and temporarily tighten the four bolts.
   2. Place the drive belt on each pulley and set up the drive belt.
   3. Tighten the four bolts.
6. Adjust drive belt tension.
   - Using a belt tension gauge, adjust the drive belt tension.
   - **Belt tension gauge:** Nippondenso BTG-20 (95506-00020) or Borroughs No. BT-33-73F
   - **Drive belt tension:**

     | Belt | New belt | Used belt |
     | ---- | -------- | --------- |
     | Alternator | 175 ± 5 lb | 115 ± 20 lb |
     | A/C | 160 ± 20 lb | 105 ± 10 lb |

   > **NOTE:**
   > - "New belt" refers to a belt which has been used less than 5 minutes on a running engine.
   > - "Used belt" refers to a belt which has been used on a running engine for 5 minutes or more.
   > - After installing the drive belt, check that it fits properly in the ribbed grooves.
7. Refill with coolant (see [Replacement of Engine Coolant](#replacement-of-engine-coolant), manual page CO-4).
8. Start engine and check for leaks.

<a id="p334"></a>
### Thermostat

#### Removal of thermostat

1. Drain coolant (see [Replacement of Engine Coolant](#replacement-of-engine-coolant), manual page CO-3).
2. Remove water inlet and thermostat.
   - Remove the two bolts, the water inlet and thermostat from the water inlet housing.

#### Inspection of thermostat

> **NOTE:** The thermostat is numbered according to the valve opening temperature.

1. Immerse the thermostat in water and heat the water gradually.
2. Check the valve opening temperature and valve lift. If the valve opening temperature and valve lift are not within the following specifications, replace the thermostat.
   - **Low temperature type:**
     - **Valve opening temperature: 80 – 84°C (176 – 183°F)**
     - **Valve lift: More than 8 mm (0.31 in.) at 95°C (203°F)**
3. Check that valve spring is tight when the thermostat is fully closed. Replace as necessary.

#### Installation of thermostat

1. Install thermostat and water inlet.
   - Install the water inlet on a new gasket with two bolts.
2. Refill radiator with coolant (see [Replacement of Engine Coolant](#replacement-of-engine-coolant), manual page CO-4).
3. Start engine and check for leaks.

<a id="p335"></a>
### Radiator

#### Cleaning of radiator

Using water or steam cleaner, remove any mud and dirt from the radiator core.

> **CAUTION:** If using a high pressure type cleaner, be careful not to deform radiator core fins. Keep a distance of more than **40 – 50 cm (15.75 – 19.69 in.)** between the radiator core and cleaner nozzle when the cleaner nozzle pressure is **30 – 35 kg-cm² (427 – 498 psi, 2,942 – 3,432 kPa)**.

#### Inspection of radiator

**1. Check radiator cap (water filler cap)** — using a radiator cap tester, pump the tester until the relief valve opens.
- Check that the valve opens between **0.75 kg/cm² (10.7 psi, 74 kPa)** and **1.05 kg/cm² (15 psi, 103 kPa)**.
- Check that the pressure gauge does not drop rapidly when pressure on the cap is below **0.6 kg/cm² (8.5 psi, 59 kPa)**.
- If either check is not within limits, replace the cap.

**2. Check cooling system for leaks**

1. Fill the radiator with coolant and attach a radiator cap tester.
2. Warm up the engine.
3. Pump it to **1.2 kg/cm² (17 psi, 118 kPa)**, check that pressure does not drop.

If the pressure drops, check for leaks from the hoses, pipes, radiator or water pump. If no external leaks are found, check the heater core, block and head.

#### Removal of radiator

1. Drain coolant (see [Replacement of Engine Coolant](#replacement-of-engine-coolant), manual page CO-3).
2. Remove electric cooling fan(s) (see [Electric Cooling Fan (Radiator) — Removal](#removal-of-electric-cooling-fan), manual page CO-16).
3. Disconnect temperature switch connector.
4. Disconnect two radiator hoses.
5. Remove two radiator supports and radiator.

#### Installation of radiator

1. Install radiator and support.
   - Place the radiator in installed position and install the two supports with two bolts.
   > **NOTE:** After installation, confirm that the rubber cushion (A) of the support is not depressed.
2. Connect two radiator hoses.
3. Connect temperature switch connector.
4. Install electric cooling fans (see [Electric Cooling Fan (Radiator) — Removal](#removal-of-electric-cooling-fan), manual page CO-16).
5. Refill with coolant (see [Replacement of Engine Coolant](#replacement-of-engine-coolant), manual page CO-4).
6. Start engine and check for leaks.

<a id="p337"></a>
### Electric Cooling Fan (Radiator)

*Components: Fan, Fan Motor, Fan Shroud, Temperature Switch. (Figure — see page image p.337.)*

#### On-vehicle inspection

**Low temperature [below 83°C (181°F)]**

1. Turn ignition switch ON — confirm that the fan stops.
   - If it doesn't, check the fan relay and temperature switch, and check for a separated connector or severed wire between the relay and temperature switch.
2. Disconnect temperature switch connector — confirm that the fan rotates.
   - If it doesn't, check the fan relay, fan motor, ignition relay and fuse, and check for a short circuit between the fan relay and temperature switch.
3. Connect temperature switch connector.

**High temperature [above 93°C (199°F)]**

4. Start engine.
   1. Raise the engine temperature to above 93°C (199°F).
   2. Confirm that the fan rotates.
   - If it doesn't, replace the temperature switch.

#### Inspection of electric cooling fan

**1. Inspect temperature switch**

> **NOTE:** The switch is located at the radiator right side.

1. Using an ohmmeter, check that there is no continuity when the coolant is above **93°C (199°F)**.
2. Check that there is continuity when the coolant temperature is below **83°C (181°F)**.

**2. Inspect fan main relay**

> **NOTE:** The relay is located in the No. 5 junction block of the front luggage compartment.

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

**3. Inspect No. 1 fan relay**

> **NOTE:** The relay is located in the No. 5 junction block of the front luggage compartment.

**Inspect relay continuity**

1. Using an ohmmeter, check that there is continuity between terminals 1 and 2.
2. Check that there is continuity between terminals 3 and 4.

If continuity is not as specified, replace the relay.

**Inspect relay operation**

1. Apply battery voltage across terminals 1 and 2.
2. Check that there is no continuity between terminals 3 and 4.

If operation is not as described, replace the relay.

**4. Inspect fan motor**

1. Connect the battery and ammeter to the fan motor connector.
2. Check to see that the motor rotates smoothly, and current is as follows:
   - **Current: 6.8 – 7.4 A (M/T)**
   - **Current: 8.8 – 10.8 A (A/T)**

#### Removal of electric cooling fan

1. Disconnect connector of fan motor.
2. Remove electric cooling fan.
   - Remove the five bolts and electric cooling fan.

#### Disassembly of electric cooling fan

*(See page image p.337.)*

1. Remove fan.
   - Remove the nut and fan.
2. Remove fan motor.
   - Remove the three screws and fan motor.

#### Assembly of electric cooling fan

1. Install fan motor.
   - Install the fan with the three screws.
2. Install fan.
   - Install the fan with the nut.

#### Installation of electric cooling fan

1. Install electric cooling fan(s).
2. Connect connector of fan motor.

<a id="p341"></a>
### Electric Cooling Fan (Engine Compartment)

*Components: Fan, Fan Shroud. (Figure — see page image p.341.)*

#### On-vehicle inspection

**Low temperature [below 64°C (129°F)]**

1. Turn ignition switch ON — confirm that the fan stops.
   - If it doesn't, then check the fan relay and temperature sensor, and check for a separated connector or severed wire between the relay and temperature sensor.
2. Disconnect temperature sensor connector — confirm that the fan rotates.
   - If it doesn't, then check the fan relay, fan motor, engine main relay, temperature sensor and cooling fan computer.
3. Connect temperature sensor connector.

**High temperature [above 70°C (168°F)]** <!-- NEEDS REVIEW: heading prints "above 70°C (168°F)" but step 4 below prints "above 70°C (158°F)"; 70°C = 158°F, so the heading's "168°F" appears to be an original-manual typo. Page image p.341 confirms both figures as printed. -->

4. Start engine.
   1. Raise the engine temperature to above **70°C (158°F)**.
   2. Confirm that the fan rotates.
   - If it doesn't, replace the temperature sensor.

#### Inspection of cooling fan circuit

*Circuit includes: Ignition Switch (AM1/AM2, IG1/IG2), fusible link 1.25B, fuses (GAUGE 7.5A, VENT FAN 20A, ENG 10A), Engine Main Relay, Vent Fan Relay, Cooling Fan Warning Light, Cooling Fan Motor, Temperature Sensor, Cooling Fan Computer. (Figure — see page image p.342.)*

| Terminals | Condition | Result |
| --------- | --------- | ------ |
| 1 – Body ground | — | Continuity |
| 1 – 3 | Ignition S/W ON | There is battery voltage |
| 4 – 5 | Less than 54°C (129°F) (temp. sensor) | More than 600 Ω (sensor resistance) |
| 4 – 5 | More than 70°C (158°F) (temp. sensor) | Less than 415 Ω (sensor resistance) |
| 1 – 2 | Ignition S/W ON | The cooling fan warning light lights |
| 1 – 6 | Ignition S/W ON | Fan motor runs and warning light lights |
| 1 – 6 | Ignition S/W ON and continuity 7–1 | Fan motor stops |

#### Inspection of electric cooling fan

**1. Inspect temperature sensor**

> **NOTE:** The sensor is located at the cylinder head rear plate.

Using an ohmmeter, measure the resistance of the temperature sensor.

| Temperature | Resistance |
| ----------- | ---------- |
| Less than 54°C (129°F) | More than 600 Ω |
| More than 70°C (158°F) | Less than 415 Ω |

**2. Inspect engine main relay**

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

**3. Inspect vent fan relay**

> **NOTE:** The relay is located in the No. 2 junction block of the engine compartment.

**Inspect relay continuity**

1. Using an ohmmeter, check that there is continuity between terminals 1 and 2.
2. Check that there is continuity between terminals 3 and 4.

If continuity is not as specified, replace the relay.

**Inspect relay operation**

1. Apply battery voltage across terminals 1 and 2.
2. Check that there is no continuity between terminals 3 and 4.

If operation is not as described, replace the relay.

**4. Inspect fan motor**

1. Connect the battery and ammeter to the fan motor connector.
2. Check to see that the motor rotates smoothly, and current is as follows:
   - **Current: 1.5 – 2.7 A**

#### Removal of electric cooling fan

1. Disconnect connector of fan motor.
2. Remove electric cooling fan.
   - Remove the three bolts, spacers and cooling fan.

#### Disassembly of electric cooling fan

*(See page image p.341.)*

1. Remove fan.
   - Remove the nut and fan.
2. Remove fan motor.
   - Remove the three screws and fan motor.

#### Assembly of electric cooling fan

1. Install fan motor.
   - Install the fan motor with the three screws.
2. Install fan.
   - Install the fan with nut.

#### Installation of electric cooling fan

1. Install electric cooling fan.
   - Install the cooling fan with the three bolts and spacers.
2. Connect connector of fan motor.
