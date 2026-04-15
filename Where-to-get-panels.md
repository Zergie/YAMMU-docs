Technical guidance for selecting and sourcing panel materials for YAMMU enclosures.

## Material Selection Overview

Panel material selection depends on operating temperature, mechanical requirements, and fabrication constraints. Polycarbonate and acrylic are commonly used for 3D printer enclosures. Each material has distinct thermal, mechanical, and optical characteristics.

**Decision Matrix:**

- **Heated chamber (sustained elevated temperatures):** Polycarbonate recommended. Acrylic may deform over time depending on mounting and stress.
- **Non-heated or low-temperature:** Acrylic can be suitable and more economical.
- **Optical clarity priority:** Both materials suitable when new. Polycarbonate may yellow under prolonged UV exposure.

## Recommendations by Use Case

### Non-Heated YAMMU Build (Ambient Temperature)

- **Panel material:** Acrylic (cast or extruded).
- **Thickness:** 3 mm.
- **Reasoning:** Cost-effective. Thermal deformation unlikely at ambient temperatures. Straightforward fabrication.

### Heated YAMMU Build (Chamber Temperature up to 60°C)

- **Panel material:** Polycarbonate recommended.
- **Thickness:** 3 mm.
- **Reasoning:** Acrylic may deform over time at these temperatures. Polycarbonate provides better dimensional stability under sustained elevated temperature.

### Heated YAMMU Build (Chamber Temperature above 60°C)

- **Panel material:** Polycarbonate.
- **Thickness:** 3 mm or 3+3 mm (double-wall).
- **Additional:** 3+3 mm double-wall polycarbonate will reduce heat loss and can improve stiffness at elevated chamber temperatures, depending on span and mounting.
- **Reasoning:** Polycarbonate tolerates elevated temperatures better than acrylic. Adequate frame support (typical 200-300mm span) helps minimize creep-induced deflection over time.

## Polycarbonate (PC)

### Alternate Names

- Lexan (GE Plastics brand name)
- Makrolon (Covestro/Bayer brand name)
- Panlite (Teijin brand name)
- Tuffak (Plaskolite brand name)

### Technical Properties

| Property                               | Value   | Unit      |
|----------------------------------------|---------|-----------|
| Glass transition temperature (Tg)      | 147     | °C        |
| Maximum continuous service temperature | 115-120 | °C        |
| Deflection temperature (1.8 MPa)       | 128-138 | °C        |
| Thermal expansion coefficient          | 65-70   | × 10⁻⁶ /K |
| Tensile strength                       | 55-75   | MPa       |
| Impact strength (Izod, notched)        | 600-850 | J/m       |
| Light transmission (clear, 3 mm)       | 86-90   | %         |
| Density                                | 1.20    | g/cm³     |

### Characteristics

**Thermal Performance**

- Glass transition at 147°C, but continuous service temperature is lower: typically 115-120°C depending on load and constraint.
- For YAMMU use cases, polycarbonate is the preferred panel material for heated chambers up to 60°C and above 60°C.
- 3 mm panels are suitable for typical spans. double-wall panels can be used above 60°C when reduced heat loss or higher panel stiffness is needed.
- Creep may occur under sustained load at elevated temperature. Deflection depends on span, mounting constraint, and stress state.
- Thermal conductivity: 0.19-0.22 W/(m·K). Provides moderate insulation.
- Long-term dimensional stability depends on mechanical constraint and stress.

**Durability Considerations**

- UV exposure may cause yellowing over extended periods. UV-stabilized grades reduce this effect.
- Surface scratches more easily than acrylic. Polishing is less effective than with acrylic.
- Hygroscopic material. May absorb moisture in humid environments, potentially affecting dimensional stability.

**Fire Performance**

- Self-extinguishing (UL94 V-2 rating typical, but lower grades exist).
- Limited flame propagation.
- Combustion produces carbon monoxide and trace hydrogen cyanide.

### Sourcing Notes

- Widely available from plastics distributors.
- Sold by sheet size or cut-to-size.

## Acrylic (PMMA)

### Alternate Names

- Polymethyl methacrylate (PMMA) – chemical name
- Plexiglas (Röhm brand name)
- Lucite (historical brand name, less common now)
- Perspex (common in UK/Europe)
- Acrylite (Evonik brand name)
- Oroglas (Altuglas brand name)

### Technical Properties

| Property                               | Value  | Unit      |
|----------------------------------------|--------|-----------|
| Glass transition temperature (Tg)      | 105    | °C        |
| Maximum continuous service temperature | 70-80  | °C        |
| Deflection temperature (1.8 MPa)       | 95-100 | °C        |
| Thermal expansion coefficient          | 70-77  | × 10⁻⁶ /K |
| Tensile strength                       | 65-75  | MPa       |
| Impact strength (Izod, notched)        | 15-25  | J/m       |
| Light transmission (clear, 3 mm)       | 92-93  | %         |
| Density                                | 1.18   | g/cm³     |

### Characteristics

**Thermal Performance**

- For YAMMU use cases, acrylic is suitable for non-heated ambient builds.
- Acrylic is not the preferred choice for sustained heated-chamber operation, including up to 60°C, due to higher risk of deformation over time depending on mounting and internal stress.
- Continuous service temperature: 70-80°C depending on grade and load.
- Glass transition at 105°C. Softening occurs as temperature approaches Tg.
- May deform or stress-craze in heated chambers at sustained elevated temperatures, particularly when mechanically constrained. Consider continuous service temperature and deflection temperature, not only Tg.
- Thermal conductivity: 0.17-0.19 W/(m·K). Slightly better insulation than polycarbonate.
- Behavior depends on panel thickness, span, mounting method, and internal stress.

**Durability Considerations**

- Good UV resistance. Yellowing less pronounced than polycarbonate.
- Surface hardness higher than polycarbonate. Better scratch resistance in typical use.
- Non-hygroscopic. Dimensional stability less affected by humidity than polycarbonate.

**Fire Performance**

- Flammable (UL94 HB rating typical).
- Combustion continues after ignition source removed.
- Combustion produces smoke and methyl methacrylate vapor. Use appropriate ventilation.

### Sourcing Notes

- Widely available. Typically 30-50% lower cost than polycarbonate.
- Sold by sheet size or cut-to-size.
- **Cast vs. Extruded:**
  - **Cast acrylic:** Better optical clarity, easier to machine, more brittle, higher cost.
  - **Extruded acrylic:** Lower optical clarity, somewhat tougher (but still brittle relative to PC), lower cost.
- Protective film removal after fabrication helps prevent surface damage.

## Manufacturing and Fabrication

### Cutting

**Laser Cutting**

- **Acrylic:** Excellent results. Cuts cleanly with polished edges. CO₂ laser typical.
- **Polycarbonate:** Poor results. Discoloration and rough edges. Not recommended.

**CNC Routing**

- Both materials cut well on CNC routers.
- Use sharp carbide bits. Dull bits cause chipping and melting.
- Moderate feed rates. Too fast causes chipping; too slow causes melting.

**Manual Cutting**

- Score-and-snap method works for acrylic up to 3 mm thickness.
- Polycarbonate requires saw cutting. Circular saw or jigsaw with fine-tooth blade.

### Drilling

- Use drill bits designed for plastics (sharp point, low helix angle).
- Back panel with scrap wood to prevent chipping on breakthrough.
- Moderate speeds (500-1500 RPM depending on bit size). High speed causes melting.
- Peck drilling recommended for holes deeper than 3× diameter.

## Panel Mounting and Thermal Decoupling

### Mounting Method

YAMMU panels are mounted using **3 mm foam tape** between the panel edge and the aluminum extrusion frame. This approach provides several functional benefits:

- **Thermal decoupling.** Foam tape reduces direct heat conduction from the frame to the panels, minimizing temperature gradients.
- **Accommodates thermal expansion.** Foam compresses slightly, allowing panel expansion without inducing stress.
- **Vibration damping.** Foam absorbs mechanical vibrations from drive motors and moving components.
- **Sealing.** Closed-cell foam tapes provide moderate air sealing, reducing heat loss in heated builds.

**Clip selection:**

- Use **Single_Pane** clips for standard 3 mm panels.
- Use **Double_Pane** clips for double-wall panels.

### Recommended Tape Products

**Foam Tapes for Thermal Decoupling**

Use closed-cell foam tape with acrylic or rubber adhesive backing. Foam structure provides thermal isolation and compliance for expansion.

**Recommended products:**

- **Generic PE or PU foam tape** (3 mm total thickness): Lower cost. Verify temperature rating and closed-cell structure before use.

Values above are representative for common industrial closed-cell PE foam tapes. Use the supplier datasheet as the primary reference.

**Thermal isolation performance:**

PE foam thermal conductivity (~0.04 W/(m·K)) is significantly lower than aluminum extrusion (~200 W/(m·K)) or panel materials (PC: 0.19-0.22 W/(m·K), PMMA: 0.17-0.19 W/(m·K)). At 3 mm thickness, foam tape provides effective thermal resistance between frame and panel.

**For YAMMU, 3 mm closed-cell PE foam tape is recommended.** 3.2 mm variants are also suitable.

**Tape Specifications to Verify:**

- Total thickness: 3 mm (or 3.2 mm).
- Adhesion strength: 15+ N/cm width minimum.
- Temperature rating: -40°C to 90°C minimum for heated builds.
- Closed-cell foam structure for sealing and moisture resistance.
- UV resistance if panels are exposed to sunlight.

### Installation Procedure

**Surface Preparation**

- Clean aluminum extrusion surfaces with isopropyl alcohol (IPA) or similar degreaser.
- Clean panel edges. Remove dust and oils.
- Surfaces must be dry before tape application.

**Tape Application**

- Apply foam tape to the extrusion frame, not to the panel edge. This simplifies panel removal if needed.
- Apply tape continuously along the entire panel perimeter. Gaps reduce sealing effectiveness.
- Press tape firmly to ensure full contact. Use a roller or flat tool for even pressure.
- Allow tape to bond for 24 hours before subjecting to load or temperature cycling. Acrylic adhesives reach full strength over time.

**Panel Installation**

- Remove the protective liner from the exposed tape surface.
- Align panel carefully. Tape bond is strong; repositioning may damage the tape.
- Press panel into place with firm, even pressure along all edges.
- Avoid flexing the panel during installation. This can cause stress concentration at mounting points.

### Heated Chamber Notes

For heated builds:

- Verify tape temperature rating exceeds maximum expected chamber temperature by 10-15°C margin.
- Monitor adhesion during first thermal cycles. Some tapes may require 2-3 heat cycles to stabilize.
- Foam compression under sustained heat and load may reduce thickness over time. Minimal effect on function but affects gap width.

### Non-Heated Builds

For non-heated builds:

- Use same 3 mm foam tape as heated builds for consistency.
- Thermal decoupling less critical but foam tape still provides vibration damping and sealing.
- Lower-cost generic 3 mm PE foam tape acceptable for ambient temperature use.

## Thickness Selection

### Panel Thickness Options

- **3 mm (standard):** Default panel thickness for YAMMU.
- **3+3 mm (double-wall):** Optional for polycarbonate in heated builds, especially above 60°C.
- 3 mm provides adequate rigidity for panels supported on 2020 extrusion frame at typical YAMMU span lengths.

## Building Double-Wall Panels (3+3 mm)

Use this process when you want double-wall panels for heated builds.

**Attention:** There are currently no parts for a double-walled door.

- **BOM quantity planning:** Order two copies of each panel you intend to build as double-wall. Keep panel dimensions and hole patterns matched as a pair.
- **Clip type:** Use **Double_Pane** clips for these panel assemblies.
- **Interlayer tape:** Use **VHB 5952** or a comparable tape with **1 mm** thickness. Verify temperature rating, adhesive compatibility, and datasheet values for your chamber target.
- **Bonding method:** Clean mating faces with IPA, apply tape strips, then laminate the second panel onto the first with even pressure.
- **Expansion allowance:** Do not make a continuous fully constrained tape ring. Leave a small discontinuity in the tape path so the panel pair can accommodate thermal expansion with lower internal stress.

## Cost Comparison

Typical pricing (regional variation significant):

| Material           | Thickness | Approximate Cost per m² |
|--------------------|-----------|-------------------------|
| Acrylic (extruded) | 3 mm      | €18-25                  |
| Acrylic (cast)     | 3 mm      | €25-35                  |
| Polycarbonate      | 3 mm      | €40-55                  |

Treat these prices as indicative only. Small-quantity purchases may see a 20-30% premium. Cut-to-size service often adds another €5-15 per cut.

## Safety and Handling

### Polycarbonate

- Gloves recommended during handling. Skin oils may cause surface haze.
- Cutting generates fine dust. Use dust mask or extraction.
- Avoid aromatic solvents for cleaning. Use mild soap and water or dedicated plastic cleaner.
- Store flat or vertically. Shallow-angle storage may cause bowing.

### Acrylic

- Brittle material. Handle with care to avoid edge cracking.
- Cutting generates dust. Use extraction or dust mask.
- Acetone dissolves PMMA. Keep separated from fabrication area.
- Store flat. Vertical storage suitable for thicker sheets (6mm and above).

## Summary Table

| Criterion                  | Polycarbonate                       | Acrylic   |
|----------------------------|-------------------------------------|-----------|
| Max continuous temperature | 115°C                               | 70-80°C   |
| Impact resistance          | Excellent                           | Poor      |
| Optical clarity            | Good (yellows over time)            | Excellent |
| Scratch resistance         | Poor                                | Good      |
| UV resistance              | Moderate (stabilized grades better) | Excellent |
| Flame resistance           | Self-extinguishing                  | Flammable |
| Cost                       | Higher                              | Lower     |
| Laser cutting              | Poor                                | Excellent |
| Chemical resistance        | Moderate                            | Moderate  |
| Polishability              | Difficult                           | Easy      |

---
*Material properties are typical values. Verify specifications with manufacturer datasheets for critical applications.*
