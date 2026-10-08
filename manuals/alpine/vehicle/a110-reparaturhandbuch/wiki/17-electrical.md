<!-- SOURCE NOTE: PDF pages 320-354 of alpine-a110-reparaturhandbuch.pdf (printed pages 329-363).
Translated from the German original; prose is English, every value is as printed, decimal
separators normalized to the English convention (Rule 13): the page prints "1,25 mkp", this wiki
writes "1.25 mkp". No unit is converted. Wire cross-sections are printed as "12/10", "16/10",
"20/10", "30/10" (tenths of a millimetre of conductor diameter, i.e. 1.2 mm etc.) and are kept in
that notation exactly as printed.
ALL pages 320-354 were read from the rendered page images (200 dpi) and, for every table cell
carrying a value, from 300 dpi crops of prepared.pdf — the OCR of the tables, the component list
and the cable directory is unusable (wrong glyphs, scrambled row order).
Scan defects: the "DerFranzose" watermark crosses every page; p.320 (section title sheet) shows
the facing page bleeding through; p.323 (wiring diagram) and pp.324, 326-329 (cable directory) are
landscape sheets; pp.335 and 341 are clipped at the left margin by a few characters (words such
as "die" read "ie" — no value affected).
HANDWRITTEN / RETOUCHED: p.321 the starter number "6183" in the 1600 S column is in a different,
hand-drawn style; p.334 the terminal letters "A", "B"(drawn like "3") and "C" on the starter figure
are handwritten; p.345 the clearance "ca 5 mm" and several letters around it are inked over by
hand. Each is flagged where it occurs.
p.333 (simple tests of regulator/alternator and starter) is in a different typewriter face from the
rest of the chapter — a later typed insertion, not handwriting.
The wiring diagram (p.323) and the alternator circuit diagrams (p.332) are delivered as images
(Rule 12), not transcribed. -->

# Electrical equipment (all types)

<a id="p320"></a>
**[PDF p.320]**

Section title sheet **C — ELEKTRISCHE AUSRÜSTUNG** (electrical equipment), with a perspective
drawing of the car showing the run of the wiring harnesses. No values on this page.

<!-- NEEDS REVIEW: scan defect — the facing page (the p.321 component table) bleeds through this
sheet in reverse; it is not this page's content and is not transcribed here. -->

<a id="p321"></a>
**[PDF p.321]**

## Electrical components fitted, by version

Components 1–10. The columns are the manual's own version headings.

| Component | 1300 | 1300 G – 1300 S | 1600 S |
|---|---|---|---|
| **1/ Starter motor** — type | DUCEL 12 V 6187 (Typ R. 1170) | PARIS-RHONE 12 V D 8 E 75 (Typ R. 1190) | DUCEL 12 V 6183 (Typ R. 1151) |
| Torque with pinion locked | 1.25 mkp | 1.05 mkp | 1.25 mkp |
| Current draw with pinion locked | 380 A | 380 to 420 A | 375 A |
| **2/ Alternator or DC dynamo** — type | GEN BOSCH 12 V 0101302103 14V 30 A 25 | ALT SEV-MOTOROLA 12 V A 14/30-40 | ALT SEV-MOTOROLA 12 V A 14/30-40 |
| Output current | 30 A — Typ R. 1190, "Grosse Kälte" (extreme cold) | 30 A at 3000 rpm at 13.2 V — Typ R. 1135 | 30 A at 3000 rpm at 13.2 V — Typ R. 1135 |
| **3/ Voltage regulator** | BOSCH 14V 30 A 0190309019 — Typ R. 1190, "Grosse Kälte" | DUCEL 8364 12 V — Typ R. 1135 | DUCEL 8364 12 V — Typ R. 1135 |
| **4/ Distributor** | see the engine chapter | see the engine chapter | see the engine chapter |
| **5/ Spark plugs** | see the engine chapter | see the engine chapter | see the engine chapter |
| **6/ Oil pressure sender (TRAMA)** | Jaeger 12 V, 6 kg/cm², Nr. 6000000624 | Jaeger 12 V, 6 kg/cm², Nr. 6000000624 | Jaeger 12 V, 6 kg/cm², Nr. 6000000624 |
| **7/ Temperature sender ELTRA** for oil and coolant temperature | Jaeger 12 V, Nr. 0853989600, Typ R. 1151 | Jaeger 12 V, Nr. 0853989600, Typ R. 1151 | Jaeger 12 V, Nr. 0853989600, Typ R. 1151 |
| **8/ Thermo-switch MOSTA** for the oil-cooler fan | — | — | Jaeger 12 V, 82/92°, Nr. 0855957600, same as MOSTA R. 1151 |
| **9/ Thermo-switch MOSTA** for the cooling fan (water) | — | Jaeger 12 V, 75/84°, Typ Peugeot | Jaeger 12 V, 75/84°, Typ Peugeot |
| **10/ Cooling fan** — radiator | — | Rabotti 12 V, Nr. 6000000631 | Rabotti 12 V, Nr. 6000000631 |
| Cooling fan — oil cooler | — | — | Rabotti 12 V, Nr. 6000000631 |

<!-- NEEDS REVIEW: the 1300 G – 1300 S starter type is printed "D 3 E 75" or "D 8 E 75" — the
digit is ambiguous on the page image; rendered "D 8 E 75" because every other Paris-Rhône starter
in this chapter is a D 8 E / D 10 E type (D 8 E 49, D 8 E 71, D 8 E 84). Verify. -->
<!-- NEEDS REVIEW: locked-pinion torque for 1300 G – 1300 S reads "1,05 mkp" on the image (OCR
"1,C5"); it could also be "1,35". The 1600 S current reads "375 A" (OCR) but the image could be
"575 A" — this typewriter's 3 has a flat top like a 5; 375 is taken as consistent with the
neighbouring 380 A values. Verify both before using them as test limits. -->
<!-- NEEDS REVIEW: HANDWRITTEN annotation — in the 1600 S starter cell the number "6183" is drawn
by hand in a different style from the typed "DUCEL 12 V" above it. 6183 does agree with the typed
Nota on PDF p.322 and with the starter overhaul section (PDF p.334), so it is reproduced, but it
is not certain the typed original read 6183. -->
<!-- NEEDS REVIEW: cross-check against chapter 02 ("DC dynamo for the Alpine 1300, 25 to 30 Amp;
alternator 30/40 Amp for all other versions"): AGREES — the 1300 has a Bosch dynamo ("GEN",
printed "14V 30 A 25", output 30 A) and the 1300 G/S and 1600 S have the SEV-Motorola 30/40 A
alternator. Note the 1300 column prints "Typ R. 1190 / Grosse Kälte" under both the dynamo and
the regulator — reproduced as printed; R. 1190 is otherwise the 1300 G/S type code. The battery
(12 V – 55 Ah per chapter 02) is not listed on these pages. -->

<a id="p322"></a>
**[PDF p.322]**

Components 11–24.

| Component | 1300 | 1300 G – 1300 S | 1600 S |
|---|---|---|---|
| **11/ Ammeter or voltmeter** | Ammeter Jaeger 30 A, Nr. 6000000059 | Voltmeter Jaeger 12 V, Nr. 0855808900, Typ R. 1135 | Voltmeter Jaeger 12 V, Nr. 0855808900, Typ R. 1135, or ammeter 30 A on works equipment |
| **12/ Oil pressure gauge** | Jaeger 12 V | Jaeger 12 V | Jaeger 12 V |
| **13/ Coolant temperature gauge** | Jaeger 12 V | Jaeger 12 V | Jaeger 12 V |
| **14/ Oil temperature gauge** | Jaeger 12 V | Jaeger 12 V | Jaeger 12 V |
| **15/ Fuel gauge** | in the instrument panel, Veglia | in the instrument panel, Veglia | in the instrument panel, Veglia |
| **16/ Speedometer – odometer** | Veglia 12 V | Veglia 12 V | Veglia 12 V |
| **17/ Rev counter** | Veglia | Veglia | Veglia |
| **18/ Relay** — halogen driving lamps, fog lamps, horns | DUCEL 12 V 22621 | DUCEL 12 V 22621 | DUCEL 12 V 22621 |
| **19/ Wiper motor** | SEV 12 V, derived from Typ R. 1133 | SEV 12 V, derived from Typ R. 1133 | SEV 12 V, derived from Typ R. 1133 |
| **20/ Heater blower motor** | Sofica 12 V, Typ R. 1135 | Sofica 12 V, Typ R. 1135 | Sofica 12 V, Typ R. 1135 |
| **21/ Lighting switch** | Jaeger, Typ R. 1132 | Jaeger, Typ R. 1132 | Jaeger, Typ R. 1132 |
| **22/ Headlamps** | Cibié Ø 180 | Cibié Ø 180 | Cibié Ø 180 |
| **23/ Halogen driving lamps** | Cibié Ø 162 | Cibié Ø 162 | Cibié Ø 162 |
| **24/ Country (long-range) horn** | DUCEL Tenor | DUCEL Tenor | DUCEL Tenor |

> **Nota:** on the 1600 S the Paris-Rhône starter type **D8 E71** is to be preferred to the
> Ducellier type **6183**.

<!-- NEEDS REVIEW: the 1600 S voltmeter cell is faint; its number reads "0855808900" (same as the
1300 G/S cell) and "Typ R. 1135"; the ammeter rating is printed "?? A" with the digits nearly
gone — rendered "30 A" by analogy with the 1300 ammeter; verify. "bei Werksausf." rendered "on
works equipment" (factory/competition specification). The meaning of "Überland-Signalhorn"
(item 24) is a long-range "country" horn as opposed to the town horn — printed
"ÜBERLAND-SIGNALHORN". -->

<a id="p323"></a>
**[PDF p.323]**

## Wiring diagram

**SCHALTPLAN — ELEKTRISCHE AUSRÜSTUNG — Ausrüstung "Frankreich"** (wiring diagram, electrical
equipment, French-market specification). The numbered components are keyed in the
[component key](#wiring-diagram-component-key) below; the lettered/numbered wires (A1, C8, D15,
101 …) are listed in the [cable directory](#cable-directory).

![Wiring diagram, A110, French-market equipment (Schaltplan) — PDF p.323](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0323-wiring-diagram-france.webp)

<!-- NEEDS REVIEW: diagram-only page, delivered as an image and not transcribed as text. It is the
French-market ("Frankreich") version; no diagram for the Italian or German equipment is printed in
this chapter (the update supplement, PDF 434-468, re-issues the electrical lists). -->

<a id="p324"></a>
**[PDF p.324]**

## Cable directory

**KABELVERZEICHNIS.** Harness letters:

| Letter | Harness |
|---|---|
| A | Rear lighting harness |
| B | Rear fan harness |
| C | Main rear harness |
| D | Combination and indicator switch harness |
| F | Fog lamp harness |
| P | Left interior lamp harness |
| R | Left headlamp harness |
| S | Right headlamp harness |
| T | Fuel level sender harness |
| V | Fog lamp power supply harness |
| W | Front fan harness |

Columns: wire number (*Kennzahl*), colour (*Farbe*), conductor size (*Ø*, as printed), and the
designation as **from → to**.

<!-- NEEDS REVIEW: translation choices used throughout the cable directory —
"Klemmleiste" = terminal strip; "Stromklemme ohne Kontakt" = permanent-feed terminal (live without
the ignition), "Stromklemme mit Kontakt" = ignition-switched feed terminal (French "+ avant / après
contact"); "Lila" = lilac/purple, rendered "Lilac"; "Rosa" = Pink. If the feed-terminal reading is
wrong, the two are swapped everywhere, so verify one against the wiring diagram before relying on
it. -->

### A — rear lighting harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| A1 | Lilac – grey | 12/10 | Left indicator | Terminal strip |
| A2 | Brown – grey | 12/10 | Right indicator | Terminal strip |
| A3 | Pink | 12/10 | Right stop lamp | Terminal strip |
| A4 | Yellow – red | 12/10 | Right tail lamp | Terminal strip |
| A5 | Yellow – red | 12/10 | Left tail lamp | Terminal strip |
| A6 | Pink | 12/10 | Left stop lamp | Terminal strip |
| A7 | Yellow – red | 12/10 | Number-plate lamp | Terminal strip |
| A8 | Yellow – red | 12/10 | Number-plate lamp | Terminal strip |

### B — rear fan harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| B1 | Red | 16/10 | Rear fan power feed | Terminal strip |
| B2 | Black | 16/10 | Fan – oil pressure switch | "mano" |

<!-- NEEDS REVIEW: B2's destination is printed "mano" (French "manocontact", pressure switch);
kept as printed. Together with "Ventilator – Öldruckschalter" the switch meant may be the fan
thermo-switch rather than the oil pressure switch — check the wiring diagram. -->

### C — main rear harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| C1 | Black – red | 12/10 | Rev counter | Terminal strip |
| C2 | Blue | 12/10 | Oil pressure switch | *(not printed)* |
| C3 | Brown – green | 12/10 | Temperature sender | Temperature sender – rev counter |
| C4 | Grey | 12/10 | Oil pressure switch | Oil pressure warning lamp |
| C5 | Lilac – red | 12/10 | Indicator relay | Terminal strip |
| C6 | Brown – red | 12/10 | Indicator relay | Terminal strip |
| C7 | Red – grey | 12/10 | Ignition coil | Ignition switch |
| C8 | Grey | 20/10 | Starter motor | Ignition switch |
| C9 | Brown | 16/10 | Temperature sender | Front fan relay |
| C10 | Red | 16/10 | Temperature sender | Front fan relay |

<!-- NEEDS REVIEW: C2 has no destination printed. C3's line prints "Wärmefühler" in the from
column and "Wärmefühler   Drehzahlmesser" across the to column — the middle word may belong to a
different column; rendered as printed. -->

<a id="p325"></a>
**[PDF p.325]**

## Wiring diagram component key

| No. | Component | No. | Component |
|---|---|---|---|
| 1 | Right headlamp | 40 | Parking lamp terminal strip |
| 2 | Right driving lamp | 41 | Switch, left half of windscreen heating |
| 3 | Right fog lamp | 42 | Front fan switch |
| 4 | Left headlamp | 43 | Wiper switch |
| 5 | Left driving lamp | 44 | Driving lamp switch |
| 6 | Left fog lamp | 45 | Fog lamp switch |
| 7 | Right indicator | 46 | Heater blower switch |
| 8 | Left indicator | 47 | Switch, right half of windscreen heating |
| 9 | Front cooling fan | 48 | Green warning lamp, left half of windscreen heating |
| 10 | Battery | 49 | Red warning lamp, front fan |
| 11 | Country horn | 50 | Blue main-beam warning lamp |
| 12 | Compressor for the country horn | 51 | Yellow warning lamp, driving lamps |
| 13 | Relay for the country horn | 52 | Yellow warning lamp, fog lamps |
| 14 | Driving lamp relay | 53 | Green warning lamp, right half of windscreen heating |
| 15 | Fog lamp relay | 54 | Red warning lamp, oil pressure |
| 16 | Terminal strip 6-5 | 55 | Yellow warning lamp, handbrake |
| 17 | Terminal strip 6-3 | 56 | Ignition switch |
| 18 | Terminal strip 6-6 | 57 | Combination switch |
| 19 | Handbrake switch | 58 | Coolant temperature sender |
| 20 | Voltage regulator DUCELLIER | 59 | Electric fuel pump |
| 21 | Indicator relay | 60 | Alternator |
| 22 | Front cooling fan relay | 61 | Starter motor |
| 23 | Fuel gauge | 62 | Rear fan |
| 24 | Town horn | 63 | Right interior lamp |
| 25 | Washer pedal | 64 | Front right door switch |
| 26 | Wiper motor | 65 | Left interior lamp |
| 27 | Right parking lamp | 66 | Front left door switch |
| 28 | Left parking lamp | 67 | Coolant temperature sender |
| 29 | Resistor, right half of windscreen heating | 68 | Distributor |
| 30 | Heater blower | 69 | Oil pressure switch |
| 31 | Cigar lighter | 70 | Oil temperature sender |
| 32 | Odometer | 71 | Ignition coil |
| 33 | Voltmeter | 72 | Rear fan terminal strip |
| 34 | Clock | 73 | Number-plate lamp |
| 35 | Oil pressure gauge | 74 | Right tail lamp |
| 36 | Rev counter | 75 | Left tail lamp |
| 37 | Instrument lighting rheostat | 76 | Permanent-feed terminal (ohne Kontakt) |
| 38 | Resistor, left half of windscreen heating | 77 | Ignition-switched feed terminal (mit Kontakt) |
| 39 | Stop lamp switch | | |

<!-- NEEDS REVIEW: item 17 reads "Klemmleiste 6-3" on the image (could be 6-5, which is item 16's
number — the 3 has a flat top). Items 58 and 67 are both printed "Kühlwasser-Temperaturgeber"
(coolant temperature sender) — reproduced as printed; the second may be the oil temperature or
fan sender. "Kilometerzähler" (item 32) is rendered "odometer"; in this car it is the
speedometer/odometer head (component 16 on PDF p.322). -->

<a id="p326"></a>
**[PDF p.326]**

### C — main rear harness (continued)

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| C11 | Blue – black | 12/10 | Alternator terminal DF | Field (exciter) terminal of the voltage regulator |
| C12 | Blue – white | 30/10 | Permanent-feed terminal on the instrument panel | Alternator |
| C13 | Yellow | 12/10 | Parking lamp terminal | Terminal strip |
| C14 | Pink | 12/10 | Combination and indicator switch harness | Terminal strip |
| C15 | Red | 16/10 | Ignition-switched feed terminal | Electric fuel pump |
| C16 | Red | 12/10 | Ignition-switched feed terminal | Terminal strip |

### D — combination and indicator switch harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| D1 | White – red | 16/10 | Combination and indicator switch | Horn relay |
| D2 | Lilac – pink | 16/10 | Combination and indicator switch | Terminal strip 6-5 |
| D3 | Brown – red | 12/10 | Combination and indicator switch | Terminal strip 6-5 |
| D4 | Lilac – red | 12/10 | Combination and indicator switch | Terminal strip 6-5 |
| D5 | Brown – red | 12/10 | Combination and indicator switch | Indicator relay |
| D6 | Lilac – red | 12/10 | Combination and indicator switch | Indicator relay |
| D7 | Blue – grey | 12/10 | Combination and indicator switch | Indicator relay |
| D8 | Blue – grey | 20/10 | Combination and indicator switch | Permanent-feed terminal |
| D9 | Yellow | 12/10 | Combination and indicator switch | Terminal strip |
| D10 | Yellow | 12/10 | Combination and indicator switch | Parking lamp terminal |
| D11 | Green | 16/10 | Combination and indicator switch | Driving lamp switch |
| D12 | Green | 12/10 | Combination and indicator switch | Main-beam warning lamp |
| D13 | Green – blue | 16/10 | Combination and indicator switch | Terminal strip |
| D14 | Pink – red | 16/10 | Combination and indicator switch | Terminal strip |
| D15 | Blue – lilac | 12/10 | Combination and indicator switch | Left parking lamp |
| D16 | Blue – brown | 12/10 | Combination and indicator switch | Right parking lamp |
| D17 | Red – grey | 20/10 | Driving lamp switch | Relay |
| D18 | Red – grey | 12/10 | Driving lamp warning lamp | Relay |
| D19 | Red – grey | 12/10 | Ignition-switched feed terminal | Stop lamp switch |
| D20 | Pink | 12/10 | Stop lamp switch | Rear harness |
| D21 | White | 30/10 | + Battery | Permanent-feed terminal |

### E — instrument panel harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| E1 | Blue | 12/10 | Interior lamp | Permanent-feed terminal |
| E2 | Red | 16/10 | Switch, right half of windscreen heating | Ignition-switched feed terminal |
| E3 | Red | 16/10 | Heater blower switch | Ignition-switched feed terminal |
| E4 | Blue | 16/10 | Cigar lighter | Permanent-feed terminal |
| E5 | Yellow | 12/10 | Cigar lighter | Lighting terminal |
| E6 | Red | 16/10 | Wiper switch | Permanent-feed terminal |
| E7 | White | 16/10 | Wiper switch | Wiper |
| E8 | Red | 16/10 | Wiper | Washer pedal |
| E9 | White | 16/10 | Wiper | Washer pedal |
| E10 | Red | 16/10 | Wiper | Ignition-switched feed terminal |

<!-- NEEDS REVIEW: on this sheet the designation lines do NOT sit level with the wire-number rows —
long designations wrap onto a second line and push the rest down. The from/to pairs above were
re-aligned by counting entries (C: 6 rows / 6 designations; D: 21 / 21; E: 10 / 10), which gives
a one-to-one fit in every block, but on the page several "to" entries print one line lower than
the wire they belong to. The E block is the least certain: E2's designation spans two lines
("Schalter f. re. Hälfte Windschutzsch. / Beheizung") and the "to" column shows ten entries
that could also be read one row offset (E2 → ignition-switched, E3 → ignition-switched, E4 →
permanent, E5 → lighting …). Verify any E-wire against the wiring diagram (PDF p.323) before
cutting into it. -->

<a id="p327"></a>
**[PDF p.327]**

### F — fog lamp harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| F1 | Green | 16/10 | Fog lamp switch | Relay |
| F2 | Green | 12/10 | Fog lamp warning lamp | Relay |

### P — left interior lamp harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| P1 | Blue | 12/10 | *(not printed)* | *(not printed)* |
| P2 | Red | 16/10 | *(not printed)* | *(not printed)* |
| P3 | Red | 12/10 | *(not printed)* | *(not printed)* |

### R — left headlamp harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| R1 | Red – grey | 20/10 | Driving lamp | Terminal strip |
| R2 | Lilac – grey | 16/10 | Left indicator | Terminal strip |
| R3 | Pink | 12/10 | Dipped beam | Terminal strip |
| R4 | Green | 16/10 | Main beam | Terminal strip |
| R5 | Yellow – red | 12/10 | Parking (side) lamp | Terminal strip |

### S — right headlamp harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| S1 | Red – grey | 20/10 | Driving lamp | Terminal strip |
| S2 | Brown – grey | 16/10 | Right indicator | Terminal strip |
| S3 | Pink | 12/10 | Dipped beam | Terminal strip |
| S4 | Green | 16/10 | Main beam | Terminal strip |
| S5 | Yellow – red | 12/10 | Parking (side) lamp | Terminal strip |
| S6 | Lilac – blue | 12/10 | Terminal strip | Town horn |
| S7 | White – green | 20/10 | Terminal strip | Town horn |

### T — fuel level sender harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| T1 | Yellow | 12/10 | Fuel level sender | Fuel gauge |

### V — fog lamp power supply harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| V1 | Green | 16/10 | Right fog lamp | Terminal strip |
| V2 | Green | 16/10 | Left fog lamp | Terminal strip |

### W — front fan harness

| Wire | Colour | Ø | From | To |
|---|---|---|---|---|
| W1 | Brown | 12/10 | Right fan | Terminal strip |
| W2 | Brown | 12/10 | Left fan | Terminal strip |

<!-- NEEDS REVIEW: this sheet's designation column is badly out of step with the wire columns.
Under the heading "INNENLEUCHTE LINKS" (left interior lamp, harness P, 3 wires) the page prints
FIVE designations — driving lamp / left indicator / dipped beam / main beam / parking lamp, all to
the terminal strip — which match harness R (left headlamp, 5 wires) exactly, mirror the seven
lines under "SCHEINWERFER RECHTS" for harness S, and agree in colour with harness A (A1
lilac-grey = left indicator = R2; A2 brown-grey = right indicator = S2). The heading
"SCHEINWERFER LINKS" for harness R is not printed at all. So: the five lines are assigned to R,
and harness P's three designations are NOT printed — they are left blank rather than guessed.
Likewise the "KRAFTSTOFFVORRATGEBER" (T), "STROMVERSORGUNG NEBELLAMPEN" (V) and "VENTILATOR" (W)
designations print one block above their wire numbers and were matched by heading. -->

<a id="p328"></a>
**[PDF p.328]**

### Connections (wires 101–148)

**ANSCHLÜSSE.** These wires carry a fifth column, the cable-end fittings (*Kabelenden*).

| Wire | Colour | Ø | From | To | Cable ends |
|---|---|---|---|---|---|
| 101 | Red | 12/10 | Voltmeter | Handbrake warning lamp | Connector – bare end |
| 102 | Red | 12/10 | Voltmeter | Ignition-switched feed terminal | Double connector, ring terminal Ø |
| 103 | Red | 12/ 0 | Voltmeter | Oil pressure switch | 2 double connectors |
| 104 | Red | 12/10 | Oil pressure switch | Warning lamp | Connector, bare end |
| 105 | Red | 12/10 | "Shunter" both + rev counter | — | Single and double connector |
| 106 | Red | 12/10 | Ignition-switched feed terminal | + Rev counter | Ring terminal with 5 single connectors |
| 107 | Black | 12/10 | Voltmeter | Clock | 2 double connectors |
| 108 | Black | 12/ 0 | Clock | Oil pressure switch | 2 double connectors |
| 109 | Yellow | 12/10 | Voltmeter | Clock | 2 double connectors |
| 110 | Yellow | 12/10 | Clock | Oil pressure switch | 2 double connectors |
| 111 | Yellow | 12/10 | Oil pressure switch | Lighting terminal | 2 double connectors |
| 112 | Blue | 16/10 | Permanent-feed terminal | Clock | Single connector, ring terminal Ø 5 |
| 113 | Yellow | 12/10 | Lighting terminal | Odometer | Single connector, ring terminal Ø 5 |
| 114 | Yellow | 12/10 | Lighting terminal | Rev counter | Single connector, ring terminal Ø 5 |
| 115 | White | 12/10 | Terminal "REP" of the indicator relay | Rev counter | 2 single connectors |
| 116 | Black | 12/10 | Interior lamp | Front right door switch | Single connector, bare |
| 117 | Black | 12/10 | Interior lamp | Front right door switch | 2 ring terminals Ø 5 |
| 118 | Black | 12/10 | Interior lamp | Front left door switch | Single connector, bare |
| 119 | Black | 12/10 | Interior lamp | Front left door switch | 2 ring terminals Ø 5 |
| 120 | Red | 12/10 | Switch, right half of windscreen heating | Warning lamp | Double connector, bare |
| 121 | Black | 12/10 | Fog lamp warning lamp | Driving lamp warning lamp | Bare at both ends |
| 122 | Black | 12/10 | Driving lamp warning lamp | Main-beam warning lamp | Bare at both ends |
| 123 | Pink | 16/10 | Combination and indicator switch | Fog lamp switch | 2 single connectors |
| 124 | Red | 12/10 | Switch, left half of windscreen heating | Warning lamp | Double connector – bare |
| 125 | White | 12/10 | Front fan relay | Switch | 2 single connectors |
| 126 | White | 12/10 | Fan switch | Warning lamp | Double connector, bare |
| 127 | Red – grey | 20/10 | Driving lamp relay | Terminal strip | Single connector, ring terminal 5 |
| 128 | Yellow | 16/10 | Driving lamp relay | Parking lamp terminal | 2 ring terminals of 5 |
| 129 | Yellow | 16/10 | Driving lamp relay | Fog lamp relay | 2 ring terminals of 5 |
| 130 | Yellow | 16/10 | Fog lamp relay, terminal B | Terminal | 2 ring terminals of 5 |
| 131 | Black | 12/10 | Horn relay "Rel. Signalh." | Driving lamp relay | 2 ring terminals of 5 |
| 132 | Red | 12/10 | Horn relay | Compressor | 2 ring terminals of 5 |
| 133 | Black | 12/10 | Horn relay | Compressor | 2 ring terminals of 5 |
| 134 | Red – black | 12/10 | Terminal strip | Ignition coil | Single connector – ring terminal 5 |
| 135 | Red | 12/10 | Indicator relay | Ignition-switched feed terminal | Single connector – ring terminal 5 |
| 136 | Red | 12/10 | Voltage regulator | Ignition-switched feed terminal | Single connector – ring terminal 5 |
| 137 | White | 12/10 | Handbrake switch | Handbrake warning lamp | Single connector – bare |
| 138 | Red | 12/10 | Fan relay | Ignition-switched feed terminal | Single connector – ring terminal 5 |

<!-- NEEDS REVIEW: wires 103 and 108 print the size as "12/ 0" — the "1" of "10" did not strike on
the typewriter (confirmed on a 300 dpi crop). Almost certainly 12/10 like every neighbour, but
kept as printed. Wire 102's cable end is printed "Kabelschuh Ø" with no size after it (the
column edge). "Shunter" (105) and "REP" (115) are French terms left as printed — "REP" is
probably the indicator relay's warning-lamp terminal ("repétiteur"); not verified. -->

<a id="p329"></a>
**[PDF p.329]**

| Wire | Colour | Ø | From | To | Cable ends |
|---|---|---|---|---|---|
| 139 | Blue | 12/10 | Fan relay | Permanent-feed terminal | Single connector – ring terminal Ø 5 |
| 140 | Red | 12/10 | Fan relay | Terminal strip | 2 single connectors |
| 141 | Red | 12/10 | Odometer | Ignition-switched feed terminal | Single connector – ring terminal Ø 5 |
| 142 | Blue | 16/10 | Ignition switch | Permanent-feed terminal | Ring terminal Ø 5 and Ø 4 |
| 143 | Red | 16/10 | Ignition switch | Ignition-switched feed terminal | Ring terminal Ø 5 and Ø 4 |
| 144 | Green | 16/10 | Fog lamp relay | Terminal strip | Ring terminal Ø 5 – single connector |
| 145 | Blue | 16/10 | Horn relay | Permanent-feed terminal | 2 ring terminals Ø 5 |
| 146 | Red – black | 16/10 | Terminal "RUP" of the ignition coil | Delco (distributor) | 2 ring terminals Ø 4 |
| 147 | Yellow | 16/10 | Parking lamp terminal | Rheostat | Ring terminal Ø 5 – bare |
| 148 | Yellow | 16/10 | Lighting terminal | Rheostat | Ring terminal Ø 5 – bare |

<!-- NEEDS REVIEW: "Klemme RUP Zündspule" (146) kept as printed — "RUP" is the coil's contact-
breaker ("rupteur") terminal in French usage; "Delco" is the French shop word for the distributor.
The upper half of this sheet is blank apart from bleed-through from the facing page. -->

<a id="p330"></a>
**[PDF p.330]**

## Bulb table

**LAMPENTABELLE.**

| Market | Application | Bulb | Order no. |
|---|---|---|---|
| France | Main and dipped beam | Bilux bulb, yellow, 12 V 40/45 W | 77 01 348 007 |
| Italy – Germany | Main and dipped beam | Bilux bulb, white, 12 V 40/45 W | 77 01 348 008 |
| France – Italy – Germany | Driving lamps | Halogen bulb, 12 V – 55 W | 08 55 829 500 |
| France – Italy – Germany | Fog lamps | Halogen bulb, 12 V – 55 W | 60 00 001 472 |
| France | Parking lamps | Bulb 12 V – 0.25 A | 60 00 000 143 |
| Germany – Italy | Parking lamps | Bulb 12 V – 4 W | 77 01 348 013 |
| France – Germany – Italy | Front indicators | Bulb 12 V – 21 W | 08 54 626 500 |
| France – Germany – Italy | Rear indicators | Bulb 12 V – 21 W – P 25-1, cap BA 15S-19 (1073) | 08 54 626 500 |
| France – Germany – Italy | Tail and stop lamps | Bulb 12 V – 21/5W – P 25-2, cap BA 15 and 19 (1034) | 08 54 576 100 |
| France | Number-plate lamp | Bulb 12 V – 7 W | 08 54 615 500 |
| Italy | Number-plate lamp | Bulb 12 V – 5 W | 77 01 348 020 |
| Germany | Number-plate lamp | Festoon bulb 12 V – 2.7 W | 60 00 001 512 |
| France – Italy – Germany | Interior lighting | Festoon bulb 12 V – 2.7 W | 60 00 001 587 |
| France – Italy – Germany | Parking lamp – oil pressure warning lamp – handbrake warning lamp | Bulb 12 V – 4 W | 77 01 348 013 |
| France – Italy – Germany | Lighting of odometer, rev counter, oil pressure gauge | Bulb 12 V – 3 W ("Spezial flash") | 60 00 001 511 |
| France – Italy – Germany | Lighting of clock – main-beam warning lamp | Bulb 12 V – 3 W | 60 00 001 510 |
| France – Italy – Germany | Warning lamps for rear window heating – fan – driving lamps – fog lamps – voltmeter lighting | Bulb 24 V – 3 W | 60 00 000 578 |

<!-- NEEDS REVIEW: the last row is printed "Lampe 24 V - 3 W" on a 12 V car (confirmed on a 300 dpi
crop — it is clearly "24"). Possibly deliberate (an under-run bulb for a dim warning lamp) or a
source misprint; kept as printed. The same row says "Heckscheibenbeheizung" (REAR window heating)
whereas the component key (PDF p.325) only lists WINDSCREEN heating warning lamps — reproduced as
printed. The France parking lamp is rated in amperes ("0,25 A"), not watts, as printed. -->

<a id="p331"></a>
**[PDF p.331]**

## Alternators and voltage regulators

**DREHSTROMLICHTMASCHINE – SPANNUNGSREGLER.**

| Equipment | Make | Type | Voltage | Output | Rotor winding resistance | Matching voltage regulator |
|---|---|---|---|---|---|---|
| Normal equipment | SEV-Motorola (1st version) | 26 607 / 26 647 | 12 V | 30/40 A | 5.2 Ohm, measured at the slip rings | S.E.V. 33 546, or Ducellier 8350 (1st version), 8364 (2nd version), 8371 (3rd version), or Paris-Rhône AYB 218 |
| Normal equipment | SEV-Motorola (2nd version) | 34 837 | 12 V | 30/40 A | 5.2 Ohm, measured at the slip rings | (as above) |
| Normal equipment | Paris-Rhône | A 13 R 63 | 12 V | 30/40 A | 4.4 Ohm, measured at the slip rings | (as above) |
| "Grosse Kälte" (extreme cold) equipment | Paris-Rhône | A 13 R123 | 12 V | 50 A | 4.4 Ohm, measured at the slip rings | (as above) |

<!-- NEEDS REVIEW: the regulator column is one merged cell spanning all four alternators; it is not
stated which regulator goes with which alternator. The S.E.V. regulator number prints as "33 ,546"
with a stray mark between the groups; rendered "33 546". The 5.2 Ohm figure is one cell spanning
both SEV-Motorola rows. Resistances printed as "Ohm" in words (no Ω→2 OCR risk here; read from
the image). -->
<!-- NEEDS REVIEW: cross-check against chapter 02 ("alternator 30/40 Amp for all other
versions"): the "Grosse Kälte" (extreme-cold) Paris-Rhône A 13 R123 is rated 50 A — a higher
rating than chapter 02 states. Chapter 02 describes standard equipment; this is an
option/market variant. Not a contradiction of the normal-equipment value, but chapter 02's
"30/40 Amp for all other versions" is not true of this variant. -->

<a id="p332"></a>
**[PDF p.332]**

## Alternator circuit diagrams

**Schaltschema der Drehstromlichtmaschinen** — circuit diagrams of the S.E.V.-Motorola (figure
76380.1, stator drawn delta-connected) and Paris-Rhône (figure 76381.1, stator drawn
star-connected) alternators, each with its six-diode rectifier, separate regulator (terminals
"Exc" and "+"), ignition switch and battery. No values.

![Alternator circuit diagrams, S.E.V.-Motorola and Paris-Rhône — PDF p.332](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0332-alternator-circuit-diagrams.webp)

<a id="p333"></a>
**[PDF p.333]**

## Simple testing of the regulator and alternator

### Checking whether the alternator charges

1. Start the engine and switch on the lights. Raise the engine speed from a very low idle.
   **The lights must become slightly brighter.**
2. Disconnect the cable from the **+ terminal** of the alternator.

   > **Caution:** only with the engine stopped!

3. Connect an ammeter between this cable and the + connection of the alternator. Start the
   engine and switch on all consumers. **The ammeter must show a high current, approx. 20 A.**

### Improvised check of the regulator voltage

1. Start the engine, switch on no consumers, and let it run at a slightly raised idle for
   approx. **5 minutes**.
2. Measure the voltage between the + and – poles of the battery. **It must be 14 V – 15 V.**
3. Switch on all consumers: the voltage must now **not fall below 13 V – 13.5 V**.

### Establishing whether the regulator or the alternator is defective

1. As a temporary measure, replace the regulator with an identical — or at least a similar —
   regulator that is known to be good.
2. Carry out the checks above.

| Result | Diagnosis |
|---|---|
| The fault no longer occurs | Regulator defective — replace it with a new one |
| The fault still occurs | Alternator defective — overhaul or replace it |

## Simple testing of the starter

Turn the ignition switch to **START**. Check whether voltage arrives at **terminal A** (see
[Overhaul of starter Ducellier 6183](#overhaul-of-starter-ducellier-6183)). Have a second person
hold the ignition switch at START continuously.

| Result | Cause | Remedy |
|---|---|---|
| No voltage arrives | Fault in the ignition switch or in cable **C8** | Bridge terminals **A** and **B** with a heavy, preferably insulated, screwdriver or similar. The starter engages. |
| Voltage arrives | Starter or solenoid defective | (Provisional only — may not succeed:) tap the solenoid or starter lightly. Better: bridge terminal **B** and terminal **C**; the starter turns without engaging properly. Try 3 – 4 times, then bridge terminal A and terminal B. If the starter still does not engage: **push-start the car!** |

<!-- NEEDS REVIEW: the terminal letters A, B and C refer to the starter figure on PDF p.334, where
they are HANDWRITTEN additions, not factory labels (see that page). This test page is itself in a
different typeface from the factory text — a later insertion. C8 is the grey 20/10 starter wire
from the ignition switch (cable directory, PDF p.324). The printed line reads "Es kommt
[gap] Spannung" — rendered "voltage arrives" from the context of the preceding "no voltage" case. -->

<a id="p334"></a>
**[PDF p.334]**

## Overhaul of starter Ducellier 6183

Remove the starter motor.

### Dismantling

1. Remove:
   - the rear cover plate;
   - the through-bolt;
   - the cable connection;
   - the rear end bracket.
2. Pull off the yoke.
3. Remove:
   - the securing nuts of the solenoid;
   - the pivot pin of the engagement fork between solenoid and pinion.
4. Take out the armature and the solenoid.
5. Check the condition of the commutator; if necessary skim the commutator and undercut the
   commutator segments.

> If the armature is replaced, the engagement fork between solenoid and pinion must be
> re-adjusted (see page 34 — i.e. [Ducellier — adjusting the engagement fork between solenoid and pinion](#ducellier-adjusting-the-engagement-fork-between-solenoid-and-pinion)).

6. Check the pinion and the brushes; replace them if necessary.

### Starter type 6183 A

If the armature is replaced, the pinion must be replaced at the same time, because the two parts
are a matched pair. If these parts are separated, on reassembly they must be aligned to each
other so that the pinion engages in the recess of the armature.

![Ducellier 6183 starter, with hand-added terminal letters A, B, C — PDF p.334](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0334-ducellier-6183-terminals.webp)

<!-- NEEDS REVIEW: HANDWRITTEN annotation — on the top figure (72459) a previous owner has inked the
letters "A" and "C" on two leader lines to the solenoid terminals and a "3"-shaped letter (read as
"B") on the top terminal. These are the terminals the starter test on PDF p.333 refers to. They
are NOT factory labels. "siehe Seite 34" is a page number from another (French) document's
pagination, not this book's; the fork adjustment is on PDF p.338. -->

<a id="p335"></a>
**[PDF p.335]**

### Reassembly

1. Grease the front bearing bush and fit the armature with the solenoid into the drive-end
   (flange) housing of the starter.
2. Tighten the securing nuts of the solenoid and fit the pivot pin of the engagement fork.
3. Fit the spacer washers to the armature and align them correctly:
   - **1** — steel washer;
   - **2** — fibre washer.
4. Grease the rear bearing bush.
5. Fit:
   - the yoke;
   - the rear end bracket;
   - the spring and the washers, observing the locating detent (**1** — spring; **2** — plastic
     washer).
6. Tighten the housing bolts and fit the cover.

<a id="p336"></a>
**[PDF p.336]**

## Ducellier — replacing the drive pinion and brushes

Remove the starter motor.

### Replacing the drive pinion

1. Remove the armature.
2. Press the stop collar back with a tube so that the circlip can be removed.
3. Pull off the drive pinion.
4. On refitting, fit the circlip and slide the stop collar over it.
5. Then align the engagement fork between solenoid and pinion correctly (see page 34 — i.e.
   [Ducellier — adjusting the engagement fork between solenoid and pinion](#ducellier-adjusting-the-engagement-fork-between-solenoid-and-pinion)).

### Starter type 6183 A

If the drive pinion is replaced, the armature must be replaced at the same time, because the two
parts are matched to each other. If these parts are separated on dismantling, on reassembly they
must be aligned to each other again so that the pinion engages in the recess of the armature.

<a id="p337"></a>
**[PDF p.337]**

### Replacing the brushes

1. Pull off the end bracket and the yoke.
2. Unsolder the brushes to be replaced.
3. Solder in the new brushes.
4. Check the armature and reassemble the starter.

<!-- NEEDS REVIEW: no brush length or commutator diameter/wear limit is printed anywhere in this
chapter (PDF 320-354) for either starter or alternator. Do not infer one from this section. -->

## Ducellier — replacing the solenoid

Remove the starter motor.

### Removal

1. Pull off the yoke and separate the solenoid from the drive-end housing.
2. Separate the engagement fork and the solenoid; when slackening the screw **(A)**, hold the
   plunger **(B)**.

### Refitting

1. Tighten the screw **(A)** firmly on reassembly.
2. Check the adjustment of the engagement fork between solenoid and pinion and correct it if
   necessary.

<a id="p338"></a>
**[PDF p.338]**

## Ducellier — adjusting the engagement fork between solenoid and pinion

1. Remove the blanking plug in front of the solenoid.
2. Check the clearance **(F)** between screw and adjusting nut: with the pinion held firmly
   against the armature, this clearance must be **as small as possible**.
3. Then push the solenoid adjusting screw fully back and check that the clearance **(G)** is
   **between 0.05 and 1.5 mm**.
4. If necessary, adjust the adjusting nut **(1)** to obtain the specified clearance at (G) and
   (F).

![Ducellier starter — engagement fork adjustment, clearances F and G and adjusting nut 1 — PDF p.338](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0338-ducellier-fork-adjustment.webp)

<!-- NEEDS REVIEW: clearance (G) is printed "0,05 und 1,5 mm" (underlined; confirmed on a 300 dpi
crop). A thirty-fold spread from 0.05 to 1.5 mm is unusual for a pinion clearance and "0,5" may
have been intended — but the page clearly prints 0,05. Kept as printed: source value, possible
source misprint, not OCR. -->

<a id="p339"></a>
**[PDF p.339]**

## Overhaul of Paris-Rhône starters

Exploded views of the Paris-Rhône starter types **D 8 E 49** (figure 76474) and **D 10 E 43**
(figure 76473). No values.

![Paris-Rhône starters D 8 E 49 and D 10 E 43 — exploded views — PDF p.339](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0339-paris-rhone-starter-d8e49-d10e43-exploded.webp)

<a id="p340"></a>
**[PDF p.340]**

Exploded view of the starter types **D8E71 – D8E84 – D10E48**, with the drive-end housings of
D8E71 – D10E48 and of D8E84, the field coils of D10E48 and of D8E71 – D8E84 shown separately
(figures 71513.2 and 71512.2).

![Paris-Rhône starters D8E71, D8E84, D10E48 — exploded view with type-specific parts — PDF p.340](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0340-paris-rhone-starter-d8e71-d8e84-d10e48-exploded.webp)

Remove the starter motor.

### Dismantling

1. Disconnect the electrical connections.
2. Remove:
   - the cover band (if fitted);
   - the rear end bracket.
3. Pull off the yoke.
4. Slacken or remove:
   - the pivot pin of the engagement fork between solenoid and pinion;
   - the securing nuts of the solenoid.
5. Take out the armature and the solenoid.
6. Check the condition of the commutator; if necessary skim the commutator and undercut the
   commutator segments.

<a id="p341"></a>
**[PDF p.341]**

### Starter types D 8 E 71 – D 8 E 84 – D 10 E 48

To replace the intermediate end bracket, the drive pinion must be removed. To do so, press the
stop collar back with a tube so that the circlip can be removed. On refitting, make sure the
spacer washers are correctly seated.

After replacing the armature or the end bracket, check the adjustment of the engagement fork
between solenoid and pinion and correct it if necessary (see page 41 — the Paris-Rhône fork
adjustment, PDF p.345).

Washer stack at the intermediate bracket (figure 74201): **1** steel washers; **2** wave
washers; **3** fibre washer; **4** normal shim.

### Reassembly

**D 8 E 71 – D 8 E 84 – D 10 E 48** — washers on the armature shaft (figure 74204.2): **1** steel
washer; **2** wave washer; **3** fibre washer.

**D 8 E 49 – D 10 E 43** — fibre washer **3** only (figure 74204.2); the engagement forks of
D10E43 (recess **A**) and D8E49 (recess **B**) differ.

1. Fit the armature and solenoid, observing the orientation of the engagement fork: **recess A
   towards the drive pinion on starters D 10 E 43; recess B towards the armature on starters
   D 8 E 49.**
2. Grease the armature bearing bush and fit the armature into the drive-end housing.
3. Tighten the solenoid fixings and fit the pivot pin of the engagement fork.
4. Fit the spacer washers of the rear end bracket.

<!-- NEEDS REVIEW: the left-margin box heading prints "8 E 71 - D 8 E 84 - D 10 E 48" with the
leading "D" clipped by the scan; the right box's last type prints "D 10 E 4?" with the final digit
lost — read as D 10 E 43 from the sub-labels beneath it. "siehe Seite 41" is another document's
page number; the Paris-Rhône fork adjustment is on PDF p.345. -->

<a id="p342"></a>
**[PDF p.342]**

Rear end bracket assembly, by type: **D 10 E 43** (figure 76549 — spring, washers and bolt
under the end cap) and **D 8 E 71 – D 8 E 74 – D 10 E 48** (figures 75385.1 and 76420; **3** —
fibre washers, figure 73684.A).

5. Fit:
   - the yoke;
   - the rear end bracket; grease the bush.
6. Tighten the securing nuts of the end bracket and remake the electrical connections.

<!-- NEEDS REVIEW: the boxed type label at the bottom of this page prints "D 8 E 74", whereas every
other occurrence in the chapter is "D 8 E 84" — probably a source misprint for D 8 E 84 (not OCR;
the image is clear). The top label prints "D 10 E 4?" with the last digit faint; read as 43. -->

<a id="p343"></a>
**[PDF p.343]**

## Paris-Rhône — replacing the drive pinion and brushes

Remove the starter motor.

### Replacing the drive pinion — removal

1. Remove the armature.
2. Press the stop collar back with a tube (starters **D 8 E 71 – D 8 E 84 – D 10 E 48**).
3. Remove the released circlip.
4. Cut open (grind off) the stop collar so that it can be removed with the half-rings (starters
   **D 8 E 49 – D 10 E 43**).

### Replacing the drive pinion — refitting

- Starters **D 8 E 71 – D 8 E 84 – D 10 E 48**: fit the circlip and slide the stop collar over
  it.
- Starters **D 8 E 49 – D 10 E 43**: slide a new stop collar over the previously fitted
  half-rings, and stake the collar rim at several points.

### Replacing the brushes

1. Remove the rear end bracket and the yoke.
2. Unsolder the brushes to be replaced.
3. Solder on the new brushes; check the armature and reassemble the starter.

<a id="p344"></a>
**[PDF p.344]**

## Paris-Rhône — replacing the solenoid

Remove the starter motor.

### Starters D 8 E 71 – D 8 E 84 – D 10 E 48

**Removal**

1. Remove the yoke and the armature.
2. Take out the solenoid.
3. Separate the fork from the solenoid after slackening the adjusting screw **(A)**.

**Refitting**

1. Fit the spring, the fork and the plastic bush. To fit the engagement fork, slacken the screw
   **(A)**.
2. Then adjust the fork (see page 41 — PDF p.345).

### Starters D 8 E 49 – D 10 E 43

**Removal**

1. Disconnect:
   - the electrical connections;
   - the securing nuts.
2. Take out the solenoid.

**Refitting**

1. Carry out the removal operations in reverse order.
2. Fit the spring and check the seal.
3. Then adjust the engagement fork between solenoid and pinion (see page 41 — PDF p.345).

<a id="p345"></a>
**[PDF p.345]**

## Paris-Rhône — adjusting the engagement fork between solenoid and drive pinion

1. Supply the solenoid with current as shown in the figure alongside (battery + and – to the
   solenoid).
2. In the position now taken up by the pinion, check the clearance **(H)** between pinion and
   stop collar. **It must be approx. 5 mm.**

**D 8 E 49 – D 10 E 43:** if the clearance is not correct, remove the solenoid and adjust the
connecting piece **(B)** accordingly.

**D 8 E 71 – D 8 E 84 – D 10 E 48:** if the clearance is not correct, remove the blanking plug in
front of the solenoid, adjust the adjusting screw **(A)** accordingly, and refit the plug.

![Paris-Rhône starter — engagement fork adjustment, clearance H, solenoid supply, adjusters A and B — PDF p.345](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0345-paris-rhone-fork-adjustment.webp)

<!-- NEEDS REVIEW: HANDWRITTEN / RETOUCHED — the clearance is printed "ca5 mm" (underlined) and the
letters "ca" and several characters around it ("Den", "det", "In", "St", "und") have been inked
over by hand. It is not certain whether the typed original read "ca. 5 mm" or e.g. "0,5 mm".
Rendered "approx. 5 mm" as it now reads. SAFETY: verify this clearance against another source
before setting a starter. -->

<a id="p346"></a>
**[PDF p.346]**

## Overhaul of S.E.V. Motorola alternators

Types **26 607 – 26 647 – 34 847**. Exploded view figure 78247 (parts marked **26 647 / 34 837**
and **34 837** apply only to those types).

Remove the alternator.

### Dismantling

1. Release the brush holder with its insulating plate.
2. Take the brush holder out of its seat.
3. Clamp the pulley, with a V-belt laid in it, in a vice.
4. Slacken the pulley nut and remove it with the washer. Pull off the pulley.

<!-- NEEDS REVIEW: the heading box prints the third type as "34 847", but the type boxes on the
same exploded view and the alternator table on PDF p.331 both print "34 837". Probable source
misprint in the heading; kept as printed. -->

<a id="p347"></a>
**[PDF p.347]**

5. Remove the four housing bolts.
6. Insert a screwdriver into the slots between the stator and the front end bracket, and press
   the rotor off with the front end bracket.

   > **Do not insert the screwdriver deeper than 2 mm, otherwise the stator winding will be
   > damaged.**

7. Remove the three securing screws of the ball-bearing retaining plate on the front end
   bracket.
8. Separate the end bracket from the rotor by striking the shaft end down onto a wooden board.
   This is only necessary if the ball bearing is to be replaced.
9. Check that the slip rings are not greasy. Check the condition of the winding insulation, the
   slip rings and the winding connections.

<a id="p348"></a>
**[PDF p.348]**

### Rear bearing

1. Pull the bearing off using the puller **B.Vi.28-01**, the claws **B.Vi.48** and the
   turned-down spindle adaptor **Elé.22-01**.
2. Fit a protective sleeve **(A)** onto the threaded portion of the rotor shaft.
3. Press the new bearing on using a tube **applied to the inner race of the bearing**.

<!-- NEEDS REVIEW: the S.E.V. section prints only the REAR bearing procedure; there is no front
bearing section for the S.E.V. alternator (the printed page numbers 356-357 run on without a gap,
so it is a source omission, not a missing scan). The Paris-Rhône front bearing procedure is on
PDF p.352. -->

### Diode holder — removal

1. Remove the four nuts, the serrated washers and the two insulating washers of the diode
   holders.
2. Separate the stator and the diode holders from the rear end bracket.

<a id="p349"></a>
**[PDF p.349]**

### Reassembly

1. When fitting the diode holders, make sure that **the insulating washers and sleeves of the
   positive-diode holder are fitted correctly.**
2. Then carry out the removal operations in reverse order.

> **Check that the wires leading to the diodes are well aligned and do not touch the rotor.**

## S.E.V. Motorola — replacing the brush holder

To remove the brush holder, remove the two securing screws.

<a id="p350"></a>
**[PDF p.350]**

## Overhaul of Paris-Rhône alternators

Exploded view of the Paris-Rhône alternator. No values on the figure.

Remove the alternator.

### Dismantling

1. Slacken the two securing screws of the brush holder and remove it.
2. Clamp the pulley, with a V-belt laid in it, in a vice so as not to damage it.
3. Slacken the pulley nut and remove it with the washer.
4. Pull off the pulley.

<a id="p351"></a>
**[PDF p.351]**

5. Remove the four housing bolts.
6. Insert a screwdriver into the slots between the stator and the front end bracket, so as to
   press the rotor off with the front end bracket.

   > **Do not insert the screwdriver deeper than 2 mm, otherwise the stator winding will be
   > damaged.**

7. Remove the securing screws of the ball-bearing retaining plate on the front end bracket.
8. Separate the end bracket from the rotor by striking the shaft end onto a wooden board, as
   shown in the figure. This is only necessary if the ball bearing is to be replaced.
9. Check that the slip rings are not greasy. Check the condition of the winding insulation, the
   slip rings and the winding connections.

<!-- NEEDS REVIEW: step 6 prints "anzudrücken" (to press on) where the S.E.V. text on PDF p.347 has
"abdrücken" (to press off); rendered "press off" as the operation shown is the same. -->

<a id="p352"></a>
**[PDF p.352]**

### Replacing the front and rear ball bearings

**Front bearing**

1. Remove the pulley key from the rotor shaft.
2. Clamp the rotor lightly **in a vice fitted with protective jaws**.
3. Fit the puller **B.Vi.28-01** with the claws **B.Vi.48** and the protective sleeve
   **Rou.15-01**.
4. Pull the bearing off.
5. Check the flat face of the bearing flange.
6. Fit the bearing flange.
7. Press the new bearing on with a tube **applied to the inner race**.
8. Refit the key.

<a id="p353"></a>
**[PDF p.353]**

**Rear bearing**

1. Pull the bearing off using the puller **B.Vi.28-01**, the claws **B.Vi.48** and the
   turned-down spindle adaptor **Elé.22-01**.
2. Fit a protective sleeve **(A)** onto the threaded portion of the rotor shaft.
3. Press the new bearing on using a tube **applied to the inner race of the bearing**.

### Reassembly

Fit the slotted bush into the housing as intended and fit the rotor with both bearings.

<a id="p354"></a>
**[PDF p.354]**

Centre the rear retaining bracket with a **10 mm Ø** drift. Tighten the securing screws.

## Paris-Rhône — replacing the diode holder

### Removal

1. Remove:
   - the cover plate;
   - the securing nuts of the diode holder and the connecting terminal.
2. Take out the diode holder.

> **If one diode is damaged, the complete holder must be replaced.**

### Refitting

Carry out the removal operations in reverse order.

## Paris-Rhône — replacing the brush holder

To remove the brush holder, remove the two securing screws.

## Special tools used in this chapter

| Tool | Use |
|---|---|
| B.Vi.28-01 | Puller for the alternator front and rear bearings |
| B.Vi.48 | Claws for B.Vi.28-01 |
| Elé.22-01 | Turned-down spindle adaptor (alternator rear bearing) |
| Rou.15-01 | Protective sleeve (alternator front bearing) |

## Next

[Bodywork](18-body.md).
