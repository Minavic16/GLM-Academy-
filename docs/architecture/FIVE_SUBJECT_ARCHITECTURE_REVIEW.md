# Five-Subject Architecture Review (Phase 12)

Conclusion: the existing v0.2 model is sufficient for all five subjects without
new entity types or relationships.

| Subject | Modeling fit | Notes |
|---|---|---|
| Mathematics | reference implementation | KC = ability; TM/Method/Item fine |
| Physics | good | same abstractions; practicals discussed below |
| Chemistry | good (expected) | concepts, calculations, practicals analogous to Physics |
| Biology | sufficient | processes/systems as KCs; diagrams → Representational methods are KCs not relationships |
| English | sufficient | language capabilities as KCs; comprehension tasks as TaskModels; no grammar-tree entities needed at this stage |

## Additive changes made in Phase 12 (already compatible with v0.2)
- `Subject` entity entities (`subj.mathematics`, `sub.physics`) added to the
  canonical store — `EntityType.SUBJECT` already existed and is used.
- No new relationship types; cross-subject dependencies use existing
  `requires`/`prerequisite` Claims with explicit subject attributes.

## Decisions on Physics practicals
Practical/laboratory capability is modeled as a **PROPOSED KC**
(`kc.practical_measurement`) and will get its own TaskModel only when evidence
(textbook/assessment objective) defines observable practical tasks. Rationale:
laboratory competence is a durable capability, not a method for a computation
TaskModel. This same convention carries into Chemistry and Biology.

## Genuine gaps
None found. Representational reasoning in Physics/Biology is modeled as a
distinct KC with a distinct TaskModel rather than a new predicate.
