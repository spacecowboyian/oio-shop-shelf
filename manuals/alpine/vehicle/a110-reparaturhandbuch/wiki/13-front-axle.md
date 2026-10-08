<!-- SOURCE NOTE: PDF pages 249-269. Translated from the German original; prose is English, every
value is as printed, decimal separators normalized to the English convention (Rule 13).
Torque on these pages is printed in "mkg" (= mkp) and is NOT converted; one figure also carries
a printed "(5 lb/ft)". Every page in the range was read from the rendered page image, and every
alignment value, torque and wear limit was checked against a high-resolution crop. PDF p.249 is
the section divider "VORDERACHSE" (section tab H) and carries no data. PDF pp.251-253 (checking
camber, castor and toe) are set in a different, larger typewriter face from the pages around
them and may be a later insert; they describe workshop CHECKS only, as p.251 itself says. The "DerFranzose" watermark crosses every
page but obscures no value in this range. -->

# Front axle (all types)

<a id="p249"></a>
**[PDF p.249]**

Section divider: **Front axle** (section tab **H**). No text or values.

<a id="p250"></a>
**[PDF p.250]**

## Description

Independent suspension using the components of the **RENAULT 8 GORDINI**:

- upper wishbone;
- lower wishbone;
- stub-axle carrier.

> **NOTE:** the mounting of the lower wishbone on the cross-member side was, however, modified to
> obtain **negative camber**. The mounting points were moved **9 mm** outwards (this applies only
> to chassis from **2163**).

The page's figures (59208.1 and a second section) mark the camber angle **Ca**, the castor angle
**Ch** and the ball-joint height **H**.

## Setting values

| | Up to chassis no. 2162 | From chassis no. 2163 |
|---|---|---|
| Camber | 1° 40' positive | 1° 30' negative |
| Castor | 9° ± 1 | 8° 30' ± 30 with the more direct steering; 7° 30' ± 30 with normal steering |
| Toe | between 1 mm toe-out and 2 mm toe-in | 2 mm ± 1 toe-out, at half load |

<!-- NEEDS REVIEW: SAFETY-RELEVANT — comparison with the key-settings plate in
[02-general-technical-data.md](02-general-technical-data.md). All values above were read from a
high-resolution crop of the image and agree with the OCR. Printed terms: "Nachspur" = toe-out,
"Vorspur" = toe-in.
(1) TOE DIRECTION: this page gives "2 mm ± 1 Nachspur bei halber Belastung" (toe-OUT, half load)
for every car from chassis 2163, with no split by type. Chapter 02 gives the same 2 ± 1 mm as
toe-OUT for the 1300 VC but toe-IN for the 1600 VD / VH. This page therefore CONFIRMS toe-out
for the 1300 VC and agrees with it for the generic setting; it does NOT confirm toe-in for the
1600s — it neither lists the 1600 types separately nor mentions toe-in for them. The two pages
conflict for the 1600 VD/VH and cannot be reconciled from this chapter. PDF p.254 adds that the
steering-box mounting is designed so the toe change from half load to unladen "always tends to
REDUCE the toe-out" (0 to 2 mm toe-in per side under those conditions), which is consistent with a
toe-out static setting. Resolve against the factory 1600 data before setting a 1600 car.
(2) CAMBER: this page gives 1° 30' negative (no tolerance printed) where chapter 02 gives
−2° ± 30' (1300 VC, 1600 VD) and −2° 25' ± 30' (1600 VH). 1° 30' negative lies at the edge of
the −2° ± 30' band, so it is not a contradiction for VC/VD, but it is a different nominal; the
VH figure is outside it. Probably different model years; kept as printed.
(3) CASTOR: 7° 30' ± 30 (normal steering) matches chapter 02's 1300 VC value (7° 30' ± 30').
8° 30' ± 30 (direct steering) does NOT match chapter 02's 1600 VD/VH value of 8° ± 30'. The
tolerance here is printed "± 30" without the minute sign.
(4) The early (to chassis 2162) castor tolerance "9° ± 1" carries no unit on the tolerance;
read as ± 1°. -->

<a id="p251"></a>
**[PDF p.251]**

## Checking the camber

> **NOTE:** the methods described here are suitable only for **CHECKING** the front-axle values.
> **SETTING** should be done only with suitable equipment, e.g. an optical alignment gauge!

1. Stand the vehicle on an absolutely level surface.
2. Set the front wheels exactly straight ahead. Bounce the front axle several times; if
   possible, have one person sit in the car.
3. With a spirit level and a vernier caliper, determine dimension **A**. Dimensions **B** and
   **C** must be equal.

- With **13"** rims, the camber is **0.1° per mm of A**.
- Example: A = 17 mm → camber = 1.7° negative.
- If dimension A occurs at the **top**, the camber is **negative**; if A occurs at the
  **bottom**, it is positive.

> **CAUTION:** because of the tyre's contact patch ("Latsch"), **E is larger than F**. The exact
> value of A is therefore **Aₑ = A − E + F**.
>
> **Or:** measure A at the rim flange — but then calculate the camber angle (see below)!

The camber of the A 110 front axle normally **cannot be adjusted** (see the note on PDF p.250).
Bear this in mind when **lowering** the car, since the front wheels then take on excessive
negative camber (tyre wear on the inside).

**Exact calculation of the camber angle:** camber (in degrees) = arctan A/D.

<!-- NEEDS REVIEW: HANDWRITTEN annotation — the cross-reference after "Sturzwinkel berechnen!"
is an ink addition reading "(s. unten)" ("see below"). Not factory text. -->

![Checking camber with a spirit level — dimensions A, B, C, D, E, F — PDF p.251](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0251-camber-check-dimensions.webp)

<a id="p252"></a>
**[PDF p.252]**

## Checking the castor of the front wheels

Prepare the vehicle as described for the camber check.

1. Turn the front wheels **20°** to the left. Measure and note the camber on both wheels.
2. Turn the front wheels **20°** to the right. Measure and note the camber on both wheels.
3. Calculate the castor: camber value of the 1st measurement (left lock) **minus** camber value
   of the 2nd measurement (right lock) **equals the castor angle**.

**Example:**

| | Left wheel | Right wheel |
|---|---|---|
| 1st measurement | 3.0° pos. | 4.5° neg. |
| 2nd measurement | 2.5° neg. | 1.0° neg. |
| Result | 5.5° castor | 3.5° castor |

The castor can be adjusted at the bolt **(1)** — see PDF p.255 (printed "s.S. 261").

<!-- NEEDS REVIEW: the right-wheel example does not follow the stated rule arithmetically:
(−4.5°) − (−1.0°) = −3.5°, printed as "3.5° castor". The left wheel gives 3.0 − (−2.5) = 5.5°
as printed. Source as printed; the sign convention for the right wheel is evidently reversed.
Treat this page as a method illustration only — the example values are not specifications. -->

<a id="p253"></a>
**[PDF p.253]**

## Checking the toe of the front wheels

Prepare the vehicle as described for the camber check.

1. Lay a **3 m** long, exactly straight batten against the left wheel (see drawing). Mark point
   **X** on the ground.
2. Find point **Y** at the right wheel. Measure dimension **A**.
3. Push the vehicle back **half a wheel revolution**. Measure dimension **B**.

**Calculating the toe:**

- A greater than B = **toe-out**.
- A smaller than B = **toe-in**.
- With a measuring batten about 3 m long, **1 cm** difference A − B corresponds to about
  **1 mm** of toe-in or toe-out.

**Example:**

| | Case 1 | Case 2 |
|---|---|---|
| A | 1.53 m | 1.60 m |
| B | 1.57 m | 1.57 m |
| A − B | −0.04 m = toe-in | +0.03 m = toe-out |

The toe is set at the **rack end** (see PDF p.258, printed "s.S. 264", item **(1)**).
**One turn of the rack end changes the toe by 3 mm.**

<!-- NEEDS REVIEW: the OCR dropped the "3" in "verändert die Spur um 3mm"; read from the image.
The second example's result OCRs as "+0,05n"; the image shows +0.03 m, which is also the
arithmetic of 1.60 − 1.57 — corrected from image. -->

<a id="p254"></a>
**[PDF p.254]**

## Setting the front axle

With the **FACOM U-70** alignment gauge or the **BEM** optical gauge.

### 1. Preliminary checks

- Check:
  - the tyre pressures;
  - the play in the joints, etc.;
  - the rim run-out (with the BEM gauge this can be neutralized).
- **Castor:** the castor must be the same on both sides; tolerance **± 1°** (the higher value
  should, where possible, be on the right).
- **Steering-box height:** two different kinds of bracket are used:
  - brackets welded to the front cross-member;
  - brackets bolted to the front cross-member — these are supplied in three versions, which
    differ in the distance between the centre of the steering mounting hole and the centre of
    the upper mounting hole on the cross-member:

| Bracket | Distance | Part no. |
|---|---|---|
| Standard bracket | 55 mm | 6000000557 |
| Raised bracket | 56 mm | 6000000351 |
| Raised bracket | 57 mm | 6000001352 |

The figures 56 and 57 are stamped on the rear face of the brackets.

The brackets determine the position of the rack ends relative to the track-rod ball pins, which
is designed so that the **toe change from half load to the unladen vehicle always tends to
reduce the toe-out** (**0 to 2 mm toe-in per side** under these conditions).

<!-- NEEDS REVIEW: printed "Spurveränderung von halber Belastung zu entlastetem Fahrzeug immer
zur Verringerung der Nachspur tendiert (0 bis 2 mm Vorspur pro Achsseite unter diesen
Bedingungen)". Rendered literally. The parenthesis is read as the permitted toe CHANGE per side
between half load and unladen, i.e. towards toe-in — the wording is ambiguous and should be
checked by a German reader. The part number 6000000351 for the 56 mm bracket does not follow the
pattern of the other two (…0557, …1352); it reads clearly on the image and is kept as printed. -->

### 2. Checks and settings

a) Carry out the checks after a test drive, or bounce the vehicle first.
b) Settle the vehicle on a level surface.
c) Check the camber.
d) Check the castor (a maximum difference of **1°** between right and left is permitted). If the
   difference exceeds **1°**, the eccentric at the lower wishbone mounting must be adjusted
   accordingly.
e) Set the steering centre point: place the tool **Dir. 326** between the end face of the
   steering housing and the rack nut on the pinion side. Lock the steering in this position with
   the clamping tool **T.Av. 34**.
f) Put the front wheels on turntables.
g) Lock the wheels with the pedal press.

<!-- NEEDS REVIEW: "Spreizung" in chapter 02's "track variation max 1°" — this page's 1° is the
maximum right/left CASTOR difference ("Den Nachlauf kontrollieren … maximale Differenz von 1°").
The figures agree (1°); whether chapter 02's "Spreizung" item is the same check is not settled
here. -->

<a id="p255"></a>
**[PDF p.255]**

h) Bring the front axle to the **"half load"** position: fit the tool **T.Av. 56 A** between the
   upper wishbone and the side member.
i) Fit the modified measuring flags **T.Av. 481** and the home-made brackets (see the figure at
   the end of this section, PDF p.256). Alternatively, fit the support tube of the tool
   **T.Av. 246** with a strap under the floor pan at a distance of **1.30 m** from the centre of
   the front wheels.
j) Depending on the tool used, aim the pointer or the light beam at the additional cross on the
   measuring flag, then release the front axle so that the pointer or the light beam reaches
   the scale.
k) If the reading lies in the **hatched zone**, the steering height is correct.
l) If the reading lies outside the hatched zone, the position of the steering housing on the
   cross-member must be changed, either by elongating the mounting holes of the housing (with
   welded brackets) or by exchanging the brackets for ones with hole spacings of **55 – 56 or
   57 mm**, as the case may be.

Investigations on the production line have shown that it is generally necessary to raise the
steering housing on the **right-hand side** by exchanging the **55 mm** bracket for one with a
**56 mm** hole spacing.

> **NOTE:** if this work does not achieve the permitted tolerances for the toe change from half
> load to the unladen vehicle, the individual parts of the front axle must be checked with the
> checking gauge.

m) Finally, set the front-wheel toe **at half load**, and the toe distribution.

The page's lower figure (59209.1) shows the lower wishbone pivot with the castor-adjusting
eccentric bolt **(1)**.

![Front axle setting — T.Av. 56 A at half load with measuring flag, and lower wishbone eccentric (1) — PDF p.255](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0255-front-axle-setting-half-load.webp)

<a id="p256"></a>
**[PDF p.256]**

## Measuring flag (Renault 12) T.Av. 481 and home-made bracket

The page is a dimensioned drawing headed **"MESSFAHNE RENAULT 12"** (measuring flag), left
(**LINKS**) and right (**RECHTS**) flags, both marked **TAV 481**, plus a home-made bracket.

| Item | Value |
|---|---|
| Left flag — hatched zone (correct steering height) | between scale marks **9.5** and **10** |
| Left flag — scale numbers printed | 8, 10 (top); 9, 9.5, 11 (bottom) |
| Right flag — scale numbers printed | 10, 8 (top); 11, 9, 7 (bottom) |
| Height of the cross above datum line A | 60 |
| Bracket — screw | ⌀ 6 |
| Bracket — screw | ⌀ 10/125 (order no. 0855622200) |
| Bracket — ring diameter | ⌀ 20 |
| Bracket — length between centres | 200 |

**Front of vehicle.** This bracket is fitted to the **seat-belt anchorage point** (from below).

<!-- NEEDS REVIEW: SAFETY-RELEVANT. The hatched "correct" zone is clearly drawn on the LEFT flag
between 9.5 and 10, which AGREES with chapter 02's 1300 VC steering-box height "9.5 to 10". The
RIGHT flag's hatching is faint on the scan and appears to straddle the line between 10 and 9 —
its limits cannot be read reliably; use the image. The page does not print the 8-to-9 zone that
chapter 02 gives for the 1600 VD/VH, nor any angle offsets (+20' to +25' / +5' to +15'). The
right-hand edge of the page is cut off in the scan. -->

![Measuring flag T.Av. 481 (left/right) and home-made bracket — PDF p.256](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0256-measuring-flag-tav481.webp)

<a id="p257"></a>
**[PDF p.257]**

## Effects of bad front-axle settings

| Fault | Effects |
|---|---|
| Insufficient camber | Excessive wear of the inner tread of the tyre. Excessive load on the outer hub bearing. Unwanted pull towards the side of the wheel whose camber is insufficient. Poor road holding. |
| Excessive camber | Wear of the outer tread of the tyre. The vehicle pulls towards the side with the excessive camber. Excessive load on the inner hub bearing. Poor road holding. |
| Incorrectly set kingpin inclination | The effects combine with those of incorrectly set camber; the camber, however, varies in the opposite direction to the kingpin inclination. |
| Insufficient castor | The wheels return poorly and the steering becomes unsteady. The vehicle wanders. |
| Excessive castor | Excessive castor gives uncontrollable guidance of the wheels, which return beyond the straight-ahead position. Heavy steering and poor cornering. The vehicle wanders. |
| Excessive toe-in | Tyre wear on the outer tread. The vehicle weaves. |
| Insufficient toe-in | The effects are similar to those above, but the tyre wear is on the inner tread. |

<!-- NEEDS REVIEW: printed "Spreizung"; rendered "kingpin inclination" (steering-axis
inclination), its usual meaning. Chapter 02 renders the same word "track variation"; one of the
two renderings should be harmonized. -->

## Causes of incorrect front-axle settings

| Cause | Effect |
|---|---|
| Wear of the hub bearings and of the ball joints of the stub-axle carriers | Reduces the camber. |
| Wear of the wishbone mountings | Changes the castor and the camber. |
| A displaced spring | Affects the camber or the castor. |
| Bending of a wishbone, a stub-axle carrier arm or a rim | Changes the castor, the kingpin inclination, the camber. |
| Fatigue sag of the rear suspension | Increases the castor. |
| Very heavy loading of the vehicle | Changes the camber. |

<a id="p258"></a>
**[PDF p.258]**

## XI — Removing and refitting a front half-axle

### Removal

1. Slacken the wheel nuts.
2. Jack up the vehicle.
3. Remove the wheel.
4. Remove the brake caliper **without disconnecting the brake hose** (see [Brakes](16-brakes.md)).
5. Slacken the locknut **(2)**.
6. Remove the connecting pin **(3)** between the rack and the track rod.
7. Remove the rack end **(1)**.
8. Pull off the rubber boot **(4)**.
9. Remove the two nuts of the anti-roll bar mountings and slacken the nuts of the retaining
   bracket on the wishbone. Free the anti-roll bar from its mountings and remove it.
10. Remove the damper mountings, top and bottom. Remove the damper.
11. Fit the spring compressor **Sus.20**.
12. Remove the four securing nuts of the wishbone-pivot bearing blocks, the two flat washers (on
    the wheel side), the lock plate and the eccentric.

<a id="p259"></a>
**[PDF p.259]**

13. Slacken the Nylstop nuts of the ball joints by a few threads.
14. Fit the special tool **T.Av.55** between the ball-joint shanks.
15. Release the ball joints by holding the hexagon **(1)** with a **26 mm** open-ended spanner and
    turning the screw **(2)** with a **23 mm** open-ended spanner.
16. Remove the two Nylstop nuts.
17. Release the spring compressor and remove the stub-axle carrier.
18. Remove the spring compressor, the lower wishbone and the spring.
19. Unscrew the Nylstop nut of the wishbone pivot, turn the steering fully to the opposite lock
    and drive out the pivot. (For this purpose there is an opening in the pedal panel towards the
    interior of the car.)
20. Remove the upper wishbone.
21. Clean and check the parts.

### Refitting

1. Coat the upper wishbone pivot with graphite grease.
2. Offer the upper wishbone up to the cross-member.
3. Turn the steering fully to the opposite lock and insert the wishbone pivot.
4. Fit a new Nylstop nut and run it down, but do not lock it.

<!-- NEEDS REVIEW: "Nylstop" (Nylstopmutter) is kept as printed — a nylon-insert self-locking
nut. -->

<a id="p260"></a>
**[PDF p.260]**

5. Insert the spring with the lower wishbone into the upper seat.
6. Fit the spring compressor **Sus.20**.
7. Compress the spring compressor until the bearing blocks of the wishbone pivot rest against the
   cross-member.

> **NOTE:** the bearing blocks are secured on the outside (towards the wheel) by two bolts of
> **8 mm** diameter; on the inside the bolts are **8.5 mm** in diameter.

8. Coat the eccentric with graphite grease and fit it.
9. Fit the two flat washers on the two outer bolts (towards the wheel) and use a new lock plate.
10. Run on the four nuts **without locking them**.
11. Release the spring compressor and insert the stub-axle carrier onto the two ball joints of the
    upper and lower wishbones.
12. Fit two new Nylstop nuts and lock them at **9 mkg ± 1**.
13. Fit the anti-roll bar.
    - Tightening torque of the two Nylstop nuts of the centre mounting: **2.5 mkg ± 0.5**.
    - Tightening torque of the four Nylstop nuts on the lower-wishbone mounting brackets:
      **1.3 mkg ± 0.3**.
14. Fit the rack ends with their locknuts. Do not forget to fit the rubber boot first.
15. Attach the track rods to the rack ends with the pins, **without locking the nuts**.

> **NOTE:** after tightening, the pin in the track-rod end must lie **parallel to the upper edge
> of the side member**.

<!-- NEEDS REVIEW: the OCR reads the lower-wishbone bracket torque as "143 Oke = 0,3"; the image
shows 1.3 mkg ± 0.3 (restated identically on PDF p.264) — corrected from image. -->

<a id="p261"></a>
**[PDF p.261]**

16. Compress the spring and fit the T-piece **T.Av.56 A** of **78 mm** between the side member and
    the upper wishbone.
17. Slacken the spring compressor.
18. **Lock:** the Nylstop nuts of the **lower** wishbone pivot at **9 mkg ± 1**; make sure both
    nuts engage the same number of threads.
19. **Lock:** the Nylstop nut of the **upper** wishbone pivot at **6.5 mkg ± 1**.
20. Set the height of the steering ball pins.
21. **Lock:** the four nuts of the bearing blocks of the wishbone pivots at **3.5 mkg ± 1**. Bend
    the edge of the lock plate up against the hexagon of the eccentric.
22. Remove the T-piece **T.Av.56 A** and the spring compressor.
23. Fit the damper (shorter end of the lower mounting lug towards the inside). Tightening torque
    of the lower mounting: **3 mkg**.
24. Fit the brake caliper (see [Brakes](16-brakes.md)).
25. **Lock:** refit the T-piece **T.Av.56 A** and tighten the nut of the connecting pin between
    rack and track rod to **2.5 mkg ± 0.5**.
26. Tighten the locknut on the rack end, holding the connecting pin so that it is parallel to the
    upper edge of the side member.
27. Align the wheels and set the toe.

<!-- NEEDS REVIEW: (a) the "Blockieren" heading on the right of the page says only "Die
Nylstopmutter der unteren Querlenkerachse mit 6,5 mkg ± 1" — i.e. it prints LOWER wishbone pivot
at 6.5 mkg, directly after the left column has locked the lower wishbone pivot nuts at 9 mkg ± 1.
The replacement procedures on PDF pp.262-264 give UPPER wishbone pivot = 6.5 mkg ± 1 and LOWER
wishbone pivot = 9 mkg ± 1. Step 19 above is therefore rendered as the UPPER pivot; source as
printed reads "unteren" — probable source misprint, not OCR (the image is clear). SAFETY-RELEVANT.
(b) The column order on this page (left column, then right column, top half then bottom half) is
an interpretation of a two-column layout; the order of steps 18-21 and 22-27 follows the
page's reading order. (c) "T.Av.56 A von 78 mm" — 78 mm is the T-piece length that sets the
half-load position. -->

<a id="p262"></a>
**[PDF p.262]**

### Checking the front-axle data

a) The camber.
b) The kingpin inclination.
c) The castor (height of the ball pin).
d) The wheel alignment and the toe.

If the last two dimensions (c and d) are not correct, they must be readjusted.

## Replacing an upper wishbone

> **NOTE:** the upper wishbone was reinforced on the **1600 S** etc. by welding on a sheet-metal
> plate.

### Removal

1. Jack up the vehicle.
2. Remove the wheel concerned.
3. Remove the damper.
4. Fit the spring compressor **Sus.20**.
5. Compress the spring.
6. Remove the track rods at the steering output, and the rack ends.
7. Remove the dust boot.
8. Slacken the Nylstop nut on the upper ball joint by a few threads.
9. Fit the tool **T.Av.55** between the two ball-joint shanks.
10. Release the upper ball joint by holding the hexagon **(1)** with a **26 mm** open-ended
    spanner and turning the screw **(2)** with a **23 mm** open-ended spanner.
11. Remove the Nylstop nut.
12. Slacken the Nylstop nut of the upper wishbone pivot.
13. Turn the steering to the opposite lock and drive out the pivot.
14. Remove the upper wishbone.

<a id="p263"></a>
**[PDF p.263]**

### Refitting

1. Coat the upper wishbone pivot with graphite grease.
2. Offer the wishbone up to the cross-member.
3. Turn the steering to the opposite lock and insert the wishbone pivot.
4. Fit a new Nylstop nut **without locking it**.
5. Insert the stub-axle carrier onto the upper ball joint.
6. Fit a new Nylstop nut on the ball joint and lock it at **9 mkg ± 1**.
7. Fit the rubber boot.
8. Screw in the rack end with its locknut.
9. Attach the track rod to the rack, **but do not lock the pin nut**.
10. Compress the spring compressor. Fit the T-piece **T.Av.56 A** between the upper wishbone and
    the side member.
11. Slacken the spring compressor.
12. Lock the Nylstop nut of the upper wishbone pivot at **6.5 mkg ± 1**.

> **NOTE:** it is extremely important to check that the nuts of the wishbone pivots, the four
> nuts of the bearing blocks and the nut of the lower ball joint are locked.

Then proceed as for refitting a front half-axle.

## Replacing a lower wishbone

### Removal

1. Jack up the vehicle.
2. Remove the wheel concerned.
3. Release the anti-roll bar retaining brackets on the lower wishbone.
4. Remove the damper.
5. Fit the spring compressor **Sus.20**.
6. Remove the four nuts of the bearing blocks of the wishbone pivots, the two flat washers (wheel
   side), the lock plate and the eccentric.
7. Slacken the Nylstop nut of the lower ball joint a few threads.
8. Fit the special tool **T.Av.55** between the two ball joints.
9. Release the ball joint by holding the hexagon **(1)** with a **26 mm** open-ended spanner and
   turning the screw **(2)** with a **23 mm** spanner.

<a id="p264"></a>
**[PDF p.264]**

10. Remove the nut.
11. Release the spring.
12. Remove the spring compressor, the lower wishbone and the spring.

### Refitting

1. Insert the spring with the lower wishbone into the upper seat.
2. Fit the spring compressor **Sus.20**.
3. Compress the spring until the bearing blocks of the wishbone pivot rest against the
   cross-member.
4. Insert the ball joint into the stub-axle carrier.
5. Fit the greased eccentric, the two flat washers (on the securing bolts on the wheel side) and
   the new lock plate.
6. Run on the four nuts **without locking them**.
7. Fit a new Nylstop nut on the ball joint and lock it at **9 mkg ± 1**.
8. Fit the anti-roll bar retaining brackets to the lower wishbone. Torque: **1.3 mkg ± 0.3**.
9. Compress the spring compressor. Fit the T-piece **T.Av.56 A**.
10. Release the spring compressor.
11. Lock the two Nylstop nuts of the lower wishbone pivot at **9 mkg ±**. Make sure that both
    nuts engage the same number of threads.

<!-- NEEDS REVIEW: step 11 prints "9 mkg ±" with the tolerance figure missing on the page (the
image is clear; the number was never typed). PDF p.261 gives the same nuts as 9 mkg ± 1. Source
misprint, not OCR. -->

> **NOTE:** it is essential to check that the nut of the upper ball joint and of the upper
> wishbone pivot are properly locked.

Then proceed as for refitting a front half-axle.

<a id="p265"></a>
**[PDF p.265]**

## Replacing a front stub axle

### Removal

1. Jack up the vehicle.
2. Remove the wheel concerned.
3. Remove the brake caliper **without disconnecting the brake hose** (see [Brakes](16-brakes.md)).
4. Release the track rod at the ball joint with the extractor **T.Av.54**.
5. Remove the damper.
6. Fit the spring compressor **Sus.20**.
7. Slightly slacken the Nylstop nuts of the two ball joints.
8. Fit the special tool **T.Av.55** between the two ball joints.
9. Release the ball joints.
10. Unscrew the two nuts.
11. Remove the stub axle with brake disc and hub.
12. Dismantle the stub axle.

### Refitting

1. Assemble the backplate, brake disc and hub with the stub axle.
2. Offer up the assembly and insert the upper and lower ball joints.
3. Fit two new Nylstop nuts and tighten them to **9 mkg ±**.
4. Reattach the track rod, using a new nut, locked at **3.5 mkg ± 0.5**.
5. Fit the brake caliper (see [Brakes](16-brakes.md)).

> **NOTE:** you must check without fail that the nuts of the wishbone pivots and the four nuts of
> the bearing blocks are properly locked.

Then proceed as for refitting a front half-axle.

<!-- NEEDS REVIEW: step 3 prints "9 mkg ±" with no tolerance figure (as on PDF p.264); the
ball-joint nuts are 9 mkg ± 1 on PDF pp.260 and 263. Source misprint, not OCR. -->

<a id="p266"></a>
**[PDF p.266]**

## Dismantling and reassembling a front half-axle

### Lower wishbone

**Dismantling:**

1. Clamp one of the nuts of the wishbone pivot in a vice.
2. Slacken the other nut, drive out the pivot and catch the washers.
3. Remove the centring sleeve, the two bearing blocks and the bump-stop rubber.

**Reassembly:**

1. Coat the wishbone pivot with graphite grease.
2. Fit the bearing blocks, the spacer sleeve and the wishbone pivot.
3. Fit the two washers.
4. Fit two new Nylstop nuts (**do not lock them**).
5. Fit the bump-stop rubber.

For dismantling and reassembling the complete half-axle — stub axle, hub, brake disc, backplate —
see [Brakes](16-brakes.md).

<a id="p267"></a>
**[PDF p.267]**

## Overhauling a front half-axle

### a) Lower wishbones

Only the lower wishbones are fitted with **"flexibloc"** rubber bushes.

**Dismantling:** press out the rubber bushes using the mandrel **(C)** of the tool **T.Av.28** and
a piece of tube **(E)**.

**Reassembly:** rub the bore in the wishbone with tallow and press in the new rubber bushes up to
the protruding ring, using a tube **(A)** of **38 mm** inside diameter.

> **NOTE:** use a tube **(E)** as a support.

### b) Upper wishbones

Only the upper wishbones are fitted with **"fluidbloc"** rubber bushes.

**Dismantling:** press out the rubber bushes with the press, using the mandrel **(D)** of the tool
**T.Av.21**. Place a spacer between the mandrel and the press ram.

**Reassembly:** coat the bore in the wishbone with tallow and press in the new rubber bushes up to
the protruding ring, using the mandrel **(D)** of the tool **T.Av.21**.

> **NOTE:** support on the tube **(E)**.

<!-- NEEDS REVIEW: the OCR reads the tool numbers as "TsAv.23" and "T.Av.2%"; the image shows
T.Av.28 (lower wishbone) and T.Av.21 (upper wishbone) — corrected from image. The upper-wishbone
reassembly figure labels the parts (B) and (E), not (D), although the text names mandrel (D). -->

<a id="p268"></a>
**[PDF p.268]**

## Replacing the two suspension ball joints on a half-axle

> The ball-joint housings are **riveted and cannot be opened**. All ball joints with abnormal
> play must be replaced as a matter of course.

Release the ball joints with the special tool **T.Av.55 A**.

### Removal

1. Drill out the securing rivets with a **5.5 mm** drill.
2. Knock off the rivet heads with a chisel.
3. Clean the seat of the ball joint on the wishbone.

### Fitting

Offer the new ball joint up to the wishbone and secure it with the **three bolts and nuts
supplied by the parts department**.

**Tightening torque: 0.6 mkg +0.1 / +0.0 (5 lb/ft).**

<!-- NEEDS REVIEW: printed "0,6 mkg +0,1 +0,0 (5 lb/ft)" — tolerance stacked as +0.1 / +0.0, i.e.
0.6 to 0.7 mkg. The printed "(5 lb/ft)" is reproduced as printed and not checked against the
mkg value (strictly 0.6 mkg ≈ 4.3 lb·ft). The OCR rendered the tolerance as "+0,19 / +0,0";
the image shows +0.1 — corrected from image. -->

<a id="p269"></a>
**[PDF p.269]**

## Front hub and wheel bearings

The front wheel hub runs on **taper roller bearings**.

### Removing a hub

> **NOTE:** the shape of the backplate makes it impossible to remove the hub on its own.

Removal is carried out as follows:

1. Remove the brake caliper **without disconnecting the brake hose** (see [Brakes](16-brakes.md)).
2. Remove the hub together with the brake disc and the backplate.

The hub is removed in the same way as the brake disc.

### Replacing the wheel bearings

> When replacing the wheel bearings, the bearing **outer races must also be renewed** without
> fail.

To remove the inner bearing, use the extractor **B.Vi.28** with the claws **B.Vi.48** and a thrust
piece of **16 mm ⌀**.

> **NOTE:** after every removal of the inner bearing, the oil deflector **(A)** and the seal **(B)**
> must be renewed.

The bearing outer races are pressed in with the press.

### Adjusting the wheel bearings

1. After checking that the wheel bearings are in good condition, tighten the hub nut while turning
   the wheel at the same time, until the wheel begins to turn stiffly.
2. **Slacken the hub nut by 1/6 of a turn and split-pin it.**
3. Strike the end of the stub axle with a copper hammer so that the parts "settle", then fit the
   hub cap filled **3/4** with grease.

**Maximum play: 0.35 mm**, read with a dial gauge on the rim **200 mm** from the axle centre.

<!-- NEEDS REVIEW: SAFETY-RELEVANT. No hub-nut torque figure is printed — the bearing is set by
the tighten-until-stiff, back-off-1/6-turn method above. 0.35 mm, 1/6 and 200 mm were all
checked against a high-resolution crop. -->

![Front hub on taper roller bearings, inner-bearing extraction with B.Vi.28 / B.Vi.48 — PDF p.269](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-a110-reparaturhandbuch/p0269-front-hub-bearings.webp)

## Special tools used in this chapter

| Tool | Use |
|---|---|
| FACOM U-70 / BEM optical gauge | Front-axle alignment |
| Dir. 326 | Setting the steering centre point |
| T.Av. 34 | Clamping tool — locking the steering at its centre point |
| T.Av. 56 A | T-piece (78 mm) — half-load position of the front axle |
| T.Av. 481 | Measuring flags (modified), steering-height check |
| T.Av. 246 | Support tube for the alignment check |
| Sus.20 | Spring compressor |
| T.Av.54 | Track-rod ball-joint extractor |
| T.Av.55 / T.Av.55 A | Ball-joint release tool |
| T.Av.28 | Mandrel (C) — lower-wishbone "flexibloc" bushes |
| T.Av.21 | Mandrel (D) — upper-wishbone "fluidbloc" bushes |
| B.Vi.28 + B.Vi.48 | Extractor and claws — inner wheel bearing |

## Next

[Rear axle (all types)](14-rear-axle.md).
