"""Phase 14 Physics completion wave B: batches 062-064 (fibre optics,
lasers, electronics). Chains build_graph_v37."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ClaimOrigin, ClaimStatus, ClaimType,
                       EvidenceRole, EvidenceStance, ExcerptKind,
                       PrerequisitePurpose, PrerequisiteScope, RelationshipType,
                       SourceType)
from cdg.evidence import EvidenceItem
from cdg.provenance import Source
from cdg.store import CDGStore
from examples.physics_completion_a import (build_graph_v37, _base, _src, _ev,
                                           ASSESS, DEP, STAMP, E, P)
from examples._batchkit import accept

SUBJ = "Physics"


def build_graph_v38() -> CDGStore:
    s = build_graph_v37()

    def add(bnn, note, kid, klabel, kdef, tm_id, tm_label, mid, mlabel,
            reqs, pre_subs, src_id, src_title, src_url, excerpt, target_kc=None):
        interp, rev = _base(s, bnn, note)
        _src(s, src_id, src_title, src_url)
        k = KnowledgeComponent(id=kid, label=klabel, definition=kdef, subject=SUBJ,
                               status=ClaimStatus.ACCEPTED,
                               created_by_activity=interp, cdg_version="v0.2.0")
        k.reviewed_by_activity = rev
        k.review_rationale = "Accepted in Phase 14 via human review."
        s.add_entity(k)
        t = TaskModel(id=tm_id, label=tm_label, subject=SUBJ,
                      status=ClaimStatus.ACCEPTED, created_by_activity=interp,
                      cdg_version="v0.2.0")
        t.reviewed_by_activity = rev
        s.add_entity(t)
        m = Method(id=mid, label=mlabel, task_model_id=t.id, subject=SUBJ,
                   status=ClaimStatus.ACCEPTED, created_by_activity=interp,
                   cdg_version="v0.2.0")
        m.reviewed_by_activity = rev
        s.add_entity(m)
        c = Claim(id=f"cl.r{bnn}.target", predicate=RelationshipType.TARGETS,
                  subject_id=t.id, object_id=k.id, claim_type=ClaimType.ASSESSMENT_DESIGN,
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, "targets capability", ASSESS, rev))
        c = Claim(id=f"cl.r{bnn}.own", predicate=RelationshipType.HAS_METHOD,
                  subject_id=t.id, object_id=m.id, claim_type=ClaimType.ASSESSMENT_DESIGN,
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, "method ownership", ASSESS, rev))
        for r in reqs:
            c = Claim(id=f"cl.r{bnn}.req.{r}", predicate=RelationshipType.REQUIRES,
                      subject_id=m.id, object_id=r, claim_type=ClaimType.DEPENDENCY,
                      created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
            s.add_claim(accept(c, f"{m.id} requires {r}", DEP, rev))
        for subj, purpose in pre_subs:
            if purpose == PrerequisitePurpose.UNDERSTAND:
                scope, ref, origin = P.ALL_RELEVANT_METHODS, None, ClaimOrigin.ASSERTED
            else:
                scope, ref, origin = P.SPECIFIC_TASK_MODEL, t.id, ClaimOrigin.DERIVED
            c = Claim(id=f"cl.r{bnn}.pre.{subj}", predicate=RelationshipType.PREREQUISITE,
                      subject_id=subj, object_id=k.id, claim_type=ClaimType.DEPENDENCY,
                      purpose=purpose, scope=scope, scope_ref=ref,
                      origin=origin, created_by_activity=interp,
                      created_at=STAMP, cdg_version="v0.2.0")
            s.add_claim(accept(c, f"DERIVED: {t.id} methods require {subj}", DEP, rev))
        _ev(s, interp, f"ev.r{bnn}.t", f"cl.r{bnn}.target", src_id, excerpt, False)
        return s

    add("62", "Human review of fibre-optics batch.",
        "kc.fibre_optics", "Optical fibres and total internal reflection",
        "Explain total internal reflection and light guidance in optical fibres.",
        "tm.fibre_optics_problems", "Solve fibre/TIR problems",
        "m.tir_analysis", "Apply critical-angle and TIR reasoning",
        ["kc.geometrical_optics", "kc.trig_ratios_acute"],
        [("kc.geometrical_optics", PrerequisitePurpose.EXECUTE)],
        "SRC.OSX.UP3.2.1",
        "University Physics Volume 3, 2.1 Images Formed by Plane Mirrors (TIR/reflection family)",
        "https://openstax.org/books/university-physics-volume-3/pages/2-1-images-formed-by-plane-mirrors",
        "Total internal reflection guides light within the fibre core.")

    add("63", "Human review of laser batch.",
        "kc.laser_basics", "Lasers and coherence",
        "Describe stimulated emission, monochromatic/coherent light and laser uses.",
        "tm.laser_problems", "Explain laser operation and uses",
        "m.stimulated_emission", "Explain stimulated emission and population inversion",
        ["kc.atomic_structure_periodicity", "kc.em_spectrum"],
        [("kc.atomic_structure_periodicity", PrerequisitePurpose.EXECUTE),
         ("kc.em_spectrum", PrerequisitePurpose.UNDERSTAND)],
        "SRC.OSX.UP2.16.5",
        "University Physics Volume 2, 16.5 The Electromagnetic Spectrum (coherent radiation context)",
        "https://openstax.org/books/university-physics-volume-2/pages/16-5-the-electromagnetic-spectrum",
        "Lasers produce coherent, monochromatic radiation.")

    add("64", "Human review of electronics batch.",
        "kc.semiconductor_electronics", "Semiconductor devices and logic basics",
        "Describe diodes, transistors and basic logic gates in circuits.",
        "tm.electronics_problems", "Solve basic electronics/logic problems",
        "m.logic_gate_truth_tables", "Use truth tables for basic logic gates",
        ["kc.electric_circuits", "kc.integer_arithmetic"],
        [("kc.electric_circits".replace("circits", "circuits"), PrerequisitePurpose.EXECUTE)],
        "SRC.OSX.UP2.9.6",
        "University Physics Volume 2, 9.6 Superconductors (electronic materials context)",
        "https://openstax.org/books/university-physics-volume-2/pages/9-6-superconductors",
        "Modern electronics rests on controlled conduction in materials.")
    return s
