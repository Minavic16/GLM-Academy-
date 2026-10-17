# Owner Decision Brief — Phase 21: Mathematics Closure Strategy

Prepared: 2026-10-17 · Phase 21 ("Mathematics Closure Strategy and Owner
Decision Brief"; audit and decision-preparation only) · Baseline: commit
`63f4567` (Phase 20 close-out), working tree clean at audit start ·
Companion audit record: `docs/PHASE21_REPORT.md`

> **Status of this document: PROPOSAL.** Nothing in this brief is ratified,
> and no implementation or retrieval action is authorized by it. It is a
> decision-preparation document only. No canonical entity, claim, evidence,
> source, activity or relationship was changed in Phase 21. No subject is
> promoted; board verification remains governed by CI-24.

## 1. Executive recommendation

**Recommendation: Strategy C — implementation closure and evidence
retrieval as separate, coordinated workstreams — sequenced P1-first, with
the smallest useful next package = "Wave B (P1 closure)".**

1. **Implement first (smallest useful package):** close the three remaining
   P1-grade gaps — binary operations (JAMB II.5), loci & construction
   (JAMB III.3 + III.1(d)), representation of data (JAMB V.1). This
   converts the coverage matrix from `NOT_COVERED 3` to `NOT_COVERED 0`
   and is the single change that most strengthens the defensibility of a
   Mathematics implementation stopping point. It is dependency-free
   (official JAMB evidence already in hand), bounded (≈3 new KCs), and
   small–medium relative effort (Phase 17 delivered 5 KCs in one wave;
   Phase 20 delivered 10).
2. **Run retrieval in parallel (bounded):** WAEC official syllabus (a new
   official retrieval channel was identified this phase — waecnigeria.org
   publishes per-subject syllabus documents as article attachments; none
   exists for Mathematics yet), NERDC SSS3 (alternate access), JAMB
   applicable-cycle determination. Pre-accepted fallback: record "blocked"
   with a full attempt log; never substitute third-party mirrors; never
   promote a status.
3. **Do not expand now:** the 13 P2 depth rows stay registered.
   Recommendation for them: accept as *documented residuals* for the
   stopping point, and schedule a dedicated P2 prioritization brief only
   after Wave B lands. The ogive deferral stands.

One-line rationale: implementation closure must not be gated on a
verification channel that has failed across five consecutive phases
(16, 18, 19, 20, 21), while board verification (OD-01/OD-04) remains a
separate dimension and can stay open without blocking a defensible
implementation completion for a declared scope.

## 2. Verified current state (live audit)

**Repository / baseline**

- HEAD = `63f4567` ("Phase 20…"), working tree clean at audit start;
  prior `238056d` (Phase 19). No repository instruction files exist
  (no AGENTS.md/CONTRIBUTING; README defines no commit policy), so per the
  Phase 21 boundary no commit/push was performed; Phase 21 documents remain
  uncommitted working-tree changes.
- Canonical builder `build_graph_v41()` (Mathematics authority since
  Phase 20): **424 entities / 678 claims / 337 evidence / 86 sources /
  234 activities**; `run_store_validation(...) == []`; `dumps_store(...)`
  md5 `0d680026d67ff729a9501544aa312980` — identical to the Phase 20
  record.
- Mathematics KCs: **54** (live extraction). Physics 25 / Chemistry 21
  unchanged.
- Full test suite (re-run this phase): **199 passed, 0 failed**.
- Phase 20 report discrepancy check: **none found** — commit, store
  counts, md5, matrix counts (5/15/3) and the 199-test claim all match the
  live repository. Two audit notes (not contradictions): (a) register row
  M-15 is tagged P2 although its V.1 "representation" component is
  topic-level NOT_COVERED (classified P1-grade here; see §3); (b) the
  CI-24 wording "WAEC downloads are CASS installers only" remains true of
  the downloads page, but an additional official channel exists (article
  attachments — see §7).

**Coverage**

- Official JAMB matrix (23 topics): **COVERED 5 / PARTIALLY_COVERED 15 /
  NOT_COVERED 3**. The three NOT_COVERED topics: II.5 Binary Operations
  (p.3), III.3 Loci (p.4), V.1 Representation of Data (p.5). V.1's gap is
  folded into register row M-15 (statistics) in the live register; this
  audit splits it as M-15a (representation; P1) and M-15b (statistics
  depth; P2).
- Gap register M-01…M-29: closed at implementation level — M-01…M-08
  (with residuals tracked in M-22/M-26/M-28), M-19/M-20/M-21; partially
  extended — M-23. Remaining: 2 P1 rows (M-09, M-10) plus the M-15a
  component, 13 P2 rows, 2 WAEC-secondary-only rows (M-17/M-18), 1
  NERDC-only row (M-29), 1 standing deferral (ogive).

**Sources and limitations**

- JAMB official UTME E-syllabus (Math/Phys/Chem) retrieved Phase 18;
  Mathematics record `SRC.JAMB.UTME.MATH.2025`: official, authenticity
  established, sha256 `aff7a7c2…754f`, PDF revision 2025-07-31,
  **applicable cycle UNRESOLVED (no cycle year printed)**, local copy not
  committed.
- NERDC SSS1/SSS2 Mathematics content-checked (Phase 16); **NERDC SSS3 not
  obtained** (LMIS login-gated; `sss_3` 404; nerdc.org.ng HTTP 500).
- **WAEC official syllabus not obtained.** Phase 21 retrieval probes (all
  official-channel): site home, article index, news pagination, targeted
  searches — official syllabus documents are published as article
  attachments (only confirmed instance: Bookkeeping & Office Practice
  2022–2025 → `/sites/default/files/2024-06/BookKeeping%26OfficePractice.pdf`);
  no Mathematics syllabus article/attachment found.
- Secondary source (Syllabus NG) remains non-authoritative; used only for
  M-17/M-18 and historical comparisons.

## 3. Remaining gaps by priority and type

All rows below are live-verified (entity extraction + zero-hit probes
against `build_graph_v41`; see `docs/PHASE21_REPORT.md` §3–§4 for the full
9-field table).

**Group 1 — P1: required implementation gaps (official JAMB, no adequate
implementation) — proposed Wave B**

| ID | Topic | Locator | Live state | Proposed disposition |
|---|---|---|---|---|
| M-09 | Loci & construction | III.3 p.4; III.1(d) p.3 | 0 entities (loci/locus/bisect/construct) | Wave B |
| M-10 | Binary operations | II.5 p.3 | 0 entities | Wave B |
| M-15a | Representation of data: frequency distribution; histogram; bar chart; pie chart | V.1 p.5 | 0 entities (stats KCs cover location/dispersion only) | Wave B |

**Group 2 — P2: required depth gaps (extend existing families) — 13 rows**

M-11 perm/comb (V.4); M-12 coordinate-geometry depth (III.4); M-13 trig
depth incl. bearings (III.5); M-14 calculus depth (IV.1/IV.3); M-15b
statistics depth incl. mode/grouped (V.2–V.3, ogive inside); M-16
probability depth (V.5); M-22 sets depth (I.4.ii–iv); M-23 polynomial
depth residual (II.1.c–g); M-24 variation depth (II.2); M-25 inequalities
depth (II.3); M-26 progression sums (II.4.ii–iii); M-27 Euclidean geometry
depth (III.1.b–c); M-28 mensuration depth incl. spheres/earth (III.2).
Each is "small" individually; cluster-level medium. Proposed cluster order
if ever authorized: algebra (M-22/23/24/25/26) → geometry/trig
(M-12/13/27/28) → stats/prob (M-11/15b/16) → calculus (M-14).

**Group 3 — Evidence/verification blockers**

- CI-24 package: WAEC official syllabus (unobtained); NERDC SSS3
  (unobtained); JAMB applicable cycle (unresolved). See §7.
- M-07 note: matrices implementation adequate; implementation evidence
  remains secondary (Syllabus NG, Phase 17 provenance), disclosed; official
  requirement confirmed. Optional evidence upgrade in a later authorized
  wave.

**Group 4 — Secondary-source-only gaps (no official board source yet)**

- M-17 vectors arithmetic detail; M-18 transformations
  (reflection/rotation/translation). Both WAEC-mirror-only, no JAMB
  locator; implementation (M-18 none; M-17 partial) held pending official
  WAEC verification. P3.

**Group 5 — Optional depth extensions (do not block declared-scope
completion)**

- M-29 proofs of basic theorems (NERDC SSS2 p.11 official; no JAMB
  locator) — scope call.
- Phase 20 boundary-exclusions (modular division/inverses; absolute/
  relative error; compound interest/depreciation/discount) remain out of
  current scope; not registered gaps.

**Group 6 — Deferred by owner decision**

- Ogive (cumulative frequency curve; within M-15b / V.2): owner-documented
  deferral stands unless the owner reverses it (reversal would fold into
  any statistics wave).

Disposition completeness: every register row M-01…M-29 and every CI-24
item now carries one of — closed at implementation level, Wave B (P1),
documented residual (P2), evidence-blocked (P3 retrieval), scope call, or
deferred. No gap is left without a traceable disposition. (Full table:
`docs/PHASE21_REPORT.md` §3.)

## 4. Strategy comparison

| Criterion | A — P1 implementation first | B — official-source retrieval first | C — coordinated (recommended) |
|---|---|---|---|
| Examination relevance | High: 3 official topics currently absent (loci/construction, binary operations, data representation are standard examinable items) | Indirect: no content change | High (as A) |
| Educational completeness | Closes all topic-level NOT_COVERED; P2 still partial | No change | Closes NOT_COVERED; evidence advances |
| Evidence quality | JAMB-official already present for all three P1s; no new evidence blocked | Highest potential gain (WAEC official; SSS3; cycle) | Both |
| Dependencies / effort | None; small–medium | None; small, but success probability low — failed official retrieval in five consecutive phases (16/18/19/20/21); only new lead is the attachment channel | None; small–medium total |
| Scope-expansion risk | Low: bounded, 3 families | None | Low |
| Defensible completion | Strong step toward a complete JAMB-topic claim; board verification still open (disclosed) | Cannot reach defensible completion alone (implementation gaps remain); zero-progress risk | Strongest overall |

**Recommendation: C, sequenced P1-first.** Repository evidence for this
ordering:

1. The P1 gaps are fully specified by the official JAMB document already
   in hand and need no further evidence to implement (M-09/M-10/M-15a
   already carry official locators).
2. Retrieval cannot be a dependency: every formal attempt since Phase 16
   has failed to obtain WAEC official or NERDC SSS3; the Phase 21 sprint
   adds a concrete new channel but no obtained document. Blocking
   implementation on it would risk indefinite zero progress.
3. OD-01/OD-04 already separate implementation from board verification,
   so an implementation stopping point can be declared (with disclosure)
   while CI-24 stays open.
4. The smallest useful package is Wave B; it is bounded, reviewable, and
   turns "3 official topics missing" into "0" — the key quantitative
   defensibility gain.

## 5. Recommended next work package

**Wave B — P1 closure (implementation) + bounded retrieval sprint
(evidence).**

| | Content |
|---|---|
| Entry criteria | Owner authorization (D1 for implementation, D3 for the sprint); baseline re-verified; boundaries unchanged (no Physics/Chemistry/Biology/English; no schema or claim-restriction changes; builder-only workflow; no hand edits of generated files) |
| Deliverables | Implementation: new batches (080+) implementing M-09 (loci KC + construction methods/items), M-10 (binary-operations KC/methods/items), M-15a (data-representation KC/methods/items) with JAMB-evidence chains; coverage-matrix rows II.5/III.3/V.1 → COVERED; register rows updated only as authorized; new regression tests. Evidence: retrieval addendum recording the WAEC attachment-channel sweep + official-request route, NERDC SSS3 alternate access, JAMB cycle check |
| Acceptance criteria | `run_store_validation == []`; full suite green (≥199 + new tests); deterministic generation double-run stable; `NOT_COVERED = 0`; no unexpected diffs; retrieval outcome recorded as either "obtained (hash + content check)" or "blocked (full attempt log)" |
| Stop conditions | Any sub-scope ambiguity in the official text → record residual and stop (no scope creep inside the wave); retrieval action list exhausted → record blocked and stop (no third-party substitution; no status promotion) |

Phased plan (each later step requires its own owner decision):

| Step | Entry | Deliverables | Acceptance | Stop |
|---|---|---|---|---|
| 0. Phase 21 audit (this) | — | this brief + `docs/PHASE21_REPORT.md` | phase exit checklist met | — |
| 1. Wave B + retrieval sprint | D1/D3 authorization | batches 080+, matrix/register updates, tests, retrieval addendum | as above | as above |
| 2. P2 prioritization brief (+ optional depth waves) | Step 1 landed + owner decision (D2) | prioritization brief; cluster waves only if authorized | every P2 row has a ratified disposition | no authorization → documented residuals stand |
| 3. Board-verification closure (CI-24) | WAEC official + SSS3 obtained (or limitation formally accepted) | board-verification package; promotions only on checked content | CI-24 criteria | retrieval blocked → status quo, disclosed |

## 6. Proposed Mathematics closure criteria (for ratification — D4)

Existing status meanings are **not** redefined by this brief. The
following criteria are **proposed**; item 1 contains a proposed scope
extension that requires explicit owner approval. **[M]** = mandatory,
**[O]** = optional extension.

1. **IMPLEMENTATION_COMPLETE (declared Mathematics scope)** — proposal:
   after Wave B, the declared scope is "all 23 official JAMB Mathematics
   topics implemented, P1 = 0". Completion requires: store validation
   `[]`; full suite green; deterministic generation; every topic ≥
   PARTIALLY_COVERED with an owner-ratified disposition; all deferrals
   documented. The current narrower meaning remains in force unless the
   owner approves this extension **[M — flagged for approval; must not be
   applied silently]**.
2. **All P1 gaps closed** — M-09, M-10, M-15a implemented with
   official-JAMB locators, evidence attached, matrix rows COVERED, register
   rows moved to no-action **[M for the full-topic-coverage claim]**.
3. **P2 gaps resolved or formally dispositioned** — every P2 row carries
   an owner-ratified disposition: accepted documented residual
   (PARTIALLY_COVERED acknowledged) or scheduled wave. Closing them is
   **[O]**; having dispositions for all of them is **[M]**.
4. **Official JAMB reconciliation** — record-level reconciliation
   maintained and re-run after any future store change; cycle
   applicability resolved from an official artifact or formally accepted
   as a documented limitation **[M — met at Phase 19/20; maintenance duty;
   cycle caveat item]**.
5. **Official WAEC verification** — official WASSCE General Mathematics
   syllabus obtained (hash + authenticity + content check) and mapped,
   including M-17/M-18 resolution **[M for BOARD_VERIFIED; O for
   implementation closure]**.
6. **NERDC SSS1–SSS3 verification** — SSS1/SSS2 mapping exists (met);
   SSS3 obtained and content-checked, with SSS3-only requirements assessed
   **[M for NERDC-complete claims; O for JAMB-side implementation closure —
   disclose the SSS3 gap otherwise]**.
7. **Final regression / determinism / canonical-store validation** — full
   suite green; `run_store_validation == []`; JSON export identical to
   builder output; generators double-run byte-stable; no unintended file
   changes **[M]**.

Status semantics unchanged: board verification remains governed by CI-24;
nothing promotes to BOARD_VERIFIED; `indicates` remains PROPOSED.

## 7. Outstanding evidence-retrieval blockers

| Blocker | Exact missing evidence | Most direct action (official channels only) | Closure criteria |
|---|---|---|---|
| WAEC official syllabus | WASSCE General Mathematics / Mathematics (Core) syllabus document (current cycle) from WAEC | Sweep the waecnigeria.org article/attachment channel for a Mathematics syllabus (channel confirmed to host syllabus documents: Bookkeeping 2022–2025 attachment); official request for the published "Regulations & Syllabuses" compilation / subject syllabuses; monitor the article index | Document obtained from waecnigeria.org or another official WAEC channel; hash + authenticity + content check recorded; mappings produced |
| NERDC SSS3 | NERDC SSS3 Mathematics curriculum | LMIS registered-access path or official request; re-check nerdc.org.ng (HTTP 500 this phase); alternate official NERDC/FME publication route | Document obtained and content-checked; SSS3-only content assessed |
| JAMB applicable cycle | Cycle/session marker for the IBASS E-syllabus revision in use (no year printed; metadata 2025-07-31) | Check official JAMB artifacts (IBASS metadata/brochure, announcement circulars) | Cycle established from an official artifact, or the limitation formally accepted by the owner (documented) |
| M-07 evidence provenance | Official-side evidence for matrices rows (currently secondary, Phase 17 provenance) | Re-source evidence in a later authorized wave (documentation-only option already recorded) | Evidence re-sourced, or the disclosed note formally accepted |

Phase 21 retrieval statement: none of the above was obtained this phase;
no third-party source was substituted; no status was promoted.

## 8. Decisions required from the owner

| ID | Decision | Options | Recommended default | If approved | If declined / deferred |
|---|---|---|---|---|---|
| D1 | Authorize Wave B (P1 closure) | Authorize / defer / broaden (not recommended) | **Authorize** | M-09/M-10/M-15a implemented; NOT_COVERED → 0; stopping point strengthened | NOT_COVERED stays 3; any completion claim must disclose three official topics as unimplemented |
| D2 | P2 depth policy | (a) documented residuals + prioritization brief after Wave B / (b) schedule depth waves now / (c) close all P2 before any closure claim (not recommended) | **(a)** | P2 rows carry ratified "accepted residual" status; deeper closure stays available later | (b) starts a larger program (4 clusters, medium each; per-wave authorization retained); (c) large, open-ended |
| D3 | Bounded retrieval sprint + blocked-outcome fallback | Authorize / defer | **Authorize** | Sprint runs in the next package; "blocked" pre-accepted as a legitimate outcome; no promotions | CI-24 status quo; WAEC/SSS3 criteria stay open indefinitely |
| D4 | Ratify closure criteria (§6), incl. the proposed declared-scope extension | Approve / amend / return to draft | **Approve** | §6 becomes the ratified closure framework (scope extension via D1 + D4) | Status semantics unchanged; nothing in §6 takes effect |

Decision principle applied: the smallest set that (i) authorizes exactly
one bounded implementation package, (ii) fixes a depth policy without
authorizing depth work, (iii) keeps verification moving without gating
anything on it, and (iv) settles the closure standard before it is needed.

## 9. Explicitly deferred work

- P2 depth waves for all 13 rows (order proposal in §3; pending D2; no
  authorization now).
- Ogive (owner-documented deferral; reversal optional, folds into a
  statistics wave).
- M-17 / M-18 implementation (gated on official WAEC verification).
- M-29 proofs (NERDC-only scope call; no JAMB locator).
- M-07 evidence upgrade (optional; no canonical change now).
- Phase 20 boundary-exclusions (modular inverses; absolute/relative error;
  compound interest/depreciation/discount).
- CI-11/CI-12 Chemistry buffers; Physics/Chemistry gap triage; Biology
  hold (OD-05) — untouched by this brief.

## 10. Resolution note (added Phase 22, 2026-10-17)

The owner's Phase 22 authorization executed this brief's package (full
record: `docs/PHASE22_REPORT.md`):

- **D1 — approved as recommended**: Wave B (P1 closure) authorized and
  implemented as batches 080–082 (build_graph_v42,
  `examples/math_p1_closure_phase22.py`). M-09/M-10 closed at
  implementation level; the M-15 data-representation component (audit
  split M-15a) implemented; official JAMB counts now COVERED 8 /
  PARTIALLY_COVERED 15 / NOT_COVERED 0.
- **D2 — policy (a) applied**: the declared target (all 23 official JAMB
  topics implemented at topic level, with residual depth documented and
  prioritized separately) matches the documented-residuals option; the 13
  P2 rows remain registered and unauthorized as a wave, with
  prioritization available for a future owner decision.
- **D3 — approved and executed**: bounded retrieval sprint run this phase
  on official channels only (probe log in `docs/PHASE22_REPORT.md` §5).
  Outcomes: WAEC official Mathematics syllabus NOT OBTAINED; NERDC SSS 3
  NOT OBTAINED; JAMB applicable cycle UNRESOLVED. Blocked outcomes
  accepted per the pre-agreed fallback; no third-party substitution; no
  promotions.
- **D4 — criteria operative in substance**: the Phase 22 instruction fixed
  the declared 23-topic target and the documented-residuals presentation;
  §6 is treated as the operative closure framework for Mathematics
  (criteria 1–3 and 5–7 semantics preserved), subject to any owner
  amendment. Status semantics unchanged: CI-24 governs board
  verification; nothing promoted to BOARD_VERIFIED.
