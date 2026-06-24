# 07 Ideas

## Candidate ideas

| ID | Idea | Evidence rows | Confidence | Next step |
|---|---|---|---|---|
| I1 | Add `scripts/validate_idea_ledger.py`. | P2,P3,P4,P5,P6 | high | Implement as the next code change. |
| I2 | Add status semantics docs after validator contract stabilizes. | P1,P6,P7 | medium | Defer until validator exists. |

## Rejected ideas

| Idea | Reason |
|---|---|
| Reuse `scripts/validate_ledger.py` for idea ledger | Existing file validates evidence ledger semantics. Evidence: P4. |
| Promote idea ledger to templates now | Validator and status docs do not exist yet. Evidence: P7. |

## Open idea questions

- Should strict mode require `status_update_reason` for all rows or only rows
  changed by a provider?
- Should the validator check evidence row ID formats?
