# Phase 13.7 Governance Audit — Owner Decisions and Subject Closure Gates

Date: 2026-10-15. Baseline: `2190cf6`, 117 tests pass, store `[]`.
No Biology work. No schema/relation changes. No promotions.

## OD-01 — Subject Completion Standard v1.0 (OPEN)

Review of `SUBJECT_COMPLETION_STANDARD.md` against required dimensions:
curriculum coverage ✓, KC/prerequisite completeness ✓, TM/Method/practical
coverage ✓, evidence/source requirements ✓, board verification ✓ (Clause F),
partial/deferred treatment ✓ (F statuses), tests/validation ✓ (Clause D),
provenance/legacy-id preservation — **was implicit only** → editorial
addition below, authority-to-approve — **was missing** → added below.
No policy content changed; standard remains **PROPOSED**.

Editorial additions made (non-policy): Clause E bullet "Provenance and legacy
identifiers must survive all migrations/corrections (PROVIDANCE_BROKEN is a
Clause E violation)" and Clause G "Authority: only the project owner may
declare a subject COMPLETE; an agent may only record evidence".
Decision required: approve v1.1 as written. Options: (a) approve — subjects
become gate-able; (b) amend specific clauses; (c) reject. Consequence of
leaving open: no subject may be marked COMPLETE; only PARTIALLY_COMPLETE
statuses are usable.

## OD-02 — 12-vs-13 entity count (OPEN, evidence CONFIRMED)

Evidence chain (all from repository, not memory):
1. Task brief froze 13 entity names including `Subject`.
2. `GLM_CDG_v0.2_Contract_Sanity_Check.md` §11 says "the 12 frozen entities";
   §12 says re-admitting EvidenceRule would make "a thirteenth entity" ⇒ the
   sanity-check's 12 = brief's 13 **minus `Subject`**; EvidenceRule would
   number 13 in the sanity convention.
3. `cdg/enums.py` implements exactly 13 values (verified below).
Resolution proposal: frozen core = 12 domain entities; `Subject` is
infrastructure added in Phase 12 for multi-subject identity (additive, no
domain-semantic change). Regression test `test_entity_type_count_frozen`
locks the implemented count at 13 with this convention documented. Owner
confirmation still required; no entity added/removed to force the count.

## OD-03 — `indicates` (OPEN; behavior unchanged)

Intended semantics (per sanity check + implemented validator): diagnostic
relation Item → Misconception | KC; requires `response_pattern`; `polarity`
required when target is KC. Distinguishing points vs existing relations:
`requires`/`prerequisite`/`targets` are CDG dependency semantics; `indicates`
is assessment-diagnostics semantics, hence the sign-off gate. Current usage:
exactly 1 claim (`cl.it.indicates`, PROPOSED, mandated unchanged) — conforms.
No broadening, no promotion. Decision required: approve current domain/range
or re-admit `EvidenceRule` as a 13th entity (which would interact with OD-02).
Consequence of leaving open: diagnostic modeling stays blocked; every new
`indicates` remains PROPOSED.

## OD-04 — Qualified-scope sign-off (OPEN)

Options assessed:
1. Strict closure — board PDFs mandatory. Blocks all completion; cannot be
   satisfied in current network conditions (below).
2. Qualified closure — implementation complete, alignment unverified. Risk:
   "complete" read as "board-verified" unless explicitly labeled.
3. Separate status dimensions — implementation completeness vs official
   verification tracked independently.

**Recommended: Option 3.** It matches the freeze-avoidance standard
(Clause F already separates per-requirement verification) and the CDG model
(Claim.status is about the claim's lifecycle, not board verification;
`Source.tier` and `inherited_from_legacy` already carry provenance authority).
Minimal representation: no schema change needed — verification dimension is
recorded in `CLOSURE_REGISTERS.md` per subject (implemented below). If the
owner wants it in the model later, the smallest change would be a
`verification` attribute on Source/claim-class records — NOT implemented
without authorization.

Mathematics test case: CI-01/CI-02 closed at implementation level →
Mathematics = "IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED" under Option 3;
NOT COMPLETE. Physics/Chemistry likewise carry PARTIAL + BOARD_UNVERIFIED.

## OD-05 — Biology start (BLOCKED)

Blocking decisions: OD-01 (standard unapproved ⇒ no completion gate exists)
and OD-05 itself (explicit authorization missing). CI-08/CI-09 deferrals do
not block a *research* phase, but per Phase 13.5, Biology needs an owner
exception even for research. Status: BLOCKED; authorization request on file.

## Official source attempts (2026-10-14, narrow scope, recorded)
JAMB IBASS: HTTP 200, JS SPA with hashed syllabus assets — no per-subject PDF
URL discoverable from bundle (re-attempted; unchanged). WAEC: 200, syllabus
documents not linked from landing HTML. NERDC: unreachable (000). Result:
OFFICIAL_VERIFICATION_GAP remains open for all three subjects. No secondary
source used to claim board alignment.

## Subject closure assessment (Option 3 vocabulary)

| Subject | Implementation | Board verification | Owner actions | Permitted next action |
|---|---|---|---|---|
| Mathematics | IMPLEMENTATION_COMPLETE (39 KCs; CI-01/02 closed; chains validated) | UNVERIFIED | OD-01, OD-02, OD-04 | Physics/Chemistry-style optional batches only for NEW evidence |
| Physics | PARTIAL (19 KCs; fibre/LASER/electronics deferred) | UNVERIFIED | OD-01, OD-04 | Continue Physics SHOULD-rows |
| Chemistry | PARTIAL (12 KCs; buffers/polymers/industrial deferred) | UNVERIFIED | OD-01, OD-04 | Continue Chemistry deferred families |

Math verification spot-checks required by the audit (all pass):
`kc.median_ungrouped` legacy id `MATH.STAT.MEDIAN` preserved;
`kc.measures_of_dispersion` legacy ids RANGE/MEAN_DEVIATION/VARIANCE/
STANDARD_DEVIATION preserved; quartile/IQR documented as PARTIAL row in
`PHASE136_COVERAGE_MATRIX.md`; `cl.pre56.log_ph` edge intact.
