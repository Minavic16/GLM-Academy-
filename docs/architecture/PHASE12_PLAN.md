# Phase 12 Execution Plan

Baseline (2026-10-08, before Phase 12 verification edits):
- Branch `main`, clean tree at `1921ac0`; pytest **90 passed**; store validation `[]`.
- Canonical `examples/math_cdg_v2.json`: 174 entities / 44 KCs (8 Physics) / 260 Claims.
- Prior Phase 12 work present: `examples/physics_slice.py`, 4 Math→Physics edges,
  subject-aware visualization, architecture reviews.

Change budget for this verification pass (minimal, justified):
1. `examples/physics_slice.py`: set `subject="Physics"` on Physics TaskModels
   and Methods (new entities lacked unambiguous subject; Mathematics baseline
   untouched). Justification: prompt §9 + existing subject-identity contract.
2. `docs/research/PHYSICS_SOURCE_RESEARCH.md`: create (required by §3.3, was missing).
3. `docs/architecture/SUBJECT_EXPANSION_PLAN.md`: expand to required table +
   per-phase exit criteria (was a minimal stub).
4. `docs/architecture/SUBJECT_RESEARCH_READINESS.md`: convert to required
   status table (was prose).
5. Regenerate canonical JSON + docs + visualizations deterministically.
6. Add one regression test (Physics TM/Method subject identity). Run full suite.

Explicit non-goals: no new KCs beyond the slice, no Chemistry/Biology/English
entities, no relation-type changes, no legacy migration, no learner model.
