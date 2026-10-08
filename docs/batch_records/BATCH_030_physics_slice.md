# BATCH 030 — Physics slice (Measurement / Kinematics / Newton)

- Subject identity: Physics KCs carry subject="Physics"; Subject entities
  subj.physics/subj.mathematics added.
- KCs added: 8 (6 ACCEPTED, 2 PROPOSED: measurement errors/precision,
  practical measurement)
- TaskModels: 4; Methods: 6 (AND-within-method, OR-across-methods preserved).
- Cross-subject edges created (4, all DERIVED/SPECIFIC_TASK_MODEL):
  algebraic expressions → motion equations; linear equations → motion
  equations; gradient → motion graphs; algebraic expressions → Newton's laws.
- Evidence: 10 items, all resolving to fetched OpenStax University Physics
  pages; official JAMB/WAEC/NERDC sources registered as metadata-only
  Sources with retrieval gaps recorded in PHYSICS_SCOPE.md.
- Practical modeling decision: practical competence = PROPOSED KC
  (kc.practical_measurement), not a method (see
  FIVE_SUBJECT_ARCHITECTURE_REVIEW.md).
- Validation: run_store_validation → []; pytest 90 passed; visualization
  regenerated with subject outline colors (Math green, Physics blue).
