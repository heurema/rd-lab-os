# 12 Memory Update

## Promote now

Do not update global memory.

## Candidate project-local memory

After X1f succeeds, consider promoting:

```text
idea_ledger_v2.csv should include allowed_statuses, update_policy, and
status_update_reason. Provider updates must preserve status when no new evidence
rows satisfy update_policy.
```

## Do not promote

- v2 as global template-ready.
- `candidate_validated_once` as final status vocabulary.

## Follow-up trigger

Promote only after a downstream implementation-planning run uses v2 without
prior memo/chat context.
