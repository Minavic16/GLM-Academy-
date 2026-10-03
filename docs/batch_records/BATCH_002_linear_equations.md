# BATCH 002 — Linear equations in one variable

- Batch ID: 002 (after math_slice_v1)
- Scope: KC kc.linear_equations_one_var plus its owning TaskModel,
  two Methods, one Item, prerequisite Claims, Evidence, provenance.
- Entities added: 1 KC (kc.integer_arithmetic, PROPOSED), 1 TaskModel
  (tm.solve_linear_equations_one_var), 2 Methods (m.isolate_variable,
  m.expand_collect), 1 Item (it.mcq.linear_one_var). kc.linear_equations_one_var
  graduated PROPOSED → ACCEPTED.
- Claims added: 9 (1 targets, 2 hasMethod, 4 requires, 2 DERIVED prerequisites).
- Evidence added/reused: 9 items, all inherited_from_legacy (E0124, E0084, E0089).
- Sources used: SRC.WAEC.WASSCE.MATH.SYL, SRC.OSX.IA2E.6.5, SRC.OSX.IA2E.5.4.
- Review state: HUMAN review activity act.batch2.review; all new substantive
  claims ACCEPTED with EXPERT/EMPIRICAL bases; no AGENT_INFERENCE-only acceptance.
- Validation: `run_store_validation` → []; pytest → 60 passed.
- Serialization: examples/math_cdg_v2.json written; round-trip preserves
  entity/claim/evidence counts.
- export_view: 26 nodes, 40 edges; requires/targets edges intact.
- Unresolved issues: kc.algebraic_expressions and kc.integer_arithmetic remain
  PROPOSED until their owning TaskModels are modeled in a later batch.
- Next batch: quadratics/factorisation ownership (kc.factorisation_quadratic_trinomial,
  kc.completing_the_square, kc.quadratic_formula TMs), then functions.
