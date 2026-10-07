# Cross-Subject Dependency Audit (Phase 11)

No cross-subject edges are entered into the canonical CDG in this phase.
All candidates below are RESEARCHED/PROPOSED only and must pass the Phase 11
policy before being added.

| Candidate | Source KC (Math) | Target capability | Classification | Evidence status |
|---|---|---|---|---|
| Algebraic manipulation → Physics equation solving | kc.algebraic_expressions | rearrange suvat, v=u+at, etc. | CORE_CROSS_SUBJECT_DEPENDENCY | Legacy evidence E0124, E0123 used in Math; Physics-specific claim needs its own source row (OPEN) |
| Graph interpretation → Motion graphs | kc.function_concept (+ linear equations) | interpret velocity-time / displacement-time graphs | CORE_CROSS_SUBJECT_DEPENDENCY | JAMB/WAEC syllabus mentions graph skills; explicit CDG edge requires TaskModel evidence (OPEN) |
| Ratio/proportion → Concentration/stoichiometry | kc.ratio_proportion_rate | chemistry molar ratios, concentrations in g/dm³ | CORE_CROSS_SUBJECT_DEPENDENCY | Mathematics-side prerequisite verified (E0033); Chemistry side needs OWN claim evidence before edge acceptance |
| Logarithms → pH | none in Graph yet | pH = -log[H+] | POSSIBLE_DEPENDENCY | pH is in JAMB/WAEC but our Math graph has no log-KC → deferred until log KC enters Math |
| Indices/scientific notation → quantitative magnitude handling | kc.equations_in_indices (weak at scientific notation) | Physics/Chemistry numeric work | IMPORTANT_CROSS_SUBJECT_DEPENDENCY | Partial; a dedicated scientific-notation KC in Math would be needed first |
| Gradient → velocity from v–t | kc.gradient | Physics motion | IMPORTANT_CROSS_SUBJECT_DEPENDENCY | Requires TM for motion-v-t; OPEN |
| Trigonometric ratios → vector resolution | kc.trig_ratios_acute | resolving forces/displacements | IMPORTANT_CROSS_SUBJECT_DEPENDENCY | Trig chain mature enough; needs in Physics construction (OPEN) |
| Statistics/probability → experiment design | kc.mean_ungrouped_data | lab data analysis | POSSIBLE_DEPENDENCY | No direct curriculum task demand yet |
| Quadratics → projectile motion | kc.quadratic_roots, kc.quadratic_by_factorisation | vertical motion equations | IMPORTANT_CROSS_SUBJECT_DEPENDENCY | Requires Physics projectile TM (OPEN) |
| Simultaneous equations → circuit analysis (2 unknowns) | kc.simultaneous_linear_equations | Kirchhoff equations | POSSIBLE_DEPENDENCY | Needs circuit KC + evidence |
| Differentiation → motion (s→v) | kc.differentiation_algebraic | rate of change of displacement | CORE_CROSS_SUBJECT_DEPENDENCY | Our Calculus chain extends to kinematics in Physics; requires Physics TM (OPEN) |
| Integration → area under curve | kc.integration_algebraic | distance from v–t | IMPORTANT_CROSS_SUBJECT_DEPENDENCY | Open — needs Physics TM (OPEN) |
| Percentage → efficiency/yield | kc.percentage_concept | Physics efficiency, Chemistry atom economy | IMPORTANT_CROSS_SUBJECT_DEPENDENCY | Math KC accepted; subject task evidence OPEN |
| Sine/cosine rules → non-right force triangles | kc.sine_rule / kc.cosine_rule | resultant of non-collinear forces | POSSIBLE_DEPENDENCY | OPEN |
| Circle geometry → circular motion | kc.circle_angle_theorems | angular relationships | POSSIBLE_DEPENDENCY | OPEN |
| Counting principle → combinatorial probability (Chemistry rare) | kc.counting_principle | independent events | NOT_YET_JUSTIFIED | recommended skip |

## Decision rules applied in the audit
- Only edges whose *target TaskModel's Method* lists the source KC as
  required get a DERIVED/SPECIFIC_TASK_MODEL prerequisite.
- Cross-subject edges are not stored until the target capability exists.
- Today's canonical CDG contains zero accepted cross-subject edges; that is
  correct given Physics/Chemistry construction has not begun.
