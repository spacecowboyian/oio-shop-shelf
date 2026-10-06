# Review-flag triage — Alpine A110

A pass over this manual's `NEEDS REVIEW` flags to turn an undifferentiated pile of 108 into
a ranked worklist. Run with [TypeSafe](https://typesafe.ai)'s **Jev** System One model.

## What the model was and was not allowed to do

**Jev classified the flags. It did not decide, supply or confirm a single value.**

Rule 0 of `scripts/04_cleanup_methodology.md` — never silently change a number — is exactly
the thing a judgment model must not be pointed at here. So the model answered questions
*about* each note (does it leave anything undecided? would guessing be dangerous? would it
block a job? what is the next step?) and all the thresholds and verdicts live in code, not
in the model's head. Where a "proposed fix" appears below it is a **recommended next action**,
never a proposed number.

Every flag the pass closed was then read by hand before it was closed.

## Result

| | Before | After |
| --- | --- | --- |
| Open `NEEDS REVIEW` flags | 108 | **76** |
| Closed as translation notes | — | 32 |

The 32 closed ones were pure glossary entries — "*Reports* is French *rapports* =
ratios", "*Rocket door* is *porte-fusée* = stub axle carrier" — where the note itself settles
the matter and no figure is in doubt. **Nothing was deleted.** They are still in the chapter
source, retagged `<!-- TRANSLATION NOTE … -->`, so the knowledge stays and only the open-item
count changes.

Each remaining flag now carries a `TRIAGE` line recording its verdict, recommended next step,
and the three probabilities behind them.

## The remaining 76, by next step

| Next step | Count |
| --------- | ----- |
| Verify against the scanned PDF page | 52 |
| Candidate for closing — borderline, went to a human (now done) | 0 |
| Record permanently as a source defect | 12 |
| Needs the French original / another manual / a real car | 5 |
| Unclassified | 1 |

## The 22 borderline candidates — resolved by hand

Jev recommended `close_as_documentation` for 22 flags that my risk gate had held back. I read
all 22 and **closed 15, kept 7**. The seven that stayed each name something genuinely still
unknown, and now carry a `HAND-CHECKED:` line saying why:

| Flag | PDF p. | Why it stays open |
| ---- | ------ | ----------------- |
| Engine characteristics | 11 | Reading `FRG` as `RFA` is an inference, and the "Engine type" row prints version names where engine codes belong. (The `812-000`/`812-00` half of this flag is now resolved — see below.) |
| Type 807-25 parts list | 11 | "Special ass." is truncated in the source and cannot be recovered. |
| Camshaft end float | 20 | The 1600 GS figures are **read as a range the page does not print as one**. |
| Steering rack supports | 42 | The component behind "rudder" is not recoverable; "steering arms" is from context only. |
| Body repair, minor damage | 52 | "scalex" names a tool or location in a repair step and is not recoverable. |
| Harness directory index | 64 | A standing warning that an entire 9-page section must not be trusted as an index. Permanent, not resolvable. |

The 15 closed were glosses that resolve themselves — "*Directorate*" is *direction*,
"*VA spring*" is *AV* transposed, "*Yours.*" is the translator's rendering of
*correspondantes*. Two were closed despite naming something unrecoverable, because what was
lost is not actionable: the `JT` column header of a table that is **empty anyway**, and the
town name of a 1971 Hylomar supplier in département 37.

## Highest risk if guessed — start here

| Risk | PDF p. | Chapter | Where | What is undecided |
| ---- | ------ | ------- | ----- | ----------------- |
| 0.94 | 73 | `u3-supplement-steering-brakes.md` | (d) Mounting the caliper | the drill diameter in step (d) prints "Ø lt" / "Ø It" — the digits are lost. DO NOT drill a caliper on this instruction; get the dimension from the so… |
| 0.88 | 84 | `u5-supplement-special-tooling.md` | Legible figures on the drawings | everything in this section is fragmentary. (1) Sheet 1's "20-11-90" looks like a date but 1990 is twenty years after this manual — it is more likely a… |
| 0.87 | 78 | `u4-supplement-bodywork-paint.md` | (b) Jack-Nut nuts | the drill in step (b)1 prints "Ø 11" while the nut is a Ø 6 Jack-Nut — that is what the page says, but it reads oddly; check the source PDF p.80. The … |
| 0.86 | 19 | `b-engine-ignition.md` | (d) Connecting rods (*bielles*) | "on the side of the decal- / This is a job that allows for its orientation" is a broken translation of a French sentence naming the identifying boss; … |
| 0.85 | 7 | `a-general.md` | Dimension drawing (A-1) | the drawing's track/clearance/height figures do not agree with the A-2 text below (drawing 1,363 / 1,290 / 0,120 / 1,113 vs text 1.29 / 1.27 / 0.11 / … |
| 0.85 | 18 | `b-engine-ignition.md` | (a) Liners (*chemises*) | the gasket rows are labelled only "Blue gasket thickness / Red / Green" on the page, and the 1300 S column prints FOUR values (0.05, 0.07, 0.10, 0.12)… |
| 0.81 | 18 | `b-engine-ignition.md` | (b) Pistons | "Remarked with an arrow on the steering motor" is French "repéré par une flèche" plus a direction word the translation garbled — the orientation refer… |
| 0.80 | 63 | `u1-supplement-general-engine-electrical.md` | Page C-1 | "D8 E7l" prints a letter l for the final character; read as D8 E71 — but the C-1 table in the main manual lists the 1300 G/1300 S starter as "PARIS-RH… |
| 0.79 | 48 | `l-suspension-shock-absorbers.md` | Spring detail | (1) "198^2 under 200kg" and "206*2 under 300kg" use ^ and * where the page prints ± — read as 198 ± 2 mm and 206 ± 2 mm. The numbers themselves are le… |
| 0.79 | 48 | `l-suspension-shock-absorbers.md` | Missing pages in this scan | ABRIDGED SCAN — section L ends at L-1 in this scan; L-2 onwards are absent. |
| 0.78 | 73 | `u3-supplement-steering-brakes.md` | (c) Mounting the hub | "head thickness: 6.8 cm" is almost certainly wrong as a unit — a screw head 68 mm thick is not plausible, and the equivalent rear-brake step below giv… |
| 0.76 | 11 | `b-engine-ignition.md` | (c) Type 1300 S, derived from 812-00 | "Bone joint" is an untranslated French term, unrecoverable from this copy. "5/10th" and "4/10th" are French shorthand for 0.5 mm and 0.4 mm; left in t… |
| 0.76 | 24 | `b-engine-ignition.md` | Missing pages in this scan | ABRIDGED SCAN — page B-1 is MISSING from this scan. PDF p.10 is the unnumbered section divider plate and PDF p.11 is already B-2, so one numbered page… |
| 0.76 | 35 | `e-gearbox.md` | Gearbox types (from the French descrip | this table is transcribed from the FRENCH column of the page images. (1) Several descriptions are cut off at the right-hand edge where the English ove… |
| 0.75 | 50 | `m-braking-system.md` | Rear brakes | (1) The rear pad-type cell prints "(733 on, version 83)" where the front cell prints "(733 on version 85)". "83" is not a version of this car — it is … |

## Worth knowing

- **Two of the top three are drill diameters.** Supplement p.73 step (d) has the caliper
  drill size printed as `Ø lt` with the digits lost, and p.78 gives `Ø 11` for a Ø 6
  Jack-Nut. Neither can be settled from this scan.
- **Five pages carry four flags each** — PDF pp. 9, 37, 48, 50, 54. If anyone sits down with
  the source PDF, those pages retire the most flags per minute.
- **The flags are not evenly spread.** `b-engine-ignition.md` and the two supplement
  bodywork/brake chapters hold most of the risk, which matches where the source is worst.

## Reproducing

The triage scripts are not committed — they are a one-off against a paid external API. The
method is: extract each flag with its surrounding transcribed text, ask Jev one Choice
(what kind of uncertainty), one Score (priority) and three Noul questions (does it leave
anything undecided / would guessing be dangerous / does it block a job), then apply
thresholds in code. The first attempt asked "is this safety-relevant?", which tracked how
dangerous the *subsystem* was rather than the note, and rated glossary entries in the brake
chapter at 0.87. Asking specifically about the *undecided remainder* fixed it.

## Two of the seven, settled afterwards

**Tyre pressure unit — resolved from the shop-shelf, not from general knowledge.** The A110
page prints the unit only as "kg". The **Renault Dauphine M.R.93** in this repo — same
manufacturer, same country, same era, and likewise an English edition of a French original —
prints its own as **"1 kg (14 psi)"** front and **"1.5 kg (23 psi)"** rear
(`manuals/renault/vehicle/dauphine`, `wiki/k-wheels-hubs-drums.md`, PDF p.332). 14 psi per
1 kg is **kg/cm²** (1 kg/cm² = 14.223 psi); the Toyota MR2 FSM here prints the same pairing
outright as "2.1 kg/cm² (30 psi)". So the bare "kg" is kg/cm², and the A110 flag is closed
with that citation. psi conversions were added to the chapter, clearly marked as computed.

**`812-000` vs `812-00`** — recorded as a maintainer judgement: the same engine, a
typographic slip in the source, not two variants. Nothing in the manual distinguishes them
and no part or procedure keys off the third zero. Both pages keep their own spelling exactly
as printed. Not independently checked against an Alpine or Renault parts catalogue.
