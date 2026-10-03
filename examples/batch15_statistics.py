"""Batch 015 — Statistics: mean of ungrouped data."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity
from cdg.store import CDGStore
from examples.batch14_trigonometry import build_graph_v14
from examples._batchkit import accept, ev

B_REVIEW = "act.batch15.review"
B_INTERP = "act.batch15.interpret"


def build_graph_v15() -> CDGStore:
    s = build_graph_v14()
    s.add_activity(Activity(id="act.batch15.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-04T04:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-04T04:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-04T05:00:00Z",
                            rationale="Human review of statistics batch."))
    kc = KnowledgeComponent(id="kc.mean_ungrouped_data",
                            label="Mean of ungrouped data",
                            definition="Compute the arithmetic mean of a list of values.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.STAT.MEAN_UNGROUPED"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.compute_mean", label="Compute the mean of a set of values",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.sum_divide_count", label="Sum the values and divide by the count",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    m1.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1)
    it = Item(id="it.mcq.mean", label="MCQ: mean", task_model_id=tm.id,
              stem="Find the mean of 4, 8, 10, 6, 7", options=["7", "6", "8", "35"], key="7",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-04T04:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm15.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets mean of ungrouped data", ASSESS)
    add("cl.tm15.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, kc_id in [("cl.req15.int", "kc.integer_arithmetic"),
                       ("cl.req15.frac", "kc.fraction_decimal_operations")]:
        add(cid, RelationshipType.REQUIRES, m1.id, kc_id, ClaimType.DEPENDENCY,
            f"{m1.id} requires {kc_id}", DEP)
    add("cl.pre15.frac_mean", RelationshipType.PREREQUISITE, "kc.fraction_decimal_operations", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via tm15 methods", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b15.t", "cl.tm15.target", "SRC.JAMB.UTME.MATH", "E0583",
                      "Node listed/entailed in JAMB syllabus: V.2(a).", True, B_INTERP))
    s.add_evidence(ev("ev.b15.m1", "cl.tm15.m1", "SRC.JAMB.UTME.MATH", "E0583",
                      "Mean of ungrouped data (JAMB syllabus objective).", True, B_INTERP))
    s.add_evidence(ev("ev.b15.r1", "cl.req15.int", "SRC.OSX.IA2E.6.2", "E0099",
                      "Requires integer summation.", False, B_INTERP))
    s.add_evidence(ev("ev.b15.r2", "cl.req15.frac", "SRC.NMAP.2008", "E0019",
                      "Requires division of a sum by a count.", True, B_INTERP))
    s.add_evidence(ev("ev.b15.p1", "cl.pre15.frac_mean", "SRC.NMAP.2008", "E0019",
                      "Requires division (fraction/decimal operations).", True, B_INTERP))
    return s
