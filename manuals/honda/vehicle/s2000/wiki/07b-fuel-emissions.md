# Fuel and Emissions Systems (Part B)

Reviewed transcription of PDF pages 386–476 (printed pages 11-90–11-180). This chapter continues PGM-FI troubleshooting and covers idle control, fuel supply, intake air, catalytic converter, PCV, and early EVAP diagnostics. Source-page links retain the printed diagrams for verification. The EVAP diagnostic procedure continues in Part C.

---

### Printed page 11-90

<a id="p386"></a>
Source: [PDF p.386, printed p.11-90](../page-images/p0386.png).

# DTC P0365 / P0369 / P1366 / P1367: CMP/TDC Sensor B (continued)

6. At the sensor side, measure resistance between terminals 1 and 2 of the CMP/TDC sensor B 2P connector. **1,850–2,450 Ω?** Yes: step 7. No: replace sensor B (p.6-3).
7. At the sensor side, check each terminal individually for continuity to body ground. **Continuity?** Yes: replace sensor B (p.6-3). No: step 8.
8. Reconnect the sensor B 2P connector.
9. Disconnect ECM connector C (31P).
10. Measure resistance between ECM terminals C29 (CMP2P, yellow) and C30 (CMP2M, black). **1,850–2,450 Ω?** Yes: step 11. No: repair the open or short in the faulty sensor wire(s).
11. Check continuity between ECM terminal C29 and body ground. **Continuity?** Yes: repair the short to body ground in the faulty sensor wire(s). No: substitute a known-good ECM (p.11-5) and recheck; if the symptom goes away, replace the original ECM (p.11-115).

---

### Printed page 11-91

<a id="p387"></a>
Source: [PDF p.387, printed p.11-91](../page-images/p0387.png).

# DTC P0500: VSS Circuit Malfunction

Before troubleshooting, record freeze data and review general troubleshooting information (p.11-3).

1. Reset the ECM (p.11-4).
2. Start the engine. Hold 3,000 rpm without load, in neutral, until the radiator fan comes on; then let it idle.
3. Test-drive in 2nd gear. Accelerate to 4,000 rpm, then decelerate to 1,500 rpm with the throttle fully closed for at least 5 seconds.
4. Check for DTC P0500 with a scan tool or HDS. **Indicated?** Yes: step 5. No: intermittent failure; check for poor connections or loose terminals between the VSS and ECM.
5. Turn ignition OFF.
6. Raise the vehicle.
7. Disconnect the VSS 3P connector.
8. Turn ignition ON (II).
9. Measure voltage between VSS connector terminal 1 (VCC2, yellow/blue) and body ground. **About 5 V?** Yes: step 11. No: step 10.
10. Measure voltage between ECM connector C terminal C28 and body ground. **About 5 V?** Yes: repair the open in the wire between ECM C28 and VSS. No: substitute a known-good ECM (p.11-5) and recheck; if the symptom goes away, replace the original ECM (p.11-115).

Continued on the next page.

---

### Printed page 11-92

<a id="p388"></a>
Source: [PDF p.388, printed p.11-92](../page-images/p0388.png).

# DTC P0500: VSS Circuit Malfunction (continued)

11. Measure voltage between VSS connector terminals 1 (VCC2, yellow/blue) and 3 (LG2, brown/yellow). **About 5 V?** Yes: step 12. No: repair the open in the wire between ECM B22 and VSS.
12. Turn ignition OFF.
13. Reconnect the VSS 3P connector.
14. Turn ignition ON (II).
15. Raise the rear of the vehicle securely. Hold one wheel and slowly rotate the other.
16. Measure voltage between ECM connector terminals A9 and B22. **Does voltage pulse between 0 V and about 5 V?** Yes: substitute a known-good ECM (p.11-5) and recheck; if the symptom goes away, replace the original ECM (p.11-115). No: step 17.
17. Turn ignition OFF.
18. Disconnect ECM connector A (32P).
19. Turn ignition ON (II).
20. Hold one wheel and slowly rotate the other.
21. Measure voltage between ECM connector terminals A9 (VSS, blue/white) and B22 (LG2, brown/yellow). **Does voltage pulse between 0 V and about 5 V?** Yes: substitute a known-good ECM and recheck; if the symptom goes away, replace it. No: repair the short or open between VSS and ECM; if the wire is OK, replace VSS (p.22-93).

---

### Printed page 11-93

<a id="p389"></a>
Source: [PDF p.389, printed p.11-93](../page-images/p0389.png).

# DTC P0607 / P1607: ECM Internal Circuit Malfunction

- **P0607:** 2004–2005 models.
- **P1607:** 2000–2003 models.

Before troubleshooting, record freeze data and review general troubleshooting information (p.11-3). An asterisk marks 2004–2005; a double asterisk marks 2000–2003. If No. 25 BACK UP (7.5 A) fuse is removed while ignition is ON (II), the MIL turns on and the ECM stores P0607* (P1607**).

1. Reset the ECM (p.11-4).
2. Turn ignition OFF.
3. Turn ignition ON (II).
4. Check for a temporary or stored DTC with a scan tool or HDS. **P0607* (P1607**) indicated?** Yes: substitute a known-good ECM (p.11-5) and recheck; if the symptom goes away, replace the original ECM (p.11-115). No: step 5.
5. Cycle ignition OFF and ON (II) five times.
6. Recheck for a temporary or stored DTC. **P0607* (P1607**) indicated?** Yes: inspect No. 25 BACK UP (7.5 A) fuse; if it is OK, repair the open in the VBU wire between the under-dash fuse/relay box and ECM. No: intermittent failure; a low battery may cause this. Ask whether the engine needed a recent jump-start.

---

### Printed page 11-94

<a id="p390"></a>
Source: [PDF p.390, printed p.11-94](../page-images/p0390.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)
### DTC P0630: VIN Not Programmed or Mismatch ('04-05 models)

**NOTE:**
*   Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).
*   This DTC is stored only when the ECM does not have the VIN information of the vehicle. Use the HDS to fill the missing VIN information.

1. Turn the ignition switch ON (II).
2. Check the VIN with the HDS.
   *   **Does the HDS show the vehicle's VIN?**
       *   **YES** — Go to step 5.
       *   **NO** — Go to step 3.

3. Input the VIN to the ECM with the HDS.
   *   **Does the screen show COMPLETE?**
       *   **YES** — Go to step 5.
       *   **NO** — Go to step 4.

4. Check for DTCs with the HDS.
   *   **Is DTC P0607 indicated?**
       *   **YES** — Go to the DTC P0607 troubleshooting.
       *   **NO** — Substitute a known-good ECM (see page 11-5), then recheck.

5. Clear the DTC with the HDS.
6. Turn the ignition switch OFF.
7. Turn the ignition switch ON (II), and wait 5 seconds.
8. Check for Temporary DTCs or DTCs with the HDS.
   *   **Are any Temporary DTCs or DTCs indicated?**
       *   **YES** — If DTC P0630 is indicated, substitute a known-good ECM (see page 11-5), then recheck. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.
       *   **NO** — Intermittent failure, the system is OK at this time.

---

### Printed page 11-95

<a id="p391"></a>
Source: [PDF p.391, printed p.11-95](../page-images/p0391.png).

# BARO Sensor DTC Troubleshooting

**Range/performance:** P1106 (2000–2003); P2227 (2004–2005). Before troubleshooting, record freeze data and review general troubleshooting information (p.11-3). Here * denotes 2000–2003, ** denotes 2004–2005.

1. Reset the ECM (p.11-4).
2. Start the engine. Hold 3,000 rpm without load in neutral until the radiator fan comes on, then let it idle.
3. Test-drive in 4th gear.
4. Accelerate for 5 seconds at wide-open throttle.
5. Check for temporary DTC P1106* (P2227**). **Indicated?** Yes: substitute a known-good ECM (p.11-5) and recheck; replace the original ECM (p.11-115) if the indication goes away. No: intermittent failure; the system is OK at this time.

**Circuit low/high voltage:** P1107/P1108 (2000–2003); P2228/P2229 (2004–2005). Record freeze data and review p.11-3. The same year footnotes apply.

1. Reset the ECM (p.11-4).
2. Turn ignition ON (II).
3. Check for temporary or stored P1107* (P2228**) or P1108* (P2229**). **Indicated?** Yes: substitute a known-good ECM and recheck; replace the original ECM if the indication goes away. No: intermittent failure; the system is OK at this time.

---

### Printed page 11-96

<a id="p392"></a>
Source: [PDF p.392, printed p.11-96](../page-images/p0392.png).

# DTC P1109: BARO Sensor Circuit Out of Range High (2004–2005)

Before troubleshooting, record freeze data and review general troubleshooting information (p.11-3).

1. Reset the ECM (p.11-4).
2. Start the engine.
3. Check for temporary or stored DTC P1109 with a scan tool or HDS. **Indicated?** Yes: substitute a known-good ECM (p.11-5) and recheck; if the symptom goes away, replace the original ECM (p.11-115). No: intermittent failure; the system is OK at this time.

---

### Printed page 11-97

<a id="p393"></a>
Source: [PDF p.393, printed p.11-97](../page-images/p0393.png).

# TP Sensor DTC Troubleshooting

**P1121: TP sensor signal lower than expected.** Record freeze data and review general troubleshooting information (p.11-3).

1. Turn ignition ON (II).
2. Check throttle position with a scan tool or HDS. **Is 9.4% or more indicated with the throttle fully opened?** Yes: intermittent failure; the system is OK at this time. No: replace the throttle body (p.11-165).

**P1122: TP sensor signal higher than expected.** Record freeze data and review p.11-3.

1. Turn ignition ON (II).
2. Check throttle position with a scan tool or HDS. **Is 14.1% or less indicated with the throttle fully closed?** Yes: intermittent failure; the system is OK at this time. No: replace the throttle body (p.11-165).

---

### Printed page 11-98

<a id="p394"></a>
Source: [PDF p.394, printed p.11-98](../page-images/p0394.png).

# PGM-FI System
## DTC Troubleshooting (cont'd)

### DTC P1128: MAP Sensor Signal Lower Than Expected
**NOTE:** Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).

1. Turn the ignition switch ON (**II**).
2. Check the MAP with a scan tool or the HDS.
   Is about **54.1 kPa** (**16.0 in.Hg**, **406 mmHg**), or **1.6 V** or more indicated?

- **YES**—Intermittent failure, the system is OK at this time.
- **NO**—Replace the MAP sensor (see page 11-166).

### DTC P1129: MAP Sensor Signal Higher Than Expected
**NOTE:** Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).

1. Start the engine. Hold the engine speed at **3,000 rpm** without load (in neutral) until the radiator fan comes on, then let it idle.
2. Check the MAP with a scan tool or the HDS.
   Is about **36.9 kPa** (**10.9 in.Hg**, **277 mmHg**), or **1.1 V** or less indicated?

- **YES**—Intermittent failure, the system is OK at this time.
- **NO**—Replace the MAP sensor (see page 11-166).

---

### Printed page 11-99

<a id="p395"></a>
Source: [PDF p.395, printed p.11-99](../page-images/p0395.png).

# DTC P1297: ELD Circuit Low Voltage

Before troubleshooting, record freeze data and review general troubleshooting information (p.11-3).

1. Reset the ECM (p.11-4).
2. Start the engine.
3. Turn on the headlights.
4. Check for temporary or stored P1297 with a scan tool or HDS. **Indicated?** Yes: step 5. No: intermittent failure; check for poor connections or loose terminals at ELD and ECM.
5. Turn ignition and headlights OFF.
6. Disconnect ELD 3P connector.
7. Turn ignition ON (II).
8. Measure voltage between ELD connector terminal 3 (ELD, green/red) and body ground. **About 5 V?** Yes: replace the main under-hood fuse/relay box. No: step 9.
9. Turn ignition OFF.
10. Disconnect ECM connector A (32P).
11. Check continuity between ECM terminal A30 and body ground. **Continuity?** Yes: repair the short between ECM A30 and ELD. No: substitute a known-good ECM (p.11-5) and recheck; if the symptom goes away, replace the original ECM (p.11-115).

---

### Printed page 11-100

<a id="p396"></a>
Source: [PDF p.396, printed p.11-100](../page-images/p0396.png).

# DTC P1298: ELD Circuit High Voltage

Before troubleshooting, record freeze data and review general troubleshooting information (p.11-3).

1. Reset ECM (p.11-4).
2. Start engine.
3. Turn on headlights.
4. Check for temporary or stored P1298 with scan tool or HDS. **Indicated?** Yes: step 5. No: intermittent failure; check ELD and ECM connections and terminals.
5. Turn ignition and headlights OFF.
6. Disconnect ELD 3P connector.
7. Turn ignition ON (II).
8. Measure voltage between ELD terminal 1 (IG1, black/yellow) and body ground. **Battery voltage?** Yes: step 9. No: repair the open between No. 6 ACG (15 A) fuse and ELD.
9. Turn ignition OFF.
10. Connect ELD terminal 3 (ELD, green/red) to body ground with a jumper wire.
11. Disconnect ECM connector A (32P).
12. Check continuity between ECM terminal A30 and body ground. **Continuity?** Yes: step 13 on next page. No: repair the open between ECM A30 and ELD.

---

### Printed page 11-101

<a id="p397"></a>
Source: [PDF p.397, printed p.11-101](../page-images/p0397.png).

# DTC P1298: ELD Circuit High Voltage (continued)

13. Check continuity between ELD connector terminal 2 (GND, black) and body ground. **Continuity?** Yes: step 14. No: repair the open between ELD terminal 2 and G201.
14. Reconnect ELD 3P and ECM A (32P) connectors.
15. Start engine and let it idle.
16. Measure voltage between ECM terminals A30 (ELD, green/red) and B20 (LG1, brown/yellow) while switching on low-beam headlights. **Does voltage drop?** Yes: substitute a known-good ECM (p.11-5) and recheck; if the symptom goes away, replace the original ECM (p.11-115). No: replace under-hood fuse/relay box.

---

### Printed page 11-102

<a id="p398"></a>
Source: [PDF p.398, printed p.11-102](../page-images/p0398.png).

# DTC P2195: Primary HO2S (Sensor 1) Circuit Low Voltage (2004)

Before troubleshooting, record freeze data and review general troubleshooting information (p.11-3). If the vehicle ran out of fuel and stalled before this DTC was stored, refuel and clear the DTC.

1. Reset ECM (p.11-4).
2. Hold engine at 3,000 rpm without load, in neutral, until radiator fan comes on.
3. Check primary HO2S sensor 1 output voltage during wide-open-throttle acceleration. **Stays at 0.5 V or less?** Yes: step 4. No: intermittent failure; check sensor and ECM connections.
4. Check fuel pressure (p.11-145). **Normal?** Yes: step 5. No: repair fuel supply system.
5. Turn ignition OFF.
6. Disconnect primary HO2S sensor 1 4P connector.
7. Start engine and let it idle.
8. Check sensor output voltage. **0.5 V or less?** Yes: step 9. No: replace sensor (p.11-114).
9. Turn ignition OFF.
10. Disconnect ECM connector C (31P).
11. Check continuity between sensor 4P connector terminal 1 (PHO2S, white) and body ground. **Continuity?** Yes: repair the short between ECM C16 and sensor. No: substitute a known-good ECM (p.11-5) and recheck; if the symptom goes away, replace original ECM (p.11-115).

---

### Printed page 11-103

<a id="p399"></a>
Source: [PDF p.399, printed p.11-103](../page-images/p0399.png).

# DTC P2195: Primary HO2S (Sensor 1) Circuit Low Voltage (2005)

Before troubleshooting, record freeze data and review general troubleshooting information (p.11-3). If the vehicle ran out of fuel and stalled before the DTC was stored, refuel and clear the DTC.

1. Reset ECM (p.11-4).
2. Hold engine at 3,000 rpm without load, in neutral, until radiator fan comes on.
3. Check primary HO2S sensor 1 output voltage. **Stays at 0.1–0.5 V?** Yes: step 4. No: intermittent failure; check sensor and ECM connections.
4. Check fuel pressure (p.11-145). **Normal?** Yes: step 5. No: repair fuel supply system.
5. Turn ignition OFF.
6. Disconnect primary HO2S sensor 1 4P connector.
7. Start engine and let it idle.
8. Check sensor output voltage. **Stays at 0.5 V or less?** Yes: step 9. No: replace sensor (p.11-114).
9. Turn ignition OFF.
10. Disconnect ECM connector C (31P).
11. Check continuity between sensor 4P connector terminal 1 (PHO2S, white) and body ground. **Continuity?** Yes: repair the short between ECM C16 and sensor. No: substitute a known-good ECM (p.11-5) and recheck; if the symptom goes away, replace original ECM (p.11-115).

---

### Printed page 11-104

<a id="p400"></a>
Source: [PDF p.400, printed p.11-104](../page-images/p0400.png).

# DTC P2270: Secondary HO2S (Sensor 2) Circuit Signal Stuck Lean (2004–2005)

Before troubleshooting, record freeze data and review general troubleshooting information (p.11-3).

1. Reset ECM (p.11-4).
2. Hold engine at 3,000 rpm without load, in neutral, until radiator fan comes on.
3. Test-drive in 6th gear at a steady 65 mph (105 km/h) for at least 1 minute. Decelerate with throttle fully closed for 4 seconds, then open throttle slowly and cruise at least 40 seconds.
4. Check secondary HO2S sensor 2 output voltage with scan tool or HDS. **Stays at 0.0–0.6 V?** Yes: replace sensor (p.11-114). No: intermittent failure; check sensor and ECM connections.

---

### Printed page 11-105

<a id="p401"></a>
Source: [PDF p.401, printed p.11-105](../page-images/p0401.png).

# DTC P2271 / P2297: HO2S Circuit Tests (2004–2005)

Before each test, record freeze data and review general troubleshooting information (p.11-3).

## P2271: Secondary HO2S (Sensor 2) Signal Stuck Rich

1. Reset ECM (p.11-4).
2. Hold engine at 3,000 rpm without load, in neutral, until radiator fan comes on.
3. Test-drive in 6th gear at a steady 65 mph (105 km/h) for at least 1 minute. Decelerate with throttle fully closed for 4 seconds, then open throttle slowly and cruise at least 40 seconds.
4. Check secondary sensor output. **Stays at 0.6–5.0 V?** Yes: replace sensor (p.11-114). No: intermittent failure; check sensor and ECM connections.

## P2297: Primary HO2S (Sensor 1) Circuit High Voltage

1. Reset ECM (p.11-4).
2. Hold engine at 3,000 rpm without load, in neutral, until radiator fan comes on.
3. Test-drive in 6th gear at a steady 65 mph (105 km/h) for at least 1 minute, then slow with throttle completely closed for at least 5 seconds.
4. Check primary sensor output. **Stays at 0.6–1.5 V?** Yes: replace sensor (p.11-114). No: intermittent failure; check sensor and ECM connections.

---

### Printed page 11-106

<a id="p402"></a>
Source: [PDF p.402, printed p.11-106](../page-images/p0402.png).

# MIL Circuit Troubleshooting

1. Turn ignition ON (II) and watch the malfunction indicator lamp (MIL). **Does it come on and stay on?**
   - **Yes, always:** go to step 20. If it sometimes works normally, first check for an intermittent short between ECM A10 and the DLC, or between ECM A18 and the gauge assembly.
   - **No, always off:** go to step 2. If it sometimes works normally, first check for a loose No. 5 INSTRUMENT LIGHT BACK UP LIGHT (7.5 A) fuse, No. 46 ACG S (15 A) fuse, or No. 2 FUEL PUMP SRS (15 A) fuse; poor ECM A18 connection; intermittent open in green/orange wire between ECM A18 and gauge assembly; intermittent short between ECM C19 and MAP sensor; intermittent short between ECM C28 and TP sensor, VSS, air pump electric current sensor, or FTP sensor; or faulty PGM-FI main relay.
2. Turn ignition OFF, then ON (II). **Is the low oil pressure indicator on?** Yes: step 3. No: check for a blown No. 5 INSTRUMENT LIGHT BACK UP LIGHT (7.5 A) fuse and a short or open between that fuse and the gauge assembly.
3. Try to start engine. **Does it start?** Yes: step 4. No: step 7 on next page.
4. Turn ignition OFF.
5. Ground ECM connector terminal A18 (MIL, green/orange) with a jumper wire.
6. Turn ignition ON (II). **Is MIL on?** Yes: substitute known-good ECM (p.11-5) and recheck; if symptom goes away, replace original ECM (p.11-115). No: check for an open between ECM A18 and gauge assembly, and for a blown MIL bulb.

---

### Printed page 11-107

<a id="p403"></a>
Source: [PDF p.403, printed p.11-107](../page-images/p0403.png).

# MIL Circuit Troubleshooting (continued)

7. Turn ignition OFF.
8. Inspect No. 46 ACG S (15 A) fuse in main under-hood fuse/relay box. **OK?** Yes: step 9. No: check for a short between fuse and PGM-FI main relay, or between relay and ECM, injectors, or IAC valve.
9. Inspect No. 2 FUEL PUMP SRS (15 A) fuse in under-dash fuse/relay box. **OK?** Yes: step 10. No: check for a short between fuse and PGM-FI main relay or SRS unit, a short between relay and fuel pump, or a faulty relay or fuel pump.
10. Disconnect ECM connector C (31P).
11. Check continuity from body ground to ECM terminals C19 (VCC1, yellow/red) and C28 (VCC2, yellow/blue), individually. **Continuity?** Yes: step 12. No: step 13.
12. Disconnect each 3P connector, one at a time, and repeat the ground-continuity checks at C19 and C28: MAP, VSS, FTP, TP, and air pump electrical current sensors. **Continuity?** Yes: repair the short to body ground from ECM C19 to MAP or from ECM C28 to TP, VSS, FTP, or air pump sensor. No: replace the sensor whose disconnection removed continuity to ground.
13. Disconnect injectors and IAC valve connectors. Continued on next page.

---

### Printed page 11-108

<a id="p404"></a>
Source: [PDF p.404, printed p.11-108](../page-images/p0404.png).

# MIL Circuit Troubleshooting (continued)

14. Turn ignition ON (II).
15. Measure voltage from body ground to ECM terminals B1 and B9 individually (IGP1, yellow/black). **Battery voltage?** Yes: step 16. No: check for an open between PGM-FI main relay and B1/B9, poor relay connections, or faulty relay (p.11-142); repair or replace as needed.
16. Turn ignition OFF.
17. Reconnect sensor connectors and ECM connector C (31P).
18. Turn ignition ON (II).
19. Measure voltage from body ground to ECM terminals B2, B10, B20, and B22 individually (PG1 black, LG1 brown/yellow). **Less than 1.0 V?** Yes: substitute a known-good ECM (p.11-5) and recheck; if symptom goes away, replace original ECM (p.11-115). No: repair the open in the wire(s) that measured over 1.0 V between G101 and those ECM terminals.
20. Turn ignition OFF.
21. Connect scan tool or HDS.
22. Turn ignition ON (II).
23. Check for temporary or stored DTCs. **Any indicated?** Yes: follow the indicated DTC troubleshooting. No: step 24 on next page.

---

### Printed page 11-109

<a id="p405"></a>
Source: [PDF p.405, printed p.11-109](../page-images/p0405.png).

# MIL Circuit Troubleshooting (continued)

24. Turn ignition OFF.
25. Disconnect ECM connector A (32P).
26. Check continuity from DLC terminal 7 (K-line, gray) to body ground. **Continuity?** Yes: repair the short between DLC and ECM A21. No: step 27.
27. Turn ignition ON (II).
28. Measure voltage between ECM terminal A10 (SCS, brown) and body ground. **About 5 V?** Yes: step 29. No: repair the short between DLC and ECM A10.
29. Turn ignition OFF.
30. Disconnect ECM connector A (32P).
31. Turn ignition ON (II). **Is MIL on?** Yes: repair the short between gauge assembly and ECM A18. No: substitute a known-good ECM (p.11-5) and recheck; if symptom goes away, replace original ECM (p.11-115).

---

### Printed page 11-110

<a id="p406"></a>
Source: [PDF p.406, printed p.11-110](../page-images/p0406.png).

# DLC Circuit Troubleshooting

Use when ECM does not communicate with a scan tool, HDS, or I/M test equipment.

1. Measure voltage between DLC terminal 16 (+B, white/green) and body ground. **Battery voltage?** Yes: step 2. No: repair open between DLC and ACG S (15 A) fuse in under-hood fuse/relay box.
2. Measure voltage between DLC terminals 4 (PG, black) and 16. **Battery voltage?** Yes: step 3. No: repair open between DLC ground and G401.
3. Measure voltage between DLC terminals 5 (LG2, brown) and 16. **Battery voltage?** Yes: step 4. No: repair open between DLC ground and G101.
4. Turn ignition ON (II).
5. Measure voltage between DLC terminals 5 and 7 (K-line, gray). **8.5 V or more?** Yes: step 10. No: step 6.
6. Turn ignition OFF. Continued on next page.

**Source ambiguity:** In the repair instructions for steps 1–3, the printed manual names “DLC terminal No. 8,” although the measurement instructions and connector drawings identify terminals 16, 4, and 5. Verify the circuit before repair.

---

### Printed page 11-111

<a id="p407"></a>
Source: [PDF p.407, printed p.11-111](../page-images/p0407.png).

# DLC Circuit Troubleshooting (continued)

7. Disconnect ECM connector A (32P), with scan tool/HDS disconnected from DLC.
8. Check continuity between DLC terminal 7 (K-line, gray) and body ground. **Continuity?** Yes: repair short to ground in K-line between DLC and ECM A21; then check DTCs and follow indicated troubleshooting. No: step 9.
9. Check continuity between DLC terminal 7 and ECM A21. **Continuity?** Yes: substitute a known-good ECM (p.11-5) and recheck; if symptom goes away, replace original ECM (p.11-115). No: repair open between DLC 7 and ECM A21; then check DTCs and follow indicated troubleshooting.
10. Turn ignition OFF.
11. Disconnect ECM connector A (32P), with scan tool/HDS disconnected from DLC.
12. Turn ignition ON (II).
13. Measure voltage between DLC terminals 5 and 7. **0 V?** Yes: substitute a known-good ECM and recheck; if symptom goes away, replace original ECM. No: repair short to power between DLC 7 and ECM A21; then check DTCs and follow indicated troubleshooting.

**Source ambiguity:** Step 8's yes branch says “DLC terminal No. 15,” while its instruction and diagram say terminal 7. The discrepancy is retained here for technician verification.

---

### Printed page 11-112

<a id="p408"></a>
Source: [PDF p.408, printed p.11-112](../page-images/p0408.png).

# Injector Replacement: Removal

1. Relieve fuel pressure (p.11-145).
2. Remove fuel rail cover (A); disconnect injector connectors (B).
3. Disconnect vacuum and fuel return hoses from fuel pressure regulator (C). Cover hoses with rag or shop towel before disconnecting.
4. Disconnect fuel hose (D) from fuel rail (E); remove vacuum lines (F).
5. Remove retainer nuts (G) and bolts (H) from fuel rail and harness holder (I). Diagram calls for **12 N·m (1.2 kgf·m, 8.7 lbf·ft)** at G and H during installation.
6. Disconnect PCV valve (J).
7. Disconnect fuel rail.
8. Remove injectors from intake manifold (K).

The source diagram identifies components A–K and the two 12 N·m fastener locations; see linked page image.

---

### Printed page 11-113

<a id="p409"></a>
Source: [PDF p.409, printed p.11-113](../page-images/p0409.png).

# Injector Replacement: Installation

9. Slide new cushion rings (A) onto injectors (B).
10. Coat new O-rings (C) with clean engine oil and install on injectors.
11. Insert injectors into fuel rail (D).
12. Coat new seal rings (E) with clean engine oil and press into intake manifold.
13. Install injectors in intake manifold.
14. Install and tighten retainer nuts. See the 12 N·m fastener locations on the preceding page.
15. Connect fuel hose to fuel rail with new washers.
16. Connect vacuum hoses and fuel return hose to fuel pressure regulator.
17. Connect PCV valve.
18. Turn ignition ON (II) without cranking. After fuel pump runs about 2 seconds, repeat 2–3 times, then check for fuel leaks.

---

### Printed page 11-114

<a id="p410"></a>
Source: [PDF p.410, printed p.11-114](../page-images/p0410.png).

# HO2S Replacement

## Primary HO2S (Sensor 1)

1. Disconnect its 4P connector (A).
2. Remove the sensor (A). **Installation torque: 44 N·m (4.5 kgf·m, 33 lbf·ft).**
3. Install parts in reverse order.

## Secondary HO2S (Sensor 2)

1. Disconnect its 4P connector (A).
2. Remove the sensor (A). **Installation torque: 44 N·m (4.5 kgf·m, 33 lbf·ft).**
3. Install parts in reverse order.

The linked source page shows connector and sensor locations for each procedure.

---

### Printed page 11-115

<a id="p411"></a>
Source: [PDF p.411, printed p.11-115](../page-images/p0411.png).

# ECM Replacement

1. Turn the ignition switch OFF.
2. Disconnect the negative cable from the battery.
3. Remove the left side kick panel (A) to expose the ECM (B).
4. Remove the two bolts from the ECM.
5. Disconnect the ECM connectors.
6. Install the ECM in the reverse order of removal.
7. Connect the HDS to the DLC (A) located under the passenger's side of dashboard ('00-01 models) or behind the driver's side of the front console ('02-05 models).

| | '00-01 models | '02-05 models |
|---|---|---|
| DLC Location | Under passenger's side of dashboard | Behind driver's side of front console |

8. Turn the ignition switch ON (II).

> **NOTE:** If DTC P0630 "VIN Not Programmed or Mismatch" is stored at this time, ignore it and continue this procedure ('04-05 models).

9. Input the VIN to the ECM with the HDS.
10. Rewrite the immobilizer code with the ECM replacement procedure in the HDS; it allows you to start the engine.
11. Reset the ECM with the HDS.
12. Do the ECM idle learn procedure (see page 11-140).

---

### Printed page 11-116

<a id="p412"></a>
Source: [PDF p.412, printed p.11-116](../page-images/p0412.png).

# VTEC Component Location Index

The source diagram locates the **rocker arm oil control solenoid (VTEC solenoid valve)** and **rocker arm oil pressure switch (VTEC oil pressure switch)** together near the rear of the engine. Solenoid inspection is on p.11-126. See the linked source image for precise location.

---

### Printed page 11-117

<a id="p413"></a>
Source: [PDF p.413, printed p.11-117](../page-images/p0413.png).

# DTC Troubleshooting
## DTC P1259: VTEC System Malfunction
### ('00-03 models)

**Special Tools Required**
*   Pressure gauge adapter 07NAJ-P07010A
*   A/T low pressure gauge w/panel 07406-0070301
*   A/T pressure hose 07406-0020201
*   A/T pressure hose, 2,210 mm 07MAJ-PY4011A
*   A/T pressure hose, adapter 07MAJ-PY40120

> **NOTE:** Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).

1.  Reset the engine control module (ECM) (see page 11-4).
2.  Check the engine oil level, and refill if necessary.
3.  Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on.
4.  Road test the vehicle:
    *   Accelerate in 1st gear to an engine speed over 6,000 rpm.
    *   Hold that engine speed for at least 2 seconds.
    *   If DTC P1259 is not repeated during the first road test, repeat this test two more times.

**Is DTC P1259 Indicated?**
*   **Y E S** — G o to step 5.
*   **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose wires at the rocker arm oil control solenoid (VTEC solenoid valve), the rocker arm oil pressure switch (VTEC oil pressure switch), and the ECM.

5.  Turn the ignition switch OFF.
6.  Disconnect the rocker arm oil pressure switch (VTEC oil pressure switch) 2P connector.
7.  At the switch side, check for continuity on the rocker arm oil pressure switch (VTEC oil pressure switch) between rocker arm oil pressure switch (VTEC oil pressure switch) 2P connector terminals No. 1 and No. 2.

> **R O C K E R A R M O I L P R E S S U R E S W I T C H**
> **(VTEC OIL P R E S S U R E SWITCH) 2P C O N N E C T O R**
> Terminal side of male terminals

**Is there continuity?**
*   **Y E S** — G o to step 8.
*   **NO** — Replace the rocker arm oil pressure switch (VTEC oil pressure switch). •

8.  Turn the ignition switch ON (II).
9.  Measure the voltage between the rocker arm oil pressure switch (VTEC oil pressure switch) harness 2P connector terminal No. 1 and body ground.

> **R O C K E R A R M O I L P R E S S U R E SWITCH**
> **(VTEC OIL P R E S S U R E SWITCH) 2P C O N N E C T O R**
> Wire side of female terminals

**Is there battery voltage?**
*   **Y E S** — G o to step 14.
*   **NO** — Go to step 10.

---

### Printed page 11-118

<a id="p414"></a>
Source: [PDF p.414, printed p.11-118](../page-images/p0414.png).

# DTC P1259: VTEC System Malfunction (continued)

10. Measure voltage between ECM terminal C10 (VTM, blue/black) and body ground. **Battery voltage?** Yes: repair open between rocker arm oil pressure switch and ECM. No: step 11.
11. Turn ignition OFF.
12. Disconnect ECM connector C (31P).
13. Check continuity between ECM terminal C10 and body ground. **Continuity?** Yes: repair short between rocker arm oil pressure switch and ECM. No: substitute a known-good ECM (p.11-5); replace original ECM (p.11-115) if symptom goes away.
14. Measure voltage between rocker arm oil pressure switch 2P connector terminals 1 and 2. **Battery voltage?** Yes: step 15. No: repair open between switch and G101.

**Source discrepancy:** Step 13 measures at C10 but its printed yes branch calls the ECM terminal C9. Verify the circuit before repair.

---

### Printed page 11-119

<a id="p415"></a>
Source: [PDF p.415, printed p.11-119](../page-images/p0415.png).

# DTC P1259: VTEC System Malfunction (continued)

15. Turn ignition OFF.
16. Disconnect rocker arm oil control solenoid 1P connector.
17. At valve side, measure resistance from solenoid 1P terminal to body ground. **14–30 Ω?** Yes: step 18. No: replace solenoid.
18. Remove rocker arm oil pressure switch (A), install pressure gauge adapter and specified gauge/hoses, then reinstall switch. Use a new O-ring on reassembly; switch torque **22 N·m (2.2 kgf·m, 16 lbf·ft)**. Tool numbers are listed on p.11-117.
19. Reconnect solenoid 1P and pressure-switch 2P connectors.
20. Connect tachometer.
21. Start engine; hold 3,000 rpm without load in neutral until radiator fan comes on.
22. Check oil pressure at 1,000, 2,000, and 6,000 rpm. Keep measuring time under 1 minute while engine runs without load. **Below 49 kPa (0.5 kgf/cm², 7 psi)?** Yes: step 23. No: inspect solenoid (p.11-126).
23. Turn ignition OFF.
24. Disconnect solenoid 1P connector.
25. Attach battery-positive cable to solenoid terminal.
26. Start engine; check oil pressure at 6,000 rpm. **Above 390 kPa (4.0 kgf/cm², 57 psi)?** Yes: step 27. No: inspect solenoid (p.11-126).

---

### Printed page 11-120

<a id="p416"></a>
Source: [PDF p.416, printed p.11-120](../page-images/p0416.png).

# DTC P1259: VTEC System Malfunction (continued)

27. With battery positive still connected to solenoid, measure voltage from ECM terminal C10 (VTM, blue/black) to body ground. **Battery voltage above 5,000 rpm?** Yes: step 28. No: replace rocker arm oil pressure switch.
28. Turn ignition OFF.
29. Disconnect battery-positive cable from solenoid terminal.
30. Disconnect ECM connector B (25P).
31. Check continuity from ECM terminal B12 (VTS, green/yellow) to body ground. **Continuity?** Yes: repair short between solenoid and ECM B12. No: step 32.
32. Ground solenoid 1P connector terminal with jumper wire.
33. Check continuity from ECM terminal B12 to body ground. **Continuity?** Yes: substitute a known-good ECM (p.11-5) and recheck; replace original (p.11-115) if symptom goes away. No: repair open between ECM B12 and solenoid.

---

### Printed page 11-121

<a id="p417"></a>
Source: [PDF p.417, printed p.11-121](../page-images/p0417.png).

# DTC P2646: Rocker Arm Oil Pressure Switch
## (VTEC Oil Pressure Switch) Circuit Low Voltage
### ('04-05 models)

**Special Tools Required**
*   Pressure gauge adapter 07NAJ-P07010A
*   A/T low pressure gauge w/panel 07406-0070301
*   A/T pressure hose 07406-0020201
*   A/T pressure hose, 2,210 mm 07MAJ-PY4011A
*   A/T pressure hose, adapter 07MAJ-PY40120

**NOTE:** Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).

1. Turn the ignition switch OFF.
2. Check the engine oil level.
   *Is the engine oil level OK?*
   *YES — Go to step 3.*
   *NO—Adjust the engine oil to the proper level.*

3. Turn the ignition switch ON (II).
4. Reset the engine control module (ECM) (see page 11-4).
5. Start the engine. Hold the engine speed at 3,000 rpm without load until the radiator fan comes on, then let it idle.
6. Test-drive under following conditions:
   Accelerate in 1st gear to an engine speed over 6,000 rpm. Hold the speed for at least 2 seconds.
7. Check for Temporary DTC or DTC with a scan tool or the HDS.
   *Is DTC P2646 indicated?*
   *YES — Go to step 8.*
   *NO—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the rocker arm oil pressure switch (VTEC oil pressure switch), the rocker arm oil control solenoid (VTEC solenoid valve), and the ECM.*

8. Turn the ignition switch OFF.
9. Remove the rocker arm oil pressure switch (VTEC oil pressure switch) (A) and install the special tools as shown, then install the rocker arm oil pressure switch (VTEC oil pressure switch) (A) to the oil pressure gauge adapter (B).
   **NOTE:** Install the parts in the reverse or order of removal with a new O-ring.
   **Switch torque: 22 N·m (2.2 kgf·m, 16 lbf·ft).**

10. Disconnect the rocker arm oil control solenoid (VTEC solenoid valve) 1P connector.
11. Start the engine. Hold the engine speed at 3,000 rpm without load until the radiator fan comes on, then let it idle.
12. Attach the battery positive terminal to the rocker arm oil control solenoid (VTEC solenoid valve) 1P connector terminal.
13. Start the engine, and check the oil pressure at an engine speed of 3,000 rpm.
    *Is the oil pressure above 390 kPa (4.0 kgf/cm², 57 psi)?*
    *YES — Go to step 15.*
    *NO — Go to step 14.*

---

### Printed page 11-122

<a id="p418"></a>
Source: [PDF p.418, printed p.11-122](../page-images/p0418.png).

# DTC P2646: VTEC Oil Pressure Switch Circuit Low Voltage (continued)

14. Check engine oil pressure (p.8-6). **OK?** Yes: replace rocker arm oil control solenoid (p.11-126, step 3). No: repair cause of low oil pressure (p.8-6, step 4).
15. Disconnect rocker arm oil pressure switch 2P connector.
16. At switch side, check continuity between terminals 1 and 2 with engine at 3,000 rpm. **Continuity?** Yes: replace switch (p.11-126). No: step 17.
17. Turn ignition OFF.
18. Disconnect battery lead(s) from solenoid terminal connector.
19. Disconnect ECM connector B. **Source text calls it 24P; source diagram calls it 25P. Verify connector before work.**
20. Check continuity between ECM terminal C10 (VTM, blue/black) and body ground. **Continuity?** Yes: repair short between ECM C10 and pressure switch. No: step 21.
21. Check continuity between ECM terminal B12 (VTS, green/yellow) and body ground. **Continuity?** Yes: repair short between ECM B12 and solenoid. No: step 22.

---

### Printed page 11-123

<a id="p419"></a>
Source: [PDF p.419, printed p.11-123](../page-images/p0419.png).

# DTC P2646: VTEC Oil Pressure Switch Circuit Low Voltage (continued)

22. Ground the rocker arm oil control solenoid 1P connector terminal with a jumper wire.
23. Check continuity between ECM connector B (25P) terminal B12 (VTS, green/yellow) and body ground. **Continuity?** Yes: substitute known-good ECM (p.11-5) and recheck; if symptom goes away, replace original ECM (p.11-115). No: repair open between ECM B12 and solenoid.

---

### Printed page 11-124

<a id="p420"></a>
Source: [PDF p.420, printed p.11-124](../page-images/p0420.png).

# VTEC
## DTC Troubleshooting (cont'd)
### DTC P2647: Rocker Arm Oil Pressure Switch
#### (VTEC Oil Pressure Switch) Circuit High Voltage
**('04-05 models)**

---

### Special Tools Required
*   Pressure gauge adapter 07NAJ-P07010A
*   A/T low pressure gauge w/panel 07406-0070301
*   A/T pressure hose 07406-0020201
*   A/T pressure hose, 2,210 mm 07MAJ-PY4011A
*   A/T pressure hose, adapter 07MAJ-PY40120

> **NOTE:** Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).

1. Turn the ignition switch OFF.
2. Check the engine oil level.
   Is the engine oil level OK ?
   * YES — Go to step 3.
   * NO—Adjust the engine oil to the proper level. •

3. Turn the ignition switch ON (II).
4. Reset the engine control module (ECM) (see page 11-4).
5. Start the engine. Hold the engine speed at 3,000 rpm without load until radiator fan comes on, then let it idle.
6. Check for Temporary DTC or DTC with a scan tool or the HDS.
   Is DTC P2647 indicated?
   * Y E S - G o to step 7.
   * NO—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the rocker arm oil pressure switch (VTEC oil pressure switch), the rocker arm oil control solenoid (VTEC solenoid valve), and the ECM.

7. Turn the ignition switch OFF.
8. Remove the rocker arm oil pressure switch (VTEC oil pressure switch) (A) and install the special tools as shown, then install the rocker arm oil pressure switch (VTEC oil pressure switch) to the oil pressure gauge adapter (B).
   > **NOTE:** Install the parts in the reverse or order of removal with a new O-ring.
   **Switch torque: 22 N·m (2.2 kgf·m, 16 lbf·ft).**

9. Start the engine. Hold the engine speed at 3,000 rpm without load until the radiator fan comes on, then let it idle.
10. Check the oil pressure at engine speeds of 1,000 and 2,000 rpm. Keep the measuring time as short as possible (less than 1 minute) because the engine is running without load.
    Is the oil pressure below 49 kPa (0.5 kgf/cm², 7 psi)?
    * YES — Go to step 11.
    * NO—Inspect the rocker arm oil control solenoid (VTEC solenoid valve) (see page 11-126).B

11. Turn the ignition switch OFF.
12. Disconnect the rocker arm oil pressure switch (VTEC oil pressure switch) 2P connector.

---

### Printed page 11-125

<a id="p421"></a>
Source: [PDF p.421, printed p.11-125](../page-images/p0421.png).

# DTC P2647: VTEC Oil Pressure Switch Circuit High Voltage (continued)

13. At pressure-switch side, check continuity between terminals 1 and 2. **Continuity?** Yes: step 14. No: replace rocker arm oil pressure switch (p.11-126).
14. Measure voltage from pressure-switch 2P connector terminal 1 (VTM, blue/black) to body ground. **Battery voltage?** Yes: repair open between switch and G101. No: step 15.
15. Measure voltage from ECM terminal C10 (VTM, blue/black) to body ground. **Battery voltage?** Yes: repair open between ECM C10 and switch. No: substitute known-good ECM (p.11-5) and recheck; if symptom goes away, replace original ECM (p.11-115).

---

### Printed page 11-126

<a id="p422"></a>
Source: [PDF p.422, printed p.11-126](../page-images/p0422.png).

# Rocker Arm Oil Control Solenoid (VTEC Solenoid Valve) Inspection

1. Disconnect solenoid 1P connector.
2. Measure resistance between terminal and body ground. **Specification: 14–30 Ω.**
3. If resistance is in range, remove valve (A) from cylinder head and inspect valve filter (B) for clogging. If clogged, replace engine oil filter, valve filter, and engine oil. If not clogged, replace valve. The source diagram labels the 6 × 1.0 mm mounting bolts **12 N·m (1.2 kgf·m, 8.7 lbf·ft)**.

---

### Printed page 11-127

<a id="p423"></a>
Source: [PDF p.423, printed p.11-127](../page-images/p0423.png).

# Idle Control System: Component Location Index

Source diagram locates electrical power steering (EPS) control unit (troubleshooting p.11-137), idle air control (IAC) valve, alternator (p.11-135), A/C compressor (p.11-133), starter switch (p.11-136), and brake pedal position switch (p.11-139). See linked source image for exact locations.

---

### Printed page 11-128

<a id="p424"></a>
Source: [PDF p.424, printed p.11-128](../page-images/p0424.png).

# Idle Control System
## DTC Troubleshooting
### DTC P0505: Idle Control System Malfunction
**('00-03 models)**

> **NOTE:**
> *   Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).
> *   If DTC P1519 is stored at the same time as DTC P0505, troubleshoot DTC P1519 first, then recheck for DTC P0505.

**1.** Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

**2.** Check the engine speed at idle without load conditions: headlights, blower fan, radiator fan, and air conditioner off.

Is the idle speed **800 ± 50 rpm**?

*   **YES**—Intermittent failure, the system is OK at this time.
*   **NO**—If the idle speed is less than 750 rpm, go to step 3; if it is 850 rpm or higher, go to step 4.

**3.** Disconnect the idle air control (IAC) valve 3P connector.

Does the engine speed increase or fluctuate?

*   **YES**—Check the idle speed with a different load condition (electrical, A/C, etc.). If it is out of specification, replace the IAC valve (see page 9-2).
*   **NO**—Replace the IAC valve (see page 9-2).

**4.** Turn the ignition switch OFF.

**5.** Remove the intake air duct from the throttle body.

**6.** Start the engine, and let it idle.

**7.** Put your fingers on the upper and lower ports **(A)** in the throttle body.

Does the engine speed drop below 750 rpm?

*   **YES**—Check the idle speed with a different load condition (electrical, A/C, etc.). If it is out of specification, replace the IAC valve (see page 9-2).
*   **NO**—Check for vacuum leaks at these parts:
    *   PCV valve
    *   PCV hose
    *   EVAP canister purge valve
    *   Intake manifold
    *   Throttle body
    *   Brake booster hose

---

### Printed page 11-129

<a id="p425"></a>
Source: [PDF p.425, printed p.11-129](../page-images/p0425.png).

# DTC P0506: Idle Control System RPM Lower Than Expected ('04-05 models)

**NOTE:**
*   Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).
*   If DTC P0511 is stored at the same time as DTC P0506, troubleshoot DTC P0511 first, then recheck for DTC P0506.

1. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
2. Check the engine speed at idle without load conditions; headlights, blower fan, radiator fan, and air conditioner off.

Is the idle speed 800± 50 rpm?

*   **YES**—Intermittent failure, the system is OK at this time.
*   **NO**—Go to step 3.

3. Turn the ignition switch OFF.
4. Disconnect the IAC valve 3P connector.
5. Start the engine, and let it idle.
6. Check the engine speed at idle without load conditions; headlights, blower fan, radiator fan, and air conditioner off.

Does the idle speed increase or fluctuate?

*   **YES**—Check the idle speed with a different load condition (electrical, A/C, etc.). If it is out of specification, replace the IAC valve (see page 9-2).
*   **NO**—Replace the IAC valve (see page 9-2).

---

### Printed page 11-130

<a id="p426"></a>
Source: [PDF p.426, printed p.11-130](../page-images/p0426.png).

# DTC P0507: Idle Control RPM Higher Than Expected (2004–2005)

Record freeze data and review general troubleshooting information (p.11-3). If P0511 is also stored, troubleshoot it first.

1. Start engine; hold 3,000 rpm without load in neutral until radiator fan comes on, then idle.
2. Check idle with headlights, blower, radiator fan, and A/C off. **800 ± 50 rpm?** Yes: intermittent failure. No: step 3.
3. Turn ignition OFF.
4. Remove intake air duct from throttle body.
5. Start engine and idle.
6. Cover upper and lower throttle-body ports (A) with fingers. **Does idle drop below 850 rpm?** Yes: check idle under another electrical or A/C load; if out of specification, replace IAC valve (p.9-2). No: check for leaks at PCV valve and hose, EVAP canister purge valve, intake manifold, throttle body, and brake booster hose. See linked image for port locations.

---

### Printed page 11-131

<a id="p427"></a>
Source: [PDF p.427, printed p.11-131](../page-images/p0427.png).

# DTC P0511 / P1519: IAC Valve Circuit Malfunction

- **P0511:** 2004–2005; marked * in source.
- **P1519:** 2000–2003; marked ** in source.

Record freeze data and review general troubleshooting information (p.11-3).

1. Reset ECM (p.11-4).
2. Turn ignition ON (II).
3. Check for temporary or stored P0511* (P1519**). **Indicated?** Yes: step 4. No: intermittent failure; check IAC valve and ECM connections.
4. Turn ignition OFF.
5. Disconnect IAC valve 3P connector.
6. Turn ignition ON (II).
7. Measure voltage from IAC terminal 2 (IGP, yellow/black) to body ground. **Battery voltage?** Yes: step 8. No: repair open between IAC valve and PGM-FI main relay.
8. Turn ignition OFF.
9. Check continuity from IAC terminal 1 (PG1, black) to body ground. **Continuity?** Yes: step 10. No: repair open between IAC valve and G101.

---

### Printed page 11-132

<a id="p428"></a>
Source: [PDF p.428, printed p.11-132](../page-images/p0428.png).

# DTC P0511 / P1519: IAC Valve Circuit Malfunction (continued)

10. Disconnect ECM connector B (25P).
11. Check continuity between ECM terminal B23 (IACV, black/red) and body ground. **Continuity?** Yes: repair short between IAC valve and ECM B23. No: step 12.
12. Ground IAC valve connector terminal 3 with jumper wire.
13. Check continuity from ECM B23 to body ground. **Continuity?** Yes: step 14. No: repair open between IAC valve and ECM B23.
14. Remove jumper and reconnect IAC valve connector.
15. Turn ignition ON (II).
16. Measure voltage from ECM B23 to body ground. **Battery voltage?** Yes: substitute known-good ECM (p.11-5) and recheck; replace original ECM (p.11-115) if symptom goes away. No: replace IAC valve (p.9-2).

---

### Printed page 11-133

<a id="p429"></a>
Source: [PDF p.429, printed p.11-133](../page-images/p0429.png).

# A/C Signal Circuit Troubleshooting

1. Turn ignition OFF.
2. Disconnect A/C pressure-switch connector.
3. Turn ignition ON (II).
4. Measure voltage between ECM terminals A27 (ACS, blue/red) and B20 (LG1, brown/yellow). **About 5 V?** Yes: step 5. No: step 12.
5. Turn ignition OFF.
6. Reconnect A/C pressure-switch connector.
7. Turn ignition ON (II).
8. Momentarily connect ECM terminals A17 (ACC, red) and B20 with jumper several times. **Compressor clutch clicks?** Yes: step 9. No: step 15.
9. Start engine.
10. Turn blower ON.
11. Turn A/C ON. **Does it operate?** Yes: A/C signal is OK. No: step 16.
12. Turn ignition OFF.
13. Disconnect ECM connector A (32P). Continued on next page.

---

### Printed page 11-134

<a id="p430"></a>
Source: [PDF p.430, printed p.11-134](../page-images/p0430.png).

# A/C Signal Circuit Troubleshooting (continued)

14. Check continuity from ECM terminal A27 (ACS, blue/red) to body ground. **Continuity?** Yes: repair short between ECM A27 and A/C pressure switch. No: substitute known-good ECM (p.11-5) and recheck; replace original (p.11-115) if voltage returns to normal, otherwise inspect A/C system.
15. Momentarily ground main under-hood fuse/relay box connector D (16P) terminal 11 (ACC, red) several times. Leave upper fuse-box cover installed while unbolting and inverting box to prevent shorts. **Compressor clutch clicks?** Yes: repair open between ECM A17 and A/C clutch relay. No: check A/C system for other symptoms.
16. Measure voltage between ECM A27 and B20 (LG1, brown/yellow). **Less than 1.0 V?** Yes: substitute known-good ECM and recheck; replace original if symptom goes away, otherwise inspect A/C system. No: repair open between ECM A27 and A/C pressure switch, or between pressure switch and heater control panel.

**Source discrepancy:** Step 15 and its diagram call connector D 16P, while its note calls the connector on the fuse-box bottom 14P. Verify connector identification before work.

---

### Printed page 11-135

<a id="p431"></a>
Source: [PDF p.431, printed p.11-135](../page-images/p0431.png).

# Alternator FR Signal Circuit Troubleshooting

1. Disconnect alternator 4P connector.
2. Turn ignition ON (II).
3. Measure voltage between ECM B20 (LG1, brown/yellow) and C5 (ALT F, white/red). **About 5 V?** Yes: step 4. No: step 13.
4. Turn ignition OFF.
5. Reconnect alternator 4P connector.
6. Start engine; hold 3,000 rpm without load in neutral until fan comes on, then idle.
7. Measure voltage between ECM B20 and C5. **Does it decrease when headlights and rear defogger turn on?** Yes: FR signal OK. No: step 8.
8. Turn ignition OFF.
9. Disconnect ECM connector C (31P).
10. Disconnect alternator 4P connector.
11. Ground alternator connector terminal 4 (ALT F, white/red) with jumper wire.
12. Check continuity between ECM C5 and body ground. **Continuity?** Yes: test alternator (p.4-38). No: repair open between ECM C5 and alternator.
13. Turn ignition OFF.
14. Disconnect ECM connector C (31P). Continued on next page.

---

### Printed page 11-136

<a id="p432"></a>
Source: [PDF p.432, printed p.11-136](../page-images/p0432.png).

# Alternator FR Signal Circuit Troubleshooting (continued)

15. Check continuity between ECM C5 and body ground. **Continuity?** Yes: repair short between ECM C5 and alternator. No: substitute known-good ECM (p.11-5) and recheck; replace original ECM (p.11-115) if prescribed voltage is restored.

# Starter Switch Signal Circuit Troubleshooting

**Clutch pedal must be pressed.**

1. With ignition ON (II) and engine start button pressed, measure voltage between ECM A24 (STS, blue/orange) and B20 (LG1, brown/yellow). **Battery voltage?** Yes: signal OK. No: step 2.
2. Inspect No. 21 STARTER SIGNAL (7.5 A) fuse in under-dash fuse/relay box. **OK?** Yes: repair open between ECM A24 and fuse. No: repair short between ECM A24 and fuse or PGM-FI main relay; replace fuse.

---

### Printed page 11-137

<a id="p433"></a>
Source: [PDF p.433, printed p.11-137](../page-images/p0433.png).

# EPS Signal Circuit Troubleshooting

1. Turn ignition ON (II).
2. Measure voltage between ECM A26 (EPSLD, blue/black) and B20 (LG1, brown/yellow). **Battery voltage?** Yes: step 6. No: step 3.
3. Start engine.
4. Turn steering wheel to full lock.
5. Measure voltage between ECM A26 and B20. **Battery voltage briefly?** Yes: EPS signal OK. No: step 10.
6. Turn ignition OFF.
7. Disconnect EPS control unit 14P connector.
8. Turn ignition ON (II).
9. Measure voltage from EPS connector terminal 13 (EPSLD, blue/black) to body ground. **Battery voltage?** Yes: substitute known-good EPS control unit and recheck. No: repair open between ECM A26 and EPS unit.
10. Turn ignition OFF.
11. Disconnect EPS 14P connector.
12. Turn ignition ON (II). Continued on next page.

---

### Printed page 11-138

<a id="p434"></a>
Source: [PDF p.434, printed p.11-138](../page-images/p0434.png).

# EPS Signal Circuit Troubleshooting (continued)

13. Measure voltage from EPS control unit connector terminal 13 (EPSLD, blue/black) to body ground. **Battery voltage?** Yes: substitute known-good EPS control unit and recheck. No: step 14.
14. Turn ignition OFF.
15. Disconnect ECM connector A (32P).
16. Check continuity between ECM A26 and body ground. **Continuity?** Yes: repair short between ECM A26 and EPS unit. No: substitute known-good ECM (p.11-5) and recheck; replace original ECM (p.11-115) if voltage becomes normal.

---

### Printed page 11-139

<a id="p435"></a>
Source: [PDF p.435, printed p.11-139](../page-images/p0435.png).

# Brake Pedal Position Switch Signal Circuit Troubleshooting

1. Check brake lights. **On without pressing brake?** Yes: inspect switch adjustment (p.19-6). No: step 2.
2. Press brake pedal. **Lights on?** Yes: step 3. No: step 4.
3. Measure voltage between ECM A32 (BKSW, white/black) and B20 with brake pressed. **Battery voltage?** Yes: signal OK. No: repair open between ECM A32 and brake pedal switch.
4. Inspect No. 47 STOP fuse in main under-hood fuse/relay box: 10 A for 2000–2001; 15 A for 2002–2005. **Fuse OK?** Yes: repair open between switch and fuse, and inspect switch (p.22-144). No: repair short between ECM A32 and fuse; replace fuse.

---

### Printed page 11-140

<a id="p436"></a>
Source: [PDF p.436, printed p.11-140](../page-images/p0436.png).

# Idle Speed Inspection

Leave IAC valve connected. Check MIL, ignition timing, spark plugs, air cleaner, and PCV system first. For Canadian models, pull parking brake lever and ensure headlights are off.

1. Disconnect EVAP canister purge valve 2P connector.
2. Connect tachometer to test connector.
3. Hold engine at 3,000 rpm without load in neutral until radiator fan comes on; then idle.
4. With headlights, blower, radiator fan, and A/C off, idle should be **800 ± 50 rpm**.
5. Idle for 1 minute with A/C on (maximum cool), blower high, and high beams. Idle should be **900 ± 50 rpm**. If out of specification, follow symptom troubleshooting.
6. Reconnect EVAP purge valve connector.

# ECM Idle Learn Procedure

Perform after battery disconnection; ECM replacement, connector disconnection, or reset; removing No. 6 ECU (15 A) fuse, No. 41 BATTERY (100 A) fuse, PGM-FI main relay, or under-hood fuse-box battery wire; disconnecting under-hood fuse-box connectors, dashboard harness connector C404, or G1 terminal; or adjusting idle. Source notes that erasing DTCs with HDS also requires idle learning.

1. Turn off all electrical items.
2. Hold engine at 3,000 rpm without load in neutral until fan comes on or coolant reaches **176–212 °F (80–100 °C)**.
3. Idle about 5 minutes with throttle fully closed and electrical items off. Exclude radiator-fan running time from the 5 minutes.

---

### Printed page 11-141

<a id="p437"></a>
Source: [PDF p.437, printed p.11-141](../page-images/p0437.png).

# Fuel Supply System: Component Location Index

The source diagrams locate the fuel rail; pressure regulator (replacement p.11-154); feed, vapor, and return lines (inspection p.11-148); fuel fill cap and tank (tank replacement p.11-156); fuel pump (test p.11-147, replacement p.11-155); fuel filter (p.11-154); fuel gauge sending unit (test p.11-160, replacement p.11-155); fuel line quick-connect fitting (precautions/removal p.11-150, installation p.11-151); and PGM-FI main relay (p.11-142). See linked source image for exact locations.

---

### Printed page 11-142

<a id="p438"></a>
Source: [PDF p.438, printed p.11-142](../page-images/p0438.png).

# PGM-FI Main Relay Circuit Troubleshooting

1. Turn ignition OFF; disconnect relay 7P connector.
2. Check continuity between relay terminal 3 (GND, black) and body ground. **Continuity?** Yes: step 3. No: repair open between relay and G101.
3. Measure voltage from relay terminal 7 (BAT, white/green) to body ground. **Battery voltage?** Yes: step 5. No: step 4.
4. Check No. 46 ACG S (15 A) fuse in main under-hood box. **Blown?** Yes: repair short between relay and fuse. No: repair open between relay and fuse.
5. With ignition ON (II), measure voltage from relay terminal 5 (IG1, black/yellow) to body ground. **Battery voltage?** Yes: step 7. No: step 6.
6. Check No. 2 FUEL PUMP SRS (15 A) fuse in under-dash box. **Blown?** Yes: repair short between relay and fuse. No: repair open between relay and fuse.

---

### Printed page 11-143

<a id="p439"></a>
Source: [PDF p.439, printed p.11-143](../page-images/p0439.png).

# PGM-FI Main Relay Circuit Troubleshooting (continued)

7. Press clutch, turn ignition ON (II), press start button, and measure voltage from relay terminal 2 (STS, blue/orange) to body ground. **Battery voltage?** Yes: step 9. No: step 8.
8. Check No. 21 STARTER SIGNAL (7.5 A) fuse in under-dash box. **Blown?** Yes: repair short between relay and fuse. No: repair open between relay and fuse.
9. Turn ignition OFF; disconnect ECM connector A (32P).
10. Check continuity between relay terminal 1 and ECM A15 (IMOFLR, green/yellow). **Continuity?** Yes: step 11. No: repair open between relay and ECM A15.
11. Reconnect ECM A and relay 7P connectors.
12. With ignition ON (II), measure B1-to-B20 and B9-to-B20 voltage individually. **Battery voltage?** Yes: step 13. No: check open between relay and ECM B1/B9; if wires OK, replace relay.

---

### Printed page 11-144

<a id="p440"></a>
Source: [PDF p.440, printed p.11-144](../page-images/p0440.png).

# PGM-FI Main Relay Circuit Troubleshooting (continued)

13. Cycle ignition OFF, then ON (II), and within 2 seconds measure voltage between ECM A15 (IMOFLR, green/yellow) and B2 (PG1, black). **1.0 V or less?** Yes: relay may be faulty; step 14. No: substitute known-good ECM (p.11-5) and recheck; replace original (p.11-115) if voltage normalizes.
14. Remove PGM-FI main relay.
15. Apply battery positive to relay terminal 2, ground terminal 1, and check continuity between terminals 5 and 4. **Continuity?** Yes: step 16. No: replace relay and recheck circuit.
16. Apply battery positive to terminal 5, ground terminal 3, and check continuity between terminals 7 and 6. **Continuity?** Yes: step 17. No: replace relay and recheck.
17. Apply battery positive to terminal 6, ground terminal 1, and check continuity between terminals 5 and 4. **Continuity?** Yes: relay OK. No: replace relay and recheck.

**Use the terminal numbers in the source diagram; ignore numbers molded into the relay.**

---

### Printed page 11-145

<a id="p441"></a>
Source: [PDF p.441, printed p.11-145](../page-images/p0441.png).

# Fuel Pressure Relieving
Before disconnecting fuel lines or hoses, release pressure from the system by loosening the fuel pulsation damper on top of the fuel rail.

## Procedure
1. Make sure you have the anti-theft code for the audio system, then write down the audio presets.
2. Disconnect the negative cable from the battery.
3. Remove the fuel fill cap.
4. Remove the intake manifold cover (A).
   *: This illustration shows '00-03 models.
5. Use a wrench on the fuel pulsation damper (A) at the fuel rail.
6. Place a rag or shop towel (B) over the fuel pulsation damper.
7. Slowly loosen the fuel pulsation damper one complete turn.

**NOTE:** Replace all washers whenever the fuel pulsation damper is loosened or removed.

---

# Fuel Pressure Test
## Special Tools Required
* Fuel pressure gauge 07406-004000B
* Fuel pressure gauge adapter 07VAJ-0040100

## Procedure
1. Make sure you have the anti-theft code for the audio system, then write down the audio presets.
2. Disconnect the negative cable from the battery.
3. Remove the fuel fill cap.
4. Remove the intake manifold cover (A).
   *Illustration shows 2000–2003 models.*
5. Use a wrench on the fuel pulsation damper (A) at the fuel rail.
6. Place a rag or shop towel (B) over the fuel pulsation damper.
7. Slowly loosen the fuel pulsation damper one complete turn.

(cont'd)

---

### Printed page 11-146

<a id="p442"></a>
Source: [PDF p.442, printed p.11-146](../page-images/p0442.png).

# Fuel Supply System
## Fuel Pressure Test (cont'd)

8. Remove the fuel pulsation damper from the fuel rail.
9. Attach the fuel pressure gauge attachment and fuel pressure gauge.
**07VAJ-0040100**

> *: This illustration shows '00-03 models.*

10. Disconnect the vacuum hose (A) from the fuel pressure regulator (B) and pinch it closed with a clamp (C).
11. Reconnect the negative battery cable, then start the engine, and let it idle.
* If the engine starts, go to step 13.
* If the engine does not start, go to step 12.

12. Check to see if the fuel pump is running: remove the fuel fill cap and listen to the fuel fill port while an assistant turns the ignition switch ON (II), you should hear the pump run for about 2 seconds when the ignition switch is turned ON (II).
* If the fuel pump runs, go to step 13.
* If the fuel pump does not run, test it (see page 11-147).

13. Read the pressure gauge (with the fuel pressure regulator vacuum hose disconnected and clamped). The pressure should be **320—370 kPa** (**3.3—3.8 kgf/cm²**, **47 - 54 psi**).
* If the pressure is OK and the engine is running, go to step 14. If the engine is not running, repair the cause, then continue this test.
* If the pressure is out of spec, go to step 14.

14. With the engine running, unpinch and reconnect the vacuum hose and read the gauge again. The pressure should be **260—310 kPa** (**2.7-3.2 kgf/cm²**, **38-46 psi**).
* If the fuel pressure is OK, the test is complete.
* If the pressure is out of spec, go to step 15.

15. Disconnect the vacuum hose from the pressure regulator again while you watch the pressure gauge. The pressure should rise when you disconnect the hose.
* If the pressure did not rise, replace the fuel pressure regulator (see page 11-154).
* If the pressure rises, but all your readings were lower than specified, check for a clogged fuel filter and for leaks in the fuel lines.
* If the pressure rises, but all your readings were higher than specified, check for a pinched or clogged fuel return hose or line.

16. Reconnect the vacuum hose, remove the pressure gauge, and reinstall the fuel pulsation damper with a new washer. Tighten the fuel pulsation damper to **22 N·m** (**2.2 kgf·m**, **16 lbf·ft**).

> NOTE: Disassemble and clean the fuel pressure gauge attachment thoroughly after use.

---

### Printed page 11-147

<a id="p443"></a>
Source: [PDF p.443, printed p.11-147](../page-images/p0443.png).

# Fuel Pump Test

Listen at fuel fill port with cap removed: pump should run about 2 seconds when ignition first turns ON. If silent:

1. Remove rear tray (p.20-73).
2. Remove floor access panel.
3. Turn ignition OFF.
4. Disconnect fuel pump 5P connector.
5. Jumper PGM-FI main relay 7P terminals 4 and 5.
6. Turn ignition ON (II).
7. Check for battery voltage between fuel pump connector terminal 5 (fuel pump, yellow/green) and body ground. If present, check pump ground; if ground is OK, replace pump (p.11-155). If absent, check harness (p.11-142).

---

### Printed page 11-148

<a id="p444"></a>
Source: [PDF p.444, printed p.11-148](../page-images/p0444.png).

# Fuel Line Inspection

Check fuel system lines, hoses, and fuel filter for damage, leaks, or deterioration; replace as needed. The source diagram specifies **22 N·m (2.2 kgf·m, 16 lbf·ft)** at fuel-rail fitting and **37 N·m (3.8 kgf·m, 27 lbf·ft)** at the line junction shown. See linked image for exact fittings.

---

### Printed page 11-149

<a id="p445"></a>
Source: [PDF p.445, printed p.11-149](../page-images/p0445.png).

# Fuel Line Clamp Inspection

Check all hose clamps and retighten if necessary. **Do not disconnect hoses from lines at the triangular-marked joints.** Replace the fuel-tank unit base gasket. Diagram labels hose clamp positions A and B; center each clamp on its fitting. For clamp A, the edge distance shown is **10–15 mm (0.39–0.59 in.)**. See linked source image for all locations and orientations.

---

### Printed page 11-150

<a id="p446"></a>
Source: [PDF p.446, printed p.11-150](../page-images/p0446.png).

# Fuel Supply System
## Fuel Line/Quick-Connect Fitting
### Precautions

The fuel tube/quick-connect fittings assembly connects the in-tank fuel pump to the fuel feed line and the fuel return line. When removing or installing the fuel pump and fuel tank, it is necessary to disconnect or connect the quick-connect fittings.

Pay attention to the following:
* The fuel tubes (A) and quick-connect fittings (B) are not heat-resistant; be careful not to damage them during welding or other heat-generating procedures.
* The fuel tubes and quick-connect fittings are not acid-proof; do not touch it with a shop towel which was used for wiping battery electrolyte. Replace them if they came into contact with electrolyte or something similar.
* When connecting or disconnecting the fuel tubes and quick-connect fittings, be careful not to bend or twist them excessively. Replace them when damaged.

A disconnected quick-connect fittings can be reconnected, but the retainer on the mating line cannot be reused once it has been removed from the line. Replace the retainer when:
* replacing the fuel tank unit.
* replacing the fuel filter.
* replacing the fuel feed line.
* replacing the fuel return line.
* it has been removed from the line.
* it is damaged.

### Fuel Line/Quick-Connect Fitting Removal

**NOTE:** Before you work on the fuel line and fittings, read the "Fuel Line/Quick-Connect Fitting Precautions" (see page 11-150).

1. Relieve fuel pressure (see page 11-145).
2. Check the fuel quick-connect fittings for dirt, and clean them if necessary.
3. Hold the connector (A) with one hand, and squeeze the retainer tabs (B) with the other hand to release them from the locking pawls (C). Pull the connector off.

**NOTE:**
* Be careful not to damage the line (D) or other parts. Do not use tools.
* If the connector does not move, keep the retainer tabs pressed down, and alternately pull and push the connector until it comes off easily.
* Do not remove the retainer from the line; once removed, the retainer must be replaced with a new one.

---

### Printed page 11-151

<a id="p447"></a>
Source: [PDF p.447, printed p.11-151](../page-images/p0447.png).

# Fuel Line/Quick-Connect Fitting Removal (continued)

4. Inspect contact area (A) of line (B). Clean dirt; replace fuel tank unit, filter, feed line, or return line if rusty or damaged.
5. Cover disconnected connector and line end with plastic bags to prevent damage and contamination. A retainer removed from the pipe cannot be reused. Replace it after changing tank unit, filter, feed or return line, or if removed or damaged.

# Fuel Line/Quick-Connect Fitting Installation

Read precautions on p.11-150 first.

1. Inspect and, if needed, clean line contact area (A) on line (B).
2. Insert a new retainer (A) into connector (B) if damaged or after changing tank unit, filter, feed or return line, or removing old retainer. Continued on next page.

---

### Printed page 11-152

<a id="p448"></a>
Source: [PDF p.448, printed p.11-152](../page-images/p0448.png).

# Fuel Line/Quick-Connect Fitting Installation (continued)

3. Before connecting a new fuel tube/quick-connect assembly (A), remove old retainer from mating line.
4. Align fittings with line (A), then align retainer (B) locking pawls with connector (C) grooves. Press fitting onto line until both pawls click. If difficult, apply a small amount of new engine oil to line end.

Source diagrams show three arrangements: a new retainer, a new fuel line with ring pull, and reconnection to an existing retainer. See linked image for orientation.

---

### Printed page 11-153

<a id="p449"></a>
Source: [PDF p.449, printed p.11-153](../page-images/p0449.png).

# Fuel Line/Quick-Connect Fitting Installation (continued)

5. When reconnecting with an old retainer, visually verify tabs (A) locked and pull connector (B) to check. When installing a new fuel line, confirm the connection is secure **before** pulling ring pull (C) upward; it can break if connection is loose.
6. Reconnect negative battery cable. Cycle ignition ON (II) two or three times; fuel pump runs about 2 seconds each time and pressure rises. Check for fuel leaks.

---

### Printed page 11-154

<a id="p450"></a>
Source: [PDF p.450, printed p.11-154](../page-images/p0450.png).

# Fuel Pressure Regulator Replacement

1. Place shop towel under regulator and relieve pressure (p.11-145).
2. Disconnect vacuum and fuel-return hoses.
3. Remove two 6 mm retainer bolts (A) and regulator (B).
4. Oil a new O-ring (C) with clean engine oil; install carefully.
5. Install regulator and bolts.
6. Reconnect vacuum and return hoses.
7. Cycle ignition ON (II) without cranking two or three times, allowing pump to run about 2 seconds each time; check for leaks.

# Fuel Filter Replacement

Replace if pressure is below **320–370 kPa (3.3–3.8 kgf/cm², 47–54 psi)** with regulator vacuum hose disconnected and pinched, after confirming pump and regulator are good.

1. Remove fuel tank unit (p.11-155).
2. Remove filter (A).
3. Reinstall with new base gasket. Ensure harness terminal (B) locks securely; clamp tab (C) clears harness; do not press lower suction-filter section (D); ensure gauge sending-unit (E) connector locks without bending or twisting.

---

### Printed page 11-155

<a id="p451"></a>
Source: [PDF p.451, printed p.11-155](../page-images/p0451.png).

# Fuel Pump/Fuel Gauge Sending Unit Replacement

1. Remove rear tray (p.20-73).
2. Remove floor access panel.
3. Disconnect fuel pump 5P connector.
4. Remove fuel fill cap.
5. Relieve fuel pressure (p.11-145).
6. Disconnect quick-connect fittings from pump.
7. Remove fuel-tank unit bolts (A), **4 N·m (0.4 kgf·m, 3 lbf·ft)**, and unit (B).
8. Remove bracket (A), filter (B), sending unit (C), hose (D), and harness (E).
9. When reconnecting pump (I), ensure suction filter (H) is firmly attached and connections secure.
10. Reassemble with new base gasket. Ensure harness terminal (F) locks; clamp tab (G) clears harness (diagram shows 1 mm); do not press lower suction-filter part; lock sending-unit connector without excessive bend or twist; check for leaks.

---

### Printed page 11-156

<a id="p452"></a>
Source: [PDF p.452, printed p.11-156](../page-images/p0452.png).

# Fuel Supply System
## Fuel Tank Replacement
### Removal

1. Remove the fuel fill cap.
2. Relieve the fuel pressure (see page 11-145).
3. Remove the rear tray (see page 20-73).
4. Drain the fuel tank: Remove the fuel tank unit (see page 11-155). Using a hand pump, hose, and a container suitable for fuel, draw the fuel from the fuel tank.
5. Reinstall the fuel tank unit.
6. Remove the brake fluid from the master cylinder reservoir with a syringe.

> **NOTE:** Do not spill brake fluid on the vehicle; it may damage the paint; if brake fluid does contact the paint, wash it off immediately with water.

7. Remove the access panel (A) from the floor, and disconnect the fuel tank 5P connector (B).
8. Disconnect both ABS rear wheel sensors 2P connectors (A), and push the connectors out (B).
9. Remove the fuel pipe cover (A), and disconnect the fuel fill neck tube (B), the fuel tank vapor recirculation tube (C) and the fuel tank vapor signal tube (D) from the fuel fill pipes (E).
10. Loosen the rear wheel nuts slightly, then raise the vehicle and make sure it is securely supported.
11. Remove the rear wheels.

---

### Printed page 11-157

<a id="p453"></a>
Source: [PDF p.453, printed p.11-157](../page-images/p0453.png).

# Fuel Tank Replacement: Removal (continued)

12. Remove bolts from both ABS rear wheel sensor harness brackets (A); 6 × 1.0 mm, **9.8 N·m (1.0 kgf·m, 7.2 lbf·ft)**.
13. Remove both caliper shields (A); 6 × 1.0 mm, **9.8 N·m** fasteners.
14. Disconnect both parking-brake cables (A) and move aside; 8 × 1.25 mm, **22 N·m (2.2 kgf·m, 16 lbf·ft)** fasteners.
15. Disconnect brake hoses from both rear brake lines using a 10 mm flare-nut wrench.

Illustrations show left side of vehicle; perform applicable operations on both sides.

---

### Printed page 11-158

<a id="p454"></a>
Source: [PDF p.454, printed p.11-158](../page-images/p0454.png).

# Fuel Tank Replacement: Removal (continued)

16. Remove flange bolt (A) from both rear dampers (B); 12 × 1.25 mm, **64 N·m (6.5 kgf·m, 47 lbf·ft)**. Illustration shows left side.
17. Remove canister cover (A), rear suspension stiffener (B), and propeller shaft (C) (p.16-18). Diagram labels 10 × 1.25 mm fasteners at **45 N·m** and 6 × 1.0 mm fasteners at **9.8 N·m**.
18. Remove muffler (A); diagram labels 10 × 1.25 mm fasteners at **33 N·m (3.4 kgf·m, 25 lbf·ft)**.
19. Disconnect quick-connect fittings (A) (p.11-150).

---

### Printed page 11-159

<a id="p455"></a>
Source: [PDF p.455, printed p.11-159](../page-images/p0455.png).

# Fuel Tank Replacement: Removal (continued)

20. Disconnect fuel-tank vapor vent tube (A); remove bolt (B) and EVAP canister (C). Diagram calls for **22 N·m (2.2 kgf·m, 16 lbf·ft)** at bolt B.
21. Disconnect hose (A) and fuel vent tube (B); remove vapor vent tube from holder (C), then bolts (D) and fuel vent assembly (E).
22. Support rear suspension subframe (A), remove mounting bolts (B), then subframe. Diagram distinguishes 14 × 1.5 mm bolts at **103 N·m (10.5 kgf·m, 76 lbf·ft)** and 12 × 1.5 mm bolts at **59 N·m (6.0 kgf·m, 43 lbf·ft)**.
23. Support fuel tank (A), remove mounting bolts (B), then tank. Diagram: 8 × 1.25 mm bolts at **45 N·m (4.6 kgf·m, 33 lbf·ft)**.

---

### Printed page 11-160

<a id="p456"></a>
Source: [PDF p.456, printed p.11-160](../page-images/p0456.png).

# Fuel Supply System
## Fuel Tank Replacement (cont'd)
### Installation
1. Install the parts in the reverse order of removal.
2. After installing, bleed the brake system (see page 19-9), and adjust the wheel alignment (see page 18-7).
3. Check for fuel leaks.

## Fuel Gauge Sending Unit Test
**NOTE:** For the fuel gauge system circuit diagram, refer to the Gauges Circuit Diagram.
* '00-03 models (see page 22-63)
* '04-05 models (see page 22-68)

1. Check the No. 5 **INSTRUMENT LIGHT BACK UP LIGHT** (7.5 A) fuse in the under-dash fuse/relay box.
   * If the fuse is OK, check for an open in the **YEL** wire between the gauge assembly and the No. 5 **INSTRUMENT LIGHT BACK UP LIGHT** (7.5 A) fuse.
   * If the fuse is blown, replace it, and check for an open in the **YEL** wire between the gauge assembly and the No. 5 **INSTRUMENT LIGHT BACK UP LIGHT** (7.5 A) fuse.

2. Remove the rear tray (see page 20-73).
3. Remove the access panel from the floor.
4. Disconnect the fuel pump 5P connector.
5. Measure voltage between fuel pump 5P connector terminals No. 1 and No. 2 with the ignition switch **ON** (**II**). There should be about 5 to 8 V.
   * If the voltage is as specified, go to step 6.
   * If the voltage is not as specified, check for:
     - an open or short in the **YEL/BLK** or **BLK** wire.
     - poor ground (**G 601**).
     - a faulty main printed circuit board in the gauge assembly.

---

### Printed page 11-161

<a id="p457"></a>
Source: [PDF p.457, printed p.11-161](../page-images/p0457.png).

# Fuel Gauge Sending Unit Test (continued)

6. Turn ignition OFF.
7. Remove bolts and fuel-tank unit (p.11-155).
8. Measure resistance between terminals 1 and 2 at each float position. Replace sending unit if outside these ranges:

| Float position | Resistance | Float height |
| --- | ---: | ---: |
| F (full) | 11–13 Ω | 82.9 ± 1.9 mm (3.26 ± 0.0748 in.) |
| 1/2 | 52–58 Ω | 154.2 ± 1.2 mm (6.07 ± 0.0472 in.) |
| LOW | 114.4–120.4 Ω | 215.5 mm (8.48 in.) |
| E (empty) | 130–132 Ω | 222.8 ± 1.9 mm (8.77 ± 0.0748 in.) |

9. Remove No. 2 FUEL PUMP SRS (15 A) fuse to keep pump off.
10. Connect pump 5P connector.
11. With float at F, turn ignition ON (II). If gauge reads F, system OK; otherwise replace gauge assembly.

# Low Fuel Indicator Test

1. Perform sending-unit test (p.11-160); repair any malfunction before continuing.
2. With float at E, turn ignition ON (II). If low-fuel indicator lights, step 3. Otherwise check circuit diagram (2000–2003 p.22-63; 2004–2005 p.22-68).
3. Lift float above LOW. If light goes out, system OK; otherwise check same circuit diagram.

---

### Printed page 11-162

<a id="p458"></a>
Source: [PDF p.458, printed p.11-162](../page-images/p0458.png).

# Intake Air System: Component Location Index

The source diagram locates air cleaner (element service p.11-169), throttle body (test p.11-163, removal/installation p.11-165, disassembly/reassembly p.11-166), and throttle cable (adjustment p.11-168, removal/installation p.11-167). See linked source image for exact locations.

---

### Printed page 11-163

<a id="p459"></a>
Source: [PDF p.459, printed p.11-163](../page-images/p0459.png).

# Throttle Body Test

**NOTE:** Do not adjust the throttle stop screw. It is preset at the factory.

1. With the engine off, check the throttle cable operation. The cable should operate without binding or sticking.
   - If the cable operates OK, go to step 2.
   - If the cable binds or sticks, check it and its routing. If it's faulty, reroute it or replace it and adjust it (see page 11-168), then go to step 2.

2. Operate the throttle lever by hand to see if the throttle valve and/or shaft are too loose or too tight.
   - If there is excessive play in the throttle valve shaft, or any binding in the throttle valve at the fully closed position, replace the throttle body.
   - If the throttle valve and shaft are OK, go to step 3.

3. Check for clearance (A) between the throttle stop screw (B) and the throttle lever (C) at the fully closed position. If there is any clearance, replace the throttle body (see page 11-165). Do not adjust the throttle stop screw.

---

### Printed page 11-164

<a id="p460"></a>
Source: [PDF p.460, printed p.11-164](../page-images/p0460.png).

# Intake Air System
## Throttle Position Sensor Signal Inspection

**NOTE:**
*   This procedure checks the APP sensor in its fully closed position. In any other position, the APP sensor stores DTCs which are covered in other troubleshooting procedures.
*   Check for Temporary DTCs or DTCs with the HDS before doing this procedure. If any DTCs are indicated, troubleshoot them first, then do this procedure.
*   Press the accelerator pedal several times to check its movement. If it does not move smoothly, check the pedal, the throttle cable, and the throttle linkage individually. If you find a problem in one of them, replace the part(s) that caused the problem.

1.  Connect the HDS or an OBD II scan tool to the data link connector (DLC) (**A**). On '00-01 models, the DLC is located under the passenger's side of the dashboard. On '02-05 models, the DLC is located behind the driver's side of the front console.

2.  Turn the ignition switch ON (**II**).

3.  Make sure the HDS or an OBD II scan tool communicates with the ECM and other vehicle systems. If it doesn't, go to the DLC circuit troubleshooting (see page 11-110).

4.  Make sure the accelerator pedal is not pressed, then check the **TP SENSOR** in the DATA LIST with the HDS.
    *   If it is below 0.5 V, the throttle position sensor is OK.
    *   If it is above 0.5 V, adjust the throttle cable (see page 11-168), then go to step 4.

5.  Make sure the accelerator pedal is not pressed, then check the **TP SENSOR** in the DATA LIST with the HDS.
    *   If it is below 0.5 V, the throttle position sensor is OK.
    *   If it is above 0.5 V, substitute a known-good **ECM** (see page 11-5), then go to step 5.

6.  Make sure the accelerator pedal is not pressed, then check the **TP SENSOR** in the DATA LIST with the HDS.
    *   If it is below 0.5 V, the throttle position sensor is OK.
    *   If it is above 0.5 V, replace the throttle body (see page 11-165), then go to step 1.

---

### Printed page 11-165

<a id="p461"></a>
Source: [PDF p.461, printed p.11-165](../page-images/p0461.png).

# Intake Air System
## Throttle Body Removal/Installation

The illustration identifies the throttle position (TP) sensor, manifold absolute pressure (MAP) sensor, throttle cable, mounting fasteners, and gasket. Replace the gasket during installation. Tighten throttle body mounting fasteners to **22 N·m (2.2 kgf·m, 16 lbf·ft)**.

**Notes:** Do not adjust the throttle stop screw. The TP sensor is not removable. After reassembly, adjust the cruise control actuator cable (see page 4-71) and throttle cable (see page 11-168).

---

### Printed page 11-166

<a id="p462"></a>
Source: [PDF p.462, printed p.11-166](../page-images/p0462.png).

# Intake Air System
## Throttle Body Disassembly/Reassembly

The illustration shows the MAP sensor and its O-ring. Replace the **MAP sensor O-ring** on reassembly. Tighten the MAP sensor screw to **2.1 N·m (0.21 kgf·m, 1.5 lbf·ft)**. The TP sensor is integral to the throttle body and is not removable.

---

### Printed page 11-167

<a id="p463"></a>
Source: [PDF p.463, printed p.11-167](../page-images/p0463.png).

# Intake Air System
## Throttle Cable Removal/Installation

1. Fully open the throttle valve, then remove throttle cable **A** from throttle link **B**.
2. Remove cable housing **C** from cable bracket **D**.
3. Remove the accelerator pedal mounting nuts **A** and pedal **B** with throttle cable **C** and actuator cable **D**. Pedal mounting nut torque: **13 N·m (1.3 kgf·m, 9.4 lbf·ft)**.
4. Pull both cables into the passenger compartment.
5. Remove throttle cable **A** and actuator cable **B** from accelerator pedal bracket **C**. Apply silicone grease (P/N **08798-9002**) at the cable/pedal bracket as shown.
6. Install in the reverse order.
7. Start the engine, hold **3,000 rpm** without load until the radiator fan comes on, then let it idle.
8. Hold the cable sheath and remove all slack.
9. Turn adjusting nut **A** until it is **3 mm (0.1 in.)** from cable bracket **B**.
10. Tighten locknut **C** to **9.8 N·m (1.0 kgf·m, 7.2 lbf·ft)**. Cable free play should be **4–6 mm (0.2–0.3 in.)**; readjust if needed.
11. Check that the throttle opens fully with the pedal depressed and returns to idle when released.

---

### Printed page 11-168

<a id="p464"></a>
Source: [PDF p.464, printed p.11-168](../page-images/p0464.png).

# Intake Air System
## Throttle Cable Adjustment

1. Check cable free play at the throttle linkage. Cable free play (A) should be **4—6 mm (0.2—0.3 in.)**.

2. If free play (A) is not within spec (**4—6 mm, 0.2—0.3 in.**), loosen the locknut (**B**), turn the adjusting nut (**C**) until the free play is as specified, then retighten the locknut.

3. With the cable properly adjusted, check the throttle valve to be sure it opens fully when you push the accelerator pedal to the floor. Also check the throttle valve to be sure it returns to the idle position whenever you release the accelerator pedal.

**Page Reference:** 11-168

---

### Printed page 11-169

<a id="p465"></a>
Source: [PDF p.465, printed p.11-169](../page-images/p0465.png).

# Air Cleaner Element Inspection/Replacement

1. Remove the air cleaner housing cover (A).
2. Remove the air cleaner element (B) from the air cleaner housing (C).
3. Check the air cleaner element for damage or clogging. If there is damage or clogging, replace the air cleaner element.
   **NOTE:** Do not clean the air cleaner element by blowing it off with compressed air.
4. Clean and remove any debris from inside the air cleaner housing.
5. Install the parts in the reverse order of removal.

**Page Reference:** 11-169

---

### Printed page 11-170

<a id="p466"></a>
Source: [PDF p.466, printed p.11-170](../page-images/p0466.png).

# Catalytic Converter System
## DTC Troubleshooting
### DTC P0420: Catalyst System Efficiency Below Threshold

**NOTE:**
*   Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).
*   If some of the DTCs listed below are stored at the same time as DTC P0420, troubleshoot those DTCs first, then recheck for DTC P0420.
    *   **P0137, P0138:** Secondary heated oxygen sensor (secondary HO2S (Sensor 2))
    *   **P0141:** Secondary HO2S (Sensor 2) heater

**Procedure:**
1.  Reset the ECM (see page 11-4), then continue to steps 2 through 5 to reset the readiness code.
2.  Start the engine. Hold the engine speed at **3,000 rpm** without load (in neutral) until the radiator fan comes on.
3.  Drive on a highway for about **10 minutes** without stopping. Your speed can vary.
4.  With the transmission in **4th gear**, drive at a steady speed between **50—62 mph (80—100 km/h)** for **30 seconds**.
5.  Repeat step 4 three times. Between each repetition, close the throttle completely for **1 —2 seconds**. If the engine is stopped during this part of the procedure, go to step 3 and do the procedure again.
6.  Check for a Temporary DTC with the scan tool.

**Decision Path:**
*   Does the scan tool indicate Temporary DTC P0420?
    *   **YES —** Check the three way catalytic converter (TWC). If necessary, replace the TWC (see page 9-5).
    *   **NO —** Check for readiness code completion.
        *   If the readiness is complete, it was a intermittent failure; the system is OK at this time.
        *   If the readiness is incomplete, repeat steps 2 through 5.

**Page Reference:**
*   11-170

---

### Printed page 11-171

<a id="p467"></a>
Source: [PDF p.467, printed p.11-171](../page-images/p0467.png).

# PCV System
## DTC Troubleshooting
### DTC P2279: Intake Air System Leak Detected ('04-05 models)

**NOTE:** Before you troubleshoot, record all freeze data and review the general troubleshooting information (see page 11-3).

1. Reset the ECM (see page 11-4).
2. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on.
3. Let the engine idle for at least 40 seconds with the throttle fully closed.
4. Check for DTC with a scan tool or the HDS.

**Is DTC P2279 indicated?**

- **YES**—Check these parts for vacuum leaks:
  - PCV valve
  - PCV hose
  - EVAP canister purge valve
  - Throttle body
  - Brake booster hose
  - Intake manifold gasket

- **NO**—Intermittent failure, the system is OK at this time.

---

## PCV Valve Inspection

1. Check the PCV valve (A), hoses (B), and connections for leaks or restrictions.
   > *: This illustration shows '00-03 models.*

2. At idle, make sure there is a clicking sound from the PCV valve when the hose between the PCV valve and intake manifold is lightly pinched (A) with your fingers or pliers.
   - If there is no clicking sound, check the PCV valve grommet for cracks or damage. If the grommet is OK, replace the PCV valve ('04-05 models) (see page 11-172), then recheck.
   > *: This illustration shows '00-03 models.*

**Page Reference:** 11-171

---

### Printed page 11-172

<a id="p468"></a>
Source: [PDF p.468, printed p.11-172](../page-images/p0468.png).

# PCV System
## PCV Valve Replacement
**'04-05 models**

1. Disconnect the PCV hose.
2. Remove the PCV valve (**A**).
   - PCV valve **A** torque: **44 N·m** (4.5 kgf·m, 33 lb-ft)
3. Install the parts in the reverse order of removal with a new washer (**B**).

*Page reference: 11-172*

---

### Printed page 11-173

<a id="p469"></a>
Source: [PDF p.469, printed p.11-173](../page-images/p0469.png).

# EVAP System
## Component Location Index

The location illustration identifies the **fuel tank pressure (FTP) sensor**, **fuel tank vapor control valve**, **EVAP canister**, **EVAP canister purge valve**, **EVAP canister bypass solenoid valve**, **EVAP canister vent shut valve**, and **EVAP two-way valve**. Fuel tank vapor control valve test: page 11-195; replacement: page 11-196. EVAP two-way valve test: page 11-194. See the source image for physical locations and hose routing.

---

### Printed page 11-174

<a id="p470"></a>
Source: [PDF p.470, printed p.11-174](../page-images/p0470.png).

# EVAP System
## DTC Troubleshooting — P0451 FTP Sensor Circuit Range/Performance

**Special tool:** Vacuum pump/gauge, 0–30 in.Hg, Snap-on YA4000A or equivalent. Before troubleshooting, record freeze data and review general troubleshooting information (page 11-3).

1. Remove the fuel fill cap.
2. Turn ignition ON (II).
3. Monitor FTP sensor voltage with the HDS, or measure between ECM connector terminals **A29 (PTANK, light green)** and **C18 (SG2, green/yellow)**. If about **2.5 V**, continue; otherwise replace the FTP sensor.
4. Turn ignition OFF.
5. Disconnect the hose between the EVAP two-way valve and FTP sensor at the two-way valve end.
6. Connect the vacuum pump/gauge to the open hose end.
7. Turn ignition ON (II).
8. Monitor FTP sensor voltage as in step 3 while slowly squeezing the vacuum pump/gauge.
9. Does voltage smoothly fall to about **1.5 V** and hold? **Stop applying vacuum at 1.5 V to avoid damaging the sensor.** If yes, the failure is intermittent; check for poor FTP sensor and ECM connections. If no, replace the FTP sensor.

---

### Printed page 11-175

<a id="p471"></a>
Source: [PDF p.471, printed p.11-175](../page-images/p0471.png).

# EVAP System — DTC P0452: FTP Sensor Circuit Low Voltage

**Note:** Record freeze data and review general troubleshooting information (page 11-3).

1. Check FTP sensor vacuum lines for misrouting, leaks, breaks, or clogs. If OK, go to step 2; otherwise repair or replace them.
2. Reset ECM (page 11-4).
3. Remove fuel fill cap.
4. Turn ignition ON (II).
5. Monitor FTP sensor voltage with HDS, or measure between body ground and ECM terminal **A29 (PTANK, light green)**. If about **2.5 V**, the fault is intermittent; check FTP sensor and ECM connections. Otherwise, continue.
6. Turn ignition OFF.
7. Reinstall fuel fill cap.
8. Disconnect FTP sensor 3P connector.
9. Turn ignition ON (II).
10. Measure voltage between FTP sensor connector terminals **1 (VCC2, yellow/blue)** and **2 (SG2, green)**. If about **5 V**, go to step 12 on the next page. Otherwise, go to step 11.

---

### Printed page 11-176

<a id="p472"></a>
Source: [PDF p.472, printed p.11-176](../page-images/p0472.png).

# EVAP System — DTC P0452 (continued)

11. Measure between ECM connector terminals **C28 (VCC2, yellow/blue)** and **C18 (SG2, green/yellow)**. If about **5 V**, repair the open between ECM C28 and FTP sensor. Otherwise, substitute a known-good ECM (page 11-5); replace the original ECM if readings normalize (page 11-115).
12. Measure between FTP sensor 3P connector terminals **2 (SG2, green)** and **3 (PTANK, light green)**. If about **5 V**, replace FTP sensor. Otherwise, continue.
13. Turn ignition OFF.
14. Disconnect ECM connector A (32P).
15. Check continuity between FTP sensor connector terminal **3** and body ground. If continuity exists, repair short between FTP sensor and ECM A29. Otherwise, substitute a known-good ECM and recheck; replace original ECM if readings normalize.

---

### Printed page 11-177

<a id="p473"></a>
Source: [PDF p.473, printed p.11-177](../page-images/p0473.png).

# EVAP System — DTC P0453: FTP Sensor Circuit High Voltage

**Note:** Record freeze data and review general troubleshooting information (page 11-3).

1. Check FTP sensor vacuum lines for misrouting, leaks, breaks, and clogs. Repair or replace if needed; otherwise continue.
2. Reset ECM (page 11-4).
3. Remove fuel fill cap.
4. Turn ignition ON (II).
5. Monitor FTP sensor voltage with HDS or measure between body ground and ECM terminal **A29 (PTANK, light green)**. At about **2.5 V**, fault is intermittent; inspect FTP sensor and ECM connections. Otherwise, continue.
6. Turn ignition OFF.
7. Reinstall fuel fill cap.
8. Disconnect FTP sensor 3P connector.
9. Turn ignition ON (II).
10. Measure between FTP sensor connector terminals **1** and **2**. At about **5 V**, go to step 12 on next page; otherwise go to step 11.

---

### Printed page 11-178

<a id="p474"></a>
Source: [PDF p.474, printed p.11-178](../page-images/p0474.png).

# EVAP System — DTC P0453 (continued)

11. Measure between ECM connector terminals **C28 (VCC2, yellow/blue)** and **C18 (SG2, green/yellow)**. If about **5 V**, repair open between ECM **C18** and FTP sensor. Otherwise, substitute a known-good ECM and recheck; replace original ECM if readings normalize.
12. Measure between FTP sensor 3P connector terminals **2 (SG2, green)** and **3 (PTANK, light green)**. If about **5 V**, replace FTP sensor. Otherwise, continue.
13. Measure between ECM terminals **A29 (PTANK, light green)** and **C18 (SG2, green/yellow)**. If about **5 V**, repair open between FTP sensor and ECM A29. Otherwise, substitute a known-good ECM and recheck; replace original ECM if readings normalize.

**Source note:** Step 11 measures C28–C18 but directs repair of the C18 wire; this apparent inconsistency is retained from the printed manual.

---

### Printed page 11-179

<a id="p475"></a>
Source: [PDF p.475, printed p.11-179](../page-images/p0475.png).

# EVAP System — DTC P0497: Low Purge Flow ('04–05 models)

**Special tool:** Vacuum pump/gauge, 0–30 in.Hg, Snap-on YA4000A or equivalent. Record freeze data and review general troubleshooting information (page 11-3).

1. Turn ignition ON (II).
2. Measure between ECM terminal **A6 (PCS, red/yellow)** and body ground. If battery voltage is present, go to step 3; otherwise go to step 8.
3. Turn ignition OFF.
4. Disconnect vacuum hose from EVAP purge joint **A** and attach vacuum pump/gauge to hose.
5. Ground ECM terminal **A6** with a jumper wire.
6. Turn ignition ON (II).
7. Apply vacuum to hose. If valve holds vacuum, replace EVAP canister purge valve; otherwise go to step 14.
8. Turn ignition OFF.
9. Disconnect EVAP canister purge valve 2P connector. Continue on next page.

---

### Printed page 11-180

<a id="p476"></a>
Source: [PDF p.476, printed p.11-180](../page-images/p0476.png).

# EVAP System — DTC P0497 (continued)

10. Check continuity between EVAP canister purge valve 2P connector terminal **2 (PCS, red/yellow)** and body ground. If continuity exists, go to step 11. Otherwise, repair open between purge valve and ECM A6.
11. Turn ignition ON (II).
12. Measure between purge valve connector terminal **1 (IG1, black/yellow)** and body ground. If battery voltage is present, go to step 13. Otherwise, repair open between purge valve and No. 6 ACG (15 A) fuse in under-dash fuse/relay box.
13. At valve side, measure resistance between terminals **1** and **2**. If about **33 Ω at room temperature**, go to step 14. Otherwise, replace purge valve.
14. Measure between ECM terminal **A4 (VSV, light green/white)** and body ground. If battery voltage is present, go to step 15. Otherwise, go to step 20.
15. Turn ignition OFF. Continue on next page.
