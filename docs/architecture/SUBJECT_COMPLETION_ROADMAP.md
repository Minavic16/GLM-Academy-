# Phase 13.8 Roadmap — Mathematics, Physics, Chemistry

Statuses under ratified model (OD-01/OD-04):

## MATHEMATICS — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED (scope expanded Phase 17; implementation waves Phase 20 + Phase 22)
Completed: 57 KCs (39 baseline + 5 in Phase 17 batches 066-069 + 10 in
Phase 20 batches 070-079 + 3 in Phase 22 batches 080-082), full chains
validated, CI-01/CI-02 closed
(median + dispersion with preserved legacy ids), kc.logarithms (b055)
enables Chemistry pH; log→pH edge cl.pre56.log_ph ACCEPTED and intact.
Phase 20 (2026-10-17) implemented the owner-authorized ten-topic wave —
see docs/PHASE20_REPORT.md.
Phase 22 (2026-10-17) implemented the owner-authorized P1 closure —
see docs/PHASE22_REPORT.md.

Phase 17 scope expansion (owner-authorized four families):
- Batch 066 Sets & logic: kc.sets_operations, kc.logical_reasoning (NERDC Math
  SSS1 pp. 7–8).
- Batch 067 Sequences & series: kc.sequences_series (NERDC Math SSS2 p.1).
- Batch 068 Matrices & determinants: kc.matrix_algebra (secondary JAMB/WAEC
  evidence via Syllabus NG; NOT in NERDC SSS1/SSS2 topic lists — disclosed).
- Batch 069 Mensuration: kc.mensuration (NERDC Math SSS1 p.11).
All new KCs ACCEPTED with HUMAN review, each with TM, Methods, Items and
evidence. Prerequisites are curriculum-adjacency elaborations (logic→sets,
sequences→integer arithmetic, matrices→linear equations, mensuration→circle
theorems); no schema change, no cross-subject edges added.

Remaining gaps:
1. Official-board verification (M-1): retrieval + content-check of JAMB/WAEC/
   NERDC Math documents; map syllabus rows to KC coverage; promote rows to
   BOARD_VERIFIED only on checked content. NERDC Math SSS 1/SSS 2 retrieved
   and content-checked (Phase 16): MATHEMATICS_SYLLABUS_COVERAGE.md maps
   all official topics to CDG KCs. JAMB official E-syllabus retrieved and
   content-checked (Phase 18): JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md maps
   all 23 official JAMB topics; JAMB-side requirements confirmed (incl.
   matrices II.6, sets I.4, progression II.4, mensuration III.2; correction:
   modular arithmetic IS official JAMB I.1(c); new depth exposures recorded).
   WAEC official documents NOT obtained (archive stub; e-learning = past
   questions only) — BOARD_VERIFIED remains unreachable (WAEC outstanding).
2. NOT_COVERED rows requiring owner scope decisions: Phase 19 triage
   complete — see `MATHEMATICS_GAP_REGISTER.md` (M-01…M-29) and
   `OWNER_DECISION_BRIEF_PHASE19.md`. Official JAMB confirmation corrected
   the picture: I.1 number bases/modular arithmetic was NOT_COVERED (Phase 19
   counts: COVERED 2 / PARTIALLY_COVERED 17 / NOT_COVERED 4: I.1, II.5,
   III.3, V.1). Phase 20 (2026-10-17) implemented the owner-authorized
   ten-topic wave (batches 070–079): modular arithmetic, number bases,
   surds, approximation/errors, standard form + log change-of-base,
   financial mathematics (M-03/04/05/19/20/21 closed at implementation
   level), plus indices laws, change-of-subject powers/roots depth and
   factorisation common-factor/difference-of-squares (M-23 partially
   extended). Official JAMB counts now COVERED 5 / PARTIALLY_COVERED 15 /
   NOT_COVERED 3 (II.5 binary operations, III.3 loci, V.1 representation of
   data). Phase 22 (2026-10-17) implemented the P1 closure (batches 080–082):
   binary operations, loci & construction, representation of data — official
   counts now COVERED 8 / PARTIALLY_COVERED 15 / NOT_COVERED 0. Remaining
   implementation items: 0×P1 and 13×P2 (officially confirmed depth
   extensions: sets depth, polynomials depth, variation, inequalities,
   progression sums, perm/comb, coordinate geometry, trig applications,
   geometry depth, mensuration depth, statistics depth, probability depth,
   calculus depth); the M-15 data-representation component is implemented
   (batch 082).
   Ogive deferral documented and stands. Matrices & determinants:
   requirement + scope officially confirmed (JAMB II.6); implementation
   evidence remains secondary (Syllabus NG, Phase 17 provenance preserved) —
   disclosed, no implementation change; assessment-depth note recorded.
Tests for closure: full suite ≥ current, store `[]`, coverage matrix rows
all COVERED-or-excluded with evidence refs.
Next task: owner decision on the P2 prioritization (the Phase 21 brief D2
documented-residuals policy is applied; P2 rows remain unauthorized as a
wave); WAEC official documents and NERDC SSS 3 outstanding (CI-24,
re-attempted in Phase 22 without result). Biology remains on hold.

Phase 21 (2026-10-17; audit only — see docs/PHASE21_REPORT.md): live audit
re-verified the Phase 20 baseline (424/678/337/86/234; validation clean;
199 tests; no discrepancy vs PHASE20_REPORT.md). Coverage stands
COVERED 5 / PARTIALLY_COVERED 15 / NOT_COVERED 3. Audit classification:
P1 = M-09 loci & construction, M-10 binary operations, plus the V.1
representation component split from M-15 as M-15a (audit-level split; the
register was not rewritten); P2 = 13 depth rows; WAEC-secondary-only =
M-17/M-18; NERDC-only = M-29; ogive deferral stands. PROPOSED (NOT
ratified; owner decisions D1–D4 in OWNER_DECISION_BRIEF_PHASE21.md):
next package "Wave B — P1 closure" (binary operations; loci &
construction; representation of data) plus a bounded retrieval sprint for
WAEC official / NERDC SSS3 / JAMB cycle; P2 rows proposed as documented
residuals pending a prioritization brief; closure criteria (brief §6)
Proposed closure criteria (brief §6)
proposed for ratification, including a proposed declared-scope extension —
none of this is in force.

Phase 22 (2026-10-17; see docs/PHASE22_REPORT.md): owner-authorized P1
closure executed — batches 080–082 (binary operations II.5; loci &
construction III.3 + III.1d; representation of data V.1) in
examples/math_p1_closure_phase22.py (build_graph_v42); three new KCs (57
total). Official JAMB counts: COVERED 8 / PARTIALLY_COVERED 15 /
NOT_COVERED 0. M-09/M-10 closed at implementation level; M-15
data-representation component implemented (residual M-15b: mode, grouped
data, cumulative frequency/ogive deferral, grouped dispersion). Bounded
retrieval sprint executed: WAEC Math syllabus not located; NERDC SSS3
still unavailable (404/login-gated); JAMB applicable cycle UNRESOLVED. P2
residuals documented and unauthorized; ogive deferral stands; board
verification unchanged (CI-24 Open; no BOARD_VERIFIED promotion).

## PHYSICS — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED (updated 2026-10-15, Phase 14; syllabus mapping Phase 16; JAMB official mapping Phase 18)
Phase 14 closed all seven audit targets: friction/machines (b059), EM spectrum
depth (b060), energy sources/society (b061), fibre optics (b062), lasers
(b063), electronics (b064); practical implementation acceptable with WAEC
detail still unverified. Historical section below retained for audit trail.

### PHYSICS — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED
Counts: 19 KCs; 4 Math→Physics edges + further Science edges.
Verified partial/deferred:
- Fibre optics / LASER / elementary electronics — NOT_IMPLEMENTED
  (SHOULD-deferral; matrix R17).
- Friction/machines, EM spectrum depth, energy-society — PARTIAL via parent
  KCs (R06/R18/R19).
- Practicals — PARTIAL; WAEC practical detail SOURCE_UNVERIFIED (R16).
NERDC syllabus mapping (Phase 16): PHYSICS_SYLLABUS_COVERAGE.md maps all
official NERDC Physics SSS 1/SSS 2 topics to CDG KCs. NEWLY MAPPED
implementation gaps vs the official curriculum: Projectile Motion (NOT_COVERED,
NERDC p.7), Simple Harmonic Motion (NOT_COVERED, p.8), Introduction to
Internet and Intranet (NOT_COVERED, p.46); many other topics PARTIALLY_COVERED
(KCs exist but performance objectives not evidenced as methods/items).
These require owner scope decisions; they do not change the ratified
IMPLEMENTATION_COMPLETE status within the declared scope.
Next task: DONE in Phase 14 — Physics is IMPLEMENTATION_COMPLETE; next is
board verification (M-1 plan) plus owner decisions on CI-17…CI-19.
Phase 18: JAMB official E-syllabus retrieved and content-checked
(JAMB_PHYSICS_OFFICIAL_COVERAGE.md maps all 40 official topics): Phase 14
closures confirmed as official requirements (topics 6, 7, 27, 39, 40); new
gaps recorded P-18 (vapours & humidity), P-19 (light energy); WAEC and NERDC
SSS 3 still outstanding (CI-24 Open; BOARD_UNVERIFIED).

## CHEMISTRY — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED (updated 2026-10-16, Phase 15; syllabus mapping 2026-10-17, Phase 16)
Counts: 21 KCs (12 foundational + 9 organic-reactions), 81 TMs.

Phase 15 closed the organic-reactions gap (the only implementation gap in
Chemistry's declared scope):
- Batch 065 (`examples/chemistry_organic_reactions.py`,
  `build_graph_v39`): kc.reactions_of_alkanes, kc.reactions_of_alkenes,
  kc.isomerism, kc.alcohols, kc.ethers, kc.aldehydes_ketones,
  kc.carboxylic_acids, kc.amines, kc.amides — each with a targeting TM,
  Methods, Items, and ACCEPTED claims. Evidence: OpenStax Chemistry 2e
  20-1–20-4 (verified). Prerequisites are Chemistry-internal; no new
  cross-subject dependency claims were created (Phase 15 restriction).
- CI-10 closed (see CLOSURE_REGISTERS.md).

Remaining gaps:
- Buffers proper — BLOCKED (Phase 15 scope constraint, CI-11/CI-12).
  Buffer pH calculations require the Mathematics logarithms KC, and creating
  that prerequisite edge would modify Mathematics-side records.
  Re-evaluate only with owner authorization.
- Polymers, industrial chemistry — DEFERRED (owner-documented deferral, CI-13/CI-14).
- Electrolytic cells detail / transition metals — DEFERRED (owner-documented
  deferral, CI-15).
- Practical: implementation complete; official verification outstanding
  (CI-25). Board verification status remains BOARD_UNVERIFIED.
NERDC syllabus mapping (Phase 16): CHEMISTRY_SYLLABUS_COVERAGE.md maps all
official NERDC Chemistry SSS 1/SSS 2 topics to CDG KCs. Organic topics
(Carbon and its compounds, Hydrocarbons, Alkanols, Electrolysis) are now
COVERED via batch 065. NEWLY MAPPED NOT_COVERED topics include Water
(CI-16), Air, Hydrogen, Oxygen, Halogens, Nitrogen, Sulphur, Chemical
industry, Branches of Chemistry, Chemical hazards, Entrepreneurship — all
requiring owner scope decisions; none change the ratified
IMPLEMENTATION_PARTIAL status.
Next task: M-1 official-source verification (JAMB/WAEC retrieval attempts +
NERDC SSS 3 attempt); owner decisions on CI-11…CI-16 (buffers, deferred
families, newly mapped topics). Biology remains on hold.
Phase 18: JAMB official E-syllabus retrieved and content-checked
(JAMB_CHEMISTRY_OFFICIAL_COVERAGE.md maps all 18 official topics): buffers
confirmed as an official JAMB requirement (topic 8 "Buffer solution") with
the CI-11/CI-12 block unchanged; new gap C-15 astronomical chemistry
recorded; WAEC and NERDC SSS 3 still outstanding (CI-24 Open;
BOARD_UNVERIFIED).
## Recommended next phase
Phase 14: Physics completion wave — DONE (implemented in Phase 14;
Physics is IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED).
Phase 15: Chemistry organic-reactions wave — DONE (implemented in Phase 15;
CI-10 closed).
Phase 16: official-source verification (M-1) — DONE as retrieval
(2026-10-17): NERDC SSS 1/SSS 2 Mathematics, Physics, Chemistry retrieved,
extracted, authenticity established; JAMB IBASS and WAEC official documents
not obtained at that time; all three subjects remain BOARD_UNVERIFIED.
Phase 16B: secondary-source comparison (Syllabus NG) — DONE; 45 proposed
gaps registered (DEDUPLICATED_IMPLEMENTATION_GAP_REGISTER.md).
Phase 17: Mathematics scope expansion — DONE (owner-authorized four
families; batches 066–069; five new KCs).
Phase 18: JAMB official E-syllabus retrieval + content check — DONE
(Math/Phys/Chem; official matrices; corrections M-03/C-12; new gaps P-18,
P-19, C-15; WAEC + NERDC SSS 3 outstanding; PHASE18_RETRIEVAL_REPORT.md).
Phase 19: Mathematics JAMB-evidence reconciliation + gap triage — DONE
(2026-10-17): all 23 official JAMB Mathematics topics reconciled
record-by-record (JAMB_MATHEMATICS_RECONCILIATION.md); I.1 corrected to
NOT_COVERED (official counts 2/17/4); deduplicated register
MATHEMATICS_GAP_REGISTER.md (M-01…M-29); owner brief
OWNER_DECISION_BRIEF_PHASE19.md (Wave A — Section I completion —
recommended); documentation corrections applied (CI-20/21/22 closed,
CI-23 partial, activity count 204); no canonical changes; no status
promotions.
Phase 20: Mathematics Wave A implementation — DONE (2026-10-17;
owner-authorized ten topics): batches 070–079 in
examples/math_wave_a_phase20.py (build_graph_v41); ten new KCs (54 total);
official JAMB source SRC.JAMB.UTME.MATH.2025 registered; M-03/04/05/19/
20/21 closed at implementation level; M-23 partially extended; official
counts now 5/15/3; no status promotions (PHASE20_REPORT.md).
Phase 21: Mathematics closure-strategy audit — DONE (2026-10-17; audit
only): all M-01…M-29 rows classified with dispositions + owner decision
brief (OWNER_DECISION_BRIEF_PHASE21.md, D1–D4); no canonical changes
(PHASE21_REPORT.md).
Phase 22: Mathematics P1 closure + retrieval sprint — DONE (2026-10-17;
owner-authorized): batches 080–082 in
examples/math_p1_closure_phase22.py (build_graph_v42); three new KCs (57
total); coverage now 8/15/0; M-09/M-10 closed at implementation level;
M-15 data-representation component implemented; bounded retrieval sprint
executed (WAEC Math syllabus not located; NERDC SSS3 still unavailable;
JAMB cycle UNRESOLVED); no status promotions (PHASE22_REPORT.md).
Next: owner decision on P2 prioritization; continue WAEC official /
NERDC SSS 3 retrieval attempts (CI-24); Physics/Chemistry gap triage
available as a follow-on; Biology only after all three subjects are
sufficiently closed and the owner authorizes it.
Biology remains on hold (BIOLOGY_HOLD_RECORD.md).
