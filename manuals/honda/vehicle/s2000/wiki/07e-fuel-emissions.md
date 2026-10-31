# Fuel and Emissions — Part E

Honda S2000 service manual, printed pages 11-363 through 11-453 (PDF pp. 659–749).

### Printed page 11-363

<a id="p659"></a>
Source: [PDF p.659, printed p.11-363](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0659.png).

## F-CAN circuit troubleshooting (continued)

16. Disconnect the VSA modulator-control unit 47P connector.
17. Disconnect the steering angle sensor 5P connector.
18. Check for continuity between ECM connector terminal **E11 (CANH, RED)** and body ground. **YES:** Repair a short between E11 and the VSA unit, steering angle sensor, or DLC. **NO:** Go to step 19.
19. Check for continuity between ECM connector terminal **E24 (CANL, WHT)** and body ground. **YES:** Repair a short between E24 and the VSA unit, steering angle sensor, or DLC. **NO:** Go to step 20.

Both checks use ECM connector E (31P), wire side of female terminals. The connector diagrams are in the source image. Procedure continues on the next page.

---

### Printed page 11-364

<a id="p660"></a>
Source: [PDF p.660, printed p.11-364](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0660.png).

## F-CAN circuit troubleshooting (continued)

20. Check continuity between VSA modulator-control unit 47P connector terminal **47 (GND, BLK)** and body ground. **YES:** Go to step 21. **NO:** Repair the open between terminal 47 and body ground **G303**.
21. Check continuity between steering angle sensor 5P connector terminal **1 (GND, BLK)** and body ground. **YES:** Go to step 22. **NO:** Repair the open between terminal 1 and body ground **G401**.
22. Reconnect the VSA modulator-control unit 47P connector.
23. Connect the HDS (p. 11-213).
24. Turn ignition ON (II) and read the HDS. **Vehicle identified:** Replace the steering angle sensor (p. 19-124). **Not identified:** Go to step 25.

The connector views are in the source image.

---

### Printed page 11-365

<a id="p661"></a>
Source: [PDF p.661, printed p.11-365](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0661.png).

## F-CAN circuit troubleshooting (continued)

25. Substitute a known-good ECM (p. 11-217).
26. Turn ignition ON (II) and read the HDS. **Vehicle identified:** The system is OK now; replace the original ECM (p. 11-389). **Not identified:** Replace the VSA modulator-control unit (p. 19-127).

---

### Printed page 11-366

<a id="p662"></a>
Source: [PDF p.662, printed p.11-366](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0662.png).

## MIL circuit troubleshooting

1. Turn ignition ON (II).
2. Run the gauge self-diagnostic function (p. 22-60). **MIL flashes:** Go to step 3. **No flash:** Substitute a known-good gauge assembly and recheck; if the MIL circuit works, replace the original gauge assembly (p. 22-89).
3. Connect the HDS to the DLC (p. 11-213).
4. Check SCS in the HDS DATA LIST. **Short indicated:** Go to step 5. **No short:** Update ECM software if needed (p. 11-216), or substitute a known-good ECM (p. 11-217), then recheck. If the symptom disappears with the known-good ECM, replace the original ECM (p. 11-389).
5. Turn ignition OFF.
6. Disconnect ECM connector E (31P), then disconnect the HDS.
7. Check continuity between ECM connector **E29 (SCS, BRN)** and body ground. **Continuity:** Repair the short between E29 and the SRS unit, EPS control unit, or DLC. **No continuity:** Update ECM software if needed (p. 11-216), or substitute a known-good ECM (p. 11-217), then recheck. If the symptom disappears, replace the original ECM (p. 11-389).

The E29 connector location is shown in the source image.

---

### Printed page 11-367

<a id="p663"></a>
Source: [PDF p.663, printed p.11-367](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0663.png).

DLC Circuit Troubleshooting
NOTE: Before you begin, make sure the HDS and the DLC cable are working properly.
1. Turn the ignition switch OFF.
2. Connect the HDS to the DLC (see page 11-213).
NOTE: Make sure the HDS is properly connected to the DLC.
3. Turn the ignition switch ON (II), and read the HDS.
Does the HDS identify the vehicle?
Y E S — G o to step 4.
N O — G o to step 22.
4. Check the Temporary DTCs or DTCs in the PGM-FI system with the HDS.
Are any Temporary DTCs or DTCs indicated?
Y E S — G o to the indicated D T C s troubleshooting. •
NO—Go to step 5.
5. Turn the ignition switch OFF.
6. Turn the ignition switch ON (II), and watch the S R S indicator.
Does the SRS indicator stay ON ?
Y E S — G o to the S R S system's general troubleshooting information (see page 23-24). •
N O — G o to step 7.
7. Turn the ignition switch OFF.
8. Turn the ignition switch ON (II), and watch the V S A indicator.
Does the VSA indicator stay ON?
Y E S — G o to the V S A system's general troubleshooting information (see page 19-69).•
NO—Go to step 9.
9. Turn the ignition switch OFF.
10. Turn the ignition switch ON (II), and watch the immobilizer indicator.
Does the immobilizer indicator stay on?
Y E S — G o to the immobilizer system check (see page 22-213). •
NO—Go to step 11.
11. Turn the ignition switch OFF.
12. Start the engine, and watch the EPS indicator.
Does the EPS indicator stay on?
Y E S — G o to the E P S system's general troubleshooting information (see page 17-17). •
N O -
• With TPMS: go to step 13.
• Without TPMS: go to step 15.
(cont'd)
11-367

---

### Printed page 11-368

<a id="p664"></a>
Source: [PDF p.664, printed p.11-368](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0664.png).

PGM-FI System DLC Circuit Troubleshooting (cont'd)

13. Turn the ignition switch OFF.
14. Start the engine, and watch the TPMS indicator.
Does the TPMS indicator stay ON?
YES — Go to the TPMS's general troubleshooting information (see page 18-51).
NO — Go to step 15.

15. Do the gauge self-diagnostic function without the HDS (see page 22-60).
Are all the indicator flashing?
YES — Go to step 16.
NO — Troubleshoot the gauge assembly.

16. Turn the ignition switch OFF.
17. Disconnect the HDS from the DLC.
18. Check for continuity between DLC terminals No. 1 and No. 7 and body ground individually.

DATA LINK CONNECTOR (DLC)
DIAG-H K-LINE
(LT BLU) (GRY)
DLC 1 DIAG-H (LT BLU); DLC 7 K-line (GRY). See source image for connector orientation.
Terminal side of female terminals

Is there continuity?
YES — Go to step 19.
NO — Go to step 20.

19. Continue to check for continuity between DLC terminals No. 1 and No. 7 and body ground individually, while disconnecting these parts, one at a time:
• EPS control unit (14P) connector
• Immobilizer control unit-receiver (7P) connector
• SRS unit connector A (28P)
• VSA modulator-control unit (47P) connector
• Gauge assembly A (22P) connector
• TPMS control unit (20P) connector (with TPMS)

DATA LINK CONNECTOR (DLC)
DIAG-H K-LINE
(LT BLU) (GRY)
DLC 1 DIAG-H (LT BLU); DLC 7 K-line (GRY). See source image for connector orientation.
Terminal side of female terminals

Does continuity go away when one of the above components is disconnected?
YES — Replace the part that caused an open when it was disconnected.
NO — Repair short in the wire between the DLC (DIAG-H) and the EPS control unit or the immobilizer control unit-receiver or the DLC (K-line) and the gauge assembly, the SRS unit, the VSA modulator-control unit, and the TPMS control unit (with TPMS).

11-368

---

### Printed page 11-369

<a id="p665"></a>
Source: [PDF p.665, printed p.11-369](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0665.png).

## DLC circuit troubleshooting (continued)

20. Ground DLC terminals **1 (DIAG-H, LT BLU)** and **7 (K-line, GRY)** with jumper wires.
21. Check continuity from body ground to each unit terminal in this chart:

| Unit connector | Unit terminal | DLC terminal |
|---|---|---|
| SRS unit A (28P) | 24 (GRY) | 7 (GRY) |
| Gauge assembly A (22P) | 11 (GRY) | 7 (GRY) |
| VSA modulator-control unit (47P) | 2 (GRY) | 7 (GRY) |
| TPMS control unit (20P) | 7 (GRY) | 7 (GRY) |
| Immobilizer control unit-receiver (7P) | 3 (LT BLU) | 1 (LT BLU) |
| EPS control unit (14P) | 14 (LT BLU) | 1 (LT BLU) |

**Continuity to each:** Replace the control unit that does not communicate with the HDS. **Missing continuity:** Repair the open between the DLC K-line or DIAG-H and the appropriate connector.
22. Turn ignition OFF.
23. Disconnect the HDS from the DLC.
24. Measure voltage between DLC terminal **16 (+B, WHT/GRN)** and body ground. **Battery voltage:** Go to step 25. **No battery voltage:** Repair the open between DLC terminal 16 and No. 46 ACGS (15 A) fuse in the under-hood fuse/relay box.

DLC connector orientation and jumper placement are shown in the source image.

---

### Printed page 11-370

<a id="p666"></a>
Source: [PDF p.666, printed p.11-370](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0666.png).

# PGM-FI System
## DLC Circuit Troubleshooting (cont'd)

**25.** Measure voltage between DLC terminals No. 4 and No. 16.

### DATA LINK CONNECTOR (DLC)
- **GND**: BLK
- **+B**: WHT/GRN
- *Terminal side of female terminals*

**Is there battery voltage?**
- **YES** — Go to step 26.
- **NO** — Repair open in the wire between the DLC terminal (No. 4) and body ground (G401).

**26.** Connect the HDS to the DLC (see page 11-213).

**27.** Jump the SCS line with the HDS.

**28.** Disconnect ECM connector E (31P).

**29.** Disconnect the HDS from the DLC.

**30.** Connect DLC terminal No. 6 to body ground with a jumper wire.

### DATA LINK CONNECTOR (DLC)
- **CANH**: RED
- *Terminal side of female terminals*
- Pins: 1, 4, 5, 6, 7, 9, 11, 12, 13, 14, 16
- **JUMPER WIRE**

**31.** Check for continuity between ECM connector terminal E11 and body ground.

### ECM CONNECTOR E (31P)
- *Wire side of female terminals*
- Pins: 1, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 27, 28, 29, 30
- **CANH (RED)**

**Is there continuity?**
- **YES** — Go to step 32.
- **NO** — Repair open in the wire between the ECM (E11) and DLC terminal No. 6.

*Page Reference: 11-370*

---

### Printed page 11-371

<a id="p667"></a>
Source: [PDF p.667, printed p.11-371](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0667.png).

## DLC circuit troubleshooting (continued)

32. Disconnect the jumper wire.
33. Ground DLC terminal **14 (CANL, WHT)** with a jumper wire.
34. Check continuity between ECM connector **E24 (CANL, WHT)** and body ground. **Continuity:** Go to step 35. **No continuity:** Repair the open between ECM E24 and DLC terminal 14.
35. Try to start the engine. **Starts and idles smoothly:** Go to F-CAN circuit troubleshooting (p. 11-360). **Otherwise:** Go to step 36.
36. Turn ignition OFF.
37. Inspect No. 42 IG1 MAIN (40 A) fuse in the under-hood fuse/relay box. **Fuse OK:** Repair the open between fuse and ignition switch; if wire is OK, go to step 38. **Fuse blown:** Repair the short between the fuse and under-hood fuse/relay box and replace the fuse.
38. Inspect No. 46 ACGS (15 A) fuse in the under-hood fuse/relay box. **Fuse OK:** Go to step 45. **Fuse blown:** Go to step 39.

The source image shows the DLC and ECM connector orientations.

---

### Printed page 11-372

<a id="p668"></a>
Source: [PDF p.668, printed p.11-372](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0668.png).

## DLC circuit troubleshooting (continued)

39. Remove the blown No. 46 ACGS (15 A) fuse from the under-hood fuse/relay box.
40. Remove PGM-FI main relay 1 (FI MAIN).
41. Check continuity from body ground to PGM-FI main relay 1 4P connector terminals **1 and 4**, separately. **Continuity:** Repair the short between No. 46 ACGS fuse and the relay; replace the fuse. **No continuity:** Go to step 42.
42. Disconnect each of these, one at a time, and check continuity between relay 1 terminal **2 (IGP, YEL/BLK)** and body ground: PGM-FI main relay 2 (FUEL PUMP), ECM connector A (31P), each injector 2P connector, CMP sensor 3P connector, CKP sensor 3P connector. **Continuity disappears when a part is disconnected:** Replace that part. If it is the ECM, update software if needed (p. 11-216) or substitute a known-good ECM (p. 11-217); replace original ECM if symptom disappears (p. 11-389). Also replace No. 46 ACGS fuse. **Continuity persists:** Go to step 43.
43. Disconnect connectors from PGM-FI main relay 2, ECM connector A, injectors, CMP sensor, and CKP sensor.

---

### Printed page 11-373

<a id="p669"></a>
Source: [PDF p.669, printed p.11-373](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0669.png).

## DLC circuit troubleshooting (continued)

44. Check continuity between PGM-FI main relay 1 (FI MAIN) 4P connector terminal **2 (IGP, YEL/BLK)** and body ground. **Continuity:** Repair the short between relay 1 and the items disconnected in step 43; replace No. 46 ACGS (15 A) fuse. **No continuity:** Replace relay 1 and No. 46 ACGS fuse.
45. Inspect No. 2 FUEL PUMP SRS (15 A) fuse in the under-dash fuse/relay box. **Fuse OK:** Go to step 58. **Blown:** Go to step 46.
46. Remove the blown No. 2 FUEL PUMP SRS fuse.
47. Jump the SCS line with the HDS.
48. Disconnect ECM connector E (31P).
49. Check continuity between ECM connector **E9 (IG1)** and body ground. **Continuity:** Go to step 50. **No continuity:** Replace No. 2 FUEL PUMP SRS fuse, then update ECM software if needed (p. 11-216) or substitute a known-good ECM (p. 11-217). If symptom disappears with known-good ECM, replace original ECM (p. 11-389).
50. Remove PGM-FI main relay 2 (FUEL PUMP).

---

### Printed page 11-374

<a id="p670"></a>
Source: [PDF p.670, printed p.11-374](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0670.png).

PGM-FI System DLC Circuit Troubleshooting (cont'd)

51. Check for continuity between ECM connector terminal E9 and body ground.

ECM CONNECTOR E (31P)
IG1 at ECM E9; see source image for connector orientation.
Wire side of female terminals

Is there continuity?
YES—Repair short in the wire between the No. 2 FUEL PUMP S R S (15 A) fuse, the ECM (E9), and PGM-FI main relay 2 (FUEL PUMP). Also replace the No. 2 FUEL PUMP S R S (15 A) fuse.
NO—Go to step 52.

52. Remove the rear tray (see page 20-73).
53. Remove the access panel from the floor.
54. Disconnect the fuel pump 5P connector.
55. Check for continuity between fuel pump 5P connector terminal No. 5 and body ground.

FUEL PUMP 5P CONNECTOR
Terminal 5, YEL/GRN; see source image for connector orientation.
Wire side of female terminals

Is there continuity?
YES—Repair short in the wire between the fuel pump and PGM-FI main relay 2 (FUEL PUMP). Also replace the No. 2 FUEL PUMP S R S (15 A) fuse.
NO—Go to step 56.

56. Reinstall PGM-FI main relay 2 (FUEL PUMP).
57. Check for continuity between fuel pump 5P connector terminal No. 5 and body ground.

FUEL PUMP 5P CONNECTOR
Terminal 5, YEL/GRN; see source image for connector orientation.
Wire side of female terminals

Is there continuity?
YES—Replace PGM-FI main relay 2 (FUEL PUMP). Also replace the No. 2 FUEL PUMP S R S (15 A) fuse.
NO—Check the fuel pump, and replace it if necessary. Also replace the No. 2 FUEL PUMP S R S (15 A) fuse.

58. Jump the SCS line with the HDS.
59. Disconnect ECM connector E (31P).
60. Turn the ignition switch ON (II).

Page Reference: 11-374

---

### Printed page 11-375

<a id="p671"></a>
Source: [PDF p.671, printed p.11-375](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0671.png).

## DLC circuit troubleshooting (continued)

61. Measure voltage between ECM connector **E9 (IG1, BLK/YEL)** and body ground. **Battery voltage:** Go to step 62. **No battery voltage:** Repair the open between No. 2 FUEL PUMP SRS (15 A) fuse and ECM E9.
62. Measure voltage between ECM connector **E7 (MRLY, GRN)** and body ground. **Battery voltage:** Go to step 67. **No battery voltage:** Go to step 63.
63. Turn ignition OFF.
64. Remove PGM-FI main relay 1 (FI MAIN).
65. Measure voltage between relay 1 4P connector terminal **4** and body ground. **Battery voltage:** Go to step 66. **No battery voltage:** Repair the open between No. 46 ACGS (15 A) fuse and relay 1.

Connector orientation is shown in the source image.

---

### Printed page 11-376

<a id="p672"></a>
Source: [PDF p.672, printed p.11-376](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0672.png).

Step 66: Check for continuity between PGM-FI main relay 1 (Fl MAIN) 4P connector terminal No. 3 and ECM connector terminal E7.

**Decision Path:**
- **Is there continuity?**
  - **YES**: Test PGM-FI main relay 1 (see page 22-48). If the relay is OK, update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217), then recheck. If the symptom/indication goes away with a known-good ECM, replace the original ECM (see page 11-389).
  - **NO**: Repair open in the wire between PGM-FI main relay 1 (Fl MAIN) and the ECM (E7).

Step 67: Reconnect ECM connector E (31P).
Step 68: Turn the ignition switch ON (II).
Step 69: Measure voltage between body ground and ECM connector terminals A2 and A3 individually.

**Decision Path:**
- **Is there battery voltage?**
  - **YES**: Go to step 76.
  - **NO**: Go to step 70.

Step 70: Turn the ignition switch OFF.
Step 71: Remove PGM-FI main relay 1 (Fl MAIN) (A).
Step 72: Turn the ignition switch ON (II).

---

### Printed page 11-377

<a id="p673"></a>
Source: [PDF p.673, printed p.11-377](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0673.png).

## DLC circuit troubleshooting (continued)

73. Measure voltage between PGM-FI main relay 1 (FI MAIN) 4P connector terminal **1 (+B, WHT/GRN)** and body ground. **Battery voltage:** Go to step 74. **No battery voltage:** Repair the open between No. 46 ACGS (15 A) fuse and relay 1.
74. Turn ignition OFF.
75. Check continuity between relay 1 4P connector terminal **2 (IGP, YEL/BLK)** and ECM connector terminals **A2 and A3 (IGP2/IGP1, YEL/BLK)** individually. **Continuity:** Replace relay 1. **No continuity:** Repair the open between relay 1 and ECM A2/A3.

Connector orientation is shown in the source image.

---

### Printed page 11-378

<a id="p674"></a>
Source: [PDF p.674, printed p.11-378](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0674.png).

## DLC circuit troubleshooting (continued)

76. Measure voltage between body ground and ECM connector terminals **A4, A5, A8, A9, and E3**, individually. **Less than 1.0 V:** Go to step 77. **More than 1.0 V:** Repair the open between ground G101 and the affected ECM terminal(s). The source image identifies PG1/PG2 and LG1/LG2/LG3 wires on ECM connectors A and E.
77. Measure voltage between body ground and ECM **A21 (VCC1, YEL/RED)**. **About 5 V:** Go to step 83. **Otherwise:** Go to step 78.
78. Disconnect the MAP sensor 3P connector; with ignition ON (II), measure voltage between body ground and ECM A21 again. **About 5 V:** Replace MAP sensor (p. 11-384). **Otherwise:** Go to step 79.

Refer to the source image for connector orientation.

---

### Printed page 11-379

<a id="p675"></a>
Source: [PDF p.675, printed p.11-379](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0675.png).

## DLC circuit troubleshooting (continued)

79. Turn ignition OFF.
80. Jump the SCS line with the HDS.
81. Disconnect ECM connector A (31P).
82. Check continuity between ECM **A21 (VCC1, YEL/RED)** and body ground. **Continuity:** Repair the short between ECM A21 and the MAP sensor. **No continuity:** Update ECM software if needed (p. 11-216), or substitute a known-good ECM (p. 11-217). If the symptom disappears, replace original ECM (p. 11-389).
83. Measure voltage between body ground and ECM **A20 (VCC2, YEL/BLU)**. **About 5 V:** Go to step 91. **Otherwise:** Go to step 84.
84. Turn ignition OFF.
85. Disconnect the APP sensor A and output shaft (countershaft) speed sensor connectors, one at a time. With ignition ON (II), measure voltage between body ground and ECM A20. **About 5 V after a sensor is disconnected:** Replace that sensor. **Otherwise:** Go to step 86.

Refer to the source image for connector orientation.

---

### Printed page 11-380

<a id="p676"></a>
Source: [PDF p.676, printed p.11-380](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0676.png).

## DLC circuit troubleshooting (continued)

86. Turn ignition OFF.
87. Jump the SCS line with the HDS.
88. Disconnect the APP sensor A and output shaft (countershaft) speed sensor connectors.
89. Disconnect ECM connector A (31P).
90. Check continuity between ECM **A20 (VCC2, YEL/BLU)** and body ground. **Continuity:** Repair the short between ECM A20 and APP sensor A or output shaft speed sensor. **No continuity:** Update ECM software if needed (p. 11-216), or substitute a known-good ECM (p. 11-217). If the symptom disappears, replace original ECM (p. 11-389).
91. Measure voltage between body ground and ECM **E5 (VCC3, YEL/BLU)**. **About 5 V:** Update ECM software if needed (p. 11-216), or substitute a known-good ECM (p. 11-217). If the symptom disappears, replace original ECM (p. 11-389). **Otherwise:** Go to step 92.
92. Turn ignition OFF.

The source image confirms the two column decision paths and connector terminals.

---

### Printed page 11-381

<a id="p677"></a>
Source: [PDF p.677, printed p.11-381](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0677.png).

## DLC circuit troubleshooting (continued)

93. Disconnect the FTP sensor and APP sensor B connectors, one at a time. With ignition ON (II), measure voltage between body ground and ECM **E5 (VCC3, YEL/BLU)**. **About 5 V after a sensor is disconnected:** Replace that sensor. **Otherwise:** Go to step 94.
94. Turn ignition OFF.
95. Jump the SCS line with the HDS.
96. Disconnect both FTP sensor and APP sensor B connectors.
97. Disconnect ECM connector E (31P).
98. Check continuity between ECM E5 and body ground. **Continuity:** Repair the short between ECM E5 and FTP sensor or APP sensor B. **No continuity:** Update ECM software if needed (p. 11-216), or substitute a known-good ECM (p. 11-217). If the symptom disappears, replace original ECM (p. 11-389).

Refer to the source image for connector orientation.

---

### Printed page 11-382

<a id="p678"></a>
Source: [PDF p.678, printed p.11-382](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0678.png).

# PGM-FI System
## Injector replacement

1. Relieve the fuel pressure (see page 11-474).
2. Remove the fuel rail cover (**A**).
3. Disconnect the connectors (**B**) from the injectors, then remove the harness holder (**C**) from the fuel rail (**D**).
4. Disconnect the quick-connect fitting (**E**) from the fuel rail.
5. Remove the retainer nuts (**F**) and bolts (**G**) from the fuel rail.
6. Disconnect the fuel rail from the intake manifold (**H**).
7. Remove the injector clips (**I**) from the fuel rail.
8. Remove the injectors (**J**) from the fuel rail.
9. Remove the O-rings (**K**) from the injector.

11-382

---

### Printed page 11-383

<a id="p679"></a>
Source: [PDF p.679, printed p.11-383](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0679.png).

## Injector replacement (continued)

10. Coat new O-rings (A) with clean engine oil and put them on the injectors (B).
11. Insert the injectors into the fuel rail (C).
12. Install the injector clips (D).
13. Install the injectors in the intake manifold (E).
14. Install and tighten the retainer nuts and bolts.
15. Connect the quick-connect fitting (F) (p. 11-483).
16. Connect the injector connectors and harness holder.
17. Install the injector cover (G).
18. Turn ignition ON (II) without operating the starter. After the fuel pump runs for about 2 seconds, fuel pressure rises. Repeat 2 or 3 times, then check for fuel leakage.

---

### Printed page 11-384

<a id="p680"></a>
Source: [PDF p.680, printed p.11-384](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0680.png).

# PGM-FI System

## MAP Sensor Replacement

1. Disconnect the MAP sensor 3P connector (A).
2. Remove the bolt (B).
3. Remove the MAP sensor (C).
4. Install the parts in the reverse order of removal with a new O-ring (D).

## IAT Sensor Replacement

1. Disconnect the IAT sensor 2P connector (A).
2. Remove the clip (B) and the IAT sensor (C).
3. Install the parts in the reverse order of removal.

**Reference:** 11-384

---

### Printed page 11-385

<a id="p681"></a>
Source: [PDF p.681, printed p.11-385](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0681.png).

# S2000 Fuel and Emissions Part E - Page 681

## ECT Sensor 1 Replacement

1. Drain the engine coolant (see page 10-9).
2. Disconnect the E C T sensor 1 2P connector (A).
3. Remove E C T sensor 1 (B).
4. Install the parts in the reverse order of removal with a new O-ring (C).
5. Refill the radiator with engine coolant (see page 10-9).

## ECT Sensor 2 Replacement

1. Drain the engine coolant (see page 10-9).
2. Remove the splash shield.
3. Disconnect the E C T sensor 2 2P connector (A), then remove E C T sensor 2 (B).
4. Install E C T sensor 2 with a new O-ring (C).
5. Install the splash shield.
6. Refill the radiator with engine coolant (see page 10-9).

**Page Reference:** 11-385

---

### Printed page 11-386

<a id="p682"></a>
Source: [PDF p.682, printed p.11-386](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0682.png).

## A/F sensor replacement

Special tool: O2 sensor wrench, Snap-on YA8875 or SWR2, or equivalent.

1. Disconnect the A/F sensor (Sensor 1) 4P connector (A).
2. Remove the A/F sensor (Sensor 1) (A). **Tightening torque: 44 N·m (4.5 kgf·m, 33 lbf·ft).**
3. Install parts in reverse order of removal.

## Secondary HO2S replacement

Special tool: O2 sensor wrench, Snap-on YA8875 or SWR2, or equivalent.

1. Disconnect the secondary HO2S (Sensor 2) 4P connector (A).
2. Remove the secondary HO2S (Sensor 2) (A). **Tightening torque: 44 N·m (4.5 kgf·m, 33 lbf·ft).**
3. Install parts in reverse order of removal.

The source image shows both sensor locations and the torque callouts.

---

### Printed page 11-387

<a id="p683"></a>
Source: [PDF p.683, printed p.11-387](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0683.png).

# CMP sensor replacement and CKP sensor replacement

**NOTE:** The CMP sensor is on the exhaust side of the cylinder head.

## CMP Sensor Replacement
1. Disconnect the CMP sensor 3P connector (A).
2. Remove the CMP sensor (B) from the exhaust camshaft side of the cylinder head.
3. Install the parts in the reverse order of removal with a new O-ring (C).

## CKP Sensor Replacement
1. Remove the CKP sensor (A).
2. Disconnect the CKP sensor 3P connector (B).
3. Install the parts in the reverse order of removal with a new O-ring (C).
4. Do the crank (CKP) pattern clear/pattern learn procedure (see page 11-214).

**Page Reference:** 11-387

---

### Printed page 11-388

<a id="p684"></a>
Source: [PDF p.684, printed p.11-388](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0684.png).

## Output shaft (countershaft) speed sensor replacement

1. Disconnect the output shaft speed sensor 3P connector (A).
2. Remove the output shaft speed sensor (B). **Tightening torque: 12 N·m (1.2 kgf·m, 8.7 lbf·ft).**
3. Install parts in reverse order of removal with a new O-ring (C).

## Knock sensor replacement

1. Remove the intake manifold (p. 9-3).
2. Disconnect the knock sensor 1P connector (A).
3. Remove the knock sensor (B). **Tightening torque: 31 N·m (3.2 kgf·m, 23 lbf·ft).**
4. Install parts in reverse order of removal.

The source image separates the two procedures and shows torque callouts.

---

### Printed page 11-389

<a id="p685"></a>
Source: [PDF p.685, printed p.11-389](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0685.png).

# ECM Replacement
## Special Tools Required
* Honda diagnostic system (HDS) tablet tester
* Honda interface module (HIM) and an iN workstation with HDS and CM update software
* HDS pocket tester
* GNA-600 and an iN workstation with HDS and CM update software

Use any one of these update tools.

**NOTE:**
* Make sure the HDS is loaded with the latest software version.
* If you are replacing the ECM after substituting a known-good ECM, reinstall the original ECM, then do this procedure.
* During the procedure, if any READ DATA, WRITE DATA, or other data checks fail, note the failure, then continue.

1. Connect the HDS to the data link connector (DLC) (A) located under the driver's side of front console.
2. Turn the ignition switch ON (II).
3. Make sure the HDS communicates with the ECM and other vehicle systems. If it doesn't, go to the DLC circuit troubleshooting (see page 11-367). If you are returning from DLC circuit troubleshooting, skip steps 4 through 7, 17 through 19, and 22 through 23, and do this after replacing the ECM:
   * Replace the engine oil (see page 8-6) and the engine oil filter (see page 8-7).
   * Clean the throttle body (see page 11-499).
4. Select the PGM-FI system with the HDS.
5. Select the INSPECTION MENU with the HDS.
6. Select the ETCS TEST, then select the TP POSITION CHECK, and follow the screen prompts.

**NOTE:** If the TP POSITION CHECK indicates FAILED, continue with this procedure.

7. Select the REPLACE ECM MENU, then select READ DATA, and follow the screen prompts.

**NOTE:**
* Doing this step copies (READS) the engine oil life data from the original ECM so you can later download (WRITES) it into the new ECM.
* If READ DATA indicates FAILED, continue with this procedure.

8. Turn the ignition switch OFF.
9. Jump the SCS line with the HDS.
10. Remove the left side kick panel (see page 20-71) to expose the ECM.

(cont'd)

**Page Reference:** 11-389

---

### Printed page 11-390

<a id="p686"></a>
Source: [PDF p.686, printed p.11-390](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0686.png).

# PGM-FI System
## ECM Replacement (cont'd)

11. Disconnect the E C M connectors (A).
12. Remove the bolts (B) then remove the E C M (C).
13. Install the E C M in the reverse order of removal.
14. Open the S C S with the HDS.
15. Turn the ignition switch ON (II).
16. Manually input the VIN to the ECM with the HDS.

> **NOTE:** DTC P0630 "VIN Not Programmed or Mismatch" may be stored because the VIN has not been programmed into the ECM; ignore it, and continue this procedure.

17. If READ DATA failed in step 7, go to step 20, otherwise to step 18.
18. Select the PGM-FI system with the HDS.
19. Select the REPLACE E C M MENU, then select WRITE DATA, and follow the screen prompts.

> **NOTE:** If the WRITE DATA indicates FAILED, continue with this procedure.

20. Select the IMMOBI system with the HDS.
21. Enter the immobilizer code with the E C M replacement procedure in the HDS; it allows you to start the engine.
22. If the TP POSITION CHECK failed in step 6 clean the throttle body (see page 11-499), then go to step 23.
23. If the READ DATA failed in step 7 or the WRITE DATA failed in step 19, replace the engine oil (see page 8-6) and engine oil filter (see page 8-7), then go to step 24.
24. Select the PGM-FI system, and reset the ECM with the HDS.
25. Update the E C M if it does not have the latest software (see page 11-216).
26. Do the ECM idle learn procedure (see page 11-462).
27. Do the CKP pattern learn procedure (see page 11-214).

**Page Reference:** 11-390

---

### Printed page 11-391

<a id="p687"></a>
Source: [PDF p.687, printed p.11-391](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0687.png).

## Electronic throttle control system — component location index

**Engine control module (ECM):** Updating, p. 11-216; substitution, p. 11-217; replacement, p. 11-389.

---

### Printed page 11-392

<a id="p688"></a>
Source: [PDF p.688, printed p.11-392](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0688.png).

# Electronic Throttle Control System
## DTC Troubleshooting
### DTC P0122: TP Sensor A Circuit Low Voltage

**NOTE:** Before you troubleshoot record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Check TP S E N S O R A in the DATA LIST with the HDS.
   Is there about 0.3 V or less?
   - **Y E S** — G o to step 4.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the throttle actuator control module.

4. Check for Temporary DTCs or DTCs with the HDS.
   Are DTC P0122 and P0222 indicated at the same time?
   - **Y E S** — G o to step 9.
   - **N O** — G o to step 5.

5. Turn the ignition switch OFF.
6. Disconnect the throttle body 6P connector.
7. Disconnect the throttle actuator control module 16P connector.
8. Check for continuity between throttle body 6P connector terminal No. 1 and body ground.
   **T H R O T T L E B O D Y 6P C O N N E C T O R**

   TPSA is at throttle body terminal 1 (RED/BLK); see source image.

Is there continuity?
   - **YES** — Repair short in the wire between the throttle body and the throttle actuator control module (TPSA line), then go to step 17.
   - **NO** — Substitute a known-good throttle actuator control module (see page 11-437), then go to step 17 and recheck. If DTC P0122 is not indicated, replace the original throttle actuator control module (see page 11-437), then go to step 17. If DTC P0122 is indicated, go to step 15.

Source printed page: 11-392

---

### Printed page 11-393

<a id="p689"></a>
Source: [PDF p.689, printed p.11-393](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0689.png).

# S2000 Fuel and Emissions Part E
## Page 689

### Step 9
Measure voltage between throttle body 6P connector terminal No. 2 and body ground.

**T H R O T T L E B O D Y 6P C O N N E C T O R**
Connector orientation: see source image.

Is there about 5 V?
- **YES** — Go to step 15.
- **NO** — Go to step 10.

### Step 10
Turn the ignition switch OFF.

### Step 11
Disconnect the throttle actuator control module 16P connector (see page 11-437).

### Step 12
Disconnect the throttle body 6P connector.

### Step 13
Connect throttle body 6P connector terminal No. 2 to body ground with a jumper wire.

**T H R O T T L E B O D Y 6P C O N N E C T O R**
Connector orientation: see source image.

### Step 14
Check for continuity between throttle actuator control module 16P connector terminal No. 11 and body ground.

**T H R O T T L E A C T U A T O R C O N T R O L M O D U L E 16P**
Connector orientation: see source image.

Is there continuity?
- **YES** — Substitute a known-good throttle actuator control module (see page 11-437), then go to step 17 and recheck. If DTC P0122 is not indicated, replace the original throttle actuator control module (see page 11-437), then go to step 17. If DTC P0122 is indicated, go to step 15.
- **NO** — Repair open in the wire between the throttle body and the throttle actuator control module (VCC line), then go to step 17.

*(cont'd)*

Source printed page: 11-393

---

### Printed page 11-394

<a id="p690"></a>
Source: [PDF p.690, printed p.11-394](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0690.png).

## Electronic throttle control — DTC P0122 troubleshooting (continued)

15. Turn ignition OFF.
16. Replace the throttle body (p. 11-500).
17. Reconnect all connectors.
18. Turn ignition ON (II).
19. Reset the ECM with the HDS.
20. Do the ECM idle learn procedure (p. 11-462).
21. Check for Temporary DTCs or DTCs with the HDS. **P0122 indicated:** Check for poor connections or loose terminals at the throttle body and throttle actuator control module, then return to step 1. **Not indicated:** Troubleshooting is complete. If other DTCs are indicated, follow their troubleshooting procedures.

---

### Printed page 11-395

<a id="p691"></a>
Source: [PDF p.691, printed p.11-395](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0691.png).

# DTC P0123: TP Sensor A Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Check TP SENSOR A in the DATA LIST with the HDS.
   Is there about 4.8 V or more?
   - **YES** — Go to step 4.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the throttle actuator control module.

4. Check for Temporary DTCs or DTCs with the HDS.
   Are DTC P0123 and P0223 indicated at the same time?
   - **YES** — Go to step 13.
   - **NO** — Go to step 5.

5. Turn the ignition switch OFF.
6. Disconnect the throttle body 6P connector.
7. Turn the ignition switch ON (II).
8. Measure voltage between throttle body 6P connector terminal No. 1 and body ground.

   **THROTTLE BODY 6P CONNECTOR**
   Connector orientation: see source image.
   Is there about 5 V?
   - **YES** — Go to step 18.
   - **NO** — Go to step 9.

9. Turn the ignition switch OFF.
10. Disconnect the throttle actuator control module 16P connector (see page 11-437).
11. Connect throttle body 6P connector terminal No. 1 to body ground with a jumper wire.

    **THROTTLE BODY 6P CONNECTOR**
    Connector orientation: see source image.

11-395

---

### Printed page 11-396

<a id="p692"></a>
Source: [PDF p.692, printed p.11-396](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0692.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)

### 12. Check for continuity between throttle actuator control module 16P connector terminal No. 10 and body ground.

**T H R O T T L E A C T U A T O R C O N T R O L M O D U L E 16P CONNECTOR**
Connector orientation: see source image.

Is there continuity?

- **YES**—Substitute a known-good throttle actuator control module (see page 11-437), then go to step 18 and recheck. If DTC P0123 is not indicated, replace the original throttle actuator control module (see page 11-437), then go to step 20. If DTC P0123 is indicated, go to step 18.
- **NO**—Repair open in the wire between the throttle body and the throttle actuator control module (TPSA line), then go to step 20.

### 13. Turn the ignition switch OFF.

### 14. Disconnect the throttle body 6P connector.

### 15. Disconnect the throttle actuator control module 16P connector (see page 11-437).

### 16. Connect throttle body 6P connector terminal No. 4 to body ground with a jumper wire.

**THROTTLE BODY 6P CONNECTOR**
Connector orientation: see source image.

### 17. Check for continuity between throttle actuator control module 16P connector terminal No. 9 and body ground.

**T H R O T T L E A C T U A T O R C O N T R O L M O D U L E 16P CONNECTOR**
Connector orientation: see source image.

Is there continuity?

- **YES**—Substitute a known-good throttle actuator control module (see page 11-437), then go to step 20 and recheck. If DTC P0123 is not indicated, replace the original throttle actuator control module (see page 11-437), then go to step 20. If DTC P0123 is indicated, go to step 18.
- **NO**—Repair open in the wire between the throttle body and the throttle actuator control module (SG line), then go to step 20.

Source printed page: 11-396

---

### Printed page 11-397

<a id="p693"></a>
Source: [PDF p.693, printed p.11-397](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0693.png).

## Electronic throttle control — DTC P0123 troubleshooting (continued)

18. Turn ignition OFF.
19. Replace the throttle body (p. 11-500).
20. Reconnect all connectors.
21. Turn ignition ON (II).
22. Reset the ECM with the HDS.
23. Do the ECM idle learn procedure (p. 11-462).
24. Check for Temporary DTCs or DTCs with the HDS. **P0123 indicated:** Check for poor connections or loose terminals at the throttle body and throttle actuator control module, then return to step 1. **Not indicated:** Troubleshooting is complete. If other DTCs are indicated, follow their troubleshooting procedures.

---

### Printed page 11-398

<a id="p694"></a>
Source: [PDF p.694, printed p.11-398](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0694.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)
### DTC P0222: TP Sensor B Circuit Low Voltage

> **NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Check TP S E N S O R B in the DATA LIST with the HDS.
   - Is there about 0.3 V or less?
     - **Y E S** — G o to step 4.
     - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the throttle actuator control module.

4. Check for Temporary DTCs or DTCs with the HDS.
   - Are DTC P0122 and P0222 indicated at the same time?
     - **Y E S** — G o to step 9.
     - **N O** — G o to step 5.

5. Turn the ignition switch OFF.
6. Disconnect the throttle body 6P connector.
7. Disconnect the throttle actuator control module 16P connector (see page 11-437).
8. Check for continuity between throttle body 6P connector terminal No. 3 and body ground.

**T H R O T T L E B O D Y 6P C O N N E C T O R**
Connector orientation: see source image.
- Is there continuity?
  - **YES** — Repair short in the wire between the throttle body and the throttle actuator control module (TPSB line), then go to step 17.
  - **NO** — Substitute a known-good throttle actuator control module (see page 11-437), then go to step 17 and recheck. If DTC P0222 is not indicated, replace the original throttle actuator control module (see page 11-437), then go to step 17. If DTC P0222 is indicated, go to step 15.

Source printed page: 11-398

---

### Printed page 11-399

<a id="p695"></a>
Source: [PDF p.695, printed p.11-399](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0695.png).

# Diagnostic Procedure: Throttle Body Voltage and Continuity Check

## Step 9
Measure voltage between throttle body 6P connector terminal No. 2 and body ground.

**Throttle Body 6P Connector Diagram:**
- **Terminals:** 1, 2, 3, 4, 5, 6
- **Pin 2 Label:** VCC (BLU)
- **Note:** Wire side of female terminals

**Result Check:** Is there about 5 V?
- **YES:** Go to step 15.
- **NO:** Go to step 10.

## Step 10
Turn the ignition switch OFF.

## Step 11
Disconnect the throttle actuator control module 16P connector (see page 11-437).

## Step 12
Disconnect the throttle body 6P connector.

## Step 13
Connect throttle body 6P connector terminal No. 2 to body ground with a jumper wire.

**Throttle Body 6P Connector Diagram (Jumper Wire View):**
- **Terminals:** 3, 4, 5, 6
- **Pin Label:** VCC (BLU)
- **Note:** Wire side of female terminals

## Step 14
Check for continuity between throttle actuator control module 16P connector terminal No. 11 and body ground.

**Throttle Actuator Control Module 16P Connector Diagram:**
- **Terminals:** 1, 2, 6, 7, 8, 9, 10, 11, 12, 14
- **Pin 11 Label:** VCC (BLU)
- **Note:** Wire side of female terminals

**Result Check:** Is there continuity?
- **YES:**
  - Substitute a known-good throttle actuator control module (see page 11-437), then go to step 17 and recheck.
  - If DTC P0222 is not indicated, replace the original throttle actuator control module (see page 11-437), then go to step 17.
  - If DTC P0222 is indicated, go to step 15.
- **NO:** Repair open in the wire between the throttle body and the throttle actuator control module (VCC line), then go to step 17.

Source printed page: (cont'd) 11-399

---

### Printed page 11-400

<a id="p696"></a>
Source: [PDF p.696, printed p.11-400](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0696.png).

## Electronic throttle control — DTC P0222 troubleshooting (continued)

15. Turn ignition OFF.
16. Replace the throttle body (p. 11-500).
17. Reconnect all connectors.
18. Turn ignition ON (II).
19. Reset the ECM with the HDS.
20. Do the ECM idle learn procedure (p. 11-462).
21. Check for Temporary DTCs or DTCs with the HDS. **P0222 indicated:** Check for poor connections or loose terminals at the throttle body and throttle actuator control module, then return to step 1. **Not indicated:** Troubleshooting is complete. If other DTCs are indicated, follow their troubleshooting procedures.

---

### Printed page 11-401

<a id="p697"></a>
Source: [PDF p.697, printed p.11-401](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0697.png).

# DTC P0223: TP Sensor B Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Check TP S E N S O R B in the DATA LIST with the HDS.
   Is there about 4.8 V or more?
   - **Y E S** — G o t o s t e p 4.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the throttle actuator control module.

4. Check for Temporary DTCs or DTCs with the HDS.
   Are DTC P0123 and P0223 indicated at the same time?
   - **Y E S** — G o t o s t e p 13.
   - **NO** — Go to step 5.

5. Turn the ignition switch OFF.
6. Disconnect the throttle body 6P connector.
7. Turn the ignition switch ON (II).
8. Measure voltage between throttle body 6P connector terminal No. 3 and body ground.

   **T H R O T T L E B O D Y 6 P C O N N E C T O R**
   Connector orientation: see source image.
   **TP S B (RED)** Wire side of female terminals

   Is there about 5 V?
   - **Y E S** — G o t o s t e p 18.
   - **N O** — G o to step 9.

9. Turn the ignition switch OFF.
10. Disconnect the throttle actuator control module 16P connector (see page 11-437).
11. Connect throttle body 6P connector terminal No. 3 to body ground with a jumper wire.

    **T H R O T T L E B O D Y 6 P C O N N E C T O R**
    Connector orientation: see source image.
    **J U M P E R W I R E T P S B (RED)** Wire side of female terminals (cont'd)

*Page Reference: 11-401*

---

### Printed page 11-402

<a id="p698"></a>
Source: [PDF p.698, printed p.11-402](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0698.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)

### 12. Check for continuity between throttle actuator control module 16P connector terminal No. 12 and body ground.

**T H R O T T L E A C T U A T O R C O N T R O L M O D U L E 16P CONNECTOR**
Connector orientation: see source image.

Is there continuity ?

- **YES**—Substitute a known-good throttle actuator control module (see page 11-437), then go to step 20 and recheck. If DTC P0223 is not indicated, replace the original throttle actuator control module (see page 11-437), then go to step 20. If DTC P0223 is indicated, go to step 18.
- **NO**—Repair open in the wire between the throttle body and the throttle actuator control module (TPS B line), then go to step 20.

### 13. Turn the ignition switch OFF.

### 14. Disconnect the throttle body 6P connector.

### 15. Disconnect the throttle actuator control module 16P connector (see page 11-437).

### 16. Connect throttle body 6P connector terminal No. 4 to body ground with a jumper wire.

**T H R O T T L E B O D Y 6P CONNECTOR**
Connector orientation: see source image.

### 17. Check for continuity between throttle actuator control module 16P connector terminal No. 9 and body ground.

**T H R O T T L E A C T U A T O R C O N T R O L M O D U L E 16P CONNECTOR**
Connector orientation: see source image.

Is there continuity?

- **YES**—Substitute a known-good throttle actuator control module (see page 11-437), then go to step 20 and recheck. If DTC P0223 is not indicated, replace the original throttle actuator control module (see page 11-437), then go to step 20. If DTC P0223 is indicated, go to step 18.
- **NO**—Repair open in the wire between the throttle body and the throttle actuator control module (SG line), then go to step 20.

Source printed page: 11-402

---

### Printed page 11-403

<a id="p699"></a>
Source: [PDF p.699, printed p.11-403](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0699.png).

## Electronic throttle control — DTC P0223 troubleshooting (continued)

18. Turn ignition OFF.
19. Replace the throttle body (p. 11-500).
20. Reconnect all connectors.
21. Turn ignition ON (II).
22. Reset the ECM with the HDS.
23. Do the ECM idle learn procedure (p. 11-462).
24. Check for Temporary DTCs or DTCs with the HDS. **P0223 indicated:** Check for poor connections or loose terminals at the throttle body and throttle actuator control module, then return to step 1. **Not indicated:** Troubleshooting is complete. If other DTCs are indicated, follow their troubleshooting procedures.

---

### Printed page 11-404

<a id="p700"></a>
Source: [PDF p.700, printed p.11-404](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0700.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)
### DTC P1683: Throttle Valve Default Position

**Spring Performance Problem**

> **CAUTION**
> Do not insert your fingers into the installed throttle body when you turn the ignition switch ON (II) or while the ignition switch is ON (II). If you do, you will seriously injure your fingers if the throttle valve is activated.

> **NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
4. Turn the ignition switch OFF, and wait 10 seconds.
5. Turn the ignition switch ON (II).
6. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P1683 indicated?**
- **YES — Go to step 7.**
- **NO — Intermittent failure, the system is OK at this time.** Check for poor connections or loose terminals at the throttle body and the throttle actuator control module. •

7. Turn the ignition switch OFF.
8. Disconnect the intake air duct from the throttle body.
9. Push the throttle valve to closed as shown.
10. Release the throttle valve.

**Does the throttle valve return?**
- **YES — Clean the throttle body (see page 11-499), then go to step 13 and recheck. If DTC P1683 is indicated, go to step 11.**
- **NO — Go to step 11.**

11. Turn the ignition switch OFF.
12. Replace the throttle body (see page 11-500).
13. Turn the ignition switch ON (II).
14. Reset the ECM with the HDS.
15. Do the ECM idle learn procedure (see page 11-462).
16. Turn the ignition switch OFF, and wait 10 seconds.
17. Turn the ignition switch ON (II).
18. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P1683 indicated?**
- **YES — Check for poor connections or loose terminals at the throttle body and the throttle actuator control module, then go to step 1.**
- **NO — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •**

Source printed page: 11-404

---

### Printed page 11-405

<a id="p701"></a>
Source: [PDF p.701, printed p.11-405](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0701.png).

# DTC P1684: Throttle Valve Return Spring

## Performance Problem

**CAUTION**: Do not insert your fingers into the installed throttle body when you turn the ignition switch ON (II) or while the ignition switch is ON (II). If you do, you will seriously injure your fingers if the throttle valve is activated.

**NOTE**: Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
4. Turn the ignition switch OFF, and wait 10 seconds.
5. Turn the ignition switch ON (II).
6. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P1684 indicated?**
- **YES** — Go to step 7.
- **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the throttle actuator control module. •

7. Turn the ignition switch OFF.
8. Disconnect the intake air duct from the throttle body.
9. Push the throttle valve open as shown.
10. Release the throttle valve.

**Does the throttle valve return?**
- **YES** — Clean the throttle body (see page 11-499), then go to step 13 and recheck. If DTC P1684 is indicated, go to step 11.
- **NO** — Go to step 11.

11. Turn the ignition switch OFF.
12. Replace the throttle body (see page 11-500).
13. Turn the ignition switch ON (II).
14. Reset the ECM with the HDS.
15. Do the ECM idle learn procedure (see page 11-462).
16. Turn the ignition switch OFF, and wait 10 seconds.
17. Turn the ignition switch ON (II).
18. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P1684 indicated?**
- **YES** — Check for poor connections or loose terminals at the throttle body and the throttle actuator control module, then go to step 1.
- **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting. •

Source printed page: 11-405

---

### Printed page 11-406

<a id="p702"></a>
Source: [PDF p.702, printed p.11-406](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0702.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)
### DTC P2101: Throttle Actuator System Malfunction

**CAUTION**
Do not insert your fingers into the installed throttle body when you turn the ignition switch ON (II) or while the ignition switch is ON (II). If you do, you will seriously injure your fingers if the throttle valve is activated.

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Do the ETCS T E S T in the INSPECTION MENU with the HDS.
4. Check for Temporary DTCs or DTCs with the HDS.

Is DTC P2101 indicated?
- **Y E S** — G o to step 7.
- **NO** — Go to step 5.

5. Test-drive the vehicle for several minutes in the range of these recorded freeze data parameters:
- **E N G I N E S P E E D**
- **V S S**
- **A P P S E N S O R**

6. Check for Temporary DTCs or DTCs with the HDS.

Is DTC P2101 indicated?
- **YES** — Go to step 7.
- **NO** — Intermittent failure; check connections at throttle body and control module, then clean throttle body (p. 11-499).

7. Turn the ignition switch OFF.
8. Disconnect the intake air duct from the throttle body.
9. Turn the ignition switch ON (II).
10. Clear the DTC with the HDS.
11. Visually check the throttle valve operation while doing the ETCS T E S T in the INSPECTION MENU with the HDS.

Does the throttle valve operate smoothly?
- **YES** — Clean the throttle body (see page 11-499), then go to step 19 and recheck. If DTC P2101 is indicated, then go to step 17.
- **NO** — Go to step 12.

12. Turn the ignition switch OFF.
13. Disconnect the throttle body 6P connector.
14. Disconnect the throttle actuator control module 16P connector (see page 11-437).
15. Connect throttle body 6P connector terminals No. 5 and No. 6 with a jumper wire.

**T H R O T T L E B O D Y 6P C O N N E C T O R**
```
1   2   3   4   5   6
M - (WHT/BLU) M + (WHT/BLK)
```
J U M P E R W I R E
Wire side of female terminals


11-406

---

### Printed page 11-407

<a id="p703"></a>
Source: [PDF p.703, printed p.11-407](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0703.png).

## Electronic throttle control — DTC P2101 troubleshooting (continued)

16. Check continuity between throttle actuator control module 16P connector terminals **1 (M+, BLU)** and **8 (M−, GRN)**. **Continuity:** Substitute a known-good throttle actuator control module (p. 11-437), then go to step 19 and recheck. If P2101 disappears, replace the original module. If P2101 persists, go to step 17. **No continuity:** Repair the open motor drive wires between throttle body and module, then go to step 19.
17. Turn ignition OFF.
18. Replace the throttle body (p. 11-500).
19. Reconnect all connectors.
20. Turn ignition ON (II).
21. Reset the ECM with the HDS.
22. Do the ECM idle learn procedure (p. 11-462).
23. Test drive for several minutes in the ranges of recorded freeze data: engine speed, VSS, and APP sensor.
24. Check DTCs with the HDS. **P2101 indicated:** Check connections at the throttle body and control module, clean the throttle body (p. 11-499), and return to step 1. **Not indicated:** Troubleshooting is complete; follow any other indicated DTC procedures.

---

### Printed page 11-408

<a id="p704"></a>
Source: [PDF p.704, printed p.11-408](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0704.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)
### DTC P2108: Throttle Actuator Control Module

**Problem**
> NOTE: Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Turn the ignition switch OFF.
4. Turn the ignition switch ON (**II**).
5. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P2108 indicated?**

- **YES**—Substitute a known-good throttle actuator control module (see page 11-437), and recheck. If DTC P2108 is not indicated, replace the original throttle actuator control module (see page 11-437).
- **NO**—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body, the throttle actuator control module, and the E C M . B

Source printed page: 11-408

---

### Printed page 11-409

<a id="p705"></a>
Source: [PDF p.705, printed p.11-409](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0705.png).

# DTC P2118: Throttle Actuator Current Range/Performance Problem

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Disconnect the throttle actuator control module 16P connector (see page 11-437).
2. Measure resistance between throttle actuator control module 16P connector terminals No. 1 and No. 8.

**T H R O T T L E A C T U A T O R C O N T R O L M O D U L E 16P C O N N E C T O R**
```
M + (BLU) M - (GRN)
1 2 / / / 6 7 8
9 10 11 12/ 14 / /
Wire side of female terminals
```

Is there about 1.0 Ω, or less?

- **Y E S** — Go to step 3.
- **NO** — Substitute a known-good throttle actuator control module (see page 11-437), then go to step 6 and recheck. If DTC P2118 is not indicated, replace the original throttle actuator control module (see page 11-437), then go to step 6.

3. Disconnect the throttle body 6P connector.
4. At throttle body side, measure resistance between throttle body 6P connector terminals No. 5 and No. 6 with the throttle fully closed.

**T H R O T T L E B O D Y 6P C O N N E C T O R**
```
1 2 3 4 5 6
M - M +
Terminal side of male terminals
```

Is there about 1.0 Ω, or less?

- **Y E S** — Go to step 5.
- **NO** — Repair short in the wires between the throttle body and the throttle actuator control module (motor drive lines), then go to step 6.

5. Replace the throttle body (see page 11-500).
6. Reconnect all connectors.
7. Turn the ignition switch ON (II).
8. Reset the ECM with the HDS.
9. Do the ECM idle learn procedure (see page 11-462).
10. Turn the ignition switch OFF.
11. Turn the ignition switch ON (II).
12. Slowly press the accelerator pedal to the floor.

*(cont'd)*

Source printed page: 11-409

---

### Printed page 11-410

<a id="p706"></a>
Source: [PDF p.706, printed p.11-410](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0706.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)

### Step 13: Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P2118 indicated?**

- **YES**—Check for poor connections or loose terminals at the throttle body and the throttle actuator control module, then go to step 1.
- **NO—**Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

*Page Reference: 11-410*

---

### Printed page 11-411

<a id="p707"></a>
Source: [PDF p.707, printed p.11-411](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0707.png).

## DTC P2122: APP sensor A (TP sensor D) circuit low voltage

Before troubleshooting, record freeze data and any on-board snapshot; see general troubleshooting (p. 11-213).

1. Turn ignition ON (II).
2. Check APP SENSOR A in the HDS DATA LIST. **About 0.1 V or less:** Go to step 3. **Otherwise:** Intermittent failure; check connections at APP sensor A and ECM.
3. Turn ignition OFF.
4. Disconnect APP sensor 6P connector.
5. Turn ignition ON (II).
6. Measure voltage between APP sensor 6P terminals **5 (VCC2, YEL/RED)** and **6 (SG2, GRN/WHT)**. **About 5 V:** Go to step 7. **Otherwise:** Go to step 17.
7. Turn ignition OFF.
8. Jump the SCS line with the HDS.
9. Disconnect ECM connector A (31P).
10. Check continuity between APP sensor 6P terminal **4 (APSA, RED/BLU)** and body ground. **Continuity:** Repair short between APP sensor A and ECM A26, then go to step 20. **No continuity:** Go to step 11.
11. Ground APP sensor terminal 4 with a jumper wire. Procedure continues on next page.

See source image for connector orientation.

---

### Printed page 11-412

<a id="p708"></a>
Source: [PDF p.708, printed p.11-412](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0708.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)

### Step 12
Check for continuity between ECM connector terminal A26 and body ground.

**ECM Connector A (31P)**
Connector orientation: see source image.

| Pin | Label | Color |
| :--- | :--- | :--- |
| A26 | APP S | RED/BLU |

**Is there continuity?**
- **YES** — Go to step 13.
- **NO** — Repair open in the wire between APP sensor A and the ECM (A26), then go to step 20.

### Step 13
Reconnect ECM connector A (31P).

### Step 14
Connect APP sensor 6P connector terminals No. 4 and No. 5 with a jumper wire.

**APP Sensor 6P Connector**
Connector orientation: see source image.

| Pin | Label | Color |
| :--- | :--- | :--- |
| 4 | APP S | RED/BLU |
| 5 | VCC 2 | YEL/RED |

**Jumper Wire**

### Step 15
Turn the ignition switch ON (II).

### Step 16
Check APP SENSOR A in the DATA LIST with the HDS.

**Is there about 0.1 V or less?**
- **YES** — Go to step 25.
- **NO** — Go to step 18.

### Step 17
Measure voltage between ECM connector terminals A20 and A23.

**ECM Connector A (31P)**
Connector orientation: see source image.

| Pin | Label | Color |
| :--- | :--- | :--- |
| A20 | VCC 2 | YEL/BLU |
| A23 | SG 2 | GRN/YEL |

**Is there about 5 V?**
- **YES** — Repair open in the wire between APP sensor A and the ECM (A20), then go to step 20.
- **NO** — Go to step 25.

---
*Page Reference: 11-412*

---

### Printed page 11-413

<a id="p709"></a>
Source: [PDF p.709, printed p.11-413](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0709.png).

## DTC P2122 troubleshooting (continued)

18. Turn ignition OFF.
19. Replace the APP sensor (p. 11-437).
20. Reconnect all connectors.
21. Turn ignition ON (II).
22. Reset the ECM with the HDS.
23. Do the ECM idle learn procedure (p. 11-462).
24. Check DTCs with the HDS. **P2122 indicated:** Check connections at APP sensor A and ECM, then return to step 1. **Not indicated:** Troubleshooting complete; follow any other DTC procedures.
25. Turn ignition OFF.
26. Reconnect all connectors.
27. Update ECM software if needed (p. 11-216) or substitute a known-good ECM (p. 11-217).
28. Check DTCs with the HDS. **P2122 indicated:** Check APP sensor A and ECM connections. If ECM was updated, substitute known-good ECM and recheck; if ECM was substituted, return to step 1. **Not indicated:** If updated, troubleshooting is complete; if substituted, replace original ECM (p. 11-389). Follow any other DTC procedures.

---

### Printed page 11-414

<a id="p710"></a>
Source: [PDF p.710, printed p.11-414](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0710.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)
### DTC P2123: APP Sensor A (Throttle Position Sensor D) Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Check APP **S E N S O R A** in the DATA LIST with the HDS.
   Is there about 4.85 V or more?
   - **Y E S** — G o to step 3.
   - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the APP sensor and the ECM. •

3. Turn the ignition switch OFF.
4. Disconnect the APP sensor 6P connector.
5. Turn the ignition switch ON (**II**).
6. Measure voltage between APP sensor 6P connector terminals No. 5 and No. 6.

   **APP SENSOR 6P CONNECTOR**
   Connector orientation: see source image.
   Is there about 5 V?
   - **Y E S** — G o to step 8.
   - **N O** — G o to step 7.

7. Measure voltage between ECM connector terminals A20 and A23.

   **ECM CONNECTOR A (31P)**
   Connector orientation: see source image.
   Is there about 5 V?
   - **YES** — Repair open in the wire between the ECM (**A23**) and the APP sensor, then go to step 10.
   - **N O** — G o to step 15.

8. Turn the ignition switch OFF.
9. Replace the APP sensor (see page 11-437).
10. Reconnect all connectors.
11. Turn the ignition switch ON (**II**).
12. Reset the **E C M** with the HDS.
13. Do the ECM idle learn procedure (see page 11-462).
14. Check for Temporary DTCs or DTCs with the HDS.
    Is DTC P2123 indicated?
    - **Y E S** — C h e c k for poor connections or loose terminals at the APP sensor and the **E C M**, then go to step 1.
    - **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated **D T C s** troubleshooting. •

**Page Reference:** 11-414

---

### Printed page 11-415

<a id="p711"></a>
Source: [PDF p.711, printed p.11-415](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0711.png).

## DTC P2123 troubleshooting (continued)

15. Turn ignition OFF.
16. Reconnect all connectors.
17. Update ECM software if needed (p. 11-216) or substitute a known-good ECM (p. 11-217).
18. Check DTCs with the HDS. **P2123 indicated:** Check APP sensor and ECM connections. If ECM was updated, substitute known-good ECM and recheck; if ECM was substituted, return to step 1. **Not indicated:** If updated, troubleshooting is complete; if substituted, replace original ECM (p. 11-389). Follow any other DTC procedures.

---

### Printed page 11-416

<a id="p712"></a>
Source: [PDF p.712, printed p.11-416](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0712.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)
### DTC P2127: APP Sensor B (TP Sensor E) - Circuit Low Voltage

**NOTE:** Before you troubleshoot record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Check APP S E N S O R B in the DATA LIST with the HDS.
   - Is there about 0.1 V or less?
     - **Y E S** — G o t o step 3.
     - **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at APP sensor B and the E C M .

3. Turn the ignition switch OFF.
4. Disconnect the APP sensor 6P connector.
5. Turn the ignition switch ON (II).
6. Measure voltage between APP sensor 6P connector terminals No. 1 and No. 2.

   **APP S E N S O R 6P C O N N E C T O R**
   Connector orientation: see source image.
   *Wire side of female terminals*

   - Is there about 5 V?
     - **Y E S** — G o to step 7.
     - **N O** — G o to step 17.

7. Turn the ignition switch OFF.
8. Jump the S C S line with the HDS.
9. Disconnect E C M connector A (31P).
10. Check for continuity between APP sensor 6P connector terminal No. 3 and body ground.

    **APP S E N S O R 6P C O N N E C T O R**
    Connector orientation: see source image.
    *Wire side of female terminals*

    - Is there continuity?
      - **YES** — Repair short in the wire between APP sensor B and the E C M (A25), then go to step 20.
      - **NO** — Go to step 11.

11. Connect APP sensor 6P connector terminal No. 3 to body ground with a jumper wire.

    **APP S E N S O R 6P C O N N E C T O R**
    Connector orientation: see source image.
    *Wire side of female terminals*

    **J U M P E R W I R E**

---
*Page Reference: 11-416*

---

### Printed page 11-417

<a id="p713"></a>
Source: [PDF p.713, printed p.11-417](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0713.png).

## DTC P2127 troubleshooting (continued)

12. Check continuity between ECM connector **A25 (APSB, RED/YEL)** and body ground. **Continuity:** Go to step 13. **No continuity:** Repair open between APP sensor B and ECM A25, then go to step 20.
13. Reconnect ECM connector A (31P).
14. Jump APP sensor 6P connector terminals **1 (VCC3, YEL/BLU)** and **3 (APSB, RED/YEL)**.
15. Turn ignition ON (II).
16. Check APP SENSOR B in HDS DATA LIST. **About 0.1 V or less:** Go to step 25. **Otherwise:** Go to step 18.
17. Measure voltage between ECM connector terminals **E4 and E5**. **About 5 V:** Repair open between APP sensor B and ECM E5, then go to step 20. **Otherwise:** Go to step 25.

See source image for connector orientation.

---

### Printed page 11-418

<a id="p714"></a>
Source: [PDF p.714, printed p.11-418](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0714.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)

**18.** Turn the ignition switch OFF.

**19.** Replace the APP sensor (see page 11-437).

**20.** Reconnect all connectors.

**21.** Turn the ignition switch ON (II).

**22.** Reset the E C M with the HDS.

**23.** Do the E C M idle learn procedure (see page 11-462).

**24.** Check for Temporary DTCs or DTCs with the HDS.

Is DTC P2127 indicated?

* **Y E S** — C h e c k for poor connections or loose terminals at APP sensor B and the E C M , then go to step 1.
* **NO** — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated D T C s troubleshooting.

**25.** Turn the ignition switch OFF.

**26.** Reconnect all connectors.

**27.** Update the E C M if it does not have the latest software (see page 11-216), or substitute a known-good E C M (see page 11-217).

**28.** Check for Temporary DTCs or DTCs with the HDS.

Is DTC P2127 indicated?

* **Y E S** — C h e c k for poor connections or loose terminals at APP sensor B and the E C M . If the E C M was updated, substitute a known-good E C M (see page 11-217), then recheck. If the E C M was substituted, go to step 1.
* **NO** — If the E C M was updated, troubleshooting is complete. If the ECM was substituted, replace the original E C M (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated D T C s troubleshooting.

**Page Reference:** 11-418

---

### Printed page 11-419

<a id="p715"></a>
Source: [PDF p.715, printed p.11-419](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0715.png).

DTC P2128: APP Sensor B (Throttle Position Sensor E) Circuit High Voltage
NOTE: Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
1. Turn the ignition switch ON (II).
2. Check APP SENSOR B in the DATA LIST with the HDS.
Is there about 4.0 V or higher?
Y E S — G o to step 3.
NO—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at APP sensor B and the E C M . B
3. Turn the ignition switch OFF.
4. Disconnect the APP sensor 6P connector.
5. Turn the ignition switch ON (II).
6. Measure voltage between APP sensor 6P connector terminals No. 1 and No. 2.
APP S E N S O R 6P C O N N E C T O R
1 2 3 4 5 6
V C C 3
( Y E L / B L U )
S G 3
(GRN)
Wire side of female terminals
Is there about 5 V?
Y E S — G o t o s t e p 8.
N O — G o to step 7.
7. Measure voltage between E C M connector terminals E4 and E5.
E C M C O N N E C T O R E (31P)
V C C 3 (YEL/BLU)
1 M 3 | 4 | 5 XI T | 1 a|»
/ 11 12 13 14 15 16 17 18 19 20 21
22
/ 24 25
/ 27 28 29 30
/
Wire side of female terminals
Is there about 5 V?
YES—Repair open in the wire between the ECM (E4) and the APP sensor, then go to step 10.
N O — G o to step 15.
8. Turn the ignition switch OFF.
9. Replace the APP sensor (see page 11-437).
10. Reconnect all connectors.
11. Turn the ignition switch ON (II).
12. Reset the E C M with the HDS.
13. Do the E C M idle learn procedure (see page 11-462).
14. Check for Temporary DTCs or DTCs with the HDS.
Is DTC P2128 Indicated?
Y E S — C h e c k for poor connections or loose terminals at APP sensor B and the E C M , then go to s t e p l .
NO—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated D T C s troubleshooting.
(cont'd)
11-419

---

### Printed page 11-420

<a id="p716"></a>
Source: [PDF p.716, printed p.11-420](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0716.png).

## DTC P2128 troubleshooting (continued)

15. Turn ignition OFF.
16. Reconnect all connectors.
17. Update ECM software if needed (p. 11-216) or substitute a known-good ECM (p. 11-217).
18. Check DTCs with the HDS. **P2128 indicated:** Check APP sensor and ECM connections. If ECM was updated, substitute known-good ECM and recheck; if ECM was substituted, return to step 1. **Not indicated:** If updated, troubleshooting is complete; if substituted, replace original ECM (p. 11-389). Follow any other DTC procedures.

---

### Printed page 11-421

<a id="p717"></a>
Source: [PDF p.717, printed p.11-421](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0717.png).

## DTC P2135: TP sensor A/B incorrect voltage correlation

**CAUTION:** Keep fingers out of the installed throttle body whenever ignition is ON (II); an activated throttle valve can seriously injure them.

Record freeze data and snapshot before troubleshooting (p. 11-213).

1. Turn ignition ON (II).
2. Clear DTC with HDS.
3. Run ETCS TEST in HDS INSPECTION MENU.
4. Check DTCs. **P2135 indicated:** Go to step 5. **Not indicated:** Intermittent fault; check throttle body and actuator control module connections.
5. Turn ignition OFF.
6. Disconnect intake air duct from throttle body.
7. Turn ignition ON (II).
8. Observe throttle valve while clearing the DTC with HDS. **Valve briefly moves fully closed:** Go to step 14. **Otherwise:** Go to step 9.
9. Turn ignition OFF.
10. Disconnect actuator control module 16P connector (p. 11-437).
11. Check continuity between actuator control module 16P terminals **10 and 12** (TPSA, RED/BLK). **Continuity:** Go to step 12. **No continuity:** Substitute a known-good actuator control module (p. 11-437), then go to step 16 and recheck. If P2135 disappears, replace original module, then go to step 16.

See source image for connector orientation.

---

### Printed page 11-422

<a id="p718"></a>
Source: [PDF p.718, printed p.11-422](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0718.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)

**12.** Disconnect the throttle body 6P connector.

**13.** Check for continuity between throttle actuator control module 16P connector terminals No. 10 and No. 12.

> **T H R O T T L E A C T U A T O R C O N T R O L M O D U L E 16P CONNECTOR**
>
> Connector orientation: see source image.
> Wire side of female terminals

**Is there continuity?**

*   **YES**—Repair short in the wire between the TPSA line and the TPSB line, then go to step 16.
*   **NO**—Go to step 14.

**14.** Turn the ignition switch OFF.

**15.** Replace the throttle body (see page 11-500).

**16.** Reconnect all connectors.

**17.** Turn the ignition switch ON (II).

**18.** Reset the ECM with the HDS.

**19.** Do the E C M idle learn procedure (see page 11-462).

**20.** Check for Temporary DTCs or DTCs with the HDS.

> **Is DTC P2135 indicated?**

*   **YES**—Check for poor connections or loose terminals at the throttle body and the throttle actuator control module, then go to step 1.
*   **NO**—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated D T C s troubleshooting. If any other Temporary DTCs or DTCs are indicated, go to the indicated D T C s troubleshooting. •

**11-422**

---

### Printed page 11-423

<a id="p719"></a>
Source: [PDF p.719, printed p.11-423](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0719.png).

## DTC P2138: APP sensor A/B incorrect voltage correlation

Record freeze data and snapshot before troubleshooting (p. 11-213).

1. Turn ignition ON (II).
2. Clear DTC with HDS.
3. Press accelerator pedal to floor.
4. Check DTCs. **P2138 indicated:** Go to step 5. **Not indicated:** Intermittent fault; check APP sensor and ECM connections.
5. Check APP SENSOR A and B voltages in HDS DATA LIST. **Same voltage:** Go to step 6. **Different:** Go to step 11.
6. Turn ignition OFF.
7. Jump SCS line with HDS.
8. Disconnect APP sensor 6P connector.
9. Disconnect ECM connector A (31P).
10. Check continuity between ECM **A25 (APSB, RED/YEL)** and **A26 (APSA, RED/BLU)**. **Continuity:** Repair short between A25 and A26, then go to step 13. **No continuity:** Go to step 21.
11. Turn ignition OFF.
12. Replace APP sensor (p. 11-437).
13. Reconnect all connectors.
14. Turn ignition ON (II).
15. Reset ECM with HDS.
16. Do ECM idle learn (p. 11-462).
17. Turn ignition OFF.
18. Turn ignition ON (II).
19. Press accelerator pedal to floor. Procedure continues on next page.

---

### Printed page 11-424

<a id="p720"></a>
Source: [PDF p.720, printed p.11-424](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0720.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)

**20.** Check for Temporary DTCs or DTCs with the HDS.

Is **DTC P2138** indicated?

*   **Y E S** — C h e c k f o r p o o r c o n n e c t i o n s o r l o o s e terminals at the APP sensor and the E C M , then go to step 1.
    *   I M O — Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated D T C s troubleshooting. •

**21.** Reconnect all connectors.

**22.** Update the E C M if it does not have the latest software (see page 11-216), or substitute a known-good E C M (see page 11-217).

**23.** Turn the ignition switch OFF.

**24.** Turn the ignition switch ON (II).

**25.** Press the accelerator pedal to the floor.

**26.** Check for Temporary DTCs or DTCs with the HDS.

Is **DTC P2138** indicated?

*   **Y E S** — C h e c k f o r p o o r c o n n e c t i o n s o r l o o s e terminals at the APP sensor and the E C M . If the ECM w a s updated, substitute a known-good E C M (see page 11-217), then go to step 23. If the E C M was substituted, go to step 1.
    *   N O — I f t h e E C M w a s u p d a t e d , troubleshooting is complete. If the E C M was substituted, replace the original E C M (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated D T C s troubleshooting. •

**Page Reference:** 11-424

---

### Printed page 11-425

<a id="p721"></a>
Source: [PDF p.721, printed p.11-425](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0721.png).

# DTC P2176: Throttle Actuator Control System - Idle Position Not Learned

## CAUTION
Do not insert your fingers into the installed throttle body when you turn the ignition switch ON (II) or while the ignition switch is ON (II). If you do, you will seriously injure your fingers if the throttle valve is activated.

## NOTE:
* Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).
* If DTC P2135 is stored at the same time as DTC P2176, troubleshoot DTC P2135 first, then recheck for DTC P2176.

### Step 1
Turn the ignition switch ON (II).

### Step 2
Clear the DTC with the HDS.

### Step 3
Turn the ignition switch OFF.

### Step 4
Turn the ignition switch ON (II), and wait **10 seconds**.

### Step 5
Check for Temporary DTCs or DTCs with the HDS.
* Is DTC P2176 indicated?
    * **YES** — Go to step 6.
    * **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the throttle actuator control module, then clean the throttle body (see page 11-499).

### Step 6
Turn the ignition switch OFF.

### Step 7
Disconnect the intake air duct from the throttle body.

### Step 8
Turn the ignition switch ON (II).

### Step 9
Clear the DTC with the HDS.

### Step 10
Visually check the throttle valve operation while performing the **ETCS TEST** in the INSPECTION MENU with the HDS.
* Does the throttle valve move to its fully closed position?
    * **YES** — Go to step 11.
    * **NO** — Go to step 12.

### Step 11
Check for sludge or carbon on the throttle valve.
* Is there sludge or carbon on the throttle valve?
    * **YES** — Clean the throttle body (see page 11-499), then go to step 20 and recheck.
    * **NO** — Go to step 19.

### Step 12
Turn the ignition switch OFF.

### Step 13
Disconnect the throttle body **6P connector**.

### Step 14
Disconnect the throttle actuator control module **16P connector** (see page 11-437).

### Step 15
Connect throttle body 6P connector terminals No. 5 and No. 6 with a jumper wire.

#### Diagram: Throttle Body 6P Connector
* **Terminal Labels:**
    * M— (WHT/BLU)
    * M + (WHT/BLK)
* **Connector Pin Configuration:**
    * 1, 2, 3, 4, 5, 6
* **Jumper Wire Connection:** Wire side of female terminals.

**Source Page Reference:** 11-425

---

### Printed page 11-426

<a id="p722"></a>
Source: [PDF p.722, printed p.11-426](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0722.png).

## DTC P2176 troubleshooting (continued)

16. Check continuity between throttle actuator control module 16P connector terminals **1 (M+, BLU)** and **8 (M−, GRN)**. **Continuity:** Substitute a known-good module (p. 11-437), then go to step 19 and recheck. If P2176 disappears, replace original module; otherwise continue at step 19. **No continuity:** Repair open motor drive wires, then go to step 19.
17. Turn ignition OFF.
18. Replace throttle body (p. 11-500).
19. Reconnect all connectors.
20. Turn ignition ON (II).
21. Reset ECM with HDS.
22. Do ECM idle learn (p. 11-462).
23. Turn ignition OFF.
24. Turn ignition ON (II) and wait 10 seconds.
25. Check DTCs with HDS. **P2176 indicated:** Check throttle body and actuator module connections, clean throttle body (p. 11-499), and return to step 1. **Not indicated:** Troubleshooting complete; follow any other DTC procedures.

---

### Printed page 11-427

<a id="p723"></a>
Source: [PDF p.723, printed p.11-427](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0723.png).

# DTC P2552: Throttle Actuator Control Module Relay Malfunction

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Do the ETCS TEST in the INSPECTION MENU with the HDS.

**Is the RELAY circuit OK?**

*   **YES**—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle actuator control module relay, the throttle actuator control module, and the ECM.
*   **NO**—Go to step 4.

4. Turn the ignition switch OFF.
5. Remove the throttle actuator control module relay (A).
6. Test the throttle actuator control module relay (see page 22-48).

**Is the relay OK?**

*   **YES**—Go to step 7.
*   **NO**—Replace the throttle actuator control module relay, then go to step 10.

7. Jump the SCS line with the HDS.
8. Disconnect ECM connector D(17P).
9. Check for continuity between ECM connector terminal D15 and body ground.

**ECM CONNECTOR D (17P)**

Connector orientation: see source image.

**Is there continuity?**

*   **YES**—Repair short in the wire between the throttle actuator control module relay and the ECM (D15), then goto step 10.
*   **NO**—Go to step 17.

*(cont'd)*

---

### Printed page 11-428

<a id="p724"></a>
Source: [PDF p.724, printed p.11-428](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0724.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)

10. Reconnect ECM connector D(17P).
11. Turn the ignition switch ON (II).
12. Reset the ECM with the HDS.
13. Do the ECM idle learn procedure (see page 11-462).
14. Turn the ignition switch OFF.
15. Turn the ignition switch ON (II), and wait 10 seconds.
16. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P2552 indicated?**

*   **YES**—Check for poor connections or loose terminals at the throttle actuator control module relay, the throttle actuator control module, and the ECM, then go to step 1.
*   **NO**—Troubleshooting is complete. If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

17. Reconnect all connectors.
18. Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).
19. Turn the ignition switch OFF.
20. Turn the ignition switch ON (II), and wait 10 seconds.
21. Check for Temporary DTCs or DTCs with the HDS.

**Is DTC P2552 indicated?**

*   **YES**—Check for poor connections or loose terminals at the throttle actuator control module relay, the throttle actuator control module, and the ECM. If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 19. If the ECM was substituted, go to step 1.
*   **NO**—If the ECM was updated, troubleshooting is complete. If the ECM was substituted, replace the original ECM (see page 11-389). If any other Temporary DTCs or DTCs are indicated, go to the indicated DTCs troubleshooting.

**Page Reference:** 11-428

---

### Printed page 11-429

<a id="p725"></a>
Source: [PDF p.725, printed p.11-429](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0725.png).

# DTC U0107: Lost Communication With Throttle Actuator Control Module

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Check for Temporary DTCs or DTCs with the HDS.

Is DTC U0107 indicated?

*   **YES**—Check for poor connections or loose terminals at the throttle body, the throttle actuator control module, and the ECM, then go to step 50. If the connections are OK, go to step 6.
*   **NO**—Go to step 4.

4. Start the engine.

5. Check for Temporary DTCs or DTCs with the HDS.

Is DTC U0107 indicated?

*   **YES**—Go to step 46.
*   **NO**—Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body, the throttle actuator control module relay, the throttle actuator control module, and the ECM.

6. Clear the DTC with the HDS.
7. Turn the ignition switch OFF.
8. Disconnect the intake air duct from the throttle body.
9. Press the accelerator pedal to the floor.
10. Turn the ignition switch ON (II),
11. Check the throttle valve operation.

Does it open after it closes?

*   **YES**—Go to step 12.
*   **NO**—Go to step 13.

12. Check the throttle valve again.

Does the throttle valve open fully?

*   **YES**—Go to step 40.
*   **NO**—Go to step 34.

13. Turn the ignition switch OFF.
14. Disconnect the throttle actuator control module 16P connector.
15. Check for continuity between throttle actuator control module 16P connector terminal No. 7 and body ground.

**T H R O T T L E A C T U A T O R C O N T R O L M O D U L E 16P C O N N E C T O R**

Connector orientation: see source image.

Is there continuity?

*   **YES**—Go to step 16.
*   **NO**—Repair open in the wire between the throttle body, the throttle actuator control module, and G101, then go to step 50.

(cont'd)

**Page Reference:** 11-429

---

### Printed page 11-430

<a id="p726"></a>
Source: [PDF p.726, printed p.11-430](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0726.png).

# Electronic Throttle Control System
## DTC Troubleshooting (cont'd)

### Step 16
Remove the throttle actuator control module relay (A).

### Step 17
Measure voltage between throttle actuator control module relay 4P connector terminal No. 2 and body ground.

**Throttle Actuator Control Module Relay 4P Connector Diagram:**
- **Wire Color:** +B (BLU/WHT)
- **Terminal Type:** Wire side of female terminals
- **Decision Path:** Is there battery voltage?
  - **YES:** Go to step 19.
  - **NO:** Go to step 18.

### Step 18
Check the No. 14 DBW (15 A) fuse in the under-dash fuse/relay box.

**Decision Path:** Is the fuse OK?
- **YES:** Repair open in the wire between the throttle actuator control module relay (+B line) and the No. 14 DBW (15 A) fuse, then go to step 50.
- **NO:** Repair short in the wire between the throttle actuator control module relay (+B line) and the No. 14 DBW (15 A) fuse. Also replace the fuse, then go to step 50.

### Step 19
Install the throttle actuator control module relay.

### Step 20
Turn the ignition switch ON (II).

### Step 21
Measure voltage between throttle actuator control module 16P connector terminal No. 2 and body ground.

**Throttle Actuator Control Module 16P Connector Diagram:**
- **Wire Color:** +B (YEL/GRN)
- **Terminal Numbers:** 1, 2, / / /, 6, 7, 8, 9, 10, 11, 12/ / 14 / /
- **Terminal Type:** Wire side of female terminals
- **Decision Path:** Is there battery voltage for about 2 seconds?
  - **YES:** Substitute a known-good throttle actuator control module (see page 11-437), then go to step 50 and recheck. If DTC U0107 is not indicated, replace the original throttle actuator control module (see page 11-437), then go to step 50.
  - **NO:** Go to step 22.

### Step 22
Turn the ignition switch OFF.

### Step 23
Remove the throttle actuator control module relay (A).

**Reference:** Page 11-430

---

### Printed page 11-431

<a id="p727"></a>
Source: [PDF p.727, printed p.11-431](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0727.png).

## DTC U0107 troubleshooting (continued)

24. Test throttle actuator control module relay (p. 22-48). **OK:** Go to step 25. **Faulty:** Replace relay, then go to step 50.
25. Turn ignition ON (II).
26. Measure voltage from throttle actuator control module relay 4P terminal **4** to body ground. **Battery voltage:** Go to step 27. **No voltage:** Repair open between relay and PGM-FI main relay 1 (FI MAIN), then go to step 50.
27. Turn ignition OFF.
28. Jump SCS line with HDS.
29. Disconnect ECM connector D (17P).
30. Check continuity between ECM **D15 (ETCSRLY, BRN)** and actuator relay 4P terminal **3 (ETCSRLY, BRN)**. **Continuity:** Go to step 31. **No continuity:** Repair open between ECM D15 and relay, then go to step 50.
31. Check continuity between actuator control module 16P terminal **2 (+B, YEL/GRN)** and body ground. **Continuity:** Repair short between module and actuator relay, then go to step 50. **No continuity:** Go to step 32.

See source image for connector orientation.

---

### Printed page 11-432

<a id="p728"></a>
Source: [PDF p.728, printed p.11-432](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0728.png).

## DTC U0107 troubleshooting (continued)

32. Ground actuator control module relay 4P terminal **1 (+B, YEL/GRN)** with a jumper wire.
33. Check continuity between actuator control module 16P terminal **2 (+B, YEL/GRN)** and body ground. **Continuity:** Go to step 56. **No continuity:** Repair open +B wire between module and relay, then go to step 50.
34. Turn ignition OFF.
35. Jump SCS line with HDS.
36. Disconnect actuator control module 16P connector (p. 11-437).
37. Disconnect ECM connector B (24P).
38. Check continuity between ECM **B19 (SEFD, GRN)** and body ground. **Continuity:** Repair short between ECM B19 and actuator module, then go to step 50. **No continuity:** Go to step 39.

The source image confirms that the first decision belongs to step 33 and the second to step 38.

---

### Printed page 11-433

<a id="p729"></a>
Source: [PDF p.729, printed p.11-433](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0729.png).

## DTC U0107 troubleshooting (continued)

39. Check continuity between ECM **B19 (SEFD, GRN)** and actuator module 16P terminal **6 (SEFD, GRN)**. **Continuity:** Substitute a known-good actuator module (p. 11-437), then go to step 50 and recheck. If U0107 disappears, replace original module; if U0107 persists, go to step 56. **No continuity:** Repair open between ECM B19 and module, then go to step 50.
40. Turn ignition OFF.
41. Jump SCS line with HDS.
42. Disconnect actuator module 16P connector.
43. Disconnect ECM connector B (24P).
44. Check continuity between ECM **B20 (SEDF, BLU)** and body ground. **Continuity:** Repair short between ECM B20 and actuator module, then go to step 50. **No continuity:** Go to step 45.

---

### Printed page 11-434

<a id="p730"></a>
Source: [PDF p.730, printed p.11-434](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0730.png).

## DTC U0107 troubleshooting (continued)

45. Check continuity between ECM **B20 (SEDF, BLU)** and actuator module 16P terminal **14 (SEDF, BLU)**. **Continuity:** Substitute a known-good actuator module (p. 11-437), then go to step 50 and recheck. If U0107 disappears, replace original module; if U0107 persists, go to step 56. **No continuity:** Repair open between ECM B20 and module, then go to step 50.
46. Turn ignition OFF.
47. Jump SCS line with HDS.
48. Disconnect ECM connector A (31P).
49. Check continuity from body ground to ECM **A8 (LG2, BRN/YEL)** and **A9 (LG1, BRN/YEL)** individually. **Continuity:** Check connections at throttle body, actuator relay, actuator module, and ECM; return to step 1. **No continuity:** Repair open between ECM A8/A9 and G101, then go to step 50.

---

### Printed page 11-435

<a id="p731"></a>
Source: [PDF p.731, printed p.11-435](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0731.png).

## DTC U0107 troubleshooting (continued)

50. Turn ignition OFF.
51. Reconnect all connectors.
52. Turn ignition ON (II).
53. Reset ECM with HDS.
54. Do ECM idle learn (p. 11-462).
55. Check DTCs. **U0107 indicated:** Check connections at throttle body, actuator relay, actuator module, and ECM; return to step 1. **Not indicated:** Troubleshooting complete; follow any other DTC procedures.
56. Reconnect all connectors.
57. Update ECM software if needed (p. 11-216), or substitute a known-good ECM (p. 11-217).
58. Check DTCs. **U0107 indicated:** Check connections at throttle body, actuator relay, actuator module, and ECM. If ECM was updated, substitute a known-good ECM and recheck. If substituted, return to step 1. **Not indicated:** If updated, troubleshooting complete; if substituted, replace original ECM (p. 11-389). Follow any other DTC procedures.

---

### Printed page 11-436

<a id="p732"></a>
Source: [PDF p.732, printed p.11-436](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0732.png).

# Electronic Throttle Control System
## APP Sensor Signal Inspection

**NOTE:**
*   This procedure checks the APP sensor in its fully closed position. In any other position, the APP sensor stores DTCs which are covered in other troubleshooting procedures.
*   Check for Temporary DTCs or DTCs with the HDS before doing this procedure. If any DTCs are indicated, troubleshoot them first, then do this procedure.
*   Press the accelerator pedal several times to check its operation. If it does not operate properly, check the pedal, the throttle cable, and the APP sensor individually. If you find a problem in one of them, replace the part(s) that caused the problem.

1.  Connect the HDS to the data link connector (DLC) **(A)** located behind the driver's side of the front console.
2.  Turn the ignition switch ON (**II**).
3.  Make sure the HDS communicates with the E C M . If it doesn't, go to the DLC circuit troubleshooting (see page **11-367**).
4.  Make sure the accelerator pedal is not pressed, then check the APP S E N S O R in the DATA LIST with the HDS.
    *   If it is below 2 %, the APP sensor is OK.
    *   If it is above 2 %, adjust the throttle cable (see page **11-504**), then go to step 5.
5.  Make sure the accelerator pedal is not pressed, then check the APP S E N S O R in the DATA LIST with the HDS.
    *   If it is below 2 %, the APP sensor is OK.
    *   If it is above 2 %, update the E C M if it does not have the latest software, or substitute a known-good E C M (see page **11-217**), then go to step 6.
6.  Make sure the accelerator pedal is not pressed, then check the APP S E N S O R in the DATA LIST with the HDS.
    *   If it is below 2 %, the APP sensor is OK.
    *   If it is above 2 %, replace the APP sensor (see page **11-437**), then go to step 1.

Source printed page: 11-436

---

### Printed page 11-437

<a id="p733"></a>
Source: [PDF p.733, printed p.11-437](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0733.png).

# APP Sensor Replacement

1. Remove the throttle cable cover (see page 11-504).
2. Remove the throttle cable (see page 11-503).
3. Disconnect the accelerator pedal position (APP) sensor 6P connector (A).
4. Remove the bolts (B) and the APP sensor (C).
5. Install the parts in the reverse order of removal.

## Throttle Actuator Control Module Replacement

1. Remove the passenger's dashboard lower cover (see page 20-86).
2. Push the tab (A), and disconnect the throttle actuator control module 16P connector (B).
3. Remove the nuts (C) and the throttle actuator control module (D).
4. Install the parts in the reverse order of removal.

Source printed page: 11-437

---

### Printed page 11-438

<a id="p734"></a>
Source: [PDF p.734, printed p.11-438](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0734.png).

## VTEC — component location index

- Rocker arm oil control valve (VTEC solenoid valve): engine compartment; removal/installation, p. 11-449.
- Rocker arm oil pressure switch (VTEC oil pressure switch): engine compartment; removal/installation, p. 11-449.
- Engine control module (ECM): behind the driver's side dash; updating, p. 11-216; substitution, p. 11-217; replacement, p. 11-389.

The source image shows their physical locations.

---

### Printed page 11-439

<a id="p735"></a>
Source: [PDF p.735, printed p.11-439](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0735.png).

## DTC P2646: VTEC oil pressure switch circuit low voltage

**Special tools:** Pressure gauge adapter 07NAJ-P07010A; A/T low pressure gauge with panel 07406-0070301; hose 07406-0020201; 2,210 mm hose 07MAJ-PY4011A; hose adapter 07MAJ-PY40120.

Record freeze data and snapshot before troubleshooting (p. 11-213).

1. Check engine oil level. **OK:** Go to step 2. **Low:** Adjust oil level, then go to step 21.
2. Turn ignition ON (II).
3. Clear DTC with HDS.
4. Run VTEC TEST in HDS INSPECTION MENU. **Result OK:** Intermittent fault; check connections at VTEC oil pressure switch, VTEC solenoid valve, and ECM. **Result not OK:** Go to step 5.
5. Turn ignition OFF.
6. Disconnect VTEC oil pressure switch 2P connector.
7. Turn ignition ON (II).
8. Check VTEC PRES SW in HDS DATA LIST. **Switch ON:** Go to step 15. **Otherwise:** Go to step 9.
9. Turn ignition OFF.
10. Remove VTEC oil pressure switch (A), install the special pressure gauge tools as shown, then install switch to gauge adapter (B). Reinstall with new O-ring. **Switch torque: 22 N·m (2.2 kgf·m, 16 lbf·ft).**
11. Reconnect the switch 2P connector.

See source image for gauge assembly and switch location.

---

### Printed page 11-440

<a id="p736"></a>
Source: [PDF p.736, printed p.11-440](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0736.png).

## DTC P2646 troubleshooting (continued)

12. Start engine.
13. Run VTEC TEST in HDS INSPECTION MENU.
14. Check VTEC oil pressure. **Increase at least 392 kPa (4.0 kgf/cm², 56.9 psi):** Replace VTEC oil pressure switch (p. 11-449), then go to step 20. **Otherwise:** Inspect VTEC system; if OK, replace VTEC solenoid valve (p. 11-449), then go to step 20.
15. Turn ignition OFF.
16. Jump SCS line with HDS.
17. Disconnect ECM connector B (24P).
18. Check continuity between ECM **B11 (VTPSW, BLU/BLK)** and body ground. **Continuity:** Repair short between ECM B11 and VTEC oil pressure switch, then go to step 19. **No continuity:** Go to step 27.
19. Reconnect all connectors.
20. Turn ignition ON (II).
21. Reset ECM with HDS.
22. Do ECM idle learn (p. 11-462).
23. Run VTEC TEST.
24. Check DTCs. **P2646 indicated:** Check VTEC switch, solenoid, and ECM connections. **Not indicated:** Go to step 25.
25. Monitor OBD STATUS for P2646. **PASSED:** Troubleshooting complete; follow other indicated DTCs. **FAILED:** Check switch, solenoid, and ECM connections, then return to step 1. **NOT COMPLETED:** Go to step 23.

The page also directs inspection of the VTEC oil line and rocker arm operation (p. 6-8); if both are OK, replace the VTEC solenoid valve (p. 11-449), then go to step 19. See source image for the two-column flow.

---

### Printed page 11-441

<a id="p737"></a>
Source: [PDF p.737, printed p.11-441](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0737.png).

# Step 26-30: DTC P2646 Troubleshooting

## Step 26
Reconnect all connectors.

## Step 27
Update the ECM if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

## Step 28
Do the VTEC TEST in the INSPECTION MENU with the HDS.

## Step 29
Check for Temporary DTCs or DTCs with the HDS. Is DTC P2646 indicated?

### Decision: YES
- Check for poor connections or loose terminals at the rocker arm oil pressure switch (VTEC oil pressure switch), the rocker arm oil control solenoid (VTEC solenoid valve), and the ECM.
- If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 28.
- If the ECM was substituted, go to step 1.

### Decision: NO
- Go to step 30.

## Step 30
Monitor the OBD STATUS for DTC P2646 in the DTCs MENU with the HDS.

### Decision: Does the screen indicate PASSED?
- **YES**
  - If the ECM was updated, troubleshooting is complete.
  - If the ECM was substituted, replace the original ECM (see page 11-389).
  - If any other Temporary DTCs or DTCs were indicated in step 29, go to the indicated DTCs troubleshooting.

- **NO**
  - If the screen indicates FAILED, check for poor connections or loose terminals at the rocker arm oil pressure switch (VTEC oil pressure switch), the rocker arm oil control solenoid (VTEC solenoid valve), and the ECM.
  - If the ECM was updated, substitute a known-good ECM (see page 11-217), then go to step 28.
  - If the ECM was substituted, go to step 1.
  - If the screen indicates NOT COMPLETED, go to step 28.

---

### Printed page 11-442

<a id="p738"></a>
Source: [PDF p.738, printed p.11-442](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0738.png).

## DTC P2647: VTEC oil pressure switch circuit high voltage

Record freeze data and snapshot before troubleshooting (p. 11-213).

1. Check engine oil level. **OK:** Go to step 2. **Low:** Adjust oil, then go to step 14.
2. Turn ignition ON (II).
3. Clear DTC with HDS.
4. Run VTEC TEST. **Result OK:** Intermittent fault; check VTEC oil pressure switch and ECM connections. **Not OK:** Go to step 5.
5. Check step 4 result. **VTEC Switch Failure, Switch Open, SIG Line Open, or GND Line Open:** Go to step 6. **None of these:** Check switch connections; if OK, replace VTEC solenoid valve (p. 11-449), then go to step 14.
6. Turn ignition OFF.
7. Disconnect VTEC oil pressure switch 2P connector.
8. At switch side, check continuity between switch terminals 1 and 2. **Continuity:** Go to step 9. **No continuity:** Replace switch (p. 11-449), then go to step 13.
9. Turn ignition ON (II).

See source image for switch terminal orientation and the two-column step 5 branch.

---

### Printed page 11-443

<a id="p739"></a>
Source: [PDF p.739, printed p.11-443](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0739.png).

# Page 739: S2000 Fuel and Emissions Part E

## Step 10
Measure voltage between rocker arm oil pressure switch (VTEC oil pressure switch) 2P connector terminal No. 1 and body ground.

**ROCKER ARM OIL PRESSURE SWITCH (VTEC OIL PRESSURE SWITCH) 2P CONNECTOR**
*Wire side of female terminals*
- **VTPSW**: (BLU/BLK)

Is there battery voltage?
- **YES**—Repair open in the wire between the rocker arm oil pressure switch (VTEC oil pressure switch) and G101, then go to step 12.
- **NO**—Go to step 11.

## Step 11
Measure voltage between ECM connector terminal B11 and body ground.

**ECM CONNECTOR B (24P)**
*Wire side of female terminals*
- Pins: 1, 2, 3, 4, 5, 6, 8, 10, 11, 13, 17, 18, 19, 20, 21
- **VTPSW**: (BLU/BLK)

Is there battery voltage?
- **YES**—Repair open in the wire between the ECM (B11) and the rocker arm oil pressure switch (VTEC oil pressure switch), then go to step 12.
- **NO**—Go to step 19.

## Step 12
Turn the ignition switch OFF.

## Step 13
Reconnect the rocker arm oil pressure switch (VTEC oil pressure switch) 2P connector.

## Step 14
Turn the ignition switch ON (II).

## Step 15
Reset the ECM with the HDS.

## Step 16
Do the ECM idle learn procedure (see page 11-462).

## Step 17
Check for Temporary DTCs or DTCs with the HDS.

Is DTC P2647 indicated?
- **YES**—Check for poor connections or loose terminals at the rocker arm oil pressure switch (VTEC oil pressure switch) and the ECM, then go to step 1.
- **NO**—Go to step 18.

## Step 18
Monitor the OBD STATUS for DTC P2647 in the DTCs MENU with the HDS.

Does the screen indicate PASSED?
- **YES**—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 17, go to the indicated DTCs troubleshooting.
- **NO**—If the screen indicates FAILED, check for poor connections or loose terminals at the rocker arm oil pressure switch (VTEC oil pressure switch) and the ECM, then go to step 1. If the screen indicates NOT COMPLETED, go to step 16 and recheck.

*(cont'd)*
Source printed page: 11-443

---

### Printed page 11-444

<a id="p740"></a>
Source: [PDF p.740, printed p.11-444](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0740.png).

# VTEC
## DTC Troubleshooting (cont'd)

**19.** Turn the ignition switch OFF.

**20.** Reconnect all connectors.

**21.** Update the E C M if it does not have the latest software (see page 11-216), or substitute a known-good ECM (see page 11-217).

**22.** Start the engine, and let it idle.

**23.** Check for Temporary DTCs or DTCs with the HDS.

Is DTC P2647 indicated?

*   **Y E S** — C h e c k for poor connections or loose terminals at the rocker arm oil pressure switch (VTEC oil pressure switch) and the ECM. If the E C M was updated, substitute a known-good E C M (see page 11-217), then go to step 22. If the E C M was substituted, go to step 1.
*   **NO** — Go to step 24.

**24.** Monitor the OBD S T A T U S for DTC P2647 in the DTCs MENU with the HDS.

Does the screen indicate PASSED?

*   **YES** — If the E C M w a s updated, troubleshooting is complete. If the E C M was substituted, replace the original E C M (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 22, go to the indicated D T C s troubleshooting.
*   **NO** — If the screen indicates FAILED, check for poor connections or loose terminals at the rocker arm oil pressure switch (VTEC oil pressure switch) and the ECM. If the E C M w a s updated, substitute a known-good E C M (see page 11-217), then go to step 22. If the ECM w a s substituted, go to step 1. If the screen indicates NOT COMPLETED, keep idling until a result comes on.

**11-444**

---

### Printed page 11-445

<a id="p741"></a>
Source: [PDF p.741, printed p.11-445](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0741.png).

## DTC P2648: VTEC solenoid circuit low voltage

Record freeze data and snapshot before troubleshooting (p. 11-213).

1. Turn ignition ON (II).
2. Clear DTC with HDS.
3. Run VTEC TEST. **Result OK:** Intermittent fault; check VTEC solenoid and ECM connections. **Not OK:** Go to step 4.
4. Turn ignition OFF.
5. Disconnect VTEC solenoid 1P connector.
6. At valve side, measure resistance from solenoid terminal to body ground. **14–30 Ω at room temperature:** Go to step 7. **Otherwise:** Go to step 10.
7. Jump SCS line with HDS.
8. Disconnect ECM connector B (24P).
9. Check continuity between ECM **B6 (VTS, GRN/YEL)** and body ground. **Continuity:** Repair short between ECM B6 and solenoid, then go to step 11. **No continuity:** Go to step 18.
10. Replace VTEC solenoid valve (p. 11-449).
11. Reconnect all connectors.
12. Turn ignition ON (II).
13. Reset ECM with HDS.
14. Do ECM idle learn (p. 11-462).
15. Run VTEC TEST.
16. Check DTCs. **P2648 indicated:** Check solenoid and ECM connections, then return to step 1. **Not indicated:** Go to step 17.

See source image for connector orientation.

---

### Printed page 11-446

<a id="p742"></a>
Source: [PDF p.742, printed p.11-446](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0742.png).

## DTC P2648 troubleshooting (continued)

17. Monitor OBD STATUS for P2648. **PASSED:** Troubleshooting complete; follow other DTCs indicated in step 16. **FAILED:** Check VTEC solenoid and ECM connections, then return to step 1. **NOT COMPLETED:** Go to step 15.
18. Reconnect all connectors.
19. Update ECM software if needed (p. 11-216), or substitute a known-good ECM (p. 11-217).
20. Run VTEC TEST.
21. Check DTCs. **P2648 indicated:** Check solenoid and ECM connections. If ECM was updated, substitute known-good ECM, then return to step 20; if ECM was substituted, return to step 1. **Not indicated:** Go to step 22.
22. Monitor OBD STATUS for P2648. **PASSED:** If ECM was updated, troubleshooting complete; if substituted, replace original ECM (p. 11-389). Follow other DTCs indicated in step 21. **FAILED:** Check solenoid and ECM connections; if ECM was updated, substitute known-good ECM and go to step 20; if substituted, return to step 1. **NOT COMPLETED:** Go to step 20.

---

### Printed page 11-447

<a id="p743"></a>
Source: [PDF p.743, printed p.11-447](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0743.png).

# DTC P2649: Rocker Arm Oil Control Solenoid (VTEC Solenoid Valve) Circuit High Voltage

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (II).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at 3,000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.
4. Check for Temporary DTCs or DTCs with the HDS.

Is DTC P2649 indicated?
- **YES** — Go to step 5.
- **NO** — Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the rocker arm oil control solenoid (VTEC solenoid valve) and the ECM.

5. Turn the ignition switch OFF.
6. Disconnect the rocker arm oil control solenoid (VTEC solenoid valve) 1P connector.
7. At the valve side, measure resistance between the rocker arm oil control solenoid (VTEC solenoid valve) 1P connector terminal and body ground.

**ROCKER ARM OIL CONTROL SOLENOID (VTEC SOLENOID VALVE) 1P CONNECTOR**
*Terminal side of male terminals*

Is there 14—30 Ω at room temperature?
- **YES** — Go to step 8.
- **NO** — Go to step 12.

8. Jump the SCS line with the HDS.
9. Disconnect ECM connector B (24P).
10. Connect the rocker arm oil control solenoid (VTEC solenoid valve) IP connector terminal to body ground with a jumper wire.

**ROCKER ARM OIL CONTROL SOLENOID (VTEC SOLENOID VALVE) IP CONNECTOR**
*Wire side of female terminals*

11. Check for continuity between ECM connector terminal B6 and body ground.

ECM B6 is VTS (GRN/YEL); see source image for connector orientation.

Is there continuity?
- **YES** — Go to step 19.
- **NO** — Repair open in the wire between the ECM (B6) and the rocker arm oil control solenoid (VTEC solenoid valve), then go to step 13.

*(cont'd)*

Page Reference: 11-447

---

### Printed page 11-448

<a id="p744"></a>
Source: [PDF p.744, printed p.11-448](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0744.png).

## DTC P2649 troubleshooting (continued)

12. Replace VTEC solenoid valve (p. 11-449).
13. Reconnect all connectors.
14. Turn ignition ON (II).
15. Reset ECM with HDS.
16. Do ECM idle learn (p. 11-462).
17. Check DTCs. **P2649 indicated:** Check solenoid and ECM connections, then return to step 1. **Not indicated:** Go to step 18.
18. Monitor OBD STATUS for P2649. **PASSED:** Troubleshooting complete; follow other DTCs indicated in step 17. **FAILED:** Check solenoid and ECM connections, then return to step 1. **NOT COMPLETED:** Keep idling until a result appears.
19. Reconnect all connectors.
20. Update ECM software if needed (p. 11-216), or substitute a known-good ECM (p. 11-217).
21. Start engine and let it idle.
22. Check DTCs. **P2649 indicated:** Check solenoid and ECM connections. If ECM was updated, substitute known-good ECM and go to step 21; if ECM was substituted, return to step 1. **Not indicated:** Go to step 23.
23. Monitor OBD STATUS for P2649. **PASSED:** If updated, troubleshooting complete; if substituted, replace original ECM (p. 11-389). Follow other DTCs indicated in step 22. **FAILED:** Check solenoid and ECM connections; if updated, substitute known-good ECM and go to step 21; if substituted, return to step 1. **NOT COMPLETED:** Keep idling until a result appears.

The source image confirms the two-column step order.

---

### Printed page 11-449

<a id="p745"></a>
Source: [PDF p.745, printed p.11-449](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0745.png).

# Rocker Arm Oil Control Valve (VTEC Solenoid Valve) Removal/Installation

1. Disconnect the rocker arm oil control valve (VTEC solenoid valve) 1P connector and rocker arm oil pressure switch (VTEC oil pressure switch) 2 P connector.
2. Remove the bolts (A).
3. Remove the rocker arm oil control valve (VTEC solenoid valve) (B).
4. Install the parts in the reverse order of removal with a new filter (C).

# Rocker Arm Oil Pressure Switch (VTEC Oil Pressure Switch) Removal/Installation

1. Disconnect the rocker arm oil pressure switch (VTEC oil pressure switch) 2 P connector (A).
2. Remove the rocker arm oil pressure switch (VTEC oil pressure switch) (B).
3. Install the parts in the reverse order of removal with a new O-ring (C).

Source printed page: 11-449

---

### Printed page 11-450

<a id="p746"></a>
Source: [PDF p.746, printed p.11-450](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0746.png).

## Idle control system — component location index

- Electrical power steering (EPS) control unit: engine compartment; circuit troubleshooting, p. 11-458.
- Alternator: engine compartment; circuit troubleshooting, p. 11-456.
- A/C compressor: engine compartment; circuit troubleshooting, p. 11-455.
- Engine control module (ECM): driver's side dash; updating, p. 11-216; substitution, p. 11-217; replacement, p. 11-389.
- Brake pedal position switch: pedal area; circuit troubleshooting, p. 11-460.

The source image shows each location.

---

### Printed page 11-451

<a id="p747"></a>
Source: [PDF p.747, printed p.11-451](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0747.png).

# Page 747: DTC Troubleshooting

## DTC P0506: Idle Control System RPM Lower Than Expected

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at **3,000 rpm** without load (in neutral) until the radiator fan comes on, then let it idle.
4. Check this data in the DATA LIST with the HDS.
   - **ECT SENSOR 1** above **158 °F (70 °C)**
   - **IAT SENSOR** above **32 °F (0 °C)**
   - **VSS** is **0 mph (0 km/h)**
   - **ST FUEL TRIM** between **0.69 and 1.47**
   - **FS S** is CLOSED
5. Monitor the OBD **S T A T U S** for DTC P0506 in the DTCs MENU with the HDS.
   Does the screen indicate FAILED?
   - **Y E S** — G o to step 6.
   - **NO** — If the screen indicates PASSED, goto step 15.
     - If the screen indicates EXECUTING, keep idling until a result comes on.
     - If the screen indicates O U T OF CONDITION, go to step 4 and recheck.

6. Remove the intake air duct from the throttle body.
7. Check for dirt, carbon, or damage in the throttle bore.
   Is there dirt, carbon, or damage in the throttle bore?
   - **YES** — If there is dirt or carbon, clean the throttle body (see page 11-499). Also check for damage at the air cleaner element (see page 11-505), then go to step 9. If there is damage in the throttle bore, go to step 8.
   - **NO** — Check the A/C system or power steering system, then go to step 17.

8. Replace the throttle body (see page 11-500).
9. Reset the ECM with the HDS.
10. Do the E C M idle learn procedure (see page 11-462).
11. Start the engine. Hold the engine speed at **3,000 rpm** without load (in neutral) until the radiator fan comes on, then let it idle.
12. Check this data in the DATA LIST with the HDS.
    - **E C T S E N S O R 1** above **158 °F (70 °C)**
    - **IAT S E N S O R** above **32 °F (0 °C)**
    - **VSS** is **0 mph (0 km/h)**
    - **ST FUEL TRIM** between **0.69 and 1.47**
    - **FS S** is CLOSED
13. Check for Temporary DTCs or DTCs with the HDS.
    Is DTC P0506 indicated?
    - **Y E S** — G o to step 19.
    - **NO** — Go to step 14.

*(cont'd)*

Source printed page: 11-451

---

### Printed page 11-452

<a id="p748"></a>
Source: [PDF p.748, printed p.11-452](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0748.png).

# Idle Control System
## DTC Troubleshooting (cont'd)

**14.** Monitor the **OBD S T A T U S** for **DTC P0506** in the **DTCs MENU** with the **HDS**.

Does the screen indicate **PASSED**?

*   **YES**—Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 13, go to the indicated **D T C s** troubleshooting.
*   **NO**—If the screen indicates **FAILED**, check the **A/C** system and/or **power steering system**, then go to step 19. If the screen indicates **EXECUTING**, keep idling until a result comes on. If the screen indicates **OUT OF CONDITION**, go to step 12.

**15.** Remove the intake air duct from the throttle body.

**16.** Check for dirt, carbon, or damage in the throttle bore.

Is there dirt, carbon, or damage in the throttle bore?

*   **YES**—If there is dirt or carbon, clean the throttle body (see page 11-499). Also check for damage at the air cleaner element (see page 11-505), then go to step 9. If there is damage in the throttle bore, go to step 8.
*   **NO**—Go to step 17.

**17.** Recheck with different load conditions (turn on the headlights, blower motor, rear window defogger and/or A/C, changing the gear position, etc.).

**18.** Monitor the **OBD S T A T U S** for **DTC P0506** in the **DTCs MENU** with the **HDS**.

Does the screen indicate **PASSED**?

*   **YES**—Intermittent failure, the system is OK at this time.
*   **NO**—If the screen indicates **FAILED**, check the **A/C** system and/or **power steering system**, then go to step 1. If the screen indicates **EXECUTING**, keep idling until a result comes on. If the screen indicates **OUT OF CONDITION**, go to step 12.

**19.** Update the **ECM** if it does not have the latest software (see page 11-216), or substitute a known-good **E C M** (see page 11-217).

**20.** Start the engine. Hold the engine speed at **3,000 rpm** without load (in neutral) until the radiator fan comes on, then let it idle.

**21.** Check the data in the **DATA LIST** with the **HDS**.

*   **E C T SENSOR 1** above **156 °F (70 °C)** [as printed; source is internally inconsistent]
*   **IAT S E N S O R** above **32 °F (0 °C)**
*   **V S S** is **0 mph (0 km/h)**
*   **S T FUEL TRIM** between **0.69** and **1.47**
*   **F S S** is **CLOSED**

**22.** Check for Temporary DTCs or DTCs with the **HDS**.

Is **DTC P0506** indicated?

*   **YES**—Check for poor connections or loose terminals at the throttle body and the **ECM**. If the **ECM** was updated, substitute a known-good **ECM** (see page 11-217), then go to step 20. If the **ECM** was substituted, go to step 1.
*   **NO**—Go to step 23.

**23.** Monitor the **OBD S T A T U S** for **DTC P0506** in the **DTCs MENU** with the **HDS**.

Does the screen indicate **PASSED**?

*   **YES**—If the **ECM** was updated, troubleshooting is complete. If the **E C M** was substituted, replace the original **E C M** (see page 11-389). If any other Temporary DTCs or DTCs were indicated in step 22, go to the indicated **D T C s** troubleshooting.*
*   **NO**—If the screen indicates **FAILED**, check for poor connections or loose terminals at the throttle body and the **ECM**. If the **E C M** was updated, substitute a known-good **ECM** (see page 11-217), then go to step 20. If the **ECM** was substituted, go to step 1. If the screen indicates **EXECUTING**, keep idling until a result comes on. If the screen indicates **O U T OF CONDITION**, go to step 20.

Source printed page: 11-452

---

### Printed page 11-453

<a id="p749"></a>
Source: [PDF p.749, printed p.11-453](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p0749.png).

# DTC P0507: Idle Control System RPM Higher Than Expected

**NOTE:** Before you troubleshoot, record all freeze data and any on-board snapshot, and review the general troubleshooting information (see page 11-213).

1. Turn the ignition switch ON (**II**).
2. Clear the DTC with the HDS.
3. Start the engine. Hold the engine speed at **3,000 rpm** without load (in neutral) until the radiator fan comes on, then let it idle.
4. Monitor the **OBD S T A T U S** for DTC P0507 in the **DTCs MENU** with the HDS.

Does the screen indicate **FAILED**?
- **Y E S** — G o to step 5.
- **NO** — If the screen indicates **PASSED**, intermittent failure, the system is OK at this time. If the screen indicates **EXECUTING**, keep idling until a result comes on. If the screen indicates **OUT OF CONDITION**, recheck with different load conditions (turn on the headlights, blower motor, or A/C; change the gear position, etc.), then go to step 3.

5. Check for vacuum leaks at these parts:
- PCV valve
- PCV hose
- EVAP canister purge valve
- Throttle body
- Intake manifold
- Brake booster hose

Are there any leaks?
- **YES** — Repair or replace faulty parts, then go to step 6.
- **NO** — Go to step 6.

6. Turn the ignition switch ON (**II**).
7. Reset the ECM with the HDS.
8. Do the **E C M idle learn procedure** (see page 11-462).
9. Start the engine. Hold the engine speed at **3,000 rpm** without load (in neutral) until the radiator fan comes on, then let it idle.
10. Check for Temporary DTCs or DTCs with the HDS.

Is DTC P0507 indicated?
- **Y E S** — G o t o s t e p 12.
- **N O** — G o to step 11.

11. Monitor the **OBD S T A T U S** for DTC P0507 in the **DTCs MENU** with the HDS.

Does the screen indicate **PASSED**?
- **YES** — Troubleshooting is complete. If any other Temporary DTCs or DTCs were indicated in step 10, goto the indicated **D T C s** troubleshooting.
- **NO** — If the screen indicates **FAILED**, go to step 12. If the screen indicates **EXECUTING**, keep idling until a result comes on. If the screen indicates **OUT OF CONDITION**, recheck with different load conditions (turn on the headlights, blower motor, or A/C; change the gear position, etc.), then go to step 9.

*(cont'd)*

Source printed page: 11-453
