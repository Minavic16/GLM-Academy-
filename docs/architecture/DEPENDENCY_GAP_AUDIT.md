# Phase 9 Stage A — Dependency-Gap Audit (pre-Wave-2)

Date: 2026-10-07. Baseline: 30 KCs, 29 TMs, 43 Methods, 189 Claims, 144→187 Evidence.

## Domain-by-domain verdict

| Domain | KCs (before) | Strongest chain | Principal gaps | Priority |
|---|---|---|---|---|
| Algebra | 12 | linear eqs → quadratics(factorisation/formula/cts) → roots; change of subject | polynomials, variation, matrices, sets, progressions, remainder theorem | rare-but-useful (variation built in wave 2) |
| Number & Numeration | 3 | integer arithmetic → fractions/percentages; fraction→ratios (missing) | ratio/proportion (built), indices/logs, surds, financial arithmetic | ratio/proportion = CORE_MISSING; built in wave 2 |
| Geometry | 3 | parallel lines → triangle angles → circle angles | quadrilaterals/polygons, constructions, mensuration | circle built in wave 1; polygons/mensuration = IMPORTANT_GAP |
| Coordinate Geometry | 2 | gradient → equation of line | parallel/perp (built), distance (built), midpoint, loci | distance + parallel/perp = CORE_MISSING; built in wave 2 |
| Trigonometry | 3 | acute ratios → sine/cosine rules (built wave 1) | special angles (built), identities, graphs, bearings | special angles = IMPORTANT_GAP; built in wave 2 |
| Calculus | 5 | differentiation → rate → maxima/minima; diff → integration | applications of diff, areas, definite integrals, limits (deferred) | rate/maxima/integration closed most of the chain in wave 1 |
| Statistics & Probability | 2 | mean (ungrouped); theoretical prob (built wave 1) | median/mode (secondary gap), dispersion, compound/independent events, counting principle (built) | counting principle = IMPORTANT_GAP; built in wave 2 |
| Functions | 1 | evaluation TM only | domain/range, composite, inverse, transformation graphs | NOT_YET_JUSTIFIED (evidence thin in legacy corpus) |

## Bottlenecks identified (and how wave 2 addressed them)

1. gradient had only one consumer (equation of line). → Wave 2 adds
   parallel/perpendicular classification and distance formula as consumers.
2. fraction_decimal_operations had no Numbers-domain consumer except percentages.
   → Wave 2 adds ratio/proportion/rate and counting principle (multiplication rule).
3. linear_equations had a gap to variation;  direct variation now exists.
4. trig ratios lacked any standalone value set → special-angle values added.
5. Coordinates: midpoint still absent — classified SECONDARY_GAP (evidence has
   agent-attributed support E0246 but no JAMB/WAEC objective at KC granularity).

## Deferred / rejected

- Equivalence handling between gradient / slope / gradient_of_line: no new KC,
  legacy aliases retained via canonical id only.
- Mensuration, polygons, bearings/elevation: NOT_YET_JUSTIFIED this wave —
  legacy evidence is thin or agent-attributed.
- Functions domain extension (composite/inverse): weak legacy evidence — skip.
- Statistical dispersion (range/variance/SD): requires squares/roots prerequisite
  chain not yet present — classified IMPORTANT_GAP for a later wave.
