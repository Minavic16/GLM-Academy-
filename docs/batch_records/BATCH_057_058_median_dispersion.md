# Batches 057–058 — Mathematics median + dispersion (Phase 13.6, CI-01/CI-02)

- 057 kc.median_ungrouped (legacy MATH.STAT.MEDIAN); tm.compute_median;
  M median-ordered (req integer) + quartile-from-ordered (req integer + fraction);
  TM-DERIVED prereqs integer + UNDERSTAND mean→median; evidence OSTX STAT2E
  2.3/2.5 (verified) + inherited E0585; item median MCQ.
- 058 kc.measures_of_dispersion (legacy RANGE/MEAN_DEVIATION/VARIANCE/
  STANDARD_DEVIATION); tm.compute_dispersion; M range/mean-deviation +
  variance/SD (req mean, alg, fraction/frac, indices); all TM-DERIVED;
  evidence OSTX STAT2E 2.7 (verified) + inherited E0591/92; item range MCQ.
- Math KCs 37→39 (39 total with 13.5 log). Physics 19, Chemistry 12 unchanged.
- Store validation []; pytest 117 green.
