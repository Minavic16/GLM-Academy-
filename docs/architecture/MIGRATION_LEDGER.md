# Migration Ledger (Phase 3, metadata only)

No legacy records have been migrated into the v0.2 graph as authoritative
data. Legacy disposition below reflects actual use in the pipeline so far.

| Disposition | Legacy material | Notes |
|---|---|---|
| MAPPED (as inherited evidence only) | Evidence records E0089, E0098, E0099, E0100, E0112, E0119, E0120, E0122–E0124, E0126–E0129, E0131, E0134–E0139, E0153, E0156, E0168, E0207, E0297, E0298, E0309, E0043, E0083, E0084, E0019, E0020, E0227, E0230, E0247, E0248, E0257, E0261, E0262, E0264, E0583, E0308, E0312, E0310, E0318, E0319, E0321, E0322, E0325, E0326, E0375, E0376, E0283, E0285, E0286, E0254, E0255, E0233, E0252, E0253, E0033, E0034, E0211, E0265, E0249, E0364, E0365 | ~58 legacy evidence items carried into v0.2 as `EvidenceItem.inherited_from_legacy=True` with `legacy_id` preserved across batches 001–023. Original assertions/statuses not overwritten. |
| PENDING_REVIEW | All other legacy nodes (~150), edges (~275), evidence (~590) | Remain out of the v0.2 graph until individually dispositioned. |
| RETIRED | none yet | `related_to` edges (10) and `applies_to` (1) are candidates for RETIRED disposition. |
| REJECTED | none decided yet | No rejection decisions made without owner/reviewer input. |

The legacy graph remains outside the CDG store. `MigrationRecord`
metadata is produced only when a record is actually dispositioned.
