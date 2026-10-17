# Phase 13.8 Roadmap — Mathematics, Physics, Chemistry

Statuses under ratified model (OD-01/OD-04):

## MATHEMATICS — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED (scope expanded Phase 17)
Completed: 44 KCs (39 baseline + 5 in Phase 17 batches 066-069), full-chains
validated, CI-01/CI-02 closed (median + dispersion with preserved legacy ids),
kc.logarithms (b055) enables Chemistry pH; log→pH edge cl.pre56.log_ph
ACCEPTED and intact.

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
2. NOT_COVERED rows requiring owner scope decisions: Modular Arithmetic,
   Approximation, Surds, Bearings, Proofs of Some Basic Theorems,
   Construction, Ogive (documented deferral). Matrices & determinants
   implemented on secondary evidence; the JAMB requirement is now officially
   confirmed (Phase 18, JAMB II.6) — implementation evidence remains
   secondary (Syllabus NG): disclosed, no implementation change.
Tests for closure: full suite ≥ current, store `[]`, coverage matrix rows
all COVERED-or-excluded with evidence refs.
Next task: M-1 official-source verification continues — JAMB DONE for Math
(Phase 18); WAEC official documents and NERDC SSS 3 still outstanding. Then
owner decisions on remaining NOT_COVERED rows (Modular Arithmetic,
Approximation, Surds, Bearings, Proofs, Construction, Ogive) plus the
Phase 18 depth exposures (Venn/cardinality; factor/remainder theorems;
graphical/quadratic inequalities; GP sums; earth-as-sphere; bearings/graphs;
limits; area under curve; grouped dispersion; data representation). Biology
remains on hold.

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
Next: WAEC official WASSCE syllabus retrieval; NERDC SSS 3 attempt; owner
decisions on register gaps (M-*, P-*, C-* incl. Phase 18 exposures); then
Biology only after all three subjects are sufficiently closed and the owner
authorizes it.
Biology remains on hold (BIOLOGY_HOLD_RECORD.md).
