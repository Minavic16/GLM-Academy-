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
| CI-08 | Physics | Fibre/LASER/electronics; EM-spectrum depth | IMPLEMENTATION_GAP | **CLOSED 2026-10-15 (Phase 14)**: kc.fibre_optics, kc.laser_basics, kc.semiconductor_electronics, kc.em_spectrum accepted with evidence | Closed |
| CI-09 | Chem | Buffers proper, polymers, industrial, transition metals | IMPLEMENTATION_GAP (deferrals stand) | Documented in matrix; buffers proper specifically BLOCKED by Phase 15 scope constraint (needs new cross-subject dependency from Mathematics log KC) — see PHASE15_GAP_AUDIT.md | Open |
| CI-10 | Chem | Organic reactions NOT_IMPLEMENTED | IMPLEMENTATION_GAP | **CLOSED 2026-10-16 (Phase 15)**: nine KCs accepted (b065) with TMs/Methods/Items, CHEM2E 20.1–20.4 evidence, HUMAN review; prerequisites Chemistry-internal | Closed |
| CI-11 | Math → Chem | Chemistry buffers need pH calculations; logarithms KC is in Mathematics; new prerequisite edge would modify Mathematics records | IMPLEMENTATION_GAP (cross-subject) | Blocked (Phase 15/16 scope constraint) | NERDC Chem SSS1 p.15 / SSS2 acids-and-salts; CDG kc.ph_scale + cl.pre56.log_ph scoped to tm.ph_problems | Owner-authorized scoped Mathematics extension, then Chemistry buffer KCs/TM | Open — owner decision on scoped Math change |
| CI-12 | Chem | Buffers proper not implemented | IMPLEMENTATION_GAP | Open | CI-09; NERDC SSS1/SSS2 topic lists do not list "buffer"; SSS3 unreachable | Implement after CI-11 unblocked | Re-evaluate after CI-11 + SSS3 retrieval |
| CI-13 | Chem | Polymers not implemented | IMPLEMENTATION_GAP | Deferred (owner-documented) | NERDC SSS1/SSS2 topic lists: no polymers topic | Owner decision to reopen | Revisit with owner authorization |
| CI-14 | Chem | Industrial chemistry not implemented | IMPLEMENTATION_GAP | Deferred (owner-documented) | NERDC "Chemical industry" SSS1 p.2 (NOT_COVERED); "Chemistry and industry" SSS2 p.30 | Owner decision | Revisit with owner authorization |
| CI-15 | Chem | Transition metals / electrolytic cells detail | IMPLEMENTATION_GAP | Deferred (owner-documented) | NERDC SSS1/SSS2: no transition-metals topic; electrolysis COVERED via kc.redox_electrochemistry | Owner decision | Revisit with owner authorization |
| CI-16 | Chem | Water topic not in CDG (newly mapped vs NERDC) | IMPLEMENTATION_GAP | Open | NERDC Chem SSS1 p.17 and SSS2 p.10 (NOT_COVERED) | Owner decision: add water KC or out of scope | Recorded in CHEMISTRY_SYLLABUS_COVERAGE.md |
| CI-17 | Phys | Projectile Motion not in CDG (newly mapped vs NERDC) | IMPLEMENTATION_GAP | Open | NERDC Phy SSS2 p.7 (NOT_COVERED); Math quadratic dependencies exist | Implement projectile KC using existing Math→Physics edges | Recorded in PHYSICS_SYLLABUS_COVERAGE.md |
| CI-18 | Phys | Simple Harmonic Motion not in CDG (newly mapped vs NERDC) | IMPLEMENTATION_GAP | Open | NERDC Phy SSS2 p.8 (NOT_COVERED) | Owner decision | Recorded in PHYSICS_SYLLABUS_COVERAGE.md |
| CI-19 | Phys | Introduction to Internet and Intranet not in CDG (newly mapped) | IMPLEMENTATION_GAP | Open / likely NOT_APPLICABLE to core physics | NERDC Phy SSS2 p.46 (NOT_COVERED) | Owner decision; likely outside CDG physics scope | Recorded in PHYSICS_SYLLABUS_COVERAGE.md |
| CI-20 | Math | Sets not in CDG (newly mapped vs NERDC) | IMPLEMENTATION_GAP | **Closed at implementation level (Phase 17 batch 066)**: kc.sets_operations + TM + methods + item, NERDC SSS1 p.7 evidence; residual depth (cardinality, Venn ≤3 sets) triaged Phase 19 (M-22) | NERDC Math SSS1 p.7 | Owner decision (done) | Recorded in MATHEMATICS_SYLLABUS_COVERAGE.md; Phase 19 triage MATHEMATICS_GAP_REGISTER.md |
| CI-21 | Math | Logic not in CDG (newly mapped vs NERDC) | IMPLEMENTATION_GAP | **Closed at implementation level (Phase 17 batch 066)**: kc.logical_reasoning + TM + methods + item, NERDC SSS1 p.8 evidence; not an official JAMB topic (Phase 19) | NERDC Math SSS1 p.8 / SSS2 p.9 | Owner decision (done) | Recorded in MATHEMATICS_SYLLABUS_COVERAGE.md; Phase 19 triage MATHEMATICS_GAP_REGISTER.md (M-02) |
| CI-22 | Math | Mensuration not in CDG (newly mapped vs NERDC) | IMPLEMENTATION_GAP | **Closed at implementation level (Phase 17 batch 069)**: kc.mensuration + TM + methods + item, NERDC SSS1 p.11 evidence; residual depth (chords, plane figures, spheres, earth-as-sphere) triaged Phase 19 (M-28) | NERDC Math SSS1 p.11 | Owner decision (done) | Recorded in MATHEMATICS_SYLLABUS_COVERAGE.md; Phase 19 triage MATHEMATICS_GAP_REGISTER.md |
| CI-23 | Math | Modular arithmetic, number bases (partial), approximation, surds, sequence & series, bearings, proofs, construction, ogive | IMPLEMENTATION_GAP | **Partially closed**: sequence & series implemented (Phase 17 batch 067); modular arithmetic, number bases, approximation/errors and surds implemented (Phase 20 batches 070/071/073/074); construction implemented (Phase 22 batch 081 — construction procedures of special angles 30°–90°, NERDC matrix p.14 row). Remaining items: bearings, proofs, ogive (triaged Phase 19) | NERDC Math SSS1/SSS2 topic lists (NOT_COVERED rows; ogive documented deferral) | Phase 20 wave and Phase 22 P1 closure authorizations executed (PHASE20_REPORT.md; PHASE22_REPORT.md); remaining items still require owner authorization | Bearings/proofs/ogive deferrals stand |
| CI-24 | All | Official-board verification (JAMB/WAEC/NERDC alignment) | OFFICIAL_VERIFICATION_GAP | Open | CI-05; JAMB official UTME E-syllabus obtained + content-checked for Math/Phys/Chem (Phase 18 — IBASS static assets; see PHASE18_RETRIEVAL_REPORT.md); WAEC not obtained (downloads are CASS installers only); NERDC SSS1/SSS2 content-checked, SSS3 unretrieved (LMIS login-gated; nerdc.org.ng 500); Phase 22 bounded sprint (2026-10-17): WAEC Math syllabus still not located (site search: Bookkeeping syllabus article only); NERDC SSS3 still 404/login-gated; JAMB applicable cycle UNRESOLVED (PHASE22_REPORT.md) | Continue retrieval: WAEC official WASSCE syllabus documents; NERDC SSS3; promote rows to BOARD_VERIFIED only on checked content; JAMB-side official matrices recorded (JAMB_*_OFFICIAL_COVERAGE.md) | M-1 official-source verification plan; Phase 18 retrieval report |
| CI-25 | Chem | Practical chemistry — WAEC practical detail unverified | OFFICIAL_VERIFICATION_GAP | Open | CI-05; kc.practical_chemistry implementation adequate | Obtain WAEC practical syllabus; map to practical KC methods/items | Same as CI-24 |
| CI-26 | Phys | Practical physics — WAEC practical detail unverified | OFFICIAL_VERIFICATION_GAP | Open | Phase 14 roadmap R16; kc.practical_measurement implementation adequate | Same as CI-24 | Same as CI-24 |

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

Phase 14: CI-08 closed; Physics now IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED.
Also fixed cl.pre57.mean_median UNDERSTAND/ALL/ASSERTED (test-found defect).

Phase 15 (2026-10-16): CI-10 closed; the organic-reactions gap
(CHEMISTRY_COVERAGE_MATRIX row "Organic reactions") is IMPLEMENTED by
batch 065 (`examples/chemistry_organic_reactions.py`,
`build_graph_v39`). Nine KCs, one TM per reaction family, all HUMAN
reviewed with OpenStax Chemistry 2e 20-1–20-4 evidence. All new
prerequisites are Chemistry-internal (no new cross-subject dependency
claims), per the Phase 15 scope restriction.
Chemistry implementation remains IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED
because of the blocked buffers gap (CI-09/CI-11/CI-12) and the deferred
families (polymers / industrial chemistry / transition metals).
Official-board verification is unchanged (CI-05/CI-24).

Phase 16 (2026-10-17): official-source retrieval completed for NERDC
SSS 1/SSS 2 Mathematics, Physics, Chemistry (all retrieved, extracted,
authenticity established — see PHASE16_RETRIEVAL_REPORT.md). JAMB IBASS
and WAEC official documents were not obtained; all three subjects remain
BOARD_UNVERIFIED (CI-24). New issues CI-11…CI-26 recorded in the
cross-subject gap register (CROSS_SUBJECT_GAP_REGISTER.md), including
cross-subject Chemistry buffers (CI-11/CI-12) and NERDC-mapped
implementation gaps (CI-16…CI-23). No subject implementation status
changed; no schema change; no Biology artifacts.

Phase 17 (2026-10-17): Mathematics scope expansion (owner-authorized four
families). CI register Mathematics rows M-01 (Sets), M-02 (Logic),
M-06 (Sequences & series), M-07 (Matrices & determinants), M-08 (Mensuration)
CLOSED as implemented in Phase 17 batches 066-069
(`examples/math_scope_expansion.py`, `build_graph_v40`). Five new Mathematics
KCs (43→44: +sets, +logic, +sequences/series, +matrices/determinants,
+mensuration), each ACCEPTED with HUMAN review, TM, Methods, Items and
evidence. Sets/logic/sequences/mensuration evidenced by NERDC Math SSS1/SSS2
(official); matrices/determinants evidenced by JAMB/WAEC via Syllabus NG
(secondary, disclosed — not in NERDC SSS1/SSS2; SSS3 unretrieved). No
schema change; 13 entity types preserved; `indicates` remains PROPOSED;
no cross-subject edges added; no Biology/English artifacts.
Mathematics remains IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED (expanded
declared scope; board verification unchanged CI-24).

Phase 18 (2026-10-17): official JAMB UTME E-syllabus retrieved for
Mathematics, Physics, Chemistry from the official IBASS portal (hashed
static assets discovered via SPA-bundle analysis; SHA-256 + page locators
recorded in PHASE18_RETRIEVAL_REPORT.md and the three SRC.JAMB.UTME.*.2025
source records). Official coverage matrices built
(JAMB_{MATHEMATICS,PHYSICS,CHEMISTRY}_OFFICIAL_COVERAGE.md) — JAMB-side
requirements content-checked. Two Phase 16B statements corrected: modular
arithmetic IS an official JAMB requirement (Math I.1(c)); "Buffer solution"
IS explicitly in official JAMB Chemistry topic 8. New requirement exposed:
Chemistry topic 18 "Astronomical Chemistry" (no CDG coverage — new gap).
WAEC official documents and NERDC SSS 3 remain unretrieved: CI-24 stays
Open and all three subjects stay BOARD_UNVERIFIED. No schema/store change;
no subject implementation status changed; secondary matrices remain
retained as history (SECONDARY / BOARD_UNVERIFIED); no Biology/English
artifacts.

Phase 19 (2026-10-17): Mathematics-only official JAMB evidence
reconciliation and gap triage (documentation-only; no canonical changes).
All 23 official JAMB Mathematics topics reconciled record-by-record against
build_graph_v40 (`JAMB_MATHEMATICS_RECONCILIATION.md`): COVERED 2 /
PARTIALLY_COVERED 17 / NOT_COVERED 4 — I.1 (number bases/modular
arithmetic) corrected from PARTIALLY_COVERED to NOT_COVERED because the
previously mapped KCs are adjacency, not scope support. Phase 17 five-KC
audit: sets, sequences, mensuration = topic confirmed + depth gaps
(M-22/M-26/M-28); logic = not a JAMB topic (NERDC-based, closed); matrices
= topic + scope confirmed, implementation evidence remains secondary
(Syllabus NG, Phase 17 provenance preserved), no implementation change.
Modular arithmetic: officially confirmed (I.1(c)), zero CDG records — final
classification NOT_COVERED (M-03). New depth exposures itemized (midpoint;
standard form; log change-of-base; polygon/cyclic/chord objectives; chord
lengths; plane-figure areas; spheres; experimental probability). Updates:
CI-20/CI-21/CI-22 closed at implementation level; CI-23 partially closed
(sequence & series implemented; remainder triaged); deduplicated register
`MATHEMATICS_GAP_REGISTER.md` (M-01…M-29); owner decisions
`OWNER_DECISION_BRIEF_PHASE19.md` (next implementation wave authorization —
Wave A recommended); documentation correction: v40 activity count is 204
(Phase 17/18 reports printed the stale v39 figure 192). No promotion to
BOARD_VERIFIED; WAEC official and NERDC SSS 3 still outstanding (CI-24
Open); no schema/store change; no Biology/English artifacts.

Phase 20 (2026-10-17): Mathematics implementation wave A (owner-authorized
ten topics; batches 070–079; `examples/math_wave_a_phase20.py`,
build_graph_v41). Ten new KCs (44→54: number bases, modular arithmetic,
indices laws, surds, approximation/errors, standard form, simple interest,
profit & loss, shares & VAT, factorisation patterns), each ACCEPTED with
HUMAN review, TM, methods, items and evidence; plus depth extensions to
kc.logarithms (change of base) and kc.change_of_subject (powers/roots).
Official JAMB source SRC.JAMB.UTME.MATH.2025 registered in the canonical
store (first time) and cited by all new evidence (JAMB Math p.2–3
locators). M-03/M-04/M-05/M-19/M-20/M-21 closed at implementation level;
M-23 partially extended (common factors, difference of two squares).
Official JAMB counts now COVERED 5 / PARTIALLY_COVERED 15 / NOT_COVERED 3.
CI-23 updated (remaining: bearings, proofs, construction, ogive). No
cross-subject edges added; no schema change; 13 entity types; `indicates`
remains PROPOSED; no Biology/English artifacts. WAEC official and NERDC
SSS 3 remain unretrieved: CI-24 stays Open; no promotion to
BOARD_VERIFIED.

Phase 21 (2026-10-17; audit only): Mathematics closure-strategy audit and
owner decision brief. Live baseline re-verified (head `63f4567`; store
424/678/337/86/234; validation clean; 199 tests; matrix 5/15/3; no
discrepancy vs the Phase 20 record). All M-01…M-29 rows classified with
dispositions (P1: M-09/M-10 plus the V.1 representation component split as
M-15a; 13 P2 residuals; M-17/M-18 evidence-gated; M-29 scope call; ogive
deferred). CI-24 status refresh from bounded official-channel probes:
waecnigeria.org publishes per-subject syllabus documents as article
attachments (confirmed instance: Bookkeeping & Office Practice 2022–2025)
— no Mathematics syllabus article/attachment found (site index, news
pagination, targeted searches); NERDC LMIS `sss_3` still 404 (portal root
= login gate); nerdc.org.ng HTTP 500; JAMB E-syllabus cycle year still
unprinted (UNRESOLVED). CI-24 remains Open; nothing was obtained; no
third-party substitution; no promotions. Proposals (Wave B P1 closure;
bounded retrieval sprint; closure criteria) are NOT ratified — see
OWNER_DECISION_BRIEF_PHASE21.md (D1–D4) and docs/PHASE21_REPORT.md. No
canonical/store change.

Phase 22 (2026-10-17): Mathematics P1 closure implemented (owner-authorized;
batches 080–082; `examples/math_p1_closure_phase22.py`, build_graph_v42):
binary operations (II.5), loci & construction (III.3 + III.1(d) special-angle
construction procedures) and representation of data (V.1) — three new KCs
(54→57), each ACCEPTED with HUMAN review, TM, methods, items and evidence.
All new claims (47) and evidence (22) cite the official JAMB source
(SRC.JAMB.UTME.MATH.2025) with II.5 / III.3 / III.1d / V.1 locators.
Official JAMB counts now COVERED 8 / PARTIALLY_COVERED 15 / NOT_COVERED 0;
M-09/M-10 closed at implementation level; the M-15 data-representation
component (audit split M-15a) implemented — P2 residuals and the ogive
deferral stand. CI-23 updated (remaining: bearings, proofs, ogive). Bounded
retrieval sprint: WAEC Math syllabus not located (site search shows only the
Bookkeeping syllabus article); NERDC SSS3 still unavailable (404 /
login-gated; nerdc.org.ng 500); JAMB applicable cycle remains UNRESOLVED
(no cycle marker in the PDF or the official SPA; metadata date
insufficient). No cross-subject edges added; no schema change; 13 entity
types; `indicates` remains PROPOSED; no Biology/English artifacts; no
promotion to BOARD_VERIFIED — CI-24 stays Open.
