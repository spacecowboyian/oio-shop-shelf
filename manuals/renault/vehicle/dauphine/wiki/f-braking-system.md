# Braking System

<!--
Source: Renault Dauphine Workshop Manual M.R.93 (English edition, November 1964), Chapter F
"Braking System" (Renault §93). Source PDF pages 248–268.

Page-mapping note: PDF p.248 is the chapter title + Contents leaf (bears no printed "F-n" number).
Numbered content runs continuously from printed F-3 = PDF p.249 to printed F-22 = PDF p.268, a
constant offset of +246 with no drift (printed F-N = PDF p.(N+246)). Citations below give the PDF
page (matches pNNNN.png) and the printed F-page. No duplicate, abridged, or foreign (misfiled)
pages were found in the range.

Chapter scope: floating-shoe hydraulic drum brakes on all four wheels (one wheel cylinder per
wheel), a pedal-operated master cylinder, and — from October 1960 / the 1961 models — a rear brake
pressure limiting valve. Covered for vehicle types R1090, R1091 and R1093. The chapter gives the
description, specifications, general repair instructions, tightening torques, a table of production
modifications, an operating-incidents (fault) chart, master-cylinder overhaul (old and new types),
master-cylinder clearance adjustment, brake-pedal / wheel-cylinder / hose / shoe removal-refitting,
shoe and hand-brake adjustment, the pressure-limiting-valve check, and pedal bleeding.

Content verification: SAFETY-CRITICAL chapter — every drum/lining/cylinder-bore dimension, shoe and
pedal clearance, brake-fluid spec, tightening torque, and limiter/residual pressure was cross-checked
against the rendered page image. Notable OCR corrections made from the image: the pressure-limiting-
valve setting (F-4) reads 50 +0/−8 kg/sqcm, not the OCR "50 * 5"; the system capacity (F-3) is
0.23 litres (½ pint); the R1091 front-lining widths and wheel-cylinder date-splits (F-4) and the
F-6 modifications table were rebuilt cell-by-cell from the image.
-->

<!-- PDF p.248 · chapter title & Contents -->

## Contents of chapter

Page numbers are the printed **F-n** pages.

| Section | Page |
| ------- | ---- |
| I — Description | F-3 |
| II — Specifications | F-4 |
| III — General repair instructions | F-5 |
| IV — Tightening torques | F-5 |
| V — Table of various braking system modifications | F-6 |
| VI — Operating incidents | F-7 |
| VII — Master cylinder (old and new): 1. Principles of operation | F-8 |
| VII — Master cylinder: 2. Removing, overhauling, refitting (interchangeability, identification) | F-9 |
| VIII — Adjusting the master cylinder clearance | F-12 |
| IX — Brake pedal: Removing, refitting | F-13 |
| X — Removing and refitting a wheel cylinder (front or rear) | F-14 |
| XI — Overhauling a wheel cylinder | F-15 |
| XII — Removing and refitting the brake hoses | F-15 |
| XIII — Removing and refitting the brake shoes (front or rear) | F-17 |
| XIV — Adjusting the brake shoes | F-18 |
| XV — Hand brake: Replacing ratchet and quadrant / lever / cable | F-19 |
| XVI — Adjusting the hand brake control | F-20 |
| XVII — Brake pressure limiting valve: Principles of operation / Checking | F-21 |
| XVIII — Bleeding the braking system (by means of the pedal) | F-22 |

---

## I — Description

<!-- PDF p.249 · F-3 -->

![Brake system layout on the vehicle (reservoir, master cylinder, rigid and flexible lines to all four wheels) — PDF p.249](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0249-brake-system-layout.webp)

- Floating-shoe hydraulically operated brakes.
- Mechanical hand brake operating on the rear wheels.
- **System capacity: 0.23 litres (½ pint).** <!-- NEEDS REVIEW: OCR read "$ pint"; page image clearly shows "½ pint" — corrected from image -->

The hydraulic part of the system consists of:

- a fluid reservoir bottle which is higher than the master cylinder;
- a master cylinder operated by the pedal;
- rigid and flexible brake lines;
- one wheel cylinder per wheel;
- a brake pressure limiting valve (from the 1961 models onwards).

This assembly permits a simultaneous load to be applied to the four wheels, and this ensures that
braking is evenly distributed.

The actual braking effect is obtained by friction between:

- a drum which is integral with the wheel;
- two lined shoes secured to the brake anchor plate.

---

## II — Specifications

<!-- PDF p.250 · F-4 -->

### R 1090

| Item | Dimension |
| ---- | --------- |
| Master cylinder inside diameter | 22 mm (.867") |
| Front wheel cylinder inside diameter | 22 mm (.867") |
| Rear wheel cylinder inside diameter | 19 mm (.749") |
| Front and rear drum diameter | 228.5 mm (9") |
| Width of front brake linings | 30 mm (1 3/16") |
| Width of front brake linings (from the 1961 model onwards) | 35 mm (1 13/32") |
| Width of rear brake linings | 30 mm (1 3/16") |
| Length of front and rear leading linings | 250 mm (9 7/8") |
| Length of front and rear trailing linings | 195 mm (7 11/16") |
| Front and rear lining chamfer | 8 mm (21/64") |
| Brake pressure limiting valve | 50 +0/−8 kg/sqcm (from 1961 models onwards) (600 psi to 715 psi) |

<!-- NEEDS REVIEW: brake pressure limiting valve — OCR read "50 * 5 ke/saom"; page image clearly shows "50 +0/−8 kg/sqcm" (superscript +0, subscript −8), i.e. a 42–50 kg/sqcm range = 600–715 psi — corrected from image (SAFETY-CRITICAL) -->

### R 1091

**Diameters:**

| Item | Dimension |
| ---- | --------- |
| Master cylinder inside | 22 mm (.867") |
| Front wheel cylinder inside — up to September 1959 | 22 mm (.867") |
| Front wheel cylinder inside — from October 1959 to September 1960 | 23.8 mm (.938") |
| Front wheel cylinder inside — from October 1960 onwards | 22 mm (.867") |
| Rear wheel cylinder inside | 19 mm (.749") |
| Front and rear drum | 228.5 mm (9") |
| Brake pressure limiting valve | 50 +0/−8 kg/sqcm (from 1961 models onwards) (600 psi to 715 psi) |

<!-- NEEDS REVIEW: brake pressure limiting valve — OCR read "50 * 5"; page image shows "50 +0/−8 kg/sqcm" — corrected from image (SAFETY-CRITICAL). "Up to September 1959" OCR read "September Llyoy" — corrected from image -->

**Linings:**

| Item | Dimension |
| ---- | --------- |
| Width of front linings — up to September 1959 | 30 mm (1 3/16") |
| Width of front linings — from October 1959 | 35 mm (1 13/32") |
| Width of rear linings | 30 mm (1 3/16") |
| Length of front and rear leading linings | 250 mm (9 7/8") |
| Length of front and rear trailing linings | 195 mm (7 11/16") |
| Front and rear lead chamfer | 8 mm (21/64") |

### R 1093

The specifications are identical to those of the R 1091. However, the R 1093 was fitted with front
drums which had external cooling fins.

---

## III — General repair instructions

<!-- PDF p.251 · F-5 -->

### Brake fluids

R1090 and R1091 models had the following brake fluids in their braking systems on initial assembly:

1. Up to July 1960: Lockheed No. 5 fluid (no identification).
2. From July 1960 onwards, the following fluids: Stop HD 65 — Lockheed HD 31 — Frelub HD.

These three fluids can be inter-mixed and are identified by a sticker applied to the fluid reservoir
cap (Stop HD 65) or a cap on which is marked "Use only fluids which conform to standard S.A.E. 70 R.1".

> **IMPORTANT:** These three fluids should not be mixed with Lockheed No. 5. If there is any doubt,
> drain the braking system, flush it out and dry with compressed air. Refill with one of the three HD
> fluids. Replace the cap by one which is marked with the inscription "Use only fluids which conform
> to standard S.A.E. 70 R.1".

### Cleanliness and inspection

In no circumstances should the fluid contain any dirt or air bubbles. To ensure that it does not:

- Dry brush the parts before disconnecting anything.
- Plug the disconnected lines with a plug.
- Clean the parts with industrial methylated spirits (denatured alcohol) only.
- Bleed the lines after reconnecting.
- Check the thickness of the copper washer, which should not have reduced by more than **0.2 to
  0.3 mm (.008" to .012")**.

New linings must be identical as regards both grade and dimensions. They should have no trace of
grease or fluid on them (do not touch them with dirty fingers).

The drums should be of good surface finish, clean and dry. **Maximum diameter after regrinding:
229.2 mm (9.023").**

> To obtain efficient braking, the drums must be re-worked when the linings are replaced. This
> operation must be carried out on both the drums on any given axle at a time.

---

## IV — Tightening torques

<!-- PDF p.251 · F-5 -->

| Fastener | Torque |
| -------- | ------ |
| Hose to wheel cylinder attachment point | 2 m.kg (15 lbs/ft) |
| Pipe unions — external diameter 4.7 mm (.186") (taper union) | 1 m.kg (10 lbs/ft) |
| Pipe unions — external diameter 6.4 mm (.252") (taper union) | 2 m.kg (15 lbs/ft) |
| Stop switch on master cylinder (taper union) | 4 m.kg (30 lbs/ft) |
| Straight union on master cylinder | 4 m.kg (30 lbs/ft) |
| Stop switch operating pressure | 8 to 10 kg/sqcm (115 psi to 145 psi) |

---

## V — Table of various braking system modifications

<!-- PDF p.252 · F-6 -->

Column headings give the vehicle type and the production period as printed in the source table.

| | R1090 (Mar 1956–Sept 1958) | R1090 / R1091 (Oct 1958–Sept 1959) | R1090 (Oct 1959–Sept 1960) | R1091 (Oct 1959–Sept 1960) | R1090 (from Oct 1960) | R1091 (from Oct 1960) |
| --- | --- | --- | --- | --- | --- | --- |
| **FRONT** — Width of linings fitted in production | 30 mm (1 3/16") | 30 mm (1 3/16") | 30 mm (1 3/16") | 30 mm (1 3/16") | 35 mm (1 13/32") | 35 mm (1 13/32") |
| **FRONT** — Diameter of wheel cylinders | 22 mm (.867") | 22 mm (.867") | 23.8 mm (.938") | 23.8 mm (.938") | 22 mm (.867") | 22 mm (.867") |
| **FRONT** — Fixed point: Straight | O | O | O | | | |
| **FRONT** — Fixed point: Inclined | | | | O | O | O |
| **REAR** — Width of linings fitted in production | 30 mm (1 3/16") | 30 mm (1 3/16") | 30 mm (1 3/16") | 30 mm (1 3/16") | 30 mm (1 3/16") | 30 mm (1 3/16") |
| **REAR** — Diameter of wheel cylinders | 19 mm (.749") | 19 mm (.749") | 19 mm (.749") | 19 mm (.749") | 19 mm (.749") | 19 mm (.749") |
| **REAR** — Fixed point: Straight | O | O | O | | | |
| **REAR** — Fixed point: Inclined | | | | O | O | O |
| **With pressure limiting valve** | | | | | O | O |

<!-- NEEDS REVIEW: F-6 table has merged/spanned cells in the source; the merged production-period values were expanded across the six vehicle columns as read from the page image. "O" marks the option fitted for that column. -->

The two front-shoe designs differ in their anchor ("fixed point"):

![Straight fixed point vs. inclined fixed point front shoes — PDF p.252](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0252-fixed-point-shoes.webp)

---

## VI — Operating incidents

<!-- PDF p.253 · F-7 -->

| Incident | Causes | Remedy |
| -------- | ------ | ------ |
| Spongy pedal and inefficient braking. | Air in the brake lines. | Bleed the system. |
| Excessive brake pedal travel. Travel reduced by pumping the pedal. | Excessive clearance between linings and drums. Hoses swelling. | Adjust the shoes. Replace the hoses. |
| Rapid fall in the fluid level in the reservoir bottle. | Leakage at the rear of the master cylinder. Leakage from the brake lines. | Overhaul the master cylinder. Retighten or replace the hoses. |
| Brakes overheating and not returning. | Insufficient brake pedal free travel. Incorrectly adjusted handbrake. Brake shoe return springs weak. | Adjust the free travel. Adjust the hand brake. Replace the springs. |
| Uneven braking. | Greasy linings or of different grades. Oval drums. Swollen cup washers. Wheel cylinders sticking. Partial blockage of brake lines. | Clean or replace the linings. Rework or replace the drums. Replace the cup washers. Replace the wheel cylinders. Replace the lines. |
| Wheels locking as soon as the brakes are applied. | Linings incorrectly chamfered. | Chamfer the linings. |

---

## VII — Master cylinder

### 1. Principles of operation

#### Master cylinders on R1090 – R1091 vehicles produced before the end of May 1959

<!-- PDF p.254 · F-8 -->

![Master cylinder (pre-May 1959 type) — sectional operating diagram, positions A/B/C — PDF p.254](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0254-master-cylinder-old-operation.webp)

- **A — At rest position:** The reservoir connection orifice is uncovered. There is a clearance (K)
  between the piston and the thrust rod. The valve is held closed by spring (6).
- **B — Applied position:** The main cup washer moves forward and blocks off the inlet orifice and
  pushes fluid into the lines by opening the valve.
- **C — Brake release position:** The shoe return springs push back the fluid from the wheel
  cylinders to the master cylinder. The fluid compresses the spring and the valve allows the fluid
  to flow through.

#### Master cylinder fitted since the end of May 1959

<!-- PDF p.255 · F-9 -->

![Master cylinder (post-May 1959 type) — sectional operating diagram, positions A/B/C — PDF p.255](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0255-master-cylinder-new-operation.webp)

Since the end of May 1959, R1090 – R1091 vehicles have been equipped in production with a new master
cylinder identical to that used in the R1093. This differs from the one formerly fitted by:

- the master cylinder body;
- the valve;
- the piston;
- the secondary cup washer;
- the snap ring;
- the thrust rod (the **17 mm lock nut** has been replaced by a **14 mm lock nut**).

The operating principles are identical to those on the master cylinder fitted before the end of May
1959.

### 2. Removing, overhauling and refitting the master cylinder

#### a) Removing

<!-- PDF p.255 · F-9 -->

1. Disconnect the battery.
2. Remove the spare wheel and the front undertray.
3. Mark and disconnect the stop switch leads.
4. Block the reservoir bottle outlet with a plug.
5. Disconnect the pipe which carries the fluid to the master cylinder.
6. Remove the stop switch (put aside the seal).
7. Remove the master cylinder securing bolts on the pedal assembly bracket and free it in a forward
   direction.

#### b) Overhauling

<!-- PDF p.256 · F-10 -->

**Master cylinder type fitted before the end of May 1959:**

![Master cylinder (pre-May 1959 type) — exploded view, parts 1–8 — PDF p.256](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0256-master-cylinder-old-exploded.webp)

Dismantle the master cylinder. Clean the parts in methylated spirits (denatured alcohol). Check them
and replace all parts that show any signs of wear with new genuine spare parts which are free from
defects. Soak the parts in brake fluid which conforms to standard **SAE 70 R.1** and fit, in the
following order:

1. the thrust washer (1);
2. the valve (2) and its spring (3);
3. the main cup washer (4) with its flat end towards the piston;
4. the piston (5) fitted with the auxiliary cup washer (6);
5. the washer (7).

Hold them all together and fit circlip (8). Ensure that all the parts slide freely.

<!-- PDF p.257 · F-11 -->

**Master cylinder fitted after the end of May 1959:**

![Master cylinder (post-May 1959 type) — exploded view, parts 1–7, and cast-boss identification — PDF p.257](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0257-master-cylinder-new-exploded.webp)

Dismantle the master cylinder. Clean all the parts with methylated spirits (denatured alcohol). Check
them and replace any parts showing signs of wear by new genuine spare parts free of any defect. Soak
the parts in brake fluid which conforms to standard **SAE 70 R.1** and fit in the following order:

1. the valve together with its seal (7);
2. the spring (6);
3. the main cup washer (5) with its flat side towards the piston;
4. the piston (4) fitted with the secondary cup washer (3);
5. the washer (2).

Hold them all together and fit snap ring (1). Ensure that all the parts slide freely.

#### c) Interchangeability

One can fit to the old type master cylinder the following: spring (6), main cup washer (5),
piston (4), secondary cup washer (3), and washer (2).

> **IMPORTANT:** Under no circumstances should one fit the new valve to the old type master cylinder
> or the old valve to the new type master cylinder.

#### d) Identification

A cast boss on the new master cylinder permits one to identify it without carrying out any
dismantling operation.

#### e) Refitting

Carry out the removing operations in reverse. Bleed the braking system. Adjust the master cylinder
clearance. Check the master cylinder for leaks.

---

## VIII — Adjusting the master cylinder clearance

<!-- PDF p.258 · F-12 -->

![Adjusting the master cylinder clearance — pedal free movement G and clearance K, thrust-rod adjustment — PDF p.258](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0258-master-cylinder-clearance.webp)

This is adjusted by means of the master cylinder thrust rod.

- The clearance K is taken up by a brake pedal movement **G = 5 mm (13/64")**.
- The system is pressurised by a total brake pedal movement of **20 mm (51/64")**.

Adjust the clearance by turning the thrust rod using adjusting spanner:

- **(Fre.02) (A)** for master cylinders produced before the end of May 1959;
- **(Fre.07) (B)** for master cylinders produced after the end of May 1959.

Tighten the lock nut (shown by the arrow).

---

## IX — Brake pedal

### Removing and refitting the brake pedal

#### Models before 1958

<!-- PDF p.259 · F-13 -->

**Removing:**

1. Disconnect the battery.
2. Plug the brake fluid reservoir bottle outlet.
3. Unhook the return springs of the three pedals from the body.
4. Disconnect the accelerator and clutch cables from their pedals.
5. Disconnect the master cylinder inlet.
6. Disconnect the stop switch and remove it.
7. Remove the pedal shaft bolt and pull back the shaft to free it from the side member.
8. Remove the bolts which secure the pedal bracket to the side member.
9. Remove the pedal assembly, freeing the pedal grommets.
10. Pull out the shaft and put aside the spacer washers.

**Refitting:**

Carry out the removing operations in reverse, then:

- Bleed the brakes.
- Adjust the brake and clutch pedal clearances.

#### 1958 Model

<!-- PDF p.260 · F-14 -->

![1958-model pedal assembly — exploded view — PDF p.260](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0260-pedal-assembly-1958.webp)

**Removing:** This operation involves removing the pedal assembly.

1. Remove the under tray.
2. Unhook the brake pedal return spring.
3. Unpin the shaft which connects the pedal to the master cylinder thrust rod. Take out the shaft and
   put aside the return spring securing lug.
4. Remove the pedal shaft securing bolt.
5. Remove the pedal shaft and put aside the spacing washers.

Inside the vehicle:

6. Lift the floor mat and remove the sheet metal screws which secure the sound proofing cards.
7. Remove the pedal assembly cover and then take out the pedals.

**Refitting:** Carry out the removing operations in reverse and then check the clutch and brake pedal
clearances.

---

## X — Removing and refitting a wheel cylinder (front or rear)

<!-- PDF p.260 · F-14 -->

**Removing:**

1. Pull back the shoes from the drums.
2. Remove the "hub – drum" assembly.
3. Remove the shoes and disconnect the hose union (block one end with a plug).
4. Remove the two cylinder securing bolts and take off the cylinder.

**Refitting:** Carry out the removing operations in reverse and bleed and adjust the braking system.

---

## XI — Overhauling a wheel cylinder

<!-- PDF p.261 · F-15 -->

1. Dismantle the cylinder.
2. Inspect the parts. If the cylinder bore finish is not smooth, or if it is oval, it is not to be
   reworked but must be replaced.

The rubber parts must be genuine spare parts and free from any defect.

When reassembling:

- Screw in the bleed screw and fit its cap.
- Smear the sliding parts with brake fluid which conforms to standard **SAE 70 R.1**.
- Refit the cup washers, the pistons and the protective caps.
- Ensure that all the parts slide freely. Hold the assembly together by means of clip (Fre.05 A).

> **IMPORTANT:** The wheel cylinders which are **19 mm (.749")** in diameter are fitted at the rear.

---

## XII — Removing and refitting the brake hoses

<!-- PDF p.261 · F-15 -->

**Removing:**

1. Remove the clip which secures the hose to its bracket using a pair of pliers.
2. Disconnect the hose from the wheel cylinder.

**Refitting:**

The two hoses (right and left hand) which connect the front wheel cylinders to the rigid brake piping
should be fitted with an initial twist which is identical to that which existed before they were
dismantled. If this precaution is not taken, it is possible for the hoses to make contact with the
upper suspension arm or the steering link when the suspension is at its maximum travel. To avoid this,
the hoses are to be twisted before they are connected to the brackets provided for this purpose.

This bracket has a 12-sided hole in it into which the hose union hexagon is fitted. The hose is to be
twisted in the following manner:

1. Connect the hose to the wheel cylinder.
2. Position the hexagon on its union opposite the bracket.
3. Place the hexagon on the hose in the 12-sided aperture in the bracket without twisting it.
4. Connect the rigid brake line, engaging only 4 or 5 threads whilst holding the hexagon in its
   location.

<!-- PDF p.262 · F-16 -->

5. Mark a line on the hexagon and continue this line onto the bracket.
6. Free the hexagon and re-engage it into the location on the bracket, moving the line on the hexagon
   forward through two notches on the location with respect to the line on the bracket.

The forward direction is considered as:

- Clockwise on the left hand side.
- Anti-clockwise on the right hand side.

7. Fit the clip which secures the hose to its bracket.
8. Finally tighten the rigid line to the hose.

> **NOTE:** Bleed the braking system after any operation carried out on the brake lines.

> **IMPORTANT:** The rear hoses are not to be twisted.

---

## XIII — Removing and refitting the brake shoes (front or rear)

<!-- PDF p.263 · F-17 -->

![Brake shoe assembly on the anchor plate — leading (C) and trailing (T) shoes, return-spring layouts — PDF p.263](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0263-brake-shoes.webp)

**Removing:**

1. Pull back the shoes from the drum.
2. Remove the hub.
3. Fit clip (Fre.05 A) to the wheel cylinder.
4. Remove the upper return spring (at the rear, unhook the hand brake cable) using tongs (Fre.03) and
   lining protector (Fre.06).
5. Remove the clips and pull the shoes apart (at the rear, put aside the hand brake link).
6. Remove the shoes and separate them from the lower return spring.

**Refitting:**

> **NOTE:** Relining the shoes or reworking the linings is not advisable. Carry out a standard service
> exchange of the shoes.
> - Relined shoes should be fitted to both wheels on any given axle at the same time.
> - Replacing a short spring by a long spring must be carried out on all four anchor plates.

Carry out the removing operations in reverse. The shoe fitted with the longest lining (C) is fitted
at the front and that with the shortest lining (T) at the rear. Do not omit to cover the clips on the
outer side with sealing compound (hermetical, Bostik adhesive, or better still, GT 105 compound
produced by "Rector"). After refitting, bleed the braking system.

---

## XIV — Adjusting the brake shoes

<!-- PDF p.264 · F-18 -->

![Adjusting the brake shoes — leading square (C) and trailing square (T) on the anchor plate — PDF p.264](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0264-brake-shoe-adjustment.webp)

This consists of bringing each shoe nearer to the drum (therefore two operations per wheel). Pull
back the shoes from the drum as far as they will go.

1. Always start by adjusting the leading shoe, turning square (C).
2. Turn the wheel in the "forward" direction, ensuring that it turns freely.
3. Turn square (C) slowly in the direction shown by the arrow to bring the shoe nearer to the drum,
   until the drum is felt to be rubbing against the shoe. Apply the brakes a few times so that the
   shoe positions itself.
4. Then turn back square (C) slightly until the wheel turns freely.
5. Then turn the wheel in the "reverse" direction and repeat these operations on square (T), to bring
   the trailing shoe nearer to the drum; turn the square in the direction shown by the arrow.
   (Brake spanner (wrench) Fre.01.)

---

## XV — Hand brake

<!-- PDF p.265 · F-19 -->

![Hand brake — ratchet, quadrant and lever exploded view — PDF p.265](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0265-hand-brake-exploded.webp)

### Replacing the ratchet and quadrant

1. Remove screw (1) which retains the quadrant.
2. Press on ratchet (2) and free quadrant (3).
3. Release and put aside the plunger and the ratchet. Replace any defective parts.
4. Re-assemble by carrying out these operations in reverse.
5. Adjust the hand brake.

### Replacing the lever

1. Fit the spring (7) and thrust washer (6) and the ratchet (2) into the lever (8).
2. Engage quadrant (3) into its location in the lever (8) by pressing on the plunger.
3. Secure the quadrant to its bracket (4).
4. Refit the lever pivot pin (5).
5. Reconnect the link which connects it to the swivel lever.
6. Reconnect the connecting link to the lever and split pin it.
7. Adjust the hand brake.

### Replacing the cable

1. Fit the cable to the swivel lever and hook its ends to the brake levers in the drums.
2. Place the cable cover end stops on the flanges.
3. Hook the cable covers to the swivel lever.
4. Refit the hubs and adjust the brake shoes and hand brake.

---

## XVI — Adjusting the hand brake control

<!-- PDF p.266 · F-20 -->

This is to be adjusted only after adjusting the foot brake.

1. Lift the rear of the vehicle, release the hand brake and place the gear box in the neutral position.
2. Loosen the sleeve nuts and turn the sleeve to adjust the cable tension.
3. Ensure that the wheels turn freely. The lever should start to apply the brake after **three notches
   on the quadrant**.
4. Tighten the nuts.

---

## XVII — Brake pressure limiting valve

<!-- PDF p.266 · F-20 -->

From October 1960 onwards, R1090 and R1091 vehicles have been fitted with a brake pressure limiting
valve as fitted to the R1093. This valve is mounted on the rear suspension cross member and replaces
the former "T" union. Its function is to limit the maximum pressure reaching the rear wheels and thus
ensure that when the brakes are violently applied the best possible brake distribution is obtained on
the two axles.

> **IMPORTANT:** The fitting of a brake pressure distributor to models previous to October 1960 is
> ABSOLUTELY FORBIDDEN.

### Principles of operation

<!-- PDF p.267 · F-21 -->

![Brake pressure limiting valve — sectional operation (A: normal braking; B: violent braking) and pressure-gauge checking set-up — PDF p.267](https://github.com/spacecowboyian/oio-shop-shelf/releases/download/manuals-dauphine/p0267-limiting-valve.webp)

- **A — Normal braking when slowing down.** Under these circumstances the pressure limiting valve
  does not operate and fluid passes freely to the rear wheels.
- **B — Violent braking.** Pressures in the system can become high (approximately **70 kg/sqcm**
  (1,000 p.s.i.)). In these circumstances, the distributor comes into operation (owing to the piston
  movement) and limits the pressure reaching the rear wheels (below **50 kg/sqcm** (715 p.s.i.)),
  thus distributing the braking effect over the two axles.

### Checking

Connect a pressure gauge (the ARU 50 type M.2 Testometer, for example) into the tapping normally
occupied by the rear wheel cylinder bleed screw. Bleed the pressure gauge by means of bleed screw (1).

1. Slowly depress the brake pedal and check on the high pressure (A) that the pressure remains lower
   than **50 kg/sqcm (715 p.s.i.)**.
2. Release the pedal and read the residual pressure on the low pressure gauge (B). This should not be
   greater than **1.6 kg/sqcm (25 p.s.i.)**.

> **NOTE:** Any brake fluid on the outside of the brake pressure limiting valve shows that it is
> damaged, even if the above tests have proved satisfactory.

In all circumstances where the valve operates incorrectly or has traces of oil on it, it is to be
replaced.

### Road test

Road tests are only to be carried out on vehicles on which the linings have been run in. (The linings
fitted in production are hard and require a running-in period of approximately **1,000 km (600
miles)**.)

<!-- NEEDS REVIEW: checking-gauge type OCR read "ARU 50 type M.2 Testometer" — verify designation ("ARU"/"ARC" and unit name) against the page image; the two check pressures (50 kg/sqcm max high pressure; 1.6 kg/sqcm max residual) were confirmed from the F-21 image (SAFETY-CRITICAL) -->

---

## XVIII — Bleeding the braking system (by means of the pedal)

<!-- PDF p.268 · F-22 -->

This operation is carried out at the wheel cylinders on each wheel. Before bleeding, check the pedal
clearance and the fluid level in the brake reservoir bottle. Start the bleeding operation at the wheel
cylinder the farthest from the master cylinder, and finish it at the nearest.

On each cylinder:

1. Remove the cap and fit the spanner (wrench) and the bleed pipe.
2. Immerse the free end of the pipe in a transparent recipient containing a little brake fluid to
   standard **SAE 70 R.1**.
3. Unscrew the bleed screw by a quarter turn.
4. Have the brake pedal operated by an assistant, slowly through its full travel until there are no
   longer any air bubbles in the fluid flowing from the pipe.
5. Close the bleed screw each time the pedal reaches the end of its travel.
6. Remove the pipe and the spanner. Refit the cap.

After bleeding each cylinder, top up the level of the fluid in the reservoir bottle, using a fluid
which conforms to standard **SAE 70 R.1**. Adjust the brakes.
