"""Phase 13.6: Mathematics median + dispersion closure (CI-01, CI-02).
Chains build_graph_v35; does not touch Physics/Chemistry records."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, EvidenceRole, EvidenceStance, ExcerptKind,
                       PrerequisitePurpose, PrerequisiteScope, RelationshipType,
                       SourceType)
from cdg.evidence import EvidenceItem
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.closure_fixes import build_graph_v35
from examples._batchkit import accept

SUBJ = "Mathematics"
ASSESS = (AcceptanceBasis.EXPERT,)
DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
STAMP = "2026-10-15T09:10:00Z"
E, P = PrerequisitePurpose.EXECUTE, PrerequisiteScope


def _base(s, nn, note):
    s.add_activity(Activity(id=f"act.m{nn}.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-15T09:00:00Z"))
    interp = f"act.m{nn}.interpret"
    rev = f"act.m{nn}.review"
    s.add_activity(Activity(id=interp, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-15T09:05:00Z"))
    s.add_activity(Activity(id=rev, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-15T10:00:00Z",
                            rationale=note))
    return interp, rev


def _src(s, sid, title, url):
    if sid not in s.sources:
        s.add_source(Source(id=sid, title=title, identifier_or_url=url,
                            publisher="OpenStax", source_type=SourceType.TEXTBOOK,
                            tier="reference"))


def build_graph_v36() -> CDGStore:
    s = build_graph_v35()

    # ---- 057 median ----
    interp, rev = _base(s, "57", "Human review of median closure batch.")
    _src(s, "SRC.OSX.STAT2E.2.3", "Introductory Statistics 2e, 2.3 Measures of the Location of the Data",
         "https://openstax.org/books/introductory-statistics-2e/pages/2-3-measures-of-the-location-of-the-data")
    _src(s, "SRC.OSX.STAT2E.2.5", "Introductory Statistics 2e, 2.5 Measures of the Center of the Data",
         "https://openstax.org/books/introductory-statistics-2e/pages/2-5-measures-of-the-center-of-the-data")
    k = KnowledgeComponent(id="kc.median_ungrouped", label="Median of ungrouped data",
                           definition="Order data and locate the middle value; handle odd/even counts.",
                           subject=SUBJ, status=ClaimStatus.ACCEPTED,
                           legacy_ids=["MATH.STAT.MEDIAN"],
                           created_by_activity=interp, cdg_version="v0.2.0")
    k.reviewed_by_activity = rev
    k.review_rationale = "Accepted in Phase 13.6 via human review."
    s.add_entity(k)
    t = TaskModel(id="tm.compute_median", label="Compute the median of ungrouped data",
                  subject=SUBJ, status=ClaimStatus.ACCEPTED, created_by_activity=interp,
                  cdg_version="v0.2.0")
    t.reviewed_by_activity = rev
    s.add_entity(t)
    m1 = Method(id="m.median_ordered", label="Order the data and take the middle value(s)",
                task_model_id=t.id, subject=SUBJ, status=ClaimStatus.ACCEPTED,
                created_by_activity=interp, cdg_version="v0.2.0")
    m1.reviewed_by_activity = rev
    m2 = Method(id="m.quartile_from_ordered", label="Read quartiles/IQR from ordered data",
                task_model_id=t.id, subject=SUBJ, status=ClaimStatus.ACCEPTED,
                created_by_activity=interp, cdg_version="v0.2.0")
    m2.reviewed_by_activity = rev
    for m in (m1, m2):
        s.add_entity(m)
    for cid, pred, subj, obj, ctype, rat, bases in [
        ("cl.m57.target", RelationshipType.TARGETS, t.id, k.id,
         ClaimType.ASSESSMENT_DESIGN, "targets median", ASSESS),
        ("cl.m57.own.m1", RelationshipType.HAS_METHOD, t.id, m1.id,
         ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS),
        ("cl.m57.own.m2", RelationshipType.HAS_METHOD, t.id, m2.id,
         ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS),
        ("cl.m57.req.m1.int", RelationshipType.REQUIRES, m1.id, "kc.integer_arithmetic",
         ClaimType.DEPENDENCY, "median ordering needs integer arithmetic", DEP),
        ("cl.m57.req.m2.int", RelationshipType.REQUIRES, m2.id, "kc.integer_arithmetic",
         ClaimType.DEPENDENCY, "quartiles need integer arithmetic", DEP),
        ("cl.m57.req.m2.frac", RelationshipType.REQUIRES, m2.id, "kc.fraction_decimal_operations",
         ClaimType.DEPENDENCY, "quartile interpolation needs fractions", DEP),
    ]:
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=interp,
                  created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, rat, bases, rev))
    for cid, subj, scope, ref, rat in [
        ("cl.pre57.int_median", "kc.integer_arithmetic", P.SPECIFIC_TASK_MODEL, "tm.compute_median",
         "DERIVED: both median methods need integer arithmetic"),
        ("cl.pre57.frac_median", "kc.fraction_decimal_operations", P.SPECIFIC_METHOD, "m.quartile_from_ordered",
         "DERIVED: quartile method needs fractions"),
        ("cl.pre57.mean_median", "kc.mean_ungrouped_data", P.SPECIFIC_TASK_MODEL, "tm.compute_median",
         "UNDERSTAND: median is learned beside mean as a location measure"),
    ]:
        purpose = (PrerequisitePurpose.UNDERSTAND if cid == "cl.pre57.mean_median" else E)
        origin = (ClaimOrigin.ASSERTED if purpose == PrerequisitePurpose.UNDERSTAND
                  else ClaimOrigin.DERIVED)
        c = Claim(id=cid, predicate=RelationshipType.PREREQUISITE, subject_id=subj,
                  object_id=k.id, claim_type=ClaimType.DEPENDENCY, purpose=purpose,
                  scope=scope, scope_ref=(None if origin == ClaimOrigin.ASSERTED else ref),
                  origin=origin, created_by_activity=interp,
                  created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, rat, DEP, rev))
    for eid, cid, src, exc, leg in [
        ("ev.m57.t", "cl.m57.target", "SRC.OSX.STAT2E.2.3",
         "To find quartiles and percentiles the data must be ordered from smallest to largest.", None),
        ("ev.m57.t2", "cl.m57.target", "SRC.OSX.STAT2E.2.5",
         "Median is robust to outliers compared with the mean.", None),
        ("ev.m57.leg", "cl.m57.target", "SRC.JAMB.UTME.MATH",
         "Node listed/entailed in JAMB syllabus: V.2(a); objective i", "E0585"),
    ]:
        s.add_evidence(EvidenceItem(
            id=eid, claim_id=cid, source_id=src,
            role=EvidenceRole.INDIRECT, stance=EvidenceStance.SUPPORTS,
            locator=("legacy JAMB pointer" if leg else "openstax section"),
            excerpt=exc, excerpt_kind=ExcerptKind.PARAPHRASE,
            extracted_by_activity=interp, inherited_from_legacy=bool(leg), legacy_id=leg))
    s.add_entity(Item(id="it.mcq.median", label="MCQ: median of 6 values",
                      task_model_id=t.id, subject=SUBJ,
                      stem="Median of 3, 7, 9, 2, 5, 8", options=["7", "6", "8", "5.5"],
                      key="7", status=ClaimStatus.ACCEPTED, created_by_activity=interp))

    # ---- 058 dispersion ----
    interp, rev = _base(s, "58", "Human review of dispersion closure batch.")
    _src(s, "SRC.OSX.STAT2E.2.7", "Introductory Statistics 2e, 2.7 Measures of the Spread of the Data",
         "https://openstax.org/books/introductory-statistics-2e/pages/2-7-measures-of-the-spread-of-the-data")
    k2 = KnowledgeComponent(id="kc.measures_of_dispersion", label="Measures of dispersion",
                            definition="Compute range, mean deviation, variance and standard deviation; compare variability.",
                            subject=SUBJ, status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.STAT.RANGE", "MATH.STAT.MEAN_DEVIATION",
                                        "MATH.STAT.VARIANCE", "MATH.STAT.STANDARD_DEVIATION"],
                            created_by_activity=interp, cdg_version="v0.2.0")
    k2.reviewed_by_activity = rev
    k2.review_rationale = "Accepted in Phase 13.6 via human review."
    s.add_entity(k2)
    t2 = TaskModel(id="tm.compute_dispersion", label="Compute and compare dispersion",
                   subject=SUBJ, status=ClaimStatus.ACCEPTED, created_by_activity=interp,
                   cdg_version="v0.2.0")
    t2.reviewed_by_activity = rev
    s.add_entity(t2)
    spans = {
        "m.range": "Compute range and mean deviation",
        "m.variance_sd": "Compute variance and standard deviation",
    }
    reqs = {
        "m.range": ["kc.mean_ungrouped_data", "kc.algebraic_expressions",
                    "kc.fraction_decimal_operations", "kc.integer_arithmetic"],
        "m.variance_sd": ["kc.mean_ungrouped_data", "kc.algebraic_expressions",
                          "kc.integer_arithmetic", "kc.equations_in_indices"],
    }
    for mid, mlab in spans.items():
        m = Method(id=mid, label=mlab, task_model_id=t2.id, subject=SUBJ,
                   status=ClaimStatus.ACCEPTED, created_by_activity=interp,
                   cdg_version="v0.2.0")
        m.reviewed_by_activity = rev
        s.add_entity(m)
        c = Claim(id=f"cl.m58.own.{mid}", predicate=RelationshipType.HAS_METHOD,
                  subject_id=t2.id, object_id=mid, claim_type=ClaimType.ASSESSMENT_DESIGN,
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, "method ownership", ASSESS, rev))
        for r in reqs[mid]:
            c = Claim(id=f"cl.m58.req.{mid}.{r}", predicate=RelationshipType.REQUIRES,
                      subject_id=mid, object_id=r, claim_type=ClaimType.DEPENDENCY,
                      created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
            s.add_claim(accept(c, f"{mid} requires {r}", DEP, rev))
    c = Claim(id="cl.m58.target", predicate=RelationshipType.TARGETS, subject_id=t2.id,
              object_id=k2.id, claim_type=ClaimType.ASSESSMENT_DESIGN,
              created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, "targets dispersion", ASSESS, rev))
    for cid, subj, scope, ref in [
        ("cl.pre58.mean_disp", "kc.mean_ungrouped_data", P.SPECIFIC_TASK_MODEL, "tm.compute_dispersion"),
        ("cl.pre58.alg_disp", "kc.algebraic_expressions", P.SPECIFIC_TASK_MODEL, "tm.compute_dispersion"),
        ("cl.pre58.frac_disp", "kc.fraction_decimal_operations", P.SPECIFIC_TASK_MODEL, "tm.compute_dispersion"),
        ("cl.pre58.indices_disp", "kc.equations_in_indices", P.SPECIFIC_METHOD, "m.variance_sd"),
    ]:
        c = Claim(id=cid, predicate=RelationshipType.PREREQUISITE, subject_id=subj,
                  object_id=k2.id, claim_type=ClaimType.DEPENDENCY, purpose=E,
                  scope=scope, scope_ref=ref, origin=ClaimOrigin.DERIVED,
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, f"DERIVED per tm58/method requires ({subj})", DEP, rev))
    for eid, cid, src, exc, leg in [
        ("ev.m58.t", "cl.m58.target", "SRC.OSX.STAT2E.2.7",
         "Standard deviation measures overall variation in a data set.", None),
        ("ev.m58.m2", "cl.m58.own.m.variance_sd", "SRC.OSX.STAT2E.2.7",
         "Variance and standard deviation quantify deviation from the mean.", None),
        ("ev.m58.leg1", "cl.m58.target", "SRC.JAMB.UTME.MATH",
         "Node listed/entailed in JAMB syllabus: V.3", "E0591"),
        ("ev.m58.leg2", "cl.pre58.mean_disp", "SRC.JAMB.UTME.MATH",
         "Node listed/entailed in JAMB syllabus: V.3", "E0592"),
    ]:
        s.add_evidence(EvidenceItem(
            id=eid, claim_id=cid, source_id=src,
            role=EvidenceRole.INDIRECT, stance=EvidenceStance.SUPPORTS,
            locator=("legacy JAMB pointer" if leg else "openstax section"),
            excerpt=exc, excerpt_kind=ExcerptKind.PARAPHRASE,
            extracted_by_activity=interp, inherited_from_legacy=bool(leg), legacy_id=leg))
    s.add_entity(Item(id="it.mcq.sd", label="MCQ: range of data",
                      task_model_id=t2.id, subject=SUBJ,
                      stem="Range of 4, 9, 2, 13", options=["11", "9", "6", "28"],
                      key="11", status=ClaimStatus.ACCEPTED, created_by_activity=interp))
    return s
