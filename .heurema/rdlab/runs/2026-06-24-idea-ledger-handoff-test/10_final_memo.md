# 10 Final Memo

## Decision

The `idea_ledger.csv` handoff test passed for readability and continuity, but
failed the stricter safety bar for status updates.

## Recommendation

Create `idea_ledger_v2.csv` with explicit update policy before promoting the
artifact to templates.

## What happened

- Agy updated the ledger and preserved all idea IDs, but over-promoted I1.
- Claude refused to update without new evidence, which better matched the
  evidence-ledger philosophy.
- The normalized result keeps I1 as `candidate_validated_once`, not
  `validated`.

## Next task

Run X1c:

```text
Create idea_ledger_v2.csv with update_policy and allowed status semantics.
Repeat Agy/Claude handoff.
```

## Deferred

- Template promotion.
- `debate_ideas.py`.
- Scorecard/template work.

## Evidence

H1-H6.
