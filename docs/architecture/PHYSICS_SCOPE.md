# Physics Scope (Phase 11 — RESEARCHED, not accepted data)

## 1. NERDC scope (FACT/RESEARCH-SYNTHESIS)
- Follows the revised SSS 1–3 science curriculum (NERDC e-Curriculum portal;
  Federal Ministry of Education notice, Sept 2025).
- Physics sits with Chemistry/Biology in the sciences core; SSS 1–3 spans
  foundations of measurement through culminating physics options.
- Limitation: per-subject topic lists are behind the NERDC eID portal; we
  have not retrieved the full PDF in this phase.

## 2. WAEC scope (FACT/RESEARCH-SYNTHESIS)
- WASSCE Physics (May/June) covers: measurement/physics of measurement,
  mechanics (motion, forces, work/energy/machines), properties of matter,
  pressure, heat/temperature/thermodynamics, waves, optics, simple
  electromagnetism/electricity, current electricity, electronics, nuclear
  physics (basics).
- Assessment includes Paper 1 (objective), Paper 2 (theory), Paper 3
  (practical alternative to candidates).

## 3. JAMB scope (FACT/RESEARCH-SYNTHESIS)
- JAMB UTME Physics mirrors WAEC chapters with fewer practical hours; the
  iBASS e-syllabus lists topic scopes for measurements/units/dimensions,
  kinematics, Newton's laws, gravitation, fluid mechanics, heat,
  electrostatics/fields, current electricity/magnetic effects,
  alternating current, waves, optics, photoelectric effect, radioactivity.
- A-official scope of Physics Paper in UTME is one paper of 40 items.

## 4. Normalized canonical domains (proposed, PROPOSED label)
1. Measurement & Units
2. Kinematics (1D/2D)
3. Forces & Newton's Laws
4. Energy, Work & Power
5. Gravitation & Motion in a Plane? (orbits if upstream source covers)
6. Fluids & Pressure
7. Heat & Temperature
8. Waves & Sound
9. Optics (reflection/refraction/lenses/instruments)
10. Electrostatics & Fields
11. Electric Circuits & Current Electricity
12. Magnetism & Electromagnetic Induction
13. Electronics Basics (semiconductor, logic)
14. Modern Physics (photons, atoms/nuclei, radioactivity)

## 5. Topic mappings
- JAMB "Measurements/Units/Dimensions" ↔ NERDC measurement foundations ↔ WAEC section "Measurement of physical quantities".
- JAMB/WAEC kinematics terminology: "motion" / "uniform acceleration" appears in all three.
- WAEC "machine" ↔ JAMB "simple machines" ↔ NERDC energy/work chapter.

## 6. Source conflicts
- Depth of nuclear/modern physics: WAEC includes radioactivity; JAMB includes
  radioactivity minimally; NERDC revised curriculum may have redistributed.
- Practical component emphasis: WAEC has a dedicated alternative paper;
  JAMB has no practical; NERDC mandates laboratory work.
- Terminology vs BECE: JAMB sometimes uses "physics of sound", WAEC uses
  "waves and sound". Canonical mapping records both.

## 7. Terminology normalization
- "speed/velocity" — canonical: `velocity_vector`
- "constant acceleration" — canonical: `uniform_acceleration`
- "Ohm's law" — canonical: `ohms_law`
- Variants recorded as Candidate synonyms only; no KC yet created.

## 8. Candidate KC areas (direct evidenced from official topic lists)
- measurement_precision, units_dimensions, velocity_time_graphs,
  suvat_equations, newtons_laws, work_energy_power, pressure_fluids,
  thermal_expansion, heat_transfer, waves_basics, reflection_refraction,
  lens_formula, electrostatics_basics, ohms_law, circuit_analysis,
  electromagnetism_basics, ac_circuits_basic, photons_photoelectric,
  radioactivity_basics.
- Status: PROPOSED (not entered into CDG store).

## 9. Candidate TaskModel areas
- apply_suvat_equations, compute_resultant_force, interpret_v_t_graph,
  apply_ohms_law_to_a_circuit, design_lens_ray_diagram, compare_specific_heat_capacities.
- These will be entered only with per-KC TaskModel definitions in the
  Physics construction phase.

## 10. Practical/laboratory considerations
- WAEC practical component implies practical-derived KCs (instrument reading,
  experimental graphs). Mark: REPRESENTATIONAL methods prohibited in CDG —
  still curriculum content, enter as knowledge capabilities only.
- JAMB does not assess practicals; WAEC/NERDC mandate them.

## 11. Mathematical prerequisites (research-synthesis, requires per-claim evidence)
- Algebraic manipulation → equation solving in physics (e.g., v=u+at refactor)
- Graph interpretation → velocity-time, I-V characteristics
- Ratio/proportion → density (m/V), concentration-style formulas
- Trigonometric ratios → components, projectile motion, vector resolution
- Gradient → v-t graphs
- Indices/scientific notation → quantitative SI magnitudes
- Logarithms → rarely direct in SS Physics (radioactive decay half-life
  is logarithmic but presented graphically)
- Circular/trigonometric graphs → AC waveforms

## 12. Unresolved questions
- Exact NERDC SSS 2025 physics topic-by-topic list still requires PDF retrieval.
- Alignment depth between WAEC practical alternative paper and NERDC competencies.
- Whether 2021/2026 WAEC syllabus editions are identical.

## 13. Explicit exclusions
- No physics KCs entered into the CDG in this phase.
- No examination question banks, scoring, or learner observations.

---

## Phase 12 update — sources retrieved and slice status

### Retrieved (verified reachable, fetched)
| Source | Evidence used |
|---|---|
| SRC.OSX.UP1.1.2 Units and Standards (HTTP 200) | kc.measurement_units_dimensions |
| SRC.OSX.UP1.3.4 Constant Acceleration (HTTP 200) | kc.motion_equations_constant_acceleration; Math→Physics edges ev.p.x1/ev.p.x2 |
| SRC.OSX.UP1.4.2 Acceleration Vector (HTTP 200) | kc.motion_graph_interpretation; ev.p.x3 |
| SRC.OSX.UP1.5.2 Newton's First Law (HTTP 200, VERBATIM quote in evidence) | kc.newtons_laws; ev.p.x4 |
| SRC.OSX.UP1.5.4 Mass and Weight (HTTP 200) | kc.mass_and_weight |

### Retrieval GAPS (recorded, not fabricated)
- JAMB/IBASS Physics PDF: portal is a JS app with hashed asset URLs; the
  per-subject PDF could not be resolved in this run. Registered as
  SRC.JAMB.IBASS.PHYSICS with metadata only — NO content claims attached.
- WAEC Physics syllabus PDF: portal reachable, document not retrieved.
  Registered as SRC.WAEC.PHYSICS, metadata only.
- NERDC SSS Physics: behind portal. Registered as SRC.NERDC.SS.PHYSICS,
  metadata only.

### Status of slice content
- OpenStax-derived capability definitions: SOURCE-DERIVED (textbook reference).
- KC/TM/Method decomposition and cross-subject edges: RESEARCH SYNTHESIS →
  reviewed acceptance (human review activity `act.physics.review`).
- Official-board confirmation of topic selection: OWNER_REVIEW_REQUIRED.
- kc.measurement_errors_precision, kc.practical_measurement: PROPOSED
  (no supporting syllabus/TM evidence yet).
