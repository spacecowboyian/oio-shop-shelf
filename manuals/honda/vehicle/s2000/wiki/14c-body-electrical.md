# Body Electrical (Part C)

Honda S2000 service manual, PDF pp. 1686–1782 (printed section 22, pp. 22-194–22-290). Covers immobilizer, security, convertible top and defogger, and audio system diagnostics and service.

---

### Printed page 22-194

<a id="p1686"></a>
Source: [PDF p.1686](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1686.png).

# Immobilizer System
## Troubleshooting
### '00-05 models

1. Turn the ignition switch ON (II) with a programmed key.
2. Check to see if the immobilizer indicator comes on.
   - **Does the indicator come on?**
     - **YES** — Go to step 3.
     - **NO** — Go to step 12.

3. Check the immobilizer indicator operation.
   - **Does the indicator come on for 2 seconds, then go off?**
     - **YES** — Go to step 4.
     - **NO** — Go to step 6.

4. Try to crank the engine.
   - **Does the starter motor operate?**
     - **YES** — Go to step 5.
     - **NO** — Check the starter motor.

5. Try to start the engine.
   - **Does the engine start?**
     - **YES** — The immobilizer system is OK at this time.
     - **NO** — Go to step 18.

6. Check to see if the immobilizer indicator comes on and blinks.
   - **Does the indicator blink?**
     - **YES** — Go to step 18.
     - **NO** — Go to step 7.

7. Disconnect ECM connector A (32P).
8. Check to see if the immobilizer indicator goes off.
   - **Does the indicator go off?**
     - **YES** — Substitute a known-good ECM.
     - **NO** — Go to step 9.

9. Turn the ignition switch OFF.
10. Remove the gauge assembly and disconnect its connectors (see page 22-89).

---

### Printed page 22-195

<a id="p1687"></a>
Source: [PDF p.1687](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1687.png).

### Immobilizer troubleshooting, 2000–2005 models (continued)

11. Check continuity between ECM connector A (32P) No. 12 (IMOLMP, PNK) and body ground. **YES:** Repair the short to ground. **NO:** Replace the immobilizer indicator bulb or gauge assembly.
12. Try to start the engine. **Starts:** Go to step 13. **Does not start:** Substitute a known-good ECM and recheck.
13. Turn the ignition switch OFF.
14. Disconnect ECM connector A (32P).
15. Measure voltage between ECM connector A No. 12 and body ground. **Battery voltage:** Go to step 16. **No battery voltage:** Check No. 25 (7.5 A) fuse in the under-dash fuse/relay box; if sound, repair the open wire between the ECM and fuse/relay box.
16. Remove the gauge assembly and disconnect its connectors (see p. 22-89).

Connector views are from the wire side of female terminals.

---

### Printed page 22-196

<a id="p1688"></a>
Source: [PDF p.1688](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1688.png).

### Immobilizer troubleshooting, 2000–2005 models (continued)

17. Check continuity from ECM connector A (32P) No. 12 (IMOLMP, PNK) to gauge assembly connector D (16P) No. 15 on 2000–2003 models, or gauge assembly connector A (22P) No. 4 on 2004–2005 models. **YES:** Replace the immobilizer indicator bulb or gauge assembly. **NO:** Repair the open wire.
18. Turn the ignition switch OFF.
19. Connect the HDS to the data link connector.
20. Turn the ignition switch ON (II).
21. Read System Check in Immobilizer Info. **Normal:** Go to fuel and emissions symptom troubleshooting. **Abnormal:** Go to step 22.
22. Check whether HDS displays an IMOCD line failure. **YES:** Go to step 23. **NO:** Go to step 30.
23. Turn the ignition switch OFF.
24. Check continuity between immobilizer receiver unit 5P connector No. 4 (BRN) and body ground. **YES:** Go to step 25. **NO:** Repair the open wire or, if the wire is sound, repair G101.

Connector views are from the wire side of female terminals.

---

### Printed page 22-197

<a id="p1689"></a>
Source: [PDF p.1689](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1689.png).

# S2000 Body Electrical - Page 1689

## Step 25
Turn the ignition switch OFF.

## Step 26
Disconnect the 5P connector from the immobilizer receiver unit.

## Step 27
Disconnect ECM connector A (32P).

## Step 28
Check for continuity between the immobilizer receiver unit 5P connector No. 2 (IMOCD) terminal and body ground.

**Decision Path:**
- Is there continuity?
  - **YES**—Repair short to ground in the wire.
  - **NO**—Go to step 29.

## Step 29
Check for continuity between the immobilizer receiver unit 5P connector No. 2 (IMOCD) terminal and ECM connector A (32P) No. 25 terminal.

**Decision Path:**
- Is there continuity?
  - **YES**—Substitute a known-good immobilizer receiver unit and/or ECM.
  - **NO**—Repair open in the wire.

## Step 30
Verify the System Check display on the HDS for the following information:
- IMOEN line failure

**Decision Path:**
- Does the HDS display IMOEN line failure?
  - **YES**—Go to step 32.
  - **NO**—Go to step 31.

---

---

### Printed page 22-198

<a id="p1690"></a>
Source: [PDF p.1690](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1690.png).

# Immobilizer System
## Troubleshooting (cont'd)

**31.** Measure the voltage between the immobilizer receiver unit 5P connector No. 1 (IG1) terminal and body ground.

*Connector view: wire side of female terminals.*

**Decision Path:**
*   **Is there battery voltage?**
    *   **YES**—Substitute a known-good immobilizer receiver unit.
    *   **NO**—Faulty No. 46 (15 A) fuse in the main under-hood fuse/relay box. If the fuse is OK, check for an open in the wire between the immobilizer receiver unit and main under-hood fuse/relay box.

**32.** Turn the ignition switch OFF.

**33.** Disconnect 5P connector from the immobilizer receiver unit.

**34.** Disconnect ECM connector A (32P).

**35.** Check for continuity between the immobilizer receiver unit 5P connector No. 3 (IMOEN) terminal and body ground.

*Connector view: wire side of female terminals.*

**Decision Path:**
*   **Is there continuity?**
    *   **YES**—Repair a short to ground in the wire.
    *   **NO**—Go to step 36.

---

### Printed page 22-199

<a id="p1691"></a>
Source: [PDF p.1691](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1691.png).

36. Check continuity between immobilizer receiver unit 5P connector No. 3 (IMOEN, PNK/BLU) and ECM connector A (32P) No. 13 (IMOEN, PNK/BLU). **YES:** Substitute a known-good immobilizer receiver unit and/or ECM. **NO:** Repair the open wire.

Connector views are from the wire side of female terminals.

---

### Printed page 22-200

<a id="p1692"></a>
Source: [PDF p.1692](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1692.png).

# Immobilizer System
## Troubleshooting (cont'd)
### '06-07 models

1. Turn the ignition switch ON (II) with a programmed key.
2. Check to see if the immobilizer indicator comes on.
   - **Does the indicator come on?**
     - **YES** — Go to step 3.
     - **NO** — Go to step 12.

3. Check the immobilizer indicator operation.
   - **Does the indicator come on for 2 seconds, then go off?**
     - **YES** — Go to step 4.
     - **NO** — Go to step 6.

4. Try to crank the engine.
   - **Does the starter motor operate?**
     - **YES** — Go to step 5.
     - **NO** — Check the starter motor.

5. Try to start the engine.
   - **Does the engine start?**
     - **YES** — Check the Status Log in the Immobilizer Info with the HDS (see page 22-214).
     - **NO** — Go to step 28.

6. Check to see if the immobilizer indicator comes on and blinks.
   - **Does the indicator blink?**
     - **YES** — Go to step 28.
     - **NO** — Go to step 7.

7. Disconnect the 7P connector from the immobilizer control unit-receiver.

8. Check to see if the immobilizer indicator goes off.
   - **Does the indicator go off?**
     - **YES** — Substitute a known-good immobilizer control unit-receiver and/or ECM.
     - **NO** — Go to step 9.

9. Turn the ignition switch OFF.

10. Remove the gauge assembly and disconnect its connectors (see page 22-89).

11. Check for continuity between the immobilizer control unit-receiver 7P connector No. 5 (IMOLMP) terminal and body ground.

*IMOLMP: PNK wire; connector view is the wire side of female terminals.*

- **Is there continuity?**
  - **YES** — Repair short to ground in the wire.
  - **NO** — Faulty immobilizer indicator, replace the gauge assembly.

---

### Printed page 22-201

<a id="p1693"></a>
Source: [PDF p.1693](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1693.png).

### Immobilizer troubleshooting, 2006–2007 models (continued)

12. Try to start the engine. **Starts:** Go to step 13. **Does not start:** Go to step 19.
13. Turn the ignition switch OFF.
14. Disconnect the 7P connector from the immobilizer control unit-receiver.
15. Measure voltage between connector No. 7 (+B, WHT/RED) and body ground. **Battery voltage:** Go to step 16. **No battery voltage:** Check No. 25 (7.5 A) fuse in the under-dash fuse/relay box; if sound, repair the open wire to the control unit-receiver.
16. Ground connector No. 5 (IMOLMP, PNK) with a jumper wire. **Indicator comes on:** Replace the immobilizer control unit-receiver. **Indicator stays off:** Go to step 17.
17. Remove the gauge assembly and disconnect its 22P connector (see p. 22-89).

Connector views are from the wire side of female terminals.

---

### Printed page 22-202

<a id="p1694"></a>
Source: [PDF p.1694](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1694.png).

### Immobilizer troubleshooting, 2006–2007 models (continued)

18. Check continuity between immobilizer control unit-receiver 7P connector No. 5 (IMOLMP, PNK) and gauge assembly connector A (22P) No. 4. **YES:** Replace the immobilizer indicator bulb or gauge assembly. **NO:** Repair the open wire.
19. Turn the ignition switch OFF.
20. Disconnect the 7P connector from the immobilizer control unit-receiver.
21. Turn the ignition switch ON (II).
22. Measure voltage between 7P connector No. 6 (IG1, BLK/YEL) and body ground. **Battery voltage:** Go to step 23. **No battery voltage:** Check No. 2 (15 A) fuse in the under-dash fuse/relay box; if sound, repair the open wire to the control unit-receiver.
23. Measure voltage between 7P connector No. 1 (LG3, GRN/WHT) and No. 6 (IG1, BLK/YEL). **Battery voltage:** Substitute a known-good immobilizer control unit-receiver and recheck. **No battery voltage:** Go to step 24.

Connector views are from the wire side of female terminals.

---

### Printed page 22-203

<a id="p1695"></a>
Source: [PDF p.1695](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1695.png).

### Immobilizer troubleshooting, 2006–2007 models (continued)

24. Turn the ignition switch OFF.
25. Jump the SCS line with the HDS.
26. Disconnect ECM connector E (31P; see p. 11-389).
27. Check continuity between immobilizer control unit-receiver 7P connector No. 1 (LG3, GRN/WHT) and ECM connector E (31P) No. 3 (LG3, GRN/WHT). **YES:** Check G101 for a poor connection; if sound, substitute a known-good control unit-receiver and recheck. **NO:** Repair the open wire.
28. Turn the ignition switch OFF.
29. Connect the HDS to the data link connector.
30. Turn the ignition switch ON (II).
31. Read System Check in Immobilizer Info (p. 22-213). **Normal:** Go to fuel and emissions symptom troubleshooting. **Abnormal:** Go to step 32.
32. Check for any of these HDS reports: IMOCD (S-Net) line short between ECM and control unit-receiver; low battery voltage interrupting communication; noise interrupting communication; control unit-receiver failure; ECM failure. **Any displayed:** Go to step 33. **None:** Go to step 38.
33. Turn the ignition switch OFF.
34. Disconnect the 7P connector from the immobilizer control unit-receiver.
35. Jump the SCS line with the HDS.
36. Disconnect ECM connector E (31P; see p. 11-389).

Connector views are from the wire side of female terminals.

---

### Printed page 22-204

<a id="p1696"></a>
Source: [PDF p.1696](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1696.png).

# Immobilizer System
## Troubleshooting (cont'd)

**37.** Check for continuity between the immobilizer control unit-receiver 7P connector No. 2 IMOCD (S-Net) terminal and body ground.

```
IMMOBILIZER CONTROL UNIT-RECEIVER 7P CONNECTOR
1   2   3   4   5   6   7
IMOCD (RED/BLU)
Wire side of female terminals
```

Is there continuity?

* **YES** — Repair a short to ground in the wire.
* **NO** — Substitute a known-good immobilizer control unit-receiver and/or ECM.

---

**38.** Verify the System Check display on the HDS for the following information:

* Blown fuse
* Harness open from the ECM and the immobilizer control unit-receiver.
* The communication was not good between the ECM and the immobilizer unit by battery voltage low.
* The communication was not good between the immobilizer control unit-receiver and the ECM by influence of some noise.
* Immobilizer control unit-receiver failure
* ECM failure

Does the HDS display any of the preceding information?

* **YES** — Go to step 39.
* **NO** — Check the Possible Failures shown on the System Check display (see page 22-213).

---

**39.** Turn the ignition switch OFF.

**40.** Disconnect the 7P connector from the immobilizer control unit-receiver.

**41.** Jump the SCS line with the HDS.

**42.** Disconnect ECM connector E (31P) (see page 11-389).

---

### Printed page 22-205

<a id="p1697"></a>
Source: [PDF p.1697](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1697.png).

43. Check continuity between immobilizer control unit-receiver 7P connector No. 2 (IMOCD/S-Net, RED/BLU) and ECM connector E (31P) No. 27 (IMOCD/S-Net, RED/BLU). **YES:** Substitute a known-good control unit-receiver and recheck; if it is sound, substitute a known-good ECM and recheck. **NO:** Repair the open wire.

Connector views are from the wire side of female terminals.

---

### Printed page 22-206

<a id="p1698"></a>
Source: [PDF p.1698](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1698.png).

# Immobilizer System
## Troubleshooting (cont'd)
### '08 model

1. Turn the ignition switch ON (II) with a programmed key.
2. Check to see if the immobilizer indicator comes on.
   - **Does the indicator come on?**
     - **YES** — Go to step 3.
     - **NO** — Go to step 12.

3. Check the immobilizer indicator operation.
   - **Does the indicator come on for 2 seconds, then go off?**
     - **YES** — Go to step 4.
     - **NO** — Go to step 6.

4. Try to crank the engine.
   - **Does the starter motor operate?**
     - **YES** — Go to step 5.
     - **NO** — Check the starter motor.

5. Try to start the engine.
   - **Does the engine start?**
     - **YES** — Intermittent failure, the vehicle is OK at this time. Check the **SYSTEM CHECK** and **STATUS LOG** information (see page 22-214).
     - **NO** — Go to step 28.

6. Check to see if the immobilizer indicator comes on and blinks.
   - **Does the indicator blink?**
     - **YES** — Go to step 28.
     - **NO** — Go to step 7.

7. Disconnect the 7P connector from the immobilizer control unit-receiver.

8. Check to see if the immobilizer indicator goes off.
   - **Does the indicator go off?**
     - **YES** — Go to step 43.
     - **NO** — Go to step 9.

9. Turn the ignition switch OFF.

10. Remove the gauge assembly and disconnect its connectors (see page 22-89).

11. Check for continuity between the immobilizer control unit-receiver 7P connector No. 5 (**IMOLMP**) terminal and body ground.

*IMOLMP: connector No. 5, PNK wire; view from wire side of female terminals.*

- **Is there continuity?**
  - **YES** — Repair a short to ground in the wire.
  - **NO** — Faulty immobilizer indicator, replace the gauge assembly.

---

### Printed page 22-207

<a id="p1699"></a>
Source: [PDF p.1699](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1699.png).

### Immobilizer troubleshooting, 2008 model (continued)

12. Try to start the engine. **Starts:** Go to step 13. **Does not start:** Go to step 19.
13. Turn the ignition switch OFF.
14. Disconnect the 7P connector from the immobilizer control unit-receiver.
15. Measure voltage between connector No. 7 (+B, WHT/RED) and body ground. **Battery voltage:** Go to step 16. **No battery voltage:** Check No. 25 (7.5 A) fuse in the under-dash fuse/relay box; if sound, repair the open wire to the control unit-receiver.
16. Ground connector No. 5 (IMOLMP, PNK) with a jumper wire. **Indicator comes on:** Replace the immobilizer control unit-receiver. **Indicator stays off:** Go to step 17.
17. Remove the gauge assembly and disconnect connector A (22P; see p. 22-89).

Connector views are from the wire side of female terminals.

---

### Printed page 22-208

<a id="p1700"></a>
Source: [PDF p.1700](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1700.png).

# Immobilizer System
## Troubleshooting (continued)

### 18. Check for continuity between the immobilizer control unit-receiver 7P connector No. 5 (IMOLMP) terminal and gauge assembly connector A (22P) No. 4 terminal.

**Is there continuity?**
*   **YES**—Faulty immobilizer indicator, replace the immobilizer indicator bulb or gauge assembly.
*   **NO**—Repair an open in the wire.

### 19. Turn the ignition switch OFF.

### 20. Disconnect the 7P connector from the immobilizer control unit-receiver.

### 21. Turn the ignition switch ON (II).

### 22. Measure the voltage between the immobilizer control unit-receiver 7P connector No. 6 (IG1) terminal and body ground.

**IMMOBILIZER CONTROL UNIT-RECEIVER 7P CONNECTOR**
*Wire side of female terminals*
| Pin | Wire Color |
|---|---|
| 1 | - |
| 2 | - |
| 3 | - |
| 4 | - |
| 5 | - |
| 6 | IG1 (BLK/YEL) |
| 7 | - |

**Is there battery voltage?**
*   **YES**—Go to step 23.
*   **NO**—Faulty No. 2 (15 A) fuse in the under-dash fuse/relay box. If the fuse is OK, check for an open in the wire between the immobilizer control unit-receiver and under-dash fuse/relay box.

### 23. Measure the voltage between the immobilizer control unit-receiver 7P connector No. 1 (LG3) and No. 6 (IG1) terminals.

**IMMOBILIZER CONTROL UNIT-RECEIVER 7P CONNECTOR**
*Wire side of female terminals*
| Pin | Wire Color |
|---|---|
| 1 | LG3 (GRN/WHT) |
| 2 | - |
| 3 | - |
| 4 | - |
| 5 | - |
| 6 | IG1 (BLK/YEL) |
| 7 | - |

**Is there battery voltage?**
*   **YES**—Substitute a known-good immobilizer control unit-receiver control, and recheck.
*   **NO**—Go to step 24.

---

---

### Printed page 22-209

<a id="p1701"></a>
Source: [PDF p.1701](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1701.png).

24. Turn the ignition switch OFF.
25. Jump the SCS line with the HDS.
26. Disconnect ECM connector E (31P).
27. Check continuity between immobilizer control unit-receiver 7P connector No. 1 and ECM connector E (31P) No. 3 (LG3, GRN/WHT). **YES:** Check G101 for a poor or loose connection; if sound, substitute a known-good control unit-receiver and recheck. **NO:** Repair the open wire.

Connector views are from the wire side of female terminals.

---

### Printed page 22-210

<a id="p1702"></a>
Source: [PDF p.1702](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1702.png).

### Immobilizer troubleshooting, 2008 model (continued)

28. Turn the ignition switch OFF.
29. Connect the HDS to the data link connector.
30. Turn the ignition switch ON (II).
31. In HDS Immobilizer Info, check System Check (p. 22-213) for: IMOCD (S-Net) line short between ECM and control unit-receiver; low battery voltage or electrical noise disrupting communication; control unit-receiver failure; ECM failure; imoes unit failure. **Any displayed:** Go to step 32. **None:** Go to step 37.
32. Turn the ignition switch OFF.
33. Disconnect the 7P connector from the immobilizer control unit-receiver.
34. Jump the SCS line with the HDS.
35. Disconnect ECM connector E (31P).
36. Check continuity between 7P connector No. 2 (IMOCD/S-Net, RED/BLU) and body ground. **YES:** Repair the short to ground. **NO:** Go to step 43.

Connector view is from the wire side of female terminals.

---

### Printed page 22-211

<a id="p1703"></a>
Source: [PDF p.1703](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1703.png).

37. Check HDS Status Log for: blown fuse; open harness between ECM and control unit-receiver; low battery voltage or noise disrupting communication; control unit-receiver, ECM, or imoes unit failure. **Any displayed:** Check Possible Failures on the Status Log display (p. 22-214). **None:** Go to step 38.
38. Turn the ignition switch OFF.
39. Disconnect the 7P connector from the immobilizer control unit-receiver.
40. Jump the SCS line with the HDS.
41. Disconnect ECM connector E (31P).
42. Check continuity between control unit-receiver 7P connector No. 2 and ECM connector E (31P) No. 27 (IMOCD/S-Net, RED/BLU). **YES:** Go to step 43. **NO:** Repair the open wire.

Connector views are from the wire side of female terminals.

---

### Printed page 22-212

<a id="p1704"></a>
Source: [PDF p.1704](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1704.png).

43. Check continuity between imoes unit 5P connector No. 2 and ECM connector E (31P) No. 27 (IMOCD/S-Net, RED/BLU). **YES:** Substitute a known-good imoes unit and/or immobilizer control unit-receiver and recheck. If those units are sound, substitute a known-good ECM and recheck. **NO:** Repair the open wire.

Connector views are from the wire side of female terminals.

---

### Printed page 22-213

<a id="p1705"></a>
Source: [PDF p.1705](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1705.png).

### System Check, 2006–2008 models

The HDS System Check tests immobilizer key registration and the IMOCD (S-Net) line. Connect HDS to the data link connector, turn ignition ON (II), and monitor System Check in Immobilizer Info. If “Immobilizer system is normal” appears, the system is OK. Otherwise use the Status Log No. below; each row reports “Immobilizer system is not normal.”

| Status Log | Possible failures |
|---|---|
| A-1 | Key unregistered (register with “KEYS”); metal near the key; low battery voltage. |
| A-2 | Intermittent transponder communication; wrong vehicle/company key type; transponder failure; metal near key; low battery voltage. |
| A-3 | Non-immobilizer key used; wrong key type; transponder failure; metal near key; low battery voltage; immobilizer control unit-receiver failure. |
| B-1, B-2 | ECM unregistered (register with “REPLACE ECM”); low battery voltage; electrical noise between ECM and control unit-receiver. |
| C-1* | Imoes unit unregistered (register with “REPLACE IMOES”). |
| C-2* | Imoes unit unregistered; noise disrupting communication with control unit-receiver. |
| D-1 | IMOCD (S-Net) short from ECM to control unit-receiver; low battery voltage; electrical noise; control unit-receiver or ECM failure. |
| D-2* | Blown fuse; open harness between control unit-receiver and imoes unit; electrical noise between them. |
| D-3 | Blown fuse; open harness between ECM and control unit-receiver; low battery voltage; electrical noise; control unit-receiver or ECM failure. |

\* 2008 model only.

---

### Printed page 22-214

<a id="p1706"></a>
Source: [PDF p.1706](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1706.png).

# Immobilizer System
## Status Log
### '06-08 models

If you suspect there is an immobilizer system problem, the HDS can be used to check the number of times the immobilizer control unit-receiver doesn't permit the engine to run by checking the status log.

**NOTE:** The Status Log count can be reset by disconnecting the negative battery terminal or by removing the No. 25 (7.5 A) fuse in the under-dash fuse/relay box, or by disconnecting the 7P connector from the immobilizer control unit-receiver.

1. Connect the HDS to the data link connector.
2. Turn the ignition switch ON (II).
3. On the HDS screen, select Honda systems, select immobilizer set-up, select immobilizer information, then select status log.
4. Check the Status log count. Troubleshoot the status with the highest count first. If no counts are listed, the immobilizer system is OK. Continue with normal symptom troubleshooting.

| Status Log No. | Detected item | Probable causes |
|---|---|---|
| A-1 | KEY CODE MISMATCH (Code format normal, but code data is mismatch) | 1. The key was not registered<br>2. Interference from metal such as key chains<br>3. Low battery voltage |
| A-2 | KEY CODE MISMATCH (Code format failure) | 1. Ignition switch was turn on with another type of immobilizer key or aftermarket key<br>2. Interference from metal such as key chains<br>3. Low battery voltage |
| A-3 | KEY CODE MISMATCH (No key code or non-immobilizer key) | 1. Ignition switch was turn on with another type of immobilizer key or aftermarket key<br>2. Interference from metal such as key chains<br>3. Low battery voltage<br>4. Key failure<br>5. Immobilizer control unit-receiver failure |
| B-1 | ECM CODE MISMATCH (Code format normal, but code data is mismatch) | 1. ECM was not registered correctly<br>2. Low battery voltage<br>3. Poor or loose terminal connections at the immobilizer control unit-receiver<br>4. Communication line electrical noise |
| B-2 | ECM MISMATCH (Code format failure) | 1. ECM was not registered correctly<br>2. Low battery voltage<br>3. Poor or loose terminal connections at the immobilizer control unit-receiver<br>4. Communication line electrical noise |
| D-1 | IMOCD (S-Net) terminal PROBLEM (Short to ground) | 1. Low battery voltage<br>2. Poor or loose terminal connections at the immobilizer control unit-receiver and the ECM<br>3. Communication line electrical noise<br>4. Short in the harness from the ECM to the immobilizer control unit-receiver (IMOCD (S-Net) line short) |
| D-3 | IMOCD (S-Net) terminal PROBLEM (Open line or ECM failure) | 1. Open in the harness from the ECM to the immobilizer control unit-receiver<br>2. Low battery voltage<br>3. Poor or loose terminal connections at the immobilizer control unit-receiver and the ECM<br>4. Communication line electrical noise |

**

---

### Printed page 22-215

<a id="p1707"></a>
Source: [PDF p.1707](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1707.png).

# Imoes Unit Input Test/Replacement

**'08 model**

1. Remove the blower motor (see page 21-62).
2. Remove the bolt (A) from the imoes unit bracket (B).
3. Remove the imoes unit (C) from the imoes unit bracket.
4. Disconnect the 5P connector (D) from the imoes unit.
5. Inspect the connector and socket terminals to be sure they are all making good contact.

*5P connector view: wire side of female terminals; cavities 1–5.*

• If the terminals are bent, loose or corroded, repair them as necessary and recheck the system.
• If the terminals look OK, go to step 3.

*(cont'd)*

**Page Reference:** 22-21

---

### Printed page 22-216

<a id="p1708"></a>
Source: [PDF p.1708](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1708.png).

### Imoes unit input test, 2008 model (continued)

6. With connectors disconnected, make the following input tests. Correct any failed test and recheck. If all pass, replace the imoes unit, register it with HDS, and verify that the immobilizer indicator blinks correctly.

| Cavity / wire | Condition and desired result | If failed |
|---|---|---|
| 5 WHT/RED (+B) | Under all conditions, voltage to ground should be battery voltage. | No. 54 (30 A) main under-hood or No. 25 (7.5 A) under-dash fuse blown; open wire. |
| 3 BLK/YEL (IG1) | Ignition ON (II): voltage to ground should be battery voltage. | No. 2 (15 A) under-dash fuse blown; open wire. |
| 1 GRN/WHT (LG3) | Jump SCS with HDS and disconnect ECM connector E (31P). Continuity to ECM connector E No. 3 should be present. | Open wire. |
| 4 RED/WHT (KEY SW) | Key inserted: voltage to ground should be less than 1 V. | Faulty ignition key switch; open wire; poor ground G401. |
| 4 RED/WHT (KEY SW) | Key removed: voltage to ground should be battery voltage. | Faulty ignition key switch; short to ground. |
| 2 RED/BLU (IMOCD/S-Net) | Jump SCS with HDS; disconnect ECM connector E (31P) and control unit-receiver 7P. Continuity to ECM connector E No. 27 and control unit-receiver No. 2 should be present. | Open wire. |
| 2 RED/BLU (IMOCD/S-Net) | With the same connectors disconnected, continuity to body ground should be absent. | Short to ground. |

---

### Printed page 22-217

<a id="p1709"></a>
Source: [PDF p.1709](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1709.png).

# Immobilizer Receiver Unit Replacement

## '00-05 models

1. Remove the steering column covers (see page 17-9).
2. Disconnect the 5P connector (A) from the immobilizer receiver unit (B).
3. Disconnect the 7P connector (C) from the ignition key switch.
4. Remove the four screws, and remove the immobilizer receiver unit from the ignition key cylinder.
5. Install in the reverse order of removal.
6. After replacement, make sure the immobilizer indicator blinks correctly.

**NOTE:** The ECM does not need to be reprogrammed if only the receiver has been replaced.

## '06-08 models

1. Remove the steering column covers (see page 17-9).
2. Disconnect the 7P connector (A) from the immobilizer control unit-receiver (B).
3. Disconnect the 7P connector (C) from the ignition key switch.
4. Remove the four screws, and remove the immobilizer control unit-receiver from the ignition key cylinder.
5. Install in the reverse order of removal.
6. Register the immobilizer control unit-receiver with the HDS.

**NOTE:** The ECM code and all of the customer's keys are required.
7. After replacement, make sure the immobilizer indicator blinks correctly.

---

### Printed page 22-218

<a id="p1710"></a>
Source: [PDF p.1710](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1710.png).

# Page 1710: Immobilizer System - Key Registration Procedures

## '08 Model

**NOTE:**
*   The HDS is required for registration of the immobilizer keys.
*   Check for aftermarket electrical equipment that can cause problems with transponder operation.
*   The immobilizer control unit-receiver can store up to six immobilizer Keys.

### Add one new key

1.  Have a registered key, a new immobilizer key that has been cut to fit the ignition switch, and the first password from the IN system.
2.  Connect the HDS to the data link connector.
3.  Turn the Ignition switch ON (II).
4.  Select "IMMOBILIZER" from the "SYSTEM SELECT" menu.
5.  Select "Add and Delete Keys", then "Add 1 key".
6.  Do the registration according to the instructions on the HDS screen.
7.  Check If the engine can be started by the newly registered key.
8.  Check the keyless remote operation to make sure that it functions properly.

### Delete or add multiple Keys

**NOTE:** If any of the registered keys were lost, do the following procedure to delete the lost registered key.

1.  Have all registered keys, all new keys, and the first password from the IN system.
2.  Connect the HDS to the data link connector.
3.  Turn the ignition switch ON (II).
4.  Select "IMMOBILIZER" from the "SYSTEM SELECT" menu.
5. Select “Add and Delete Keys” or “Delete or Add Multiple Keys”.
6. Do the registration according to the instructions on the HDS screen.
7.  Check if the engine can be started by all the registered keys.
8.  Check the keyless remote operation to make sure that it functions properly.

### All keys are lost

1.  Prepare all new keys and have the Immobilizer ECM code from the IN system.
2.  Connect the HDS to the data link connector.
3.  Turn the Ignition switch ON (II).
4.  Select "IMMOBILIZER" from the "SYSTEM SELECT" menu.
5.  Select "Add and Delete Keys", then "ALL KEYS LOST".
6.  Do the registration according to the Instruction of the HDS screen.
7.  Check if the engine can be started by all the registered keys.
8.  Check the keyless remote operation to make sure that it functions properly.


**Page Reference:** 22-218

---

### Printed page 22-219

<a id="p1711"></a>
Source: [PDF p.1711](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1711.png).

### Power windows — component location index

The diagram locates the power window master switch and driver's window motor in the driver's door, and the passenger's switch and motor in the passenger's door. The master switch contains the control unit. See master switch test p. 22-221, input test p. 22-222, passenger switch test/replacement p. 22-225, and motor tests p. 22-226. Use the source image for the exact positions.

---

### Printed page 22-220

<a id="p1712"></a>
Source: [PDF p.1712](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1712.png).

### Power windows — circuit diagram

The source diagram shows battery feed through main under-hood fuses No. 41 (100 A), No. 42 (40 A), and No. 51 (40 A), then under-dash fuses No. 8 and No. 17 (both 20 A). It shows the power window master switch with its control unit, passenger switch, both window motors, convertible top control unit, and ground G501. Use the source diagram for terminal-to-terminal wiring and switch positions; the OCR does not preserve the circuit topology.

---

### Printed page 22-221

<a id="p1713"></a>
Source: [PDF p.1713](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1713.png).

### Power window master switch test

1. Remove the driver's door panel (p. 20-5).
2. Disconnect the 14P connector from the master switch.
3. Check continuity for the passenger switch in each position. The driver's switch is combined with the control unit and cannot be isolated; use the master switch input test (step 6, p. 22-224).

| Passenger switch | Main switch | Terminals with continuity |
|---|---|---|
| OFF | ON | 4–12 |
| OFF | OFF | None shown |
| UP | ON | 13–4–12 |
| UP | OFF | 13–12 |
| DOWN | ON | 4–6–12 |
| DOWN | OFF | 6–12 |

4. If continuity differs, replace the switch. The source image shows the 14P connector cavity layout.

---

### Printed page 22-222

<a id="p1714"></a>
Source: [PDF p.1714](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1714.png).

### Power window master switch input test

1. Remove the door panel (p. 20-5).
2. Remove the master switch (A) from the door panel.
3. Disconnect its 14P connector (B) and 10P connector (C).
4. Inspect connectors and socket terminals for good contact. Repair bent, loose, or corroded terminals and recheck. If sound, continue to step 5.

The source image shows the wire-side view of the female terminals and switch removal.

---

### Printed page 22-223

<a id="p1715"></a>
Source: [PDF p.1715](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1715.png).

### Power window master switch input test — step 5

Reconnect the master switch and perform these tests at the 14P connector. Repair any failed test and recheck; if all pass, go to step 6.

| Cavity / wire | Condition and desired result | Possible cause if failed |
|---|---|---|
| 4 GRN/BLK | Ignition ON (II); voltage to ground: battery voltage. | No. 8 (20 A) under-dash fuse blown; open wire. |
| 1 BLK | All conditions; voltage to ground: less than 0.5 V. | Poor G501 ground; open wire. |
| 11 GRN/WHT | All conditions; voltage to ground: battery voltage. | No. 17 (20 A) under-dash fuse blown; open wire. |
| 8 BLU | Operate driver's window switch; voltage between No. 8 and No. 2: 0–5 V or more repeatedly. | Driver's window motor or master switch faulty; open wire. |
| 2 BLK | All conditions; voltage to ground: less than 0.5 V. | Master switch faulty; open wire. |
| 14 BLU/ORN | Ignition ON (II), convertible top switch ON, parking brake UP; voltage between No. 14 and No. 1: 0–8 V or more repeatedly. | Convertible top control unit or master switch faulty; open wire. |

---

### Printed page 22-224

<a id="p1716"></a>
Source: [PDF p.1716](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1716.png).

### Power window master switch input test — steps 6–7

6. Disconnect the 14P and 10P connectors from the master switch; test at the 14P connector. Correct any failed test and recheck. If all pass, go to step 7.

| Cavity / wire | Connection and desired result | Possible cause if failed |
|---|---|---|
| 13 BLU/RED and 12 RED/WHT | Connect No. 4 to No. 13 and No. 4 to No. 12; turn ignition ON (II). Then connect No. 4 to No. 12, turn ignition ON (II), and turn passenger switch UP. Passenger motor should run, window moving up. | No. 8 or No. 18 (both 20 A) under-dash fuse blown; passenger motor or switch faulty; convertible top control unit faulty; poor G501 ground; open wire. |
| 6 BLU/WHT | Connect No. 4 to No. 6. Passenger motor should run, window moving down. | Same passenger circuit causes above. |
| 5 RED/BLK | Connect No. 5 to No. 11 and No. 3 to No. 1. Driver's motor should run, window moving up. | No. 17 (20 A) under-dash fuse blown; master switch or driver's motor faulty; open wire; poor G501 ground. |
| 3 RED/YEL | Connect No. 3 to No. 11 and No. 5 to No. 1. Driver's motor should run, window moving down. | Same driver circuit causes above. |

7. If all input tests pass, replace the faulty master switch.

---

### Printed page 22-225

<a id="p1717"></a>
Source: [PDF p.1717](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1717.png).

### Passenger power window switch test/replacement

1. Remove the passenger switch and switch panel from the door panel.
2. Disconnect the switch 6P connector.
3. Remove the two mounting screws from the switch panel.
4. Check continuity in each switch position:

| Position | Terminals with continuity |
|---|---|
| UP | 3–4–6 |
| OFF | 3–6 |
| DOWN | 1–3 and 2–6 |

5. Replace the switch if continuity differs. The source image shows the 6P connector orientation.

---

### Printed page 22-226

<a id="p1718"></a>
Source: [PDF p.1718](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1718.png).

### Driver's power window motor test

Remove the driver's door panel (p. 20-5), disconnect the motor 4P connector, and apply battery power and ground to terminals 1 and 2. For **UP**, No. 1 is ground and No. 2 is positive. For **DOWN**, No. 1 is positive and No. 2 is ground. Disconnect one lead immediately when the motor stops. Replace a motor that does not run smoothly.

For the detect circuit, connect an analog ohmmeter to No. 3 and No. 4. Run the motor with power and ground on No. 1 and No. 2; the needle should alternate back and forth. Otherwise replace the motor.

### Passenger's power window motor test

Remove the passenger door panel (p. 20-5) and disconnect the 2P motor connector. For **UP**, No. 1 is positive and No. 2 is ground. For **DOWN**, No. 1 is ground and No. 2 is positive. Disconnect one lead immediately when the motor stops. Replace a motor that does not run smoothly. Connector views are from the terminal side of male terminals.

---

### Printed page 22-227

<a id="p1719"></a>
Source: [PDF p.1719](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1719.png).

### Keyless/power door lock system — component location index

The source diagram identifies the transmitter (lock, unlock, trunk, and panic buttons; test p. 22-234; programming/deleting p. 22-235), passenger door switch, ignition key switch (test p. 22-232), trunk lid opener solenoid (test p. 22-168), driver door key-cylinder switch (test p. 22-234), driver and passenger door lock actuators (p. 22-233), driver door lock knob switch (p. 22-232), and keyless door lock control unit (input test p. 22-229). Use the image for exact locations.

---

### Printed page 22-228

<a id="p1720"></a>
Source: [PDF p.1720](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1720.png).

### Keyless/power door lock system — circuit diagram

The source diagram shows battery feeds through main under-hood fuses No. 41 (100 A), No. 42 (40 A), and No. 54 (30 A), then under-dash fuses No. 5 (7.5 A) and No. 26 (15 A). The keyless door lock control unit interfaces with the transmitter, gauge assembly, ignition key switch, door switches, key-cylinder switch, door lock knob switch, both door lock actuators, trunk lid opener switch and solenoid, horn relay, ceiling/spotlights, and grounds G401 and G501. Use the source diagram for exact terminal and wire connections; OCR does not preserve their topology.

---

### Printed page 22-229

<a id="p1721"></a>
Source: [PDF p.1721](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1721.png).

### Keyless door lock control unit input test

1. Disconnect the control unit 18P connector.
2. Check connector and socket terminals for good contact. Repair bent, loose, or corroded terminals and recheck. If sound, go to step 3.

The source image shows the 18P female-terminal wire-side view: No. 2 GRN/YEL, 3 ORN, 4 RED/BLK, 5 BLK/YEL, 6 PNK/BLK, 7 YEL/GRN, 8 WHT, 9 YEL, 10 YEL/BLK, 13 RED/WHT, 14 BLK/WHT, 15 WHT, 16 YEL, 17 BLK, 18 PNK/BLU.

---

### Printed page 22-230

<a id="p1722"></a>
Source: [PDF p.1722](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1722.png).

### Keyless door lock control unit input test — step 3

Reconnect the connector and test at the control unit. Correct any failed test and recheck; if all pass, go to step 4.

| Cavity / wire | Condition and desired result | Possible cause if failed |
|---|---|---|
| 17 BLK | All conditions; ground voltage less than 0.5 V. | Poor G501 ground; open wire. |
| 5 BLK/YEL | All conditions; ground voltage less than 1 V. | Trunk lid opener solenoid faulty; poor G601 ground; open wire. |
| 8 WHT | All conditions; battery voltage to ground. | No. 26 (15 A) under-dash fuse blown; open wire. |
| 16 YEL | Ignition ON (II); battery voltage to ground. | No. 5 (7.5 A) under-dash fuse blown; open wire. |
| 4 RED/BLK | Lighting switch ON; battery voltage to ground. | No. 23 (10 A) under-dash fuse blown; taillight relay faulty; open wire. |
| 3 ORN | All conditions; battery voltage to ground. | No. 47 main under-hood fuse blown (10 A for 2000–2001, 15 A for 2002–2008); horn relay faulty; open wire. |
| 14 BLK/WHT | Either door open; 1 V or less to ground. | Door switch or gauge assembly faulty; open wire. |
| 2 GRN/YEL | Both doors closed, ceiling/spotlight switch MIDDLE; battery voltage to ground. | No. 24 (7.5 A) under-dash fuse blown; ceiling/spotlight bulb blown; open wire. |
| 10 YEL/BLK | Driver lock knob at LOCK; less than 1 V to ground. | Door lock actuator or gauge assembly faulty; poor G501 ground; open wire. |
| 9 YEL | Driver lock knob at UNLOCK; less than 1 V to ground. | Same causes as No. 10. |
| 13 RED/WHT | Key inserted; less than 1 V to ground. | Gauge assembly or ignition key switch faulty; poor G401 ground; open or grounded wire. |
| 13 RED/WHT | Key removed; 5 V or more to ground. | Same causes as inserted-key test. |
| 15 WHT | Driver key-cylinder switch at UNLOCK; less than 1 V to ground. | Key-cylinder switch faulty; poor G501 ground; open or grounded wire. |
| 15 WHT | Driver key-cylinder switch at LOCK or neutral; 5 V or more to ground. | Same causes as UNLOCK test. |

---

### Printed page 22-231

<a id="p1723"></a>
Source: [PDF p.1723](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1723.png).

### Disconnect and Input Test Procedure

Disconnect the 18P connector from the control unit, then make these input tests at the connector.

* If any test indicates a problem, find and correct the cause, then recheck the system.
* If all the input tests prove OK, the control unit must be faulty; replace it.

#### Cavity Wire Test

| Test condition | Test: Desired result | Possible cause if desired result is not obtained |
| :--- | :--- | :--- |
| **7 YEL/GRN** | Connect the No. 7 terminal to the No. 8 terminal, and the No. 6 terminal to the No. 17 terminal momentarily.<br><br>Check the door lock operation:<br>The driver's door should unlock. | • Faulty door lock actuator<br>• Blown No. 26 (15 A) fuse in the under-dash fuse/relay box<br>• Poor ground (G501)<br>• An open in the wire |
| **18 PNK/BLU** | Connect the No. 18 terminal to the No. 8 terminal, and the No. 6 terminal to the No. 17 terminal momentarily.<br><br>Check the door lock operation:<br>The passenger's door should unlock. | • Faulty door lock actuator<br>• Blown No. 26 (15 A) fuse in the under-dash fuse/relay box<br>• Poor ground (G501)<br>• An open in the wire |
| **6 PNK/BLK** | Connect the No. 6 terminal to the No. 8 terminal, and the No. 7 and No. 18 terminals to the No. 17 terminal momentarily.<br><br>Check the door lock operation:<br>Both doors should lock. | • Faulty door lock actuator<br>• Blown No. 26 (15 A) fuse in the under-dash fuse/relay box<br>• Poor ground (G501)<br>• An open in the wire |

---

### Printed page 22-232

<a id="p1724"></a>
Source: [PDF p.1724](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1724.png).

### Ignition key switch test

Remove the steering column covers (p. 17-9) and disconnect the 7P connector. Check continuity between No. 1 and No. 3: present with the key inserted, absent with the key removed. Replace the ignition key switch if different.

### Driver's door lock knob switch test

Remove the driver's door panel (p. 20-5), then disconnect the 3P connector (A) from the driver's door lock actuator (B). In LOCK, continuity should be between A1–A2. In UNLOCK, continuity should be between A2–A3. Replace the door lock actuator assembly if different. Connector orientation is shown in the source image.

---

### Printed page 22-233

<a id="p1725"></a>
Source: [PDF p.1725](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1725.png).

### Door lock actuator tests

Remove the relevant door panel (p. 20-5) and disconnect the actuator's 2P connector. Apply battery voltage **momentarily** to prevent damage, then replace the actuator assembly if it fails to operate as specified.

| Door / operation | First terminal | Second terminal |
|---|---|---|
| Driver LOCK | B1 positive | B2 ground |
| Driver UNLOCK | B1 ground | B2 positive |
| Passenger LOCK | No. 1 positive | No. 2 ground |
| Passenger UNLOCK | No. 1 ground | No. 2 positive |

The source image shows connector orientation and actuator locations.

---

### Printed page 22-234

<a id="p1726"></a>
Source: [PDF p.1726](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1726.png).

### Driver's door key-cylinder switch test

Remove the driver's door panel (p. 20-5) and disconnect the key-cylinder switch 2P connector. With switch OFF, No. 1–No. 2 should be open; at UNLOCK they should have continuity. Replace the switch if different.

### Transmitter test

If locks operate but the transmitter LED stays off, replace the transmitter. A door left open prevents transmitter locking; doors unlocked remotely relock after 30 seconds if none opens; an inserted ignition key prevents remote lock/unlock.

1. Press LOCK or UNLOCK five or six times to reset. If locks work, the transmitter is OK; otherwise continue.
2. Open the transmitter. Replace it if water damaged; otherwise continue.
3. Replace its battery, press LOCK or UNLOCK five or six times, and retest. If locks work, it is OK; otherwise continue.
4. Reprogram and retest. If locks work, it is OK; otherwise replace it.

---

### Printed page 22-235

<a id="p1727"></a>
Source: [PDF p.1727](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1727.png).

# Kef less Transmitter Programming/Deleting - Manual Method

## Storing transmitter codes: The codes of up to three transmitters can be programmed into the keyless receiver unit memory. (If a fourth code is stored, the code which was input first will be erased.)

**NOTE:** It is important to maintain the time limits between the steps. Make sure the doors, the hood and the trunk are closed.

1. Turn the ignition switch ON (II).
2. Within 1 to 4 sec, push the transmitter lock or unlock button with the transmitter aimed at the receiver unit behind the driver's side dash.
3. Within 1 to 4 sec, turn the ignition switch OFF.
4. Within 1 to 4 sec, turn the ignition switch ON (II).
5. Within 1 to 4 sec, push the transmitter lock or unlock button with the transmitter aimed at the receiver unit behind the driver's side dash.
6. Within 1 to 4 sec, turn the ignition switch OFF.
7. Within 4 sec, turn the ignition switch ON (II).
8. Within 1 to 4 sec, push the transmitter lock or unlock button with the transmitter aimed at the receiver unit behind the driver's side dash.
9. Within 1 to 4 sec, turn the ignition switch OFF.
10. Within 4 sec, turn the ignition switch ON (II).
11. Within 1 to 4 sec, push the transmitter lock or unlock button with the transmitter aimed at the receiver unit behind the driver's side dash.
12. Confirm you can hear the sound of the door lock actuators. Within 1 to 4 sec, push the transmitter lock or unlock button again. The keyless receiver unit is now in the program mode. You must push the transmitter lock or unlock button of the first transmitter again to program that remote.
13. Within 10 sec, aim the transmitters (up to two additional ones) whose codes you want to store at the receiver unit, and press the transmitter lock or unlock buttons.
Confirm that you can hear the sound of the door lock actuators after each transmitter code is stored.

14. Turn the ignition switch OFF and remove the key.
15. Confirm that the programmed transmitters operate correctly.

---

### Printed page 22-236

<a id="p1728"></a>
Source: [PDF p.1728](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1728.png).

### Convertible top — component location index

The source diagram locates the convertible top switch (test p. 22-241), control unit (input test p. 22-242), left top motor (test p. 22-246), right top motor (test p. 22-245), top motor emergency connector (removal step 8, p. 22-245), and both power window motors (tests p. 22-226). Use the image for exact locations.

---

### Printed page 22-237

<a id="p1729"></a>
Source: [PDF p.1729](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1729.png).

Printed page 22-237 contains no readable procedure or diagram; the scan has a central black artifact.

---

### Printed page 22-238

<a id="p1730"></a>
Source: [PDF p.1730](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1730.png).

### Convertible top — circuit diagram

The source diagram shows main under-hood fuses No. 41 (100 A), No. 42 (40 A), No. 51 (40 A), No. 54 (30 A), No. 52 (20 A), and No. 55 (20 A), plus under-dash fuses No. 5 (7.5 A), No. 8 (20 A), No. 18 (20 A), and No. 25 (7.5 A). The convertible top control unit drives the left and right motors through emergency connectors and receives inputs from the ignition switch, VSS driving circuit, parking brake switch, and associated indicator/control circuits. Ground is G402. Use the source diagram for exact terminal-to-terminal wiring and switch states.

---

### Printed page 22-239

<a id="p1731"></a>
Source: [PDF p.1731](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1731.png).

### Convertible top — circuit diagram (continued)

The source continuation shows the convertible top switch, passenger power window switch and motor, master switch connections, and the convertible top control unit. It also shows the hardtop-only top disable switch and rear window defogger change relay. Under-dash fuse No. 12 (15 A) supplies the top switch circuit; No. 23 (10 A) supplies its illumination. Grounds shown include G501, G601, and G901. Use the source diagram for exact wiring and hardtop-only connections.

---

### Printed page 22-240

<a id="p1732"></a>
Source: [PDF p.1732](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1732.png).

# Convertible Top

## Description
The convertible top can automatically be opened and closed by operating the convertible top switch.

The convertible top system consists of the convertible top switch, control unit and the motors located on the convertible top assembly. The top switch outputs open and close signals to the control unit. The control unit opens the driver's and the passenger's power windows then about 0.5 second after the windows start to open, the control unit operates the top motors to open or close the top.

## Basic Operation
### Lowering and Raising the Convertible Top
1. Turn the ignition switch to ON (II).
2. At the latch on each side, push in the tab, and pull the locking lever down.
3. Push the top forward while you release the latches from the windshield header (striker) by pushing the locking levers forward.
4. With the latches released, pull back on the locking levers and push them up until they latch.
5. Pull back and hold the ROOF switch. The windows lower and the roof folds back. Release the ROOF switch when the roof is retracted completely into the rear shelf.
6. Push the ROOF switch forward and hold it.
7. The windows, if raised, lower automatically, then the convertible top goes up. Release the ROOF switch when the top reaches the windshield header.
8. Push in the tab on each locking lever, and pull the locking lever down.
9. Push the locking lever forward, and set the latch into the windshield header (striker) while pushing the convertible top forward.
10. Pull back on the locking lever, and push it up until it latches. Make sure both levers are securely latched.

---

### Printed page 22-241

<a id="p1733"></a>
Source: [PDF p.1733](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1733.png).

### Convertible top switch test

1. Remove the center console (p. 20-80).
2. Disconnect the switch 6P connector (A).
3. Check continuity: in OPEN, terminals 1–3 and 5–6; in CLOSE, terminals 2–3 and 5–6. See the source image for connector orientation and illumination bulb circuit.
4. If continuity differs, replace the illumination bulb (B) or switch.

---

### Printed page 22-242

<a id="p1734"></a>
Source: [PDF p.1734](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1734.png).

# Convertible Top
## Convertible Top Control Unit Input Test

1. Remove the passenger's dashboard lower cover (see page 20-86).
2. Disconnect the 14P connector (A) and 10P connector (B) from the convertible top control unit (C).
   - Wire side of female terminals *: With Hardtop
3. Inspect the connector and socket terminals to be sure they are all making good contact.
   - If the terminals are bent, loose or corroded, repair them as necessary, and recheck the system.
   - If the terminals look OK, go to step 4.

---

### Printed page 22-243

<a id="p1735"></a>
Source: [PDF p.1735](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1735.png).

### Convertible top control unit input test — step 4

Reconnect the control unit connectors. Correct any failed test and recheck; if all pass, go to step 5.

| Cavity / wire | Condition and desired result | Possible cause if failed |
|---|---|---|
| B1 YEL | Ignition ON (II); battery voltage to ground. | No. 5 (7.5 A) under-dash fuse blown; open wire. |
| A14 BLU/BLK | All conditions; battery voltage to ground. | No. 18 (20 A) under-dash fuse blown; open wire. |
| A13 WHT/RED | All conditions; battery voltage to ground. | No. 25 (7.5 A) under-dash fuse blown; open wire. |
| A7, A8, A11 BLK | All conditions; less than 0.5 V to ground. | Poor G402 ground; open wire. |
| B10 BLK | All conditions; less than 0.5 V to ground. | Poor G501 ground; open wire. |
| A6 GRY/RED | All conditions; battery voltage to ground. | No. 52 (20 A) main under-hood fuse blown; open wire. |
| A3 GRY | All conditions; battery voltage to ground. | No. 55 (20 A) main under-hood fuse blown; open wire. |
| A12 GRN/WHT | Parking brake pulled; less than 1 V to ground. | Parking brake switch faulty; open wire. |
| B2 BLU/ORN | Ignition ON (II), parking brake pulled, operate top switch; B2-to-ground voltage should repeatedly vary 0–8 V or more. | Power window master switch faulty; open wire. |
| B6 WHT/BLK | Ignition ON (II), rear raised, rotate one wheel slowly; voltage between B6 and A8 should repeatedly vary 0–5 V or more. | Gauge assembly, VSS, or VSS driving circuit faulty; open wire. |

---

### Printed page 22-244

<a id="p1736"></a>
Source: [PDF p.1736](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1736.png).

### Convertible top control unit input test — step 5

Disconnect control unit connectors. Correct any failed test and recheck; if all pass, replace the faulty control unit. Connector views are from the wire side of female terminals.

| Cavity / wire | Test and desired result | If failed |
|---|---|---|
| A5 RED/WHT | Disconnect left motor 2P; connect A5 to A6 power and A4 to A11 ground; support left top side. Right motor should OPEN. | Right motor faulty; open wire. |
| A4 LT GRN/RED | Disconnect left motor 2P; connect A4 to A6 power and A5 to A11 ground; support left side. Right motor should CLOSE. | Right motor faulty; open wire. |
| A2 RED/BLU | Disconnect right motor 2P; connect A2 to A3 power and A1 to A7 ground; support right side. Left motor should OPEN. | Left motor faulty; open wire. |
| A1 RED | Disconnect right motor 2P; connect A1 to A3 power and A2 to A7 ground; support right side. Left motor should CLOSE. | Left motor faulty; open wire. |
| B5 LT GRN (hardtop only) | Top disable switch closed: continuity to ground. | Disable switch faulty; poor G601/G901 ground; open wire. |
| B3 RED/BLU | Connect B3 to A14 and B4 to B10. Passenger window should move UP. | Passenger motor faulty; open wire. |
| B4 RED | Connect B4 to A14 and B3 to B10. Passenger window should move DOWN. | Passenger motor faulty; open wire. |
| A9 RED/BLK | Ignition ON (II), top switch OPEN: battery voltage to ground. | No. 12 (15 A) under-dash fuse blown; top switch faulty; open wire. |
| A10 RED/YEL | Ignition ON (II), top switch CLOSE: battery voltage to ground. | Same A9 causes. |
| B7 BLU/WHT | Ignition ON (II), master main switch ON, passenger switch DOWN: battery voltage to ground. | No. 8 (20 A) under-dash fuse blown; master or passenger switch faulty; open wire. |
| B8 BLU/RED | Same, passenger switch UP: battery voltage to ground. | Same B7 causes. |
| B9 RED/BLU | Ignition ON (II), master main switch ON: battery voltage to ground. | Same B7 causes. |

---

### Printed page 22-245

<a id="p1737"></a>
Source: [PDF p.1737](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1737.png).

### Right convertible top motor test

1. Remove the right corner gusset (p. 20-39).
2. Disconnect the motor 2P connector (A).
3. Support the left side of the top by hand.
4. Apply battery power and ground to the terminal side of the male connector: **OPEN:** No. 1 positive, No. 2 ground. **CLOSE:** No. 1 ground, No. 2 positive.
5. Replace the motor if it does not operate as specified.
6. If motor failure prevents top operation, close the top manually: remove the passenger's dashboard lower cover (p. 20-86), disconnect the top motor emergency 2P connector, then close the top by hand (steps 7–9).

---

### Printed page 22-246

<a id="p1738"></a>
Source: [PDF p.1738](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1738.png).

### Left convertible top motor test

1. Remove the left corner gusset (p. 20-39).
2. Disconnect the left motor 2P connector (A).
3. Support the right side of the top by hand.
4. Apply battery power and ground to the terminal side of the male connector: **OPEN:** No. 1 ground, No. 2 positive. **CLOSE:** No. 1 positive, No. 2 ground.
5. Replace the motor if it does not operate as specified.
6. If motor failure prevents top operation, continue to close it manually.
7. Remove the passenger's dashboard lower cover (p. 20-86).
8. Disconnect the top motor emergency 2P connector (A).
9. Close the top manually.

---

### Printed page 22-247

<a id="p1739"></a>
Source: [PDF p.1739](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1739.png).

### Removable hardtop — component location index

The source image locates the convertible top control unit in the hardtop area (input test p. 22-242) and the convertible top disable switch near the left rear side trim (test p. 22-248). Use the image for exact locations.

---

### Printed page 22-248

<a id="p1740"></a>
Source: [PDF p.1740](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1740.png).

# Removable Hardtop
## Convertible Top Disable Switch Test

**NOTE:** For the convertible top disable switch circuit diagram, refer to the Convertible Top Circuit Diagram (see page 22-238) and the Rear Window Defogger Circuit Diagram (see page 22-251).

1. Remove the left rear side trim (see page 20-72).
2. Disconnect the 2P connector (A) from the convertible top disable switch (B).
3. Push the convertible top disable switch.
4. Check for continuity between the No. 1 and No. 2 terminals.
   - There should be continuity.
5. If the continuity is not as specified, replace the switch.

---

### Printed page 22-249

<a id="p1741"></a>
Source: [PDF p.1741](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1741.png).

### Rear window defogger — component location index

The source diagram identifies the defogger switch in the center console for 2000–2001 models and in the instrument panel for 2002–2005 (tests p. 22-254), and again in the center console for 2006–2008 (test p. 22-255). It also locates the defogger relay for 2000–2001 in the under-dash fuse/relay box and the 2002–2008 relay (test p. 22-48). Use the image for exact locations.

---

### Printed page 22-250

<a id="p1742"></a>
Source: [PDF p.1742](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1742.png).

### Rear window defogger — component location index (continued)

The source image locates the rear-window grid (function test p. 22-256; wire repair p. 22-257), the hardtop-only convertible top disable switch (test p. 22-248), and the 2002–2008 noise condenser, diode, and rear window defogger change relay (test p. 22-48). Use the image for exact locations.

---

### Printed page 22-251

<a id="p1743"></a>
Source: [PDF p.1743](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1743.png).

### Rear window defogger circuit, 2000–2001 models

The source diagram shows battery supply through main under-hood fuses No. 41 (100 A) and No. 42 (40 A), auxiliary under-hood fuse No. 34 (20 A), and under-dash fuse No. 19 (7.5 A). It includes the ignition switch, IG2 cut relay, defogger relay and switch, rear-window grid, indicator and illumination lamps, and grounds G902, G601/G901, and G401. Use the source image for exact wiring.

---

### Printed page 22-252

<a id="p1744"></a>
Source: [PDF p.1744](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1744.png).

### Rear window defogger circuit, 2002–2005 models

The source diagram shows main under-hood fuses No. 41 and 42, auxiliary under-hood No. 34, under-dash No. 6 and 19, and the No. 23 illumination feed. It includes the ignition switch, IG2 cut relay, defogger switch and relay, noise condenser, and hardtop-only defogger change relay, diode, top disable switch and rear-window grid. Use the source image for wiring and ground locations.

---

### Printed page 22-253

<a id="p1745"></a>
Source: [PDF p.1745](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1745.png).

### Rear window defogger circuit, 2006–2008 models

The source diagram shows main under-hood fuses No. 41 and 42, auxiliary under-hood No. 34, under-dash No. 6 and 19, and No. 23 illumination. It includes the ignition switch, IG2 cut relay, defogger switch and relay, noise condenser, and the hardtop-only change relay, diode, top disable switch and rear-window grid. Use the source image for exact terminal connections.

---

### Printed page 22-254

<a id="p1746"></a>
Source: [PDF p.1746](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1746.png).

### Rear window defogger switch test

**2000–2001:** Remove center console (p. 20-80), remove switch (A), disconnect its 5P connector (B), and check continuity in OFF and ON positions. The source table shows an illumination-bulb path between terminals 1–2 in both positions; in OFF, a bulb path between 3–5; in ON, the 3–4–5 switching path. Replace bulbs (C) or switch if the source table is not matched.

**2002–2005:** Remove instrument panel (p. 20-84), remove switch (A), disconnect its 6P connector (B), and check both positions. The source table shows bulb paths 2–3 and 4–5 in both positions, plus switching continuity 1–6 in ON. Replace bulbs (C) or switch if different. See the image for connector orientation and exact lamp symbols.

---

### Printed page 22-255

<a id="p1747"></a>
Source: [PDF p.1747](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1747.png).

### Rear window defogger switch test, 2006–2008 models

1. Remove the center console (p. 20-80).
2. Remove the defogger switch (A) and disconnect its 6P connector (B).
3. Compare continuity to the source table. It shows a bulb path between terminals 1–4 and another between 3–5 in both positions. The ON position adds switching continuity from 4 to 6. The source image shows connector orientation and lamp symbols.
4. Replace bulbs (C) or the switch if continuity differs.

---

### Printed page 22-256

<a id="p1748"></a>
Source: [PDF p.1748](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1748.png).

# Rear Window Defogger
## Function Test

**NOTE:** Be careful not to scratch or damage the defogger wires with the tester probe.

1. Measure the voltage between the positive terminal (A) and body ground with the ignition switch and defogger switch ON.
   - There should be battery voltage.

   • If there is no voltage, check for:
     - Faulty defogger relay.
     - Faulty defogger change relay ('02-08 models).
     - Faulty diode ('02-08 models).
     - An open in the wire.

   • If there is battery voltage, go to step 2.

2. Check for continuity between the negative terminal (B) and body ground.
   - If there is no continuity, check for an open in the defogger ground wire.

3. Touch the voltmeter positive probe to the halfway point of each defogger wire, and the negative probe to the negative terminal.
   - There should be approximately 6 V with the ignition switch and the defogger switch ON.

   • If the voltage is as specified, the defogger wire is OK.
   • If the voltage is not as specified, repair the defogger wire.
     - If it is more than 6 V, there is a break in the negative half of the wire.
     - If it is less than 6 V, there is a break in the positive half of the wire.

---

### Printed page 22-257

<a id="p1749"></a>
Source: [PDF p.1749](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1749.png).

# Defogger Wire Repair

**NOTE:** To make an effective repair, the broken section must be no longer than 1 inch (25 mm).

1. Lightly rub the area around the broken section (**A**) with fine steel wool, then clean it with isopropyl alcohol.
2. Carefully mask above and below the broken portion of the defogger wire (**B**) with cellophane tape (**C**).
3. Thoroughly mix the silver conductive paint using a small brush, apply a heavy coat of the paint extending about 1/8" on both sides of the break. Allow 25 minutes to dry.
4. Check for continuity in the repaired wire.
5. Apply a second coat of paint in the same way. Let it dry 3 hours before removing the tape.

---

### Printed page 22-258

<a id="p1750"></a>
Source: [PDF p.1750](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1750.png).

### Audio system — component location index

The source image locates the ACC cut relay (test p. 22-48), audio unit (removal/installation p. 22-288; connector I/O p. 22-260), audio remote switch (test/replacement p. 22-287), door speakers (p. 22-288), 2002–2008 left/right tweeters and 2006–2008 rear speakers (p. 22-289), and AM/FM antenna and lead (antenna replacement p. 22-290). Use the image for exact locations.

---

### Printed page 22-259

<a id="p1751"></a>
Source: [PDF p.1751](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1751.png).

# Symptom Troubleshooting Index

## Poor AM or FM radio reception or interference
**Symptom Diagnostic procedure**: Also check for Antenna lead short or open in the wire.
**Reference**: Symptom Troubleshooting (see page 22-267)

## Power switch will not turn ON (No information display and no sound)
**Reference**: Symptom Troubleshooting (see page 22-270)

## Power will not turn OFF
**Reference**: Symptom Troubleshooting (see page 22-271)

## No sound is heard from speaker(s) (display is normal)
**Reference**: Symptom Troubleshooting (see page 22-271)

## Audio system sound is weak or distorted (display is normal)
**Reference**: Symptom Troubleshooting (see page 22-273)

## Audio unit button illumination does not work
**Reference**: Symptom Troubleshooting (see page 22-274)

## Radio preset memory is lost
**Reference**: Symptom Troubleshooting (see page 22-275)

Also check battery condition and battery cable condition.

## Audio disc does not eject
**Reference**: Symptom Troubleshooting (see page 22-276)

## Volume does not change
**Reference**: Symptom Troubleshooting (see page 22-276)

## Radio tuner does not change stations
**Reference**: Symptom Troubleshooting (see page 22-277)

## Audio disc does not load
**Reference**: Symptom Troubleshooting (see page 22-277)

## Audio disc does not play
**Reference**: Symptom Troubleshooting (see page 22-278)

## Audio disc skips
**Reference**: Symptom Troubleshooting (see page 22-278)

Also check over-inflated tires and whether the disc is smudged, dirty, or scratched.

## Audio remote switch does not work properly
**Reference**: Symptom Troubleshooting (see page 22-279)

---
**Page Reference**: 22-259

---

### Printed page 22-260

<a id="p1752"></a>
Source: [PDF p.1752](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1752.png).

### Audio unit connector inputs and outputs

Match replacement connector wires to the 20P connector cavities shown in the source image.

| Cavity | Wire color | Connection |
|---|---|---|
| 1 | YEL/GRN | AM/FM antenna amplifier |
| 2 | WHT/RED | ACC, main stereo power |
| 3 | GRN/RED | Audio remote switch |
| 5*2 | RED/YEL | Rear right speaker (+) |
| 6*2 | BLU/YEL | Rear left speaker (+) |
| 7 | GRN/BLK | Passenger door speaker (+), right tweeter (+)*1 |
| 8 | GRN/YEL | Driver door speaker (+), left tweeter (+)*1 |
| 9 | RED/BLK | Lights-on signal |
| 10 | WHT/BLU | Constant power |
| 14 | YEL/BLU | Audio remote switch MUTE |
| 15*2 | BRN/WHT | Rear right speaker (−) |
| 16*2 | GRY/RED | Rear left speaker (−) |
| 17 | LT GRN | Passenger door speaker (−), right tweeter (−)*1 |
| 18 | GRY/RED | Driver door speaker (−), left tweeter (−)*1 |
| 19*1 | RED | Dash lights brightness controller |
| 20 | BLK | Ground G502 |

*1: 2002–2008 models. *2: 2006–2008 models. See the source image for connector orientation.

---

### Printed page 22-261

<a id="p1753"></a>
Source: [PDF p.1753](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1753.png).

# Audio Glossary

| Item | Definition |
| :--- | :--- |
| **AM** (Amplitude Modulation) | The type of transmission used in the standard radio broadcast band from 530 to 1705 kHz. |
| **Amplifier** | A device that increases the level of a signal by increasing the current or voltage. |
| **Antenna** | A device used to send or receive electromagnetic waves through the air. |
| **ATA (PC Card)** | A type of card that has been tested for use in playing WMA, and MP3 music files in the PC card slot. Sizes of up to 1 GB have been tested. |
| **Audio Remote switch** | The switches on the steering wheel that control the audio system. |
| **Auxiliary jack** | Allows the customer to use a portable audio device to input music recordings. |
| **Balance** | A control that changes the relative volume of the left and right channels. |
| **Band** | A range of frequencies between two definite limits. Bands are assigned by the Federal Communications Commission for specific uses. |
| **Bass** | An adjustment for the low frequency sounds of around 160 Hz and below. |
| **Byte** | A unit of storage for computer files and memory. A CD holds approximately 700 million bytes. |
| **Cassette** | Audio or video magnetic tape container having two reels. Customers can insert it for recording or play back. |
| **Compact Flash** | A standard for small-size (3 x 4 cm), memory cards used in mobile computers, PDAs, digital cameras. Compact flash memory cards are available in size of 32 MB up to 4 GB or more and can be played in the audio PC slot. Sizes above 1 GB has not been tested. |
| **CD** (Compact Disc) | A 4.5-inch plastic disc containing digital audio recording that is played optically on a laser equipped player. Never use discs with a paper label. In a hot car, labels can curl up and jam the unit. |
| **CD Changer** | CD player that can store and play more than one CD. Two types are available. Some units accept CDs fed into the changer one at a time, and others accept a magazine (with CD's stacked in a container). |
| **CD player** | A component designed to play compact disc CD recording using a laser optical pickup. The signal from a CD player usually requires amplification, which case the Auxiliary jacks can be used. |
| **Distortion** | Inexact reproduction of an audio signal caused by playing music at levels the audio system cannot handle. |
| **Dolby (noise reduction)** | A processing system developed by Dolby Laboratories that reduces the background noise on recording media. The result is clearer playback from the audio system. |
| **DVD** (Digital Versatile Disc) | A 4.5-inch CD-like format used for storing movies with digital audio and video features. The DVD-A format is a DVD format designed for DVD audio systems. Some vehicles can play DVD or DVD-A formats. |
| **Equalizer** | A device that changes the relative volume of individual frequency bands to suit personal tastes of the listener. |
| **Fader** | The control that adjusts the relative volume levels of front and rear speakers in a four-speaker system. |
| **Format** | To prepare a PC card to receive files, this function is performed on a PC. Always choose either FAT or FAT32 as the NTFS format is not accepted by the system. Pick the default sectors for the format method selected. |
| **FM** (Frequency Modulation) | The modulation used for radio and television sound transmission in most of the world. Less prone to interference than AM. The FM broad cast band covers roughly 87 to 108 MHz. |
| **GB** (Gigabyte) | A unit of memory or disk storage equal to billion bytes (1000 million bytes). |

*(cont'd)*

22-261

---

### Printed page 22-262

<a id="p1754"></a>
Source: [PDF p.1754](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1754.png).

# Audio System
## System Description (cont'd)
### Audio Glossary

| Item | Definition |
| :--- | :--- |
| **HDD** | Abbreviation for hard disc drive. They are sensitive to heat and it is not recommended that they be used in the PC card slot for playing audio files. |
| **Hertz (HZ)** | The unit of frequency equal to one cycle per second (cps). One kilohertz (kHz) equals 1,000 cps; one megahertz (MHz) equals 1 million cps. |
| **Integrated Amplifier** | A component that combines a preamp and a power amp into a single unit. A receiver combines an integrated amp and a tuner into a single unit. |
| **Jewel Case** | The hard plastic case that contains a compact disc or DVD. Always use a jewel case to prevent scratches on the underside of a CD or DVD. |
| **LCD (Liquid Crystal Display)** | A type of digital display that changes reflectance or transmittance when an electrical field is applied to it. |
| **Memory** | Circuitry or devices that hold information in electrical or magnetic form, such as the AM/FM radio presets. |
| **MB (Megabyte)** | One million bytes. Written as 1 MB. Megabytes are used as a measure of digital storage space. For example, a CD can hold 650 MB. |
| **Mic** | An abbreviation for microphone. For vehicles with navigation, the microphone accepts navigation voice commands to control audio and navigation functions. |
| **MP3 music files** | MP3 is an audio coding format. MP3 is popular audio compression format on the Internet and computers. CDs, and PC card with these files can be played on some vehicle's audio system. |
| **Mute** | When the navigation gives guidance, the front speakers are muted (no music). When you use the voice control system, all of the speakers are muted. |
| **Noise** | Unwanted random sounds like buzzing, hiss, pops, static, whine, etc. |
| **PC Card** | The slot used for playing MP3 and WMA music files. The PC card is usually a combination of a small flash card in a PCMCIA adaptor that slides into the slot. The ATA, SD, and compact flash types of cards have been tested up to 1 GB. |
| **PCMCIA** | A computer standard for the slot that the PC card slides into. Another term for the PC card slot. |
| **Processor** | The part of an audio device that performs task/calculations. In the audio unit, the processor handles muting to allow the nav to speak voice commands, and the decoding/playback of the sound files etc. |
| **Radio** | A head unit that combines a tuner, a preamplifier, and often a power-amplifier. |
| **SCF (Cold Start Fix) screens** | These screens are displayed if the system requires a GPS initialization. The vehicle should be moved outside into an open area away from buildings/power lines. |
| **Stereo** | A recording of at least two channels where you can hear sound or music from the left or right side. |
| **SD (Secure Digital) card** | This compact type of memory card allows for fast data transfer and has built-in security functions. SD cards have a small write-protection switch on the side. |
| **Shield** | A metallic foil or braided wire layer surrounding conductors which are designed to prevent electrostatic or electromagnetic interference (noise) from external sources such as buzzing, or popping sounds heard on the speakers. |
| **Speaker (Loudspeaker)** | A device that converts electrical energy into acoustical energy (sound). |
| **Subwoofer** | A loudspeaker made to reproduce the lowest audio frequencies, approx 25 Hz to 125 Hz. |

*Page Reference: 22-262*

---

### Printed page 22-263

<a id="p1755"></a>
Source: [PDF p.1755](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1755.png).

# Audio Glossary

| Item | Definition |
| :--- | :--- |
| Track | A sound recording on a CD, tape, or PC card. |
| Treble | An adjustment to control the volume of the high frequency sounds. |
| Tuner | A component (or part of a component) that receives radio signals and selects one broadcast from many. |
| Tweeter | A speaker designed to reproduce the higher frequencies (treble) only. |
| Voice Coil | A coil of wire wrapped around a tube and attached to the speaker cone or diaphragm. When an audio signal is applied, the coil becomes an electromagnet and interacts with the permanent magnet causing the cone or diaphragm to vibrate. We interpret this vibration as sound. |
| Volume Control | Allows you to control the loudness of the music. |
| WMA | Windows Media Audio music file. This is an accepted format for music files to be played on either a CD or a PC card. |
| Woofer | A speaker that is designed to reproduce bass frequencies only. |
| XM Radio | Satellite based radio transmission, which also uses a ground based repeater network to ensure seamless reception. The channels originate from XM's broadcast center, in Washington, DC, and uplink to two satellites. These satellites transmit the signal across the entire continental United States. |
| XM Receiver | The external component that receives and processes the XM signals from the XM satellites, and terrestrial (land) stations. The audio unit communicates to the XM receiver over the GA-Net bus. |

*Page Reference: 22-263*

---

### Printed page 22-264

<a id="p1756"></a>
Source: [PDF p.1756](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1756.png).

### Audio system circuit diagram

The source diagram shows battery power through main under-hood fuses No. 41 (100 A), No. 42 (40 A), and No. 54 (30 A), and under-dash fuses No. 9 (10 A), No. 22 (15 A), and No. 23 (10 A, illumination). It traces the ignition switch and ACC cut relay to the audio unit and AM/FM antenna amplifier, plus the audio remote switch, dash lights brightness controller, and grounds G502 and G501. Use the source image for exact wire colors, cavity positions, and circuit connections.

---

### Printed page 22-265

<a id="p1757"></a>
Source: [PDF p.1757](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1757.png).

### Audio system circuit diagram — speaker wiring

The source diagram shows the 2006–2008 rear speaker circuits: left rear through audio unit cavities 6 (+) and 16 (−), and right rear through cavities 5 (+) and 15 (−). Optional 2004–2005 headrest speakers use the corresponding rear speaker output positions. Door speakers and the 2002–2008 tweeters are shown on the front speaker paths: driver side cavities 8 (+) and 18 (−), passenger side cavities 7 (+) and 17 (−). Use the diagram for exact connector and wire routing.

---

### Printed page 22-266

<a id="p1758"></a>
Source: [PDF p.1758](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1758.png).

### Audio unit serial number display mode

**Note:** This procedure is available after battery power to the audio unit has been interrupted and the display shows `CODE`.

1. Turn the ignition switch to ON (II).
2. With the audio unit off, hold preset buttons No. 1 (A) and No. 6 (B). While holding them, press the `VOL PUSH PWR` knob (C) to turn the unit on.
3. The display first shows `U` and four digits (example `U1234`), then `L` and four digits (example `L5678`). These are respectively the first and last four digits of the serial number.
4. Use all eight digits with the Interactive Network (iN) to retrieve the five-digit anti-theft code.
5. Display mode ends when the audio unit is turned off or the ignition switch is turned to LOCK (0).

---

### Printed page 22-267

<a id="p1759"></a>
Source: [PDF p.1759](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1759.png).

# Symptom Troubleshooting
## Poor AM or FM radio reception or interference

**NOTE:**
*   Check the vehicle battery condition first.
*   Check for aftermarket accessories.
*   Check the connectors for poor connections or loose terminals.
*   Check the radio reception in an open area. Poor reception/interference can be caused by the following:
    *   The radio station is far away.
    *   Atmospheric conditions are unfavorable.
    *   Tall buildings, mountains, or high-voltage power lines are nearby.

1.  Turn the ignition switch to ON (II).
2.  Do the seek stop test (see page 22-285).

Is the number of stations the same or within 10% of the known-good vehicle?
*   **YES** — Multipath interference or weak station. Operation is normal.
*   **NO** — Go to step 3.

3.  Check if the radio reception/interference is the same in several locations.

Is the reception/interference the same?
*   **YES** — Go to step 4.
*   **NO** — Multipath interference or weak station. Operation is normal.

4.  Start the engine.
5.  Check the reception/interference while the engine is running.

Is there noise (static or whine) only with the engine running?
*   **YES** — Check all of the AM/FM antenna connections and the AM/FM antenna and radio grounds. If OK, check the charging system and the ignition system.
*   **NO** — Go to step 6.

6.  Turn the ignition switch to LOCK (0).


7.  Check the antenna mast for cracks, or other damage. Make sure that the AM/FM antenna mast isn't loose.

**NOTE:** Do not use any tools to tighten the antenna mast.

Is there any damage?
*   **YES** — Replace the AM/FM antenna mast (see page 22-290).
*   **NO** — Go to step 8.

8.  Turn the ignition switch to ON (II).
9.  Turn on the audio unit.
10. Measure the voltage between AM/FM antenna 2P connector terminal No. 2 and body ground.

Is there battery voltage?
*   **YES** — Go to step 11.
*   **NO** — Go to step 18.

11. Turn the ignition switch to LOCK (0).

---
**Page Reference:** 22-267

---

### Printed page 22-268

<a id="p1760"></a>
Source: [PDF p.1760](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1760.png).

# Audio System

## Symptom Troubleshooting (cont'd)

12. Remove the audio unit, and disconnect the AM/FM antenna lead (see page 22-290).

13. Disconnect the AM/FM antenna lead from the AM/FM antenna.

14. Check for continuity between the AM/FM antenna lead center pin at the audio unit side and body ground.

Is there continuity?

- **YES**—Replace the AM/FM antenna lead.
- **NO**—Go to step 15.

15. Check for continuity between the AM/FM antenna lead center pin and the surface of the AM/FM antenna lead.

Is there continuity?

- **YES**—Replace the AM/FM antenna lead.
- **NO**—Go to step 16.

22-268

---

### Printed page 22-269

<a id="p1761"></a>
Source: [PDF p.1761](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1761.png).

### Poor AM/FM radio reception — continued

16. Check continuity between the AM/FM antenna lead center pin at the audio unit end and the center pin at the antenna end. If there is continuity, go to step 17; otherwise replace the lead.
17. Substitute a known-good antenna lead and check reception. If reception returns to normal, replace the original lead. Otherwise substitute a known-good audio unit; if reception remains poor, replace the antenna.
18. Turn the ignition to LOCK (0).
19. Remove the audio unit and disconnect its 20P connector. Eject the disc before removal to protect the CD load mechanism.
20. Check continuity between audio unit 20P terminal No. 1 and AM/FM antenna 2P terminal No. 2 (YEL/GRN wire). If continuity exists, substitute a known-good audio unit and retest. Otherwise repair the open wire between the audio unit and antenna. See source diagram for connector orientation.

---

### Printed page 22-270

<a id="p1762"></a>
Source: [PDF p.1762](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1762.png).

# Audio System
## Symptom Troubleshooting (cont'd)
### Power switch will not turn ON (No information display and no sound)

**NOTE:**
*   Check the vehicle battery condition first.
*   Check the connectors for poor connections or loose terminals.

1.  Turn the ignition switch to **ON (II)**.
2.  Push the power switch **ON** to see if audio unit turns **ON**.

**Does the power turn ON?**
*   **YES**—Operation is normal. If the display turns **ON**, but no sound is heard or if the display does not turn **ON**, but the sound is **OK**. *Go to audio system sound is weak or distorted (see page 22-273), or no sound is heard from speakers (see page 22-271).*
*   **NO**—Go to step 3.

3.  Turn the ignition switch to **LOCK (0)**.
4.  Check the **No. 22 (15 A)** fuse and **No. 9 (10 A)** fuse in the under-dash fuse/relay box.

**Are the fuses OK?**
*   **YES**—Go to step 5.
*   **NO**—Replace the fuse, and recheck.

5.  Remove the audio unit (see page 22-288). Check that the audio unit connector is properly connected.

**Is it connected properly?**
*   **YES**—Go to step 6.
*   **NO**—Reconnect the connector, and recheck the function.

6.  Disconnect the audio unit **20P** connector.
    > **NOTE:** Eject the disc before removing the audio unit to prevent damaging the CD player's load mechanism.

7.  Turn the ignition switch to **ON (II)**.
8.  Measure the voltage between the **No. 2** and **No. 10** terminals of the audio unit **20P** connector and body ground.

Connector terminals No. 2 ACC (WHT/RED) and No. 10 +B (WHT/BLU) are measured to body ground. See source image for orientation.

**Is there battery voltage?**
*   **YES**—Go to step 9.
*   **NO**—Repair open in the wire(s) between the **No. 22 (15 A)** fuse and **No. 9 (10 A)** in the under-dash fuse/relay box and the audio unit.

9.  Turn the ignition switch to **LOCK (0)**.
10. Reconnect the audio unit **20P** connector.
11. Turn the ignition switch to **ON (II)**.
12. Measure the voltage between audio unit **20P** connector **No. 20** terminal and body ground while pressing and releasing the audio unit power switch several times.

Connector terminal No. 20 is GND (BLK). See source image for orientation.

**Is there less than 0.1 V?**
*   **YES**—Replace the audio unit (see page 22-288).
*   **NO**—Repair open in the wire between the audio unit connector **A (20P)** **No. 20** terminal and body ground (**G502**).

---
**Page Reference:** 22-270

---

### Printed page 22-271

<a id="p1763"></a>
Source: [PDF p.1763](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1763.png).

### Power will not turn OFF

Check for aftermarket accessories plugged into vehicle accessory sockets. With ignition ON (II), press the audio power switch OFF or turn ignition to LOCK (0). If the unit turns off, operation is normal. Otherwise turn ignition to LOCK (0), remove the audio unit and disconnect its 20P connector. Eject the disc before removal. Measure voltage from connector terminal No. 2 (ACC, WHT/RED) to body ground. Battery voltage indicates a short to power on the WHT/RED wire; without battery voltage, replace the audio unit (p. 22-288).

### No sound from speakers (display normal)

Check battery and connectors; center fader and balance; complete power-switch troubleshooting (p. 22-270) first. Turn ignition ON (II), turn on the audio unit, and verify volume is above MIN. Raise it if needed. Check and cancel MUTE if set. Determine whether one speaker alone is silent: if yes, continue at step 7 on p. 22-272; otherwise turn ignition to LOCK (0) and continue at step 6.

---

### Printed page 22-272

<a id="p1764"></a>
Source: [PDF p.1764](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1764.png).

# S2000 Body Electrical
## Audio System Troubleshooting (continued)

### Step 6
Remove the audio unit (see page 22-288). Check that the audio unit connector is properly connected.

> **NOTE:** Eject the disc before removing the audio unit to prevent damaging the CD player's load mechanism.

**Is it connected properly?**
*   **YES** — Go to step 11.
*   **NO** — Reconnect the connector, and recheck the function.

### Step 7
Turn the ignition switch to LOCK (0).

### Step 8
Check the speaker with no sound for any damage.

**Is there any damage?**
*   **YES** — Substitute the speaker and recheck.
*   **NO** — Go to step 9.

### Step 9
Remove the speaker(s) with no sound: Door speaker (see page 22-288), Rear speaker (see page 22-289), Tweeter (see page 22-289), and disconnect its connector.

### Step 10
Check the speaker connector for a loose or poor connection.
Reconnect the speaker connector and recheck the symptom; does it still fail?
*   **YES** — Go to step 11.
*   **NO** — Operation is normal.

### Step 11
Disconnect the speaker connector.

### Step 12
Remove the audio unit (see page 22-288), and disconnect the audio unit 20P connector.

> **NOTE:** Eject the disc before removing the audio unit to prevent damaging the CD player's load mechanism.

### Step 13
Check for continuity between both pairs of speaker wires (+) and (−) at audio unit 20P connector.

#### Speaker terminal and wire colors

| Speaker | Positive | Negative |
|---|---|---|
| Driver door, left tweeter | A8 GRN/YEL | A18 GRN/RED |
| Passenger door, right tweeter | A7 GRN/BLK | A17 LT GRN |
| Left rear | A6 BLU/YEL | A16 GRY/RED |
| Right rear | A5 YEL | A15 BRN/WHT |

The printed A18 and A5 colors differ from the connector table on p. 22-260; verify on the vehicle before wiring repair. See the source image for connector orientation.

**Is there continuity?**
*   **YES** — Repair short in the wire(s) between the audio unit and speaker(s).
*   **NO** — Go to step 14.

---

---

### Printed page 22-273

<a id="p1765"></a>
Source: [PDF p.1765](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1765.png).

### No sound from speakers — continued

14. Bridge the silent speaker connector's (+) and (−) terminals with a jumper wire.
15. Check continuity between that speaker's paired wires at the audio unit 20P connector, using the table on p. 22-272. If continuity exists, continue at step 16; otherwise repair the open wire between audio unit and speaker. The source table's A18 and A5 wire colors differ from the connector input/output table on p. 22-260; confirm at the vehicle.
16. Substitute a known-good speaker. If the symptom resolves, replace the faulty speaker. Otherwise substitute a known-good audio unit and, if that resolves the symptom, replace the original unit (p. 22-288).

### Weak or distorted audio (display normal)

Check battery condition and connectors, then test AM, FM, and CD sound. If all modes sound normal, check for intermittent loose connections at the audio unit and speakers. If sound is poor only on AM or FM, follow reception troubleshooting (p. 22-267); if poor in all modes, follow sound quality diagnosis (p. 22-281).

---

### Printed page 22-274

<a id="p1766"></a>
Source: [PDF p.1766](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1766.png).

# Audio System
## Symptom Troubleshooting (cont'd)
### Audio unit button illumination does not work

**NOTE:**
*   Check the vehicle battery condition first.
*   Check the connectors for poor connections or loose terminals.

1.  Turn the ignition switch to ON (II).
2.  Turn the headlight switch to the parking light position.
3.  Check the illumination of the audio unit buttons.
    *   **Are the buttons illuminated?**
        *   **YES** — Intermittent problem: the audio unit is OK at this time. Check for loose or poor connections at audio unit 20P connector.
        *   **NO** — Go to step 4.

4.  Check the illumination of several other buttons not related to the audio system.
    *   **Are the buttons illuminated?**
        *   **YES** — Go to step 5.
        *   **NO** — Troubleshoot the interior lights.

5.  Turn the ignition switch to LOCK (0).
6.  Disconnect audio unit 20P connector.
    *   **NOTE:** Eject the disc before removing the audio unit to prevent damaging the CD player's load mechanism.

7.  '00-03 models: Disconnect gauge assembly connector B (12P).
    '04-08 models: Disconnect gauge assembly connector A (22P).

8.  '00-03 models: Check for continuity between audio unit 20P connector No. 19 terminal and gauge assembly connector B (12P) No. 10 terminal.
    '04-08 models: Check for continuity between audio unit connector A (20P) No. 19 terminal and gauge assembly connector A (22P) No. 19 terminal.

**Connector orientation:** See the source image. For 2000–2003, test the RED ILL− wire between audio unit terminal 19 and gauge connector B terminal 10. For 2004–2008, test audio unit terminal 19 to gauge connector A terminal 19.

**Is there continuity?**
*   **YES** — Go to step 9.
*   **NO** — Repair open in the wire between the gauge assembly and the audio unit.

**Page Reference:** 22-274

---

### Printed page 22-275

<a id="p1767"></a>
Source: [PDF p.1767](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1767.png).

### Audio button illumination — conclusion

9. Turn ignition ON (II).
10. With headlights still on, measure voltage between audio unit 20P terminal No. 9 (ILL+, RED/BLK) and body ground. If battery voltage is present, check the audio connector and replace the audio unit if connections are sound. If absent, repair the open wire between under-dash fuse/relay box and audio unit.

### Radio preset memory is lost

Check battery condition and connector terminals first. Set each station preset. If every button sets normally, continue to step 5. Otherwise turn ignition to LOCK (0), remove audio unit (p. 22-288), and measure voltage between audio unit 20P terminal No. 10 (+B, WHT/BLU) and body ground. If battery voltage is present, continue to step 5. If absent, repair the open wire from under-dash fuse No. 22 (15 A) to terminal 10. Turn ignition to LOCK (0) for one minute, then ON (II), and test preset recall. If recall works, inspect audio unit connections for an intermittent fault; otherwise replace the unit.

**Source correction:** The source prints `YES` for both voltage-test branches; the repair-open branch applies when battery voltage is absent.

---

### Printed page 22-276

<a id="p1768"></a>
Source: [PDF p.1768](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1768.png).

# Audio System
## Symptom Troubleshooting(cont'd)
### Audio disc does not eject
**NOTE:**
* Check the vehicle battery condition first.
* Check the connectors for poor connections or loose terminals.
* Disc labels should not be used in the audio unit. They may damage the player mechanism.

1. Turn on the audio unit.
Does the system turn on?
* **YES** — Go to step 2.
* **NO** — Go to power switch will not turn ON (see page 22-270).

2. Check to see if the disc ejects correctly with no binding by pushing the **EJECT** button.
Is it normal?
* **YES** — Operation is normal .
* **NO** — Replace the audio unit (see page 22-288).

### Volume does not change
**NOTE:**
* Check the vehicle battery condition first.
* Check the connectors for poor connections or loose terminals.
* Set the fader and balance positions to the center.

1. Turn on the audio unit and listen to sound from the speakers.
Is the sound normal ?
* **YES** — Go to step 2.
* **NO** — Go to audio system sound is weak or distorted (see page 22-273), or no sound is heard from speakers (see page 22-271).

2. Operate the volume knob to see if the volume changes.
Does the volume change?
* **YES** — Operation is normal.
* **NO** — Replace the audio unit (see page 22-288).

---

### Printed page 22-277

<a id="p1769"></a>
Source: [PDF p.1769](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1769.png).

# Radio tuner does not change stations

**NOTE:**
*   Check the vehicle battery condition first.
*   Check the connectors for poor connections or loose terminals.

1.  Turn on the audio unit and check the audio information on the display panel.
    Does the audio information display properly?
    *   **YES** - Go to step 2 .
    *   **NO**—Go to power switch will not turn ON (see page 22-270).

2.  Operate the tuning knob to see if the radio station changes.
    Does the radio station change?
    *   **YES**—Intermittent failure: the tuning knob is OK at this time. Check for loose or poor connections.
    *   **NO**—Replace the audio unit (see page 22-288).

# Audio disc does not load

**NOTE:**
*   Check the vehicle battery condition first.
*   Check the connectors for poor connections or loose terminals.
*   Disc labels should not be used in the audio unit. They may damage the player mechanism.
*   Make sure the disc is compatible with the system (see the owner's manual for more information).

1.  Insert a known-good disc to see if the symptom can be duplicated.
    Does the disc load?
    *   **YES**—Operation is normal. If the disc loads normally, but will not play, go to audio disc does not play (see page 22-278).
    *   **NO** — Go to step 2.

2.  Insert another disc.
    Does the disc load?
    *   **YES** — T h e original disc is faulty.
    *   **NO**—Replace the audio unit (see page 22-288).

*Page reference: 22-277*

---

### Printed page 22-278

<a id="p1770"></a>
Source: [PDF p.1770](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1770.png).

### Audio disc does not play

Diagnostics CD: 07AAZ-SDBA100. Check battery and connector condition. With ignition ON (II), try loading a disc. If it does not load, follow p. 22-277. If it loads, try another disc. If that plays, operation is normal; otherwise insert the audio diagnostic CD. If the diagnostic CD plays, the original disc is faulty or unreadable. Otherwise replace the audio unit (p. 22-288).

### Audio disc skips — start

Tools: diagnostics CD 07AAZ-SDBA100 and skip-test CD 07AAZ-SDBA200 or 07AAZ-SDBA300. Confirm tire pressure and inspect the customer's disc for scratches, fingerprints, or marks. Set bass and treble to the customer's listening settings. Compare only with a known-good vehicle of the same model and trim. Test drive to reproduce the skip; if the customer's disc is unavailable, use diagnostic CD tracks 10–12. If no skip occurs, operation is normal. If it skips, test that disc under the same conditions in a known-good vehicle. If it skips there too, the disc/conditions are the cause; otherwise continue at step 5 on the next page, parked with the engine running.

---

### Printed page 22-279

<a id="p1771"></a>
Source: [PDF p.1771](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1771.png).

### Audio disc skips — conclusion

5. Play tracks 2–11 of skip-test CD 07AAZ-SDBA300 and record where skipping starts. Repeat in a known-good vehicle. If the same tracks skip, operation is normal; otherwise continue.
6. Play tracks 7–11 and 13–15 of skip-test CD 07AAZ-SDBA200 and compare with a known-good vehicle. If the same tracks skip, operation is normal; otherwise replace the audio unit (p. 22-288).

### Audio remote switch does not work properly — start

Check battery and connectors. Test the remote switch (p. 22-287); replace it if faulty. Check audio unit volume, channel, and mode. If these do not work, substitute a known-good audio unit, replacing the original if the fault clears. Otherwise remove the audio unit and continue at step 4 on p. 22-280.

---

### Printed page 22-280

<a id="p1772"></a>
Source: [PDF p.1772](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1772.png).

### Audio remote switch troubleshooting — continued

4. Measure resistance between audio unit 20P terminal No. 3 (GRN/RED) and remote switch 6P terminal No. 5 (BLK ground). The source table gives approximately 263 Ω for VOL DOWN, 512 Ω for VOL UP, 1.1 kΩ for CHANNEL UP, 2.5 kΩ for MODE, and 10 kΩ with no button pressed. If resistance is out of range, repair the open or high-resistance circuit; if wiring is sound, check switch ground G501. If in range, continue.
5. Disconnect both connectors. Eject any disc before removing the audio unit.
6. Check continuity from audio unit terminal No. 3 to body ground. Continuity indicates a wire short to ground between unit and remote switch; no continuity points to the audio unit, which should be replaced (p. 22-288). See the source image for connector orientation.

**Source discrepancy:** The separate switch test on p. 22-287 reverses the VOL UP and VOL DOWN resistance values. Confirm the correct mapping before diagnosis.

---

### Printed page 22-281

<a id="p1773"></a>
Source: [PDF p.1773](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1773.png).

# Sound Quality Diagnosis

## Special Tools Required
* Diagnostics CD 07AAZ-SDBA100

Use the following tests to check sound quality.

> **NOTE:** Before beginning the following tests, write down the customer's bass, treble, fader and balance settings, then set them to their center positions for the testing.

---

### Left/Right Channel ID

Do this test to confirm proper channel routing.

1. Insert audio diagnostic CD (T/N 07AAZ-SDBA100) into the CD player.
2. Play track No. 1 (left, both, right channel ID) at a normal, or slightly higher than normal, volume level.
3. The voice should be audible only from the channel or channels when indicated.

* If the channel ID is correct for each side, go to phase test.
* If the channel ID is not correct, check for:
  * Shorted speaker wire
  * Faulty audio unit

---

### Phase Test

Do this test to confirm proper speaker phasing.

1. Insert audio diagnostic CD (T/N 07AAZ-SDBA100) into the CD player.
2. Play track No. 2 (phase) at a normal, or slightly higher than normal, volume level.
3. The voice should sound centered and focused when it is in-phase.
4. The voice should sound diffused, and have less bass when it is out of phase.

* If the voice changes from in-phase to out of phase as indicated by the prompt, the phasing is correct. Go to electrical noise test (see page 22-282).
* If the voice always sounds out of phase, phasing is not correct. Check for:
  * Crossed speaker wires
  * Faulty audio unit

**Page Reference:** 22-281

---

### Printed page 22-282

<a id="p1774"></a>
Source: [PDF p.1774](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1774.png).

# Audio System
## Sound Quality Diagnosis (cont'd)
### Special Tools Required
**Diagnostics CD**: 07AAZ-SDBA100

### Electrical Noise Test
Do this test to check for electrical noise being induced into the audio system.

> **NOTE**: Electrical noise may be caused by outside sources that cannot be handled by the audio system. Make sure you remove any cell phones and/or turn off any aftermarket device before beginning this test.

1. Insert audio diagnostic CD (**T/N 07AAZ-SDBA100**) into the CD player.
2. Play track No. 4 (**digital zero**) at a normal, or slightly higher than normal, volume level.
3. Operate any electrical device that may create electrical noise in the audio system, including starting the engine.
4. Play track No. 5 (**near digital zero**) at a normal, or slightly higher than normal, volume level.
5. Operate any electrical device that may create electrical noise in the audio system, including starting the engine.
6. Play track No. 6 (**SNR**) at a normal, or slightly higher than normal, volume level.
7. Operate any electrical device that may create electrical noise in the audio system, including starting the engine.

- If no abnormal noise is heard, go to individual speaker test.
- If the noise is present only during the SNR track, replace the audio unit.
- If the noise is heard during the digital zero or near digital zero track, check for:
  - Poor ground for the audio unit, engine or battery cable
  - Pinched or shorted speaker or amplifier wire
  - Faulty audio unit
  - Other faulty components causing excessive electrical noise (ignition coils, alternator, door lock actuators, etc.). Disconnect any suspect components, and then replay the tracks that were originally noisy. If the noise is gone, check the component's circuit and the component.

**Page Reference**: 22-282

---

### Printed page 22-283

<a id="p1775"></a>
Source: [PDF p.1775](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1775.png).

# Page 1775: S2000 Body Electrical - Audio Diagnostics

## Special Tools Required
*   **Diagnostics CD**: T/N 07AAZ-SDBA100

---

### Individual Speaker Test
**Purpose**: Identify a faulty speaker.

1.  Insert audio diagnostic CD (T/N 07AAZ-SDBA100) into the CD player.
2.  Play track No. 30 (steady 300 Hz tone) at a normal, or slightly higher than normal, volume level.
3.  Listen to each speaker for poor sound compared to the other speakers. Use the audio unit's fader and balance settings to help isolate the channel with the problem.
    *   **If** the sound quality produced by a specific speaker is poor, substitute it with a known-good speaker. If the poor sound quality continues, go to the sound balance test (see page 22-283).
    *   **If** the sound quality is OK, go to the sound balance test (see page 22-283).

---

### Sound Balance Test
**Purpose**: Perform this test to identify a faulty channel or speaker.

1.  Insert audio diagnostic CD (T/N 07AAZ-SDBA100) into the CD player.
2.  Confirm the bass and treble are set to the center positions.
3.  Play track No. 3 (pink noise) at a normal, or slightly higher than normal, volume level.
4.  A static type sound should be heard through all speakers.
5.  Insert audio diagnostic CD (T/N 07AAZ-SDBA100) into the CD player of a known-good vehicle.
6.  Set the bass and treble to the center position.
7.  Play track No. 3 (pink noise) all the same level as was played in step 3.
8.  Compare the sounds made by the two vehicles.
    *   **If** the sounds made by the two vehicles are very similar, go to the Frequency Sweep Test (see page 22-284).
    *   **If** the sound does not have as much bass, check the speaker circuit.
    *   **If** the sound does not have enough hiss, check the tweeters and their circuits.

---

*Reference: Page 22-283*

---

### Printed page 22-284

<a id="p1776"></a>
Source: [PDF p.1776](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1776.png).

# Sound Quality Diagnosis (cont'd)

## Special Tools Required
*   Diagnostics CD 07AAZ-SDBA100

### Frequency sweep
Do this test to find rattles or reverberation that may cause a perception of poor sound quality.

1. Insert audio diagnostic CD (T/N 07AAZ-SDBA100) into the CD player.
2. Play track No. 13 (sweep from 500 Hz to 35 Hz) at a normal, or slightly higher than normal, volume level.
3. Listen to each speaker for poor sound quality or reverberations caused by specific frequencies. Use the voice-over to estimate the frequency that causes the vibration. Use the audio unit's fader and balance settings to help isolate the channel with the problem.
*   If vibrations or poor sound quality is heard, go to step 4.
*   If no vibrations or poor sound quality is heard, go to sound judging (see page 22-284).

4. Choose the appropriate track from No. 14 to 25 (small range frequency sweep) or 26 to 53 (single frequencies) to recreate the frequency that caused the poor sound quality or vibration located in step 3: this aids in diagnosis of the cause.

> NOTE: When you get to the track that recreates the problem, select the repeat function on the audio unit, this will help you isolate the cause.

5. Replace or insulate the source of the vibration or, if the speaker is the source of the poor sound quality, replace it.

---

## Sound judging
Do this test to compare overall sound quality, imaging, and dynamics between the customer's vehicle and a known-good vehicle. Only use a vehicle of the same model and trim level for this test.

1. In the customer's vehicle, set the bass, treble, fader, and balance settings to the customer's normal settings that were written down before beginning testing.
2. insert audio diagnostic CD (T/N 07AAZ-SDBA100) into the CD player.
3. Play tracks No. 7 to 12 (sound quality, midband, dynamics, and imaging demonstration tracks) at a normal, or slightly higher than normal, volume level. Write d o w n the volume setting being used.
4. Listen to areas of the track that stand out as being either very clear or poorer than other areas of the track.
5. Insert audio diagnostic CD (T/N 07AAZ-SDBA100) into the CD player of a known-good vehicle.
6. Play the tracks at the same volume level and the same bass, treble, balance, and fader settings as used in step 3 in the customer's vehicle.
7. Listen to the same area of the track that stood out as being either very clear or poorer than other areas of the track.

**22-284**

---

### Printed page 22-285

<a id="p1777"></a>
Source: [PDF p.1777](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1777.png).

### Sound judging — conclusion

Compare the customer's audio quality with a known-good vehicle. Comparable quality means operation is as designed. Otherwise inspect, in order, loose or improperly installed speakers/hardware, poor power or ground, damaged speakers, and a faulty audio unit.

### Seek stop test — start

This tests AM/FM tuner reception after audio symptom troubleshooting (p. 22-271). Window tint, theft-recovery devices, accessories, clouds, and atmospheric conditions may affect reception.

1. Park the customer's vehicle in an open area, away from obstructions.
2. Park a known-good vehicle of the same year, model, and trim alongside it, facing the same direction.
3. Start the customer's engine and turn on the radio.
4. Tune FM to 87.7 MHz.
5. Press Seek+ and record the first locked station.
6. Keep pressing Seek+, recording each station until the first recurs.
7. Tune AM to 530 kHz.
8. Press Seek+ and record the first locked station.
9. Keep pressing Seek+, recording stations until the first recurs. Continue on p. 22-286.

---

### Printed page 22-286

<a id="p1778"></a>
Source: [PDF p.1778](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1778.png).

# Audio System
## Sound Quality Diagnosis (cont'd)
10. Turn the ignition switch to LOCK (0).
11. Start the engine in the known-good vehicle, and then perform steps 4 through 10 on the known-good vehicle.
12. Compare the number of stations received in steps 6 and 9 in the customer's vehicle with the number of stations received in the known-good vehicle.

* If the number of stations received is the same, or within 10%, the audio unit's tuner performance is OK. The problem may be atmospheric conditions, multipath interference, or other obstructions to the radio signal.
* If the customer's vehicle receives fewer stations by at least 10%, go to step 2 of poor AM or FM radio reception or interference (see page 22-267).

**Page Reference:** 22-286

---

### Printed page 22-287

<a id="p1779"></a>
Source: [PDF p.1779](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1779.png).

### Audio remote switch replacement

Remove the instrument panel (p. 20-84), disconnect the remote switch 6P connector (A), remove the three mounting screws (B), and pull out the engine start switch (C). Replace bulbs (D) if needed, then install in reverse order. See the source image for part locations.

### Audio remote switch test

Disconnect the 6P connector. Between terminals No. 5 and No. 6, expect about 10 kΩ with no button pressed, 263 Ω with VOL UP, 512 Ω with VOL DOWN, 1.1 kΩ with CH, and 2.5 kΩ with MODE. Replace the switch if values differ. The source table shows an illumination-bulb path between terminals 3 and 4 with the combination light switch on or off; use the source image for its symbols. With MUTE on, terminals No. 2 (+) and No. 1 (−) should have continuity; otherwise replace the switch.

**Source discrepancy:** The remote troubleshooting table on p. 22-280 reverses the VOL UP/DOWN resistances. Confirm mapping before diagnosis.

---

### Printed page 22-288

<a id="p1780"></a>
Source: [PDF p.1780](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1780.png).

# Audio System
## Audio Unit Removal/Installation
**NOTE:** Eject the disc before removing the audio unit to prevent damaging the CD player's load mechanism.
1. Make sure you have the anti-theft code for the audio system, then write down the audio presets.
2. Remove the radio panel (see page 20-84).
3. Remove the four mounting screws (A).
4. Disconnect the 20P connector (B) and AM/FM antenna lead (C) from the audio unit.
5. Install the audio unit in the reverse order of removal.
6. Enter the anti-theft code for the audio system, then enter the audio presets. Set the clock.

## Door Speaker Replacement
1. Remove the door panel (see page 20-5).
2. Remove the three mounting screws.
3. Disconnect the 2P connector from the speaker.
4. Install the speaker in the reverse order of removal.

---

### Printed page 22-289

<a id="p1781"></a>
Source: [PDF p.1781](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1781.png).

# Rear Speaker Replacement
'06-08 models
1. Remove the roll bar and upper trim assembly (see page 20-73).
2. Disconnect the 2P or 3P connector (A). When disconnecting the 2P connector, remove the harness clip (B).
3. Remove the rear speaker grille (C) and the mounting screws.
4. Carefully pull the rear speaker harness out from the roll bar and upper trim assembly, and remove the rear speaker. Be careful not to break the rear speaker harness.
5. Install the rear speaker in the reverse order of removal.

# Tweeter Replacement
'02-08 models
1. Remove the door panel (see page 20-5).
2. Remove the two screws.
3. Disconnect the 2P connector from the tweeter.
4. Install the tweeter in the reverse order of removal.

---

### Printed page 22-290

<a id="p1782"></a>
Source: [PDF p.1782](https://github.com/spacecowboyian/oio-shop-shelf/blob/manuals-s2000/manuals/honda/vehicle/s2000/page-images/p1782.png).

# Audio System
## AM/FM Antenna Replacement

1. Open the trunk lid.
2. Remove the right side trunk trim panel (see page 20-77).
3. Disconnect the 2P connector (A) from the AM/FM antenna amplifier.
4. Remove the AM/FM antenna mast (A).
5. Remove the antenna nut (B) and spacer (C).
6. Disconnect the AM/FM antenna lead (D) from the AM/FM antenna amplifier (E).
7. Loosen the mounting bolt from the AM/FM antenna amplifier.
8. Remove the AM/FM antenna amplifier.
9. Install the AM/FM antenna in the reverse order of removal.

**Page Reference:** 22-290
