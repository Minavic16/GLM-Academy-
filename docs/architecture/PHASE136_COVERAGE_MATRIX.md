# Mathematics Closure Coverage Matrix — Median and Dispersion (Phase 13.6)

| Requirement | Scope | Existing KC | Status pre-phase | Evidence | Change | Acceptance |
|---|---|---|---|---|---|---|
| Median meaning/calculation | JAMB V.2(a) (E0585), WAEC | none | NOT_IMPLEMENTED | E0585 inherited + OSTX 2.3 (data must be ordered) + 2.5 (robust to outliers) | Build `kc.median_ungrouped` | ACCEPTED, reviewed, targeting TM |
| Range | JAMB V.3 (E0589), WAEC | none | NOT_IMPLEMENTED | E0589 + OSTX 2.7 | Build `kc.measures_of_dispersion` (method) | same |
| Mean deviation | JAMB V.3 (E0590) | none | NOT_IMPLEMENTED | E0590 + OSTX 2.7 | same KC, method | same |
| Variance / standard deviation | JAMB V.3 (E0591/92), WAEC | none | NOT_IMPLEMENTED | E0591/92 + OSTX 2.7 (verified content) | same KC, method | same |
| Quartiles/IQR | WAEC-style | none | NOT_IMPLEMENTED | OSTX 2.3 (verified) | PARTIAL via median KC method | documented, no over-claim |
| Ordered-data prerequisite | derived | kc.mean_ungrouped_data (mean) | present | legacy edge FRACTION_DEC→MEAN | REUSE: median method requires mean-derived fraction/integer skills (no duplicate KC) | edges validate |

Median/mode: mode is JAMB V.2(a) (E0586) but secondary; grouped mean (E0584) unchanged. Mode NOT built — recorded as deferred secondary row with evidence located (avoids fragmentation; mean/median carry the location family).
