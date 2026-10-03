# Mathematics CDG — Human Inspection Index

Generated deterministically from `examples/math_cdg_v2.json`
by `tools/generate_math_cdg_docs.py`. Do not edit by hand.

## Current Graph Statistics

- Knowledge Components: 14
- TaskModels: 14
- Methods: 26
- Items: 11
- Misconceptions: 1
- Claims: 105
- Evidence records: 103
- Sources: 14
- Activities: 30
- Agents: 2
- Exported nodes: 66
- Exported edges: 105
- Accepted Claims: 103; PROPOSED Claims: 2

## KC Index

| ID | Name | Domain | Status | Owning TMs |
|---|---|---|---|---|
| `kc.algebraic_expressions` | Algebraic expressions: terms, coefficients, like terms, substitution | Algebra | ACCEPTED | tm.handle_algebraic_expressions |
| `kc.change_of_subject` | Change of subject of a formula/relation | Algebra | ACCEPTED | tm.make_subject |
| `kc.completing_the_square` | Completing the square | Algebra | ACCEPTED | tm.complete_square |
| `kc.equations_in_indices` | Equations involving indices | Number & Numeration | ACCEPTED | tm.solve_index_equation |
| `kc.factorisation_quadratic_trinomial` | Factorisation of quadratic trinomials | Algebra | ACCEPTED | tm.factorise_quadratic_trinomial |
| `kc.function_concept` | Function concept and notation | Functions | ACCEPTED | tm.evaluate_and_represent_function |
| `kc.integer_arithmetic` | Signed-number (integer) arithmetic | Number & Numeration | ACCEPTED | tm.signed_number_arithmetic |
| `kc.linear_equations_one_var` | Linear equations in one variable | Algebra | ACCEPTED | tm.solve_linear_equations_one_var |
| `kc.linear_inequalities_analytic` | Linear inequalities: analytical solution | Algebra | ACCEPTED | tm.solve_linear_inequality |
| `kc.quadratic_by_factorisation` | Solving quadratic equations by factorisation | Algebra | ACCEPTED | tm.solve_quadratic_by_factorisation |
| `kc.quadratic_formula` | Quadratic formula | Algebra | ACCEPTED | tm.apply_quadratic_formula |
| `kc.quadratic_roots` | Roots of quadratic equations (any method) | Algebra | ACCEPTED | tm.find_quadratic_roots |
| `kc.simultaneous_linear_equations` | Simultaneous linear equations in two variables | Algebra | ACCEPTED | tm.solve_simultaneous_linear_two_vars |
| `kc.simultaneous_linear_quadratic` | Simultaneous equations: one linear, one quadratic | Algebra | ACCEPTED | tm.solve_linear_quadratic_system |

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
| `kc.linear_equations_one_var` | → | `kc.linear_inequalities_analytic` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.equations_in_indices` | EXECUTE | SPECIFIC_METHOD | DERIVED |
| `kc.linear_equations_one_var` | → | `kc.change_of_subject` | EXECUTE | SPECIFIC_TASK_MODEL | DERIVED |

## TaskModel Index

### `tm.apply_quadratic_formula` — Apply the quadratic formula

- Targets: kc.quadratic_formula
- Methods: m.substitute_formula
- Status: ACCEPTED

### `tm.complete_square` — Complete the square

- Targets: kc.completing_the_square
- Methods: m.cts_standard_form, m.cts_then_roots
- Status: ACCEPTED

### `tm.evaluate_and_represent_function` — Evaluate and represent functions

- Targets: kc.function_concept
- Methods: m.evaluate_substitution, m.table_of_values
- Status: ACCEPTED

### `tm.factorise_quadratic_trinomial` — Factorise quadratic trinomials

- Targets: kc.factorisation_quadratic_trinomial
- Methods: m.factorise_by_grouping, m.factorise_unit_leading
- Status: ACCEPTED

### `tm.find_quadratic_roots` — Find the roots of a quadratic equation

- Targets: kc.quadratic_roots
- Methods: m.roots_via_completing_square, m.roots_via_factorisation, m.roots_via_formula
- Status: ACCEPTED

### `tm.handle_algebraic_expressions` — Simplify and evaluate algebraic expressions

- Targets: kc.algebraic_expressions
- Methods: m.collect_like_terms, m.expand_simplify
- Status: ACCEPTED

### `tm.make_subject` — Make a specified variable the subject

- Targets: kc.change_of_subject
- Methods: m.collect_factor_subject, m.inverse_operations
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

### `tm.solve_quadratic_by_factorisation` — Solve a quadratic equation by factorisation

- Targets: kc.quadratic_by_factorisation
- Methods: m.factorise_zero_product, m.special_product_zero_product
- Status: ACCEPTED

### `tm.solve_simultaneous_linear_two_vars` — Solve simultaneous linear equations in two variables

- Targets: kc.simultaneous_linear_equations
- Methods: m.solve_by_elimination, m.solve_by_substitution
- Status: ACCEPTED

## Method Index (AND within method, OR across methods)

### `tm.apply_quadratic_formula`

- **`m.substitute_formula`** requires: kc.algebraic_expressions, kc.integer_arithmetic

### `tm.complete_square`

- **`m.cts_standard_form`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.cts_then_roots`** requires: kc.algebraic_expressions, kc.integer_arithmetic

### `tm.evaluate_and_represent_function`

- **`m.evaluate_substitution`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.table_of_values`** requires: kc.algebraic_expressions

### `tm.factorise_quadratic_trinomial`

- **`m.factorise_by_grouping`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.factorise_unit_leading`** requires: kc.algebraic_expressions, kc.integer_arithmetic

### `tm.find_quadratic_roots`

- **`m.roots_via_completing_square`** requires: kc.completing_the_square
- **`m.roots_via_factorisation`** requires: kc.quadratic_by_factorisation
- **`m.roots_via_formula`** requires: kc.quadratic_formula

### `tm.handle_algebraic_expressions`

- **`m.collect_like_terms`** requires: kc.integer_arithmetic
- **`m.expand_simplify`** requires: kc.integer_arithmetic

### `tm.make_subject`

- **`m.collect_factor_subject`** requires: kc.algebraic_expressions, kc.integer_arithmetic
- **`m.inverse_operations`** requires: kc.algebraic_expressions, kc.linear_equations_one_var

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

### `tm.solve_quadratic_by_factorisation`

- **`m.factorise_zero_product`** requires: kc.factorisation_quadratic_trinomial, kc.linear_equations_one_var
- **`m.special_product_zero_product`** requires: kc.factorisation_quadratic_trinomial, kc.linear_equations_one_var

### `tm.solve_simultaneous_linear_two_vars`

- **`m.solve_by_elimination`** requires: kc.algebraic_expressions, kc.linear_equations_one_var
- **`m.solve_by_substitution`** requires: kc.algebraic_expressions, kc.linear_equations_one_var

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
