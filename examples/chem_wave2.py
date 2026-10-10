"""Phase 13 Chemistry wave 2: batches 048-052 (redox/electrochemistry,
energetics, rates/equilibrium, gases, organics, practical). Chains v33."""
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
from examples.chem_wave1 import (build_graph_v33, _base, _src, _kc, _tm, _m,
                                 _pre, _ev, _item, E, P, DEP)


def build_graph_v34() -> CDGStore:
    s = build_graph_v33()
    if "SRC.WAEC.CHEMISTRY" not in s.sources:
        s.add_source(Source(id="SRC.WAEC.CHEMISTRY", title="WAEC WASSCE Chemistry Syllabus",
                            identifier_or_url="https://www.waec.ng",
                            publisher="exam-board/curriculum body",
                            source_type=SourceType.SYLLABUS, tier="primary",
                            retrieved_at=None))

    # ---- 048 redox/electrochemistry ----
    interp, rev = _base(s, "48", "Human review of redox batch.")
    _src(s, "SRC.OSX.CHEM2E.17.1", "OpenStax Chemistry 2e, 17.1 Review of Redox Chemistry",
         "https://openstax.org/books/chemistry-2e/pages/17-1-review-of-redox-chemistry")
    _src(s, "SRC.OSX.CHEM2E.17.7", "OpenStax Chemistry 2e, 17.7 Electrolysis",
         "https://openstax.org/books/chemistry-2e/pages/17-7-electrolysis")
    _kc(s, interp, rev, "kc.redox_electrochemistry", "Redox reactions and electrolysis",
        "Assign oxidation numbers; identify redox; compute electrolysis quantities.")
    _tm(s, interp, rev, "tm.redox_problems", "Solve redox and electrolysis problems",
        ["kc.redox_electrochemistry"])
    _m(s, interp, rev, "m.redox_identification", "Track oxidation-number changes",
       "tm.redox_problems", ["kc.chemical_bonding", "kc.integer_arithmetic"])
    _m(s, interp, rev, "m.electrolysis_quantitative", "Relate charge, moles and mass deposited",
       "tm.redox_problems", ["kc.mole_stoichiometry", "kc.electric_circuits"])
    _pre(s, interp, rev, "cl.pre48.bonding_redox", "kc.chemical_bonding", "kc.redox_electrochemistry",
         E, P.SPECIFIC_METHOD, "m.redox_identification",
         ClaimOrigin.DERIVED, "DERIVED: oxidation numbers need formulae (bonding)")
    _pre(s, interp, rev, "cl.pre48.mole_redox", "kc.mole_stoichiometry", "kc.redox_electrochemistry",
         E, P.SPECIFIC_METHOD, "m.electrolysis_quantitative",
         ClaimOrigin.DERIVED, "DERIVED: electrolysis quantities need mole")
    _pre(s, interp, rev, "cl.pre48.circuits_redox", "kc.electric_circuits", "kc.redox_electrochemistry",
         E, P.SPECIFIC_METHOD, "m.electrolysis_quantitative",
         ClaimOrigin.DERIVED, "Physics→Chemistry: electrolysis needs current/voltage ideas")
    _ev(s, interp, "ev.c48.t", "cl.ctm.redox_problems.target.kc.redox_electrochemistry",
         "SRC.OSX.CHEM2E.17.1", "Oxidation is loss of electrons; reduction is gain.", False)
    _ev(s, interp, "ev.c48.m2", "cl.c.own.m.electrolysis_quantitative",
         "SRC.OSX.CHEM2E.17.7", "Mass deposited proportional to charge passed.", False)

    # ---- 049a energetics ----
    interp, rev = _base(s, "49a", "Human review of energetics batch.")
    _src(s, "SRC.OSX.CHEM2E.5.1", "OpenStax Chemistry 2e, 5.1 Energy Basics",
         "https://openstax.org/books/chemistry-2e/pages/5-1-energy-basics")
    _kc(s, interp, rev, "kc.chemical_energetics", "Energy changes in chemical reactions",
        "Classify exo/endothermic changes; apply Hess's-law cycles with mole quantities.")
    _tm(s, interp, rev, "tm.energetics_problems", "Solve reaction-energy problems",
        ["kc.chemical_energetics"])
    _m(s, interp, rev, "m.enthalpy_hess", "Combine enthalpies around a Hess cycle",
       "tm.energetics_problems", ["kc.mole_stoichiometry", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre49a.mole_energetics", "kc.mole_stoichiometry", "kc.chemical_energetics",
         E, P.SPECIFIC_METHOD, "m.enthalpy_hess",
         ClaimOrigin.DERIVED, "DERIVED: per-mole enthalpies need mole")
    _ev(s, interp, "ev.c49a.t", "cl.ctm.energetics_problems.target.kc.chemical_energetics",
         "SRC.OSX.CHEM2E.5.1", "Enthalpy change is heat at constant pressure.", False)

    # ---- 049b rates/equilibrium ----
    interp, rev = _base(s, "49b", "Human review of rates/equilibrium batch.")
    _src(s, "SRC.OSX.CHEM2E.12.1", "OpenStax Chemistry 2e, 12.1 Chemical Reaction Rates",
         "https://openstax.org/books/chemistry-2e/pages/12-1-chemical-reaction-rates")
    _src(s, "SRC.OSX.CHEM2E.13.1", "OpenStax Chemistry 2e, 13.1 Chemical Equilibria",
         "https://openstax.org/books/chemistry-2e/pages/13-1-chemical-equilibria")
    _kc(s, interp, rev, "kc.rates_equilibrium", "Reaction rates and chemical equilibrium",
        "Read rate curves; predict equilibrium shifts (Le Chatelier).")
    _tm(s, interp, rev, "tm.rate_equilibrium_problems", "Interpret rates and equilibria",
        ["kc.rates_equilibrium"])
    _m(s, interp, rev, "m.rate_curves", "Read concentration-time rate curves",
       "tm.rate_equilibrium_problems", ["kc.function_concept", "kc.algebraic_expressions"])
    _m(s, interp, rev, "m.le_chatelier", "Predict shift from concentration/temperature change",
       "tm.rate_equilibrium_problems", ["kc.chemical_bonding"])
    _pre(s, interp, rev, "cl.pre49b.fn_rates", "kc.function_concept", "kc.rates_equilibrium",
         E, P.SPECIFIC_METHOD, "m.rate_curves",
         ClaimOrigin.DERIVED, "Math→Chemistry: rate curves need graph/function reading")
    _ev(s, interp, "ev.c49b.t", "cl.ctm.rate_equilibrium_problems.target.kc.rates_equilibrium",
         "SRC.OSX.CHEM2E.12.1", "Rate measured as concentration change over time.", False)
    _ev(s, interp, "ev.c49b.m2", "cl.c.own.m.le_chatelier",
         "SRC.OSX.CHEM2E.13.1", "Systems at equilibrium counteract imposed changes.", False)

    # ---- 050 gases ----
    interp, rev = _base(s, "50", "Human review of gases batch.")
    _src(s, "SRC.OSX.CHEM2E.9.2", "OpenStax Chemistry 2e, 9.2 Relating Pressure, Volume, Amount, and Temperature: The Ideal Gas Law",
         "https://openstax.org/books/chemistry-2e/pages/9-2-relating-pressure-volume-amount-and-temperature-the-ideal-gas-law")
    _kc(s, interp, rev, "kc.gas_behaviour", "Gas laws and molar gas volumes",
        "Apply Boyle's/Charles'/combined laws and PV = nRT with molar quantities.")
    _tm(s, interp, rev, "tm.gas_problems", "Solve gas-law problems",
        ["kc.gas_behaviour"])
    _m(s, interp, rev, "m.combined_gas_law", "Relate P, V, n, T across two states",
       "tm.gas_problems", ["kc.mole_stoichiometry", "kc.ratio_proportion_rate", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre50.mole_gases", "kc.mole_stoichiometry", "kc.gas_behaviour",
         E, P.SPECIFIC_TASK_MODEL, "tm.gas_problems",
         ClaimOrigin.DERIVED, "DERIVED: gas quantities need mole")
    _pre(s, interp, rev, "cl.pre50.ratio_gases", "kc.ratio_proportion_rate", "kc.gas_behaviour",
         E, P.SPECIFIC_TASK_MODEL, "tm.gas_problems",
         ClaimOrigin.DERIVED, "Math→Chemistry: gas proportions need ratio reasoning")
    _ev(s, interp, "ev.c50.t", "cl.ctm.gas_problems.target.kc.gas_behaviour",
         "SRC.OSX.CHEM2E.9.2", "Ideal gas law relates pressure, volume, moles and temperature.", False)

    # ---- 051 organics ----
    interp, rev = _base(s, "51", "Human review of organics batch.")
    _src(s, "SRC.OSX.CHEM2E.20.1", "OpenStax Chemistry 2e, 20.1 Hydrocarbons",
         "https://openstax.org/books/chemistry-2e/pages/20-1-hydrocarbons")
    _kc(s, interp, rev, "kc.organic_foundations", "Hydrocarbons and functional groups",
        "Name simple alkanes/alkenes; recognise key functional groups.")
    _tm(s, interp, rev, "tm.organic_problems", "Name hydrocarbons and classify groups",
        ["kc.organic_foundations"])
    _m(s, interp, rev, "m.hydrocarbon_naming", "Name chains by longest chain + substituents",
       "tm.organic_problems", ["kc.chemical_bonding"])
    _pre(s, interp, rev, "cl.pre51.bonding_organic", "kc.chemical_bonding", "kc.organic_foundations",
         E, P.SPECIFIC_TASK_MODEL, "tm.organic_problems",
         ClaimOrigin.DERIVED, "DERIVED: C–C/C–H bonding precedes organic naming")
    _ev(s, interp, "ev.c51.t", "cl.ctm.organic_problems.target.kc.organic_foundations",
         "SRC.OSX.CHEM2E.20.1", "Hydrocarbons contain carbon and hydrogen only.", False)
    _item(s, interp, "it.chem.organic", "tm.organic_problems",
          "The first member of the alkene series is…",
          ["ethene", "methene", "propene", "butene"], "ethene")

    # ---- 052 practical ----
    interp, rev = _base(s, "52", "Human review of practical-chemistry batch.")
    _src(s, "SRC.OSX.CHEM2E.14.7", "OpenStax Chemistry 2e, 14.7 Acid-Base Titrations",
         "https://openstax.org/books/chemistry-2e/pages/14-7-acid-base-titrations")
    _kc(s, interp, rev, "kc.practical_chemistry", "Practical chemistry procedures",
        "Carry out titrations; record observations; report qualitative test results.")
    _tm(s, interp, rev, "tm.practical_chemistry", "Perform titration and qualitative tests",
        ["kc.practical_chemistry"])
    _m(s, interp, rev, "m.titration_procedure", "Run a titration to an indicator endpoint",
       "tm.practical_chemistry", ["kc.acids_bases_salts", "kc.measurement_units_dimensions"])
    _m(s, interp, rev, "m.qualitative_tests", "Report flame/precipitate/gas test observations",
       "tm.practical_chemistry", ["kc.matter_classification"])
    _pre(s, interp, rev, "cl.pre52.acids_practical", "kc.acids_bases_salts", "kc.practical_chemistry",
         E, P.SPECIFIC_METHOD, "m.titration_procedure",
         ClaimOrigin.DERIVED, "DERIVED: titration procedure needs acid/base ideas")
    _pre(s, interp, rev, "cl.pre52.matter_practical", "kc.matter_classification", "kc.practical_chemistry",
         E, P.SPECIFIC_METHOD, "m.qualitative_tests",
         ClaimOrigin.DERIVED, "DERIVED: qualitative tests need matter ideas")
    _ev(s, interp, "ev.c52.t", "cl.ctm.practical_chemistry.target.kc.practical_chemistry",
         "SRC.OSX.CHEM2E.14.7", "Titration determines unknown concentration from a standard.", False)
    _ev(s, interp, "ev.c52.waec", "cl.ctm.practical_chemistry.target.kc.practical_chemistry",
         "SRC.WAEC.CHEMISTRY", "WAEC chemistry practical paper assesses titration and qualitative analysis (detail pending official PDF).",
         locator="WAEC practical requirement (detail unverified)", direct=False)
    return s
