# Subject Expansion Plan (Phase 11 research output)

Phase boundary: this is a plan. Nothing below is implemented yet.

## Phase 12 — Physics CDG bootstrap
1. Retrieve and archive the actual source PDFs (JAMB iBASS Physics, WAEC
   May/June Physics, NERDC SSS Physics).
2. Register their bytes as read-only LEGACY_DATASET or new Sources in the
   canonical store (additive — preserve existing Mathematics records).
3. Bootstrap one coherent Physics slice of ~V1 scale mirroring the
   Mathematics slice methodology:
   - Measurement/units
   - Kinematics (displacement-velocity-time and s-t/v-t graphs)
   - Newton's laws
   - one or two downstream slices (work/energy; circular motion if
     evidence/dependency clear).
4. Establish explicit cross-subject prerequisites per
   `CROSS_SUBJECT_DEPENDENCY_POLICY.md` — only where a Physics TaskModel's
   Method requires a Mathematics KC.
5. One human-review pass, full validation chain, deterministic generation.

## Phase 13 — Chemistry CDG bootstrap
Same methodology for one slice:
   - Matter & atomic structure basics
   - Moles/stoichiometry
   - Cross-subject edges from Mathematics ratio/proportion where evidence
     supports it.

## Phase 14 — Cross-subject integration hardening
- Queries, regression tests, audit of all cross-subject edges.
- BA-oriented "shared prerequisite" reporting (no new architecture unless a
  concrete consumer demands it).

## Governance checkpoints before each phase
- FREEZE doc reconciliation if it appears.
- `indicates` owner decision.
- 12-vs-13 entity count decision.
- No new relationship types in these phases.
