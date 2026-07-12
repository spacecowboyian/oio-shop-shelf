# Body Electrical System (Part 1)

Toyota MR2 (AW11) factory service manual — Body Electrical System, Part 1
(manual section **BE**, pages BE-1 through BE-76). Covers general wiring
information, switch/relay locations, the ignition switch, lighting, wiper and
washer, instruments/gauges/warning lights, rear window defogger, heater, cruise
control, power window, door lock control, remote control mirror, and radio.

> **Continuity tables.** Switch-continuity charts are printed as dot-and-line
> matrices. They are transcribed here as **connected-terminal groups** per switch
> position (e.g. "ON: 2–3–4, 7–8" means terminals 2, 3, 4 are joined and terminals
> 7, 8 are joined). Wire colors, where the manual prints them, are noted next to
> the terminal number.

> **Figures.** Wiring diagrams and connector pin-layout illustrations are
> image-only and are left as figure references to the page image.

---

## General Information

### Wiring color code

Wire colors are indicated by an alphabetical code. The first letter indicates the
basic wire color and the second letter indicates the color of the stripe.

| Code | Color       | Code | Color       | Code | Color   |
| ---- | ----------- | ---- | ----------- | ---- | ------- |
| B    | Black       | L    | Blue        | R    | Red     |
| BR   | Brown       | LG   | Light Green | V    | Violet  |
| G    | Green       | O    | Orange      | W    | White   |
| GR   | Gray        | P    | Pink        | Y    | Yellow  |

### Connectors

1. **Pin number of female connector** — numbered in order from upper left to lower right.
2. **Pin number of male connector** — numbered in order from upper right to lower left.
3. **Distinction of male and female connectors** — male and female connectors are
   distinguished by the shape of their internal pins.
   - (a) All connectors are shown from the open end, with the lock on top.
   - (b) To pull connectors apart, pull on the connector itself, not the wires.

### Replacement of combination switch

**Remove terminals from connector**

- (a) From the open end, insert a miniature screwdriver between the locking lugs
  and terminal.
- (b) Pry up the locking lugs with the screwdriver and pull the terminal out from
  the rear.

**Install terminals to connector**

- (a) Push in the terminal until it is securely locked in the connector lug.
- (b) Pull on the wire to confirm that it is securely locked.

### Reset circuit breaker

1. **Remove circuit breaker**
   - (a) Remove the kick panel.
   - (b) Remove the circuit breaker.
2. **Reset circuit breaker**
   - (a) Insert the needle into the reset hole and push it.
   - (b) Using an ohmmeter, check that there is continuity between both terminals of
     the circuit breaker. If there is no continuity, replace the circuit breaker.
3. **Install circuit breaker**
   - (a) Install the circuit breaker.
   - (b) Install the kick panel.

   > **NOTE:** If a circuit breaker continues to cut out, a short circuit is
   > indicated. Have the system checked by a qualified technician.

### Replacement of fuses

Install new fuses with correct amperage ratings.

> **CAUTION:**
> 1. Turn off all electrical components and the ignition switch before replacing a
>    fuse. Do not exceed the fuse amp rating.
> 2. Always use a fuse puller for removing and inserting a fuse. Remove and insert
>    straight in and out without twisting. Twisting could force open the terminals
>    too much, resulting in a bad connection.

If a fuse continues to blow, the circuit is probably shorted. Have the system
checked by a qualified technician.

### Take care when inspecting headlight circuit

> **WARNING:** Before inspecting or adjusting the retractable headlight circuit,
> disconnect the light retractor control relay connector.

**Remove HEAD 60A fusible link**

- (a) Remove negative battery cable.
- (b) Remove the relay block undercover.
- (c) Pull out the fusible link cassette from below.
- (d) Remove the bolt, and remove the fusible link.

### Voltage check

- (a) Establish conditions in which voltage is present at the check point.
- (b) Using a voltmeter, connect the negative lead to a good ground point or
  negative battery terminal and the positive lead to the connector or component
  terminal. This check can be done with a test light instead of a voltmeter.

### Continuity and resistance check

- (a) Disconnect the battery terminal or wire so there is no voltage between the
  check points.
- (b) Contact the two leads of an ohmmeter to each of the check points.

If the circuit has diodes, reverse the two leads and check again. When contacting
the negative lead to the diode positive side and the positive lead to the negative
side, there should be continuity. When contacting the two leads in reverse, there
should be no continuity.

- (c) Use a volt/ohmmeter with high impedance (10 kΩ/V minimum) for troubleshooting
  of the electrical circuit.

### Finding a short circuit

- (a) Remove the blown fuse and disconnect all loads of the fuse.
- (b) Connect a test light in place of the fuse.
- (c) Establish conditions in which the test light comes on.
- (d) Disconnect and reconnect the connectors while watching the test light. The
  short lies between the connector where the test light stays lit and the connector
  where the light goes out.
- (e) Find the exact location of the short by lightly shaking the problem wire along
  the body.

---

## Location of Switches and Relays

*(Figure: Engine compartment switches and relays — Water Temperature Sender Gauge;
4A-GZE / 4A-GE (A/T) — see page image p.802)*

*(Figure: Instrument panel switches and relays — Wiper and Washer Switch, Headlight
Dimmer Switch, Turn Signal and Hazard Warning Switch, Turn Signal Lever, Horn
Contact — see page image p.803)*

*(Figure: Passenger compartment switches and relays — Brake Fluid Level Warning
Switch, Turn Signal Flasher, Headlight Retainer Relay, Taillight Control Relay,
Headlight Control Relay — see page image p.804)*

*(Figure: Passenger and luggage compartment switches and relays — Power Window Door
Switch, Stop Light Switch, Door Lock Switch, Clutch Switch, Door Lock Control Relay,
Door Lock Key Switch, Seat Belt Warning Relay, Door Courtesy Switch, Fuel Sender
Gauge — see page image p.805)*

---

## Ignition Switch

### Inspection of ignition switch

**Inspect switch continuity** — inspect the switch continuity between terminals.

| Switch position   | Connected terminals |
| ----------------- | ------------------- |
| LOCK              | (none)              |
| ACC               | 3–4                 |
| ON                | 2–3–4, 7–8          |
| START             | 1–2–4, 5–7–8        |
| Warning — Normal  | (none)              |
| Warning — Push    | 9–10                |

If continuity is not as specified, replace the switch.

---

## Lighting

### Troubleshooting

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| Only one light does not light (all exterior) | Light bulb burned out | Replace bulb | |
| | Socket, wire or ground faulty | Repair as necessary | |
| Headlights do not flip up | Fusible link blown | Replace fusible link | |
| | RTR MTR fuse blown | Replace fuse and check for short | BE-4 |
| | Light retractor control relay faulty | Check relay | BE-16 |
| | Light retractor motor faulty | Check motor | BE-17 |
| | Wiring or ground faulty | Repair as necessary | |
| No headlights light | Fusible link blown | Replace fusible link | |
| | Headlight control relay faulty | Check relay | BE-14 |
| | Light control switch faulty | Check switch | BE-12 |
| | Wiring or ground faulty | Repair as necessary | |
| High beam headlights or headlight flasher do not operate | Light control switch faulty | Check switch | BE-12 |
| | Wiring faulty | Repair as necessary | |
| Tail, parking and license lights do not light | TAIL fuse blown | Replace fuse and check for short | BE-4 |
| | Fusible link blown | Replace fusible link | |
| | Taillight control relay faulty | Check relay | BE-14 |
| | Light control switch faulty | Check switch | BE-12 |
| | Wiring or ground faulty | Repair as necessary | |
| Stop lights do not light | STOP fuse blown | Replace fuse and check for short | BE-4 |
| | Stop light switch faulty | Adjust or replace switch | |
| | Wiring or ground faulty | Repair as necessary | |
| Stop lights stay on | Stop light switch faulty | Adjust or replace switch | |
| Instrument lights do not light (taillights light) | Light control rheostat faulty | Check rheostat | BE-12 |
| | Wiring or ground faulty | Repair as necessary | |
| Turn signal does not flash on one side | Turn signal switch faulty | Check switch | BE-18 |
| | Wiring or ground faulty | Repair as necessary | |
| Turn signals do not operate | TURN GAG fuse blown | Replace fuse and check for short | BE-4 |
| | Turn signal flasher faulty | Check flasher | BE-18 |
| | Turn signal/hazard switch faulty | Check switch | BE-17 |
| | Wiring or ground faulty | Repair as necessary | |
| Hazard warning lights do not operate | HAZ-RADIO fuse blown | Replace fuse and check for short | BE-4 |
| | Turn signal flasher faulty | Check flasher | BE-18 |
| | Turn signal/hazard switch faulty | Check switch | BE-17 |
| | Wiring or ground faulty | Repair as necessary | |

### Light Control Switch and Rheostat

**1. Inspect light control switch continuity** — inspect the switch continuity
between terminals.

| Switch position | Connected terminals |
| --------------- | ------------------- |
| OFF             | (none)              |
| TAIL            | 8–9                 |
| HEAD            | 4–7–8–9             |
| HOLD            | 7–9                 |

If continuity is not as specified, replace the switch.

**2. Inspect operation of light control rheostat**

- (a) Gradually change the brightness of rheostat from maximum to minimum, and check
  that the resistance between terminals 1 and 9 increases from 0 Ω to 10 Ω.
- (b) Check that there is no continuity between terminals 1 and 9 with the rheostat
  turned off.

If operation is not as specified, replace the switch.

**3. Check that idle increases** — start the engine. When the light control switch is
set to TAIL, engine revolution should increase.

### Headlight Dimmer Switch

**Inspect continuity of headlight dimmer switch** — inspect the switch continuity
between terminals. Terminals: 13 = ED (W-B), 6 = HL (R-G), 5 = HU (R-Y), 12 = HF (R-W).

| Switch position | Connected terminals |
| --------------- | ------------------- |
| Flash           | 13–5–12             |
| Low Beam        | 13–6                |
| High Beam       | 13–5                |

If continuity is not as specified, replace the switch.

**Replacement of headlight dimmer switch**

- (a) Remove the terminals from the connector. (See General Information, above.)
- (b) Remove the turn signal and hazard warning switch.
- (c) Remove the headlight dimmer switch.
- (d) Install the headlight dimmer switch.
- (e) Insert the spring into the lever.
- (f) Push in the hinge of the lever to the switch body. (Type "A")
- (g) Install the lever to the switch body with the screw and nut. (Type "B")
- (h) Place the ball on the spring, position the lever at HI and install the plate.
- (i) Ensure that the switch operates smoothly.
- (j) Install the terminals to the connector.

### Headlight Control Relay

**1. Inspect relay continuity**

- (a) Check that there is continuity between terminals 1 and 2.
- (b) Check that there is no continuity between terminals 3 and 4.
- (c) Check that there is no continuity between terminals 1 and 4.

If continuity is not as specified, replace the relay.

**2. Inspect relay operation**

- (a) Apply battery voltage across terminals 1 and 2.
- (b) Check that there is continuity between terminals 3 and 4.
- (c) Check that there is no continuity between terminals 1 and 4.

If operation is not as described, replace the relay.

### Taillight Control Relay

**1. Inspect relay continuity**

- (a) Check that there is continuity between terminals 1 and 3.
- (b) Check that there is no continuity between terminals 2 and 4.
- (c) Check that there is no continuity between terminals 3 and 4.

If continuity is not as specified, replace the relay.

**2. Inspect relay operation**

- (a) Apply battery voltage across terminals 1 and 3.
- (b) Check that there is continuity between terminals 2 and 4.
- (c) Check that there is no continuity between terminals 3 and 4.

If operation is not as described, replace the relay.

### Headlight Retainer Relay

**1. Inspect headlight circuit operation** — connect the positive (+) leads from the
battery to terminals 4 and 7. Connect the negative (−) lead to terminal 2. Connect a
3.4 W test bulb between terminal 8 and the positive (+) lead from the battery.

- (a) Disconnect the positive (+) lead from terminal 4. Check that the test bulb is
  lighting.
- (b) Connect the negative (−) lead to terminal 6. Check that the test bulb does not
  light.

If operation is not as specified, replace the relay.

**2. Inspect taillight circuit operation** — connect the positive (+) lead from the
battery to terminals 4 and 7. Connect the negative (−) lead to terminal 3. Connect a
3.4 W test bulb between terminal 1 and the positive (+) lead from the battery.

- (a) Disconnect the positive (+) lead from terminal 4. Check that the test bulb is
  lighting.
- (b) Connect the negative (−) lead to terminal 6. Check that the test bulb does not
  light.

If operation is not as specified, replace the relay.

### Light Retractor Control Relay

**1. Inspect relay continuity** — inspect the relay continuity between terminals.

| Condition | Connected terminals |
| --------- | ------------------- |
| Standard inspection | 1–2 |
| With battery voltage applied between terminals 3 and 2 | 1–2, 4–5 |
| With battery voltage applied between terminals 3 and 5 | 1–2 |

<!-- NEEDS REVIEW: Light retractor control relay continuity matrix (BE-16) is a dense dot-matrix; connected-terminal groups read from page image p.812 — verify against the page image. -->

If continuity is not as specified, replace the relay.

**2. Inspect relay operation**

- (a) With the light control switch off, connector connected, and terminal 8
  grounded, raise the headlights with the lights lit.
- (b) Quickly ground terminal 6. The light will go out, but the headlight will
  remain up.
- (c) When terminal 6 is taken off ground, the headlights will flip down.

If operation is not as specified, replace the relay.

### Light Retractor Motor

**1. Inspect motor operation** — connect the positive (+) lead from the battery to
terminal 2 and the negative (−) lead to terminal 1. Check that the motor operates.
If there is no motor operation, replace the motor.

**2. Inspect diode continuity of motor**

- (a) Operate the motor to a position except the uppermost or lowermost position.
- (b) Connect the ohmmeter test leads so that the current from the meter can flow
  from terminal 5 to 4; check that there is no continuity.
- (c) Connect the ohmmeter test leads so that the current from the meter can flow
  from terminal 3 to 4; check that there is no continuity.
- (d) Reverse the test leads of the ohmmeter; check that there is continuity.

If continuity is not as specified, replace the motor.

### Turn Signal and Hazard Warning Switch

**Inspect turn signal and hazard warning switch** — inspect switch continuity between
terminals. Terminals: 9 = TL (G-B), 3 = TB (G-W), 8 = TR (G-Y), 2 = B1 (G-L),
7 = F (G), 1 = B2 (G-O).

| Switch position     | Connected terminals |
| ------------------- | ------------------- |
| Turn signal — L     | 9–3, 2–7            |
| Turn signal — N     | 2–7                 |
| Turn signal — R     | 3–8, 2–7            |
| Hazard — ON         | 9–3–8, 7–1          |

If continuity is not as specified, replace the switch.

**Replacement of turn signal and hazard warning switch**

- (a) Remove the terminals from the connector.
- (b) Remove the turn signal and hazard switch.
- (c) Install the turn signal and hazard switch.
- (d) Install the terminals to the connector.

### Turn Signal Flasher

**Inspect relay operation**

- (a) Connect the positive (+) lead from the battery to terminal 3 and the negative
  (−) lead to terminal 2.
- (b) Connect the two turn signal light bulbs (27 W) parallel to each other to
  terminals 1 and 2. Check that the bulbs turn on and off.

> **NOTE:** The turn signal lights should flash 60 to 120 times per minute. If one
> of the front or rear turn signal lights has an open circuit, the number of flashes
> will be more than 140 per minute.

If operation is not as specified, replace the flasher.

---

## Wiper and Washer

### Troubleshooting

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| Wiper does not operate or return to off position | WIPER fuse blown | Replace fuse and check for short | BE-4 |
| | Wiper motor faulty | Check motor | BE-20 |
| | Wiper control switch faulty | Check switch | BE-19 |
| | Wiring or ground faulty | Repair as necessary | |
| Wiper does not operate in INT position | Wiper control switch faulty | Check switch | BE-19 |
| | Wiper motor faulty | Check motor | BE-20 |
| | Wiring or ground faulty | Repair as necessary | |
| Washer does not operate | Washer hose or nozzle clogged | Repair as necessary | |
| | Wiper control switch faulty | Check switch | BE-19 |
| | Wiring faulty | Repair as necessary | |

### Wiper and Washer Switch

**1. Inspect wiper and washer switch continuity** — inspect the switch continuity
between terminals. Terminals: 2 = +B, 1 = +2, 3 = +1, 5 = +S, 4 = E, 7 = W.

| Switch position | Connected terminals |
| --------------- | ------------------- |
| MIST            | +B(2)–+1(3)         |
| OFF             | +1(3)–+S(5)         |
| INT             | +1(3)–+S(5)         |
| LO              | +B(2)–+1(3)         |
| HI              | +B(2)–+2(1)         |
| Washer          | E(4)–W(7)           |

If continuity is not as specified, replace the switch.

**2. Inspect intermittent operation**

- (a) Turn the wiper switch to INT position.
- (b) Connect the positive (+) lead from the battery to terminal 2 and the negative
  (−) lead to terminal 4.
- (c) Connect the positive (+) lead from the voltmeter to terminal 3 and the negative
  (−) lead to terminal 4. Check that the meter needle indicates battery voltage.
- (d) After connecting terminal 5 to terminal 2, connect it to terminal 4. Then check
  that the voltage rises from 0 volts to battery voltage within 3 to 5 seconds.

If operation is not as specified, replace the switch.

**3. Inspect washer switch operation**

- (a) Connect the positive (+) lead from the battery to terminal 2 and the negative
  (−) lead to terminal 4.
- (b) Connect the positive (+) lead from the voltmeter to terminal 3 and the negative
  (−) lead to terminal 4.
- (c) Push in the washer switch. Check that the voltage changes as shown: with the
  washer switch ON, voltage rises to battery voltage after approx. 0.5 sec and drops
  to 0 volt after approx. 2.5 sec when released.

If operation is not as specified, replace the wiper and washer switch.

### Wiper Motor

**1. Inspect that motor operates at low speed**

- (a) Disconnect the connector from the wiper motor.
- (b) Connect the positive (+) lead from the battery to terminal 2. Connect the
  negative (−) lead to the motor body.
- (c) Check that the motor operates at low speed.

If operation is not as specified, replace the motor.

**2. Inspect that motor operates at high speed**

- (a) Connect the positive (+) lead from the battery to terminal 1. Connect the
  negative (−) lead to the motor body.
- (b) Check that the motor operates at high speed.

If operation is not as specified, replace the motor.

**3. Inspect that motor operates, stopping at stop position**

- (a) Operate the motor at low speed.
- (b) Stop motor operation anywhere except stop position by disconnecting terminal 2.
- (c) Connect terminals 2 and 3.
- (d) Connect the positive (+) lead from the battery to terminal 4.
- (e) Check that the motor stops running at stop position after the motor operates
  again.

If operation is not as specified, replace the motor.

**Replacement of wiper motor**

1. **Stop wiper arm in up position**
   - (a) Turn the ignition switch to ON.
   - (b) Turn the wiper switch to low.
   - (c) With the wiper arm up, turn the ignition switch OFF.

   > **NOTE:** If the wiper motor does not operate, disassemble the motor and remove
   > the armature.
2. **Remove wiper motor**
   - (a) Disconnect the connector from the wiper motor.
   - (b) Remove the light retractor relay from the wiper bracket.
   - (c) Remove the wiper motor set bolts.
   - (d) Lower the wiper arm by hand until it stops. Then hook the wiper link's hook
     onto the dash panel service hole.
   - (e) Using a screwdriver, disconnect the motor from the wiper link.
3. **Install wiper motor**
   - (a) Connect the wiper motor to the wiper link.

     > **CAUTION:** When replacing the motor, rotate the motor crank 180° from the
     > auto-stop position.
     >
     > **NOTE:** Supply parts motors come with the crank already rotated.
   - (b) Move the wiper arm to the up position by hand.
   - (c) Install the wiper motor set bolts.
   - (d) Connect the wiper motor connector.
   - (e) Install the light retractor control relay to the wiper motor bracket.

---

## Instruments, Gauges and Warning Lights

### Troubleshooting

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| Voltmeter does not work | Fuses blown | Replace in-line fuses and check for short | BE-4 |
| | Voltmeter faulty | Check voltmeter | BE-25 |
| | Wiring faulty | Repair as necessary | |
| Tachometer does not work | "TURN GAG" fuse blown | Replace fuse and check for short | BE-4 |
| | Tachometer faulty | Check tachometer | BE-25 |
| | Wiring faulty | Repair as necessary | |
| Fuel gauge does not work | "TURN GAG" fuse blown | Replace fuse and check for short | BE-4 |
| | Fuel gauge faulty | Check gauge | BE-26 |
| | Sender gauge faulty | Check sender gauge | BE-26 |
| | Wiring or ground faulty | Repair as necessary | |
| Fuel level warning light does not work | "TURN GAG" fuse blown | Replace fuse and check for short | BE-4 |
| | Bulb burned out | Replace bulb | |
| | Fuel level warning switch faulty | Check switch | BE-27 |
| | Wiring or ground faulty | Repair as necessary | |
| Water temperature gauge does not work | "TURN GAG" fuse blown | Replace fuse and check for short | BE-4 |
| | Water temperature receiver gauge faulty | Check gauge | BE-27 |
| | Water temperature sender gauge faulty | Check sender gauge | BE-28 |
| | Wiring or ground faulty | Repair as necessary | |
| Oil pressure receiver gauge does not work | "TURN GAG" fuse blown | Replace fuse and check for short | BE-4 |
| | Oil pressure receiver gauge faulty | Check receiver gauge | BE-28 |
| | Oil pressure sender gauge faulty | Check sender gauge | BE-28 |
| | Wiring or ground faulty | Repair as necessary | |
| Brake warning light does not light | "TURN GAG" fuse blown | Replace fuse and check for short | BE-4 |
| | Bulb burned out | Replace bulb | |
| | Brake fluid level warning switch faulty | Check switch | BE-29 |
| | Parking brake switch faulty | Check switch | BE-29 |
| | Wiring or ground faulty | Repair as necessary | |
| Discharge warning light does not light | "CHARGE" fuse blown | Replace fuse and check for short | BE-4 |
| | Bulb burned out | Replace bulb | |
| | Wiring faulty | Repair as necessary | |

### Combination Meter and Gauge

*(Figure: Combination meter connectors "A", "B", "C" pin layout — see page image p.820)*

**Combination meter circuit** — wire harness connector terminal assignments:

| Connector | Terminal | Connects to |
| --------- | -------- | ----------- |
| A | 1 | Fuel Level Warning Switch terminal 2 |
| A | 2 | TURN GAG Fuse |
| A | 4 | Cooling Fan Computer |
| A | 5 | Fuel Sender Gauge terminal 1 |
| A | 8 | ECT Select Switch |
| A | 9 | Igniter terminal 4 |
| A | 10 | OD Main Switch |
| B | 1 | ECT Select Switch |
| B | 2 | Light Control Rheostat terminal 1 |
| B | 3 | TAIL Fuse |
| B | 4 | TCCS ECU and Cruise Control Computer terminal 7 |
| B | 5 | Ground |
| B | 6 | Ground |
| B | 7 | Turn Signal Switch terminal 6 |
| B | 8 | Turn Signal Switch terminal 9 |
| C | 1 | Turn Signal Switch terminal 8 |
| C | 2 | TCCS ECU |
| C | 3 | Oil Pressure Sender Gauge |
| C | 4 | Ground |
| C | 5 | Water Temperature Sender Gauge |
| C | 7 | CHARGE Fuse |
| C | 8 | Parking Brake Switch terminal 1 and Brake Fluid Level Warning Switch terminal 1 |
| C | 9 | Ignition Switch terminal 2 |
| C | 10 | TCCS ECU |
| C | 11 | Seat Belt Warning Relay terminal 5 |

*(Figure: Combination meter circuit schematic — see page image p.820)*

### Speedometer

**On-vehicle inspection of speedometer**

- (a) Using a speedometer tester, inspect the speedometer for allowable indication
  error and check the operation of the odometer.

  > **NOTE:** Tire wear and tire over- or under-inflation will increase the
  > indication error.

  If error is excessive, replace the speedometer.
- (b) Check the speedometer for pointer vibration and abnormal noise.

  > **NOTE:** Pointer vibration can be caused by a loose speedometer cable.

| Standard indication (km/h) | Allowable range (km/h) |
| -------------------------- | ---------------------- |
| 20  | 18 – 23 |
| 40  | 40 – 44 |
| 60  | 60 – 64.5 |
| 80  | 80 – 85 |
| 100 | 100 – 105 |
| 120 | 120 – 125.5 |
| 140 | 140 – 146 |
| 160 | 160 – 167 |
| 180 | 180 – 188 |
| 200 | 200 – 209 |

| Standard indication (mph) | Allowable range (mph) |
| ------------------------- | --------------------- |
| 20  | 20 – 23 |
| 40  | 40 – 43.5 |
| 60  | 60 – 64 |
| 80  | 80 – 84.5 |
| 100 | 100 – 105 |
| 120 | 120 – 125.5 |

### Tachometer

**On-vehicle inspection of tachometer** (DC 13.5 V, 25°C (77°F))

- (a) Connect a tune-up test tachometer, and start the engine.

  > **CAUTION:**
  > - Reversing the connection of the tachometer will damage the transistors and
  >   diodes inside.
  > - When removing or installing the tachometer, be careful not to drop or subject
  >   it to any heavy shocks.
- (b) Compare the tester and tachometer indication.

If error is excessive, replace the tachometer.

| Standard indication (rpm) | Allowable range (rpm) |
| ------------------------- | --------------------- |
| 700   | 610 – 750 |
| 800   | 710 – 850 |
| 1,000 | 940 – 1,140 |
| 2,000 | 1,940 – 2,240 |
| 3,000 | 2,930 – 3,330 |
| 4,000 | 3,970 – 4,370 |
| 5,000 | 5,000 – 5,400 |
| 6,000 | 6,000 – 6,500 |
| 7,000 | 6,990 – 7,590 |
| 8,000 | 8,030 – 8,630 |

### Voltmeter

**Inspection of voltmeter** — compare the tester and voltmeter indications. If error
is excessive, replace the voltmeter.

### Fuel Gauge

**1. Inspect receiver gauge operation**

- (a) Disconnect the connector from the fuel sender gauge. Turn ignition switch on.
  Check that the receiver gauge needle moves to the empty position.
- (b) Connect a 3.4 W bulb between terminal 1 and body ground. Check that the bulb
  lights and that the receiver gauge needle operates.

  > **NOTE:** Because of the silicon oil in the gauge, it will take about 180 seconds
  > for the needle to stabilize.

If indications are not correct, remove and test the receiver gauge.

**2. Measure receiver gauge resistance between terminals**

| Between terminals | Resistance (Ω) |
| ----------------- | -------------- |
| IG – E  | Approx. 203.2 |
| FU – E  | Approx. 101.3 |
| IG – FU | Approx. 101.9 |

If each resistance value is not as shown above, replace the receiver gauge.

**3. Inspect sender gauge operation**

- (a) Connect a series of three 1.5 V dry cell batteries.
- (b) Connect the positive (+) lead from the dry cell batteries to terminal 1 through
  a 3.4 W test bulb and the negative (−) lead to terminal 3.
- (c) Check that the voltage rises between terminals 1 and 3 as the float is moved
  from the top to bottom position.
- (d) Measure the resistance between terminals 1 and 3 for each float position.

| Float position | Height mm (in.) | Resistance (Ω) |
| -------------- | --------------- | -------------- |
| F | 69.5 ± 3 (2.736 ± 0.12) | 3 ± 1 |
| E | 241 ± 3 (9.49 ± 0.12) | 110 ± 7.7 |

If each resistance value is not as shown above, replace the receiver gauge.

### Fuel Level Warning

**1. Inspect warning light operation**

- (a) Disconnect the connector from the fuel sender gauge. Connect terminal 2 and
  body ground.
- (b) Turn the ignition switch. Check that the bulb lights.

If operation is not correct, remove and test the bulb.

**2. Inspect level warning switch operation**

- (a) Apply battery voltage between terminals 2 and 3 through a 3.4 W bulb. Check
  that the bulb lights.

  > **NOTE:** It will take a short time for the bulb to light.
- (b) Submerge the switch in gasoline. Check that the bulb goes out.

If operation is not correct, replace the sender gauge.

### Water Temperature Gauge

**1. Inspect receiver gauge operation**

- (a) Disconnect the connector from the sender gauge. Ground the terminal through a
  3.4 W bulb.
- (b) Turn the ignition switch on. Check that the bulb lights and that the receiver
  gauge needle operates.

If indication is not correct, remove and test the receiver gauge.

**2. Measure receiver gauge resistance between terminals**

| Between terminals | Resistance (Ω) |
| ----------------- | -------------- |
| IG – E  | 145.8 |
| TU – E  | 201.8 |
| IG – TU | 56 |

If each resistance value is not as shown above, replace the receiver gauge.

**3. Measure sender gauge resistance** — measure the resistance between the terminal
and ground.

| Water temperature °C (°F) | Resistance (Ω) |
| ------------------------- | -------------- |
| 50 (122)  | 226 +33.6 / −33.6 |
| 115 (239) | 26.4 +1.71 / −2.21 <!-- NEEDS REVIEW: OCR read "264"; page image p.824 clearly shows "26.4 +1.71/-2.21" — corrected from image --> |

If each resistance value is not as shown above, replace the sender gauge.

### Oil Pressure Gauge

**1. Inspect receiver gauge operation**

- (a) Disconnect the connector from the sender gauge.
- (b) Turn the ignition switch on. Check that the receiver gauge needle moves to the
  low position.
- (c) Ground the terminal on the wire harness side connector through a 3.4 W test
  bulb. Check that the receiver gauge needle moves to the high side.

If operation is not as specified, measure the receiver gauge resistance.

**2. Measure resistance of receiver gauge** — using an ohmmeter, measure the
resistance between terminals A and B.

- **Resistance:** Approx. 42 Ω

If resistance value is not correct, replace the receiver gauge.

**3. Inspect sender gauge operation**

- (a) Disconnect the connector from the sender gauge.
- (b) Connect a 12 V battery to the sender gauge terminal in series with a 3.4 W
  bulb. Check that the bulb does not light when the engine is stopped, and flashes
  when the engine is running. The number of flashes should vary with engine speed.

If operation is not correct, replace the sender gauge.

### Brake Warning

**1. Inspect warning light operation**

- (a) Disconnect the connectors from the level warning switch and parking brake
  switch.
- (b) Connect the terminals on the wire harness side of the level warning switch
  connector.
- (c) Remove CHARGE fuse and turn the ignition switch ON. Check that the warning
  light lights.

If the warning light does not light, test the bulb.

**2. Inspect level warning switch operation**

- (a) Check that there is no continuity between terminals with the switch OFF (float
  up).
- (b) Check that there is continuity between terminals with the switch ON (float
  down).

If operation is not as specified, replace the switch.

**3. Inspect parking brake switch operation**

- (a) Check that there is continuity between the terminals with the switch pin
  released. (Parking brake lever pulled up)
- (b) Check that there is no continuity between the terminals with the switch pin
  pushed in. (Parking brake lever released)

If the operation is not as specified, replace the switch.

### Supercharger Indicator Circuit

**Inspect indicator light operation**

- (a) Connect the positive (+) leads from the battery to terminals A2 and C7, and the
  negative (−) lead to terminal B6 on the meter side. Check that the indicator light
  does not light up.
- (b) Connect the negative (−) lead to terminal C2, under the same conditions as in
  (a). Check that the indicator light lights up.
- (c) Connect the positive (+) lead from the battery to terminal A2 and the negative
  (−) leads to terminals B6 and C7 on the meter side. Check that the indicator light
  lights up.

### Seat Belt Warning

**1. Inspect warning light operation**

- (a) Disconnect the connectors from the seat belt warning relay and ground terminal
  5 on the wire harness side.
- (b) Turn the ignition switch ON, check that the warning light lights.

If warning light does not light, test the bulb.

**2. Inspect buckle switch operation**

- (a) Disconnect the connector from the switch.
- (b) Check that there is no continuity between terminals on the switch side
  connector with the belt fastened.
- (c) Check that there is continuity between terminals on the switch side connector
  with the belt unfastened.

If operation is not as specified, replace the seat belt inner.

**3. Inspect unlock warning switch operation** — see [Ignition Switch](#ignition-switch)
(BE-10). If operation is not as specified, replace the switch.

**4. Inspect seat belt warning relay circuit** — disconnect the relay connector and
inspect the connector on the wire harness side as shown in the chart.

| Check for | Tester connection | Condition | Specified value |
| --------- | ----------------- | --------- | --------------- |
| Voltage | 1 – Ground | Courtesy switch OFF (Door closed) | Battery voltage |
| | | Courtesy switch ON (Door opened) | No voltage |
| Voltage | 2 – Ground | Turn ignition switch to Lock or ACC | No voltage |
| | | Turn ignition switch ON | Battery voltage |
| Voltage | 3 – Ground | Unlock warning switch OFF (Ignition key removed) | No voltage |
| | | Unlock warning switch ON (Ignition key set) | Battery voltage |
| Continuity | 4 – Ground | Always | Continuity |
| Voltage | 5 – Ground | Turn ignition switch to Lock or ACC | No voltage |
| | | Turn ignition switch ON | Battery voltage |
| Continuity | 6 – Ground | Buckle switch OFF (Seat belt fastened) | No continuity |
| | | Buckle switch ON (Seat belt unfastened) | Continuity |

If circuit is as specified, replace the relay.

---

## Rear Window Defogger

### Troubleshooting

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| Rear window defogger does not work | DEFOG fuse blown | Replace fuse and check for short | BE-4 |
| | Defogger switch faulty | Check switch | BE-31 |
| | Defogger wire broken | Check wires | BE-31 |
| | Wiring and ground faulty | Repair as necessary | |

### Rear Window Defogger Switch

**1. Inspect switch continuity** — inspect continuity between the terminals
(terminals 3, 5 = illumination).

| Switch position | Connected terminals |
| --------------- | ------------------- |
| OFF | 2–4 (illumination) |
| ON  | 1–2, 2–4 |

If continuity is not as specified, replace the switch or bulb.

**2. Check that idle increases** — when the defogger switch is set to ON, engine
revolution should increase.

### Rear Window Defogger Wires

> **CAUTION:**
> - When cleaning the glass, use a soft, dry cloth, and wipe the glass in the
>   direction of the wire. Take care not to damage the wires.
> - Do not use detergents or glass cleaners with abrasive ingredients.
> - When measuring voltage, wind a piece of tin foil around the tip of the negative
>   probe and press the foil against the wire with your finger as shown.

**Inspection of rear window defogger wires**

1. **Inspect for wire breakage**
   - (a) Turn the ignition switch to ON.
   - (b) Turn the defogger switch to ON.
   - (c) Inspect the voltage at the center of each heat wire as shown.

     | Voltage | Criteria |
     | ------- | -------- |
     | Approx. 5 V | Okay (no break in wire) |
     | Approx. 10 V or 0 V | Broken wire |

     > **NOTE:** If there are 10 V, the wire is broken between the center of the wire
     > and the positive (+) end. If there is no voltage, the wire is broken between
     > the center of the wire and ground.
2. **Inspect for wire breakage point**
   - (a) Place the voltmeter positive (+) lead against the defogger positive (+)
     terminal.
   - (b) Place the voltmeter negative (−) lead with the foil strip against the heat
     wire at the positive (+) terminal end and slide it toward the negative (−)
     terminal end.
   - (c) The point where the voltmeter deflects from zero to several volts is the
     place where the heat wire is broken.

     > **NOTE:** If the heat wire is not broken, the voltmeter will indicate 0 V at
     > the positive (+) end of the heat wire but gradually increase to about 12 V as
     > the meter probe is moved to the other end.

**Repair of rear window defogger wires**

1. Clean broken wire tips with cleaner.
2. Place masking tape along both sides of the wire to be repaired.
3. Repair defogger wires:
   - (a) Thoroughly mix the repair agent (Dupont paste No. 4817).
   - (b) Using a fine tip brush, apply a small amount to the wire.
   - (c) After a few minutes, remove the masking tape.
   - (d) Allow to stand at least 24 hours.

---

## Heater

### Wiring Diagram

*(Figure: Heater wiring diagram — heater control assembly, blower motor, blower
switch, resistor, servo motors, relay — see page image p.829)*

*(Figure: Heater connectors — Heater Control Assembly, Blower Switch, Amplifier, Air
Vent Mode Control Servo Motor, RECIRC/FRESH Control Servo Motor, Blower Motor, Blower
Resistor, Heater Relay pin layouts — see page image p.830)*

### Troubleshooting

| Problem | Possible cause | Remedy | Page |
| ------- | -------------- | ------ | ---- |
| Blower does not work when fan switch is on | HEATER fuse blown | Replace fuse and check for short | BE-4 |
| | Heater relay faulty | Check relay | BE-35 |
| | Heater blower switch faulty | Check switch | BE-35 |
| | Heater blower resistor faulty | Check resistor | BE-36 |
| | Heater blower motor faulty | Replace motor | |
| | Wiring or ground faulty | Repair as necessary | |
| Incorrect temperature output | Control cables broken or binding | Check cables | BE-36 |
| | Servo motor faulty | Check servo motor | BE-37 |
| | Heater hoses leaking or clogged | Replace hose | |
| | Water valve faulty | Replace valve | |
| | Air dampers broken | Repair dampers | |
| | Air ducts clogged | Repair ducts | |
| | Heater radiator leaking or clogged | Replace radiator | |
| | Heater control unit faulty | Repair control unit | |

### Heater Blower Switch

**Inspect switch continuity**

| Switch position | Connected terminals |
| --------------- | ------------------- |
| OFF | (none) |
| LO  | 5–8 |
| II  | 2–4–8 |
| III | 1–4–8 |
| HI  | 4–6–8 |

If continuity is not as specified, replace the switch.

### Heater Relay

**1. Inspect relay continuity**

- (a) Check that there is continuity between terminals 1 and 3.
- (b) Check that there is continuity between terminals 2 and 4.
- (c) Check that there is no continuity between terminals 4 and 5.

If continuity is not as specified, replace the relay.

**2. Inspect relay operation**

- (a) Apply battery voltage across terminals 1 and 3.
- (b) Check that there is continuity between terminals 4 and 5.
- (c) Check that there is no continuity between terminals 2 and 4.

If operation is not as specified, replace the relay.

### Heater Blower Resistor

**Inspect resistor continuity** — check that there is continuity between terminals 2
and 3. If continuity is not as specified, replace the resistor.

### Heater Control Assembly

**1. Inspect indicator light operation**

- (a) Connect the positive (+) battery lead to terminal 11 and the negative (−)
  battery lead to terminal 3.
- (b) With the RECIRC/FRESH control button pushed in, check that the (RECIRC)
  indicator light is lit.
- (c) Next, press the RECIRC/FRESH control button in again (FRESH) and check that the
  indicator light goes off.
- (d) Press each of the mode buttons in and check that their indicator lights go on.

If operation is not as specified, replace the heater control.

**2. Inspect illumination operation** — check that the illumination lights come on
when the positive (+) battery lead is connected to terminal 12 and the negative (−)
battery lead is connected to terminal 14. If operation is not as specified, inspect
the bulbs.

**3. Inspect air vent mode switch continuity** — inspect the mode switch continuity
between terminals (columns 7, 6, 11, 17, 16, 5, 3).

| Switch position | Connected terminals |
| --------------- | ------------------- |
| FACE      | 6–3 |
| BI-LEVEL  | 6–11, 5–3 |
| FOOT      | 7–11, 16–3 |
| FOOT/DEF  | 11–5 |
| DEF       | 11–17 |

<!-- NEEDS REVIEW: Air vent mode switch continuity matrix (BE-37) is a very dense dot-matrix and the OCR/scan is ambiguous; connected-terminal groups above are a best-effort read — verify against page image p.833. -->

If continuity is not as specified, replace the switch.

### RECIRC/FRESH Control Servo Motor

**Inspect servo motor operation**

- (a) With the positive (+) lead from the battery to terminal 1 and negative (−) lead
  to terminal 2, check that the lever moves smoothly from RECIRC to FRESH.
- (b) With the positive (+) lead from the battery to terminal 1 and negative (−) lead
  to terminal 3, check that the lever moves smoothly from FRESH to RECIRC.

If operation is not as specified, replace the motor.

### Air Vent Mode Control Servo Motor

**Inspect servo motor operation**

- (a) Connect the positive (+) lead from the battery to terminal A1 and the negative
  (−) lead to terminal A5.
- (b) Check that the arm turns.
- (c) Connect the positive (+) lead from the battery to terminal A5 and the negative
  (−) lead to terminal A1.
- (d) Check that the arm turns the opposite way.
- (e) Check for continuity between terminals as shown in the position-encoder matrix.

The position-encoder continuity between terminals A2, A6, B1, B2, B3, B4, B5 for each
mode position (FACE, BI-LEVEL and the BI-LEVEL→FOOT, FOOT, FOOT→FOOT/DEF, FOOT/DEF,
FOOT/DEF→DEF, DEF transition positions) is a dense multi-contact matrix.

*(Figure: Air Vent Mode Control Servo Motor position-encoder continuity matrix — see
page image p.834)*

<!-- NEEDS REVIEW: Air vent mode control servo motor continuity matrix (BE-38) has many transition-position rows and 7 terminal columns; not reliably transcribable from the scan. Left as a figure reference — read directly from page image p.834. -->

If operation is not as specified, replace the servo motor.

### Heater Control — Adjustment

1. **Adjust air mix damper** — set the air mix damper and control lever to "COOL."
2. **Adjust water valve** — set the water valve and control lever to "COOL."

   > **NOTE:** Place the water valve lever on "COOL" and, while pushing the outer
   > cable in the "COOL" direction, clamp the outer cable to the water valve bracket.

---

## Cruise Control System

### Wiring Diagram

*(Figure: Cruise control system wiring diagram — actuator, cruise control computer,
control switch, ECT ECU, vacuum switch, alternator, brake fluid level warning switch
— see page image p.835)*

*(Figure: Cruise control connectors — Neutral Start Switch, Cruise Control Computer,
Control S/W, Parking Brake S/W, Clutch S/W, Stop Light S/W, Vacuum S/W, Vacuum Pump,
Actuator, Speed Sensor, ECT Computer, Alternator, Brake Fluid Level Warning Switch
pin layouts — see page image p.836)*

### Diagnosis System — Output of Diagnostic Codes

**1. Read Type A code**

- (a) Turn the ignition switch on.
- (b) Turn the set/coast switch on, and keep it on.
- (c) Turn the main switch on.
- (d) Turn the set/coast switch off.
- (e) Meet the conditions listed below.
- (f) Read the diagnostic code on the main switch indicator.

| No. | Conditions | Diagnosis (when normal) |
| --- | ---------- | ----------------------- |
| 1 | Set/coast switch on | Set/coast switch circuit is normal. |
| 2 | Resume/accel switch on | Resume/accel switch circuit is normal. |
| 3 | Vacuum switch on | Vacuum switch circuit is normal. |
| 4 | Each cancel switch on (stop light switch, parking brake switch, clutch switch, neutral start switch) | Each cancel switch circuit is normal. |
| 5 | Drive 40 km/h (25 mph) or over | Speed sensor circuit is normal. |
| 6 | Drive 30 km/h (19 mph) or below | Speed sensor circuit is normal. |

> **NOTE:**
> - Checking of No. 4 code is done with the rear jacked up and engine idling.
> - If there is no indication code, perform diagnosis and inspection. (See
>   Cruise Control Troubleshooting, BE-44)

**2. Read Type B code**

- (a) If, while driving with the cruise control on, the system is cancelled by a
  malfunction in either the actuator, speed sensor, or control switch circuit, the
  main switch indicator will blink 5 times.
- (b) While driving at a speed of 16 km/h (10 mph) or less, press the SET/COAST
  switch three times in two seconds.

  > **NOTE:** In order to save the diagnostic code when a malfunction has occurred,
  > always inspect with the ignition and main switches on. Should the power be cut,
  > the diagnostic code will be erased from the computer memory.
- (c) Read the diagnostic code on the main switch indicator.

| Indication code | Diagnosis |
| --------------- | --------- |
| (steady) | Normal |
| 11 | Actuator circuit is abnormal. |
| 21 | Speed sensor signal circuit is abnormal. |
| 23 | Speed sensor signal circuit is abnormal. / Actuator circuit is abnormal. |
| 31 | Resume/accel switch circuit is abnormal. |
| 33 | Resume/accel switch and set/coast switch circuit is abnormal. |

> **NOTE:**
> - Indication codes appear in order from No. 11.
> - Indication is stopped when vehicle speed is over 16 km/h (10 mph) or the main
>   switch is turned off.
> - If there is no indication code, perform diagnosis and inspection. (See
>   Cruise Control Troubleshooting, BE-44)

### Troubleshooting

| Problem | Inspection item | Result | Go to (chart) |
| ------- | --------------- | ------ | ------------- |
| Cruise control does not operate. | (a) Inspect type A codes. | No. 1 NO | B |
| | | No. 2 NO | C |
| | | No. 3 NO | J |
| | | No. 4 NO | F to I |
| | | No. 5 NO | E |
| | | No. 6 NO | E |
| | (b) Inspect type B codes. | 11 | D |
| | | 21 | E |
| | | 23 | D, E |
| | | 31 | C |
| | | 33 | B, C |
| | (c) All codes are normal. | — | A, D, E |
| Vehicle speed does not decrease when coast switch turned on. / does not fluctuate when set switch turned on. | Inspect No. 1 of type A code. | OK | D |
| | | NO | B |
| Vehicle speed does not accelerate when accel switch turned on. / does not return to memorized speed when resume switch turned on. | Inspect No. 2 of type A code. | OK | D |
| | | NO | C |
| Setting speed deviates on high side / low side. | — | — | D, E |
| Return and acceleration response is sluggish. | Inspect No. 3 of type A code. | OK | D |
| | | NO | J |
| Setting speed does not cancel when brake pedal depressed. | Inspect No. 4 of type A code. | OK | D |
| | | NO | F |
| Setting speed does not cancel when parking brake pulled up. | Inspect No. 4 of type A code. | OK | D |
| | | NO | G |
| Setting speed does not cancel when clutch pedal depressed (M/T only). | Inspect No. 4 of type A code. | OK | D |
| | | NO | H |
| Setting speed does not cancel when shifted to "N" range (A/T only). | Inspect No. 4 of type A code. | OK | D |
| | | NO | I |
| Speed can be set below about 40 km/h (25 mph). / Cruise control will not disengage even about 40 km/h (25 mph). | Inspect No. 5 / No. 6 of type A code. | OK | D |
| | | NO | E |
| A short period after the O/D cut (approx. within 14 seconds) the O/D will resume. | — | — | K |

### Chart A — Inspection of power source circuit

Turn ignition switch on.

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| Is TURN GAUGE fuse normal? | No | Replace fuse. If operation normal after replacing → fuse faulty. If not normal → short circuit in wire harness between TURN GAUGE fuse and terminal 16 of control switch; inspect control switch (BE-59). |
| | Yes | Go to Control S/W below. |
| **Control S/W:** Is there continuity between terminal 20 and body ground? | No | Open circuit in wire harness between terminal 20 of control switch and body ground; or body ground faulty. |
| | Yes | Continue. |
| Is there battery voltage between terminal 16 and body ground? | No | Open circuit in wire harness between TURN GAUGE fuse and terminal 16 of control switch. |
| | Yes | Continue. |
| Is there battery voltage between terminal 21 and body ground with main switch turned on? | No | Inspect control switch (BE-59). |
| | Yes | Continue. |
| Is there battery voltage between terminal 21 and body ground with main switch turned off? | Yes | Inspect control switch (BE-59). |
| | No | Continue. |
| Connect terminal 18 to body ground. Does indicator light light with main switch turned on? | No | Inspect control switch (BE-59). |
| | Yes | Continue. |
| Does indicator light light with main switch turned off? | Yes | Inspect control switch (BE-59). |
| | No | Go to Computer below. |
| **Computer:** Disconnect connector from computer; inspect wire harness side. Is there continuity between terminal 13 and body ground? | No | Open circuit in wire harness between terminal 13 and body ground; or body ground faulty. |
| | Yes | Continue. |
| Is there battery voltage between terminal 10 and body ground with main switch turned on? | No | Open circuit in wire harness between terminal 10 of computer and terminal 21 of control switch. |
| | Yes | Continue. |
| Connect terminal 3 to body ground. Does indicator light light with main switch turned on? | No | Open circuit in wire harness between terminal 3 of computer and terminal 18 of control switch. |
| | Yes | Continue. |
| Disconnect connector from control switch. Is there continuity between terminal 3 and body ground? | Yes | Short circuit in wire harness between terminal 3 of computer and terminal 18 of control switch. |
| | No | Replace computer. |

### Chart B — Inspection of set/coast switch circuit

Turn ignition switch off.

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| **Control S/W:** Disconnect connector. Is there continuity between terminal 20 of wire harness side connector and body ground? | No | Open circuit in wire harness between terminal 20 and body ground; or body ground faulty. |
| | Yes | Continue. |
| Is set/coast switch operation normal? (BE-59) | No | Replace control switch. |
| | Yes | Connect connector to control switch. |
| **Computer:** Disconnect connector; inspect wire harness side. Is there continuity between terminal 5 and body ground with set/coast switch turned on? | No | Open or short circuit in wire harness between terminal 5 of computer and terminal 14 of control switch. |
| | Yes | Replace computer. |

### Chart C — Inspection of resume/accel switch circuit

Turn ignition switch off.

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| **Control S/W:** Disconnect connector. Is there continuity between terminal 20 of wire harness side connector and body ground? | No | Open circuit in wire harness between terminal 20 and body ground; or body ground faulty. |
| | Yes | Continue. |
| Is resume/accel switch operation normal? (BE-59) | No | Replace control switch. |
| | Yes | Connect connector to control switch. |
| **Computer:** Disconnect connector; inspect wire harness side. Is there continuity between terminal 17 and body ground with resume/accel switch turned on? | No | Open or short circuit in wire harness between terminal 17 of computer and terminal 15 of control switch. |
| | Yes | Replace computer. |

### Chart D — Inspection of actuator circuit

Turn ignition switch off.

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| **Vacuum hose:** Are there cracks or other damage on the vacuum hose? | Yes | Replace vacuum hose. |
| | No | Continue. |
| **Actuator:** Is control cable freeplay less than 10 mm (0.39 in.)? | No | Adjust control cable freeplay. |
| | Yes | Continue. |
| Disconnect connector from actuator. Is actuator operation normal? (BE-61) | No | Replace actuator. |
| | Yes | Continue. |
| **Stop light S/W:** Disconnect connector from stop light switch. Is there continuity between terminal 4 of wire harness side connector and body ground? | Yes | Short circuit in wire harness between terminal 1 of actuator and terminal 4 of stop light switch. |
| | No | Connect connector to actuator. Is there continuity between terminal 4 and body ground? — No → open circuit between terminal 1 of actuator and terminal 4 of stop light switch. |
| Is stop light switch operation normal? (BE-59) | No | Replace stop light switch. |
| | Yes | Connect connector to stop light switch. |
| **Computer:** Disconnect connector; inspect wire harness side. Is there continuity between terminals 2 and 14 with stop light switch released? | No | Open circuit in wire harness between terminals 2 and 14 of computer. |
| | Yes | Continue. |
| Is there continuity between terminals 2 and 14 with stop light switch depressed? | Yes | Short circuit in wire harness between terminals 2 and 14 of computer. |
| | No | Continue. |
| Is there continuity between terminals 4 and 14? | No | Open circuit in wire harness between terminals 4 and 14 of computer. |
| | Yes | Replace computer. |

### Chart E — Inspection of speed sensor circuit

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| **Speedometer cable:** Does the meter fluctuate when driving at a steady speed? | Yes | Meter cable faulty. |
| | No | Turn ignition switch off. |
| **Speed sensor:** Disconnect connector from meter (speed sensor). Is there continuity between terminal B5 of wire harness side connector and body ground? | No | Open circuit in wire harness between terminal B5 and body ground. |
| | Yes | Continue. |
| Is speed sensor operation normal? (BE-60) | No | Speed sensor faulty. |
| | Yes | Continue. |
| **Computer:** Disconnect connector from computer. Is there continuity between terminal B4 of wire harness side connector and terminal 7 of computer? | No | Open circuit in wire harness between terminal B4 of speed sensor and terminal 7 of computer. |
| | Yes | Replace computer. |

### Chart F — Inspection of stop light switch circuit

Turn ignition switch off.

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| Is STOP fuse normal? | No | Replace fuse. If operation normal → fuse faulty. If not → short circuit in wire harness between terminal 16 of computer or terminal 1 of stop light switch and fuse. |
| | Yes | Continue. |
| **Stop light S/W:** Disconnect connector. Is there continuity between terminal 2 of wire harness side connector and body ground? | No | Open circuit in wire harness between terminal 2 and body ground; or body ground faulty. |
| | Yes | Continue. |
| Is stop light switch operation normal? (BE-59) | No | Replace stop light switch. |
| | Yes | Connect connector to stop light switch. |
| **Computer:** Disconnect connector; inspect wire harness side. Is there battery voltage between terminal 16 and body ground with brake pedal released? | No | Open circuit in wire harness between terminal 16 of computer and STOP fuse. |
| | Yes | Continue. |
| Is there battery voltage between terminal 15 and body ground with brake pedal depressed? | No | Open circuit in wire harness between terminal 15 of computer and terminal 2 of stop light switch. |
| | Yes | Replace computer. |

### Chart G — Inspection of parking brake switch circuit

Turn ignition switch off.

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| **Alternator:** Is alternator operation normal? (See Charging system, CH-4) | No | Replace alternator. |
| | Yes | Continue. |
| **Brake fluid level warning switch:** Disconnect connector. Is there continuity between terminal 2 of wire harness side connector and body ground? | No | Open circuit in wire harness between terminal 2 and body ground; or body ground faulty. |
| | Yes | Continue. |
| Is brake fluid level warning switch operation normal? (BE-29) | No | Replace brake warning switch. |
| | Yes | Connect connector to brake warning switch. |
| **Parking brake switch:** Disconnect connector. Is there continuity between terminal 2 of wire harness side connector and body ground? | No | Open circuit in wire harness between terminal 2 and body ground; or body ground faulty. |
| | Yes | Continue. |
| Is parking brake switch operation normal? (BE-60) | No | Replace parking brake switch. |
| | Yes | Connect connector to parking brake switch. |
| **Computer:** Disconnect connector; inspect wire harness side. Remove CHARGE fuse and turn ignition switch on. Is there no voltage between terminal 12 and body ground with parking brake pulled up? | No | Open circuit in wire harness between terminal 12 of computer and terminal 1 of parking brake switch. |
| | Yes | Continue. |
| Is there battery voltage between terminal 12 and body ground with parking brake released? | No | Short circuit in wire harness between terminal 12 of computer and terminal 1 of parking brake switch, terminal 1 of brake fluid level warning switch, or terminal 2 of alternator. |
| | Yes | Replace computer. |

### Chart H — Inspection of clutch switch circuit

Turn ignition switch off.

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| **Clutch S/W:** Disconnect connector. Is there continuity between terminal 2 of wire harness side connector and body ground? | No | Open circuit in wire harness between terminal 2 and body ground; or body ground faulty. |
| | Yes | Continue. |
| Is clutch switch operation normal? (BE-60) | No | Replace clutch switch. |
| | Yes | Connect connector to clutch switch. |
| **Computer:** Disconnect connector; inspect wire harness side. Is there continuity between terminal 11 and body ground with clutch pedal depressed? | No | Open circuit in wire harness between terminal 11 of computer and terminal 3 of clutch switch. |
| | Yes | Continue. |
| Is there continuity between terminal 11 and body ground with clutch pedal released? | Yes | Short circuit in wire harness between terminal 11 of computer and terminal 3 of clutch switch. |
| | No | Replace computer. |

### Chart I — Inspection of neutral start switch circuit

Turn ignition switch off.

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| **Neutral start S/W:** Disconnect connector. Is there continuity between terminal 2 of wire harness side connector and body ground? | No | Open circuit in wire harness between terminal 2 and body ground. |
| | Yes | Continue. |
| Is neutral start switch operation normal? (BE-60) | No | Replace neutral switch. |
| | Yes | Connect connector to neutral start switch. |
| **Computer:** Disconnect connector; inspect wire harness side. Is there continuity between terminal 11 and body ground when shifted to "N" and "P" range? | No | Open circuit in wire harness between terminal 11 of computer and terminal 3 of neutral start switch. |
| | Yes | Replace computer. |

### Chart J — Inspection of vacuum circuit

Turn ignition switch off.

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| **Vacuum hose:** Are there cracks or other damage on the vacuum hose? | Yes | Replace vacuum hose. |
| | No | Continue. |
| **Vacuum S/W:** Disconnect connector. Is there continuity between terminal 1 of vacuum switch and body ground? | No | Vacuum switch improperly installed; or body ground faulty. |
| | Yes | Continue. |
| Is vacuum switch normal? (BE-62) | No | Replace vacuum switch. |
| | Yes | Continue. |
| **Vacuum pump:** Disconnect connector. Is there continuity between terminal 2 of wire harness side connector and body ground? | No | Open circuit in wire harness between terminal 2 and body ground; or body ground faulty. |
| | Yes | Continue. |
| Is vacuum pump operation normal? (BE-62) | No | Replace vacuum pump. |
| | Yes | Connect connector to vacuum switch and pump. |
| **Computer:** Disconnect connector; inspect wire harness side. Is there continuity between terminal 9 and body ground? | No | Open circuit in wire harness between terminal 9 of computer and terminal 1 of vacuum switch. |
| | Yes | Start engine (idling). |
| Is there continuity between terminal 9 and body ground (engine idling)? | Yes | Short circuit in wire harness between terminal 9 of computer and terminal 1 of vacuum switch. |
| | No | Stop the engine. |
| Is there continuity between terminal 1 and body ground? | No | Open circuit in wire harness between terminal 1 of computer and terminal 1 of vacuum switch. |
| | Yes | Continue. |
| Is there continuity between terminal 1 and body ground with connector disconnected from vacuum pump? | Yes | Short circuit in wire harness between terminal 1 of computer and terminal 1 of vacuum pump. |
| | No | Replace computer. |

### Chart K — Inspection of ECT solenoid circuit

| Check | Result | Action / Next |
| ----- | ------ | ------------- |
| **Computer:** Disconnect connector; inspect wire harness side. Is there continuity between terminal 8 of wire harness side connector and terminal 11 of ECT computer? | No | Open circuit in wire harness between terminal 8 of computer and terminal 11 of ECT computer. |
| | Yes | Continue. |
| Is resistance value about 11 – 15 Ω between terminal 8 of wire harness side connector and body ground? | No | Open or short circuit in wire harness between terminal 8 of computer and terminal 11 of ECT computer, or ECT solenoid (No. 2). |
| | Yes | Continue. |
| Is there continuity between terminal 6 of wire harness side connector and terminal 17 of ECT computer? | No | Open circuit in wire harness between terminal 6 of computer and terminal 17 of ECT computer. |
| | Yes | Replace computer. |

### Cruise Control Computer Circuit

**Inspection of computer circuit** — disconnect the computer connector and inspect the
connector on the wire harness side as shown.

| Connection / measure item | Check for | Tester connection | Condition | Specified value |
| ------------------------- | --------- | ----------------- | --------- | --------------- |
| Stop Fuse | Voltage | 16 – Body ground | — | Battery voltage |
| Stop Light Switch | Voltage | 15 – Body ground | Brake pedal depressed | Battery voltage |
| | | | Brake pedal released | No voltage |
| Stop Light Switch and Release Valve | Resistance | 2 – 14 | Brake pedal released | Approx. 68 Ω |
| Control Valve | Resistance | 4 – 14 | — | Approx. 30 Ω <!-- NEEDS REVIEW: OCR dropped this value; page image p.854 clearly shows "Approx. 30 Ω" — read from image --> |
| Control Switch | Voltage | 10 – Body ground | Turn ignition switch and main switch on | Battery voltage |
| | | | Turn ignition switch and main switch off | No voltage |
| Control Switch (indicator circuit) | Voltage | 3 – Body ground | Turn ignition switch and main switch on | Battery voltage |
| | | | Turn ignition switch and main switch off | No voltage |
| Control Switch (set/coast) | Continuity | 5 – Body ground | Turn set/coast switch on | Continuity |
| | | | Turn set/coast switch off | No continuity |
| Control Switch (resume/accel) | Continuity | 17 – Body ground | Turn resume/accel switch on | Continuity |
| | | | Turn resume/accel switch off | No continuity |
| Speed Sensor | Continuity | 7 – Body ground | Vehicle moving slowly | 1 pulse each 40 cm (15.75 in.) |
| Clutch Switch (M/T) or Neutral Start Switch (A/T) | Continuity | 11 – Body ground | Clutch pedal depressed or shifted into "N" range | Continuity |
| | | | Clutch pedal released or shifted into any range except "N" and "P" | No continuity |
| Parking Brake Switch | Voltage | 12 – Body ground | Remove CHARGE fuse and ignition switch turned on with parking brake lever pulled up | No voltage |
| | | | Remove CHARGE fuse and ignition switch turned on with parking brake lever released | Battery voltage |
| Vacuum Switch | Continuity | 9 – Body ground | Apply vacuum approx. 170 mmHg (6.69 in.Hg, 22.7 kPa) | No continuity |
| | | | No vacuum | Continuity |
| Vacuum Pump | Continuity | 1 – Body ground | — | Continuity |
| Body Ground | Continuity | 13 – Body ground | — | Continuity |

### Control Switch

**1. Inspect switch continuity**

- (a) Connect the positive (+) lead from the battery to terminal 16 and the negative
  (−) lead to terminal 20.
- (b) Check that there is continuity between terminals 16 and 21 with the main switch
  turned on.
- (c) Check that there is no continuity between terminals 16 and 21 with the main
  switch turned off.

If continuity is not as specified, replace the switch.

**2. Inspect switch continuity** — inspect the switch continuity between terminals.

| Switch position | Connected terminals |
| --------------- | ------------------- |
| RESUME/ACCEL | 15–20 |
| OFF          | (none) |
| SET/COAST    | 14–20 |

If continuity is not as specified, replace the switch.

### Stop Light Switch

**Inspect switch continuity** — inspect the switch continuity between terminals.

| Switch position   | Connected terminals |
| ----------------- | ------------------- |
| Switch free       | 1–2 |
| Switch pin pushed | 3–4 |

If continuity is not as specified, replace the switch.

### Clutch Switch

**Inspect switch continuity**

- (a) Check that there is continuity between terminals 2 and 3 with the switch free.
  (Clutch pedal depressed)
- (b) Check that there is no continuity between terminals 2 and 3 with the switch pin
  pushed. (Clutch pedal released)

If continuity is not as specified, replace the switch.

### Parking Brake Switch

**Inspect switch continuity**

- (a) Check that there is continuity between the terminals with the switch free.
  (Parking brake lever pulled up)
- (b) Check that there is no continuity between the terminals with the switch pin
  pushed. (Parking brake lever released)

If continuity is not as specified, replace the switch.

### Neutral Start Switch

**Inspect switch continuity** — check that there is continuity between terminals 2 and
3 with switch position in "P" and "N" ranges. If continuity is not as specified,
replace the switch.

### Speed Sensor

**Inspect sensor continuity** — check that there is continuity between terminals B4
and B5 four times per each revolution of the shaft. If continuity is not as specified,
replace the sensor.

### Actuator

**1. Inspect actuator resistance** — measure the resistance value between terminals as
follows.

- **Resistance:** 2 – 3 approx. 30 Ω; 1 – 3 approx. 68 Ω

If the resistance value is not as specified, replace the actuator.

**2. Inspect actuator operation**

- (a) Connect the positive (+) lead from the battery to terminals 1 and 2, and the
  negative (−) lead to terminal 3.
- (b) Slowly apply vacuum from 0 – 300 mmHg (0 – 11.81 in.Hg, 0 – 40.0 kPa), and check
  that the control cable can be pulled smoothly.
- (c) Disconnect terminal 1 or 2 and check that the control cable returns to its
  original position and the vacuum returns to 0 mmHg (0 in.Hg, 0 kPa).

If operation is not as specified, replace the actuator.

**3. Inspect control cable freeplay**

- (a) Connect the positive (+) lead from the battery to terminals 1 and 2, and the
  negative (−) lead to terminal 3.
- (b) Slowly apply vacuum from 0 – 300 mmHg (0 – 11.81 in.Hg, 0 – 40.0 kPa), and
  measure the cable stroke to where the throttle valve begins to open.
- **Standard:** Approx. within 10 mm (0.39 in.) with a slight amount of freeplay.

If freeplay is not as specified, adjust the control cable freeplay.

### Vacuum Switch

**Inspect switch operation**

- (a) Check that there is no continuity between terminal and body with a vacuum of
  170 ± 10 mmHg (6.69 ± 0.39 in.Hg, 22.7 ± 1.3 kPa) or above.
- (b) Check that there is continuity between terminal and body with no vacuum.

If operation is not as specified, replace the switch.

### Vacuum Pump

**Inspect vacuum pump operation**

- (a) Connect a vacuum gauge to the ACT side of the pump.
- (b) Connect the positive (+) lead from the battery to terminal 1 and the negative
  (−) lead to terminal 2.
- (c) Check that there is a vacuum of 200 mmHg (7.87 in.Hg, 26.7 kPa) or above.

If operation is not as specified, replace the pump.

---

## Power Window

### Power Window Master Switch

**Inspect switch continuity** — inspect the switch continuity between terminals.
Driver's side terminals: 2, 8, 9; passenger's side terminals: 3, 6, 1, 4.

| Group | Switch position | Connected terminals |
| ----- | --------------- | ------------------- |
| Window unlock | Up   | 2–3–6, 1–4 |
| Window unlock | OFF  | 1–4, 6–4 |
| Window unlock | DOWN | 3–6, 6–4 |
| Window lock   | UP   | 2–3–6 |
| Window lock   | OFF  | 6–1 |
| Window lock   | DOWN | 3–6, 6–4 |
| (Auto)        | AUTO | 2–8–9 |

<!-- NEEDS REVIEW: Power window master switch continuity matrix (BE-63) is a dense dot-matrix with parallel driver/passenger contacts; connected-terminal groups above are a best-effort read from page image p.859 — verify against the page image. -->

If continuity is not as specified, replace the switch.

### Power Window Door Switch

**Inspect switch continuity** — inspect the switch continuity between terminals
(columns 3, 4, 7, 8, 9).

| Switch position | Connected terminals |
| --------------- | ------------------- |
| UP   | 4–7, 8–9 |
| OFF  | 3–4, 7–9 |
| DOWN | 3–4, 8–9 |

<!-- NEEDS REVIEW: Power window door switch continuity (BE-63) read from page image p.859 — verify dot positions. -->

If continuity is not as specified, replace the switch.

### Power Window Relay

**On-vehicle inspection of power window relay**

- (a) Disconnect the relay connector and inspect the connector on the wire harness
  side as shown in the table below.

| Check for | Tester connection | Condition | Specified value |
| --------- | ----------------- | --------- | --------------- |
| Voltage | 2 – Body ground | Turn ignition switch on. | Battery voltage |
| | | Turn ignition switch off. | No voltage |
| Continuity | 3 – Body ground | — | Continuity |
| Voltage | 5 – Body ground | Turn master switch to UP. | Battery voltage |
| | | Turn master switch to except UP. | No voltage |
| Voltage | 8 – Body ground | Turn master auto switch to DOWN. | Battery voltage |
| | | Turn master auto switch to OFF. | No voltage |
| Voltage | 9 – Body ground | Turn master switch or master auto switch to DOWN. | Battery voltage |
| | | Turn master switch or master auto switch to except DOWN. | No voltage |

- (b) Connect the positive (+) lead from the battery to terminal 1 and negative (−)
  lead to terminal 4; check that the window operates up. Then reverse the polarity;
  check that the window operates down. If it does not operate, remove and test the
  motor.

If circuit operation is correct, replace the motor.

### Power Window Motor

**1. Inspect motor operation**

- (a) Connect the positive (+) lead from the battery to terminal 1 and negative (−)
  lead to terminal 2, and check that the motor turns.
- (b) Connect the positive (+) lead from the battery to terminal 2 and negative (−)
  lead to terminal 1, and check that the motor turns the opposite way.

If operation is not as specified, replace the motor.

**2. Inspect circuit breaker operation**

- (a) With the window fully closed, hold the power window switch on "UP" and check
  that there is circuit breaker operation noise within 4 to 40 seconds.
- (b) With the window fully closed, hold the switch on "DOWN" and check that the
  window begins to descend within 60 seconds.

If operation is not as specified, replace the motor.

---

## Door Lock Control System

### Door Lock Switch

**Inspect switch continuity** — inspect the switch continuity between terminals.

**Driver's side** (terminals 12, 5, 4):

| Switch position | Connected terminals |
| --------------- | ------------------- |
| LOCK   | 5–4 |
| OFF    | (none) |
| UNLOCK | 12–4 |

**Passenger's side** (terminals 2, 5, 6):

| Switch position | Connected terminals |
| --------------- | ------------------- |
| LOCK   | 2–5 |
| OFF    | (none) |
| UNLOCK | 5–6 |

If continuity is not as specified, replace the switch.

### Unlock Warning Switch

See [Ignition Switch](#ignition-switch) (BE-11).

### Door Lock Key Switch

**Inspect switch continuity**

- (a) Check that there is continuity between terminals 2 and 3 with the switch free.
  (Switch to Lock)
- (b) Check that there is continuity between terminals 1 and 2 with the switch pin
  pushed. (Switch to unlock)

If continuity is not as specified, replace the switch.

### Door Lock Control Relay

**Inspect relay operation**

- (a) Disconnect the relay connector and inspect the connector on the wire harness
  side as shown in the table.

| Check for | Tester connection | Condition | Specified value |
| --------- | ----------------- | --------- | --------------- |
| Continuity | 1 – Body ground | LH door opened | Continuity |
| | | LH door closed | No continuity |
| Voltage | 2 – Body ground | — | Battery voltage |
| Continuity | 6 – Body ground | Turn the following switches, one by one, to lock: Control switch LH, LH door key switch, RH door key switch, Control switch RH | Continuity |
| | | Turn the following switches, one by one, to except lock | No continuity |
| Continuity | 7 – Body ground | RH door opened | Continuity |
| | | RH door closed | No continuity |
| Continuity | 9 – Body ground | LH door lock switch to unlock | Continuity |
| | | LH door lock switch to lock | No continuity |
| Continuity | 10 – Body ground | — | Continuity |
| Continuity | 11 – Body ground | RH door lock switch to unlock | Continuity |
| | | RH door lock switch to lock | No continuity |
| Continuity | 12 – Body ground | Set the ignition key switch | Continuity |
| | | Remove the ignition key switch | No continuity |
| Continuity | 13 – Body ground | Turn the following switches, one by one, to unlock: Control switch LH, LH door key switch, RH door key switch, Control switch RH | Continuity |
| | | Turn the following switches, one by one, to except unlock | No continuity |

- (b) Connect the positive (+) lead from the battery to terminal 3 and negative (−)
  lead to terminal 4; check that the solenoids operate in the unlock direction. Then
  reverse the polarity; check that the solenoids operate in the lock direction. If
  any of the solenoids does not operate, remove and test the solenoid.

If circuit operation is correct, replace the relay.

### Door Lock Solenoid

**Inspect solenoid operation**

- (a) Connect the positive (+) lead from the battery to terminal 1. Connect the
  negative (−) lead to terminal 2. Check that the solenoid operates in the lock
  direction.
- (b) Check that there is no continuity between terminals 3 and 4.
- (c) Connect the positive (+) lead from the battery to terminal 2. Connect the
  negative (−) lead to terminal 1. Check that the solenoid operates in the unlock
  direction.
- (d) Check that there is continuity between terminals 3 and 4.

If operation is not as specified, replace the solenoid.

---

## Remote Control Mirror

### Mirror Switch

**Inspect switch continuity** — inspect the switch continuity between terminals. Left
mirror terminals: 7, 6, 1, 2, 3; right mirror terminals: 2, 1, 5, 4. (Terminals 1 and
2 appear in both the left and right terminal groups on the connector.)

| Switch position | Left mirror | Right mirror |
| --------------- | ----------- | ------------ |
| UP    | 7–1, 2–3–2 | 1–4 |
| DOWN  | 1–3–1, 7–2 | 2–4 |
| LEFT  | 6–1, 2–3–2 | 1–5 |
| RIGHT | 1–3–1, 6–2 | 2–5 |

<!-- NEEDS REVIEW: Remote control mirror switch is a joystick with shared terminal numbers across the left/right groups (BE-68); connected-terminal groups above are a best-effort read from page image p.864 — verify against the page image. -->

If continuity is not as specified, replace the switch.

### Remote Control Mirror

**On-vehicle inspection of mirror**

- (a) Connect the positive (+) lead from the battery to terminal 1 and the negative
  (−) lead to terminal 2. Check that the mirror moves upward.
- (b) Connect the leads in reverse. Check that the mirror moves downward.
- (c) Connect the positive (+) lead from the battery to terminal 3 and the negative
  (−) lead to terminal 2. Check that the mirror moves to the left.
- (d) Connect the leads in reverse. Check that the mirror moves to the right.

If operation is not as specified, replace the mirror.

---

## Radio, Stereo Tape Player and Antenna

### Troubleshooting

**Description of symbols**

- ☐ — Inspection
- ○ — Check or replace part
- Ⓒ — Test by operating radio

**1. Dead radio and tape player**

- (a) No power to radio or tape player, or power but no sound.

  Possible causes:
  - Blown CIG-RADIO fuse
  - Short circuit or broken wire in power source wire harness
  - Loose connectors behind radio and tape player
  - Loose speaker connector
  - Defective speaker
  - Broken wire in speaker wire harness
  - Improperly installed radio or tape player
  - Defective radio or tape player

  **Test 1** — Check CIG-RADIO fuse.

  | Check | Result | Action / Next |
  | ----- | ------ | ------------- |
  | Check CIG-RADIO fuse. | OK | Proceed to Test 2. |
  | | Blown | Replace fuse. If it does not blow → OK. If it blows again → check for short circuit in power source wire harness. |
  | Check for short circuit in power source wire harness. | No short | Replace radio and tape player. |
  | | Short | Inspect and repair wire harness for radio and tape player. |

  **Test 2**

  | Check | Result | Action / Next |
  | ----- | ------ | ------------- |
  | Are all connectors behind radio and tape player properly connected? | Yes | Proceed to Test 3. |
  | | No (connectors) | Connect properly. |
  | | No (power harness) | Inspect and repair power wire harness to radio and player. |
  | | No (installation) | Properly re-install. |

  **Test 3**

  | Check | Result | Action / Next |
  | ----- | ------ | ------------- |
  | Are speaker connectors connected? | — | Replace speaker (if speaker defective). |
  | | No | Connect properly. |
  | Is there continuity in speaker wire harness? | No | Inspect and repair speaker wire harness. |
  | | (w/o player) | Proceed to Test 1 of following item. |
  | | (radio and player faulty) | Replace radio and tape player. |

- (b) Tape player okay but no sound from either the AM or FM band.

  Possible causes:
  - Antenna disconnected
  - Antenna plug not properly connected
  - Defective antenna
  - Defective antenna cable
  - Defective radio or tape player
  - Blown HAZ-RADIO fuse
  - Short circuit or broken wire in wire harness for back-up power source

  **Test 1**

  | Check | Result | Action / Next |
  | ----- | ------ | ------------- |
  | Is radio electronic search type? | Yes | Is either AM or FM okay? — Yes → Proceed to Test 2. |
  | | No | Proceed to Test 3. |

  **Test 2**

  | Check | Result | Action / Next |
  | ----- | ------ | ------------- |
  | Check HAZ-RADIO fuse. | OK | Is there back-up power to connectors behind radio? — Yes → Proceed to Test 3. — No → inspect and repair back-up power wire harness. |
  | | Blown | Replace fuse. If it does not blow → OK. If it blows again → check for short circuit in back-up power source wire harness (Short → inspect and repair wire harness for back-up power source). |

  > **NOTE:** Back-up power refers to the storage voltage for preset tuning. This is
  > applied even when the ignition switch is OFF.

  **Test 3**

  | Check | Result | Action / Next |
  | ----- | ------ | ------------- |
  | Check that antenna plug is secure in radio. | OK | Inspect antenna plug. Reinsert plug — okay? → OK. |
  | | Loose | Properly insert. Does radio alone work? — Yes → Replace tape player. — No → Proceed to Test 4. |
  | **Test 4:** Temporarily install another antenna. Okay? | OK | Inspect antenna and antenna cable, and replace as necessary. |
  | | No | Replace radio. |

---

*This chapter covers manual pages BE-1 through BE-71. The remainder of the Radio /
Antenna section and the Clock (BE-72 through BE-76) continue in Body Electrical
System, Part 2.*
