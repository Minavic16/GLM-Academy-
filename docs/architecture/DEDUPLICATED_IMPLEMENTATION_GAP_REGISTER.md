# Deduplicated Proposed Implementation-Gap Register (Phase 16B)

Combines gaps from:
- Phase 16 NERDC SSS1/SSS2 content check (docs/architecture/CHEMISTRY_SYLLABUS_COVERAGE.md, PHYSICS_SYLLABUS_COVERAGE.md, MATHEMATICS_SYLLABUS_COVERAGE.md, CLOSURE_REGISTERS.md CI-11…CI-26)
- Phase 16B Syllabus NG JAMB/WAEC secondary-source coverage comparison (six JAMB/WAEC coverage matrices)

Gaps are deduplicated by topic family per subject. Each gap lists every source that evidences it. This register is PROPOSED only — no implementation occurs in Phase 16B, and no gap here may be implemented without an explicit owner-scoped, validated change. Subject implementation statuses: Mathematics scope EXPANDED in Phase 17 (batches 066-069: sets, logic, sequences & series, matrices & determinants, mensuration) but remains BOARD_UNVERIFIED; Physics IMPL_COMPLETE/BOARD_UNVERIFIED; Chemistry IMPL_PARTIAL/BOARD_UNVERIFIED.

Status vocabulary: Open | Blocked | Deferred (owner-documented).

## MATHEMATICS gaps

| ID | Topic family | Sources evidencing gap | CDG entities affected | Gap class | Status | Rationale | Proposed resolution | Next action |
|---|---|---|---|---|---|---|---|---|
| M-01 | Sets | NERDC SSS1 p.7; JAMB SN4; WAEC topic 7 | kc.sets_operations | IMPLEMENTATION_GAP | Closed (implemented Phase 17 batch 066) | NERDC SSS1 p.7 lists sets; no CDG KC existed | Added kc.sets_operations + tm.set_operations + 2 methods + item; NERDC evidence | Owner decision: scope extension (now implemented) |
| M-02 | Logical reasoning | NERDC SSS1 p.8; SSS2 p.9; WAEC topic 8 | kc.logical_reasoning | IMPLEMENTATION_GAP | Closed (implemented Phase 17 batch 066) | NERDC SSS1 p.8/SSS2 p.9 list logic; no CDG KC existed | Added kc.logical_reasoning + tm.logical_reasoning + 2 methods + item; NERDC evidence; prerequisite link to sets is curriculum-adjacency elaboration | Owner decision: scope extension (now implemented) |
| M-03 | Modular arithmetic | WAEC topic 2 | — | IMPLEMENTATION_GAP | Open | WAEC lists modulo arithmetic; NERDC SSS1/SSS2 topic lists and JAMB do not show it explicitly | Add modular-arithmetic KC | Owner decision: scope extension |
| M-04 | Number bases (conversion/fractional parts) | NERDC SSS1 p.1/p.5; JAMB SN1; WAEC topic 1 | kc.equations_in_indices | PARTIAL_GAP | Open | All three sources include number bases; CDG KC exists but base-conversion operations not explicitly evidenced | Add number-base methods to indices TM | Owner decision |
| M-05 | Surds | NERDC SSS2 p.3; JAMB SN3; WAEC topic 10 | — | IMPLEMENTATION_GAP | Open | All three sources include surds; no CDG KC | Add surds KC | Owner decision: scope extension |
| M-06 | Sequences & series | NERDC SSS2 p.1; JAMB SN4; WAEC topic 6 | kc.sequences_series | IMPLEMENTATION_GAP | Closed (implemented Phase 17 batch 067) | All three sources include sequences/series; no CDG KC existed | Added kc.sequences_series + tm.sequences_series + 2 methods + item; NERDC SSS2 p.1 evidence | Owner decision: scope extension (now implemented) |
| M-07 | Matrices & determinants | JAMB SN6; WAEC topic 11 | kc.matrix_algebra | IMPLEMENTATION_GAP | Closed (implemented Phase 17 batch 068) | JAMB and WAEC include matrices; NERDC SSS1/SSS2 topic lists do not show it | Added kc.matrix_algebra + tm.matrix_algebra + 2 methods + item; secondary JAMB/WAEC evidence via Syllabus NG ONLY (disclosed — not in NERDC SSS1/SSS2; SSS3 unretrieved) | Owner decision: scope extension (now implemented); disclose secondary-evidence limitation |
| M-08 | Mensuration (areas/volumes) | NERDC SSS1 p.11; JAMB SN3; WAEC topics 25–27 | kc.mensuration | PARTIAL_GAP | Closed (implemented Phase 17 batch 069) | NERDC SSS1 p.11 and JAMB/WAEC include mensuration; only kc.distance_formula existed | Added kc.mensuration + tm.mensuration + 2 methods + item; NERDC SSS1 p.11 evidence | Owner decision: scope extension (now implemented) |
| M-09 | Loci & construction | JAMB SN3; WAEC topics 31–32 | — | IMPLEMENTATION_GAP | Open | JAMB and WAEC include loci/construction; no CDG KC | Add loci/construction KC | Owner decision: scope extension |
| M-10 | Binary operations | JAMB SN5; WAEC topic 17(iii) | — | IMPLEMENTATION_GAP | Open | JAMB and WAEC include binary operations; no CDG KC | Add binary-operations KC | Owner decision: scope extension |
| M-11 | Permutation & combination | JAMB SN5 | kc.counting_principle | PARTIAL_GAP | Open | JAMB includes permutation/combination; CDG counting-principle KC exists but arrangement objectives not evidenced | Add permutation/combination methods | Owner decision |
| M-12 | Coordinate geometry (line-equation forms) | JAMB SN3; WAEC topic 33 | kc.equation_of_line, kc.gradient, kc.distance_formula | PARTIAL_GAP | Open | JAMB/WAEC include coordinate geometry; CDG has line KCs but two-point/point-slope/general forms not evidenced | Add line-equation methods | Owner decision |
| M-13 | Trigonometry applications (elevation/depression; bearings; triangle area) | JAMB SN3; WAEC topics 34–36 | kc.trig_ratios_acute, kc.sine_rule, kc.cosine_rule | PARTIAL_GAP | Open | All three sources include trigonometry; application objectives not evidenced | Add trig-application methods | Owner decision |
| M-14 | Calculus (limits; trig differentiation; area under curve) | JAMB SN4; WAEC topic 40 | kc.differentiation_algebraic, kc.integration_algebraic | PARTIAL_GAP | Open | JAMB/WAEC include calculus; NERDC SSS1/SSS2 topic lists do not show it explicitly | Add limits/trig/area methods | Owner decision |
| M-15 | Statistics: grouped data; ogive; charts | NERDC SSS2 p.16–19 (ogive documented deferral); JAMB SN5; WAEC topic 41 | kc.mean_ungrouped_data, kc.median_ungrouped, kc.measures_of_dispersion | PARTIAL_GAP | Open | Ogive documented as deferral; grouped-data statistics and charts not evidenced | Add grouped-data/ogive methods OR retain deferral | Owner decision (ogive deferral stands unless reversed) |
| M-16 | Compound probability rules | JAMB SN5; WAEC topic 42 | kc.theoretical_probability | PARTIAL_GAP | Open | All three sources include probability; compound-event rules not evidenced | Add probability methods | Owner decision |
| M-17 | Vectors (plane arithmetic) | WAEC topic 43 | kc.scalar_vector_quantities | PARTIAL_GAP | Open | WAEC only (among sources checked) | Add vector-arithmetic methods | Owner decision |
| M-18 | Transformations | WAEC topic 44 | — | IMPLEMENTATION_GAP | Open | WAEC only | Add transformations KC | Owner decision: scope extension |
| M-19 | Financial mathematics | WAEC topics 13–14; JAMB SN2 (simple interest/profit/loss/VAT) | kc.percentage_concept, kc.ratio_proportion_rate | PARTIAL_GAP | Open | WAEC lists extensive financial maths; no financial KC | Add financial-mathematics KC | Owner decision: scope extension |

## PHYSICS gaps

| ID | Topic family | Sources evidencing gap | CDG entities affected | Gap class | Status | Rationale | Proposed resolution | Next action |
|---|---|---|---|---|---|---|---|---|
| P-01 | Projectile motion | NERDC SSS2 p.7; JAMB topic 3(f) | — | IMPLEMENTATION_GAP | Open | NERDC SSS2 and JAMB both list projectile motion; no CDG KC | Add projectile KC using existing Math→Physics quadratic dependencies | Recorded (CI-17); owner decision |
| P-02 | Simple harmonic motion | NERDC SSS2 p.8; JAMB topic 3(i) | — | IMPLEMENTATION_GAP | Open | NERDC SSS2 and JAMB both list SHM; no CDG KC | Add SHM KC | Recorded (CI-18); owner decision |
| P-03 | Simple machines | JAMB topic 8 | — | IMPLEMENTATION_GAP | Open | JAMB lists simple machines; NERDC SSS1/SSS2 topic lists do not show it | Add machines KC | Owner decision: scope extension |
| P-04 | Elasticity | JAMB topic 9 | — | IMPLEMENTATION_GAP | Open | JAMB lists elasticity; NERDC SSS1/SSS2 topic lists do not show it | Add elasticity KC | Owner decision: scope extension |
| P-05 | Circular motion | JAMB topic 3(h) | kc.newtons_laws | PARTIAL_GAP | Open | JAMB lists circular motion; CDG Newton's laws KC exists but circular-motion objectives not evidenced | Add circular-motion methods | Owner decision |
| P-06 | Electrostatics (Coulomb's law; electric field) | JAMB topic 28 | kc.electric_circuits | PARTIAL_GAP | Open | JAMB lists electrostatics; CDG circuits KC exists but electrostatics detail not evidenced | Add electrostatics methods | Owner decision |
| P-07 | Capacitors | JAMB topic 29 | kc.electric_circuits | PARTIAL_GAP | Open | JAMB lists capacitors; not a distinct KC | Add capacitor methods | Owner decision |
| P-08 | Electric cells | JAMB topic 30 | kc.electric_circuits | PARTIAL_GAP | Open | JAMB lists cell types; not explicitly evidenced | Add cell methods | Owner decision |
| P-09 | Circuit analysis methods (Ohm's law; meter bridge; potentiometer) | JAMB topic 31 | kc.electric_circuits | PARTIAL_GAP | Open | JAMB lists circuit methods; not explicitly evidenced | Add circuit-analysis methods | Owner decision |
| P-10 | Electrical energy & power applications (transmission; wiring; fuses) | JAMB topic 32 | kc.electric_circuits | PARTIAL_GAP | Open | JAMB lists applications; not explicitly evidenced | Add application methods | Owner decision |
| P-11 | Electromagnetic induction applications (generators; transformers; inductance; eddy current) | JAMB topic 35 | kc.electromagnetism | PARTIAL_GAP | Open | JAMB lists induction applications; not explicitly evidenced | Add induction-application methods | Owner decision |
| P-12 | A.C. circuits | JAMB topic 36 | kc.electromagnetism | PARTIAL_GAP | Open | JAMB lists A.C. circuits; not explicitly evidenced | Add A.C.-circuit methods | Owner decision |
| P-13 | Modern physics detail (photoelectric; x-rays; radioactivity; half-life) | NERDC SSS2 p.45; JAMB topic 38 | kc.atomic_nuclear_physics | PARTIAL_GAP | Open | All three sources (NERDC/JAMB; WAEC page defective) agree modern physics is core | Add modern-physics methods | Owner decision |
| P-14 | Viscosity / Stoke's law | JAMB topic 7; WAEC topic 7 | kc.friction | PARTIAL_GAP | Open | All three sources list friction; viscosity detail not evidenced | Add viscosity methods | Owner decision |
| P-15 | Force–time graph; Lami's theorem; moments | JAMB topic 3(g); JAMB topic 5 | kc.newtons_laws, kc.friction | PARTIAL_GAP | Open | JAMB lists equilibrium/momentum objectives; not explicitly evidenced | Add equilibrium/momentum methods | Owner decision |
| P-16 | Energy-society applications (dams; nuclear; solar devices) | JAMB topic 6(b) | kc.work_energy_power, kc.energy_sources | PARTIAL_GAP | Open | JAMB lists energy-society; not explicitly evidenced | Add application methods | Owner decision |
| P-17 | Specific heat capacity; latent heat; heat transfer | JAMB topics 13–19 | kc.heat_temperature | PARTIAL_GAP | Open | JAMB lists heat topics; not explicitly evidenced | Add heat-measurement methods | Owner decision |

## CHEMISTRY gaps

| ID | Topic family | Sources evidencing gap | CDG entities affected | Gap class | Status | Rationale | Proposed resolution | Next action |
|---|---|---|---|---|---|---|---|---|
| C-01 | Water | NERDC SSS1 p.17; SSS2 p.10; JAMB SN6 | — | IMPLEMENTATION_GAP | Open | NERDC SSS1/SSS2 and JAMB list water; no CDG KC | Add water KC | Recorded (CI-16); owner decision |
| C-02 | Air | NERDC SSS2 p.12; JAMB SN5 | — | IMPLEMENTATION_GAP | Open | NERDC SSS2 and JAMB list air; no CDG KC | Add air KC | Owner decision: scope extension |
| C-03 | Non-metals (hydrogen, oxygen, nitrogen, sulphur, halogens) | NERDC SSS2 p.13/15/17/19/21; JAMB SN15 | — | IMPLEMENTATION_GAP | Open | NERDC SSS2 and JAMB list non-metals; no CDG KC | Add non-metals KC | Owner decision: scope extension |
| C-04 | Metals & extraction | NERDC SSS1 p.18 (mention); JAMB SN16 | — | IMPLEMENTATION_GAP | Open | NERDC SSS1 and JAMB list metals; no CDG KC | Add metals KC | Owner decision: scope extension |
| C-05 | Alkynes; benzene/aromatic; carbohydrates; proteins; enzymes | JAMB SN17; WAEC Chemistry of Carbon Compounds | kc.organic_foundations, kc.reactions_of_alkanes, kc.reactions_of_alkenes, kc.isomerism, kc.alcohols, kc.ethers, kc.aldehydes_ketones, kc.carboxylic_acids, kc.amines, kc.amides | PARTIAL_GAP | Open | CDG batch 065 covers alkanes/alkenes/isomerism/alcohols/ethers/aldehydes-ketones/carboxylic acids/amines/amides; JAMB/WAEC list additional organic families | Add organic-family KCs | Owner decision |
| C-06 | Polymers | JAMB SN17; WAEC Basic Biochemistry & Synthetic Polymers | — | IMPLEMENTATION_GAP | Deferred (owner-documented CI-13) | JAMB/WAEC include polymers; deferral stands | Revisit with owner authorization | Recorded (CI-13) |
| C-07 | Industrial chemistry | JAMB SN18; WAEC Chemistry Industry & the Environment | — | IMPLEMENTATION_GAP | Deferred (owner-documented CI-14) | JAMB/WAEC include industry; deferral stands | Revisit with owner authorization | Recorded (CI-14) |
| C-08 | Environmental pollution | JAMB SN8; WAEC Chemistry Industry & the Environment | — | IMPLEMENTATION_GAP | Open | JAMB and WAEC include pollution; NERDC SSS1/SSS2 topic lists do not show it | Add pollution KC | Owner decision: scope extension |
| C-09 | Solubility | WAEC topic: Solubility of Substances | — | IMPLEMENTATION_GAP | Open | WAEC lists solubility; NERDC SSS1/SSS2 topic lists do not show it | Add solubility KC | Owner decision: scope extension |
| C-10 | Separation techniques & purity criteria (methods) | NERDC SSS1 p.4; JAMB SN1; WAEC Standard Separation Techniques | kc.matter_classification, kc.practical_chemistry | PARTIAL_GAP | Open | All three sources list separation; CDG practical KC covers titration/qualitative tests only | Add separation-technique methods | Owner decision |
| C-11 | Salt preparation & hydrolysis | JAMB SN9; WAEC Acids Bases & Salts | kc.acids_bases_salts | PARTIAL_GAP | Open | All three sources list salts; hydrolysis/preparation detail not evidenced | Add salt-methods | Owner decision |
| C-12 | Buffers proper | Phase 15 scope constraint; no NERDC/JAMB/WAEC topic lists "buffer" explicitly | kc.ph_scale | IMPLEMENTATION_GAP | Blocked | Buffer pH needs Mathematics kc.logarithms; new cross-subject dependency would modify Mathematics records | Owner-authorized scoped Mathematics extension; then Chemistry buffer KCs/TM | Recorded (CI-11/CI-12); blocked |
| C-13 | Titration systems & standard solutions (WAEC practical) | WAEC Quantitative Analysis (acid-base; redox systems: MnO4–/Fe2+; MnO4–/C2O42–; I2/S2O32-) | kc.practical_chemistry | PARTIAL_GAP | Open | WAEC practical paper lists specific systems; CDG covers titration generally | Add WAEC titration-system methods | Owner decision |
| C-14 | Qualitative-analysis detail (WAEC practical) | WAEC Qualitative Analysis (cations; anions; gases; functional-group tests) | kc.practical_chemistry | PARTIAL_GAP | Open | WAEC lists specific confirmatory/gas/organic tests | Add qualitative-test methods | Owner decision |

## Cross-subject gaps

| ID | Topic family | Sources evidencing gap | Gap class | Status | Rationale | Proposed resolution | Next action |
|---|---|---|---|---|---|---|---|
| X-01 | Chemistry buffers ← Mathematics logarithms | Phase 15 scope constraint; CI-09; NERDC/JAMB/WAEC acids/bases topics include pH but not buffers explicitly | IMPLEMENTATION_GAP (cross-subject) | Blocked | Creating the prerequisite edge modifies Mathematics-side records; Phase 15/16 forbid | Owner-authorized scoped Mathematics change (new prerequisite edge scoped to a buffer TM), then Chemistry buffer KCs | Owner decision on scoped Mathematics change |

## Topics whose inclusion, depth, or current applicability requires official confirmation

All topics above marked BOARD_UNVERIFIED. In particular:
- Topics present in JAMB/WAEC secondary sources but absent from NERDC SSS1/SSS2 topic lists (M-03 modular arithmetic; M-07 matrices; M-09 loci/construction; M-17 vectors; M-18 transformations; P-03 simple machines; P-04 elasticity; C-02 air; C-04 metals; C-06 polymers; C-07 industry; C-08 pollution; C-09 solubility) require confirmation against NERDC SSS3 (unretrieved) and against official JAMB/WAEC documents before any scope decision.
- Topics present in NERDC but not yet evidenced at method level in the CDG (all PARTIAL_GAP rows) require evidence mapping before the CDG can claim COVERED.
- No topic may be promoted to COVERED-at-official level until official JAMB/WAEC/NERDC documents are obtained and content-checked (CI-24).
