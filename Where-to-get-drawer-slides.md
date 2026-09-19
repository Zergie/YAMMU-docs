YAMMU uses four drawer slides to support two spool drawers inside the heated enclosure. Slide selection affects usable drawer travel, load capacity, and long-term serviceability. Verify dimensions and load ratings against the supplied CAD before ordering.

## Required Specification

YAMMU requires full-extension ball-bearing drawer slides. Full extension is necessary to reach the rear spool positions when loading filament. Without full extension, the rear spools are not accessible without removing the drawer entirely. Partial-extension slides reduce usable access and are not compatible with this requirement.

<img width="1275" height="215" alt="image" src="https://github.com/user-attachments/assets/bc179d36-d65a-4d51-a95c-3132a673e339" />
<img width="1275" height="215" alt="image" src="https://github.com/user-attachments/assets/7f2daae4-9e14-4e44-bf46-a26ccbd173d8" />


| Parameter    | Required Value              |
|--------------|-----------------------------|
| Extension    | Full extension (100%)       |
| Length       | 400 mm (16 inch equivalent) |
| Width        | 35 mm                       |
| Load rating  | 25 kg per pair              |
| Bearing type | Ball bearing                |
| Quantity     | 4 (2 per drawer, 2 drawers) |

## Travel and Mount Geometry

Usable travel depends on both slide length and mounting method. If slides are mounted directly to the frame, effective extension may be shorter than the nominal slide length. Mounting slides on a ball-bearing-supported offset interface can recover usable travel in builds where direct frame mounting is insufficient.

Short extension is a common serviceability problem. If the drawer does not open far enough to practically load or inspect spools, consider increasing the mount offset before sourcing longer slides.

## Load Rating

Each pair of slides carries one drawer. YAMMU has two drawers, so two pairs are required. The 25 kg per pair rating is the target range. Higher-rated slides tend to be physically larger and may not fit within the YAMMU frame geometry. Slides rated significantly above 25 kg are likely too bulky for this application.

## Sourcing Notes

Standard 35 mm wide full-extension ball-bearing slides in 400 mm or 15 3/4 inch length are widely available. European hardware suppliers, local cabinet fitting suppliers, and online marketplaces carry compatible slides. Quality varies; ball-bearing smoothness and side-load rigidity differ significantly between budget and mid-range options.

The BOM includes a sourced reference that has been tested in the current YAMMU configuration. Substitutions may work, but verify width, length, load rating, and mounting hole pattern before ordering.

## Optional Features

Many slides are available with additional features. None of these have been tested in YAMMU and compatibility is unknown:

- **Soft-close**: Hydraulic damper slows the drawer at the end of travel. May add bulk or affect mounting geometry.
- **Push-to-open**: Spring-loaded mechanism opens the drawer without a handle. May add bulk or affect mounting geometry.
- **Self-closing**: Spring pulls the drawer closed from partway. May resist drawer extension under low load.
- **Over-extension**: Extends beyond 100% of slide length. May increase usable travel but verify frame clearance.

If you are willing to test any of these features with YAMMU, get in contact with the project team before starting.

## Slide Variants to Avoid

- **Undermount or concealed slides**: Typically designed for cabinet drawer boxes, not for the YAMMU mounting geometry.
- **Partial-extension slides**: Reduce usable drawer access and are incompatible with the tethered routing requirement.
- **Roller-only (non-ball-bearing) slides**: Higher friction, reduced smoothness under load, and less consistent behavior over temperature.

---
Verify slide dimensions and mounting hole pattern against the CAD before ordering.
