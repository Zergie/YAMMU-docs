Practical guidance for acquiring components. Verify dimensions and interfaces against the CAD before ordering.


## Frame & Structural Parts

### Aluminum Extrusions

- 2020 profile standard throughout.
- See [Where to get aluminium extrusions](Where-to-get-aluminium-extrusions.md) for extrusion variants and practical notes.
- Note: Aluminum conducts heat. Consider thermal isolation if running sustained elevated chamber temperatures.

### Panels

- **Polycarbonate recommended** for heated builds. Better dimensional stability at elevated temperatures, but creep can still occur depending on mounting and load.
- **Acrylic acceptable** for non-heated or low-temperature applications.
- Typical thickness: 3 mm for side panels, 4 mm for structural panels.
- See [Where to get panels](Where-to-get-panels.md) for detailed material behavior.

### Fasteners

- Stainless steel M3 and M5 bolts, T-nuts, and drop-in nuts preferred.
- Avoid zinc-plated fasteners in heated environments.

### Motion Components

- **400mm full-extension drawer slides** for drawer movement.
- GT2 pulleys and belts for feeder drives.

#### BLDC Motors (36mm class)

- YAMMU uses **36mm-class BLDC gear motors** for the feeders.
- Typical supply voltage: **24V**.
- Select gear ratio for the required feed speed and torque.
- The commonly used **3525 gear motor** variant is typically based on the **JGB37** gearbox family.
- Control interface is simple:
    - **PWM** (speed command)
    - **DIR** (direction)
    - **Tacho** output (speed feedback)
- Verify logic voltage levels and pull-up requirements for the tacho output.
- Verify shaft diameter/length and mounting pattern against the CAD before ordering.

#### Drive Gears

- Dual-gear BMG-style extruder gears recommended.
- Avoid cheap brass gears. They wear quickly under abrasive filaments.
- Stainless hobbed gears are preferred.

#### Servos

- YAMMU uses **DSPOWER 21 g metal gear servos** (4x) for actuator functions. Dimensions: **29.6 x 13.2 x 40 mm**.

### PTFE Tubing

- Use **4 mm OD** PTFE tube to match the fittings used in YAMMU.
- A mixed-ID approach can work well:
    - **3 mm ID / 4 mm OD** for runs that do not move during operation (static routing inside the frame/drawer). This can reduce drag and is more tolerant of slightly oval filament.
    - **2 mm ID / 4 mm OD** for runs that move (e.g. the connection between the drawer and the printer, or any section that flexes during drawer motion). This provides better lateral support and can reduce the tendency to buckle under compression.
- For soft or high-friction filaments (e.g. TPU, heavily filled materials), **2 mm ID** can increase drag. Verify with your filament set and routing.
- Tube ends should be cut square, deburred, and lightly chamfered on the ID to avoid catching at fittings.
- Fittings: YAMMU uses several **ECAS04** collets and one **PC4-M10** fitting.

### Spool Rollers

- 608 bearings typical.
- Ensure smooth rotation. Binding rollers cause feed inconsistency.
- Spool holders include an auto-rewind feature with an adjustable clutch.
- Rewind force is provided by an ID card badge spring.

### Filament Sensors

- Mechanical sensors placed at the splitter.
- Used to confirm filament presence and detect runout/jams.

Consistency and low friction matter more than exotic solutions.


## Electronics

This section requires careful attention to safety.

### Power Supply

- **24V DC PSU recommended.** 600W range typical for 8-channel system with optional heating.
- Mean Well LRS-600-24 widely used and reliable.
- Size PSU for continuous load, not peak. Leave 20% headroom.

### Routing and Safety

- **Avoid routing mains voltage into the chamber if possible.**
- Use MOSFETs for DC heater control. Ensure adequate heat sinking.
- If AC heaters are used, mount the SSR or contactor outside the heated area (e.g. the electronics bay).
    - **Mains wiring must be performed by qualified personnel.** Follow local electrical regulations. Incorrect wiring can cause fire, electric shock, or death.

### Wiring

- Use proper gauge wiring. 18 AWG for feeder motor power lines, 16 AWG or larger for heater circuits.
- Secure cable routing. Avoid sharp bends near heated areas.
- Use silicone-insulated wire in high-temperature zones.

**Critical Disclaimer:**

**Mains voltage wiring must be performed by qualified personnel in accordance with local electrical regulations. If you are not competent in electrical safety, do not attempt mains wiring. Incorrect wiring can cause fire, electric shock, or death.**


## Heating (Optional)

Adding chamber heating increases complexity and risk. Proceed only if you understand thermal and electrical safety.

### PTC Heaters

- Self-limiting ceramic heaters. Simple and robust.
- Typical: 200W heater.
- Operate on 24V DC or mains AC depending on model. **DC variants strongly preferred inside chamber.**

### Thermal Protection

- A thermal fuse is strongly recommended. 80-90°C cutoff is typical for chamber safety.
- Consider bimetallic thermostats as secondary protection.
- Use a dedicated temperature sensor for feedback control.

### Voltage Isolation

- If using AC heaters, ensure no live metal is accessible inside the chamber.
- Ground all conductive parts properly.

**If you are not comfortable with electrical safety, do not build a heated system.**


### Upgrade Path

- Double-wall polycarbonate panels can improve insulation.
- Added thickness can affect fit and mounting. Verify clearances before ordering.

---
Keep tone pragmatic. Overengineering is expensive. Build for your actual requirements.
