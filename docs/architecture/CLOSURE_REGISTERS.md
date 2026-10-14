# Closure Issue Register (Phase 13.5)

| ID | Subject | Issue | State | Class | Action/Status |
|---|---|---|---|---|---|
| CI-01 | Math | Median/mode missing | IMPLEMENTATION_GAP | **Resolved**: kc.median_ungrouped (057) with TM+2 methods; evidence E0585 + OSTX 2.3/2.5; mode deferred as documented secondary row | Closed (implementation); official confirmation still open |
| CI-02 | Math | Dispersion missing | IMPLEMENTATION_GAP | **Resolved**: kc.measures_of_dispersion (058) TM+2 methods covering range/mean-deviation/variance/SD; E0589-92 + OSTX 2.7 | Closed (implementation); official confirmation still open |
| CI-03 | Math→Chem | pH blocked on log KC | DEPENDENCY_BLOCKER | **Resolved**: kc.logarithms + kc.ph_scale built, DERIVED edge | Closed |
| CI-04 | All | Phase 13 "11 sections" vs 15 source records | DOCUMENTATION_INCONSISTENCY | Reconciled: store authoritative (15); report superseded | Closed |
| CI-05 | All | Official PDFs inaccessible (IBASS SPA, WAEC placeholder, NERDC down; re-attempted 2026-10-10) | OFFICIAL_VERIFICATION_GAP | Recorded; owner decision on qualified-scope sign-off | Open |
| CI-06 | All | 12-vs-13 entity count | GOVERNANCE_BLOCKER | Proposed resolution documented (Subject = infrastructure); owner approval required | Open |
| CI-07 | All | `indicates` sign-off; freeze doc absent | GOVERNANCE_BLOCKER | Preserved, unchanged | Open |
| CI-08 | Physics | Fibre/LASER/electronics; EM-spectrum depth | IMPLEMENTATION_GAP (SHOULD-deferral stands) | Documented in matrix R17/R18 | Open |
| CI-09 | Chem | Buffers proper, polymers, industrial, transition metals | IMPLEMENTATION_GAP (deferrals stand) | Documented in matrix | Open |

# Owner Decision Register (Phase 13.5)

| ID | Decision | Options | Recommended default | If unresolved |
|---|---|---|---|---|
| OD-01 | Accept SUBJECT_COMPLETION_STANDARD v1.0 | Approve / amend / reject | Approve | Subjects stay PARTIALLY_COMPLETE |
| OD-02 | 12-vs-13: confirm Subject as infrastructure, 12 frozen domain entities | Confirm / alternative count | Confirm | Remains open; no code impact |
| OD-03 | `indicates` domain sign-off | Confirm Item→Misc/KC / re-admit EvidenceRule | Confirm existing | New `indicates` stay PROPOSED |
| OD-04 | Qualified-scope sign-off (slices COMPLETE against OpenStax-verified scope pending official PDFs) | Sign off / require PDFs first | Sign off qualified scope | Board confirmation stays open; BA design proceeds at risk |
| OD-05 | Biology start exception (Math median/dispersion + SHOULD-rows still open) | Allow parallel start / require closure first | Allow parallel start (independent subject, no dependency on open items) | Biology gated |


## Phase 13.6 closure note
CI-01/CI-02 closed at implementation level (2026-10-15): new KCs
kc.median_ungrouped (b057), kc.measures_of_dispersion (b058), both
ACCEPTED with HUMAN review + legacy-inherited JAMB pointers + verified
OpenStax evidence. Board-level verification (OD-04) still open;
implementation of these two families is complete against the declared scope.
