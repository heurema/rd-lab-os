# 06 Synthesis

## Summary

`idea_ledger_v2.csv` fixed the previous handoff safety failure. Both Agy and
Claude preserved status when row-level update policy said not to promote without
new evidence.

## Findings

1. `allowed_statuses`, `update_policy`, and `status_update_reason` are useful.
   Evidence: V2-2.
2. Agy no longer over-promoted I1. Evidence: V2-3.
3. Claude remained evidence-disciplined. Evidence: V2-4.
4. No idea should be promoted from this run alone. Evidence: V2-5.

## Recommendation

Keep `idea_ledger_v2.csv` as the current best run-local handoff shape.

Do not promote it to `templates/run_project_lab/` yet. First decide whether to:

- add a small validator for idea ledger status/policy;
- define status vocabulary in docs;
- run one practical implementation-planning pass using v2 as input.

## Confidence

High that update policy prevents the observed unsupported status upgrade.

Medium that the v2 schema is the final shape, because it is wider and may need a
validator or policy document.
