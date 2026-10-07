# Cross-Subject Dependency Policy (Phase 11)

## 1. Definition
A cross-subject dependency is a CDG relationship whose source and target KCs
carry different `subject` attribute values (Mathematics → Physics,
Physics → Chemistry, Chemistry → Mathematics, etc.).

## 2. Representation decision
**Existing relationship types are retained; cross-subject context is carried
by Entity metadata, not by a new relationship.**

| Need | Current support | Decision |
|---|---|---|
| KC subject identity | `EntityBase.subject: Optional[str]` (versioned attribute) | Keep |
| Cross-subject prerequisite | `prerequisite` Claim with `purpose`/`scope`/`origin`; domain/range both KC; no same-subject restriction in validator | Keep — Phase 11 test confirms |
| Querying cross-subject prerequisites | filter Claims where source KC.subject ≠ target KC.subject | Keep; export_view already preserves subject-less but Claims carry subject_id — resolve via entity lookup |
| New relationship types (e.g. `dependsOnAcrossSubject`) | Not required at current model granularity | NOT INTRODUCED — would duplicate `prerequisite` semantics |

**Rationale.** The existing contract already forbids self-loops and demands
per-claim purpose/scope/origin/qualifyiers. Introducing a second cross-subject
predicate would double the semantics without adding validation.

## 3. Qualification rules — what qualifies as a legitimate cross-subject edge
An edge is legitimate only when ALL of the following hold:
1. **What capability is required** — a specific KC in the source subject whose
   absence would block a specific TaskModel in the target subject.
2. **In which subject the dependency lives** — source KC.subject and target
   KC.subject are distinct.
3. **Why it is genuine, not merely useful** — the target task is undefined,
   impossible, or invalid without the source capability (not "nice to have").
4. **What task requires it** — a concrete TaskModel in the target subject
   whose Method's `requires` set includes the source KC (the CDG rule:
   `requires` Method→KC is the canonical edge; prerequisite only summarizes
   that).
5. **What evidence supports it** — at least one EvidenceItem linking the
   claim to a source that documents the mathematical content of the physical
   or chemical task.
6. **Dependency character** — explicitly classified as one of:
   - computational (numeric manipulation)
   - procedural (steps needing the source capability)
   - conceptual (target reasoning invokes the source concept)
   - representational (graphs/symbols/formulas read the source skill)
   - assessment-specific (rare — flagged for review)
7. **Whether it models as prerequisite** — defaults to `EXECUTE` with
   `SPECIFIC_TASK_MODEL` or `SPECIFIC_METHOD` scope and `DERIVED` origin
   when derivable from `requires`; else `ASSERTED` with evidence.
8. **Target blocking** — prerequisite graph traversal must keep the target
   KC unserved in the diagnostic engine until the source is satisfied; this
   is a *consumer rule* enforced by future BA/diagnostic layers, not a
   CDG storage change.
9. **Review status** — created PROPOSED; human review required before ACCEPTED.

## 4. What MUST NOT be done
- Do NOT add edges simply because two topics look thematically related.
- Do NOT add edges based on literature lists without a TaskModel/Method
  carrying the dependency (no orphan cross-subject edges).
- Do NOT create cross-subject edges where the source skill would only
  appear as "one way" — use scoped `requires` on the relevant Method instead.
- Do NOT accept cross-subject edges without evidence + review.
- Do NOT introduce "transfer" or weighted cross-subject relations.

## 5. Classification of candidates (for the audit)
- CORE_CROSS_SUBJECT_DEPENDENCY: plainly required for the target task to be
  meaningful (e.g., algebraic rearrangement for kinematic equations).
- IMPORTANT_CROSS_SUBJECT_DEPENDENCY: required for specific Methods, not all.
- POSSIBLE_DEPENDENCY: suggested by topic overlap but not yet substantiated
  by a TaskModel/Method pair.
- NOT_YET_JUSTIFIED: appears related but has no task-level demand.
