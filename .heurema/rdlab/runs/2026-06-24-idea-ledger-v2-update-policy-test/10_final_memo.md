# 10 Final Memo

## Decision

`idea_ledger_v2.csv` passed the update-policy handoff test.

## Recommendation

Keep v2 as the current run-local idea ledger shape. Do not promote it to global
templates yet. Next, test whether `idea_ledger_v2_normalized.csv` can drive a
small implementation-planning pass without prior memo context.

## What changed

The previous ledger allowed Agy to over-promote I1. The v2 ledger added:

- `allowed_statuses`
- `update_policy`
- `status_update_reason`

Both Agy and Claude preserved statuses when no new evidence rows were present.

## Next task

Run X1f:

```text
Give only idea_ledger_v2_normalized.csv to a provider and ask for the smallest
implementation plan. The provider should choose validator/docs before template
promotion.
```

## Deferred

- Template promotion.
- `debate_ideas.py`.
- `pipeline_report.py`.
- Discussion import.

## Evidence

V2-1 through V2-6.
