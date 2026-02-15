YAMMU - Yet Another Multi-Material Unit is an open-source multi-material filament handling system for enclosed 3D printers.

## Introduction

YAMMU is an open-source multi-material filament handling system designed for enclosed 3D printers, particularly Voron-style builds. It provides 8-spool capacity through a dual-drawer storage system, with modular feeder units and a PTFE splitter architecture. The design prioritizes mechanical robustness and heated chamber compatibility.

**This is not a commercial plug-and-play product.**

YAMMU is in beta stage. Builders should understand mechanics, electronics, and the iterative nature of open-source hardware development. This project requires technical competency and patience. Contributions are welcome.

### Why YAMMU Exists

Many multi-material systems are closed-source, unnecessarily complex, or mechanically fragile. YAMMU takes a different approach:

- **Mechanical robustness first.** The filament path and feed mechanism prioritize reliability over feature count.
- **Simplicity where possible.** Avoid electronics complexity when mechanical solutions suffice.
- **Serviceability.** Components are accessible. No proprietary lock-in.
- **Understandable design.** If you can read CAD files and understand basic electromechanical principles, you can build and modify YAMMU.

This project targets builders who value engineering clarity over marketing promises.

## Builder Advice

### Before You Start

- **Study the CAD files thoroughly.** Understand how the system works before ordering parts.
- **Read the build documentation in the main YAMMU repository.** It contains the current build steps, wiring notes, and Klipper/Happy Hare configuration details.
- **Check the Bill of Materials.** See [Bill-Of-Material](Bill-Of-Material.md) for current component list.
- **Expect iteration.** This is beta stage. You may need to adjust dimensions, tolerances, or component choices.
- **Do not expect plug-and-play.** You may need to troubleshoot and modify parts. This is normal for open-source hardware.

### During the Build

- Test each subsystem independently before integration.
- Verify drawer movement before installing feeders.
- Verify feeder motor control: PWM range, direction, and tacho signal before loading filament.
- Check PTFE routing for kinks or sharp bends.

**Electrical Safety**

- YAMMU uses 24V DC for heater control and motor circuits inside the enclosure.
- Mains voltage wiring must be performed by qualified personnel only.
- Follow local electrical regulations and codes.
- Do not route mains voltage inside heated enclosures unless absolutely necessary and properly rated.

### After First Power-On

- Run thermal tests if using chamber heating. Monitor temperatures for 1 hour minimum.
- Verify filament feeds consistently at low speed before attempting fast retractions.
- Ramp feeder speed/torque gradually. Aggressive settings can cause slip, grinding, or jams.

### Sharing Your Work

Contributions improve YAMMU for everyone:

- **Share modifications.** Post CAD changes, wiring improvements, firmware tweaks.
- **Fork the design.** If you need a variant, make it and document it.
- **Contribute back.** Pull requests welcome. Documentation improvements welcome.

---
YAMMU is not finished. It is functional but evolving. Expect iteration. Verify dimensions and fit before ordering parts.
