# Mathematics CDG — Human Inspection Index

Generated deterministically from `examples/math_cdg_v2.json`
by `tools/generate_math_cdg_docs.py`. Do not edit by hand.

## Current Graph Statistics

- Knowledge Components: 68
- TaskModels: 64
- Methods: 95
- Items: 40
- Misconceptions: 1
- Claims: 451
- Evidence records: 253
- Sources: 73
- Activities: 165
- Agents: 2
- Exported nodes: 271
- Exported edges: 451
- Accepted Claims: 449; PROPOSED Claims: 2

## KC Index

| ID | Name | Domain | Status | Owning TMs |
|---|---|---|---|---|
| `kc.acids_bases_salts` | Acids, bases, salts and neutralisation | Chemistry | ACCEPTED | tm.acid_base_problems |
| `kc.algebraic_expressions` | Algebraic expressions: terms, coefficients, like terms, substitution | Algebra | ACCEPTED | tm.handle_algebraic_expressions |
| `kc.atomic_nuclear_physics` | Atomic structure, photoelectric effect and nuclei | Physics | ACCEPTED | tm.modern_physics_problems |
| `kc.atomic_structure_periodicity` | Atomic structure and the periodic table | Chemistry | ACCEPTED | tm.atomic_model_problems |
| `kc.change_of_subject` | Change of subject of a formula/relation | Algebra | ACCEPTED | tm.make_subject |
| `kc.chemical_bonding` | Ionic and covalent bonding | Chemistry | ACCEPTED | tm.bonding_problems |
| `kc.chemical_energetics` | Energy changes in chemical reactions | Chemistry | ACCEPTED | tm.energetics_problems |
| `kc.circle_angle_theorems` | Basic circle angle theorems | Geometry | ACCEPTED | tm.circle_angle_problems |
| `kc.completing_the_square` | Completing the square | Algebra | ACCEPTED | tm.complete_square |
| `kc.cosine_rule` | Cosine rule for oblique triangles | Trigonometry | ACCEPTED | tm.solve_oblique_triangle |
| `kc.counting_principle` | Fundamental (multiplication) counting principle | Statistics & Probability | ACCEPTED | tm.count_outcomes |
| `kc.differentiation_algebraic` | Differentiation of explicit algebraic functions | Calculus | ACCEPTED | tm.differentiate_explicit |
| `kc.direct_variation` | Direct variation | Algebra | ACCEPTED | tm.direct_variation_problems |
| `kc.displacement_velocity` | Displacement, velocity and acceleration | Physics | ACCEPTED | tm.interpret_motion_graph |
| `kc.distance_formula` | Distance between two points in the plane | Coordinate Geometry | ACCEPTED | tm.compute_distance |
| `kc.electric_circuits` | Current, voltage, resistance and circuits | Physics | ACCEPTED | tm.circuit_analysis |
| `kc.electromagnetism` | Electromagnetic induction and AC basics | Physics | ACCEPTED | tm.emi_ac_problems |
| `kc.equation_of_line` | Equation of a straight line (all forms) | Coordinate Geometry | ACCEPTED | tm.find_line_equation |
| `kc.equations_in_indices` | Equations involving indices | Number & Numeration | ACCEPTED | tm.solve_index_equation |
| `kc.factorisation_quadratic_trinomial` | Factorisation of quadratic trinomials | Algebra | ACCEPTED | tm.factorise_quadratic_trinomial |
| `kc.fraction_decimal_operations` | Operations on fractions and decimals | Number & Numeration | ACCEPTED | tm.fraction_decimal_operations |
| `kc.function_concept` | Function concept and notation | Functions | ACCEPTED | tm.evaluate_and_represent_function |
| `kc.gas_behaviour` | Gas laws and molar gas volumes | Chemistry | ACCEPTED | tm.gas_problems |
| `kc.geometrical_optics` | Reflection, refraction and image formation | Physics | ACCEPTED | tm.optics_problems |
| `kc.gradient` | Gradient of a line segment | Coordinate Geometry | ACCEPTED | tm.compute_gradient |
| `kc.gravitation` | Gravitation and gravitational field | Physics | ACCEPTED | tm.gravitation_problems |
| `kc.heat_temperature` | Heat, temperature and thermal behaviour | Physics | ACCEPTED | tm.thermal_problems |
| `kc.integer_arithmetic` | Signed-number (integer) arithmetic | Number & Numeration | ACCEPTED | tm.signed_number_arithmetic |
| `kc.integration_algebraic` | Elementary integration of algebraic functions | Calculus | ACCEPTED | tm.integrate_polynomial |
| `kc.linear_equations_one_var` | Linear equations in one variable | Algebra | ACCEPTED | tm.solve_linear_equations_one_var |
| `kc.linear_inequalities_analytic` | Linear inequalities: analytical solution | Algebra | ACCEPTED | tm.solve_linear_inequality |
| `kc.linear_momentum` | Linear momentum and its conservation | Physics | ACCEPTED | tm.momentum_problems |
| `kc.logarithms` | Logarithms and their laws | Number & Numeration | ACCEPTED | tm.logarithm_problems |
| `kc.mass_and_weight` | Mass, weight and inertia | Physics | ACCEPTED | tm.apply_newtons_second_law |
| `kc.matter_classification` | Elements, compounds, mixtures and separation | Chemistry | ACCEPTED | tm.classify_matter |
| `kc.maxima_minima` | Maxima and minima of a function | Calculus | ACCEPTED | tm.find_maxima_minima |
| `kc.mean_ungrouped_data` | Mean of ungrouped data | Statistics & Probability | ACCEPTED | tm.compute_mean |
| `kc.measurement_errors_precision` | Measurement errors, precision and significant figures | Physics | ACCEPTED | tm.practical_physics |
| `kc.measurement_units_dimensions` | Physical quantities, SI units and dimensions | Physics | ACCEPTED | tm.convert_and_check_units |
| `kc.mole_stoichiometry` | Mole concept and stoichiometry | Chemistry | ACCEPTED | tm.stoichiometry_problems |
| `kc.motion_equations_constant_acceleration` | Equations of motion (constant acceleration) | Physics | ACCEPTED | tm.solve_constant_acceleration |
| `kc.motion_graph_interpretation` | Interpretation of motion graphs | Physics | ACCEPTED | tm.interpret_motion_graph |
| `kc.newtons_laws` | Newton's laws of motion | Physics | ACCEPTED | tm.apply_newtons_second_law |
| `kc.organic_foundations` | Hydrocarbons and functional groups | Chemistry | ACCEPTED | tm.organic_problems |
| `kc.parallel_line_angles` | Angles formed by parallel lines and a transversal | Geometry | ACCEPTED | tm.identify_parallel_line_angles |
| `kc.parallel_perpendicular_lines` | Conditions for parallel and perpendicular lines | Coordinate Geometry | ACCEPTED | tm.classify_line_relationships |
| `kc.percentage_concept` | Percentages | Number & Numeration | ACCEPTED | tm.percentage_problems |
| `kc.ph_scale` | pH scale and calculations | Chemistry | ACCEPTED | tm.ph_problems |
| `kc.practical_chemistry` | Practical chemistry procedures | Chemistry | ACCEPTED | tm.practical_chemistry |
| `kc.practical_measurement` | Experimental measurement practice | Physics | ACCEPTED | tm.practical_physics |
| `kc.pressure_fluids` | Density, pressure and fluids at rest | Physics | ACCEPTED | tm.fluid_pressure_problems |
| `kc.quadratic_by_factorisation` | Solving quadratic equations by factorisation | Algebra | ACCEPTED | tm.solve_quadratic_by_factorisation |
| `kc.quadratic_formula` | Quadratic formula | Algebra | ACCEPTED | tm.apply_quadratic_formula |
| `kc.quadratic_roots` | Roots of quadratic equations (any method) | Algebra | ACCEPTED | tm.find_quadratic_roots |
| `kc.rate_of_change` | Rate of change of a function | Calculus | ACCEPTED | tm.compute_rate_of_change |
| `kc.rates_equilibrium` | Reaction rates and chemical equilibrium | Chemistry | ACCEPTED | tm.rate_equilibrium_problems |
| `kc.ratio_proportion_rate` | Ratio, proportion and rate | Number & Numeration | ACCEPTED | tm.solve_proportions |
| `kc.redox_electrochemistry` | Redox reactions and electrolysis | Chemistry | ACCEPTED | tm.redox_problems |
| `kc.scalar_vector_quantities` | Scalars, vectors and vector resolution | Physics | ACCEPTED | tm.resolve_vectors |
| `kc.simultaneous_linear_equations` | Simultaneous linear equations in two variables | Algebra | ACCEPTED | tm.solve_simultaneous_linear_two_vars |
| `kc.simultaneous_linear_quadratic` | Simultaneous equations: one linear, one quadratic | Algebra | ACCEPTED | tm.solve_linear_quadratic_system |
| `kc.sine_rule` | Sine rule for oblique triangles | Trigonometry | ACCEPTED | tm.solve_oblique_triangle |
| `kc.special_angle_values` | Exact trigonometric values of special angles | Trigonometry | ACCEPTED | tm.recall_special_values |
| `kc.theoretical_probability` | Theoretical probability of an event | Statistics & Probability | ACCEPTED | tm.compute_probability |
| `kc.triangle_angle_properties` | Triangle angle properties | Geometry | ACCEPTED | tm.triangle_angle_problems |
| `kc.trig_ratios_acute` | Trigonometric ratios of acute angles | Trigonometry | ACCEPTED | tm.trig_ratio_problems |
| `kc.wave_phenomena` | Wave motion, frequency and wave speed | Physics | ACCEPTED | tm.wave_problems |
| `kc.work_energy_power` | Work, energy and power | Physics | ACCEPTED | tm.work_energy_problems |

### KC Prerequisite Index

| Prerequisite | → | Dependent | Purpose | Scope | Origin |
|---|---|---|---|---|---|
| `kc.algebraic_expressions` | → | `kc.factorisation_quadratic_trinomial` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.function_concept` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.quadratic_formula` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.algebraic_expressions` | → | `kc.linear_equations_one_var` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.simultaneous_linear_equations` | EXECUTE | ALL_RELEVANT_METHODS | DERIVED |
| `kc.completing_the_square` | → | `kc.quadratic_formula` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.factorisation_quadratic_trinomial` | → | `kc.quadratic_by_factorisation` | EXECUTE | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.quadratic_formula` | → | `kc.quadratic_roots` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.integer_arithmetic` | → | `kc.algebraic_expressions` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.integer_arithmetic` | → | `kc.factorisation_quadratic_trinomial` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.integer_arithmetic` | → | `kc.linear_equations_one_var` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.displacement_velocity` | → | `kc.motion_equations_constant_acceleration` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.displacement_velocity` | → | `kc.motion_graph_interpretation` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.quadratic_by_factorisation` | EXECUTE | ALL_RELEVANT_METHODS | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.simultaneous_linear_equations` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.mass_and_weight` | → | `kc.newtons_laws` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.quadratic_by_factorisation` | → | `kc.quadratic_roots` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.quadratic_roots` | → | `kc.simultaneous_linear_quadratic` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.simultaneous_linear_equations` | → | `kc.simultaneous_linear_quadratic` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.fraction_decimal_operations` | → | `kc.percentage_concept` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.integer_arithmetic` | → | `kc.fraction_decimal_operations` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.parallel_line_angles` | → | `kc.triangle_angle_properties` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.parallel_line_angles` | → | `kc.triangle_angle_properties` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.algebraic_expressions` | → | `kc.gradient` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.trig_ratios_acute` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.fraction_decimal_operations` | → | `kc.mean_ungrouped_data` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.differentiation_algebraic` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.function_concept` | → | `kc.differentiation_algebraic` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.differentiation_algebraic` | → | `kc.rate_of_change` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.differentiation_algebraic` | → | `kc.maxima_minima` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.quadratic_roots` | → | `kc.maxima_minima` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.differentiation_algebraic` | → | `kc.integration_algebraic` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.fraction_decimal_operations` | → | `kc.theoretical_probability` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.trig_ratios_acute` | → | `kc.cosine_rule` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.trig_ratios_acute` | → | `kc.sine_rule` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.gradient` | → | `kc.equation_of_line` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.change_of_subject` | → | `kc.equation_of_line` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.triangle_angle_properties` | → | `kc.circle_angle_theorems` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.gradient` | → | `kc.parallel_perpendicular_lines` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.fraction_decimal_operations` | → | `kc.ratio_proportion_rate` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.direct_variation` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.trig_ratios_acute` | → | `kc.special_angle_values` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.integer_arithmetic` | → | `kc.counting_principle` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.distance_formula` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.gradient` | → | `kc.distance_formula` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.scalar_vector_quantities` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.trig_ratios_acute` | → | `kc.scalar_vector_quantities` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.measurement_units_dimensions` | → | `kc.scalar_vector_quantities` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.algebraic_expressions` | → | `kc.work_energy_power` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.newtons_laws` | → | `kc.work_energy_power` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.rate_of_change` | → | `kc.work_energy_power` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.algebraic_expressions` | → | `kc.linear_momentum` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.newtons_laws` | → | `kc.linear_momentum` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.gravitation` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.newtons_laws` | → | `kc.gravitation` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.pressure_fluids` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.ratio_proportion_rate` | → | `kc.pressure_fluids` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.heat_temperature` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.integer_arithmetic` | → | `kc.heat_temperature` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.ratio_proportion_rate` | → | `kc.heat_temperature` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.algebraic_expressions` | → | `kc.wave_phenomena` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.displacement_velocity` | → | `kc.wave_phenomena` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.geometrical_optics` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.ratio_proportion_rate` | → | `kc.geometrical_optics` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.triangle_angle_properties` | → | `kc.geometrical_optics` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.algebraic_expressions` | → | `kc.electric_circuits` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.ratio_proportion_rate` | → | `kc.electric_circuits` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.simultaneous_linear_equations` | → | `kc.electric_circuits` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.algebraic_expressions` | → | `kc.electromagnetism` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.rate_of_change` | → | `kc.electromagnetism` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.algebraic_expressions` | → | `kc.atomic_nuclear_physics` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.equations_in_indices` | → | `kc.atomic_nuclear_physics` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.gradient` | → | `kc.practical_measurement` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.integer_arithmetic` | → | `kc.practical_measurement` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.measurement_units_dimensions` | → | `kc.practical_measurement` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.matter_classification` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.matter_classification` | → | `kc.atomic_structure_periodicity` | UNDERSTAND | ALL_RELEVANT_METHODS | ASSERTED |
| `kc.atomic_structure_periodicity` | → | `kc.chemical_bonding` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.chemical_bonding` | → | `kc.mole_stoichiometry` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.percentage_concept` | → | `kc.mole_stoichiometry` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.ratio_proportion_rate` | → | `kc.mole_stoichiometry` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.mole_stoichiometry` | → | `kc.acids_bases_salts` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.chemical_bonding` | → | `kc.redox_electrochemistry` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.electric_circuits` | → | `kc.redox_electrochemistry` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.mole_stoichiometry` | → | `kc.redox_electrochemistry` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.mole_stoichiometry` | → | `kc.chemical_energetics` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.function_concept` | → | `kc.rates_equilibrium` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.mole_stoichiometry` | → | `kc.gas_behaviour` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.ratio_proportion_rate` | → | `kc.gas_behaviour` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.chemical_bonding` | → | `kc.organic_foundations` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.acids_bases_salts` | → | `kc.practical_chemistry` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.matter_classification` | → | `kc.practical_chemistry` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.algebraic_expressions` | → | `kc.logarithms` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.equations_in_indices` | → | `kc.logarithms` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.acids_bases_salts` | → | `kc.ph_scale` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.ph_scale` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.logarithms` | → | `kc.ph_scale` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.linear_inequalities_analytic` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.equations_in_indices` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.change_of_subject` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.motion_equations_constant_acceleration` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.algebraic_expressions` | → | `kc.newtons_laws` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.gradient` | → | `kc.motion_graph_interpretation` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.motion_equations_constant_acceleration` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |

## TaskModel Index

### `tm.acid_base_problems` — Solve neutralisation and titration problems

- Targets: kc.acids_bases_salts
- Methods: m.neutralisation_titration
- Status: ACCEPTED

### `tm.apply_newtons_second_law` — Apply Newton's second law to force problems

- Targets: kc.mass_and_weight, kc.newtons_laws
- Methods: m.f_equals_ma, m.resultant_force
- Status: ACCEPTED

### `tm.apply_quadratic_formula` — Apply the quadratic formula

- Targets: kc.quadratic_formula
- Methods: m.substitute_formula
- Status: ACCEPTED

### `tm.atomic_model_problems` — Deduce structure and predict periodic trends

- Targets: kc.atomic_structure_periodicity
- Methods: m.electron_arrangement, m.trend_prediction
- Status: ACCEPTED

### `tm.bonding_problems` — Classify bonds and write formulae

- Targets: kc.chemical_bonding
- Methods: m.formula_from_valency, m.ionic_vs_covalent
- Status: ACCEPTED

### `tm.circle_angle_problems` — Solve circle angle problems using theorems

- Targets: kc.circle_angle_theorems
- Methods: m.centre_vs_circumference
- Status: ACCEPTED

### `tm.circuit_analysis` — Analyse DC circuits

- Targets: kc.electric_circuits
- Methods: m.kirchhoff_loops, m.ohms_law
- Status: ACCEPTED

### `tm.classify_line_relationships` — Classify whether two lines are parallel, perpendicular or neither

- Targets: kc.parallel_perpendicular_lines
- Methods: m.compare_gradients
- Status: ACCEPTED

### `tm.classify_matter` — Classify matter and separate mixtures

- Targets: kc.matter_classification
- Methods: m.separate_mixtures
- Status: ACCEPTED

### `tm.complete_square` — Complete the square

- Targets: kc.completing_the_square
- Methods: m.cts_standard_form, m.cts_then_roots
- Status: ACCEPTED

### `tm.compute_distance` — Compute the distance between two coordinate points

- Targets: kc.distance_formula
- Methods: m.distance_formula
- Status: ACCEPTED

### `tm.compute_gradient` — Compute the gradient of a line segment

- Targets: kc.gradient
- Methods: m.gradient_from_two_points
- Status: ACCEPTED

### `tm.compute_mean` — Compute the mean of a set of values

- Targets: kc.mean_ungrouped_data
- Methods: m.sum_divide_count
- Status: ACCEPTED

### `tm.compute_probability` — Compute the theoretical probability of an event

- Targets: kc.theoretical_probability
- Methods: m.favourable_over_total
- Status: ACCEPTED

### `tm.compute_rate_of_change` — Compute the rate of change of a function at a point

- Targets: kc.rate_of_change
- Methods: m.derivative_at_point
- Status: ACCEPTED

### `tm.convert_and_check_units` — Convert physical quantities and check dimensions

- Targets: kc.measurement_units_dimensions
- Methods: m.dimensional_consistency, m.si_prefix_conversion
- Status: ACCEPTED

### `tm.count_outcomes` — Count outcomes of a multi-stage experiment

- Targets: kc.counting_principle
- Methods: m.multiply_choices
- Status: ACCEPTED

### `tm.differentiate_explicit` — Differentiate an explicit algebraic function

- Targets: kc.differentiation_algebraic
- Methods: m.power_rule
- Status: ACCEPTED

### `tm.direct_variation_problems` — Solve direct-variation problems

- Targets: kc.direct_variation
- Methods: m.find_constant
- Status: ACCEPTED

### `tm.emi_ac_problems` — Solve induction/AC problems

- Targets: kc.electromagnetism
- Methods: m.faraday_rate
- Status: ACCEPTED

### `tm.energetics_problems` — Solve reaction-energy problems

- Targets: kc.chemical_energetics
- Methods: m.enthalpy_hess
- Status: ACCEPTED

### `tm.evaluate_and_represent_function` — Evaluate and represent functions

- Targets: kc.function_concept
- Methods: m.evaluate_substitution, m.table_of_values
- Status: ACCEPTED

### `tm.factorise_quadratic_trinomial` — Factorise quadratic trinomials

- Targets: kc.factorisation_quadratic_trinomial
- Methods: m.factorise_by_grouping, m.factorise_unit_leading
- Status: ACCEPTED

### `tm.find_line_equation` — Find the equation of a straight line

- Targets: kc.equation_of_line
- Methods: m.point_gradient
- Status: ACCEPTED

### `tm.find_maxima_minima` — Find local maxima and minima

- Targets: kc.maxima_minima
- Methods: m.first_derivative
- Status: ACCEPTED

### `tm.find_quadratic_roots` — Find the roots of a quadratic equation

- Targets: kc.quadratic_roots
- Methods: m.roots_via_completing_square, m.roots_via_factorisation, m.roots_via_formula
- Status: ACCEPTED

### `tm.fluid_pressure_problems` — Solve density/pressure problems

- Targets: kc.pressure_fluids
- Methods: m.hydrostatic
- Status: ACCEPTED

### `tm.fraction_decimal_operations` — Perform operations on fractions/decimals

- Targets: kc.fraction_decimal_operations
- Methods: m.convert_common_denominator
- Status: ACCEPTED

### `tm.gas_problems` — Solve gas-law problems

- Targets: kc.gas_behaviour
- Methods: m.combined_gas_law
- Status: ACCEPTED

### `tm.gravitation_problems` — Solve gravitation and g-field problems

- Targets: kc.gravitation
- Methods: m.inverse_square
- Status: ACCEPTED

### `tm.handle_algebraic_expressions` — Simplify and evaluate algebraic expressions

- Targets: kc.algebraic_expressions
- Methods: m.collect_like_terms, m.expand_simplify
- Status: ACCEPTED

### `tm.identify_parallel_line_angles` — Identify/apply parallel-line angle relations

- Targets: kc.parallel_line_angles
- Methods: m.corresponding_alternate
- Status: ACCEPTED

### `tm.integrate_polynomial` — Integrate a polynomial term-by-term

- Targets: kc.integration_algebraic
- Methods: m.reverse_power_rule
- Status: ACCEPTED

### `tm.interpret_motion_graph` — Interpret and construct motion graphs (displacement/velocity)

- Targets: kc.displacement_velocity, kc.motion_graph_interpretation
- Methods: m.displacement_from_st, m.slope_of_vt
- Status: ACCEPTED

### `tm.logarithm_problems` — Evaluate and manipulate logarithms

- Targets: kc.logarithms
- Methods: m.apply_log_laws, m.convert_exp_log
- Status: ACCEPTED

### `tm.make_subject` — Make a specified variable the subject

- Targets: kc.change_of_subject
- Methods: m.collect_factor_subject, m.inverse_operations
- Status: ACCEPTED

### `tm.modern_physics_problems` — Solve photoelectric/nuclear problems

- Targets: kc.atomic_nuclear_physics
- Methods: m.photoelectric_equation
- Status: ACCEPTED

### `tm.momentum_problems` — Solve momentum and collision problems

- Targets: kc.linear_momentum
- Methods: m.conservation_collisions
- Status: ACCEPTED

### `tm.optics_problems` — Solve reflection/refraction/image problems

- Targets: kc.geometrical_optics
- Methods: m.mirror_lens_equation, m.reflection_refraction
- Status: ACCEPTED

### `tm.organic_problems` — Name hydrocarbons and classify groups

- Targets: kc.organic_foundations
- Methods: m.hydrocarbon_naming
- Status: ACCEPTED

### `tm.percentage_problems` — Solve percentage problems

- Targets: kc.percentage_concept
- Methods: m.percent_as_fraction
- Status: ACCEPTED

### `tm.ph_problems` — Compute pH from concentration

- Targets: kc.ph_scale
- Methods: m.ph_from_concentration
- Status: ACCEPTED

### `tm.practical_chemistry` — Perform titration and qualitative tests

- Targets: kc.practical_chemistry
- Methods: m.qualitative_tests, m.titration_procedure
- Status: ACCEPTED

### `tm.practical_physics` — Carry out measurements and analyse data

- Targets: kc.measurement_errors_precision, kc.practical_measurement
- Methods: m.instrument_tabulate, m.plot_gradient
- Status: ACCEPTED

### `tm.rate_equilibrium_problems` — Interpret rates and equilibria

- Targets: kc.rates_equilibrium
- Methods: m.le_chatelier, m.rate_curves
- Status: ACCEPTED

### `tm.recall_special_values` — State exact trig values at special angles

- Targets: kc.special_angle_values
- Methods: m.from_special_triangles
- Status: ACCEPTED

### `tm.redox_problems` — Solve redox and electrolysis problems

- Targets: kc.redox_electrochemistry
- Methods: m.electrolysis_quantitative, m.redox_identification
- Status: ACCEPTED

### `tm.resolve_vectors` — Classify quantities and resolve vectors

- Targets: kc.scalar_vector_quantities
- Methods: m.classify_quantities, m.resolve_components
- Status: ACCEPTED

### `tm.signed_number_arithmetic` — Perform signed-number arithmetic

- Targets: kc.integer_arithmetic
- Methods: m.sign_rules
- Status: ACCEPTED

### `tm.solve_constant_acceleration` — Solve constant-acceleration motion problems

- Targets: kc.motion_equations_constant_acceleration
- Methods: m.graph_extract_motion, m.suvat_equations
- Status: ACCEPTED

### `tm.solve_index_equation` — Solve an equation involving indices

- Targets: kc.equations_in_indices
- Methods: m.logs, m.match_bases
- Status: ACCEPTED

### `tm.solve_linear_equations_one_var` — Solve linear equations in one variable

- Targets: kc.linear_equations_one_var
- Methods: m.expand_collect, m.isolate_variable
- Status: ACCEPTED

### `tm.solve_linear_inequality` — Solve a linear inequality in one variable

- Targets: kc.linear_inequalities_analytic
- Methods: m.balance_inverse, m.test_graph
- Status: ACCEPTED

### `tm.solve_linear_quadratic_system` — Solve a system with one linear and one quadratic equation

- Targets: kc.simultaneous_linear_quadratic
- Methods: m.substitute_linear_into_quadratic
- Status: ACCEPTED

### `tm.solve_oblique_triangle` — Solve a non-right triangle

- Targets: kc.cosine_rule, kc.sine_rule
- Methods: m.cosine_rule, m.sine_rule
- Status: ACCEPTED

### `tm.solve_proportions` — Solve proportion and rate problems

- Targets: kc.ratio_proportion_rate
- Methods: m.unitary_method
- Status: ACCEPTED

### `tm.solve_quadratic_by_factorisation` — Solve a quadratic equation by factorisation

- Targets: kc.quadratic_by_factorisation
- Methods: m.factorise_zero_product, m.special_product_zero_product
- Status: ACCEPTED

### `tm.solve_simultaneous_linear_two_vars` — Solve simultaneous linear equations in two variables

- Targets: kc.simultaneous_linear_equations
- Methods: m.solve_by_elimination, m.solve_by_substitution
- Status: ACCEPTED

### `tm.stoichiometry_problems` — Solve mole and equation problems

- Targets: kc.mole_stoichiometry
- Methods: m.empirical_formula, m.mole_ratio
- Status: ACCEPTED

### `tm.thermal_problems` — Solve heat/temperature/gas problems

- Targets: kc.heat_temperature
- Methods: m.calorimetry, m.gas_law
- Status: ACCEPTED

### `tm.triangle_angle_problems` — Solve triangle angle problems

- Targets: kc.triangle_angle_properties
- Methods: m.exterior_angle, m.triangle_angle_sum
- Status: ACCEPTED

### `tm.trig_ratio_problems` — Solve right-triangle problems using trigonometric ratios

- Targets: kc.trig_ratios_acute
- Methods: m.label_sides_match_ratio
- Status: ACCEPTED

### `tm.wave_problems` — Solve wave speed/frequency problems

- Targets: kc.wave_phenomena
- Methods: m.wave_equation
- Status: ACCEPTED

### `tm.work_energy_problems` — Solve work/energy/power problems

- Targets: kc.work_energy_power
- Methods: m.power_as_rate, m.work_from_force
- Status: ACCEPTED

## Method Index (AND within method, OR across methods)

### `tm.acid_base_problems`

- **`m.neutralisation_titration`** requires: kc.algebraic_expressions, kc.mole_stoichiometry

### `tm.apply_newtons_second_law`

- **`m.f_equals_ma`** requires: kc.algebraic_expressions, kc.mass_and_weight, kc.newtons_laws
- **`m.resultant_force`** requires: kc.algebraic_expressions, kc.mass_and_weight, kc.newtons_laws

### `tm.apply_quadratic_formula`

- **`m.substitute_formula`** requires: kc.algebraic_expressions, kc.integer_arithmetic

### `tm.atomic_model_problems`

- **`m.electron_arrangement`** requires: kc.integer_arithmetic, kc.matter_classification
- **`m.trend_prediction`** requires: kc.matter_classification

### `tm.bonding_problems`

- **`m.formula_from_valency`** requires: kc.atomic_structure_periodicity, kc.integer_arithmetic
- **`m.ionic_vs_covalent`** requires: kc.algebraic_expressions, kc.atomic_structure_periodicity

### `tm.circle_angle_problems`

- **`m.centre_vs_circumference`** requires: kc.integer_arithmetic, kc.triangle_angle_properties

### `tm.circuit_analysis`

- **`m.kirchhoff_loops`** requires: kc.algebraic_expressions, kc.simultaneous_linear_equations
- **`m.ohms_law`** requires: kc.algebraic_expressions, kc.ratio_proportion_rate

### `tm.classify_line_relationships`

- **`m.compare_gradients`** requires: kc.gradient, kc.integer_arithmetic

### `tm.classify_matter`

- **`m.separate_mixtures`** requires: kc.algebraic_expressions

### `tm.complete_square`

- **`m.cts_standard_form`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.cts_then_roots`** requires: kc.algebraic_expressions, kc.integer_arithmetic

### `tm.compute_distance`

- **`m.distance_formula`** requires: kc.algebraic_expressions, kc.gradient, kc.integer_arithmetic

### `tm.compute_gradient`

- **`m.gradient_from_two_points`** requires: kc.algebraic_expressions, kc.integer_arithmetic

### `tm.compute_mean`

- **`m.sum_divide_count`** requires: kc.fraction_decimal_operations, kc.integer_arithmetic

### `tm.compute_probability`

- **`m.favourable_over_total`** requires: kc.fraction_decimal_operations, kc.integer_arithmetic

### `tm.compute_rate_of_change`

- **`m.derivative_at_point`** requires: kc.differentiation_algebraic, kc.integer_arithmetic

### `tm.convert_and_check_units`

- **`m.dimensional_consistency`** requires: kc.algebraic_expressions
- **`m.si_prefix_conversion`** requires: kc.algebraic_expressions

### `tm.count_outcomes`

- **`m.multiply_choices`** requires: kc.integer_arithmetic, kc.ratio_proportion_rate

### `tm.differentiate_explicit`

- **`m.power_rule`** requires: kc.algebraic_expressions, kc.function_concept

### `tm.direct_variation_problems`

- **`m.find_constant`** requires: kc.integer_arithmetic, kc.linear_equations_one_var

### `tm.emi_ac_problems`

- **`m.faraday_rate`** requires: kc.algebraic_expressions, kc.rate_of_change

### `tm.energetics_problems`

- **`m.enthalpy_hess`** requires: kc.algebraic_expressions, kc.mole_stoichiometry

### `tm.evaluate_and_represent_function`

- **`m.evaluate_substitution`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.table_of_values`** requires: kc.algebraic_expressions

### `tm.factorise_quadratic_trinomial`

- **`m.factorise_by_grouping`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.factorise_unit_leading`** requires: kc.algebraic_expressions, kc.integer_arithmetic

### `tm.find_line_equation`

- **`m.point_gradient`** requires: kc.algebraic_expressions, kc.change_of_subject, kc.gradient

### `tm.find_maxima_minima`

- **`m.first_derivative`** requires: kc.differentiation_algebraic, kc.quadratic_roots

### `tm.find_quadratic_roots`

- **`m.roots_via_completing_square`** requires: kc.completing_the_square
- **`m.roots_via_factorisation`** requires: kc.quadratic_by_factorisation
- **`m.roots_via_formula`** requires: kc.quadratic_formula

### `tm.fluid_pressure_problems`

- **`m.hydrostatic`** requires: kc.algebraic_expressions, kc.ratio_proportion_rate

### `tm.fraction_decimal_operations`

- **`m.convert_common_denominator`** requires: kc.integer_arithmetic

### `tm.gas_problems`

- **`m.combined_gas_law`** requires: kc.algebraic_expressions, kc.mole_stoichiometry, kc.ratio_proportion_rate

### `tm.gravitation_problems`

- **`m.inverse_square`** requires: kc.algebraic_expressions, kc.newtons_laws

### `tm.handle_algebraic_expressions`

- **`m.collect_like_terms`** requires: kc.integer_arithmetic
- **`m.expand_simplify`** requires: kc.integer_arithmetic

### `tm.identify_parallel_line_angles`

- **`m.corresponding_alternate`** requires: kc.integer_arithmetic

### `tm.integrate_polynomial`

- **`m.reverse_power_rule`** requires: kc.algebraic_expressions, kc.function_concept

### `tm.interpret_motion_graph`

- **`m.displacement_from_st`** requires: kc.displacement_velocity, kc.gradient
- **`m.slope_of_vt`** requires: kc.algebraic_expressions, kc.displacement_velocity, kc.gradient

### `tm.logarithm_problems`

- **`m.apply_log_laws`** requires: kc.algebraic_expressions, kc.equations_in_indices
- **`m.convert_exp_log`** requires: kc.algebraic_expressions, kc.equations_in_indices

### `tm.make_subject`

- **`m.collect_factor_subject`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.inverse_operations`** requires: kc.algebraic_expressions, kc.linear_equations_one_var

### `tm.modern_physics_problems`

- **`m.photoelectric_equation`** requires: kc.algebraic_expressions, kc.equations_in_indices

### `tm.momentum_problems`

- **`m.conservation_collisions`** requires: kc.algebraic_expressions, kc.newtons_laws

### `tm.optics_problems`

- **`m.mirror_lens_equation`** requires: kc.algebraic_expressions, kc.ratio_proportion_rate
- **`m.reflection_refraction`** requires: kc.algebraic_expressions, kc.triangle_angle_properties

### `tm.organic_problems`

- **`m.hydrocarbon_naming`** requires: kc.chemical_bonding

### `tm.percentage_problems`

- **`m.percent_as_fraction`** requires: kc.fraction_decimal_operations, kc.integer_arithmetic

### `tm.ph_problems`

- **`m.ph_from_concentration`** requires: kc.acids_bases_salts, kc.algebraic_expressions, kc.logarithms

### `tm.practical_chemistry`

- **`m.qualitative_tests`** requires: kc.matter_classification
- **`m.titration_procedure`** requires: kc.acids_bases_salts, kc.measurement_units_dimensions

### `tm.practical_physics`

- **`m.instrument_tabulate`** requires: kc.integer_arithmetic, kc.measurement_units_dimensions
- **`m.plot_gradient`** requires: kc.gradient, kc.measurement_units_dimensions

### `tm.rate_equilibrium_problems`

- **`m.le_chatelier`** requires: kc.chemical_bonding
- **`m.rate_curves`** requires: kc.algebraic_expressions, kc.function_concept

### `tm.recall_special_values`

- **`m.from_special_triangles`** requires: kc.algebraic_expressions, kc.trig_ratios_acute

### `tm.redox_problems`

- **`m.electrolysis_quantitative`** requires: kc.electric_circuits, kc.mole_stoichiometry
- **`m.redox_identification`** requires: kc.chemical_bonding, kc.integer_arithmetic

### `tm.resolve_vectors`

- **`m.classify_quantities`** requires: kc.measurement_units_dimensions
- **`m.resolve_components`** requires: kc.algebraic_expressions, kc.trig_ratios_acute

### `tm.signed_number_arithmetic`

- **`m.sign_rules`** requires: kc.integer_arithmetic

### `tm.solve_constant_acceleration`

- **`m.graph_extract_motion`** requires: kc.algebraic_expressions, kc.motion_graph_interpretation
- **`m.suvat_equations`** requires: kc.algebraic_expressions, kc.displacement_velocity, kc.linear_equations_one_var

### `tm.solve_index_equation`

- **`m.logs`** requires: kc.algebraic_expressions
- **`m.match_bases`** requires: kc.algebraic_expressions, kc.linear_equations_one_var

### `tm.solve_linear_equations_one_var`

- **`m.expand_collect`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.isolate_variable`** requires: kc.algebraic_expressions, kc.integer_arithmetic

### `tm.solve_linear_inequality`

- **`m.balance_inverse`** requires: kc.algebraic_expressions, kc.linear_equations_one_var
- **`m.test_graph`** requires: kc.linear_equations_one_var

### `tm.solve_linear_quadratic_system`

- **`m.substitute_linear_into_quadratic`** requires: kc.change_of_subject, kc.quadratic_roots, kc.simultaneous_linear_equations

### `tm.solve_oblique_triangle`

- **`m.cosine_rule`** requires: kc.algebraic_expressions, kc.trig_ratios_acute
- **`m.sine_rule`** requires: kc.algebraic_expressions, kc.trig_ratios_acute

### `tm.solve_proportions`

- **`m.unitary_method`** requires: kc.fraction_decimal_operations, kc.integer_arithmetic

### `tm.solve_quadratic_by_factorisation`

- **`m.factorise_zero_product`** requires: kc.factorisation_quadratic_trinomial, kc.linear_equations_one_var
- **`m.special_product_zero_product`** requires: kc.factorisation_quadratic_trinomial, kc.linear_equations_one_var

### `tm.solve_simultaneous_linear_two_vars`

- **`m.solve_by_elimination`** requires: kc.algebraic_expressions, kc.linear_equations_one_var
- **`m.solve_by_substitution`** requires: kc.algebraic_expressions, kc.linear_equations_one_var

### `tm.stoichiometry_problems`

- **`m.empirical_formula`** requires: kc.algebraic_expressions, kc.chemical_bonding, kc.percentage_concept
- **`m.mole_ratio`** requires: kc.algebraic_expressions, kc.chemical_bonding, kc.ratio_proportion_rate

### `tm.thermal_problems`

- **`m.calorimetry`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.gas_law`** requires: kc.algebraic_expressions, kc.ratio_proportion_rate

### `tm.triangle_angle_problems`

- **`m.exterior_angle`** requires: kc.parallel_line_angles
- **`m.triangle_angle_sum`** requires: kc.integer_arithmetic, kc.parallel_line_angles

### `tm.trig_ratio_problems`

- **`m.label_sides_match_ratio`** requires: kc.algebraic_expressions, kc.integer_arithmetic

### `tm.wave_problems`

- **`m.wave_equation`** requires: kc.algebraic_expressions, kc.displacement_velocity

### `tm.work_energy_problems`

- **`m.power_as_rate`** requires: kc.algebraic_expressions, kc.newtons_laws, kc.rate_of_change
- **`m.work_from_force`** requires: kc.algebraic_expressions, kc.newtons_laws

## Misconceptions

- `mis.factorisation_sign_error` — Factorising with unchanged middle-term sign (PROPOSED)

## Open Review Items

- PROPOSED KCs: 0
- PROPOSED Claims: 2 (misconception catalog entry, item indicator, etc.)
- Owner sign-off: `indicates` domain (OWNER_SIGN_OFF_REQUIRED)
- Owner input: 12 vs 13 frozen-entity count discrepancy
- FREEZE document still absent

## Batches

See [`docs/batch_records/`](../batch_records/).

| Batch | KC |
|---|---|
| 001 | kc.quadratic_by_factorisation, kc.quadratic_roots, kc.simultaneous_linear_equations |
| 002 | kc.linear_equations_one_var |
| 003 | kc.algebraic_expressions, kc.integer_arithmetic |
| 004 | kc.factorisation_quadratic_trinomial |
| 005 | kc.completing_the_square, kc.quadratic_formula |
| 006 | kc.function_concept |
| 007 | kc.linear_inequalities_analytic |
| 008 | kc.equations_in_indices |
| 009 | kc.change_of_subject |
| 010 | kc.simultaneous_linear_quadratic |
| 011 | kc.fraction_decimal_operations, kc.percentage_concept |
| 012 | kc.parallel_line_angles, kc.triangle_angle_properties |
| 013 | kc.gradient |
| 014 | kc.trig_ratios_acute |
| 015 | kc.mean_ungrouped_data |
| 016 | kc.differentiation_algebraic |
| 017 | kc.rate_of_change |
| 018 | kc.maxima_minima |
| 019 | kc.integration_algebraic |
| 020 | kc.theoretical_probability |
| 021 | kc.cosine_rule, kc.sine_rule |
| 022 | kc.equation_of_line |
| 023 | kc.circle_angle_theorems |
| 024 | kc.parallel_perpendicular_lines |
| 025 | kc.ratio_proportion_rate |
| 026 | kc.direct_variation |
| 027 | kc.special_angle_values |
| 028 | kc.counting_principle |
| 029 | kc.distance_formula |
| 030 | kc.displacement_velocity, kc.mass_and_weight, kc.measurement_errors_precision, kc.measurement_units_dimensions, kc.motion_equations_constant_acceleration, kc.motion_graph_interpretation, kc.newtons_laws, kc.practical_measurement |
| 031 | kc.scalar_vector_quantities |
| 032 | kc.work_energy_power |
| 033 | kc.linear_momentum |
| 034 | kc.gravitation |
| 035 | kc.pressure_fluids |
| 036 | kc.heat_temperature |
| 037 | kc.wave_phenomena |
| 038 | kc.geometrical_optics |
| 039 | kc.electric_circuits |
| 040 | kc.electromagnetism |
| 041 | kc.atomic_nuclear_physics |
| 043 | kc.matter_classification |
| 044 | kc.atomic_structure_periodicity |
| 045 | kc.chemical_bonding |
| 046 | kc.mole_stoichiometry |
| 047 | kc.acids_bases_salts |
| 048 | kc.redox_electrochemistry |
| 049a | kc.chemical_energetics |
| 049b | kc.rates_equilibrium |
| 050 | kc.gas_behaviour |
| 051 | kc.organic_foundations |
| 052 | kc.practical_chemistry |
| 055 | kc.logarithms |
| 056 | kc.ph_scale |
