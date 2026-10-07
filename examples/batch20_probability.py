"""Batch 020 — Elementary probability: sample space and events."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch19_integration import build_graph_v19
from examples._batchkit import accept, ev

B_REVIEW = "act.batch20.review"
B_INTERP = "act.batch20.interpret"


def build_graph_v20() -> CDGStore:
    s = build_graph_v19()
    s.add_activity(Activity(id="act.batch20.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-07T06:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-07T06:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-07T07:00:00Z",
                            rationale="Human review of probability batch."))
    for sid, title in [("SRC.OSX.AT2E.13.7", "Algebra and Trigonometry 2e, 13.7 Introduction to Probability"),
                       ("SRC.OSX.CM.7.5", "Calculus/Common Mathematics reference 7.5")]:
        if sid not in s.sources:
            s.add_source(Source(id=sid, title=title, identifier_or_url=f"legacy:{sid}",
                                publisher="OpenStax", source_type=SourceType.TEXTBOOK, tier="reference"))
    kc = KnowledgeComponent(id="kc.theoretical_probability",
                            label="Theoretical probability of an event",
                            definition="P(E) = favourable outcomes / total equally likely outcomes.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.STAT.THEORETICAL_PROBABILITY"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.compute_probability",
                   label="Compute the theoretical probability of an event",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.favourable_over_total", label="Count favourable and total outcomes and form the fraction",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    m1.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1)
    it = Item(id="it.mcq.prob", label="MCQ: probability", task_model_id=tm.id,
              stem="A fair die is rolled once. P(rolling a 4) = ?",
              options=["1/6", "1/4", "4/6", "1/2"], key="1/6",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-07T06:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm20.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets theoretical probability", ASSESS)
    add("cl.tm20.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, kc_id in [("cl.req20.frac", "kc.fraction_decimal_operations"),
                       ("cl.req20.int", "kc.integer_arithmetic")]:
        add(cid, RelationshipType.REQUIRES, m1.id, kc_id, ClaimType.DEPENDENCY,
            f"{m1.id} requires {kc_id}", DEP)
    add("cl.pre20.frac_prob", RelationshipType.PREREQUISITE, "kc.fraction_decimal_operations", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via tm20", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b20.t", "cl.tm20.target", "SRC.OSX.AT2E.13.7", "E0375",
                      "The set of all possible outcomes of an experiment is called the sample space.", True, B_INTERP))
    s.add_evidence(ev("ev.b20.m1", "cl.tm20.m1", "SRC.OSX.CM.7.5", "E0376",
                      "An event is a subset of the sample space.", True, B_INTERP))
    s.add_evidence(ev("ev.b20.r1", "cl.req20.frac", "SRC.NMAP.2008", "E0019",
                      "Probability computed as a fraction.", True, B_INTERP))
    s.add_evidence(ev("ev.b20.r2", "cl.req20.int", "SRC.OSX.IA2E.6.2", "E0099",
                      "Requires counting.", False, B_INTERP))
    s.add_evidence(ev("ev.b20.p1", "cl.pre20.frac_prob", "SRC.OSX.AT2E.13.7", "E0375",
                      "Probability value is a fraction of outcomes.", True, B_INTERP))
    return s
