# GLM CDG v0.2 — Vertical Slice Report (Phase 2)

Date: 2026-10-03. Code location: `/root/glm-academy`.

## 1. Freeze reconciliation

- Freeze document found: **No.** `GLM_CDG_v0.2_FREEZE.md` is still absent;
  no document was invented. See
  `docs/architecture/FREEZE_RECONCILIATION.md`.
- Discrepancies: none requiring an implementation change. The only edit was
  additive review metadata on entities (see below).
- Decisions: Sanity Check contract remains the contract source; the three
  pending owner items are preserved, not resolved:
  - `indicates` domain kept as implemented (Item → Misconception | KC,
    required `response_pattern`; `polarity` required for KC);
    marked OWNER_SIGN_OFF_REQUIRED.
  - 12 vs 13 entity count remains documented as unresolved owner input.
  - Legacy disposition remains metadata-only; no legacy records were
    migrated or imported.
- Unresolved owner decisions: the three above.

## 2. Contract changes

One additive, optional change:

- `cdg/entities.py`: `EntityBase` gained `reviewed_by_activity` and
  `review_rationale` (both optional; existing constructors/validations
  unaffected). Motivation: the contract required human-review signals on
  entity records, not only on Claims.
- `docs/architecture/CDG_CONTRACT_DOCUMENTATION.md`: `indicates` marked
  OWNER_SIGN_OFF_REQUIRED.
- New test `test_indicates_domain_is_not_broadened` added.

No other contract changes required.

## 3. Mathematics slice (`examples/math_slice_v1.py`, `examples/math_slice_v1.json`)

Coherent progression: algebraic expressions / linear equations →
factorisation → solving quadratics by factorisation → quadratic roots
(also via formula and completing the square), plus simultaneous linear
equations in two variables.

- KCs: **8** (3 ACCEPTED: quadratic_by_factorisation, quadratic_roots,
  simultaneous_linear_equations; 5 PROPOSED — their owning TaskModels are
  out-of-slice and not yet modeled)
- TaskModels: **3**
- Methods: **7** (AND within method, OR across methods preserved per TM)
- Items: **2**
- Misconceptions: **1** (PROPOSED)
- Claims: **31** total — 29 ACCEPTED, 2 PROPOSED (relatedMisconception,
  indicates; both pending human review with rationale recorded)
- Evidence records: **29** (all `inherited_from_legacy=True`; legacy ids
  like E0119/E0122/E0128/E0134/E0137/E0207 preserved)
- Sources: **6** (NERDC SSS1/SSS2, WAEC syllabus, OpenStax Intermediate
  Algebra 2e sections — reused from the legacy corpus, unedited)
- Agents: **2** (1 HUMAN reviewer, 1 AI_AGENT research runner)
- Activities: **3** (EXTRACTION, INTERPRETATION by AI_AGENT; REVIEW by HUMAN)

Every ACCEPTED Claim has an admissible acceptance basis
(DEPENDENCY/ASSESSMENT_DESIGN: EXPERT, with EMPIRICAL carried from legacy
review stance), a REVIEW activity reference, `review_rationale`, and ≥1
EvidenceItem. `AGENT_INFERENCE` alone was never used to accept a claim.

## 4. Validation

- **pytest**: `python3 -m pytest -q` → **52 passed** (42 pre-existing +
  10 new slice/validation/regression tests).
- **Store validation**: `run_store_validation(build_slice())` →
  **[] (no errors)**.
- **JSON round-trip**: `dumps_store` →
  `examples/math_slice_v1.json` (52,177 bytes); prerequisite
  `purpose`/`scope`/`origin` metadata preserved on all 8 prerequisite
  Claims.
- **export_view**: 21 nodes, 31 edges, predicates
  `{targets, hasMethod, requires, prerequisite, relatedMisconception,
  indicates}`; requires-edge count 11, confirming Method AND structure was
  not flattened. Relation direction preserved (e.g.
  `tm.find_quadratic_roots --targets--> kc.quadratic_roots`,
  `m.roots_via_formula --requires--> kc.quadratic_formula`).

## 5. Human-review status

- Supporting KCs intentionally **stay PROPOSED** because validation requires
  a targeting TaskModel for exit from PROPOSED, and their owning
  TaskModels are not in this slice — this is policy fidelity, not evasion.
- The two candidate claims (misconception catalog entry, item-response
  indicator) remain PROPOSED rather than forced through the lifecycle.
- Every accepted item gained its claim through
  PROPOSED → UNDER_REVIEW → ACCEPTED (state machine unbypassed), with a
  HUMAN review Activity, an admissible basis, and evidence or rationale.

## 6. Remaining blockers

- FREEZE document still absent (owner notified twice); reconciliation is
  pending, future curriculum batch approval is blocked on it.
- `indicates` owner sign-off still open.

## 7. Next logical step

Obtain owner sign-off (FREEZE doc reconciliation + `indicates` decision),
then review-accept the 5 PROPOSED supporting KCs by giving each its owning
TaskModel in a second small slice, repeating the same validation/
serialization path.

---

## Addendum — Phase 3 execution 1

- Scope documented: `docs/architecture/MATHEMATICS_SCOPE.md`.
- Legacy corpus inventoried; batch-1 legacy evidence reused as MAPPED
  evidence only; migration ledger at `docs/architecture/MIGRATION_LEDGER.md`.
- Next batch after slice v1 executed: **batch 002 (linear equations in
  one variable)**, `examples/batch2_linear_equations.py`;
  combined graph serialized at `examples/math_cdg_v2.json` (26 nodes /
  40 edges via export_view). Tests: **60 passed**.
  See `docs/batch_records/BATCH_002_linear_equations.md`.
- Batch 2 graduated `kc.linear_equations_one_var` from PROPOSED →
  ACCEPTED via its owning TaskModel (2 methods, AND/OR preserved).
- No DB, no learner model, no probabilities/weights, no equivalence
  relations, no auto-inference added. Pipeline demonstrated:
  evidence → agent proposal → human-reviewed acceptance → validation →
  JSON → export_view. Ready for a subsequent batch run.

---

## Addendum — Phase 4 construction run

Batches 003–006 completed (5 batches total including 002):

- batch 003 (algebra foundations): graduated kc.algebraic_expressions +
  kc.integer_arithmetic
- batch 004 (factorisation): graduated kc.factorisation_quadratic_trinomial
- batch 005 (quadratic tools): graduated kc.quadratic_formula +
  kc.completing_the_square
- batch 006 (function concept): new KC kc.function_concept → ACCEPTED

Current graph (examples/math_cdg_v2.json, canonical):
10 KCs (all ACCEPTED), 10 TaskModels, 19 Methods, 8 Items≈4,
PROPOSED misconception/indicates retained, 69→76 Claims, 74 Evidence
items, exported nodes 47 / edges 76. Store validation: [].
pytest: **66 passed**. One namespacing collision between batch-4/5
claim IDs was found by validation and fixed (tests guard it).

Batch records: docs/batch_records/BATCH_003…BATCH_006.

---

## Addendum — Phase 5 run

4 additional batches built (007–010): linear inequalities (analytical),
equations in indices, change of subject, simultaneous linear-quadratic.
All validated identically to earlier batches.

Canonical artifact `examples/math_cdg_v2.json` now exports
**66 nodes / 105 edges**, 14 KCs (all ACCEPTED), 14 TaskModels, 26 Methods,
105 Claims (103 ACCEPTED, 2 PROPOSED), 103 Evidence items (legacy-inherited),
14 Sources. Store validation: []. pytest: **69 passed**.

GitHub inspection layer added:
- `docs/MATHEMATICS_CDG.md` (human-readable index with KC/TM/Method indexes,
  stats, open review items; deterministic, generated)
- `docs/architecture/MATHEMATICS_COVERAGE.md` (domain coverage ledger)
- `tools/generate_math_cdg_docs.py` (deterministic generator; output verified
  byte-identical across runs)
- `README.md` now links README → CDG → Coverage → Architecture → Batch records
  → Canonical JSON

Documentation QA: every ID token in the generated index resolves to a real
entity in the canonical JSON; batch records all present.
