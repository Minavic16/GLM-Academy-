# Owner Decision Brief — Phase 19 (Mathematics Gap Triage)

Date: 2026-10-17. Baseline commit `765a292`. Evidence:
`JAMB_MATHEMATICS_RECONCILIATION.md`,
`MATHEMATICS_GAP_REGISTER.md`, `JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md`.

Resolution (Phase 20, 2026-10-17). Decision 1 was made: the owner
authorized a ten-topic implementation wave — the Wave A variant, expanded
with indices, change of subject and factorisation. It is implemented in
batches 070–079 (`examples/math_wave_a_phase20.py`, `build_graph_v41`);
see `docs/PHASE20_REPORT.md`. The Decision 2 items remain open as recorded.
This brief is retained as the Phase 19 record.

Scope rule reminder: official syllabus evidence establishes requirements;
only the owner authorizes implementation. This brief contains only decisions
that genuinely block the next implementation step. Already executed by
Phase 19 and not requiring decisions: all documentation corrections (I.1
classification correction; matrix/gap-register refinements; CI-register
refresh; activity-count correction).

## Decision 1 (immediate blocker) — Which Mathematics implementation work to authorize next

**Question.** 21 open implementation items were triaged (P1: 8 officially
confirmed, zero-implementation rows; P2: 13 officially confirmed depth
extensions). Which group should be authorized for implementation, in what
sequence?

**Options**

1. **Wave A only — Section I completion (Number & Numeration)** *(recommended)*
   M-03 modular arithmetic; M-04 number bases; M-05 surds; M-20
   approximation/errors (sig. figures, decimal places, percentage errors);
   M-21 standard form + log change-of-base; M-19 financial mathematics
   (simple interest, profit/loss, shares, VAT). ~4–6 new KCs plus methods,
   items, evidence; internal Mathematics-only changes; no cross-subject
   edges. Consequence: closes 6 of 8 P1 rows; makes Section I of the
   official JAMB syllabus the first fully addressed section. If declined,
   Section I remains the least-covered official section.
2. **Wave A + Wave B — add Algebra completion (Section II)**
   M-10 binary operations; M-22 sets depth (cardinality/Venn ≤3);
   M-23 polynomials depth (factor/remainder theorems, cubic, graphs);
   M-24 variation depth; M-25 inequalities depth; M-26 progression sums;
   M-11 permutations/combinations. Consequence: larger single phase
   (roughly double Wave A); still internal to Mathematics; higher review
   load, same validation gates.
3. **All waves A–E in one authorization** (B Algebra; C Geometry/Trig:
   M-09/M-12/M-13/M-27/M-28; D Statistics & Probability: M-15/M-16;
   E Calculus: M-14). Consequence: maximum closure potential but the
   largest single change surface; contrary to the established one-family
   wave practice (Phases 14–17); not recommended.
4. **Defer implementation** — continue retrieval/verification phases only
   (WAEC official, NERDC SSS3). Consequence: all P1/P2 gaps stay open;
   Mathematics stays IMPLEMENTATION_COMPLETE within the declared scope /
   BOARD_UNVERIFIED.

**Recommendation:** Option 1 (Wave A). It is the smallest coherent completion
unit, targets only officially confirmed and fully unimplemented
requirements, and keeps the established phase pattern (bounded batch with
full test/validation/determinism gates).

**Independent of this decision** (can proceed without owner input):
WAEC official WASSCE retrieval and NERDC SSS3 attempts (CI-24);
documentation and test upkeep; continued separation of JAMB/WAEC/NERDC/
secondary evidence.

## Decision 2 (later — not blocking now)

- **Waves B–E sequencing**: decide after Wave A lands (or with Decision 1
  if the owner prefers Option 2/3 now).
- **Ogive deferral**: documented deferral stands unless the owner
  explicitly reverses it; reversal would fold into the statistics wave
  (M-15). No action requested now.
- **WAEC-secondary-only rows** M-17 (vectors) and M-18 (transformations),
  and the NERDC-only proofs row M-29: revisit after official WAEC
  retrieval (evidence-retrieval dependency, not an implementation
  authorization).
- **Matrices assessment depth** (item exercises 2×2 determinant only):
  recorded as an observation in the reconciliation report; deepening
  assessment items would be canonical work and is *not* requested here.

## Deliberately not asked

- Re-ratification of OD-01…OD-05 (all ratified 2026-10-15) — not requested;
  the Phase 19 evidence supports the existing model (two status dimensions,
  13 entity types, `indicates` PROPOSED, Biology hold).
- CI-11/CI-12 (Chemistry buffers blocked on a Mathematics-side prerequisite
  edge) — separate, unchanged, not reopened by this phase.
- Any BOARD_VERIFIED promotion — unreachable until WAEC official documents
  are obtained; no decision available.

## Summary

| decision | blocking | recommendation | if unresolved |
|---|---|---|---|
| 1. Next Mathematics implementation wave | Yes — no canonical implementation can start without it | Wave A (Section I completion) | No Math implementation; retrieval/documentation continue |
| 2. Waves B–E, ogive reversal, WAEC-only rows, proofs | No — later choices | Sequence after Wave A; retrieval proceeds | Gaps stay registered; nothing regresses |
