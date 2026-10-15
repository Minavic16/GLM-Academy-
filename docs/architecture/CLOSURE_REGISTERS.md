# Closure Issue Register (Phase 13.5)

| ID | Subject | Issue | State | Class | Action/Status |
|---|---|---|---|---|---|
| CI-01 | Math | Median/mode missing | IMPLEMENTATION_GAP | **Resolved**: kc.median_ungrouped (057) with TM+2 methods; evidence E0585 + OSTX 2.3/2.5; mode deferred as documented secondary row | Closed (implementation); official confirmation still open |
| CI-02 | Math | Dispersion missing | IMPLEMENTATION_GAP | **Resolved**: kc.measures_of_dispersion (058) TM+2 methods covering range/mean-deviation/variance/SD; E0589-92 + OSTX 2.7 | Closed (implementation); official confirmation still open |
| CI-03 | Math→Chem | pH blocked on log KC | DEPENDENCY_BLOCKER | **Resolved**: kc.logarithms + kc.ph_scale built, DERIVED edge | Closed |
| CI-04 | All | Phase 13 "11 sections" vs 15 source records | DOCUMENTATION_INCONSISTENCY | Reconciled: store authoritative (15); report superseded | Closed |
| CI-05 | All | Official PDFs inaccessible (IBASS SPA, WAEC placeholder, NERDC down; re-attempted 2026-10-10) | OFFICIAL_VERIFICATION_GAP | Recorded; owner decision on qualified-scope sign-off | Open |
| CI-06 | All | 12-vs-13 entity count | GOVERNANCE_BLOCKER | **CLOSED 2026-10-15**: OD-02 RATIFIED (13 incl. Subject); test_entity_type_count_frozen locks count; sanity §12's '12' excludes Subject | Closed |
| CI-07 | All | `indicates` sign-off; freeze doc absent | GOVERNANCE_BLOCKER | Preserved, unchanged | Open |
| CI-08 | Physics | Fibre/LASER/electronics; EM-spectrum depth | IMPLEMENTATION_GAP (SHOULD-deferral stands) | Documented in matrix R17/R18 | Open |
| CI-09 | Chem | Buffers proper, polymers, industrial, transition metals | IMPLEMENTATION_GAP (deferrals stand) | Documented in matrix | Open |

# Owner Decision Register (Phase 13.5)

| ID | Decision | Options | Recommended default | If unresolved |
|---|---|---|---|---|
| OD-01 | Standard approval — APPROVED IN PRINCIPLE (separate implementation / board-verification statuses) | Approve in principle / full ratification | Approve in principle | RATIFIED 2026-10-15; standard v1.2 issued. Full-document formal ratification remains with owner | RATIFIED (in principle) |
| OD-02 | Canonical entity count 13 incl. Subject | Confirm / alternative count | Confirm | RATIFIED 2026-10-15; CI-06 closed; docs corrected | RATIFIED |
| OD-03 | `indicates` definition/restrictions | Confirm Item→Misc/KC / re-admit EvidenceRule | Confirm existing | RATIFIED 2026-10-15; claim stays PROPOSED; no broadening | RATIFIED |
| OD-04 | Qualified implementation completion (separate statuses) | Strict closure / qualified / separate dimensions | Separate dimensions | RATIFIED 2026-10-15; statuses applied: Math IMPL_COMPLETE/BOARD_UNVERIFIED; Phys/Chem IMPL_PARTIAL/BOARD_UNVERIFIED | RATIFIED |
| OD-05 | Biology start | Allow start / hold | Hold | RATIFIED 2026-10-15: BIOLOGY ON HOLD; see BIOLOGY_HOLD_RECORD.md | RATIFIED (hold) |


## Phase 13.6 closure note
CI-01/CI-02 closed at implementation level (2026-10-15): new KCs
kc.median_ungrouped (b057), kc.measures_of_dispersion (b058), both
ACCEPTED with HUMAN review + legacy-inherited JAMB pointers + verified
OpenStax evidence. Board-level verification (OD-04) still open;
implementation of these two families is complete against the declared scope.


## Phase 13.7 registers update (2026-10-15)
- OD-01: standard reviewed; editorial additions only (authority + provenance clauses); v1.1 still PROPOSED.
- OD-02: evidence chain documented in PHASE137_GOVERNANCE_AUDIT.md; test_entity_type_count_frozen added.
- OD-03: semantics documented; usage conforms; unchanged.
- OD-04: Option 3 recommended (separate implementation vs board-verification dimensions, recorded here — no schema change).
- OD-05: Biology remains BLOCKED pending OD-01 + explicit authorization.
- Subject statuses now recorded: Math IMPLEMENTATION_COMPLETE/BOARD_UNVERIFIED; Physics/Chemistry PARTIAL/BOARD_UNVERIFIED.


## Phase 13.8 updates (2026-10-15)
All five decisions recorded as RATIFIED per explicit owner instruction.
Subject statuses recorded under the OD-01/OD-04 model in
`SUBJECT_COMPLETION_ROADMAP.md`. Milestones (owner-approved /
docs-updated / implementation-verified / external-verified) kept distinct:
only docs-updated and implementation-verified are complete; external
official verification remains outstanding for all three subjects.
No Biology artifacts created (BIOLOGY_HOLD_RECORD.md).
