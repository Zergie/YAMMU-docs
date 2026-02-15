YAMMU prioritizes mechanical reliability and serviceability over feature count.

## Design Constraints

YAMMU targets enclosed printers and may operate in elevated chamber temperatures. Components and mounting methods should allow for thermal expansion and long-term creep behavior where applicable. The system is designed for Klipper with Happy Hare and should remain serviceable with common tools, using readily available parts. Electrical design should prefer 24 V inside the chamber where practical, and avoid routing mains voltage through heated areas.

Additional constraints used in the released files:

- STL files are provided pre-oriented for printing.
- YAMMU aims to avoid slicer-generated supports. If a part requires support features, they are included in the STL geometry.
- Printed parts are designed around ABS. ABS shrinkage is accounted for in the part geometry, but fit can still vary by printer, filament brand, and process tuning.
- Other materials may work depending on chamber temperature, part geometry, and mounting, but should be validated.
- Only commonly available components are used.

## Goals

- **Mechanical reliability first.** Robust feed mechanism and consistent filament path.
- **Simple filament path.** Minimize friction points and failure modes.
- **Low-friction and serviceable design.** Components can be accessed, maintained, and replaced.
- **Prefer 24V systems over mains voltage inside the chamber.** Reduce risk by using lower voltage where practical.
- **Builder freedom.** Choose PSU and heater type. Avoid proprietary lock-in where practical.
- **Scalable concept.** Modular architecture allows future expansion.

## Notes

- YAMMU is beta-stage and evolving. Verify dimensions and fit before ordering parts.
- Heated builds require careful electrical design. Follow local electrical regulations and applicable safety practices.

## Voron Print Settings

These are the recommended settings.

- Layer height: 0.2 mm
- Extrusion width: 0.4 mm, forced
- Infill percentage: 40%
- Infill type: grid, gyroid, honeycomb, triangle, or cubic
- Wall count: 4
- Solid top/bottom layers: 5
- Supports: NONE

---
Goals and constraints may evolve as the design iterates.
