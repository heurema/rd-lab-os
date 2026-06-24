# 09 Critic Review

## Critical issues

- Do not overwrite or repurpose `scripts/validate_ledger.py`.
- Do not promote idea ledger templates before validation exists.

## Medium issues

- Provider output identified the correct kind of step but not the exact safe
  filename.
- Validator scope should stay narrow.

## Minor issues

- Provider plans did not inspect repo files; local inspection corrected naming.

## Missing primary sources

- No implementation exists yet.
- No invalid fixture exists yet.

## Unsupported claims

- "Idea ledger is template-ready" remains unsupported.
- "validate_run.py should validate idea ledgers" is not supported yet.

## Provider / critic debate

| Reviewer | Provider / role | Main objection | Change made or reason rejected |
|---|---|---|---|
| Claude Sonnet | implementation planner | Build a validator before template promotion. | Accepted. |
| Agy | implementation planner | Build minimal validator for `status in allowed_statuses`. | Accepted. |
| Codex | repo-normalizer | Existing `validate_ledger.py` is evidence-ledger-specific. | Renamed target to `validate_idea_ledger.py`. |

## Final confidence rating

High for next implementation: `scripts/validate_idea_ledger.py`.
