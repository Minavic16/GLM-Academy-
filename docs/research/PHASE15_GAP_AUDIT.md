# Phase 15 Gap Audit — Chemistry

Baseline: branch `main` @ `b20c53b` ("Phase 14: physics completion wave"),
working tree clean, **125 tests passing**, store validation `[]`
(builder `build_graph_v38`). Canonical counts: 300 entities / 509 claims /
267 evidence / 80 sources / 189 activities; Mathematics 39 KCs,
Physics 25 KCs, Chemistry 12 KCs, Biology 0.

Purpose of this audit: identify every documented Chemistry
implementation gap before any curriculum change. Nothing here authorizes
implementation; dispositions become binding only when Phase 15B
(implementation) executes them.

## Documented Chemistry gaps (source of each item)

| # | Gap (as documented) | Where documented | Current coverage |
|---|---|---|---|
| 1 | Organic reactions NOT_IMPLEMENTED (reactions of alkanes/alkenes, carbonyl reactions, amines/amides) | CHEMISTRY_COVERAGE_MATRIX.md row 10; ROADMAP "Next task"; PHASE13_PLAN | PARTIAL — `kc.organic_foundations` is naming/classification only |
| 2 | Buffers proper NOT_COVERED | CHEMISTRY_COVERAGE_MATRIX.md row 11; CI-09 | NOT_COVERED |
| 3 | Polymers NOT_COVERED (deferred) | CHEMISTRY_COVERAGE_MATRIX.md row 12; ROADMAP | NOT_COVERED (deferred) |
| 4 | Industrial chemistry NOT_COVERED (deferred) | CHEMISTRY_COVERAGE_MATRIX.md row 13; ROADMAP | NOT_COVERED (deferred) |
| 5 | Electrolytic cells detail / transition metals NOT_COVERED (deferred) | CHEMISTRY_COVERAGE_MATRIX.md row 14; CI-09 | NOT_COVERED (deferred) |
| 6 | Practical chemistry WAEC detail PARTIAL (official verification) | CHEMISTRY_COVERAGE_MATRIX.md row 9; CI-05 | PARTIAL — implementation adequate, verification outstanding |
| 7 | Cross-check of all existing 12 Chemistry KCs | CLOSURE_AUDIT_CHEMISTRY.md (Phase 13.5) | All COVERED; no implementation gap found |

No other implementation gaps were found after checking: every existing
Chemistry KC has a targeting TaskModel, every TaskModel has Methods and
Items, every ACCEPTED Chemistry claim has human-reviewed evidence, and
every cross-subject dependency already present is intact (including the
Math→Chemistry `cl.pre56.log_ph` edge).

## Gap-by-gap findings

### Gap 1 — Organic reactions (primary target) — IMPLEMENT

Existing records: `kc.organic_foundations` (KC b051) with
`tm.organic_problems` (method `m.hydrocarbon_naming`); its Method owns
only hydrocarbon naming. No KC, Method, Item, or ACCEPTED claim covers
reaction mechanisms; every claim about organic content is either absent
or references naming only.

Verified OpenStax coverage: Chemistry 2e chapter 20 (all four sections
verified HTTP 200 during Phase 15, content quoted below):
- 20-1 Hydrocarbons — "reactions characteristic of saturated and
  unsaturated hydrocarbons", structural/geometric isomers; alkanes burn
  (exothermic, fuels); alkenes/alkynes defined;
- 20-2 Alcohols and Ethers — alcohols (structure, polyols, naming), ethers
  (structure, naming);
- 20-3 Aldehydes, Ketones, Carboxylic Acids and Esters — carbonyl group,
  aldehydes/ketones, oxidation and reduction, esterification;
- 20-4 Amines and Amides — amines (structure, nomenclature), amides
  (amidisation/condensation, peptide bonds).

Proposed change: nine bounded KCs (batches 065):
`kc.reactions_of_alkanes`, `kc.reactions_of_alkenes`, `kc.isomerism`,
`kc.alcohols`, `kc.ethers`, `kc.aldeydes_ketones`,
`kc.carboxylic_acids`, `kc.amines`, `kc.amides`, each with a targeting
TM, Methods, Items, and ACCEPTED claims; prerequisites are all
Chemistry-internal (no new cross-subject dependency claims).

Disposition: IMPLEMENT in Phase 15B.

### Gap 2 — Buffers proper — BLOCKED (Phase 15 scope constraint)

Existing records: `kc.acids_bases_salts` and `tm.acid_base_problems`
cover Brønsted–Lowry acids/bases, pH, and titration; pH calculations rely
on the existing cross-subject edge `cl.pre56.log_ph`
(`kc.logarithms` Mathematics → `kc.ph_scale`), scoped to method
`m.ph_from_concentration` in `tm.ph_problems`.

Verified OpenStax coverage: Chemistry 2e 14-6 "Buffers" exists
(verified HTTP 200).

Why it cannot be implemented in Phase 15: buffer pH calculations
(Henderson–Hasselbalch-style reasoning) require the logarithms KC that
lives in the Mathematics subject. Adding the required prerequisite edge
would create a new cross-subject dependency claim whose subject is a
Mathematics KC. Phase 15 explicitly forbids modifying Mathematics or
Physics records ("Do not modify Mathematics or Physics except to fix a
demonstrated regression"). No existing edge can be reused: the existing
`cl.pre56.log_ph` edge is scoped (SPECIFIC_METHOD) to
`m.ph_from_concentration` in `tm.ph_problems`, not to any new buffer
TaskModel.

Disposition: BLOCKED for Phase 15; documented with this constraint.
Requires either Phase 15 owner authorization to add the cross-subject
edge, or a separate cross-subject phase. Not implemented.

### Gaps 3–5 — Polymers / industrial chemistry / transition metals — DEFERRED (unchanged)

Verified OpenStax coverage: Chemistry 2e contains no chapters on polymers
or industrial chemistry (the book ends at chapter 21, nuclear
chemistry); chapter 19 covers transition metals.

These rows were explicitly DEFERRED by owner-documented scope decisions
(COVERAGE_MATRIX "deferred"; ROADMAP "Verified partial/deferred"). Phase
15's objective is explicitly the organic-reactions gap; reopening these
families would expand declared scope without owner authorization.
OpenStax chapter 19 evidence exists, but the deferral was deliberate
(owner-recorded) and Phase 15 must not reopen resolved or deferred
Chemistry scope without owner direction.

Disposition: DEFERRED; no change in Phase 15. Revisit only with owner
authorization.

### Gap 6 — Practical WAEC detail (official verification) — UNCHANGED

Implementation: adequate (measurement, apparatus, procedure, observation,
interpretation covered by `tm.practical_chemistry` and its Methods).
Official board verification remains outstanding (CI-05, owner decision).
Not an implementation gap; official verification is out of scope for
Phase 15 and remains blocked by unavailable official sources.

Disposition: unchanged.

## Implementation sequence (dependency-aware)

| Batch | Content | New KCs |
|---|---|---|
| 065 | Organic reactions (Chemistry 2e ch. 20) — the only gap Phase 15 is authorized to close | 9 KCs |

No new cross-subject dependency claims are created (Phase 15 restriction).
All prerequisites of the new batches are Chemistry-internal.

## Validation performed before this audit was acted upon

- `python3 -m pytest -q` — 125 passed (baseline).
- Store validation `run_store_validation(build_graph_v38())` — `[]`.
- Existing Chemistry closure audit (Phase 13.5): all 12 KCs, all
  cross-subject edges intact.
