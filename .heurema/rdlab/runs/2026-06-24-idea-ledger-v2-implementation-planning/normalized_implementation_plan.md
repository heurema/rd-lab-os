# Normalized Implementation Plan

## verdict

Implement a new stdlib-only `scripts/validate_idea_ledger.py` before template
promotion.

## why

Both providers converged on a validator before templates, score fields, debate
automation, or reporting. The exact provider suggestion to create or reuse
`scripts/validate_ledger.py` is unsafe because that file already validates the
evidence ledger. Idea ledgers and evidence ledgers need separate validators.

## files_to_change

1. Add `scripts/validate_idea_ledger.py`.
2. Add focused smoke coverage in `scripts/smoke_test.py` or a dedicated command
   check.
3. Document status semantics only after the validator shape is proven.

## validator scope

Required columns:

- `idea_id`
- `status`
- `allowed_statuses`
- `update_policy`
- `status_update_reason`

Initial checks:

- every non-empty row has `idea_id`;
- `status` is included in `allowed_statuses` split on `|`;
- `update_policy` is non-empty;
- `status_update_reason` is non-empty in strict mode;
- duplicate `idea_id` fails.

## tests

- Current `idea_ledger_v2_normalized.csv` passes.
- A fixture with invalid status fails.
- A fixture with missing `update_policy` fails.
- A fixture with duplicate `idea_id` fails.

## explicit_deferred

- Template promotion.
- `debate_ideas.py`.
- Score columns and scorecard templates.
- Pipeline report.
- Change brief generator.
- Discussion import.
