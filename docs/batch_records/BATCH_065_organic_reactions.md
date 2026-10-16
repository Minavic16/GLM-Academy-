# Batches 065 — Chemistry organic-reactions wave (Phase 15)

Builder: `examples/chemistry_organic_reactions.py` (`build_graph_v39`,
chains `build_graph_v38`). Batch 065 is the only batch added by Phase 15.

| KC | TM / Methods | Key prerequisites |
|---|---|---|
| kc.reactions_of_alkanes | tm.alkane_reactions / m.combustion_analysis, m.fuel_comparison | UNDERSTAND: kc.organic_foundations; EXECUTE: kc.mole_stoichiometry → tm.alkane_reactions |
| kc.reactions_of_alkenes | tm.alkene_reactions / m.addition_reactions | UNDERSTAND: kc.organic_foundations |
| kc.isomerism | tm.isomer_identification / m.isomer_comparison | UNDERSTAND: kc.organic_foundations |
| kc.alcohols | tm.alcohol_properties / m.alcohol_structure, m.alcohol_naming | UNDERSTAND: kc.organic_foundations |
| kc.ethers | tm.ether_properties / m.ether_structure | UNDERSTAND: kc.organic_foundations |
| kc.aldehydes_ketones | tm.aldehyde_reactions / m.nucleophilic_addition, m.oxidation_reduction | UNDERSTAND: kc.organic_foundations |
| kc.carboxylic_acids | tm.carboxylic_acid_reactions / m.esterification | UNDERSTAND: kc.organic_foundations |
| kc.amines | tm.amine_properties / m.amine_naming, m.amine_properties | UNDERSTAND: kc.organic_foundations |
| kc.amides | tm.amide_reactions / m.amide_reactions | UNDERSTAND: kc.organic_foundations |

All prerequisite edges are PREREQUISITE claims with `purpose`/`scope`/
`origin` qualifiers (8 UNDERSTAND / ALL_RELEVANT_METHODS/ASSERTED;
1 EXECUTE / SPECIFIC_TASK_MODEL/DERIVED). All are Chemistry-internal —
Phase 15 forbids new cross-subject dependency claims, so no edge
references a Mathematics or Physics entity.

Sources (verified HTTP 200 before citation): OpenStax Chemistry 2e
20-1 Hydrocarbons, 20-2 Alcohols and Ethers, 20-3 Aldehydes,
Ketones, Carboxylic Acids and Esters, 20-4 Amines and Amides.
