# Charging System

*Section code: `CH` | PDF pages 213-218 of `Toyota-4A-FE-4A-GE-engine-repair-manual-OCR.pdf` | 6 pages*

> Faithful transcription. Applies to **both engines**; the alternator components are shown
> separately for 4A-FE and 4A-GE, and the drive-belt tension value is tagged 4A-FE. Charging
> voltage/amperage verified against the page image (CH-5). See [llm-instructions.md](llm-instructions.md).
>
> **Scan gaps:** CH-3 (first on-vehicle inspection steps) is missing (pages jump CH-2 →
> CH-4); the alternator disassembly / inspection / reassembly (CH-8 onward) is **not in
> this scan** — it ends at CH-7 (components). See [10-needs-review.md](10-needs-review.md).

## In this chapter

- [PRECAUTIONS · TROUBLESHOOTING · CHARGING CIRCUIT](#p214) — [PDF p.214]
- [ON-VEHICLE INSPECTION](#p215) — [PDF p.215]
- [CHARGING CIRCUIT — without load](#p216) — [PDF p.216]
- [CHARGING CIRCUIT — with load](#p217) — [PDF p.217]
- [ALTERNATOR — components (4A-FE & 4A-GE)](#p218) — [PDF p.218]

---
<a id="p213"></a>
**[PDF p.213]** — CHARGING SYSTEM (section contents)

Contents as printed: PRECAUTIONS (CH-2), TROUBLESHOOTING (CH-2), CHARGING CIRCUIT (CH-2),
ON-VEHICLE INSPECTION (CH-3), ALTERNATOR (CH-7).

---
<a id="p214"></a>
**[PDF p.214]** — PRECAUTIONS · TROUBLESHOOTING · CHARGING CIRCUIT

### PRECAUTIONS
1. Check that the battery cables are connected to the correct terminals.
2. Disconnect the battery cables when the battery is given a quick charge.
3. Do not perform tests with a high-voltage insulation resistance tester.
4. Never disconnect the battery while the engine is running.

### TROUBLESHOOTING

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| Discharge warning light does not light (ignition ON, engine off) | Fuse blown | Check "CHARGE" and "IGN" fuses | |
| | Light burned out | Replace light | |
| | Wiring connection loose | Tighten loose connections | |
| | IC regulator faulty | Replace IC regulator | CH-7 |
| Discharge warning light does not go out (engine running; battery needs frequent recharging) | Drive belt loose or worn | Adjust or replace drive belt | CH-3 |
| | Battery cables loose, corroded or worn | Repair or replace cables | |
| | Fuse blown | Check "CHARGE" or "ENGINE" fuse | |
| | Fusible link blown | Replace fusible link | |
| | IC regulator or alternator faulty | Check charging system | CH-2 |
| | Wiring faulty | Repair wiring | |

### CHARGING CIRCUIT
Wiring diagram (image on [PDF p.214]): Ignition Switch, Charge Warning Light, Alternator,
and fuses/links — **FL AM1 40A (AE, AT180) / 60A (AT171)**, **FL AM2 30A**, **Fuse IGN 10A
(AE) / 7.5A (AT)**, **Fuse CHARGE 7.5A**.
<!-- NEEDS REVIEW: fuse/fusible-link ratings read from a wiring diagram — verify against the page image before quoting. -->

---
<a id="p215"></a>
**[PDF p.215]** — ON-VEHICLE INSPECTION (drive belt, wiring, warning light)

> **Scan gap:** CH-3 (the first on-vehicle inspection steps — battery electrolyte/voltage,
> initial drive-belt visual) is missing; this page begins mid-inspection at the drive-belt
> tension reference.

**(Reference) Drive belt tension** — using SST, check the drive belt tension.
**SST A 09216-00020, SST B 09216-00030.**
**Drive belt tension (4A-FE): New belt 60 – 70 kg; Used belt 40 – 55 kg.**
> **HINT:** "New belt" = used less than 5 minutes on a running engine; "Used belt" = 5
> minutes or more. After installing, confirm the belt seats in the ribbed grooves (check by
> hand it has not slipped out of the crank-pulley groove), then run the engine ~5 minutes
> and recheck tension.

4. **VISUALLY CHECK ALTERNATOR WIRING AND LISTEN FOR ABNORMAL NOISES** — check wiring is in good condition; check for no abnormal noise from the alternator while running.
5. **CHECK DISCHARGE WARNING LIGHT CIRCUIT**
   a. Warm up the engine, then turn it off.
   b. Turn off all accessories.
   c. Turn the ignition switch ON — check the discharge warning light is lit.
   d. Start the engine — check the light goes out. If not as specified, troubleshoot the warning-light circuit.

---
<a id="p216"></a>
**[PDF p.216]** — CHECK CHARGING CIRCUIT WITHOUT LOAD

6. **CHECK CHARGING CIRCUIT WITHOUT LOAD**
   > **HINT:** If a battery/alternator tester is available, connect it per the maker's instructions.

   a. If no tester, connect a voltmeter and ammeter to the charging circuit:
      - Disconnect the wire from alternator terminal **B** and connect it to the ammeter (−).
      - Connect the ammeter (+) to alternator terminal **B**.
      - Connect the voltmeter (+) to alternator terminal **B**; ground the voltmeter (−).
   b. With the engine running from idling to **2,000 rpm**, read the ammeter and voltmeter:
      - **Standard amperage: less than 10 A**
      - **Standard voltage: 13.9 – 15.1 V at 25°C (77°F); 13.5 – 14.3 V at 115°C (239°F)**
   - If voltage is **greater** than standard, replace the IC regulator.
   - If voltage is **less** than standard: with terminal **F** grounded, start the engine and read terminal B — if higher than standard, replace the IC regulator; if less, repair the alternator.

---
<a id="p217"></a>
**[PDF p.217]** — CHECK CHARGING CIRCUIT WITH LOAD

7. **INSPECT CHARGING CIRCUIT WITH LOAD**
   a. With the engine at **2,000 rpm**, turn on the high-beam headlights and set the heater blower switch to "HI".
   b. Read the ammeter. **Standard amperage: 30 A or more.**
   - If less than standard, repair the alternator (see CH-7).
   > **HINT:** With the battery fully charged, the indication will sometimes be less than
   > standard amperage.

---
<a id="p218"></a>
**[PDF p.218]** — ALTERNATOR — COMPONENTS (4A-FE & 4A-GE)

Exploded views for **both engines** (images on [PDF p.218]).

- **4A-FE** components: Pulley, Drive End Frame, Front Bearing, Retainer, Rotor, Rear
  Bearing, Bearing Cover, Rectifier End Frame, Rectifier Holder, Brush Holder with Cover,
  Brush, IC Regulator, Terminal Insulator, Rear End Cover.
- **4A-GE** components: Pulley, Drive End Frame, Front Bearing, Rubber Insulator, Terminal
  Insulator, Brush Holder, Rotor, Rear Bearing, Bearing Cover, IC Regulator, Rear End
  Frame / Cover, Rear End Cover.

> **Scan gap:** the alternator disassembly, inspection, and reassembly procedures (CH-8
> onward) are not present in this scan.
