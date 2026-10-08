<!-- SOURCE NOTE: PDF pages 139-141 of alpine-a110-reparaturhandbuch.pdf. Translated from the
German original; prose is English, every value is as printed. Decimal separators are normalized
to the English convention (Rule 13): the page prints "0,4 - 0,5mm", this wiki writes
"0.4 - 0.5 mm". Notation changes, value does not; no unit is converted.
All three pages were read from the rendered page images: the timing/points-gap table on PDF
p.139 OCRs badly (tolerances lost), and PDF p.141 is three advance-curve graphs that OCR to
noise (read at 400 dpi). The "DerFranzose" watermark crosses the 1600 S rows of the table on
p.139 and the R.234 graph on p.141 but does not obscure any digit.
The distributor identification table that opens the ignition section (PDF p.138) is transcribed
in chapter 06, not here. -->

# Ignition system (all types)

Distributor identification (distributor numbers, advance curves, spark plugs per version) — see
[Engine type 812 — overhaul](06-engine-812.md), which carries PDF p.138.

<a id="p139"></a>
**[PDF p.139]**

## Setting the ignition timing and the contact-breaker gap

These settings are made in the usual way. The methods described here, using a test lamp or a
feeler gauge, are not absolutely exact; setting with a stroboscopic (timing) lamp or a dwell
meter is more accurate. In that case follow the instrument's operating instructions, and take
the setting values from the table.

| Vehicle, engine type | Ignition timing (static) | Contact-breaker gap | Dwell angle |
|---|---|---|---|
| **1300 VC** | | | |
| 810-05 | 0° ± 1 | 0.4 - 0.5 mm | All types: 57° ± 2, corresponding to 63 % ± 3 |
| 810-10 | 0° ± 1 | 0.4 - 0.5 mm | (as above) |
| 810-30 | 5° | 0.4 - 0.5 mm | (as above) |
| **1300 G** | | | |
| 812-00 | 0° +1 −0 | 0.4 mm | (as above) |
| **1300 S** | 0° | 0.4 mm | (as above) |
| **1600 S** | | | |
| 807-25 | 0° | 0.4 - 0.5 mm | (as above) |
| 843-30 | 7° +3 −0 | 0.4 - 0.5 mm | (as above) |
| 844-30 | 6° ± 2 | 0.4 - 0.5 mm | (as above) |
| 844-34 | 14° +0 −2 | 0.4 - 0.5 mm | (as above) |

<!-- NEEDS REVIEW: table read from the page image; the OCR loses every tolerance ("> oor'",
"> 0+1", "0 0)"). The dwell column is a single printed entry for the whole table ("Alle:
57° ± 2 entsprechen 63 % ± 3"); it is repeated as "(as above)" per row only for layout.
The 810-30 cell prints "5°" followed by a short stroke that may be the start of a tolerance; no
tolerance digits are legible, so none is given.
The 843-30 "7° +3 −0" and 844-30 "6° ± 2" entries are printed overlapping, with arrows from
both rows; the arrow from 843-30 ends at "7°" and the arrow from 844-30 at "6°". -->

<!-- NEEDS REVIEW: cross-check against the key-settings plate in
[02-general-technical-data.md](02-general-technical-data.md) (PDF p.13).
AGREES: 1300 VC 0° ± 1°; 1600 VD 6° ± 2° (SC) / 14° +0° −2° (SI) — these match 844-30 and
844-34 here; 1600 VH 7° −0° +3° matches 843-30 here; dwell 63 % ± 3 %.
DISAGREES: the plate gives the dwell ANGLE as 57° ± 3°; this page clearly prints 57° ± 2 (the
"2" is unambiguous on the image). This page is the more legible of the two; the plate's "± 3"
may be a misreading of its own hard-to-read cell, or the two sources differ. Not resolved —
both values are as printed/read. This page prints no spark plug types (see PDF p.138 in
chapter 06). -->

## Setting the contact-breaker gap (dwell angle) — valid for all types

1. Remove the distributor cap. (On the 1600 S, possibly remove the distributor completely —
   **mark its position exactly beforehand!**)
2. Turn the distributor cam to give the maximum contact gap.
3. Then, depending on the type of distributor:
   - **either:** slacken screw **1**, set the contact-breaker gap with a feeler gauge (by moving
     the fixed contact), and lock the screw;
   - **or:** insert a screwdriver through the triangular opening of the cassette and adjust
     accordingly. **Never slacken screw A!**
4. Refit the distributor cap and turn the engine over a few times.
5. Check the setting on a **different** cam lobe.

> **IMPORTANT:** afterwards the ignition timing **must** be reset.

<!-- NEEDS REVIEW: printed "Kassette" (cassette) — the contact-set carrier of the second
distributor type; "screw A" is named in the text but the letter A is not visible on either
figure (the left figure is labelled "1"; the right figure shows the screwdriver in the
triangular opening). -->

<a id="p140"></a>
**[PDF p.140]**

## Setting the ignition timing (static)

### 1300 VC / G / S

1. Connect a test lamp between the low-tension terminal of the distributor and earth.
2. Slacken the distributor clamp bolt.
3. Set the valves of **No. 4 cylinder** on overlap ("rocking").
4. Line up the mark on the pulley with the corresponding tooth of the timing pointer on the
   timing cover (figure 1).
5. Switch on the ignition.
6. Turn the distributor **anticlockwise** until the test lamp lights.
7. Lock the distributor.
8. Turn the engine over a few times and check the setting.

Figure 1 shows the timing pointer on the timing cover with three teeth marked **8° 5° 0°**,
and the arrow of engine rotation on the pulley.

<!-- NEEDS REVIEW: printed "Einstellpfeil auf dem Steuergehäusedeckel" — rendered "timing
pointer on the timing cover". "Überschneidung" rendered "overlap (rocking)". -->

### 1600 S

Two possibilities:

- **Figure 2:** mark on the flywheel, visible through the flap inside the car, below the
  alternator, behind the camshaft pulley. The scale on the clutch housing is marked **0, 2, 5**.
- **Figure 3:** marks on the pulley and timing pointer on the timing cover.
  - **One** mark on the pulley: corresponds to advance 0°, top dead centre.
  - **Three** marks: correspond to **0°, 8°, 16°** (see figure 3).

> **NOTE:** the **5°** mark on the clutch housing (figure 2) corresponds to a piston position
> **0.2 mm before TDC**, and to **6 mm (not 6°!)** before the 0° notch on the pulley (figure 3).

The ignition timing is then set as described for the 1300 VC/G/S.

<!-- NEEDS REVIEW: printed "Schwungscheibe" (flywheel), "Klappe im Innenraum" (flap/hatch inside
the car), "Kupplungsgehäuse" (clutch housing / bell housing), "OT" (oberer Totpunkt = TDC). -->

<a id="p141"></a>
**[PDF p.141]**

## Centrifugal advance curves

The page prints three advance graphs (degrees of advance against speed). They are delivered as an
image; the legible axis labels are transcribed below. Read the curves themselves from the image.

![Centrifugal advance curves R.230, R.234 and R.236 — PDF p.141](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0141-advance-curves-r230-r234-r236.webp)

| Curve | Degree labels on the vertical axis | Speed labels on the horizontal axis | Shape of the nominal (centre) line |
|---|---|---|---|
| R. 230 | 0°, 5°, 7°, 10°, 14°, 15° | (illegible), "?00", 750, 1000, 1500, 2000, 2250 | steep rise to about 7° just below 750, then a shallower rise to 14°, level from about 2250 |
| R. 234 | 0°, 5°, 11.9°, 12.1°, 14°, 15.9°, 17.3°, 18° | 450, 880, 1000, 1500, 2000, 2800 / 2900 (overprinted) | steep rise from 0° at 450 to about 11.9° at 880, then a shallower rise to about 18°, level at the top |
| R. 236 | 0°, 10°, 17°, 20° | 500, 1000, 2000, 2750 | almost vertical rise from 0° at about 500 to 10°, then a shallower rise to 17°, level from 2750 |

Each graph shows a tolerance band either side of the nominal line.

<!-- NEEDS REVIEW: the axes carry no units on the page (R.234's horizontal axis is labelled
"t/m" = rev/min); whether the degrees and speeds are distributor or crankshaft values is NOT
stated. The R.230 low-speed labels are cut off by the scan ("- - -  ?00"); the "?00" before 750 is
probably 500 by its spacing but that is not legible. The R.234 small labels read "17.3" (could be
"17.5") and "15.9"; its last speed label is overprinted "2800" over "2900" — not resolvable.
Chart numbers printed inside the graphs: R.236 "64 704"; R.230 a small illegible number.
The "shape" column is a reading of the graph, not printed data.
Note that p.138 (chapter 06) assigns R.230 to the 1300 G / 1300 S, R.234 to the 1600 S/GS and
R.236 to the 1300. The later curves named on the key-settings plate (R 248, R 257, R 258, R 278,
vacuum C 34, D 60, D 62) are NOT printed in this chapter. -->

## Next

[Fuel system](08-fuel-system.md).
