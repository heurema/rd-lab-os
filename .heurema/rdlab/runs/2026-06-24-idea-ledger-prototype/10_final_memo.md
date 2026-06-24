# 10 Final Memo

## Decision

Keep `idea_ledger.csv` as a run-local experimental artifact for now.

## Recommendation

Do one more run-local test before changing templates. The next test should use
the ledger as the only idea handoff artifact and ask providers to update
`status`, `critic_verdict`, and `next_test`.

## What to change now

Nothing in global templates yet.

## What to use next

Use:

```text
idea_ledger.csv
```

Optionally use:

```text
idea_scorecard.csv
```

Do not promote `idea_scorecard.csv` until score fields prove useful.

## Deferred

- `scripts/debate_ideas.py`
- `scripts/pipeline_report.py`
- change brief generator
- discussion import

## Evidence

L1-L7.
