# 10 Final Memo

## Decision

The next implementation should be `scripts/validate_idea_ledger.py`.

## Why

The v2 ledger led both providers to choose validator/docs before template
promotion. Local repo inspection shows `scripts/validate_ledger.py` already
means evidence-ledger validation, so idea-ledger validation needs its own file.

## Implementation scope

Add a stdlib-only CSV validator for idea ledgers:

- required columns;
- duplicate `idea_id` fails;
- `status` must be in `allowed_statuses`;
- `update_policy` is required;
- strict mode requires `status_update_reason`.

## Tests

- Current `idea_ledger_v2_normalized.csv` passes.
- Invalid status fixture fails.
- Missing update policy fixture fails.
- Duplicate idea ID fixture fails.

## Deferred

- Template promotion.
- Status docs.
- Debate automation.
- Scorecard/report/change-brief work.

## Evidence

P1-P7.
