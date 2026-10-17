# JAMB Mathematics — Official Requirement Reconciliation (Phase 19)

Date: 2026-10-17. Baseline commit: `765a292` (Phase 18), working tree clean.
Scope: official-JAMB evidence reconciliation and Mathematics gap triage —
documentation only. No canonical entity/claim/edge changes, no canonical
implementation work, no Biology/English artifacts (OD-05 hold intact).

Phase 20 addendum (2026-10-17; baseline commit `238056d`): the owner
authorized a ten-topic Mathematics implementation wave (the Wave A variant,
expanded with indices, change of subject and factorisation). Batches 070–079
implemented it in `build_graph_v41` (`examples/math_wave_a_phase20.py`); the
full record is `docs/PHASE20_REPORT.md`. Disposition of the rows this
reconciliation tracks: M-03/M-04/M-05/M-19/M-20/M-21 → NO_ACTION_COVERED
(implemented); M-23 partially extended (common factors and difference of two
squares; cubic/theorem depth remains open). Coverage counts are now
COVERED 5 / PARTIALLY_COVERED 15 / NOT_COVERED 3. §5's modular-arithmetic
"final classification" is superseded for the implementation dimension (the
requirement is unchanged; an implementation now exists). The Phase 19 record
below is preserved as written — nothing was backdated or rewritten; Phase 20
only appended canonical records and updated dispositions.

Authoritative inputs:

- `docs/architecture/JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md` — Phase 18 matrix
  (23 official topics, content-checked).
- `docs/source-documents/SRC.JAMB.UTME.MATH.2025.json` — source record.
- `docs/architecture/PHASE18_RETRIEVAL_REPORT.md` — retrieval provenance.
- Extracted-text working copy `/tmp/phase18/ibass/jamb_mathematics.txt`
  (page locators below refer to this exact revision; not committed —
  copyrighted board material).
- Canonical store, builder `build_graph_v40()` — 365 entities / 583 claims /
  288 evidence / 85 sources / **204 activities**; `run_store_validation == []`.
  (Documentation correction, see §8.3: the Phase 17/18 reports printed
  "192 activities" — a stale v39 figure; the v40 store has 204, the twelve
  Phase 17 batch activities included.)

This reconciliation concludes that the Phase 18 matrix required three kinds
of refinement: one coverage-status correction (I.1), several gap-description
refinements (see §3, §8.1), and additional depth exposures that Phase 18's
topic-level pass did not itemize (§7). No requirement was promoted to a
subject-level status, and no subject status changed.

## 1. Source verification (Phase B)

Checked directly against `SRC.JAMB.UTME.MATH.2025.json` and the retained
working copy:

| item | value |
|---|---|
| Origin | JAMB official domain `ibass.jamb.gov.ng` (Integrated Brochure & Syllabus System), hashed static asset of the official web app |
| Document identity | `Mathematics.c0621f4b8b674e75fd05.pdf`, retrieved 2026-10-17 |
| SHA-256 | `aff7a7c2cc46036902dda38db1d1567d10982de709305cfbfc90dc437329754f` |
| Size / pages | 143,244 bytes / 6 pages |
| PDF metadata | Author "Abeeb Ibrahim Adeyemi"; Microsoft Word 2016; created/modified 2025-07-31 (+01:00) |
| Cycle applicability | No semester/cycle year printed — recorded `UNRESOLVED`; treated as the current official syllabus as published on the live portal at retrieval time |
| Content-check method | `pypdf` text extraction; topic-by-topic human checking (Phase 18); disputed findings re-verified against the extracted text in Phase 19 |
| Local copies | Not committed (copyright); `/tmp/phase18/ibass/jamb_mathematics.{pdf,txt}` |

No provenance defect was found; no further retrieval was performed. Two
distinct artefacts are deliberately kept apart: the **Phase 18 source record**
(docs-level, official PDF above) and the **legacy store source**
`SRC.JAMB.UTME.MATH` ("legacy:…" pointer, no bytes, used by the pre-v0.2
corpus). Only the former is cited for official confirmation; the legacy
pointer remains as historical implementation provenance.

Disputed findings re-inspected directly in the extracted text (all confirmed):
I.1(c) "modular arithmetic" is present with objective "perform operations in
modulo arithmetic"; II.4 objectives include "compute the sum of A. P. and
G.P." and "sum to infinity of a given G.P."; II.6 "algebra of matrices not
exceeding 3 x 3 … determinants … 3 x 3 … inverses of 2 x 2 matrices";
III.2(e) "the earth as a sphere: longitudes and latitudes"; V.2 cumulative
frequency and "Ogive"; V.1 representation of data.

## 2. Method and classification vocabulary

Record-level traceability was established by walking the canonical store:
`KnowledgeComponent → TaskModel` (`targets` claims) → `Method`
(`hasMethod`) → `Item` (`task_model_id`), plus `requires`/`prerequisite`
dependency claims. Absence checks were performed by keyword search across all
entity ids/labels/definitions/item stems/options **and** evidence excerpts
(for example `modul|modulo|number base|base 2|base 10` → 0 hits; `surd|rationali[sz]` → 0 hits;
`midpoint` → 0 hits; `standard form` → no relevant hits; `loci|locus|bisector`
→ 0 hits; `chord|cyclic|polygon` → 0 implementation hits; `sphere` → 0 hits;
`limit` → 0 hits; `ogive|cumulative|histogram|frequency distribution` → no
Math implementation hits). A matching topic name was never treated as
coverage; scope and depth were checked against the KC definition, methods and
items.

Vocabulary mapping (repository conventions):

- Coverage statuses (matrix vocabulary): `COVERED | PARTIALLY_COVERED |
  NOT_COVERED | NOT_APPLICABLE | UNRESOLVED`.
- Per-requirement implementation statuses (`SUBJECT_COMPLETION_STANDARD.md`
  clause F): `IMPLEMENTED_EVIDENCED | IMPLEMENTED_PENDING_CONFIRMATION |
  PARTIAL | NOT_IMPLEMENTED | BLOCKED | NOT_APPLICABLE`.
- Phase 19 working labels (`COVERED | PARTIAL | NOT_COVERED | UNRESOLVED |
  NOT_APPLICABLE`) map one-to-one onto the matrix vocabulary above.
- Evidence dimensions, never merged: **JAMB-OFFICIAL**
  (checked Phase 18/19) · **NERDC-SS1/SS2-OFFICIAL** (checked Phase 16) ·
  **SECONDARY-SyllabusNG** (Phase 16B; never authoritative) ·
  **WAEC-OFFICIAL** (outstanding) · **NERDC-SSS3** (unavailable).

## 3. Requirement-by-requirement reconciliation (23 official topics)

Implementation chain = actual canonical records (KC → TM → methods → item).
"Evidence basis" = sources backing the *implementation* (not the requirement).

| # locator | Official requirement (abridged) | Implementation chain (actual records) | Coverage | Impl. status | Evidence basis (implementation) | Gap / covered reason | Disposition |
|---|---|---|---|---|---|---|---|
| I.1 p.2 | Operations in bases 2–10; base conversion incl. fractional parts; modular arithmetic | adjacency only: `kc.equations_in_indices`, `kc.integer_arithmetic` (no base/modulo methods) | **NOT_COVERED** (corrected from PARTIALLY_COVERED) | NOT_IMPLEMENTED | — (adjacent KCs only) | No number-base or modular-arithmetic method/item exists (search: 0 hits) | OWNER_SCOPE_DECISION (M-03, M-04) |
| I.2 p.2 | Fractions/decimals; sig. figures; dec. places; percentage errors; simple interest; profit/loss %; ratio/proportion/rate; shares; VAT | `kc.fraction_decimal_operations` → `tm.fraction_decimal_operations` {`m.convert_common_denominator`}; `kc.percentage_concept` → `tm.percentage_problems` {`m.percent_as_fraction`} + `it.mcq.percentage`; `kc.ratio_proportion_rate` → `tm.solve_proportions` {`m.unitary_method`} + `it.mcq.ratio` | PARTIALLY_COVERED | PARTIAL | legacy `SRC.JAMB.UTME.MATH` pointers, OSX, NMAP 2008, Siegler 2012 | Missing: sig. figures, decimal places, percentage errors, simple interest, profit/loss, shares, VAT (zero entity hits) | OWNER_SCOPE_DECISION (M-19, M-20) |
| I.3 p.2 | Laws of indices; equations in indices; standard form; log laws; log to given base; change of base; indices–log relation; surds | `kc.equations_in_indices` → `tm.solve_index_equation` {`m.match_bases`, `m.logs`} + `it.mcq.index_eq`; `kc.logarithms` → `tm.logarithm_problems` {`m.convert_exp_log`, `m.apply_log_laws`} | PARTIALLY_COVERED | PARTIAL | legacy `SRC.JAMB.UTME.MATH`, OSX IA2E.10.3/10.4 | Missing: surds (all objectives), standard form, change of base, log-to-given-base evaluation; index laws applied only inside equations (no standalone simplification method) | OWNER_SCOPE_DECISION (M-05, M-21) |
| I.4 p.2 | Types of sets; algebra of sets; cardinality; symbols; Venn ≤3 sets | `kc.sets_operations` → `tm.set_operations` {`m.set_notation`, `m.set_operations`} + `it.math.sets_basic` | PARTIALLY_COVERED | PARTIAL | NERDC SSS1 p.7 (official) | Implemented: notation (roster/rule/set-builder), types (empty/subset/infinite/universal), union/intersection/complement. Missing: cardinality problems, Venn diagrams ≤3 sets, disjoint/finite types | OWNER_SCOPE_DECISION (M-22) |
| II.1 pp.2–3 | Change of subject; +,−,×,÷ of polynomials; factorisation ≤ deg 3; roots ≤ deg 3; factor & remainder theorems; one-linear-one-quadratic; polynomial graphs | `kc.change_of_subject` {`tm.make_subject`, `m.inverse_operations`, `m.collect_factor_subject`, `it.mcq.subject`}; `kc.algebraic_expressions` {`tm.handle_algebraic_expressions`, `m.collect_like_terms`, `m.expand_simplify`, `it.mcq.alg_simplify`}; `kc.factorisation_quadratic_trinomial`; `kc.quadratic_by_factorisation`; `kc.quadratic_formula`; `kc.quadratic_roots` {`tm.find_quadratic_roots`, 3 methods, `it.mcq.quadratic_roots`}; `kc.simultaneous_linear_quadratic` {`tm.solve_linear_quadratic_system`, `m.substitute_linear_into_quadratic`, `it.mcq.linquad`} | PARTIALLY_COVERED | PARTIAL | mixed: legacy JAMB pointers, OSX IA2E, NERDC, WAEC-SYL | Missing: factor & remainder theorems, cubic factorisation, polynomial division (÷), polynomial graphs ≤ deg 3, defined/undefined expressions, degree-3 roots | OWNER_SCOPE_DECISION (M-23) |
| II.2 p.3 | Direct, inverse, joint, partial variation; percentage increase/decrease | `kc.direct_variation` → `tm.direct_variation_problems` {`m.find_constant`} + `it.mcq.direct` | PARTIALLY_COVERED | PARTIAL | NERDC SSS1 (2 evidence rows) | Missing: inverse, joint, partial variation; variation percentage-change problems | OWNER_SCOPE_DECISION (M-24) |
| II.3 p.3 | Analytical & graphical linear inequalities; quadratic inequalities (integral roots) | `kc.linear_inequalities_analytic` → `tm.solve_linear_inequality` {`m.balance_inverse`, `m.test_graph` (number line)} + `it.mcq.linear_ineq` | PARTIALLY_COVERED | PARTIAL | legacy WAEC-SYL pointers | Missing: graphical (region) solutions; quadratic inequalities | OWNER_SCOPE_DECISION (M-25) |
| II.4 p.3 | nth term; sum of AP and GP; sum to infinity of GP | `kc.sequences_series` → `tm.sequences_series` {`m.ap_gp_nth_term`, `m.ap_gp_problems`} + `it.math.ap_gp` | PARTIALLY_COVERED | PARTIAL | NERDC SSS2 p.1 (official) | Missing: AP/GP sum formulas; sum to infinity | OWNER_SCOPE_DECISION (M-26) |
| II.5 p.3 | Binary operations: closure/commutativity/associativity/distributivity; identity & inverse elements | — | NOT_COVERED | NOT_IMPLEMENTED | — | No binary-operations KC/method/item (search: 0 hits) | OWNER_SCOPE_DECISION (M-10) |
| II.6 p.3 | Algebra of matrices ≤3×3; determinants ≤3×3; inverses of 2×2 | `kc.matrix_algebra` → `tm.matrix_algebra` {`m.matrix_operations`, `m.determinants_inverses`} + `it.math.matrix` | COVERED | IMPLEMENTED_EVIDENCED (implementation evidence secondary — Syllabus NG; disclosed) | `SRC.SYLLABUSNG.JAMB.MATH`, `SRC.SYLLABUSNG.WAEC.MATH` (SECONDARY) | Covered: scope/depth at KC & method level align with the official requirement (≤3×3 algebra, ≤3×3 determinants, 2×2 inverses, simultaneous equations). Item depth thin (2×2 determinant only) — assessment note, not a curriculum gap | NO_ACTION_COVERED (evidence note only) |
| III.1 p.3 | Lines/angles; polygons; circles (angle properties, cyclic quadrilaterals, intersecting chords); construction of special angles | `kc.parallel_line_angles` {`tm.identify_parallel_line_angles`, `m.corresponding_alternate`}; `kc.triangle_angle_properties` {`tm.triangle_angle_problems`, `m.triangle_angle_sum`, `m.exterior_angle`, `it.mcq.triangle_angle`}; `kc.circle_angle_theorems` {`tm.circle_angle_problems`, `m.centre_vs_circumference`, `it.mcq.circle`} | PARTIALLY_COVERED | PARTIAL | NERDC SSS1/SSS2, WAEC-SYL | Missing: quadrilateral/general-polygon objectives; cyclic quadrilaterals; intersecting chords; construction (30°–90° procedures) | OWNER_SCOPE_DECISION (M-09, M-27) |
| III.2 p.4 | Plane-figure lengths/areas; arcs & chords; sectors/segments; surface areas & volumes; earth as a sphere | `kc.mensuration` → `tm.mensuration` {`m.circle_mensuration`, `m.solid_mensuration`} + `it.math.mensuration` | PARTIALLY_COVERED | PARTIAL | NERDC SSS1 p.11 (official) | Missing: chord lengths; plane-figure perimeters/areas (triangles, quadrilaterals, composite); spheres; earth-as-sphere (longitudes/latitudes) | OWNER_SCOPE_DECISION (M-28) |
| III.3 p.4 | Loci in 2D (parallel lines, perpendicular bisectors, angle bisectors, circles) | — | NOT_COVERED | NOT_IMPLEMENTED | — | No loci KC/method/item (search: 0 hits) | OWNER_SCOPE_DECISION (M-09) |
| III.4 p.4 | Midpoint & gradient; distance; parallel/perpendicular; line equations (two-point, point-slope, slope-intercept, general) | `kc.distance_formula` {`tm.compute_distance`, `m.distance_formula`, `it.mcq.distance`}; `kc.gradient` {`tm.compute_gradient`, `m.gradient_from_two_points`, `it.mcq.gradient`}; `kc.equation_of_line` {`tm.find_line_equation`, `m.point_gradient`, `it.mcq.line_eq`}; `kc.parallel_perpendicular_lines` {`tm.classify_line_relationships`, `m.compare_gradients`, `it.mcq.parperp`} | PARTIALLY_COVERED | PARTIAL | OSX IA2E, WAEC-SYL | Missing: **midpoint** (search: 0 hits — added by Phase 19), two-point form, general form (slope-intercept emerges via point-gradient rearrangement only) | OWNER_SCOPE_DECISION (M-12) |
| III.5 pp.4–5 | Trig ratios (angles −360°≤θ≤360°); special angles; elevation/depression; bearings; triangle areas; sine/cosine graphs; sine/cosine formulae | `kc.trig_ratios_acute` {`tm.trig_ratio_problems`, `m.label_sides_match_ratio`, `it.mcq.trig_ratio`}; `kc.special_angle_values` {`tm.recall_special_values`, `m.from_special_triangles`, `it.mcq.special_angle`}; `kc.sine_rule` + `kc.cosine_rule` {`tm.solve_oblique_triangle`, `m.sine_rule`, `m.cosine_rule`, `it.mcq.sine_rule`} | PARTIALLY_COVERED | PARTIAL | OSX AT2E.10.x, CM.10.8 | Missing: angles beyond acute range (−360°…360°), special values 75°/105°/135°, elevation/depression, bearings, triangle-area formulae, sine/cosine graphs | OWNER_SCOPE_DECISION (M-13) |
| IV.1 p.5 | Limit of a function; differentiation of explicit algebraic & simple trig functions (sin, cos, tan) | `kc.differentiation_algebraic` → `tm.differentiate_explicit` {`m.power_rule`} + `it.mcq.diff` | PARTIALLY_COVERED | PARTIAL | OSX CALC1.3.x | Missing: limits (search: 0 hits); trig derivatives | OWNER_SCOPE_DECISION (M-14) |
| IV.2 p.5 | Rate of change; maxima and minima (applications) | `kc.rate_of_change` {`tm.compute_rate_of_change`, `m.derivative_at_point`, `it.mcq.rate`}; `kc.maxima_minima` {`tm.find_maxima_minima`, `m.first_derivative`, `it.mcq.extremum`} | COVERED | IMPLEMENTED_EVIDENCED | OSX CALC1.3.4, CALC1.4.3, NERDC SSS1 | Covered | NO_ACTION_COVERED |
| IV.3 p.5 | Integration of explicit algebraic & simple trig functions; area under the curve | `kc.integration_algebraic` → `tm.integrate_polynomial` {`m.reverse_power_rule`} + `it.mcq.integral` | PARTIALLY_COVERED | PARTIAL | OSX CALC1.4.10 | Missing: trig integration; area under curve | OWNER_SCOPE_DECISION (M-14) |
| V.1 p.5 | Frequency distribution; histogram; bar chart; pie chart | — | NOT_COVERED | NOT_IMPLEMENTED | — | No data-representation KC/method/item (search: 0 implementation hits) | OWNER_SCOPE_DECISION (M-15) |
| V.2 p.5 | Mean/mode/median ungrouped & grouped (simple cases); cumulative frequency; ogive (median, quartiles, percentiles) | `kc.mean_ungrouped_data` {`tm.compute_mean`, `m.sum_divide_count`, `it.mcq.mean`}; `kc.median_ungrouped` {`tm.compute_median`, `m.median_ordered`, `m.quartile_from_ordered`, `it.mcq.median`} | PARTIALLY_COVERED | PARTIAL | legacy JAMB pointers, OSX STAT2E.2.3/2.5 | Missing: mode (0 hits), grouped data, cumulative frequency/ogive (documented deferral — stands) | OWNER_SCOPE_DECISION (M-15; ogive deferral retained) |
| V.3 p.5 | Range, mean deviation, variance, SD (ungrouped & grouped) | `kc.measures_of_dispersion` {`tm.compute_dispersion`, `m.range`, `m.variance_sd`, `it.mcq.sd`} | PARTIALLY_COVERED | PARTIAL | legacy JAMB pointers, OSX STAT2E.2.7 | Missing: grouped-data dispersion | OWNER_SCOPE_DECISION (M-15) |
| V.4 p.5 | Permutation & combination: linear/circular arrangements; repeated objects | `kc.counting_principle` {`tm.count_outcomes`, `m.multiply_choices`, `it.mcq.count`} | PARTIALLY_COVERED | PARTIAL | OSX CM.7.2 | Missing: permutations/combinations (0 method hits); circular arrangements; repeated objects | OWNER_SCOPE_DECISION (M-11) |
| V.5 p.5 | Experimental probability; addition & multiplication of probabilities (mutually exclusive / independent) | `kc.theoretical_probability` {`tm.compute_probability`, `m.favourable_over_total`, `it.mcq.prob`} | PARTIALLY_COVERED | PARTIAL | OSX AT2E.13.7 | Missing: experimental probability (0 hits); addition/multiplication rules; mutually-exclusive/independent cases | OWNER_SCOPE_DECISION (M-16) |

Summary of the 23 official topics: **COVERED 2** (II.6, IV.2);
**PARTIALLY_COVERED 17**; **NOT_COVERED 4** (I.1, II.5, III.3, V.1).
Change vs the Phase 18 matrix: I.1 corrected PARTIALLY_COVERED → NOT_COVERED
(the previously listed KCs are adjacent, not supporting, records — the
coverage rule requires scope/depth support, not name adjacency); the other
22 classifications stand, with gap descriptions refined where Phase 19 found
additional depth exposures (§7). Phase 20 update: the counts in this section
are the Phase 19 record; after the Phase 20 implementation wave the counts
are COVERED 5 / PARTIALLY_COVERED 15 / NOT_COVERED 3 (see the addendum above
and §12).

## 4. Phase 17 scope-expansion audit (five KCs)

All five KCs exist, ACCEPTED, human-reviewed, with TM/methods/item and
evidence (verified against `build_graph_v40()` — nothing changed since
Phase 17). Their JAMB-evidence findings:

| KC | JAMB official finding (Phase 18/19) | Implementation assessment | Result |
|---|---|---|---|
| `kc.sets_operations` (batch 066) | **Topic confirmed**: official I.4 sets; implemented subset = notation/types/operations; official also requires cardinality problems + Venn diagrams ≤3 sets (not implemented) | Partially covers the official scope; no defect in what exists | PARTIAL (depth gap → M-22) |
| `kc.logical_reasoning` (batch 066) | **Not listed in the official JAMB Mathematics topic list** (checked for equivalent terminology: absent; binary operations II.5 is a different family). NERDC SSS1/SSS2 official basis; WAEC secondary lists logic | Implementation closed (NERDC-based); JAMB dimension NOT_APPLICABLE | Closed; no JAMB action |
| `kc.sequences_series` (batch 067) | **Topic confirmed**: official II.4; official depth adds AP/GP sums and sum-to-infinity (not implemented) | nth-term + application methods cover part of the official scope | PARTIAL (depth gap → M-26) |
| `kc.matrix_algebra` (batch 068) | **Topic + scope confirmed**: official II.6 exactly matches the KC definition (operations ≤3×3; determinants ≤3×3; inverses 2×2). Implementation evidence remains SECONDARY (Syllabus NG) — see §6 | Scope/depth aligned at KC and method level; item exercises 2×2 determinant only | COVERED; evidence note only |
| `kc.mensuration` (batch 069) | **Topic confirmed**: official III.2; official depth adds chords, plane-figure areas, spheres, earth-as-sphere (not implemented) | Arcs/sectors/segments/solids/frustums/composites implemented | PARTIAL (depth gap → M-28) |

Topic confirmation is kept distinct from depth confirmation: official
confirmation of matrices, sets, progressions and mensuration does **not**
validate every depth detail; the depth gaps above are recorded against the
specific official objective text.

## 5. Modular arithmetic — final classification

- Phase 16B (secondary) recorded "JAMB: not listed"; Phase 18 corrected this
  against the official document: topic I.1 is "Number bases/Modular
  Arithmetic" and objective iii is "perform operations in modulo arithmetic".
  Phase 19 re-verified the correction directly in the extracted text (p.2).
- Canonical search: `modul|modulo` across ids/labels/definitions/stems/
  options and evidence excerpts → **0 hits**; no modular-arithmetic KC,
  TM, method, item or claim exists.
- Final classification: requirement **officially confirmed (JAMB I.1(c))**;
  implementation **NOT_IMPLEMENTED / NOT_COVERED**. No duplicate KC was
  created; the deficit is the absence of any number-base/modulo
  representation, proposed for owner triage as M-03/M-04 (Wave A candidate).

## 6. Matrices and determinants — evidence and implementation classification

- Official requirement: CONFIRMED (II.6, p.3), depth specified as
  "algebra of matrices not exceeding 3×3", "determinants … 3×3", "inverses
  of 2×2 matrices" (plus the objective set; the "[excluding quadratic and
  higher degree equations]" note bounds matrix-inverse equation solving —
  which matches the CDG KC's simultaneous-equations scope).
- Implementation: `kc.matrix_algebra` → `tm.matrix_algebra` →
  {`m.matrix_operations`, `m.determinants_inverses`} + `it.math.matrix`
  (Phase 17 batch 068, unchanged).
- Implementation evidence: `ev.m68.mat.target` (`SRC.SYLLABUSNG.JAMB.MATH`,
  SECONDARY) and `ev.m68.mat.det` (`SRC.SYLLABUSNG.WAEC.MATH`, SECONDARY).
  **Phase 17 provenance is preserved**: the original implementation was based
  on secondary Syllabus NG evidence and is not retro-labelled as
  official-evidenced.
- Official JAMB evidence is recorded in the documentation layer only (this
  report and the matrix row note) because Phase 19 may not change canonical
  records; the KC's evidence base therefore remains secondary **by design**,
  disclosed here and in the matrix/register.
- Depth assessment: operations (add/subtract/scalar/multiply) ✓;
  determinants at definition level up to 3×3 ✓ (method instrumented as
  "Compute determinants and 2×2 inverses…"); inverses 2×2 ✓; simultaneous
  equations via matrices ✓. Assessment depth note: the single item covers a
  2×2 determinant only — no 3×3 determinant, inverse, or
  simultaneous-system item exercises the declared depth. This is an
  assessment-design observation (not a curriculum gap), recorded here;
  changing items would be canonical work and is not done in this phase.
- Residual uncertainty: WAEC official syllabus outstanding (its secondary
  row corroborates); NERDC SSS3 unretrieved (matrices absent from SSS1/SSS2
  topic lists; SSS3 possibly carries it).

## 7. Additional depth exposures found by Phase 19 (beyond the Phase 18 matrix)

Each was found by explicit search returning no implementation records; each
is an official objective under a topic already represented in the matrix,
and none had been itemized as a gap before:

| Official objective | Locator | Search result | Register |
|---|---|---|---|
| Midpoint of a line segment | III.4(a)/objective i | `midpoint` → 0 hits | M-12 |
| Standard form | I.3(c) | no relevant hits (only "completed-square standard form") | M-21 |
| Change of base in logarithms | I.3(f) | `change of base` → 0 hits | M-21 |
| Quadrilateral/general-polygon angle objectives | III.1(b)/ii | `polygon|quadrilateral` → 0 implementation hits | M-27 |
| Cyclic quadrilaterals; intersecting chords | III.1(c) | `cyclic|chord` → 0 hits | M-27 |
| Chord lengths | III.2(b)/ii | `chord` → 0 hits | M-28 |
| Plane-figure perimeters/areas (triangles, quadrilaterals, composite) | III.2(a)/i | `area` → only circle/solid mensuration hits | M-28 |
| Spheres in solids | III.2(d)/iii | `sphere` → 0 hits | M-28 |
| Experimental probability | V.5(a) | `experimental` → no probability records | M-16 |
| Grouped-data dispersion (already implied) | V.3 | `grouped` → no Math implementation hits | M-15 |

## 8. Corrections to earlier records (documentation only)

1. **Phase 18 matrix refinements** (applied to
   `JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md`): I.1 status corrected to
   NOT_COVERED; gap descriptions refined for I.2, I.3, I.4, II.1, II.2,
   II.3, II.4, III.1, III.2, III.4, III.5, IV.1, IV.3, V.2, V.3, V.4, V.5;
   II.6 depth/evidence note; cdg_entity_ids cells upgraded to full
   implementation chains (KC → TM → methods → items) with a Phase 19
   traceability note.
2. **Closure register refresh**: CI-20 (sets), CI-21 (logic), CI-22
   (mensuration) still showed "Open" although Phase 17 implemented them;
   statuses updated to closed-at-implementation with residual-depth pointers.
   CI-23 re-stated as partially closed (sequence & series implemented);
   remaining items triaged in `MATHEMATICS_GAP_REGISTER.md`. CI-24 unchanged
   (WAEC + NERDC SSS3 still outstanding).
3. **Activity-count correction**: Phase 17/18 reports printed "192
   activities" for the final v40 store. The v40 store has **204** activities
   (v39 had 192; batches 066–069 added 12: `act.m66–69.{extract,interpret,review}`).
   The historical report lines are left as-is (historical records); the
   correct figure is recorded here and in the Phase 19 report. Entities,
   claims, evidence and sources counts in those reports were correct
   (365/583/288/85).
4. **Gap-register cross-reference**: the deduplicated cross-subject register
   points to `MATHEMATICS_GAP_REGISTER.md` for the Phase 19 Mathematics
   triage; no row was deleted or overwritten.

## 9. Evidence dimension separation (Phase E)

| Dimension | Status for Mathematics | Where recorded |
|---|---|---|
| JAMB official UTME syllabus | Retrieved + content-checked (Phase 18); all 23 topics reconciled (this document) — requirement confirmation only | `SRC.JAMB.UTME.MATH.2025.json`; `JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md`; this report |
| NERDC official curriculum (SSS1/SSS2 only) | Retrieved + content-checked Phase 16; SSS3 unavailable — SSS1/SSS2 evidence does **not** establish SSS3 coverage | `MATHEMATICS_SYLLABUS_COVERAGE.md` |
| Secondary (Syllabus NG JAMB/WAEC mirrors) | Retained as audit history only; labelled SECONDARY; never authoritative; not overwritten; matrices implementation evidence stays here by Phase 17 provenance | `JAMB_MATHEMATICS_SECONDARY_COVERAGE.md`, `WAEC_MATHEMATICS_SECONDARY_COVERAGE.md` |
| WAEC official WASSCE syllabus | **Outstanding** — not obtained (no public downloads; CASS installers only; attempts in retrieval reports) | `PHASE18_RETRIEVAL_REPORT.md` §6; CI-24 |
| NERDC SSS3 | **Unavailable** (LMIS login-gated; portal 500) | `PHASE18_RETRIEVAL_REPORT.md` §6 |

Consequences applied: a checked official JAMB topic is confirmed **in the
JAMB dimension only**; the same topic remains unverified in the WAEC
dimension; official source confirmation and adequate CDG implementation are
separate facts (e.g. matrices: requirement confirmed, implementation
evidence secondary; number bases/modular: requirement confirmed, not
implemented). No topic is promoted to a subject-level BOARD_VERIFIED status:
WAEC is outstanding, and the completion standard governs. Mathematics
remains **IMPLEMENTATION_COMPLETE (declared scope) / BOARD_UNVERIFIED**.

## 10. Disposition summary

- `NO_ACTION_COVERED`: II.6 (with evidence note), IV.2; closed families
  M-01, M-02 (JAMB: not applicable), M-06, M-07, M-08 carry residual depth
  rows only.
- `DOCUMENTATION_CORRECTION`: Phase 18 matrix refinements; CI-register
  refresh; activity-count correction (all applied in this phase).
- `OWNER_SCOPE_DECISION` (implementation candidates, grouped for the owner
  brief): M-03, M-04, M-05, M-09, M-10, M-11, M-12, M-13, M-14, M-15,
  M-16, M-19, M-20, M-21, M-22, M-23, M-24, M-25, M-26, M-27, M-28.
- `EVIDENCE_RETRIEVAL_REQUIRED`: M-17, M-18 (WAEC-secondary-only rows;
  require official WAEC confirmation); M-29 (NERDC SSS2 "Proofs of Some
  Basic Theorems" — NERDC-side requirement, no JAMB locator).
- `UNRESOLVED`: none outstanding at requirement level; the source-level
  cycle-applicability caveat (no cycle year printed) remains recorded.
- `IMPLEMENTATION_CANDIDATE`: none authorized this phase — every remaining
  implementation item requires owner scope authorization first.

Full rows, priorities and dedup mapping: `MATHEMATICS_GAP_REGISTER.md`.
Owner decisions: `OWNER_DECISION_BRIEF_PHASE19.md`.

Phase 20 update (2026-10-17): M-03, M-04, M-05, M-19, M-20 and M-21 moved
from `OWNER_SCOPE_DECISION` to `NO_ACTION_COVERED` (implemented, batches
070–077); M-23 is partially addressed (batch 079) and remains in the owner
decision group for the outstanding polynomial depth. See §12.

## 11. What this phase does not change

- No canonical entities, claims, evidence, edges, items or activities added,
  deleted or modified; store counts and `run_store_validation == []`
  unchanged (365/583/288/85/204).
- No subject-status changes: Mathematics IMPLEMENTATION_COMPLETE (declared
  scope) / BOARD_UNVERIFIED; Physics IMPLEMENTATION_COMPLETE /
  BOARD_UNVERIFIED; Chemistry IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED.
- No Biology or English artifacts; `indicates` claim remains PROPOSED;
  13 entity types intact.
- No implementation of any gap: official syllabus evidence establishes the
  requirement; owner authorization determines whether and when
  implementation proceeds.

## 12. Phase 20 disposition update (2026-10-17)

Owner-authorized ten-topic wave (batches 070–079, `build_graph_v41`; full
record in `docs/PHASE20_REPORT.md`). Dispositions of the reconciled rows:

| Row | Phase 19 state | Phase 20 effect |
|---|---|---|
| M-03 modular arithmetic | NOT_COVERED | COVERED — kc.modular_arithmetic + TM + 2 methods + item (batch 071); boundary: residues and +, −, × implemented; modular division/inverses beyond the UTME treatment not included |
| M-04 number bases | NOT_COVERED | COVERED — kc.number_bases + TM + 2 methods + 2 items (batch 070); conversion incl. fractional parts; four operations in bases 2–10 |
| M-05 surds | NOT_COVERED | COVERED — kc.surds + TM + 3 methods + 2 items (batch 073) |
| M-19 financial mathematics | PARTIALLY_COVERED | COVERED — kc.simple_interest, kc.profit_and_loss, kc.shares_and_vat (+ TMs/methods/items; batch 077); boundary: compound interest, depreciation and discount are not JAMB I.2 requirements |
| M-20 approximation and errors | NOT_COVERED | COVERED — kc.approximation_errors + TM + 2 methods + 2 items (batch 074); boundary: absolute/relative error not required |
| M-21 standard form; log change-of-base | PARTIALLY_COVERED | COVERED — kc.standard_form (+ TM/methods/items; batch 075); m.change_of_base + item on tm.logarithm_problems (batch 076); kc.indices_laws prerequisite (batch 072) |
| M-23 polynomials depth | PARTIALLY_COVERED | PARTIALLY_COVERED (extended) — kc.factorisation_patterns (batch 079) adds common factors + difference of two squares; m.subject_powers_roots (batch 078); cubic/theorem/division/graph depth remains open |
| kc.equations_in_indices depth | (adjacency note) | Extended — kc.indices_laws (batch 072) with a DERIVED prerequisite to kc.equations_in_indices; existing index-equation records untouched |

Updated official counts (JAMB dimension): COVERED 5 / PARTIALLY_COVERED 15 /
NOT_COVERED 3 (`JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md`). Extended entities
keep their Phase 17/15/8 provenance: the matrices family and the original
change-of-subject, index-equation and logarithms claims/evidence are
untouched; Phase 20 added methods/claims/evidence only. WAEC official and
NERDC SSS 3 remain unretrieved (CI-24); nothing promoted to BOARD_VERIFIED;
the JAMB applicable cycle remains UNRESOLVED (no cycle year printed in the
retrieved revision).

## 13. Phase 22 P1 closure + retrieval sprint (2026-10-17)

Owner-authorized P1 closure (batches 080–082, `build_graph_v42`; full record
in `docs/PHASE22_REPORT.md`). Dispositions of the three former NOT_COVERED
rows and of the III.1(d) construction component:

| Row | Phase 21 state | Phase 22 effect |
|---|---|---|
| II.5 binary operations | NOT_COVERED | COVERED — kc.binary_operations + tm.binary_operations_problems + 3 methods (evaluation by rule/table; properties; identity/inverse) + 2 items (batch 080); boundary: UTME treatment only, no abstract-algebra expansion |
| III.3 loci (+ III.1(d) construction) | NOT_COVERED (loci); construction not evidenced | COVERED — kc.loci_and_construction + tm.loci_construction_problems + 5 methods (describe locus; perpendicular bisector; angle bisector; special angles 30°–90°; intersection of loci) + 3 items (batch 081); the III.1 row retains its polygon/cyclic/chord depth gaps under M-27 |
| V.1 representation of data | NOT_COVERED | COVERED — kc.data_representation + tm.data_representation_problems + 4 methods (frequency distribution; bar chart; histogram; pie chart) + 3 items (batch 082); ogive/cumulative frequency remain excluded (standing owner deferral); the location/dispersion KCs are untouched |

Updated official counts (JAMB dimension): COVERED 8 / PARTIALLY_COVERED 15 /
NOT_COVERED 0 (`JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md`). The 15 remaining
PARTIALLY_COVERED rows are the documented P2 depth residuals
(`MATHEMATICS_GAP_REGISTER.md`); no P2 work was performed in this phase.

Retrieval sprint (bounded; official channels only; nothing obtained, nothing
substituted):

| Blocker | Probes (this phase) | Outcome |
|---|---|---|
| WAEC official WASSCE Mathematics syllabus | waecnigeria.org sitemap.xml (404); site search "mathematics syllabus" and "syllabus" (Drupal search) — only the Bookkeeping & Office Practice 2022–2025 syllabus article, selected-texts lists and FAQ pages surface; no Mathematics syllabus article/attachment | NOT OBTAINED — channel confirmed (per-subject syllabus articles with attachments) but no Mathematics document exists there; follow-up: official WAEC enquiry for the "Regulations & Syllabuses" publication and periodic recheck |
| NERDC SSS3 Mathematics curriculum | lmis.nerdcportals.com.ng/sss_3/ recheck (404, unchanged); lmis.nerdcportals.com.ng root (login gate: "Please log in to continue" + registration); nerdc.org.ng recheck (HTTP 500, unchanged) | NOT OBTAINED — no alternative official SSS3 publication found; follow-up: registered-institution access route or official NERDC contact; periodic recheck; reconstruction from SSS1/SSS2 or third-party sources is not permitted |
| JAMB applicable cycle for the official PDF | PDF metadata re-inspected (CreationDate = ModDate = 2025-07-31; author/creator fields; no cycle); extracted text re-grepped (no year/cycle marker); official IBASS SPA bundle (main.js) re-grepped (no cycle strings); jamb.gov.ng context check (2026 cycle active at retrieval; no statement tying the e-syllabus revision to a cycle) | UNRESOLVED — a PDF metadata date alone is insufficient; evidence needed: an official JAMB statement tying the IBASS e-syllabus revision to a UTME cycle (or a versioned syllabus listing). Treated as the current official syllabus as published on the live portal at retrieval time |

Evidence discipline: every Phase 22 claim is evidenced by the official JAMB
source (SRC.JAMB.UTME.MATH.2025) with precise locators (II.5; III.3 +
III.1d; V.1a–b); no secondhand aggregator was used; nothing is promoted to BOARD_VERIFIED;
WAEC official and NERDC SSS3 remain outstanding (CI-24 Open).
