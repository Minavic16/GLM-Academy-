# Mathematics CDG — Human Inspection Index

Generated deterministically from `examples/math_cdg_v2.json`
by `tools/generate_math_cdg_docs.py`. Do not edit by hand.

## Current Graph Statistics

- Knowledge Components: 36
- TaskModels: 35
- Methods: 49
- Items: 30
- Misconceptions: 1
- Claims: 221
- Evidence records: 207
- Sources: 28
- Activities: 87
- Agents: 2
- Exported nodes: 151
- Exported edges: 221
- Accepted Claims: 219; PROPOSED Claims: 2

## KC Index

| ID | Name | Domain | Status | Owning TMs |
|---|---|---|---|---|
| `kc.algebraic_expressions` | Algebraic expressions: terms, coefficients, like terms, substitution | Algebra | ACCEPTED | tm.handle_algebraic_expressions |
| `kc.change_of_subject` | Change of subject of a formula/relation | Algebra | ACCEPTED | tm.make_subject |
| `kc.circle_angle_theorems` | Basic circle angle theorems | Geometry | ACCEPTED | tm.circle_angle_problems |
| `kc.completing_the_square` | Completing the square | Algebra | ACCEPTED | tm.complete_square |
| `kc.cosine_rule` | Cosine rule for oblique triangles | Trigonometry | ACCEPTED | tm.solve_oblique_triangle |
| `kc.counting_principle` | Fundamental (multiplication) counting principle | Statistics & Probability | ACCEPTED | tm.count_outcomes |
| `kc.differentiation_algebraic` | Differentiation of explicit algebraic functions | Calculus | ACCEPTED | tm.differentiate_explicit |
| `kc.direct_variation` | Direct variation | Algebra | ACCEPTED | tm.direct_variation_problems |
| `kc.distance_formula` | Distance between two points in the plane | Coordinate Geometry | ACCEPTED | tm.compute_distance |
| `kc.equation_of_line` | Equation of a straight line (all forms) | Coordinate Geometry | ACCEPTED | tm.find_line_equation |
| `kc.equations_in_indices` | Equations involving indices | Number & Numeration | ACCEPTED | tm.solve_index_equation |
| `kc.factorisation_quadratic_trinomial` | Factorisation of quadratic trinomials | Algebra | ACCEPTED | tm.factorise_quadratic_trinomial |
| `kc.fraction_decimal_operations` | Operations on fractions and decimals | Number & Numeration | ACCEPTED | tm.fraction_decimal_operations |
| `kc.function_concept` | Function concept and notation | Functions | ACCEPTED | tm.evaluate_and_represent_function |
| `kc.gradient` | Gradient of a line segment | Coordinate Geometry | ACCEPTED | tm.compute_gradient |
| `kc.integer_arithmetic` | Signed-number (integer) arithmetic | Number & Numeration | ACCEPTED | tm.signed_number_arithmetic |
| `kc.integration_algebraic` | Elementary integration of algebraic functions | Calculus | ACCEPTED | tm.integrate_polynomial |
| `kc.linear_equations_one_var` | Linear equations in one variable | Algebra | ACCEPTED | tm.solve_linear_equations_one_var |
| `kc.linear_inequalities_analytic` | Linear inequalities: analytical solution | Algebra | ACCEPTED | tm.solve_linear_inequality |
| `kc.maxima_minima` | Maxima and minima of a function | Calculus | ACCEPTED | tm.find_maxima_minima |
| `kc.mean_ungrouped_data` | Mean of ungrouped data | Statistics & Probability | ACCEPTED | tm.compute_mean |
| `kc.parallel_line_angles` | Angles formed by parallel lines and a transversal | Geometry | ACCEPTED | tm.identify_parallel_line_angles |
| `kc.parallel_perpendicular_lines` | Conditions for parallel and perpendicular lines | Coordinate Geometry | ACCEPTED | tm.classify_line_relationships |
| `kc.percentage_concept` | Percentages | Number & Numeration | ACCEPTED | tm.percentage_problems |
| `kc.quadratic_by_factorisation` | Solving quadratic equations by factorisation | Algebra | ACCEPTED | tm.solve_quadratic_by_factorisation |
| `kc.quadratic_formula` | Quadratic formula | Algebra | ACCEPTED | tm.apply_quadratic_formula |
| `kc.quadratic_roots` | Roots of quadratic equations (any method) | Algebra | ACCEPTED | tm.find_quadratic_roots |
| `kc.rate_of_change` | Rate of change of a function | Calculus | ACCEPTED | tm.compute_rate_of_change |
| `kc.ratio_proportion_rate` | Ratio, proportion and rate | Number & Numeration | ACCEPTED | tm.solve_proportions |
| `kc.simultaneous_linear_equations` | Simultaneous linear equations in two variables | Algebra | ACCEPTED | tm.solve_simultaneous_linear_two_vars |
| `kc.simultaneous_linear_quadratic` | Simultaneous equations: one linear, one quadratic | Algebra | ACCEPTED | tm.solve_linear_quadratic_system |
| `kc.sine_rule` | Sine rule for oblique triangles | Trigonometry | ACCEPTED | tm.solve_oblique_triangle |
| `kc.special_angle_values` | Exact trigonometric values of special angles | Trigonometry | ACCEPTED | tm.recall_special_values |
| `kc.theoretical_probability` | Theoretical probability of an event | Statistics & Probability | ACCEPTED | tm.compute_probability |
| `kc.triangle_angle_properties` | Triangle angle properties | Geometry | ACCEPTED | tm.triangle_angle_problems |
| `kc.trig_ratios_acute` | Trigonometric ratios of acute angles | Trigonometry | ACCEPTED | tm.trig_ratio_problems |

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
| `kc.linear_equations_one_var` | → | `kc.quadratic_by_factorisation` | EXECUTE | ALL_RELEVANT_METHODS | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.simultaneous_linear_equations` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
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
| `kc.linear_equations_one_var` | → | `kc.linear_inequalities_analytic` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.equations_in_indices` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.change_of_subject` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |

## TaskModel Index

### `tm.apply_quadratic_formula` — Apply the quadratic formula

- Targets: kc.quadratic_formula
- Methods: m.substitute_formula
- Status: ACCEPTED

### `tm.circle_angle_problems` — Solve circle angle problems using theorems

- Targets: kc.circle_angle_theorems
- Methods: m.centre_vs_circumference
- Status: ACCEPTED

### `tm.classify_line_relationships` — Classify whether two lines are parallel, perpendicular or neither

- Targets: kc.parallel_perpendicular_lines
- Methods: m.compare_gradients
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

### `tm.fraction_decimal_operations` — Perform operations on fractions/decimals

- Targets: kc.fraction_decimal_operations
- Methods: m.convert_common_denominator
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

### `tm.make_subject` — Make a specified variable the subject

- Targets: kc.change_of_subject
- Methods: m.collect_factor_subject, m.inverse_operations
- Status: ACCEPTED

### `tm.percentage_problems` — Solve percentage problems

- Targets: kc.percentage_concept
- Methods: m.percent_as_fraction
- Status: ACCEPTED

### `tm.recall_special_values` — State exact trig values at special angles

- Targets: kc.special_angle_values
- Methods: m.from_special_triangles
- Status: ACCEPTED

### `tm.signed_number_arithmetic` — Perform signed-number arithmetic

- Targets: kc.integer_arithmetic
- Methods: m.sign_rules
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

### `tm.triangle_angle_problems` — Solve triangle angle problems

- Targets: kc.triangle_angle_properties
- Methods: m.exterior_angle, m.triangle_angle_sum
- Status: ACCEPTED

### `tm.trig_ratio_problems` — Solve right-triangle problems using trigonometric ratios

- Targets: kc.trig_ratios_acute
- Methods: m.label_sides_match_ratio
- Status: ACCEPTED

## Method Index (AND within method, OR across methods)

### `tm.apply_quadratic_formula`

- **`m.substitute_formula`** requires: kc.algebraic_expressions, kc.integer_arithmetic

### `tm.circle_angle_problems`

- **`m.centre_vs_circumference`** requires: kc.integer_arithmetic, kc.triangle_angle_properties

### `tm.classify_line_relationships`

- **`m.compare_gradients`** requires: kc.gradient, kc.integer_arithmetic

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

### `tm.count_outcomes`

- **`m.multiply_choices`** requires: kc.integer_arithmetic, kc.ratio_proportion_rate

### `tm.differentiate_explicit`

- **`m.power_rule`** requires: kc.algebraic_expressions, kc.function_concept

### `tm.direct_variation_problems`

- **`m.find_constant`** requires: kc.integer_arithmetic, kc.linear_equations_one_var

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

### `tm.fraction_decimal_operations`

- **`m.convert_common_denominator`** requires: kc.integer_arithmetic

### `tm.handle_algebraic_expressions`

- **`m.collect_like_terms`** requires: kc.integer_arithmetic
- **`m.expand_simplify`** requires: kc.integer_arithmetic

### `tm.identify_parallel_line_angles`

- **`m.corresponding_alternate`** requires: kc.integer_arithmetic

### `tm.integrate_polynomial`

- **`m.reverse_power_rule`** requires: kc.algebraic_expressions, kc.function_concept

### `tm.make_subject`

- **`m.collect_factor_subject`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.inverse_operations`** requires: kc.algebraic_expressions, kc.linear_equations_one_var

### `tm.percentage_problems`

- **`m.percent_as_fraction`** requires: kc.fraction_decimal_operations, kc.integer_arithmetic

### `tm.recall_special_values`

- **`m.from_special_triangles`** requires: kc.algebraic_expressions, kc.trig_ratios_acute

### `tm.signed_number_arithmetic`

- **`m.sign_rules`** requires: kc.integer_arithmetic

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

### `tm.triangle_angle_problems`

- **`m.exterior_angle`** requires: kc.parallel_line_angles
- **`m.triangle_angle_sum`** requires: kc.integer_arithmetic, kc.parallel_line_angles

### `tm.trig_ratio_problems`

- **`m.label_sides_match_ratio`** requires: kc.algebraic_expressions, kc.integer_arithmetic

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
