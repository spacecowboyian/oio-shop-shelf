# Ignition System

*Section code: `IG` | PDF pages 103-113 of `Toyota-4A-F-4A-GE-engine-manual-OCR.pdf` | 11 pages*

## In this chapter

- [Ignition System](#p103) ([p.103](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=103)-[p.104](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=104))
- [TENSION CORDS FROM](#p105) ([p.105](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=105)-[p.106](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=106))
- [IGNITION SYSTEM](#p107) ([p.107](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=107)-[p.109](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=109))
- [DISTRIBUTOR](#p110) ([p.110](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=110)-[p.113](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=113))

See also: [Torque Specifications index](09-torque-specs.md) for every torque value in this manual with links back to source.

---
<a id="p103"></a>
**[PDF p.103](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=103)** — Ignition System

### Ignition — Chapter Table of Contents

Chapter table of contents (manual page codes, for reference only — use the section links above to navigate):

| Section | Manual page |
|---|---|
| Ignition System | IG-1 |
| Distributor | IG-7 |

<!-- NEEDS REVIEW: in-manual table of contents lines for "IGNITION SYSTEM" (IG-1) and "DISTRIBUTOR" (IG-7) — dot-leader fill between title and page code OCR'd as unreadable noise; section names and internal page codes appear legible but exact original spacing/formatting is uncertain -->

---
<a id="p104"></a>
**[PDF p.104](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=104)** — Ignition System

### IGNITION SYSTEM — ON-VEHICLE INSPECTION

#### Spark Test

1. CHECK THAT SPARK OCCURS
   (a) Disconnect the high-tension cord (from the ignition coil) from the distributor cap.
   (b) Hold the end approx. 12.5 mm (0.50 in.) from the body ground.
   (c) See if spark occurs while engine is being cranked.

   NOTICE: To prevent gasoline from being injected from injectors during this test, crank the engine for no more than 5 – 10 seconds at a time.

If the spark does not occur, perform the test as follows:

<!-- NEEDS REVIEW: lines below through "ANOTHER IGNITER" are a garbled OCR of a troubleshooting flowchart/decision-tree diagram (a series of checks with OK/BAD branches). Layout and word order are too scrambled to confidently reconstruct; resistance values within are left exactly as OCR'd even though some appear to conflict with the clean restatement of the same checks later in this chapter (e.g. primary ignition coil resistance reads "0.96-0.55" here vs "0.36-0.55" on PDF p.108 — not corrected, left as-is per rule against altering numeric values) -->

Best-effort reconstruction of the spark-test troubleshooting flowchart below (branch order is a best guess from the scrambled OCR — see flagged note above; resistance/gap values are transcribed exactly as OCR'd even where they conflict with the clean restatement on PDF p.108):

| Step | Check | Std Value | If OK | If NG |
|---|---|---|---|---|
| 1 | Check connection of ignition coil, igniter, and distributor connector | — | Go to step 2 | Connect securely |
| 2 | Check resistance of high-tension cord | Maximum resistance: 25 kΩ per cord | Go to step 3 | Replace the cord(s) |
| 3 | Check power supply to ignition coil and igniter | Turn ignition switch to ON. Check that there is battery positive voltage at ignition coil positive (+) terminal | Go to step 4 | Check wiring between ignition switch, ignition coil, and igniter |
| 4 | Check resistance of ignition coil | Primary — Cold: 0.96-0.55, Hot: 0.45-0.659; Secondary — Cold: 9.0-15.4k0, Hot: 114-18.4 kA | Go to step 5 | Replace the ignition coil |
| 5 | Check resistance of signal generator (pickup coil) (see page IG-5) | G1 and G⊙ — Cold: 125-200, Hot: 160-235; G2 and G⊙ — Cold: 125-2000, Hot: 160-235; NE and G⊙ — Cold: 155-2509, Hot: 190-2900 | Go to step 6 | Replace the distributor housing assembly |
| 6 | Check air gap of distributor (see page IG-5) | Air gap: 0.2-0.5 mm (0.008-0.020 in.) | Go to step 7 | Replace the distributor housing assembly |
| 7 | Check IGT signal from ECU (see page FI-26) | — | Go to step 8 | Check wiring between ECU, distributor, and igniter, and then try another ECU |
| 8 | (if all checks above are OK but spark still does not occur) | — | — | Fragment reads "...ANOTHER IGNITER" — likely "Try another igniter"; exact original wording uncertain |

---
<a id="p105"></a>
**[PDF p.105](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=105)** — TENSION CORDS FROM

### High-Tension Cords

<!-- NEEDS REVIEW: step numbers for items 2 and 4 below ("DISCONNECT HIGH-TENSION CORD FROM IGNITION COIL" and "INSPECT HIGH-TENSION CORD RESISTANCE") were not visible in the OCR — they are inferred sequentially between the numbered 1 and the numbered 3/5 that are visible; exact original numbering is uncertain -->

1. DISCONNECT HIGH-TENSION CORDS FROM SPARK PLUGS
   (a) Remove the 6 screws and No.2 cylinder head cover...
   (b) Disconnect the high-tension cords at the rubber boot; do not pull on the high-tension cords.

   NOTICE: Pulling on or bending the cords may damage the conductor inside.

<!-- NEEDS REVIEW: step 1(a) "Remove the 6 screws and No.2 cylinder head cover..." trails off with an ellipsis in the source OCR — the rest of the sentence appears to be missing -->

2. DISCONNECT HIGH-TENSION CORD FROM IGNITION COIL

3. DISCONNECT HIGH-TENSION CORDS FROM DISTRIBUTOR CAP
   (a) Using a screwdriver, lift up the lock claw and disconnect the holder from the distributor cap.
   (b) Disconnect the high-tension cord at the grommet. DO NOT pull on the cords.

   NOTICE: Pulling on or bending the cords may damage the conductor inside.

4. INSPECT HIGH-TENSION CORD RESISTANCE
   Using an ohmmeter, measure the resistance.
   Maximum resistance: 25 kΩ per cord
   If the resistance is greater than maximum, check th...

<!-- NEEDS REVIEW: step 4's last sentence "If the resistance is greater than maximum, check th" is cut off mid-word in the source OCR — likely continues "...check the cord(s)" but the remainder is missing -->

5. RECONNECT HIGH-TENSION CORDS TO DISTRIBUTOR CAP
   (a) Connect the holder and grommet portion to the distributor cap as shown in the illustration.
   (b) Check that the lock claw of the holder is engaged by lightly pulling the holder. *(continues on PDF p.106)*

   NOTICE: Check that the holder is correctly installed to the grommet and distributor cap as shown in the illustration.

   Illustration shows WRONG vs. CORRECT installation. Figure: 1GO949R.

---
<a id="p106"></a>
**[PDF p.106](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=106)** — TENSION CORDS FROM

6. RECONNECT HIGH-TENSION CORDS TO SPARK PLUGS
   (a) Secure the high-tension cords with the clamps as shown in the illustration.
   (b) Reinstall the No.2 cylinder head cover with 6 screws.

### Spark Plugs

NOTICE:
- Never use a wire brush for cleaning.
- Never attempt to adjust the electrode gap on a used spark plug.
- Spark plugs should be replaced every 100,000 km (60,000 miles).

1. INSPECT ELECTRODE
   Using a megger (insulation resistance meter), measure the insulation resistance.
   Standard correct insulation resistance: 10 MΩ or more
   If the resistance is less than specified, proceed to step 4.

   HINT: If a megger is not available, use the following simple method:
   (a) Quickly race the engine to 4,000 rpm 5 times.
   (b) Remove the spark plug. (See step 2)
   (c) Visually check the spark plug.
       - If the electrode is dry ... OK
       - If the electrode is wet ... proceed to step 3
   (d) Reinstall the spark plug. (See step 6)

2. REMOVE SPARK PLUGS
   Using a spark plug wrench, remove the 4 spark plugs.

---
<a id="p107"></a>
**[PDF p.107](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=107)** — IGNITION SYSTEM

### Spark Plugs (continued)

<!-- NEEDS REVIEW: step numbers for "VISUALLY INSPECT SPARK PLUGS" through "RECONNECT HIGH-TENSION CORDS TO SPARK PLUGS" below were not visible in the OCR (likely lost to margin/column noise) — sequential numbers 3-5 are inferred from context following step 2 on PDF p.106; exact original numbering is uncertain -->

3. VISUALLY INSPECT SPARK PLUGS
   Check the spark plug for thread damage and insulator damage.
   If abnormal, replace the spark plug.
   Recommended spark plug:
   - DENSO: PK20R11
   - NGK: BKRGEP-11

<!-- NEEDS REVIEW: NGK spark plug code "BKRGEP-11" (PDF p.107) — the "G" may be an OCR misread of the digit "6" (i.e. "BKR6EP-11"), but left exactly as OCR'd per rule against altering part numbers/values without confidence -->

   INSPECT ELECTRODE GAP
   Maximum electrode gap for used spark plug: 1.3 mm (0.051 in.)
   If the gap is greater than maximum, replace the spark plug.
   Correct electrode gap for new spark plug: 1.1 mm (0.043 in.)

   NOTICE: If adjusting the gap of a new spark plug, bc only the base of the ground electrode. Do not touch thé. Never attempt to adjust the gap on the used plug.

<!-- NEEDS REVIEW: NOTICE sentence about adjusting a new spark plug's gap is truncated at line wraps ("...spark plug, bc" / "Do not touch thé") — likely "bend" and "the [electrode/insulator]" but exact missing words are uncertain -->

   CLEAN SPARK PLUGS
   If the electrode has traces of wet carbon, allow it tq and then clean with a spark plug cleaner.

<!-- NEEDS REVIEW: "If the electrode has traces of wet carbon, allow it tq" — sentence appears to be missing a word after "to" (possibly "dry") before "and then clean with a spark plug cleaner." -->

   Air pressure: Below 588 kPa (6 kgf/cm², 85 psi)
   Duration: 20 seconds or less
   HINT: If there are traces of oil, remove it with gasoline before using the spark plug cleaner.

4. REINSTALL SPARK PLUGS
   Using a spark plug wrench, install the 4 spark plugs.
   Torque: 18 N-m (180 kgf-cm, 13 ft-lbf) → [torque-specs #t041](09-torque-specs.md#t041)

5. RECONNECT HIGH-TENSION CORDS TO SPARK PLUGS

### Ignition Coil

NOTICE: "Cold" and "Hot" in the following sentences express the temperature of the coils themselves. "Cold" is from -10°C (14°F) to 50°C (122°F) and "Hot" is from 50°C (122°F) to 100°C (212°F).

1. DISCONNECT IGNITION COIL CONNECTOR
2. DISCONNECT HIGH-TENSION CORD FROM IGNITION COIL

---
<a id="p108"></a>
**[PDF p.108](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=108)** — IGNITION SYSTEM

3. INSPECT PRIMARY COIL RESISTANCE
   Using an ohmmeter, measure the resistance between the positive (+) and negative (−) terminals.
   Primary coil resistance:
   - Cold: 0.36 - 0.55 Ω
   - Hot: 0.45 - 0.65 Ω

   If the resistance is not as specified, replace the ignition coil.

4. INSPECT SECONDARY COIL RESISTANCE
   Using an ohmmeter, measure the resistance between the positive (+) and high-tension terminals.
   Secondary coil resistance:
   - Cold: 9.0 - 15.4 kΩ
   - Hot: 11.4 - 18.1 kΩ

   If the resistance is not as specified, replace the ignition coil.

5. RECONNECT HIGH-TENSION CORD TO IGNITION COIL
6. RECONNECT IGNITION COIL CONNECTOR

### Distributor

NOTICE: "Cold" and "Hot" in the following sentences express the temperature of the coils themselves. "Cold" is from -10°C (14°F) to 50°C (122°F) and "Hot" is from 50°C (122°F) to 100°C (212°F).

1. REMOVE DISTRIBUTOR CAP
   Remove the 2 bolts, and disconnect the distributor cap from the distributor housing.
2. REMOVE ROTOR
3. INSPECT AIR GAP
   Using SST, measure the air gap between the signal rotor and pickup coil projection.
   SST 09240-00020
   Air gap: 0.2 - 0.5 mm (0.008 - 0.020 in.)
   If the air gap is not as specified, replace the distributor housing assembly.
4. DISCONNECT DISTRIBUTOR CONNECTOR
5. INSPECT SIGNAL GENERATOR (PICKUP COIL) RESISTANCE
   Using an ohmmeter, measure the resistance between terminals.

   | Terminal | Cold | Hot |
   |---|---|---|
   | G1 and G⊙ | 125-200 Ω | 160-235 Ω |
   | G2 and G⊙ | 125-200 Ω | 160-285 Ω |
   | NE and G⊙ | 155-250 Ω | 190-290 Ω |

---
<a id="p109"></a>
**[PDF p.109](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=109)** — IGNITION SYSTEM

If the resistance is not as specified, replace the distributor housing assembly.

6. RECONNECT DISTRIBUTOR CONNECTOR

<!-- NEEDS REVIEW: reassembly step list below (distributor cap/rotor reinstall, igniter reconnect) has scrambled step numbers (6, 8, 7 in that order) and fragmentary lines ("8. Install", "igniter", "(See spark test)") — content present but original step order/wording is uncertain -->

- (fragment) "8. Install"
- REINSTALL DISTRIBUTOR CAP — install a new packing and the distributor cap with the 2 bolts, and [reconnect the] igniter (see Spark Test)
- 7. REINSTALL ROTOR

---
<a id="p110"></a>
**[PDF p.110](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=110)** — DISTRIBUTOR

### DISTRIBUTOR — Components

- Distributor Connector
- Distributor Housing Assembly
- Packing

<!-- NEEDS REVIEW: fragment "Lae 27.8)" on the distributor components diagram is unclear — may be a torque value or page cross-reference; left exactly as OCR'd per rule against guessing at numeric content -->

---
<a id="p111"></a>
**[PDF p.111](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=111)** — DISTRIBUTOR

### DISTRIBUTOR — Removal, Disassembly, Inspection, Reassembly

#### Removal

1. DISCONNECT DISTRIBUTOR CONNECTOR
2. DISCONNECT HIGH-TENSION CORD FROM DISTRIBUTOR CAP
3. REMOVE DISTRIBUTOR
   (a) Remove the hold-down bolt, and pull out the dig...
   (b) *(no text captured)*

<!-- NEEDS REVIEW: removal step (a) is cut off after "pull out the dig" (likely "the distributor"); step (b) has no visible text at all — content appears lost to OCR -->

#### Disassembly

1. REMOVE DISTRIBUTOR CAP
2. REMOVE ROTOR
   Remove the 2 screws and rotor.

#### Inspection

INSPECT SHAFT
Turn the shaft and check that it is not rough or worn. If it feels rough or worn, replace the distributor assembly.

#### Reassembly

1. INSTALL ROTOR
   (a) Align the hollow of the signal rotor with the ¢ the rotor.

<!-- NEEDS REVIEW: rotor-install alignment sentence "Align the hollow of the signal rotor with the ¢" / "the rotor." appears to be missing words in the middle — original instruction unclear -->

   (b) Install the rotor with the 2 screws.
2. INSTALL DISTRIBUTOR CAP
   (a) Install a new packing to the distributor housing.
   (b) Install the distributor cap with the 3 bolts.

---
<a id="p112"></a>
**[PDF p.112](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=112)** — DISTRIBUTOR

### DISTRIBUTOR — Installation

1. SET NO. 1 CYLINDER TO TDC/COMPRESSION
   Turn the crankshaft clockwise, and position the slit of the intake camshaft as shown in the illustration.
2. INSTALL DISTRIBUTOR
   (a) Install a new O-ring to the housing.
   (b) Apply a light coat of engine oil on the O-ring.
   (c) Align the cutout of the coupling with the line of the housing.
   (d) Insert the distributor, aligning the center of the flange with that of the bolt hole on the cylinder head.
   (e) Tighten the hold-down bolt.
       Torque: 23 N-m (230 kgf-cm, 17 ft-lbf) → [torque-specs #t042](09-torque-specs.md#t042)
3. CONNECT HIGH-TENSION CORDS TO SPARK PLUGS
   Firing order: 1-3-4-2
4. CONNECT HIGH-TENSION CORD TO IGNITION COIL
5. CONNECT DISTRIBUTOR CONNECTOR

---
<a id="p113"></a>
**[PDF p.113](https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view#page=113)** — DISTRIBUTOR

This page's OCR text consists solely of the word "LUBRICATION" (likely bleed-through from the header of the next chapter); no distributor content was captured on this page.

