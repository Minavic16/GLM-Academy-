# Physics Coverage Matrix (Phase 12B)

Denominator: JAMB UTME Physics topic families 1–39 as reconstructed from the
myschool.ng syllabus mirror (secondary source — wording SOURCE_UNVERIFIED;
topic *existence* corroborated by known JAMB structure + OpenStax volume
organization). Official PDFs still pending; see `PHYSICS_SOURCE_RESEARCH.md`.

Statuses: COVERED | PARTIALLY_COVERED | NOT_COVERED | SOURCE_UNVERIFIED |
OWNER_REVIEW_REQUIRED. Covered rows cite canonical IDs verified in
`examples/math_cdg_v2.json` after the Phase 12B build.

| Req | Topic family (mirror wording) | KCs | TMs / Methods | Prereqs | Evidence | Mapping |
|---|---|---|---|---|---|---|
| R01 | 1. Measurements and units | kc.measurement_units_dimensions | tm.convert_and_check_units / si_prefix, dimensional | math alg (DERIVED) | UP1 1.2 | COVERED |
| R02 | 2. Scalars and vectors | kc.scalar_vector_quantities | tm.resolve_vectors / classify, resolve-components | math trig (DERIVED, method-scope) | UP1 2.2 | COVERED |
| R03 | 3. Motion (position, speed, velocity, acceleration) | kc.displacement_velocity | tm.interpret_motion_graph (co-target) | math alg | UP1 4.2 | COVERED |
| R04 | Rectilinear acceleration / equations of motion | kc.motion_equations_constant_acceleration | tm.solve_constant_acceleration / suvat, graph-extract | math alg + linear eqs (DERIVED) | UP1 3.4 | COVERED |
| R05 | 4. Mass/weight; 5. Equilibrium; Newton + momentum | kc.newtons_laws, kc.mass_and_weight, kc.linear_momentum | tm.apply_newtons_second_law / resultant, F=ma; tm.momentum_problems / conservation | internal mass→Newton (UNDERSTAND); math alg | UP1 5.2/5.4/6.1/9.1 | COVERED |
| R06 | 6.–7. Friction; simple machines | (via work/energy methods) | — | — | UP1 7.1 | PARTIALLY_COVERED |
| R07 | 8.–11. Elasticity; pressure; fluids | kc.pressure_fluids | tm.fluid_pressure_problems / hydrostatic | math ratio (DERIVED) | UP1 14.1 | COVERED |
| R08 | 12.–17. Temperature, expansion, gas laws, heat | kc.heat_temperature | tm.thermal_problems / calorimetry, gas-law | math alg | UP2 1.1 | COVERED |
| R09 | SHM; 17.–22. Waves and sound | kc.wave_phenomena | tm.wave_problems / v=fλ | physics disp→waves (DERIVED) | UP1 15.1/16.1 | COVERED |
| R10 | 23.–27. Light, reflection, refraction, lenses, instruments | kc.geometrical_optics | tm.optics_problems / reflection-law, refraction | physics tri→optics (UNDERSTAND) | UP3 2.1 | COVERED |
| R11 | Gravitational field; satellites | kc.gravitation | tm.gravitation_problems / inverse-square | physics newton→grav (DERIVED) | UP1 13.1 | COVERED |
| R12 | 15. Work, energy, power | kc.work_energy_power | tm.work_energy_problems / work-from-force, conservation | physics newton→work; math rate (method-scope) | UP1 7.1/7.3/8.1 | COVERED |
| R13 | 28.–32. Electrostatics, cells, current, energy/power | kc.electric_circuits | tm.circuit_analysis / ohm-law, kirchhoff-loops | math simlin (DERIVED, method-scope) + alg | UP2 9.4/10.3 | COVERED |
| R14 | 33.–37. Magnets, force on conductor, EMI, AC | kc.electromagnetism | tm.emi_ac_problems / faraday-rate | math rate (DERIVED) | UP2 13.1/15.2 | COVERED |
| R15 | 38. Modern physics; 29.–30. Atom/nucleus; photoelectric | kc.atomic_nuclear_physics | tm.modern_physics_problems / photoelectric-E, nuclear-Q | math indices (DERIVED) | UP3 6.2/10.1 | COVERED |
| R16 | Practical / experimental skills | kc.practical_measurement, kc.measurement_errors_precision | tm.practical_physics / instrument-tabulate, plot-gradient | physics units→practical; math gradient (DERIVED) | UP1 lab-context + WAEC-practical (SOURCE_UNVERIFIED detail) | PARTIALLY_COVERED |
| R17 | 5. Fibre optics; 6. LASER; 39. Intro electronics | — | — | — | — | NOT_COVERED |
| R18 | 21. EM waves / spectrum | (via UP2 16.5 evidence; no dedicated KC) | — | — | UP2 16.5 | PARTIALLY_COVERED |
| R19 | 14. Energy (mechanical/heat/society), renewables | (covered computationally via work/heat KCs) | — | — | — | PARTIALLY_COVERED |

Notes: R17–R19 are SHOULD/DEFER level; R16 is MUST but WAEC-practical detail
is SOURCE_UNVERIFIED, so PARTIALLY_COVERED. Using the mirror as denominator is
itself OWNER_REVIEW_REQUIRED (recorded, not silently decided).
