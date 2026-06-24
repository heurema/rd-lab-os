# 12 Memory Update

## Promote now

Do not update global memory.

## Candidate project-local memory

After validator implementation succeeds:

```text
For rd-lab-os idea ledgers, validate idea status separately from evidence
ledger validation. Use scripts/validate_idea_ledger.py, not
scripts/validate_ledger.py.
```

## Do not promote

- Template promotion as accepted.
- Debate automation as next implementation.

## Follow-up trigger

Promote only after `scripts/validate_idea_ledger.py` is implemented and passes
valid/invalid fixture checks.
