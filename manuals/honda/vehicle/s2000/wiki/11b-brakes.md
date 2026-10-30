# Brakes (Part B)

Honda S2000 service manual, PDF pp. 1200–1265. Continues the brakes chapter with 2006–08 VSA components, diagnostics, wiring, and component service (printed pp. 19-68–19-129). PDF pp.1200 and 1264 are blank scans; p.1265 is an SRS notice.

---

### Printed page blank

<a id="p1200"></a>
Source: [PDF p.1200](../page-images/p1200.png).

*This source page is blank apart from a black scanning artifact. No service content is recoverable.*

---

### Printed page contents

<a id="p1201"></a>
Source: [PDF p.1201](../page-images/p1201.png).

# Brakes — contents (continued)

- Conventional brake components: 19-1.
- ABS components (2000–05): 19-31.
- VSA components (2006–08): component location index 19-68; general troubleshooting 19-69; DTC index 19-72; symptom index 19-74; system description 19-75; circuit diagram 19-86; DTC troubleshooting 19-89; symptom troubleshooting 19-112; steering angle sensor replacement 19-124; sensor cluster replacement and VSA neutral-position memorization 19-125; VSA OFF switch test 19-126; VSA modulator-control unit removal/installation 19-127; wheel-speed sensor inspection and replacement 19-129.

---

### Printed page 19-68

<a id="p1202"></a>
Source: [PDF p.1202](../page-images/p1202.png).

# VSA component location index

The source image locates these items on the vehicle: VSA OFF switch, steering angle sensor, data link connector (DLC), main under-hood fuse/relay box, under-dash fuse/relay box, sensor cluster, VSA modulator-control unit, and right/left front and rear wheel-speed sensors. Use the linked diagram for exact positions.

| Component | Service reference |
| --- | --- |
| VSA OFF switch | Test, 19-126 |
| Steering angle sensor | Replacement, 19-124 |
| Sensor cluster | Replacement, 19-125 |
| VSA modulator-control unit | Removal and installation, 19-127 |
| Each of the four wheel-speed sensors | Inspection and replacement, 19-129 |

---

### Printed page 19-69

<a id="p1203"></a>
Source: [PDF p.1203](../page-images/p1203.png).

# Page 1203: General Troubleshooting Information - System Indicator

## System Indicator
This system has four indicators:
*   **ABS indicator (A)**
*   **Brake system indicator (B)**
*   **VSA indicator (C)**
*   **VSA activation indicator (D)**

When the system detects a problem, it will turn the appropriate indicator on. Depending on the failure, the VSA modulator-control unit determines which indicators are turned on.

When the system is OK, each indicator comes on for about 2 seconds after turning the ignition switch to ON (II), then goes off.

---

## ABS Indicator
The **ABS** indicator comes on when the **ABS** function is lost. The brakes still work like a conventional system.

---

## Brake System Indicator
The brake system indicator comes on when the EBD function is lost, the parking brake is applied, and/or the brake fluid level is low.

---

## VSA Indicator
The **VSA** indicator comes on, when **VSA** function is lost.

---

## ABS/VSA Indicator
*   If the system is OK, the **ABS** and **VSA** indicators go off 2 seconds after turning the ignition switch to ON (II).
*   The **ABS** and **VSA** indicators come on when the control unit detects a problem in the system.

However, even though the system is operating properly, the indicator may come on under these conditions:
1.  Only the drive wheels rotate.
2.  One drive wheel is stuck.
3.  The vehicle goes into a spin.
4.  The **ABS** or **VSA** continues to operate for a long time.
5.  The vehicle is subjected to an electrical signal disturbance.

To determine the actual cause of the problem, question the customer, taking these conditions into consideration.

*   When a problem is detected, there are cases when the indicator stays on until the ignition switch is turned to LOCK (0), and cases when the indicator goes off automatically when the system returns to normal.

### Indicator Behavior by DTC

**DTC 61 or 62:**
The **ABS** and **VSA** indicators go off automatically when the system returns to normal.

**DTC 31, 32, 33, 34, 35, 36, 37, 38, 54, 81, 121, 122, 123 or 124:**
The **ABS** and **VSA** indicators stay on until the ignition switch is turned to LOCK (0) whether or not the system returns to normal.

**DTC 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 51 or 52:**
The **ABS** and **VSA** indicators stay on until the system returns to normal after the engine is restarted, and the vehicle is driven.

**DTC 25, 26, 27, 64, 65, 66, 68, 83, 86, 91, 104 or 105:**
The **VSA** indicator stays on until the ignition switch is turned to LOCK (0) whether or not the system returns to normal.

**DTC 84:**
The **VSA** activation indicator go off automatically when the system returns to normal.

---

## VSA Activation Indicator
The **VSA** activation indicator blinks, when the **VSA** function is activating. The **VSA** activation indicator comes on, when the **VSA** is turned OFF by using the **VSA** OFF switch, or the **VSA** function is lost.

---

### Printed page 19-70

<a id="p1204"></a>
Source: [PDF p.1204](../page-images/p1204.png).

# VSA System Components
## General Troubleshooting Information
### Diagnostic Trouble Code (DTC)
* The memory can hold any number of DTCs. However, when the same DTC is detected more than once, the more recent DTC is written over the earlier one. Therefore, when the same problem is detected repeatedly, it is memorized as a single DTC.
* The DTCs are indicated in ascending number order, not in the order they occur.
* The DTCs are memorized in the EEPROM. Therefore, the memorized DTCs cannot be erased by disconnecting the battery. Do the specified procedures to clear the DTCs.

### Self-diagnosis
* Self-diagnosis can be classified into two categories:
  * Initial diagnosis: Done right after the ignition switch is turned to ON (II) and until the ABS and VSA indicators go off.
  * Regular diagnosis: Done right after the initial diagnosis until the ignition switch is turned to LOCK (0).
* When the system detects a problem, the VSA modulator-control unit shifts to fail-safe mode.

### Kickback
The pump motor operates when the VSA modulator-control unit is functioning, and the fluid in the reservoir is forced out to the master cylinder, causing kickback at the brake pedal.

### Pump Motor
* The pump motor operates when the VSA modulator-control unit is functioning.
* The VSA modulator-control unit checks the pump motor operation one time after completing initial diagnosis during regular diagnosis when the vehicle is driven over 12 mph (20 km/h). You may hear the motor operate at this time, but it is normal.

### Brake Fluid Replacement/Air Bleeding
Brake fluid replacement and air bleeding procedures are identical to the procedures used on vehicles without the VSA system (see page 19-9).

---
## How to Troubleshoot DTCs
The troubleshooting procedures assume that the cause of the problem is still present and the ABS and/or VSA indicator is still on. Following the troubleshooting procedure when the ABS and/or VSA indicator does not come on (no problem is present) can result in incorrect diagnosis.

The connector illustrations show the female terminal connectors with a single outline and the male terminal connectors with a double outline.

1. Question the customer about the conditions when the problem occurred, and try to reproduce the same conditions for troubleshooting. Find out when the ABS and/or VSA indicator came on, such as during activation, after activation, when the vehicle was traveling at a certain speed, etc. If necessary, have the customer demonstrate the concern.
2. When the ABS or VSA indicator does not come on during the test-drive, but troubleshooting is done based on the DTC, check for loose connectors, poor contact of the terminals, etc. before you start troubleshooting.
3. After troubleshooting, or repairs are done, clear the DTCs, and test-drive the vehicle under the same conditions as originally set with the DTCs. Make sure the ABS and VSA indicators do not come on.
4. Check for DTCs from other systems which connected via F-CAN, if there are DTCs that are related to F-CAN, the most likely cause was that the ignition switch was turned to ON (II) with the VSA modulator-control unit connector disconnected. Clear the DTCs. Check for fuel and emissions codes, and troubleshoot those first.

### Intermittent Failures
The term "intermittent failure" means a system may have had a failure, but it checks OK now. If the indicator(s) of the system does not come on, check for loose connectors and grounds, poor contact of the terminals related to the circuit that you are troubleshooting.

---

### Printed page 19-71

<a id="p1205"></a>
Source: [PDF p.1205](../page-images/p1205.png).

# How to Use the HDS (Honda Diagnostic System)

## General Procedure
1. If the system indicators stay on, connect the HDS to the data link connector (DLC) (A) located under the driver's side of the dashboard.
2. Turn the ignition switch to ON (II).
3. Make sure the HDS communicates with the vehicle and the VSA modulator-control unit. If it doesn't, troubleshoot the DLC circuit (see page 11-367).
4. Check the diagnostic trouble code (DTC) and note it. Then refer to the indicated DTC troubleshooting, and do the appropriate troubleshooting procedure.

**NOTE:**
* The HDS can read the DTC, the current data, and other system data.
* For specific operations, refer to the Help menu that came with the HDS.

---

## How to Retrieve DTCs
1. With the ignition switch at LOCK (0), connect the HDS to the data link connector (DLC) under the driver's side of the dashboard.
2. Turn the ignition switch to ON (II).
3. Make sure the HDS communicates with the vehicle and the VSA modulator-control unit. If it doesn't, troubleshoot the DLC circuit (see page 11-367).
4. Follow the prompts on the HDS to display the DTC(s) on the screen. After determining the DTC, refer to the DTC troubleshooting.
5. Turn the ignition switch to LOCK (0).

---

## How to Clear DTCs
1. With the ignition switch at LOCK (0), connect the HDS to the data link connector (DLC) under the driver's side of the dashboard.
2. Turn the ignition switch to ON (II).
3. Make sure the HDS communicates with the vehicle and the VSA modulator-control unit. If it doesn't, troubleshoot the DLC circuit (see page 11-367).
4. Clear the DTC(s) by following the screen prompts on the HDS.
5. Turn the ignition switch to LOCK (0).

---

### Printed page 19-72

<a id="p1206"></a>
Source: [PDF p.1206](../page-images/p1206.png).

# VSA DTC troubleshooting index (11–38)

| DTC | Detection item | ABS indicator | Brake system indicator | VSA indicator | VSA activation indicator | See |
| --- | --- | --- | --- | --- | --- | --- |
| 11, 13, 15, 17 | Right-front, left-front, right-rear, left-rear wheel-speed sensor: short to power, short to ground, or open | ON | ON or OFF* | ON | ON | 19-89 |
| 12, 14, 16, 18 | Corresponding wheel-speed sensor: electrical noise or intermittent interruption | ON | ON or OFF* | ON | ON | 19-92 |
| 21, 22, 23, 24 | Right-front, left-front, right-rear, left-rear pulser | ON | ON or OFF* | ON | ON | 19-94 |
| 25 | Yaw rate sensor | OFF | OFF | ON | ON | 19-94 |
| 26 | Lateral acceleration sensor | OFF | OFF | ON | ON | 19-94 |
| 27 | Steering angle sensor | OFF | OFF | ON | ON | 19-96 |
| 31–38 | ABS solenoid | ON | ON | ON | ON | 19-98 |

*Brake system indicator turns ON when two or more wheels fail.*

---

### Printed page 19-73

<a id="p1207"></a>
Source: [PDF p.1207](../page-images/p1207.png).

# VSA DTC troubleshooting index (51–124)

| DTC | Detection item | ABS indicator | Brake system indicator | VSA indicator | VSA activation indicator | See |
| --- | --- | --- | --- | --- | --- | --- |
| 51 | Motor lock | ON | OFF | ON | ON | 19-98 |
| 52 | Motor stuck ON/OFF | ON | OFF | ON | ON | 19-98 |
| 54 | Fail-safe relay | ON | ON | ON | ON | 19-99 |
| 61 | Low +B-FSR voltage | ON | ON or OFF | ON | ON | 19-100 |
| 62 | High +B-FSR voltage | ON | ON | ON | ON | 19-100 |
| 64 | Sensor power voltage | OFF | OFF | ON | ON | 19-100 |
| 65 | Brake fluid level | OFF | OFF | ON | ON | 19-101 |
| 66 | VSA pressure sensor (inside modulator-control unit) | OFF | OFF | ON | ON | 19-102 |
| 68 | Brake pedal position switch | OFF | OFF | ON | ON | 19-102 |
| 81 | Central processing unit (CPU) | ON or OFF | ON or OFF | ON | ON | 19-103 |
| 83 | ECM communication | OFF | OFF | ON | ON | 19-104 |
| 84 | VSA sensor neutral position | OFF | OFF | OFF | ON | 19-104 |
| 86 | F-CAN communication | OFF | OFF | ON | ON | 19-105 |
| 91 | VSA operation | OFF | OFF | ON | ON | 19-108 |
| 104 | Sensor cluster | OFF | OFF | ON | ON | 19-94 |
| 105 | Hydraulic unit temperature sensor | OFF | OFF | ON | ON | 19-111 |
| 121–124 | VSA solenoid | ON | ON | ON | ON | 19-111 |

*The source footnote states that the brake system indicator turns ON when two or more wheels fail.*

---

### Printed page 19-74

<a id="p1208"></a>
Source: [PDF p.1208](../page-images/p1208.png).

# VSA System Components

## Symptom Troubleshooting Index

When the vehicle has one of these symptoms, check for a diagnostic trouble code (DTC) with the HDS. If there is no DTC, do the diagnostic procedure for the symptom, in the sequence listed, until you find the cause.

| Symptom | Diagnostic procedure |
| :--- | :--- |
| HDS does not communicate with the VSA modulator-control unit or the vehicle | Troubleshoot the DLC circuit (see page 11-367) |
| ABS indicator does not come on | Symptom Troubleshooting (see page 19-112) |
| ABS indicator does not go off, and no DTCs are stored | Symptom Troubleshooting (see page 19-113) |
| Brake system indicator does not come on | Symptom Troubleshooting (see page 19-115) |
| Brake system indicator does not go off, and no DTCs are stored | Symptom Troubleshooting (see page 19-117) |
| VSA indicator does not come on | Symptom Troubleshooting (see page 19-119) |
| VSA indicator does not go off, and no DTCs are stored | Symptom Troubleshooting (see page 19-120) |
| VSA activation indicator does not come on at start-up (bulb check) | Symptom Troubleshooting (see page 19-122) |
| VSA activation indicator does not go off, and no DTCs are stored | Symptom Troubleshooting (see page 19-122) |

---

### Printed page 19-75

<a id="p1209"></a>
Source: [PDF p.1209](../page-images/p1209.png).

# VSA modulator-control unit 47P connector — inputs and outputs

Connector drawing is viewed from the **wire side of female terminals**. See the source image for cavity layout. Measurements require disconnecting the 47P connector.

| Terminal | Wire | Sign | Function | Test terminals | Conditions | Result |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | WHT/BLU | +B-P | Pump-motor power | 1–GND | At all times | Battery voltage |
| 2 | GRY | K-LINE | HDS communication | — | — | — |
| 4 | BLK/YEL | IG1 | System power | 4–GND | Ignition ON (II) | Battery voltage |
| 6 | GRN/WHT | CLST-IG | Sensor-cluster power | — | — | — |
| 9 | GRN/RED | BFLS | Brake-fluid-level switch | 9–GND | Ignition ON (II), fluid level high | Battery voltage |
| 9 | GRN/RED | BFLS | Brake-fluid-level switch | 9–GND | Ignition ON (II), fluid level low | 1.0 V or less |
| 11 | RED | CAN1-H | F-CAN circuit | — | — | — |
| 13 | PNK | WL-EBD | Brake-system indicator | 13–GND | Ignition ON (II) | Battery voltage |
| 15 | WHT | CAN1-L | F-CAN circuit | — | — | — |
| 16 | BLK | GND-V | Unit ground | 16–GND | At all times | Continuity |
| 17 | PNK/BLK | VSA | VSA indicator | 17–GND | Ignition ON (II) | Battery voltage |
| 25 | RED | CAN2-L | CAN2 circuit | — | — | — |
| 27 | WHT | VSA OFF SW | VSA OFF switch signal | — | — | — |
| 29 | WHT | CAN2-H | CAN2 circuit | — | — | — |

---

### Printed page 19-76

<a id="p1210"></a>
Source: [PDF p.1210](../page-images/p1210.png).

# VSA modulator-control unit 47P connector — inputs and outputs (continued)

Connector drawing is viewed from the **wire side of female terminals**. See the source image for cavity layout. Measurements require disconnecting the 47P connector.

| Terminal | Wire | Sign | Function | Test terminals | Conditions | Result |
| --- | --- | --- | --- | --- | --- | --- |
| 31 | LT GRN | CLST-GND | Sensor-cluster ground | — | — | — |
| 32 | WHT/RED | +B-V | Fail-safe-relay power | 32–GND | At all times | Battery voltage |
| 33 | BLU | FRS (−) | Right-front wheel-speed sensor signal | — | — | — |
| 34 | GRN/BLK | FRS (+) | Right-front wheel-speed sensor signal | — | — | — |
| 35 | GRN | ACT | VSA activation indicator | 35–GND | Ignition ON (II) | Battery voltage |
| 36 | YEL/RED | RLS (+) | Left-rear wheel-speed sensor signal | — | — | — |
| 37 | GRY/RED | RLS (−) | Left-rear wheel-speed sensor signal | — | — | — |
| 42 | BLU/YEL | RRS (−) | Right-rear wheel-speed sensor signal | — | — | — |
| 43 | GRN/WHT | RRS (+) | Right-rear wheel-speed sensor signal | — | — | — |
| 44 | BLU/RED | ABS | ABS indicator | 44–GND | Ignition ON (II) | Battery voltage |
| 45 | BLU/ORN | FLS (+) | Left-front wheel-speed sensor signal | — | — | — |
| 46 | BRN/WHT | FLS (−) | Left-front wheel-speed sensor signal | — | — | — |
| 47 | BLK | GND-P | Pump-motor ground | 47–GND | At all times | Continuity |

---

### Printed page 19-77

<a id="p1211"></a>
Source: [PDF p.1211](../page-images/p1211.png).

# ABS Features

When the brake pedal is pressed while driving, the wheels can lock before the vehicle comes to a stop. In such an event, the maneuverability of the vehicle is reduced if the front wheels are locked, and the stability of the vehicle is reduced if the rear wheels are locked, creating an extremely unstable condition. The ABS precisely controls the slip rate of the wheels to ensure maximum grip force from the tires, and it thereby ensures maneuverability and stability of the vehicle.

The ABS calculates the slip rate of the wheels based on the vehicle speed and the wheel speed, and then it controls the brake fluid pressure to reach the target slip rate.

## Grip force of tire and road surface

### SLIP RATE


# T C S Features

The T C S provides low-speed traction. When a drive wheel loses traction on a slippery road surface and starts to spin, the VSA modulator-control unit applies brake pressure to slow the spinning wheel. At that time, the VSA modulator-control unit sends a traction control signal to the E C M to reduce engine power.

| NORMAL ROADSURFACE | SLIPPERY ROAD SURFACE |
| :--- | :--- |

---

### Printed page 19-78

<a id="p1212"></a>
Source: [PDF p.1212](../page-images/p1212.png).

# VSA System Components
## System Description (cont'd)
### VSA System Features

#### Oversteer control
* Applies the brake to the front and rear outside wheels
* The brake makes the yaw rate opposite to the turning direction

#### Understeer control
* Applies the brake to the rear inside wheel
* Controls the engine torque when accelerating
* The brake increases the yaw rate toward the turning direction
* The throttle control effect:
  * reduces vehicle speed
  * increases cornering force

---

### Printed page 19-79

<a id="p1213"></a>
Source: [PDF p.1213](../page-images/p1213.png).

# Electronic Brake Distribution (EBD)

Electronic brake distribution (EBD) has been added to the VSA system. EBD eliminates the need for an external, mechanical proportioning valve and improves overall braking performance.

When the vehicle is heavily loaded, most of the increase in weight is borne by the rear wheels, increasing braking capability. Proportioning valves maintain a fixed distribution of brake pressure between the front and the rear wheels, making it very difficult to fully utilize increased rear wheel braking capability. EBD varies brake pressure distribution according to load, using input from the wheel speed sensors, which improves overall braking performance.

## Normal Braking

Under normal braking conditions, brake pressure is evenly distributed between the front and rear brakes, and EBD is not used.

## Firm Braking

Under hard braking conditions, the VSA modulator-control unit monitors wheel speed in order to allow a maximum amount of brake distribution individually to the rear wheels. Once the VSA modulator-control unit detects that one or both rear wheels are nearing their maximum braking potential, the inlet valve closes for one or both rear wheels, maintaining the current pressure. If the traction is improved, and the wheel(s) is no longer nearing its limits, the VSA modulator-control unit will open the inlet solenoid allowing additional pressure to be distributed to the rear wheel. The rear wheels are controlled independently of each other during EBD function.

If during EBD function the VSA modulator-control unit determines that the wheels are beginning to slip more than a predetermined amount, the control unit abandons EBD control and shifts to select low 3-channel ABS control.

## Best distribution under heavy load

| Rear wheel brake pressure | Front wheel brake pressure |
| :--- | :--- |
| (cont'd) | 19-79 |

---

### Printed page 19-80

<a id="p1214"></a>
Source: [PDF p.1214](../page-images/p1214.png).

# VSA System Components
## System Description (cont'd)
### Brake Assist Features

Brake assist helps ensure that any driver can achieve the full braking potential of the vehicle by increasing brake system pressure in a panic situation, bringing the vehicle into a full ABS stop.

If during a panic stop the VSA modulator-control unit determines that the brake system pressure increases above a threshold in less than a certain amount of time, the VSA modulator-control unit engages brake assist.

Because the brake system pressure crossed the pressure threshold before the time threshold had expired, the VSA modulator-control unit goes into brake assist mode.

**Brake Pedal Effort Reduced**

| Panic Stop with Brake Assist | Pressure Threshold | Brake Assist Begins |
| :--- | :--- | :--- |
| **Panic Stop without Brake Assist** | | Normal Stop |

*Time Threshold Time*

---

### Printed page 19-81

<a id="p1215"></a>
Source: [PDF p.1215](../page-images/p1215.png).

# Modulator Unit

The modulator unit consists of the inlet solenoid valve, outlet solenoid valve, VSA normally open (NO) solenoid valve,
VSA normally closed (NC) solenoid valve, reservoir, pump, pump motor, and the damping chamber.
The modulator controls the caliper fluid pressure directly. It is a circulating-type modulator because the brake fluid
circulates through the caliper, the reservoir, and the master cylinder.
The hydraulic control has three modes: pressure intensifying, pressure retaining, and pressure reducing.
The hydraulic circuit is an independent four channel type, one channel for each wheel.

## ABS Control

### Pressure Intensifying Mode
VSA NO valve open, VSA NC valve closed, inlet valve open, outlet valve closed.
Master cylinder fluid is pumped out to the caliper.

### Pump Motor
When starting the pressure reducing mode, the pump motor is ON. When stopping ABS operation, the pump motor is
OFF.
The reservoir fluid is pumped out by the pump, through the damping chamber, to the master cylinder.

The source image contains the four-channel modulator hydraulic schematic. Consult it for valve and line routing.

---

### Printed page 19-82

<a id="p1216"></a>
Source: [PDF p.1216](../page-images/p1216.png).

# VSA System Components

## System Description (cont'd)

### Pressure Retaining Mode
VSA NO valve open, VSA NC valve closed, inlet valve closed, outlet valve closed.
Caliper fluid is retained by the inlet valve and outlet valve.
**MASTER CYLINDER**
RL FR FL RR

### Pressure Reducing Mode
VSA NO valve open, VSA NC valve closed, inlet valve closed, outlet valve open.
Caliper fluid flows through the outlet valve to the reservoir.
**MASTER CYLINDER**
RL FR FL RR

---

### Printed page 19-83

<a id="p1217"></a>
Source: [PDF p.1217](../page-images/p1217.png).

# S2000 Brakes (Part B)

## Page 1217

### TCS Control: Pressure Intensifying Mode
- **VSA NO**: Valve closed
- **VSA NC**: Valve open
- **Inlet valve**: Open
- **Outlet valve**: Closed
- **Pump motor**: ON

**Fluid Path**: The reservoir and master cylinder fluid is pumped out by the pump, through the damping chamber, to the rear caliper.


### TCS Control: Pressure Retaining Mode
- **VSA NO**: Valve closed
- **VSA NC**: Valve open
- **Inlet valve**: Closed
- **Outlet valve**: Closed
- **Pump motor**: ON

**Fluid Path**: Rear caliper fluid is retained by the inlet valve and outlet valve.

The source image shows the hydraulic flow diagrams for both modes.

---

### Printed page 19-84

<a id="p1218"></a>
Source: [PDF p.1218](../page-images/p1218.png).

# VSA System Components

## System Description (cont'd)

### Pressure Reducing Mode
VSA NO valve open, VSA NC valve closed, inlet valve closed, rear outlet valve open, pump motor ON.
Caliper fluid flows through the outlet valve to the reservoir.

**MASTER CYLINDER**
RL FR FL RR

### VSA Control — Pressure Intensifying Mode
VSA NO valve closed, VSA NC valve open, inlet valve open, outlet valve closed, pump motor ON.
The reservoir and master cylinder fluid is pumped out by the pump, through the damping chamber, to the front and rear calipers.

**MASTER CYLINDER**
RL FR FL RR

---

### Printed page 19-85

<a id="p1219"></a>
Source: [PDF p.1219](../page-images/p1219.png).

# Pressure Retaining Mode
VSA NO valve closed, VSA NC valve open, inlet valve closed, outlet valve closed, pump motor ON.
Front and rear caliper fluid is retained by the inlet valve and outlet valve.
MASTER CYLINDER
RL FR FL RR

# Pressure Reducing Mode
VSA NO valve open, VSA NC valve closed, inlet valve closed, outlet valve open, pump motor ON.
Caliper fluid flows through the outlet valve to the reservoir.
MASTER CYLINDER
RL FR FL RR

---

### Printed page 19-86

<a id="p1220"></a>
Source: [PDF p.1220](../page-images/p1220.png).

# VSA circuit diagram — first sheet

The source image shows gauge assembly indicators and VSA, ABS, and EBD circuits; the main under-hood and under-dash fuse/relay boxes; ignition and parking-brake switches; brake-fluid-level and brake-pedal-position switches; steering-angle sensor; ECM; and data-link connector. **Use the linked source image for wire routing, connector pins, and branch points.**

The under-hood fuse/relay box shows fuse No. 41 (100 A), No. 42 (40 A), No. 46 (30 A), No. 50 (30 A), and No. 47 (15 A). The under-dash box shows No. 5 (7.5 A) and No. 6 (15 A).

---

### Printed page 19-87

<a id="p1221"></a>
Source: [PDF p.1221](../page-images/p1221.png).

# VSA circuit diagram — second sheet

The source image continues the VSA wiring diagram through the modulator-control unit, VSA OFF switch, gauge assembly, wheel-speed sensors, sensor cluster, and the CAN/F-CAN communication lines. **Use the linked source image for exact electrical connections and pin positions.** The 47P connector signal names and wire colors are tabulated on printed pp.19-75–76.

---

### Printed page 19-88

<a id="p1222"></a>
Source: [PDF p.1222](../page-images/p1222.png).

# VSA connector-face diagrams

The source image shows the cavity layouts for the main under-hood fuse/relay box connectors A (18P) and B (7P), brake-fluid-level switch (2P), brake-pedal-position switch (4P), VSA OFF switch (6P), steering-angle sensor (5P), gauge assembly connectors A (22P) and B (30P), sensor cluster (6P), VSA modulator-control unit (47P), ECM connector E (31P), data-link connector, and wheel-speed sensor (2P). **Use the linked image for cavity numbering and terminal-side orientation.**

---

### Printed page 19-89

<a id="p1223"></a>
Source: [PDF p.1223](../page-images/p1223.png).

# DTC Troubleshooting

## DTC 11,13,15,17: Wheel Speed Sensor (Short to Power/Short to Body Ground/Open)

1. Turn the ignition switch to LOCK (0).
2. Disconnect the VSA modulator-control unit 47P connector.
3. Start the engine.
4. Measure the voltage between body ground and the appropriate wheel speed sensor (+) and (-) terminals of the VSA modulator-control unit 47P connector individually (see table).

| DTC | Appropriate Terminal (+) Side | Appropriate Terminal (-) Side |
| :--- | :--- | :--- |
| 11 (Right-front) | FRS (+): No. 34 | FRS (-): No. 33 |
| 13 (Left-front) | FLS (+): No. 45 | FLS (-): No. 46 |
| 15 (Right-rear) | RRS (+): No. 43 | RRS (-): No. 42 |
| 17 (Left-rear) | RLS (+): No. 36 | RLS (-): No. 37 |

**VSA MODULATOR-CONTROL UNIT 47P CONNECTOR**
See linked source image for connector cavity positions.
Wire side of female terminals

Is there 0.1 V or more?
* **YES** — Repair short to power in the wire between the VSA modulator-control unit and the appropriate wheel speed sensor.
* **NO** — Go to step 5.

5. Turn the ignition switch to LOCK (0).
6. Check for continuity between body ground and the appropriate wheel speed sensor (+) and (-) terminals of the VSA modulator-control unit 47P connector individually (see table).

| DTC | Appropriate Terminal (+) Side | Appropriate Terminal (-) Side |
| :--- | :--- | :--- |
| 11 (Right-front) | FRS (+): No. 34 | FRS (-): No. 33 |
| 13 (Left-front) | FLS (+): No. 45 | FLS (-): No. 46 |
| 15 (Right-rear) | RRS (+): No. 43 | RRS (-): No. 42 |
| 17 (Left-rear) | RLS (+): No. 36 | RLS (-): No. 37 |

**VSA MODULATOR-CONTROL UNIT 47P CONNECTOR**
See linked source image for connector cavity positions.
Wire side of female terminals

Is there continuity?
* **YES** — Go to step 7.
* **NO** — Go to step 9.

(cont'd)

---

### Printed page 19-90

<a id="p1224"></a>
Source: [PDF p.1224](../page-images/p1224.png).

# VSA System Components
## DTC Troubleshooting (cont'd)

### Step 7
Disconnect the appropriate wheel speed sensor 2P connector.

### Step 8
Check for continuity between body ground and the appropriate wheel speed sensor (+) and (—) terminals of the VSA modulator-control unit 47P connector individually (see table).

**Table: DTC Appropriate Terminal Continuity Check (Body Ground)**
| DTC No. | Location | (+) Side Terminal | (-) Side Terminal |
| :--- | :--- | :--- | :--- |
| 11 | Right-front | FRS (+): No. 34 | FRS (-): No. 33 |
| 13 | Left-front | FLS (+): No. 45 | FLS (-): No. 46 |
| 15 | Right-rear | RRS (+): No. 43 | RRS (-): No. 42 |
| 17 | Left-rear | RLS (+): No. 36 | RLS (-): No. 37 |

**VSA Modulator-Control Unit 47P Connector Diagram Reference:**
See linked source image for connector cavity positions.

**Decision Path:**
- **Is there continuity?**
  - **YES**—Repair short to body ground in the wire between the VSA modulator-control unit and the wheel speed sensor.
  - **NO**—Replace the wheel speed sensor (see page 19-129).

### Step 9
Disconnect the appropriate wheel speed sensor 2P connector.

### Step 10
Check for continuity between the appropriate wheel speed sensor (+) and (—) terminals of the VSA modulator-control unit 47P connector (see table).

**Table: DTC Appropriate Terminal Continuity Check (VSA Modulator-Control Unit)**
| DTC No. | Location | (+) Side Terminal | (-) Side Terminal |
| :--- | :--- | :--- | :--- |
| 11 | Right-front | FRS (+): No. 34 | FRS (-): No. 33 |
| 13 | Left-front | FLS (+): No. 45 | FLS (-): No. 46 |
| 15 | Right-rear | RRS (+): No. 43 | RRS (-): No. 42 |
| 17 | Left-rear | RLS (+): No. 36 | RLS (-): No. 37 |

**VSA Modulator-Control Unit 47P Connector Wire Color Reference:**
See linked source image for connector cavity positions.

**Wire Color Associations (OCR Fragments):**
- FRS (-): (BLU)
- FRS (+): (GRN/BLK)
- RLS (+): (YEL/RED)
- RLS (-): (GRY/RED)
- FLS (-): (BRN/WHT)
- FLS (+): source labels BLU/ORN in step 8, BLU/WHT in step 10; verify against vehicle wiring before use
- RRS (+): (GRN/WHT)
- RRS (-): (BLU/YEL)

**Decision Path:**
- **Is there continuity?**
  - **YES**—Repair short in the wires between the VSA modulator-control unit and the wheel speed sensor.
  - **NO**—Go to step 11.

---

### Printed page 19-91

<a id="p1225"></a>
Source: [PDF p.1225](../page-images/p1225.png).

# Page 1225: Vehicle Stability Assist (VSA) Brakes (Part B)

## Step 11
Connect wheel speed sensor 2P connector terminals No. 1 and No. 2 to body ground with a jumper wire.

**DTC Appropriate Wheel Speed Sensor**
| DTC | Appropriate Wheel Speed Sensor |
| :--- | :--- |
| 11 | Right-front |
| 13 | Left-front |
| 15 | Right-rear |
| 17 | Left-rear |

The source diagram shows the terminal side of the 2P male connector; see linked image for jumper placement.

## Step 12
Check for continuity between body ground and the appropriate wheel speed sensor (+) and (-) terminals of the VSA modulator-control unit 47P connector individually (see table).

**DTC Appropriate Terminal DTC**
| DTC | Appropriate Terminal | (+) Side | (-) Side |
| :--- | :--- | :--- | :--- |
| 11 | (Right-front) FRS | No. 34 | No. 33 |
| 13 | (Left-front) FLS | No. 45 | No. 46 |
| 15 | (Right-rear) RRS | No. 43 | No. 42 |
| 17 | (Left-rear) RLS | No. 36 | No. 37 |

**Is there continuity?** YES—Go to step 13. NO—Repair the open between the VSA unit and the wheel-speed sensor. See linked image for 47P cavity positions.

---

### Printed page 19-92

<a id="p1226"></a>
Source: [PDF p.1226](../page-images/p1226.png).

# Wheel-speed sensor DTC troubleshooting (continued)

## DTC 11, 13, 15, 17 — step 13

On the sensor side, measure resistance between the (+) and (−) terminals of the appropriate wheel-speed sensor: 11 right-front, 13 left-front, 15 right-rear, 17 left-rear. The source diagram shows the terminal side of the female 2P connector.

**Is resistance 450–2,000 Ω?** YES—Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good unit (19-127) and retest. NO—Replace the wheel-speed sensor (19-129).

## DTC 12, 14, 16, 18 — electrical noise/intermittent interruption

If electrical noise brings on the ABS and VSA indicators, they go off when the vehicle is test-driven at 19 mph (30 km/h).

1. Turn ignition to LOCK (0).
2. Check the appropriate wheel-speed sensor and pulser (19-129): 12 right-front, 14 left-front, 16 right-rear, 18 left-rear. **Are they OK?** YES—Go to step 3. NO—Reinstall or replace the sensor or pulser.
3. Disconnect the VSA modulator-control unit 47P connector.

---

### Printed page 19-93

<a id="p1227"></a>
Source: [PDF p.1227](../page-images/p1227.png).

# DTC 12, 14, 16, 18 — continued

4. Check continuity between the affected wheel-speed sensor (−) terminal and the other wheel-speed sensor (−) terminals at the VSA modulator-control unit 47P connector.

| DTC | Affected terminal | Compare with terminals |
| --- | --- | --- |
| 12 | FRS (−), No. 33 | 46, 42, 37 |
| 14 | FLS (−), No. 46 | 33, 42, 37 |
| 16 | RRS (−), No. 42 | 33, 46, 37 |
| 18 | RLS (−), No. 37 | 33, 46, 42 |

**Is there continuity?** YES—Repair the short between the affected wheel-speed sensor and the other wheel-speed sensor. NO—Go to step 5.

5. Substitute a known-good wheel-speed sensor: 12 right-front, 14 left-front, 16 right-rear, 18 left-rear.
6. Reconnect all disconnected connectors.
7. Turn ignition ON (II).
8. Clear the DTC with the HDS.
9. Turn ignition to LOCK (0), then disconnect the HDS.
10. Test-drive at 19 mph (30 km/h) or more.
11. Check for DTCs with the HDS. **Is DTC 12, 14, 16, or 18 indicated?** YES—Check for loose 47P terminals; if needed substitute a known-good VSA modulator-control unit (19-127) and retest. NO—Replace the original wheel-speed sensor or pulser (19-129).

---

### Printed page 19-94

<a id="p1228"></a>
Source: [PDF p.1228](../page-images/p1228.png).

# VSA System Components
## DTC Troubleshooting (cont'd)

### DTC 21, 22, 23, 24: Pulser

1. Turn the ignition switch to ON (II).
2. Clear the DTC with the HDS.
3. Turn the ignition switch to LOCK (0), then disconnect the HDS.
4. Test-drive the vehicle at 19 mph (30 km/h) or more.
5. Check for DTCs with the HDS.

**Is DTC 21, 22, 23, or 24 indicated?**
- **YES — Go to step 6.**
- **NO — The system is OK at this time.**


#### Step 6: Check the appropriate pulser (see table) (see page 19-129)

**DTC Appropriate Pulser**
| DTC | Appropriate Pulser |
| :--- | :--- |
| 21 | Right-front |
| 22 | Left-front |
| 23 | Right-rear |
| 24 | Left-rear |

**Is the pulser OK?**
- **YES — Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.**
- **NO — Replace the pulser.**


### DTC 25: Yaw Rate Sensor
### DTC 26: Lateral Acceleration Sensor
### DTC 104: Sensor Cluster

1. Check the size, air pressure, and amount of wear of all four tires, and the wheel alignment (see page 18-7).

**Is the tire condition and wheel alignment OK?**
- **YES — Go to step 2.**
- **NO — Make sure the suspension is not modified, and adjust the wheel alignment correctly, and recheck by test-driving.**

2. Turn the ignition switch to LOCK (0).
3. Disconnect the sensor cluster 6P connector.
4. Disconnect the VSA modulator-control unit 47P connector.
5. Turn the ignition switch to ON (II).

---

### Printed page 19-95

<a id="p1229"></a>
Source: [PDF p.1229](../page-images/p1229.png).

# Page 1229: S2000 Brakes (Part B)

## Step 6
Measure the voltage between body ground and **VSA modulator-control unit 47P connector** terminals No. 6, No. 25, No. 29, and No. 31 individually.

### VSA Modulator-Control Unit 47P Connector Diagram
*Note: Diagram shows wire side of female terminals.*

| Pin | Label | Color/Type |
| :--- | :--- | :--- |
| 6 | CLST-IG | GRN/WHT |
| 25 | CAN2-L | RED |
| 29 | CAN2-H | WHT |
| 31 | CLST-GND | LT GRN |

**Decision Path:**
Is there **0.1 V or more**?
*   **YES**—Repair short to power in the wire between the VSA modulator-control unit and the sensor cluster.
*   **NO**—Go to step 7.


## Step 7
Turn the ignition switch to **LOCK (0)**.

## Step 8
Check for continuity between body ground and **VSA modulator-control unit 47P connector** terminals No. 6, No. 25, No. 29, and No. 31 individually.

### VSA Modulator-Control Unit 47P Connector Diagram (Continued)
*Note: Diagram shows wire side of female terminals.*

| Pin | Label | Color/Type |
| :--- | :--- | :--- |
| 6 | CLST-IG | GRN/WHT |
| 25 | CAN2-L | RED |
| 29 | CAN2-H | WHT |
| 31 | CLST-GND | LT GRN |

**Decision Path:**
Is there **continuity**?
*   **YES**—Repair short to body ground in the wire between the VSA modulator-control unit and the sensor cluster.
*   **NO**—Go to step 9.


## Step 9
Check for continuity between **VSA modulator-control unit 47P connector** terminals No. 6, No. 25, No. 29, and No. 31 and **sensor cluster 6P connector** terminals No. 1, No. 3, No. 2, and No. 5.

### VSA Modulator-Control Unit 47P Connector Diagram (Continued)
*Note: Diagram shows wire side of female terminals.*

| Pin | Label | Color/Type |
| :--- | :--- | :--- |
| 6 | CLST-IG | GRN/WHT |
| 25 | CAN2-L | RED |
| 29 | CAN2-H | WHT |
| 31 | CLST-GND | LT GRN |

**Check matching pairs:** VSA 6 ↔ cluster 1; VSA 25 ↔ cluster 3; VSA 29 ↔ cluster 2; VSA 31 ↔ cluster 5.

### Sensor Cluster 6P Connector Diagram
*Note: Diagram shows wire side of female terminals.*

| Pin | Label | Color/Type |
| :--- | :--- | :--- |
| 1 | CLST-IG | GRN/WHT |
| 2 | CAN2-H | WHT |
| 3 | CAN2-L | RED |
| 5 | CLST-GND | LT GRN |

**Decision Path:**
Is there **continuity**?
*   **YES**—Go to step 10.
*   **NO**—Repair open in the wire between the VSA modulator-control unit and the sensor cluster.

---

### Printed page 19-96

<a id="p1230"></a>
Source: [PDF p.1230](../page-images/p1230.png).

# DTC Troubleshooting (cont'd)

## VSA System Components

**10.** Substitute a known-good sensor cluster (see page 19-125).
> **NOTE:** Check that the sensor cluster mounting bracket is not bent or twisted, and make sure the sensor cluster is mounted properly and fixed.

**11.** Reconnect all of the disconnected connectors.

**12.** Turn the ignition switch to ON (II).

**13.** Clear the DTC with the HDS.

**14.** Do the VSA sensor neutral position memorization (see page 19-125).

**15.** Turn the ignition switch to LOCK (0), then disconnect the HDS.

**16.** Test-drive the vehicle around a number of corners.

**17.** Check for DTCs with the HDS.

Is DTC 25, 26, or 104 indicated?

*   **YES**—Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.
*   **NO**—If any DTCs are indicated, go to the indicated DTCs troubleshooting. If DTC is not indicated, replace the sensor cluster (see page 19-125).


## DTC 27: Steering Angle Sensor

**1.** Check the size, air pressure, and amount of wear of all four tires, and the wheel alignment (see page 18-7).

Is the tire condition and wheel alignment OK?

*   **YES**—Go to step 2.
*   **NO**—Make sure the suspension is not modified, and adjust the wheel alignment correctly, and recheck by test-driving.

**2.** Turn the ignition switch to ON (II).

**3.** Clear the DTC with the HDS.

**4.** Slowly drive the vehicle straight ahead without turning the steering wheel for 10 ft (3 m) or more, then park the vehicle while holding the steering wheel in the straight ahead position.

**5.** Check the STEERING ANGLE in the VSA DATA LIST with the HDS.

Is it 0° ±3°?

*   **YES**—Go to step 7.
*   **NO**—Go to step 6.

**6.** Do the VSA sensor neutral position memorization (see page 19-125).

**7.** Turn the ignition switch to LOCK (0), then disconnect the HDS.

---

### Printed page 19-97

<a id="p1231"></a>
Source: [PDF p.1231](../page-images/p1231.png).

# DTC 27 — steering angle sensor (continued)

8. Test-drive around a number of corners.
9. Check DTCs with the HDS. **Is DTC 27 indicated?** YES—Go to step 10. NO—If DTC 86 is indicated, follow DTC 86 troubleshooting (19-105); if no DTCs are indicated, the system is OK.
10. Turn ignition to LOCK (0).
11. Substitute a known-good steering-angle sensor (19-124). Make sure the sensor and combination switch are mounted properly.
12. Turn ignition ON (II).
13. Clear the DTC with the HDS.
14. Perform VSA sensor neutral-position memorization (19-125).
15. Turn ignition to LOCK (0), then disconnect the HDS.
16. Test-drive around a number of corners.
17. Check DTCs. **Is DTC 27 indicated?** YES—Go to step 18. NO—Replace the original steering-angle sensor (19-124).
18. Turn ignition to LOCK (0).
19. Substitute a known-good sensor cluster (19-125). Check that its mounting bracket is not bent or twisted, and that the cluster is mounted properly and fixed.
20. Turn ignition ON (II).
21. Clear the DTC with the HDS.
22. Perform VSA sensor neutral-position memorization (19-125).
23. Turn ignition to LOCK (0), then disconnect the HDS.
24. Test-drive around a number of corners.
25. Check DTCs. **Is DTC 27 indicated?** YES—Check loose terminals in the VSA modulator-control unit 47P connector; if needed substitute a known-good unit (19-127) and retest. NO—Replace the original sensor cluster (19-125).

---

### Printed page 19-98

<a id="p1232"></a>
Source: [PDF p.1232](../page-images/p1232.png).

# VSA System Components
## DTC Troubleshooting (cont'd)

### DTC 31, 32, 33, 34, 35, 36, 37, 38: ABS Solenoid

1. Turn the ignition switch to ON (II).
2. Clear the DTC with the HDS.
3. Turn the ignition switch to LOCK (0), then turn it to ON (II) again.
4. Check for DTCs with the HDS.

**Is DTC 31, 32, 33, 34, 35, 36, 37, or 38 indicated?**

*   **YES —** Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.

*   **NO —** The system is OK at this time.


### DTC 51: Motor Lock
### DTC 52: Motor Stuck ON/OFF

1. Turn the ignition switch to LOCK (0).
2. Check the No. 50 (30 A) fuse in the main under-hood fuse/relay box.

**Is the fuse blown?**

*   **YES —** Install the new No. 50 (30 A) fuse, and recheck. If the fuse continues to blow, check for short to body ground in the wire between the No. 50 (30 A) fuse in the main under-hood fuse/relay box and the VSA modulator-control unit. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.

*   **NO —** Reinstall the checked fuse, then go to step 3.

3. Disconnect the VSA modulator-control unit 47P connector.
4. Measure the voltage between VSA modulator-control unit 47P connector terminal No. 1 and body ground.

VSA 47P terminal 1 is +B-P (WHT/BLU), viewed from wire side of female terminals; see source image.

**Is there battery voltage?**

*   **YES —** Go to step 5.
*   **NO —** Repair open in the wire between the No. 50 (30 A) fuse in the main under-hood fuse/relay box and the VSA modulator-control unit.

---

### Printed page 19-99

<a id="p1233"></a>
Source: [PDF p.1233](../page-images/p1233.png).

# DTC 51/52 — motor lock or stuck ON/OFF (continued)

5. Check continuity between VSA modulator-control unit 47P connector terminal **47, GND-P (BLK)**, and body ground. Connector view is from the wire side of female terminals. **Is there continuity?** YES—Go to step 6. NO—Repair open between the unit and body ground G303.
6. Reconnect the 47P connector.
7. Turn ignition ON (II).
8. Clear the DTC with the HDS.
9. Turn ignition to LOCK (0), then disconnect the HDS.
10. Test-drive at 10 mph (15 km/h) or more.
11. Check DTCs. **Is DTC 51 or 52 indicated?** YES—Check for loose 47P terminals; if needed substitute a known-good VSA modulator-control unit (19-127) and retest. NO—System OK at this time.

## DTC 54 — fail-safe relay

1. Turn ignition ON (II).
2. Clear the DTC with the HDS.
3. Turn ignition to LOCK (0), then disconnect the HDS.
4. Test-drive.
5. Check DTCs. **Is DTC 54 indicated?** YES—Check for loose 47P terminals; if needed substitute a known-good VSA modulator-control unit (19-127) and retest. NO—Intermittent failure; vehicle OK at this time.

---

### Printed page 19-100

<a id="p1234"></a>
Source: [PDF p.1234](../page-images/p1234.png).

# VSA System Components
## DTC Troubleshooting (cont'd)

### DTC 61: Low +B-FSR Voltage
### DTC 62: High +B-FSR Voltage

> **NOTE:** If the vehicle has high electric load or a weak battery, DTC 61 may be stored when starting the engine.

1. Turn the ignition switch to ON (II).
2. Clear the DTC with the HDS.
3. Turn the ignition switch to LOCK (0), then turn it to ON (II) again.

**Does the ABS indicator come on?**
- **YES — Go to step 4.**
- **NO — The system is OK at this time.**

4. Check for DTCs with the HDS.

**Is DTC 61 or 62 indicated?**
- **YES — Check the charging system (see page 4-36).**
- **NO — Do the appropriate troubleshooting for the DTC indicated.**

### DTC 64: Sensor Power Voltage

1. Turn the ignition switch to ON (II).
2. Clear the DTC with the HDS.
3. Turn the ignition switch to LOCK (0), then disconnect the HDS.
4. Test-drive the vehicle.
5. Check for DTCs with the HDS.

**Is DTC 64 indicated?**
- **YES — Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.**
- **NO — The system is OK at this time.**

---

### Printed page 19-101

<a id="p1235"></a>
Source: [PDF p.1235](../page-images/p1235.png).

# DTC 65: Brake Fluid Level

## Step 1
Check the brake fluid level in the master cylinder reservoir.

**Is brake fluid level OK?**
*   **YES** — Go to step 2.
*   **NO** — Inspect the brake pads: Front (see page 19-13), rear (see page 19-22), and replace worn out brake pads, then recheck.

## Step 2
Turn the ignition switch to ON (II).

## Step 3
Clear the DTC with the HDS.

## Step 4
Turn the ignition switch to LOCK (0).

## Step 5
Disconnect the brake fluid level switch 2P connector.

## Step 6
Turn the ignition switch to ON (II).

## Step 7
Check for DTCs with the HDS.

**Is DTC 65 indicated?**
*   **YES** — Go to step 8.
*   **NO** — Replace the reservoir (brake fluid level switch is included) on the master cylinder (see page 19-18).

## Step 8
Turn the ignition switch to LOCK (0).

## Step 9
Disconnect the VSA modulator-control unit 47P connector.

## Step 10
Disconnect the gauge assembly connector B (30P).

## Step 11
Check for continuity between brake fluid level switch 2P connector terminal No. 2 and body ground.

### Diagram Label: BRAKE FLUID LEVEL SWITCH 2P CONNECTOR
*   **Wire Color:** GRN/RED
*   **Location:** Wire side of female terminals

**Is there continuity?**
*   **YES** — Repair short to body ground in the wire between the gauge assembly or the VSA modulator-control unit and the brake fluid level switch.
*   **NO** — Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.

---

### Printed page 19-102

<a id="p1236"></a>
Source: [PDF p.1236](../page-images/p1236.png).

# VSA System Components
## DTC Troubleshooting (cont'd)

### DTC 66: VSA Pressure Sensor (Inside of VSA Modulator-control Unit)
1. Turn the ignition switch to ON (II).
2. Clear the DTC with the HDS.
3. Turn the ignition switch to LOCK (0), then disconnect the HDS.
4. Test-drive the vehicle.
5. Check for DTCs with the HDS.

**Is DTC 66 Indicated?**
- **YES**—Replace the VSA modulator-control unit (see page 19-127).
- **NO**—The system is OK at this time.

### DTC 68: Brake Pedal Position Switch
1. Turn the ignition switch to ON (II).
2. Check for other DTCs.

**Is another DTC indicated?**
- **YES**—Do the appropriate troubleshooting for the DTC.
- **NO**—Go to step 3.

3. Turn the ignition switch to LOCK (0).
4. Check the brake pedal position switch (see page 22-144), and adjustment (see page 19-6).

**Is the switch and adjustment OK?**
- **YES**—Go to step 5.
- **NO**—Adjust the brake pedal position switch. If necessary, replace the switch (see page 19-6).

5. Turn the ignition switch to ON (II).
6. Clear the DTC with the HDS.
7. Turn the ignition switch to LOCK (0), then disconnect the HDS.
8. Test-drive the vehicle.

---

### Printed page 19-103

<a id="p1237"></a>
Source: [PDF p.1237](../page-images/p1237.png).

# DTC 68 — brake pedal position switch (continued)

### Step 9
Check for DTCs with the HDS.

**Is DTC 68 indicated?**
- **YES** — Go to step 10.
- **NO** — The system is OK at this time.

### Step 10
Troubleshoot the brake pedal position switch signal circuit (see page 11-460).

**Is the brake pedal position switch circuit OK?**
- **YES** — Check for loose terminals in the ECM connector, if the connections are OK, substitute a known-good ECM and recheck. If the problem is gone, replace the original ECM. If the problem continues, replace the VSA modulator-control unit (see page 19-127).
- **NO** — Repair the brake pedal position switch circuit.


---

# DTC 81: Central Processing Unit (CPU)

## Step 1
Turn the ignition switch to ON (II).

## Step 2
Check for other DTCs.

**Is another DTC indicated?**
- **YES** — Do the appropriate troubleshooting for the DTC.
- **NO** — Go to step 3.

## Step 3
Clear the DTC with the HDS.

## Step 4
Turn the ignition switch to LOCK (0), then disconnect the HDS.

## Step 5
Test-drive the vehicle.

## Step 6
Check for DTCs with the HDS.

**Is DTC 81 indicated?**
- **YES** — Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.
- **NO** — Intermittent failure; the system is OK at this time.

---

### Printed page 19-104

<a id="p1238"></a>
Source: [PDF p.1238](../page-images/p1238.png).

# DTC Troubleshooting (cont'd)

## DTC 83: ECM Communication

1. Turn the ignition switch to ON (II).
2. Check for DTCs with the HDS.

**Is DTC 86 indicated?**
- **YES** — Go to the troubleshooting for DTC 86.
- **NO** — Go to step 3.

3. Clear the DTC with the HDS.
4. Turn the ignition switch to LOCK (0), then disconnect the HDS.
5. Test-drive the vehicle.
6. Check for DTCs with the HDS.

**Is DTC 83 indicated?**
- **YES** — Go to step 7.
- **NO** — The system is OK at this time.

7. Check for fuel and emission systems (PGM-FI) DTCs with the HDS (see page 11-213).

**Are any ECM DTCs indicated?**
- **YES** — Do the applicable troubleshooting for the ECM.
- **NO** — Check for loose VSA modulator-control unit 47P terminals; if needed substitute a known-good unit (19-127) and retest.


## DTC 84: VSA Sensor Neutral Position

> **NOTE:** If DTC 84 is stored, the VSA activation indicator does not go off until doing the VSA sensor neutral position memorization (see page 19-125).

1. Do the VSA sensor neutral position memorization (see page 19-125).
2. Clear the DTC with the HDS.
3. Turn the ignition switch to LOCK (0), then turn it to ON (II) again.
4. Check for DTCs with the HDS.

**Is DTC 84 indicated?**
- **YES** — Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.
- **NO** — The system is OK at this time.

---

### Printed page 19-105

<a id="p1239"></a>
Source: [PDF p.1239](../page-images/p1239.png).

# DTC 86: F-CAN Communication

**Procedure:**
1. Turn the ignition switch to ON (II).
2. Clear the DTC with the HDS.
3. Turn the ignition switch to LOCK (0), then turn it to ON (II) again.
4. Check for DTCs with the HDS.

**Is DTC 86 indicated?**
- **YES — Go to step 5.**
- **NO — The system is OK at this time.**

**Step 5:** Clear the DTC with the HDS.

**Step 6:** Start and run the engine for at least 5 seconds.

**Step 7:** Check for DTCs with the HDS.

**Is DTC 86 indicated?**
- **YES — Go to step 8.**
- **NO — Intermittent failure; the F-CAN communication line is OK at this time.**

**Step 8:** Turn the ignition switch to LOCK (0).

**Step 9:** Short the SCS line with the HDS.

**Step 10:** Disconnect ECM connector E (31P).

**Step 11:** Disconnect the steering angle sensor 5P connector.

**Step 12:** Disconnect the VSA modulator-control unit 47P connector.

**Step 13:** Turn the ignition switch to ON (II).

**Step 14:** Measure the voltage between body ground and VSA modulator-control unit 47P connector terminals No. 11 and No. 15 individually.

The test points are CAN1-H (RED), terminal 11, and CAN1-L (WHT), terminal 15, viewed from the wire side of female terminals. See source image for cavities.

**Is there 0.1 V or more?**
- **YES — Repair short to power in the wire between the VSA modulator-control unit and the ECM.**
- **NO — Go to step 15.**

*(Continued on page 19-106)*

---

### Printed page 19-106

<a id="p1240"></a>
Source: [PDF p.1240](../page-images/p1240.png).

# VSA System Components
## DTC Troubleshooting (cont'd)

**15.** Turn the ignition switch to LOCK (0).

**16.** Check for continuity between body ground and VSA modulator-control unit 47P connector terminals No. 11 and No. 15 individually.

Test CAN1-H (RED) and CAN1-L (WHT); see source image for connector cavities.

**Is there continuity?**
- **YES**—Repair short to body ground in the wire between the VSA modulator-control unit, the steering angle sensor, and the ECM.
- **NO**—Go to step 17.


**17.** Check for continuity between VSA modulator-control unit 47P connector terminals No. 11, No. 15 and ECM connector E (31P) terminals No. 11, No. 24 individually.

The terminal pairs are VSA 11 ↔ ECM E11 and VSA 15 ↔ ECM E24; see source image.

**Is there continuity?**
- **YES**—Go to step 18.
- **NO**—Repair open in the wire between the VSA modulator-control unit and the ECM.


**18.** Check for continuity between the steering angle sensor 5P connector terminals No. 2, No. 4 and body ground individually.

Steering-angle sensor 5P terminals 2 (CAN1-L, WHT) and 4 (CAN1-H, RED) are viewed from wire side of female terminals.

**Is there continuity?**
- **YES**—Trace and repair short to body ground on the CAN1-L or CAN1-H wires between the steering angle sensor, the ECM, and the VSA modulator-control unit.
- **NO**—Go to step 19.

---

### Printed page 19-107

<a id="p1241"></a>
Source: [PDF p.1241](../page-images/p1241.png).

# S2000 Brakes (Part B) - Page 1241

## Steering Angle Sensor Diagnosis

### Step 19
Check the No. 6 (15 A) fuse in the under-dash fuse/relay box.

**Is the fuse blown?**
*   **YES**—Replace the fuse, and recheck.
*   **NO**—Reinstall the checked fuse, then go to step 20.

### Step 20
Turn the ignition switch to ON (II).

### Step 21
Measure the voltage between steering angle sensor 5P connector terminal No. 5 and body ground.

**S T E E R I N G A N G L E S E N S O R 5 P C O N N E C T O R**
*   **IG1 (BLK/YEL)** - Wire side of female terminals

**Is there battery voltage?**
*   **YES**—Go to step 22.
*   **NO**—Repair open in the wire between the No. 6 (15 A) fuse and the steering angle sensor.

### Step 22
Turn the ignition switch to LOCK (0).

### Step 23
Reconnect all of the disconnected connectors.

### Step 24
Turn the ignition switch to ON (II).

### Step 25
Measure the voltage between steering angle sensor 5P connector terminal No. 1 and body ground.

**S T E E R I N G A N G L E S E N S O R 5 P C O N N E C T O R**
*   **1 / 2 / 4 / 5** - Wire side of female terminals
*   **G N D (BLK)**

**Is there 0.1 V or less?**
*   **YES**—Replace the steering angle sensor (see page 19-124).
*   **NO**—Repair open in the wire between the steering angle sensor and body ground (G401).


**Source Reference:** 19-107

---

### Printed page 19-108

<a id="p1242"></a>
Source: [PDF p.1242](../page-images/p1242.png).

# DTC Troubleshooting (cont'd)

## DTC 91: VSA Operation

1. Turn the ignition switch to ON (II).
2. Clear the DTC with the HDS.
3. Turn the ignition switch to LOCK (0), then disconnect the HDS.
4. Test-drive the vehicle.
5. Check for DTCs with the HDS.

**Is DTC 91 indicated?**
- **YES — Go to step 6.**
- **NO — If DTC 86 is indicated, do the DTC 86 troubleshooting (see page 19-105). If no DTCs are indicated, the system is O K at this time.**


**6. Turn the ignition switch to LOCK (0).**

**7. Disconnect the sensor cluster 6P connector.**

**8. Disconnect the VSA modulator-control unit 47P connector.**

**9. Turn the ignition switch to ON (II).**

**10. Measure the voltage between body ground and VSA modulator-control unit 47P connector terminals No. 6, No. 25, No. 29, and No. 31 individually.**

Test VSA 47P terminals 6 (CLST-IG, GRN/WHT), 25 (CAN2-L, RED), 29 (CAN2-H, WHT), and 31 (CLST-GND, LT GRN). See source image for cavities.

**Is there 0.1 V or more?**
- **YES — Repair short to power in the wire between the VSA modulator-control unit and the sensor cluster.**
- **NO — Go to step 11.**


**11. Turn the ignition switch to LOCK (0).**

**12. Check for continuity between body ground and VSA modulator-control unit 47P connector terminals No. 6, No. 25, No. 29, and No. 31 individually.**

Test the same four terminals to body ground individually.

**Is there continuity?**
- **YES — Repair short to body ground in the wire between the VSA modulator-control unit and the sensor cluster.**
- **NO — Go to step 13.**

---

### Printed page 19-109

<a id="p1243"></a>
Source: [PDF p.1243](../page-images/p1243.png).

# DTC 91 — VSA operation (continued)

13. Check continuity between VSA modulator-control unit 47P terminals 6, 25, 29, 31 and sensor cluster 6P terminals 1, 3, 2, 5, respectively. The corresponding circuits are CLST-IG (GRN/WHT), CAN2-L (RED), CAN2-H (WHT), and CLST-GND (LT GRN). **Continuity?** YES—Go to step 14. NO—Repair open between the unit and sensor cluster.
14. Substitute a known-good sensor cluster (19-125).
15. Reconnect all disconnected connectors.
16. Turn ignition ON (II).
17. Clear the DTC with the HDS.
18. Turn ignition to LOCK (0), then disconnect the HDS.
19. Test-drive around a number of corners.
20. Check DTCs. **Is DTC 91 indicated?** YES—Go to step 21. NO—Replace the original sensor cluster (19-125).
21. Turn ignition to LOCK (0).
22. Disconnect the steering-angle sensor 5P connector.
23. Check continuity between VSA 47P terminals 11 and 15 and steering-angle sensor 5P terminals 4 and 2, respectively (CAN1-H RED and CAN1-L WHT). **Continuity?** YES—Go to step 24. NO—Repair open between VSA unit and steering-angle sensor.

See the linked source image for connector orientation and cavity positions.

---

### Printed page 19-110

<a id="p1244"></a>
Source: [PDF p.1244](../page-images/p1244.png).

# DTC 91 — VSA operation (continued)

24. Check under-dash fuse No. 6 (15 A). **Blown?** YES—Install a new fuse and recheck. If it blows again, check for short to body ground between the fuse and steering-angle sensor or VSA unit. NO—Reinstall checked fuse and go to step 25.
25. Turn ignition ON (II).
26. Measure voltage between steering-angle sensor 5P terminal 5 (IG1, BLK/YEL) and body ground. **Battery voltage?** YES—Go to step 27. NO—Repair open between fuse No. 6 (15 A) and steering-angle sensor.
27. Turn ignition to LOCK (0).
28. Reconnect all connectors.
29. Turn ignition ON (II).
30. Measure voltage between steering-angle sensor 5P terminal 1 (GND, BLK) and body ground. **0.1 V or less?** YES—Replace steering-angle sensor (19-124). NO—Repair open between sensor and body ground G401.

Both connector views are from the wire side of female terminals; see source image.

---

### Printed page 19-111

<a id="p1245"></a>
Source: [PDF p.1245](../page-images/p1245.png).

# Page 19-111: VSA DTC Diagnostic Procedures

## DTC 105: Hydraulic Unit Temperature Sensor

1. Turn the ignition switch to ON (II).
2. Clear the DTC with the HDS.
3. Turn the ignition switch to LOCK (0), then disconnect the HDS.
4. Test-drive the vehicle.
5. Check for DTCs with the HDS.

**Is DTC 105 indicated?**
- **YES**—Replace the VSA modulator-control unit (see page 19-127).
- **NO**—The system is OK at this time.


## DTC 121, 122, 123, 124: VSA Solenoid

1. Turn the ignition switch to ON (II).
2. Clear the DTC with the HDS.
3. Turn the ignition switch to LOCK (0), then disconnect the HDS.
4. Test-drive the vehicle.
5. Check for DTCs with the HDS.

**Is DTC 121, 122, 123, or 124 indicated?**
- **YES**—Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.
- **NO**—Intermittent failure; the system is OK at this time.

---

### Printed page 19-112

<a id="p1246"></a>
Source: [PDF p.1246](../page-images/p1246.png).

# VSA System Components
## Symptom Troubleshooting

**ABS indicator does not come on**

1. Turn the ignition switch to ON (II), and watch the ABS indicator.
   Does the ABS indicator come on?
   - **YES** — The system is OK at this time.
   - **NO** — Go to step 2.

2. Turn the ignition switch to LOCK (0), then turn it to ON (II) again.
   Does the brake system indicator come on?
   - **YES** — Go to step 7.
   - **NO** — Go to step 3.

3. Turn the ignition switch to LOCK (0).

4. Remove the gauge assembly. Do not disconnect the gauge assembly connector A (22P) and connector B (30P) (see page 22-89).

5. Turn the ignition switch to ON (II).

6. Measure the voltage between gauge assembly connector A (22P) terminal No. 18 and body ground.

   Gauge assembly connector A (22P), terminal 18 (GND, BLK), viewed from wire side of female terminals; see source image.
   Is there 0.1 V or less?
   - **YES** — Do the self-diagnostic function troubleshooting for the gauge assembly (see page 22-60).
   - **NO** — Repair open in the wire between the gauge assembly and body ground (G501).

7. Turn the ignition switch to LOCK (0).

8. Disconnect the VSA modulator-control unit 47P connector.

9. Turn the ignition switch to ON (II).
   Does the ABS indicator come on?
   - **YES** — Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.
   - **NO** — Go to step 10.

10. Turn the ignition switch to LOCK (0).

11. Check the ABS indicator bulb in the gauge assembly (see page 22-58).
    Is the bulb OK?
    - **YES** — Go to step 12.
    - **NO** — Replace the ABS indicator bulb (see page 22-58).

12. Disconnect the gauge assembly connector B (30P).

13. Check for continuity between gauge assembly connector B (30P) terminal No. 20 and body ground.

    Gauge assembly connector B (30P), terminal 20 (ABS, BLU/RED), viewed from wire side of female terminals; see source image.
    Is there continuity?
    - **YES** — Repair short to body ground in the wire between the gauge assembly and the VSA modulator-control unit.
    - **NO** — Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.

---

### Printed page 19-113

<a id="p1247"></a>
Source: [PDF p.1247](../page-images/p1247.png).

# ABS indicator does not go off, and no DTCs are stored

1. Turn the ignition switch to LOCK (0).
2. Check the No.48 (30 A) fuse in the main under-hood fuse/relay box.

**Is the fuse blown?**
- **YES**—Check for a short to body ground in the fuse circuit, then replace the fuse, and recheck.
- **NO**—Reinstall the checked fuse, then go to step 3.

3. Check the No.6 (15 A) fuse in the under-dash fuse/relay box.

**Is the fuse blown?**
- **YES**—Check for a short to body ground in the fuse circuit, then replace the fuse, and recheck.
- **NO**—Reinstall the checked fuse, then go to step 4.

4. Disconnect the VSA modulator-control unit 47P connector.
5. Measure the voltage between VSA modulator-control unit 47P connector terminal No.32 and body ground.

47P terminal 32, +B-V (WHT/RED); see source image for cavity.

**Is there battery voltage?**
- **YES**—Go to step 6.
- **NO**—Repair open in the wire between the No. 48 (30 A) fuse in the main under-hood fuse/relay box and the VSA modulator-control unit.

6. Turn the ignition switch to ON (II).
7. Measure the voltage between VSA modulator-control unit 47P connector terminal No. 4 and body ground.

47P terminal 4, IG1 (BLK/YEL); see source image for cavity.

**Is there battery voltage?**
- **YES**—Go to step 8.
- **NO**—Repair open in the wire between the No.6 (15 A) fuse in the under-dash fuse/relay box and the VSA modulator-control unit.

8. Turn the ignition switch to LOCK (0).
9. Check for continuity between VSA modulator-control unit 47P connector terminal No. 16 and body ground.

47P terminal 16, GND-V (BLK); see source image for cavity.

**Is there continuity?**
- **YES**—Go to step 10.
- **NO**—Repair open in the wire between the VSA modulator-control unit and body ground (G303).

---

### Printed page 19-114

<a id="p1248"></a>
Source: [PDF p.1248](../page-images/p1248.png).

# Symptom Troubleshooting (cont'd)

## Step 10
Turn the ignition switch to ON (II).

## Step 11
Connect VSA modulator-control unit 47P connector terminal No.44 and body ground with a jumper wire.

47P terminal 44 is ABS (BLU/RED), viewed from wire side of female terminals; see source image.

**Outcome: YES**
- Check for loose terminals in the VSA modulator-control unit 47P connector.
- If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.

**Outcome: NO**
- Go to step 12.

## Step 12
Connect gauge assembly connector B (30P) terminal No.20 and body ground with a jumper wire.

Gauge assembly connector B terminal 20 is ABS (BLU/RED), viewed from wire side of female terminals; see source image.

**Outcome: YES**
- Repair open in the wire between the gauge assembly and the VSA modulator-control unit.

**Outcome: NO**
- Check for loose terminals in the gauge assembly connector B (30P).
- If necessary, substitute a known-good gauge assembly (see page 22-89), and retest.

---

### Printed page 19-115

<a id="p1249"></a>
Source: [PDF p.1249](../page-images/p1249.png).

# Brake system indicator does not come on

1. Apply parking brake.
2. Turn ignition ON (II) and watch brake-system indicator. **Comes on and stays on?** YES—Go to step 3. NO—Go to step 6.
3. Turn ignition to LOCK (0).
4. Release parking brake.
5. Turn ignition ON (II) and watch indicator. **Comes on for several seconds?** YES—System OK at this time. NO—Go to step 14.
6. Turn ignition to LOCK (0), then ON (II). **Does ABS indicator come on for several seconds?** YES—Go to step 11. NO—Go to step 7.
7. Turn ignition to LOCK (0).
8. Remove gauge assembly without disconnecting its A (22P) or B (30P) connector.
9. Turn ignition ON (II).
10. Measure voltage between gauge connector A terminal 18, GND (BLK), and body ground. **0.1 V or less?** YES—Perform gauge-assembly self-diagnostic troubleshooting (22-60). NO—Repair open between gauge assembly and body ground G501.
11. Turn ignition to LOCK (0).
12. Release parking brake.
13. Turn ignition ON (II). **Does brake-system indicator come on for several seconds?** YES—Test parking-brake switch (19-12). NO—Go to step 14.
14. Turn ignition to LOCK (0).
15. Disconnect VSA modulator-control unit 47P connector.

See source image for connector cavity view.

---

### Printed page 19-116

<a id="p1250"></a>
Source: [PDF p.1250](../page-images/p1250.png).

# VSA System Components
## Symptom Troubleshooting (cont'd)

**16.** Turn the ignition switch to ON (II).

Does the brake system indicator come on for several seconds?

*   **YES** — Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.
*   **NO** — Go to step 17.

**17.** Turn the ignition switch to LOCK (0).

**18.** Remove the gauge assembly (see page 22-89).

**19.** Check the brake system indicator bulb in the gauge assembly (see page 22-58).

Is the bulb OK?

*   **YES** — Go to step 20.
*   **NO** — Replace the brake system indicator bulb (see page 22-58).

**20.** Disconnect the gauge assembly connector B (30P).

**21.** Check for continuity between gauge assembly connector B (30P) terminal No. 25 and body ground.

> **GAUGE ASSEMBLY CONNECTOR B (30P)**
> / 2 3 4 5 6 7 8 9 10 11 12 13
> 15 16 17 18 19 20 21 22|X|23 24 25 26 27 28 29 30
> W L - E B D (PNK)
> Wire side of female terminals

Is there continuity?

*   **YES** — Repair short to body ground between the gauge assembly and the VSA modulator-control unit.
*   **NO** — Check for loose terminals in the gauge assembly connector B (30P). If necessary, substitute a known-good gauge assembly (see page 22-89), and retest.

19-116

---

### Printed page 19-117

<a id="p1251"></a>
Source: [PDF p.1251](../page-images/p1251.png).

# Brake system indicator does not go off, and no DTCs are stored

1. Release the parking brake.
2. Turn the ignition switch to ON (II).

Does the brake system indicator go off after several seconds?
- **YES** — The system is OK at this time.
- **NO** — Go to step 3.

3. Check the brake fluid level in the master cylinder reservoir.
Is brake fluid level OK?
- **YES** — Go to step 4.
- **NO** — Inspect the brake pads: Front (see page 19-13), rear (see page 19-22), and replace worn out pads, then recheck.

4. Check the ABS indicator.
Does ABS indicator stay on?
- **YES** — Check for DTCs and do the indicated DTC troubleshooting.
- **NO** — Go to step 5.

5. Do the brake fluid level switch test (see page 19-12).
Is the switch OK?
- **YES** — Go to step 6.
- **NO** — Replace the master-cylinder reservoir, which includes the brake-fluid-level switch (19-18).

6. Do the parking brake switch test (see page 19-12).
Is the switch OK?
- **YES** — Go to step 7.
- **NO** — Replace the parking brake switch (see page 19-30).

7. Turn the ignition switch to LOCK (0).
8. Remove the gauge assembly (see page 22-89).
9. Disconnect the gauge assembly connector B (30P).
10. Check for continuity between gauge assembly connector B (30P) terminal No. 23 and body ground.

Gauge assembly connector B (30P), terminal 23 (GRN/WHT), viewed from wire side of female terminals; see source image.

Is there continuity?
- **YES** — Repair short to body ground in the wire between the gauge assembly and the parking brake switch.
- **NO** — Go to step 11.

---

### Printed page 19-118

<a id="p1252"></a>
Source: [PDF p.1252](../page-images/p1252.png).

# Brake system indicator does not go off, no DTCs — continued

11. Reconnect gauge assembly connector B (30P).
12. Turn ignition ON (II).
13. Jumper VSA modulator-control unit 47P terminal 13, WL-EBD (PNK), to body ground. **Does brake-system indicator go off?** YES—Check loose 47P terminals; if needed substitute a known-good VSA modulator-control unit (19-127) and retest. NO—Go to step 14.
14. Jumper gauge assembly connector B (30P) terminal 25, WL-EBD (PNK), to body ground. **Does indicator go off?** YES—Repair open between gauge assembly and VSA unit. NO—Check gauge connector B terminals; if needed substitute a known-good gauge assembly (22-89) and retest.

Connector diagrams are viewed from the wire side of female terminals; see source image.

---

### Printed page
<a id="p1253"></a>
Source: [PDF p.1253](../page-images/p1253.png).

VSA indicator does not come on
1. Turn the ignition switch to ON (II), and watch the VSA indicator.
Does the VSA indicator come on?
YES— T h e system is OK at this time.
NO— G o to step 2.
2. Turn the ignition switch to LOCK (0), then turn it to
ON (II) again.
Does the brake system indicator come on?
YES— G o to step 7.
NO—Goto step 3.
3. Turn the ignition switch to LOCK (0).
4. Remove the gauge assembly. Do not disconnect
the gauge assembly connector A (22P) and
connector B (30P) (see page 22-89).
5. Turn the ignition switch to ON (II).
6. Measure the voltage between gauge assembly
connector A (22P) terminal No. 18 and body ground.
GAUGE ASSEMBLY C O N N E C T O R A (22P)
1 2 3 4 5 7 8 9 10
11 12 13 14 15 161X117 18 19 20
/ / G N D (BLK)
Wire side of female terminals
is there 0.1 V or less?
YES— D o the self-diagnostic function
troubleshooting for the gauge assembly (see page
22-60).
NO—Repair open in the wire between the gauge
assembly and body ground (G501.H
7. Turn the ignition switch to LOCK (0).
8. Disconnectthe VSA modulator-control unit 47P
connector.
9. Turn the ignition switch to ON (II).
Does the VSA indicator come on?
YES— C h e c k for loose terminals in the VSA
modulator-control unit 47P connector. If necessary,
substitute a known-good VSA modulator-control
unit (see page 19-127), and retest.
NO— G o to step 10.
10. Turn the ignition switch to LOCK (0).
11. Check the VSA indicator bulb in the gauge
assembly (see page 22-58).
Is the bulb OK?
YES— G o to step 12.
NO—Replace the VSA indicator bulb (see page
22-58).
12. Disconnectthe gauge assembly connector B (30P).
13. Check for continuity between gauge assembly
connector B (30P) terminal No. 14 and body ground.
GAUGE ASSEMBLY CONNECTOR B (30P)
q~7 VSA (PNK/BLK)
/ 2 3 4 5 6 7 8 9 10 11 12 13 14
Wire side of female terminals
Is there continuity?
YES—Repair short to body ground in the wire
between the gauge assembly and the VSA
modulator-control unit.
NO—Check for loose terminals in the VSA
modulator-control unit 47P connector. If necessary,
substitute a known-good VSA modulator-control
unit (see page 19-127), and retest.

---

### Printed page 19-120

<a id="p1254"></a>
Source: [PDF p.1254](../page-images/p1254.png).

# Symptom Troubleshooting (cont'd)

## VSA indicator does not go off, and no DTCs are stored

1. Turn the ignition switch to LOCK (0).
2. Check the No. 48 (30 A) fuse in the main under-hood fuse/relay box.
   - Is the fuse blown?
     - **YES** — Check for a short to body ground in the fuse circuit, then replace the fuse, and recheck.
     - **NO** — Reinstall the checked fuse, then go to step 3.
3. Check the No. 6 (15 A) fuse in the under-dash fuse/relay box.
   - Is the fuse blown?
     - **YES** — Check for a short to body ground in the fuse circuit, then replace the fuse, and recheck.
     - **NO** — Reinstall the checked fuse, then go to step 4.
4. Disconnect the VSA modulator-control unit 47P connector.
5. Measure the voltage between VSA modulator-control unit 47P connector terminal No. 32 and body ground.

See source image for 47P connector cavities.

- Is there battery voltage?
  - **YES** — Go to step 6.
  - **NO** — Repair open in the wire between the No. 48 (30 A) fuse in the main under-hood fuse/relay box and the VSA modulator-control unit.

6. Turn the ignition switch to ON (II).
7. Measure the voltage between VSA modulator-control unit 47P connector terminal No. 4 and body ground.

See source image for 47P connector cavities.

- Is there battery voltage?
  - **YES** — Go to step 8.
  - **NO** — Repair open in the wire between the No. 6 (15 A) fuse in the under-dash fuse/relay box and the VSA modulator-control unit.

8. Turn the ignition switch to LOCK (0).
9. Check for continuity between VSA modulator-control unit 47P connector terminal No. 16 and body ground.

See source image for 47P connector cavities.

- Is there continuity?
  - **YES** — Go to step 10.
  - **NO** — Repair open in the wire between the VSA modulator-control unit and body ground (G303).

---

### Printed page 19-121

<a id="p1255"></a>
Source: [PDF p.1255](../page-images/p1255.png).

# VSA indicator does not go off, no DTCs — continued

10. Turn ignition ON (II).
11. Jumper VSA modulator-control unit 47P terminal 17, VSA (PNK/BLK), to body ground. **Does VSA indicator go off?** YES—Check loose 47P terminals; if needed substitute a known-good VSA unit (19-127) and retest. NO—Go to step 12.
12. Jumper gauge assembly connector B (30P) terminal 14, VSA (PNK/BLK), to body ground. **Does VSA indicator go off?** YES—Repair open between gauge assembly and VSA unit. NO—Check gauge connector B terminals; if needed substitute a known-good gauge assembly (22-89) and retest.

Connector views are from wire side of female terminals; see source image.

---

### Printed page 19-122

<a id="p1256"></a>
Source: [PDF p.1256](../page-images/p1256.png).

# VSA System Components
## Symptom Troubleshooting (cont'd)
### VSA activation indicator does not come on at start-up (bulb check)

**1.** Turn the ignition switch to ON (II), and watch the VSA activation indicator.

Does the VSA activation indicator come on for several seconds?
*   **YES** — The system is OK at this time.
*   **NO** — Go to step 2.

**2.** Apply the parking brake.

Does the brake system indicator come on?
*   **YES** — Go to step 3.
*   **NO** — Do the self-diagnostic function troubleshooting for the gauge assembly (see page 22-60).

**3.** Turn the ignition switch to LOCK (0).

**4.** Disconnect the VSA modulator-control unit 47P connector.

**5.** Connect VSA modulator-control unit 47P connector terminal No. 35 and body ground with a jumper wire, and turn the ignition switch to ON (II).


The source diagram identifies terminal 35, ACT (GRN), on the wire side of the female 47P connector.

**Post-Step 5 Diagnostic:**
Does the VSA activation indicator come on?
*   **YES** — Check for loose terminals in the VSA modulator-control unit 47P connector. If necessary, substitute a known-good VSA modulator-control unit (see page 19-127), and retest.
*   **NO** — Repair open in the wire between the gauge assembly and the VSA modulator-control unit.


### VSA activation indicator does not go off, and no DTCs are stored

**NOTE:** Do the VSA neutral position memorization (see page 19-125) first, if the indicator remains on, proceed with this flow chart.

**1.** Turn the ignition switch to ON (II), and watch the VSA activation indicator.

Does the VSA activation indicator go off?
*   **YES** — The system is OK at this time.
*   **NO** — Go to step 2.

**2.** Turn the ignition switch to LOCK (0).

**3.** Check the VSA OFF switch (see page 19-126).

Is the switch OK?
*   **YES** — Go to step 4.
*   **NO** — Replace the VSA OFF switch (see page 19-126).

**4.** Remove the gauge assembly (see page 22-89).

**5.** Disconnect the gauge assembly connector B (30P).

**6.** Disconnect the VSA modulator-control unit 47P connector.

*Procedure continues on the next page.*

---

### Printed page 19-123

<a id="p1257"></a>
Source: [PDF p.1257](../page-images/p1257.png).

# VSA activation indicator does not go off, no DTCs — continued

7. Check continuity between VSA modulator-control unit 47P terminal 35, ACT (GRN), and body ground. **Continuity?** YES—Repair short to ground between gauge assembly and VSA unit. NO—Go to step 8.
8. Disconnect VSA OFF switch 6P connector.
9. Check continuity between VSA 47P terminal 27, VSA OFF SW (WHT), and body ground. **Continuity?** YES—Repair short to ground between VSA OFF switch and VSA unit. NO—Go to step 10.
10. Substitute a known-good VSA modulator-control unit (19-127).
11. Reconnect all disconnected connectors.
12. Turn ignition ON (II).
13. Clear the DTC with the HDS.
14. Test-drive. **Does VSA activation indicator go off?** YES—Replace original VSA unit (19-127). NO—Check loose gauge-assembly connector terminals; if needed substitute a known-good gauge assembly (22-89) and retest.

See source image for 47P cavity views.

---

### Printed page 19-124

<a id="p1258"></a>
Source: [PDF p.1258](../page-images/p1258.png).

# Steering Angle Sensor Replacement

**NOTE:** Do not damage or drop the combination switch as the steering angle sensor is sensitive to shock and vibration.

1. Remove the steering wheel (see page 17-6).
2. Remove the steering column covers (see page 17-9) and the cable reel (see page 23-174).
3. Remove the combination switch assembly (see page 17-9).
4. Remove the combination light switch (A) and the wiper/washer switch (B).
   - A
5. Replace the combination switch body (C).
6. Install the combination switch in the reverse order of removal.
   **NOTE:**
    Do not remove the steering angle sensor from the combination switch body.
    When installing the cable reel, set the turn signal canceling sleeve position (see page 23-177).
7. Do the VSA sensor neutral position memorization (see page 19-125).

---

### Printed page 19-125

<a id="p1259"></a>
Source: [PDF p.1259](../page-images/p1259.png).

# Sensor cluster replacement

**Notes:** Do not damage or drop this sensitive sensor. Do not use power tools.

1. Turn ignition to LOCK (0).
2. Remove rear console (20-82).
3. Disconnect sensor cluster 6P connector (A).
4. Remove sensor cluster (B). The illustrated 6 × 1.0 mm mounting bolts torque to **9.8 N·m (1.0 kgf·m, 7.2 lbf·ft)**.
5. Install in reverse order.
6. Perform VSA sensor neutral-position memorization (19-125).

## VSA sensor neutral-position memorization

**Do not press the brake pedal during this procedure.**

1. Drive straight without steering for at least 10 ft (3 m), then park on a flat level surface with steering wheel straight.
2. With ignition at LOCK (0), connect HDS to DLC under driver's side of dashboard.
3. Turn ignition ON (II).
4. Ensure HDS communicates with vehicle and VSA unit; otherwise troubleshoot DLC circuit (11-367).
5. In HDS VSA ADJUSTMENT, perform neutral-position memorization. See HDS Help for specific instructions.
6. Turn ignition to LOCK (0).

---

### Printed page 19-126

<a id="p1260"></a>
Source: [PDF p.1260](../page-images/p1260.png).

# VSA System Components
## VSA OFF Switch Test

1. Remove the instrument panel (see page 20-84).
2. Remove the VSA OFF switch (A) by pushing from the back side of the instrument panel.
3. Check for continuity between VSA OFF switch 6P connector terminals No. 1 and No. 6. There should be continuity when the switch is pressed, and no continuity when the switch is released.
   See linked source image for terminal-side views.

4. Check for continuity between VSA OFF switch 6P connector terminals No. 2 and No. 3. There should be continuity at all times.

---

### Printed page 19-127

<a id="p1261"></a>
Source: [PDF p.1261](../page-images/p1261.png).

# VSA Modulator-Control Unit Removal and Installation

**NOTE:**
*   Do not spill brake fluid on the vehicle; it may damage the paint; if brake fluid gets on the paint, wash it off immediately with water.
*   Be careful not to damage or deform the brake lines during removal and installation.
*   To prevent the brake fluid from flowing, plug and cover the hose ends and joints with a shop towel or equivalent material.

## Removal

1. Turn the ignition switch to LOCK (0).
2. Pull down the lock (A) on the VSA modulator-control unit 47P connector (B), and remove the connector.

**Illustrated torque values:** The **two master-cylinder flare nuts** are 22 N·m (2.2 kgf·m, 16 lbf·ft); the **four wheel-circuit flare nuts** are 15 N·m (1.5 kgf·m, 11 lbf·ft); illustrated 6 mm bracket fasteners are 9.8 N·m (1.0 kgf·m, 7.2 lbf·ft). See source image for port orientation.

3. Disconnect the six brake lines from the VSA modulator-control unit (C).
4. Remove the VSA unit with bracket (D) from the body.
5. Remove the VSA unit from the bracket.

---

### Printed page 19-128

<a id="p1262"></a>
Source: [PDF p.1262](../page-images/p1262.png).

# VSA System Components
## VSA Modulator-Control Unit Removal and Installation (cont'd)
### Installation

1. Install the VSA modulator-control unit on the bracket.
2. Install the bracket with the VSA modulator-control unit to the body.
3. Reconnect the six brake lines, then tighten the flare nuts to the specified torque.
4. Align the connecting surface of the VSA modulator-control unit 47P connector to the VSA modulator-control unit.
5. Pull up the lock of the VSA modulator-control unit 47P connector, then confirm the connector is fully seated.
6. Bleed the brake system (see page 19-9).
7. Do the VSA sensor neutral position memorization (see page 19-125).
8. Start the engine, and check that the ABS and VSA indicators go off.
9. Test-drive the vehicle, and check that the ABS and VSA indicators do not come on.

**NOTE:** If the brake pedal is spongy, there may be air trapped in the modulator and then induced into the normal brake system during modulation. Bleed the brake system again (see page 19-9).

---

### Printed page 19-129

<a id="p1263"></a>
Source: [PDF p.1263](../page-images/p1263.png).

# Wheel-speed sensor inspection

1. Inspect front and rear pulsers for chipped or damaged teeth.
2. Measure the sensor-to-pulser air gap all the way around while rotating the pulser. Remove rear brake disc to measure rear sensor. If gap exceeds 1.0 mm (0.04 in.), check for a bent suspension arm.

**Standard, front and rear:** 0.4–1.0 mm (0.02–0.04 in.).

## Wheel-speed sensor replacement

Install sensors carefully to avoid twisting their wires. The illustrated front and rear sensor mounting fasteners torque to **9.8 N·m (1.0 kgf·m, 7.2 lbf·ft)**. See source image for sensor and harness routing.

---

### Printed page blank

<a id="p1264"></a>
Source: [PDF p.1264](../page-images/p1264.png).

*This source page is blank apart from a black scanning artifact. No service content is recoverable.*

---

### Printed page SRS notice

<a id="p1265"></a>
Source: [PDF p.1265](../page-images/p1265.png).

# SUPPLEMENTAL RESTRAINT SYSTEM (SRS)

**Context:** If body maintenance is required.

The S2000 SRS includes a driver's airbag in the steering wheel hub, a passenger's airbag in the dashboard above the glove box, and seat belt tensioners in the seat belt retractors. Information necessary to safely service the SRS is included in this Service Manual. Items marked with an asterisk (*) on the contents page include or are located near SRS components. Servicing, disassembling, or replacing these items requires special precautions and tools, and should be done by an authorized Honda dealer.

### Safety Warnings

*   To avoid rendering the SRS inoperative, which could lead to personal injury or death in the event of a severe frontal collision, all SRS service work should be done by an authorized Honda dealer.
*   Improper service procedures, including incorrect removal and installation of the SRS, could lead to personal injury caused by unintentional activation of the airbags and seat belt tensioners.
*   Do not bump or impact the SRS unit, or front impact sensors when the ignition switch is ON (II), or for at least 3 minutes after the ignition switch is turned OFF; otherwise, the system may fail in a collision, or airbags may deploy.
*   SRS electrical connectors are identified by yellow color coding. Related components are located in the steering column, console, dashboard, dashboard lower panel, in the dashboard above the glove box. Do not use electrical test equipment on these circuits.
