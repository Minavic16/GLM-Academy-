# Phase 21 Report — Mathematics Closure Strategy and Owner Decision Brief

Date: 2026-10-17 · Phase: 21 ("Mathematics Closure Strategy and Owner
Decision Brief") · Type: **audit and decision preparation only — no
canonical changes** · Baseline: commit `63f4567` (Phase 20 close-out) ·
Companion owner-facing document:
`docs/architecture/OWNER_DECISION_BRIEF_PHASE21.md`

## 1. Purpose and boundary

Inspect the completed Phase 20 CDG implementation, classify every
remaining Mathematics gap against the live canonical graph and the 23
official JAMB Mathematics topics, separate implementation closure from
board verification, compare closure strategies, and prepare an
evidence-backed owner decision brief. No new curriculum content, no
canonical entity/claim/evidence/source/activity/relationship changes, no
status promotions, no Biology/English, no Physics/Chemistry work.
Documentation-only outputs; no commit/push (no repository instruction
requires it for documentation-only phases).

## 2. Baseline verification (live)

- HEAD = `63f4567` ("Phase 20…"); working tree clean at audit start; prior
  `238056d` (Phase 19). No repository instruction files exist (no
  AGENTS.md/CONTRIBUTING; README defines no commit policy) — recorded as
  the basis for the no-commit boundary.
- Canonical builder `build_graph_v41()` (sole authority for Mathematics
  since Phase 20): **424 entities / 678 claims / 337 evidence / 86
  sources / 234 activities**; `run_store_validation(...) == []`;
  `dumps_store(...)` md5 `0d680026d67ff729a9501544aa312980` — identical to
  the Phase 20 record. Mathematics KCs: **54** (live extraction by id).
- Full regression suite re-run twice this phase (before and after the
  documentation edits): **199 passed, 0 failed** (58 custom-mark
  warnings).
- Phase 20 report discrepancy check: **none found** — commit, store
  counts, md5, coverage counts (5/15/3), and the 199-test claim in
  `docs/PHASE20_REPORT.md` all match the live repository.
  Audit notes (not contradictions):
  - **N-1**: register row M-15 (statistics) is tagged P2, but its V.1
    "representation of data" component is topic-level NOT_COVERED in the
    official matrix — P1-grade under the Phase 21 classification. This
    report splits it as **M-15a** (representation; P1) and **M-15b**
    (statistics depth; P2). Audit-level split only; the register was not
    rewritten.
  - **N-2**: CI-24 states "WAEC not obtained (downloads are CASS
    installers only)". Still true of the downloads page, but Phase 21
    identified an additional official channel: waecnigeria.org publishes
    per-subject syllabus documents as article attachments (confirmed
    instance: Bookkeeping & Office Practice 2022–2025). No Mathematics
    syllabus article/attachment exists on that channel as of this audit.
- Coverage matrix (official JAMB, 23 topics): **COVERED 5 /
  PARTIALLY_COVERED 15 / NOT_COVERED 3** (II.5 Binary Operations p.3;
  III.3 Loci p.4; V.1 Representation of Data p.5).
- Source records (inventory): JAMB official Math/Phys/Chem + IBASS
  attempt record; NERDC SSS1/SSS2 Math/Phys/Chem; Syllabus NG secondary
  (JAMB/WAEC Math); WAEC attempt record; NERDC portal attempt record;
  FEDMOE curriculum-offerings record. **No WAEC official syllabus; no
  NERDC SSS3.** JAMB Mathematics record limits: sha256 `aff7a7c2…754f`,
  revision 2025-07-31, **applicable cycle UNRESOLVED**, local copy not
  committed.

## 3. Method

- Live extraction from `build_graph_v41` (entity counts; the 54
  Mathematics KCs by id; the 96 TMs with their `hasMethod` chains; all
  37 Mathematics-subject TMs carry explicit chains).
- Zero-hit probes for each un-implemented family over entity `id` +
  `label` (structural check, then entity-type/subject verification before
  any absence claim). Substring false positives were identified and
  excluded, e.g.: "loci" ⊂ "ve**loci**ty" (Physics motion graphs); "mode"
  ⊂ "**mode**rn/atomic model"; "reflection" hits = Physics optics;
  "construct" hit = a Physics motion-graph label; "pie" ⊂ "enthal**pie**"
  (enthalpy). After filtering: 0 Mathematics hits for loci/locus/bisect,
  binary, histogram/bar/pie/frequency distribution/ogive/cumulative,
  remainder/factor theorem/cubic, limit, bearing/elevation/depression,
  cyclic/chord, sphere/earth/longitude, midpoint/two-point, inverse/joint/
  partial variation, graphical/quadratic inequality, sum of/infinity,
  permutation/combination/circular, experimental/mutually exclusive/
  independent, Venn/cardinality/disjoint, transformation/reflection/
  rotation/translation, proof.
- Register-vs-graph cross-check: chain claims in
  `MATHEMATICS_GAP_REGISTER.md` and `JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md`
  were re-verified against live chains (all consistent; no register row
  claims an entity that is absent, and no gap row claims coverage that a
  live chain contradicts).
- Observation (no action taken): pre-Phase-16 Mathematics TMs carry
  `subject=None` while Phase 16–20 additions carry
  `subject="Mathematics"` (37 TMs). Live extraction must not rely on the
  subject attribute alone; not a gap, not changed in this phase.

## 4. Gap classification (M-01…M-29, live-verified)

Groups: **1** P1 required implementation; **2** P2 required depth;
**3** evidence/verification blockers; **4** secondary-source-only;
**5** optional depth; **6** deferred. Effort: S = small, S–M =
small–medium, M = medium (grounded against Phase 17: 5 KCs per wave ≈
medium; Phase 20: 10 KCs ≈ medium–large).

| ID | Topic | Locator | Evidence | Existing implementation (live) | Remaining work | Dependencies | Effort | Proposed disposition |
|---|---|---|---|---|---|---|---|---|
| M-09 | Loci & construction | JAMB III.3 p.4; III.1(d) p.3 | JAMB OFFICIAL (both); NERDC SSS2 p.14 construction NOT_COVERED; loci not in NERDC SS1/2 lists | None — 0 live hits (loci/locus/bisect/construct) | Loci KC + construction methods/items | None | S–M | **Wave B (P1)** — D1 |
| M-10 | Binary operations | JAMB II.5 p.3 | JAMB OFFICIAL; secondary mirror topic 17(iii); not in NERDC SS1/2 lists | None — 0 live hits | Closure/commutativity/associativity/distributivity; identity/inverse KC + methods + items | None | S | **Wave B (P1)** — D1 |
| M-15a | Representation of data (frequency distribution; histogram; bar chart; pie chart) | JAMB V.1 p.5 | JAMB OFFICIAL; NERDC SSS1 p.12 partial | None for representation; statistics KCs cover location/dispersion only | Data-representation KC + methods + items | None | S–M | **Wave B (P1)** — D1 (split from M-15; see N-1) |
| M-15b | Statistics depth (mode; grouped location/dispersion; cumulative frequency) | JAMB V.2–V.3 p.5 | JAMB OFFICIAL; NERDC SSS2 pp.16–19 (ogive NOT_COVERED, deferral documented) | kc.mean_ungrouped_data → tm.compute_mean {m.sum_divide_count}; kc.median_ungrouped → tm.compute_median {m.median_ordered, m.quartile_from_ordered}; kc.measures_of_dispersion → tm.compute_dispersion {m.range, m.variance_sd} | Mode (0 hits); grouped-data location/dispersion; cumulative frequency (ogive deferred) | Ogive gate = owner reversal | S–M | Documented residual (P2) — D2; ogive deferred (group 6) |
| M-11 | Permutation & combination | JAMB V.4 p.5 | JAMB OFFICIAL; not separately in NERDC SS1/2 lists | kc.counting_principle → tm.count_outcomes {m.multiply_choices} | Formulas; circular; repeated-object arrangements | None | S | Documented residual (P2) — D2 |
| M-12 | Coordinate geometry depth | JAMB III.4 p.4 | JAMB OFFICIAL; not explicitly in NERDC SS1/2 lists | kc.distance_formula → tm.compute_distance {m.distance_formula}; kc.gradient → tm.compute_gradient {m.gradient_from_two_points}; kc.equation_of_line → tm.find_line_equation {m.point_gradient}; kc.parallel_perpendicular_lines → tm.classify_line_relationships {m.compare_gradients} | Midpoint; two-point form; general form | None | S | Documented residual (P2) — D2 |
| M-13 | Trig applications depth | JAMB III.5 pp.4–5 | JAMB OFFICIAL; NERDC SSS2 p.10 bearings NOT_COVERED | kc.trig_ratios_acute → tm.trig_ratio_problems {m.label_sides_match_ratio}; kc.special_angle_values → tm.recall_special_values {m.from_special_triangles}; kc.sine_rule + kc.cosine_rule → tm.solve_oblique_triangle {m.sine_rule, m.cosine_rule} | Angles −360°…360°; 75/105/135; elevation/depression; bearings; triangle areas; sine/cosine graphs | None | S–M | Documented residual (P2) — D2 (geometry/trig cluster) |
| M-14 | Calculus depth | JAMB IV.1 p.5; IV.3 p.5 | JAMB OFFICIAL | kc.differentiation_algebraic → tm.differentiate_explicit {m.power_rule}; kc.integration_algebraic → tm.integrate_polynomial {m.reverse_power_rule} | Limits; trig derivatives; trig integration; area under curve | None | S | Documented residual (P2) — D2 |
| M-16 | Probability depth | JAMB V.5 p.5 | JAMB OFFICIAL; NERDC SSS2 p.15 topic row COVERED | kc.theoretical_probability → tm.compute_probability {m.favourable_over_total} | Experimental probability; addition/multiplication rules; mutually exclusive/independent | None | S | Documented residual (P2) — D2 |
| M-22 | Sets depth | JAMB I.4 ii–iv p.2 | JAMB OFFICIAL; NERDC SSS1 p.7 | kc.sets_operations → tm.set_operations {m.set_notation, m.set_operations} | Cardinality; Venn ≤3 sets; disjoint/finite types; symbol problems | None (residual of M-01) | S | Documented residual (P2) — D2 |
| M-23 | Polynomials depth (remaining) | JAMB II.1 c–g ii–vi pp.2–3 | JAMB OFFICIAL; NERDC quadratic rows COVERED, cubic/theorem rows not evidenced | Phase 20 partial: kc.factorisation_patterns → tm.factorise_common_patterns {m.common_factor_extraction, m.difference_of_two_squares}; kc.change_of_subject (+ m.subject_powers_roots); quadratic KCs/chains | Factor & remainder theorems; cubic factorisation; polynomial division; polynomial graphs; defined/undefined; degree-3 roots | None | S–M | Documented residual (P2) — D2 (Phase 20 partially extended) |
| M-24 | Variation depth | JAMB II.2 p.3 | JAMB OFFICIAL; NERDC SSS1 variation row partial | kc.direct_variation → tm.direct_variation_problems {m.find_constant} | Inverse/joint/partial variation; percentage-change problems | None | S | Documented residual (P2) — D2 |
| M-25 | Inequalities depth | JAMB II.3 a–b p.3 | JAMB OFFICIAL; NERDC SSS2 p.8 | kc.linear_inequalities_analytic → tm.solve_linear_inequality {m.balance_inverse, m.test_graph} | Graphical region solutions; quadratic inequalities | Quadratic-roots KCs exist | S | Documented residual (P2) — D2 |
| M-26 | Progression depth | JAMB II.4 ii–iii p.3 | JAMB OFFICIAL; NERDC SSS2 p.1 (sums not evidenced) | kc.sequences_series → tm.sequences_series {m.ap_gp_nth_term, m.ap_gp_problems} | Sum of AP/GP; sum to infinity | None (residual of M-06) | S | Documented residual (P2) — D2 |
| M-27 | Euclidean geometry depth | JAMB III.1 b–c ii–iii p.3 | JAMB OFFICIAL; NERDC SSS2 p.12 Chord Properties partial | kc.parallel_line_angles → tm.identify_parallel_line_angles {m.corresponding_alternate}; kc.triangle_angle_properties → tm.triangle_angle_problems {m.triangle_angle_sum, m.exterior_angle}; kc.circle_angle_theorems → tm.circle_angle_problems {m.centre_vs_circumference} | Polygons; cyclic quadrilaterals; intersecting chords | None | S–M | Documented residual (P2) — D2 |
| M-28 | Mensuration depth | JAMB III.2 a–e i–iv p.4 | JAMB OFFICIAL; NERDC SSS1 p.11 (arcs/sectors/solids only) | kc.mensuration → tm.mensuration {m.circle_mensuration, m.solid_mensuration} | Chords; plane-figure/composite areas; spheres; earth-as-sphere | None (residual of M-08) | S–M | Documented residual (P2) — D2 |
| M-17 | Vectors arithmetic detail | No JAMB locator (not in official list) | WAEC-secondary-only (official unretrieved); NERDC SS1/2 lists exclude | kc.scalar_vector_quantities (partial; arithmetic detail not evidenced) | Vector arithmetic detail per WAEC syllabus | WAEC official retrieval (CI-24) | S + evidence | Evidence-gated hold (P3) — group 4 |
| M-18 | Transformations | No JAMB locator | WAEC-secondary-only (official unretrieved) | None — 0 Math hits (reflection hits are Physics optics) | Reflection/rotation/translation representation | WAEC official retrieval (CI-24) | S + evidence | Evidence-gated hold (P3) — group 4 |
| M-29 | Proofs of basic theorems | NERDC SSS2 p.11 only | NERDC OFFICIAL; no JAMB locator | None — 0 hits | Proof-oriented representation | Scope call (no technical blocker) | M | Optional/scope call (group 5) |
| M-07 | Matrices evidence provenance | JAMB II.6 p.3 | JAMB OFFICIAL (requirement); implementation evidence SECONDARY (Syllabus NG, Phase 17) | kc.matrix_algebra → tm.matrix_algebra {m.matrix_operations, m.determinants_inverses} | None (assessment-depth note recorded) | Evidence upgrade optional | S (evidence/docs only) | Disclosed note; optional upgrade (group 3) |
| Ogive | Cumulative frequency curve | JAMB V.2 p.5 (within M-15b) | JAMB OFFICIAL | None — 0 hits | Deferred by owner decision | Owner reversal option | S | **Deferred (group 6) — stand** |

Closed rows (not gaps; listed for completeness): M-01, M-02, M-03, M-04,
M-05, M-06, M-07 (implementation), M-08, M-19, M-20, M-21 — closed at
implementation level in Phases 17/20 with residuals tracked in M-22/M-26/
M-28 and M-23. Disposition completeness: **every M-row and every CI-24
item carries a traceable disposition or an explicit unresolved
(evidence-gated) status — none is left unclassified.**

## 5. Implementation closure vs board verification (OD-01/OD-04 preserved)

**Workstream A — Mathematics implementation.**

- Remaining uncovered JAMB topics: II.5 Binary Operations, III.3 Loci,
  V.1 Representation of Data — all three are P1, dependency-free, and
  fully specified by the official JAMB document already in hand.
- Remaining JAMB learning-objective depth gaps: the 13 P2 rows in §4
  (plus ogive standing deferred). Each extends an existing family whose
  live chains are verified above.
- Declared-scope sufficiency: the current declared scope (expanded Phase
  17/20) does not include the three P1 topics. With Wave B implemented,
  a defensible declared scope becomes "all 23 official JAMB Mathematics
  topics implemented, P1 = 0" — flagged as a proposed scope extension
  requiring owner approval (brief §6 item 1; D4).
- Defensible stopping point: recommended = after Wave B, with P2 rows
  owner-dispositioned as documented residuals, deferrals documented, and
  validation/tests/determinism green. Fallback if Wave B is not
  authorized: the current narrower scope with the three official topics
  explicitly disclosed as unimplemented.

**Workstream B — official-source verification (CI-24: OPEN; unchanged).**

| Blocker | Exact missing evidence | Most direct action (official only) | Closure criteria |
|---|---|---|---|
| WAEC official syllabus | WASSCE General Mathematics / Mathematics (Core) syllabus document (current cycle) | Sweep waecnigeria.org article/attachment channel for a Mathematics syllabus (channel confirmed: Bookkeeping 2022–2025 attachment); official request for the "Regulations & Syllabuses" compilation / subject syllabuses; monitor article index | Document obtained from waecnigeria.org or another official WAEC channel; hash + authenticity + content check; mappings |
| NERDC SSS3 | NERDC SSS3 Mathematics curriculum | LMIS registered-access path or official request; re-check nerdc.org.ng; alternate official NERDC/FME route | Obtained + content-checked; SSS3-only content assessed |
| JAMB applicable cycle | Cycle/session marker for the IBASS E-syllabus revision (no year printed; metadata 2025-07-31) | Official JAMB artifacts (IBASS metadata/brochure, circulars) | Cycle established or limitation formally accepted (documented) |
| M-07 provenance | Official-side evidence for matrices rows | Re-source in a later authorized wave (documentation-only note already recorded) | Re-sourced or note formally accepted |

No retrieval was claimed this phase; no third-party source was
substituted; no status was promoted.

## 6. Strategy comparison and recommendation

| Criterion | A — P1 first | B — retrieval first | C — coordinated |
|---|---|---|---|
| Examination relevance | High (3 official topics absent) | Indirect | High |
| Educational completeness | NOT_COVERED → 0 | No change | As A + evidence advance |
| Evidence quality | Unchanged (JAMB official already present) | High potential, low success probability (five failed phases) | Both |
| Dependencies / effort | None; S–M | None; S expected but likely blocked | None; S–M |
| Scope-expansion risk | Low | None | Low |
| Defensible completion | Strong step; board still open | Cannot complete alone | Strongest |

**Recommendation: Strategy C, sequenced P1-first.** The smallest useful
next work package is **Wave B — P1 closure** (binary operations; loci &
construction; representation of data) **plus a bounded retrieval sprint**
for WAEC official / NERDC SSS3 / JAMB cycle, with pre-accepted "blocked"
fallback. Full rationale, entry/acceptance/stop conditions and the phased
plan are in `OWNER_DECISION_BRIEF_PHASE21.md` §4–§5. No wave is
authorized by this report.

## 7. Proposed closure criteria

Seven proposed criteria (mandatory vs optional; one proposed
declared-scope extension flagged for approval) are set out in
`OWNER_DECISION_BRIEF_PHASE21.md` §6. Existing status meanings are not
redefined here; nothing takes effect without owner ratification (D4).
Board verification remains governed by CI-24.

## 8. Retrieval attempts this phase (bounded; official channels only)

1. `https://waecnigeria.org/` — fetched; no syllabus link in site
   navigation (e-learning = past questions; CASS = installers).
2. Site search (`site:waecnigeria.org` variants) — found the official
   2017–2019 syllabuses article and the Bookkeeping 2022–2025 syllabus
   article; **no Mathematics syllabus article**; third-party results
   (Scribd, masterwaec.com, waecsyllabus.com) were **not used**.
3. `https://www.waecnigeria.org/article/wassce-syllabuses-2017-2019` —
   selected-texts article; no Mathematics syllabus attachment.
4. `https://www.waecnigeria.org/article/bookkeeping-office-practice-2022-2025-wassce-syllabus`
   — official attachment confirmed:
   `https://www.waecnigeria.org/sites/default/files/2024-06/BookKeeping%26OfficePractice.pdf`
   (channel: syllabus documents ARE published as article attachments).
5. News pagination (`?page=4`, `?page=15`) — same item set; no older
   syllabus articles surfaced via this route.
6. `https://lmis.nerdcportals.com.ng/sss_3/` — HTTP 404 (persisted);
   portal root — login gate (SSS1/SSS2 viewer pattern only);
   `https://nerdc.org.ng/` — HTTP 500 (persisted).
7. JAMB cycle re-check: extracted-text scan shows no cycle/session
   marker (bibliography years only); source record
   `applicable_cycle = UNRESOLVED`.

Outcome: **no document obtained**; retrieval actions updated with the
newly identified WAEC attachment channel; CI-24 remains Open.

## 9. Verification of this audit and boundary compliance

- Full suite after documentation edits: **199 passed, 0 failed**
  (58 warnings). Canonical store: counts `424/678/337/86/234`;
  `run_store_validation == []`; `dumps_store` md5
  `0d680026d67ff729a9501544aa312980` — **unchanged**, proving the audit
  and its documentation did not alter the store.
- Git working tree contains only intended documentation changes:
  `docs/architecture/CLOSURE_REGISTERS.md` (M), `docs/architecture/
  SUBJECT_COMPLETION_ROADMAP.md` (M), `docs/architecture/
  OWNER_DECISION_BRIEF_PHASE21.md` (new), `docs/PHASE21_REPORT.md` (new).
  No generated artifacts, canonical exports, tests, or source-document
  records were touched. No commit/push performed (boundary).
- Boundaries held: no canonical changes; no new curriculum content; no
  Physics/Chemistry/Biology/English work; no entity-type/claim-restriction
  changes; `indicates` remains PROPOSED; nothing promoted to
  BOARD_VERIFIED; Phase 19/20 historical records preserved (register not
  rewritten; M-15a/b split is audit-level, recorded here and in the
  brief only).

## 10. Phase exit checklist

- [x] Every current Mathematics gap has a traceable disposition or an
  explicit unresolved status (§4 table; complete).
- [x] JAMB reconciliation and gap register checked against the live
  graph (§2–§3; consistent; discrepancy check clean).
- [x] Implementation and board-verification workstreams separated (§5).
- [x] Strategy comparison and recommended next work package documented
  (§6; brief §4–§5).
- [x] Closure criteria and owner decisions explicit (brief §6/§8; this
  report §7).
- [x] No unauthorized implementation occurred (§9; store md5 unchanged).

## 11. Outputs

- `docs/architecture/OWNER_DECISION_BRIEF_PHASE21.md` (new; owner
  decisions D1–D4, defaults, consequences).
- `docs/PHASE21_REPORT.md` (this file).
- `docs/architecture/SUBJECT_COMPLETION_ROADMAP.md` (Phase 21 audit note
  added; proposals explicitly labeled NOT ratified).
- `docs/architecture/CLOSURE_REGISTERS.md` (Phase 21 log entry: CI-24
  status refresh; no register-row changes).

Phase 21 documents remain uncommitted: no repository instruction requires
commits for documentation-only phases; the owner may direct a commit at
close-out.

Close-out disclosures (standing protocol):

- Clipboard: `docs/PHASE21_REPORT.md` was set via `termux-clipboard-set`
  ("set OK"); read-back returned EMPTY on two attempts — the known
  intermittent behavior. Disclosed as set-but-unverifiable.
- `/sdcard/Download/glm-cdg/` sync: `PHASE21_REPORT.md`,
  `OWNER_DECISION_BRIEF_PHASE21.md`, `SUBJECT_COMPLETION_ROADMAP.md` and
  `CLOSURE_REGISTERS.md` copied; the sync was re-run after this report's
  final edit and `cmp` verified byte-identical copies for all four files
  (brief md5 `242793f4…`, roadmap `a6612f3d…`, closure registers
  `c2924163…`; report md5 recomputed at the final sync and matching the
  repository file).
