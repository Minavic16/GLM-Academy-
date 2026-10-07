# Mathematics CDG Readiness Audit — Phase 10

Date: 2026-10-07. Canonical: `examples/math_cdg_v2.json`.

## 1. Current graph state (after two local corrections)

- Entities: **151** (36 KCs, 35 TMs, 49 Methods, 30 Items, 1 Misconception)
- Claims: **221** (219 ACCEPTED, 2 PROPOSED)
- Evidence: **207** (all legacy-inherited with preserved legacy IDs)
- Sources: **28** (previously missing `SRC.OSX.IA2E.5.4` and `SRC.OSX.AT2E.7.2`
  added as canonicalization corrections)
- export_view: **151 nodes / 221 edges**
- Store validation: **`[]`**
- pytest: **77 passed**
- Documentation determinism: byte-identical across two generator runs

Corrections made in this phase:
- Added did IDs-merge: none (no equivalence was created).
- Added two missing Source records; added `test_evidence_source_resolution`
  invariant; no architecture change.

## 2. Domain coverage matrix

| Domain | KCs | TMs | Methods | Status | Important gaps |
|---|---|---|---|---|---|
| Algebra | 11 | 11 | 15 | STRONG | polynomials, remainder theorem, matrices, sets, progressions |
| Number & Numeration | 4 | 4 | 5 | ADEQUATE | indices/logs, surds, financial arithmetic |
| Geometry | 4 | 4 | 6 | STRONG | quadrilaterals/polygons, constructions, mensuration |
| Coordinate Geometry | 4 | 4 | 6 | ADEQUATE | midpoint, loci, distance/alley |
| Trigonometry | 4 | 4 | 6 | ADEQUATE | identities, graphs, bearings/elevation |
| Calculus | 4 | 4 | 5 | ADEQUATE | definite integrals, area under curve, limits (deferred) |
| Statistics & Probability | 3 | 3 | 4 | PARTIAL | median/mode/dispersion, compound events |
| Functions | 1 | 1 | 2 | THIN | domain/range, inverse, composite, graphs |

Status basis: representation exists for the core chain; advanced topics
remain NOT REPRESENTED rather than partially modeled.

## 3. Curriculum → CDG mapping (spot check)

- Fractions/decimals/percentages → kc.fraction_decimal_operations, kc.percentage_concept →
  tm.fraction_decimal_operations / tm.percentage_problems → Methods with explicit
  prerequisite chains (integer arithmetic) — DIRECTLY REPRESENTED.
- Bootcamp "JAMB stat V.2(a)" → kc.mean_ungrouped_data + E0583 — DIRECTLY REPRESENTED.
- JAMB "identify conditions for parallelism and perpendicularity" →
  kc.parallel_perpendicular_lines + E0253 — DIRECTLY REPRESENTED.
- Matrices/determinants → present only in legacy candidates — MISSING — SECONDARY.
- Functions domain/range/inverse → MISSING — SECONDARY (thin legacy evidence).

## 4. Dependency audit (derived chains)

1. integer arithmetic → fractions/decimals → ratio/proportion → direct variation
2. algebraic expressions → factorisation → quadratic by factorisation → roots
   → maxima/minima; formula/cts branches persist through separate TMs/Methods
3. gradient → equation of straight line → parallel/perpendicular classification;
   gradient → distance formula
4. acute trig ratios → special-angle values; acute ratios → sine/cosine rules
5. differentiation → rate of change; differentiation → integration (UNDERSTAND link)
6. fractions → theoretical probability

All EXECUTE/ALL-scope chains are acyclic. No isolated KC remains: every KC has
≥1 targeting TaskModel, every TM has ≥1 Method, every Method has explicit
`requires`.

## 5. Structural audit

| Check | Result |
|---|---|
| Orphan entity references | 0 |
| TMs without target or Method | 0 |
| Methods without `requires` | 0 |
| KCs without any targeting TM | 0 |
| ALL-scope EXECUTE cycles | none |
| Duplicate labels | 0 |
| Claims missing review reference among ACCEPTED | 0 |
| Evidence→claim resolution | OK |
| Evidence→source resolution | OK (after Phase 10 correction) |

## 6. TaskModel audit

35 TMs total. Structural classification — READY: 35 (every TM targets an
accepted KC, has ≥1 Method, and that Method has explicit prerequisites);
NEEDS MINOR CORRECTION: 0; NEEDS SUBSTANTIVE MODELING: 0.
22/35 TMs have exactly one Method (acceptable — OR holds across the method set).

## 7. Method audit

49 Methods — READY: 49 (each is an executable approach under exactly one TM,
AND-within-method structure explicit, ≥1 prerequisite). No Method was found
that is really a KC or topic label; AND/OR semantics verified test-side
(`evaluate_task_model` against slice and store data).

## 8. BA-readiness audit

Structural verdict over all 36 KCs: **BA_READY: 36** (each has ≥1 observable
TaskModel, ≥1 executable Method, and explicit prerequisites with purpose/
scope/origin). BA items themselves are intentionally out of scope for this
document; 2 PROPOSED Claims (misconception catalog entry, item indicator)
remain correctly outside BA acceptance.

## 9. Remaining curriculum gaps (ranked)

1. **Median/mode of ungrouped data** — MUST ADD BEFORE BA only if BA includes
   location-measure items; otherwise DEFER.
2. **Measures of dispersion** — IMPORTANT_GAP; prerequisite chain through
   squares/roots not yet present; defer.
3. **Polynomial addition/subtraction and remainder theorem** — SHOULD ADD
   BEFORE BA for Algebra chapter completeness.
4. **Counting/permutations expansion** — CAN DEFER (counting principle present).
5. **Matrices/determinants** — THE legacy corpus has heavy evidence; SHOULD
   ADD BEFORE BA if JAMB objective selected.
6. **Mensuration, polygons, bearings/elevation** — DEFER until BA specifies
   those chapters.

## 10. Legacy corpus question

Does any remaining legacy capability block BA readiness?
**No capability required for the current BA-scoped chapters is absent.** The
remaining ~147 nodes / ~211 edges (matrices deep dive, mensuration, circle
expansion, bearings, etc.) map to secondary topics. Legacy migration can stay
deferred; no bulk import is warranted.

## 11. Freeze-readiness

**FREEZE READY AFTER OWNER DECISIONS.** Architecture, contracts, tests,
serialization, docs, and dependency structure are stable. Owner decisions
still outstanding: FREEZE doc content, `indicates` sign-off, entity-count
reconciliation.

## 12. Final recommendation

**BA READY AFTER TARGETED CORRECTIONS** — the only corrections applied in this
phase were the two missing Source records (now repaired and locked by a
regression test). No corpus wave is required for BA on the currently scoped
chapters; add items 1–5 above to a targeted corrective queue rather than a
new open-ended wave.
