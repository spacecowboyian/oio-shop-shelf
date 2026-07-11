# Starting System

*Section code: `ST` | PDF pages 208-212 of `Toyota-4A-FE-4A-GE-engine-repair-manual-OCR.pdf` | 5 pages*

> **Scan gap (this manual is abridged).** The section's own page numbers jump from
> **ST-3 to ST-15** — pages **ST-4 through ST-14** (starter removal, disassembly,
> component inspection, reassembly) are **not present in this scan**. See
> [10-needs-review.md](10-needs-review.md). For those procedures, cross-check the other
> 4A manual in this repo ([`toyota-4a-fe-4a-ge`](../../toyota-4a-fe-4a-ge/wiki/00-index.md))
> until this scan is completed.

## In this chapter

- [TROUBLESHOOTING](#p209) — [PDF p.209]
- [STARTING SYSTEM CIRCUIT](#p209) — [PDF p.209]
- [PLANETARY TYPE STARTER — components (4A-GE)](#p210) — [PDF p.210]
- [PLANETARY TYPE STARTER — performance test](#p211) — [PDF p.211]

---
<a id="p208"></a>
**[PDF p.208]** — STARTING SYSTEM (section title / contents)

Section contents as printed: TROUBLESHOOTING (ST-2), STARTING SYSTEM CIRCUIT (ST-2),
PLANETARY TYPE STARTER (ST-3).

---
<a id="p209"></a>
**[PDF p.209]** — TROUBLESHOOTING · STARTING SYSTEM CIRCUIT

### TROUBLESHOOTING

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| Engine will not crank | Battery charge low | Check battery specific gravity; charge or replace battery | CH-4 |
| | Battery cables loose, corroded or worn | Repair or replace cables | |
| | Neutral start switch faulty (A/T) | Adjust or replace switch | |
| | Fusible link blown | Replace fusible link | |
| | Starter faulty | Repair starter | ST-3, 17 |
| | Ignition switch faulty | Replace ignition switch | |
| Engine cranks slowly | Battery charge low | Check battery specific gravity; charge or replace battery | CH-4 |
| | Battery cables loose, corroded or worn | Repair or replace cables | |
| | Starter faulty | Repair starter | ST-3, 17 |
| Starter keeps running | Starter faulty | Repair starter | ST-3, 17 |
| | Ignition switch faulty | Replace ignition switch | |
| | Short in wiring | Repair wiring | |
| Starter spins — engine will not crank | Pinion gear teeth broken or faulty starter | Repair starter | ST-3, 17 |
| | Flywheel or drive plate teeth broken | Replace flywheel or drive plate | |

<!-- NEEDS REVIEW: Remedy pages cite "ST-3, 17" and "ST-17", but ST-17 is beyond the pages present in this scan (see section gap note). -->

### STARTING SYSTEM CIRCUIT

Wiring diagram (image only — see [PDF p.209]). Shows: Ignition Switch, Battery, Starter,
Neutral Start Switch (A/T), and fusible links —
`ALT 100A`, `MAIN 2.0L`, `40A (AE, AT180)`, `60A (AT171)`.
<!-- NEEDS REVIEW: fusible-link ratings OCR'd from a diagram and are low-confidence — "80A"/"BOA" and "AT1 BO"/"AT180" were ambiguous in OCR. Verify against the page image before quoting. -->

---
<a id="p210"></a>
**[PDF p.210]** — PLANETARY TYPE STARTER — COMPONENTS (**4A-GE**)

Exploded-view diagram (image only — see [PDF p.210]). Labeled components include:
Magnetic Switch, Starter Housing, Armature, Planetary Gear, Plate Carrier Shaft,
Plate Washer, Field Frame, Commutator End Frame, Through Bolt, O-Ring.

> **NOTE:** Parts marked ✦ (O-Ring, Through Bolt seal) are non-reusable — replace on
> reassembly.

---
<a id="p211"></a>
**[PDF p.211]** — PERFORMANCE TEST OF PLANETARY TYPE STARTER

> **NOTICE:** These tests must be performed within **3 to 5 seconds** to avoid burning
> out the coil.

1. **PERFORM PULL-IN TEST**
   a. Disconnect the field coil lead from terminal C.
   b. Connect the battery to the magnetic switch as shown. Check that the clutch pinion
      gear moves outward.
   - If the clutch pinion gear does not move, replace the magnetic switch.
2. **PERFORM HOLD-IN TEST**
   - With the battery connected as above and with the pinion out, disconnect the
     negative (−) lead from terminal C. Check that the clutch pinion remains out.
   - If the clutch pinion gear returns inward, replace the magnetic switch.
3. **INSPECT CLUTCH PINION GEAR RETURN**
   - Disconnect the negative (−) lead from the switch body. Check that the clutch pinion
     gear returns inward.
   - If the clutch pinion does not return, replace the magnetic switch.
4. **INSPECT CLUTCH PINION GEAR CLEARANCE** *(continued on [PDF p.212])*
   a. Connect the battery to the magnetic switch as shown.

---
<a id="p212"></a>
**[PDF p.212]** — CLUTCH PINION GEAR CLEARANCE · NO-LOAD PERFORMANCE TEST

4. **INSPECT CLUTCH PINION GEAR CLEARANCE** *(continued)*
   b. Move the pinion gear toward the armature to remove slack and measure the clearance
      between the pinion gear end and stop collar.
   - **Standard clearance: 1 – 5 mm (0.04 – 0.20 in.)**
     <!-- NEEDS REVIEW: printed value verified against the page image (ST-16) and internally consistent (1 mm ≈ 0.04 in), but 1–5 mm is unusually large for pinion-gear clearance; confirm against a full copy of this manual. -->
5. **PERFORM NO-LOAD PERFORMANCE TEST**
   a. Connect the field coil lead to terminal C. Check that the lead is not grounded.
   b. Connect the battery and ammeter to the starter as shown (ammeter to Terminal 30).
   c. Check that the starter rotates smoothly and steadily with the clutch pinion gear
      moving out. Check the reading on the ammeter.
   - **Specified current: 90 A or less at 11.5 V**
