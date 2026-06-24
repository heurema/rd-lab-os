# 08 Experiments

## Candidate experiments

| ID | Hypothesis | Method | Evidence rows | Success criteria | Risk |
|---|---|---|---|---|---|
| X1e | A small validator is enough to make v2 ledger safe for repeated use. | Write a project-local or core `validate_idea_ledger.py` that checks required columns and status membership. | V2-2,V2-5,V2-6 | Invalid status or missing update_policy fails. | Validator may imply premature template support. |
| X1f | v2 ledger can drive implementation planning without reading prior memos. | Give only `idea_ledger_v2_normalized.csv` to a provider and ask for a one-step implementation plan. | V2-3,V2-4,V2-5 | Provider chooses validator/docs next without unsupported promotion. | Provider may still infer too much. |

## Experiment backlog

1. Run X1f before changing code.
2. If X1f succeeds, add `validate_idea_ledger.py`.
3. Defer template promotion until validator and status docs exist.

## Experiments not worth running

- Debate script now.
- UI/reporting around idea ledgers.
- Discussion import.
