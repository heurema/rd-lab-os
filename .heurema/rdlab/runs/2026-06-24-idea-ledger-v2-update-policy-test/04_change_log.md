# 04 Change Log

## New artifacts

- `idea_ledger_v2_input.csv`
- `agy_v2_handoff_output.csv`
- `claude_v2_handoff_output.csv`
- `idea_ledger_v2_normalized.csv`

## Schema changes

Added columns:

- `allowed_statuses`
- `update_policy`
- `status_update_reason`

## Provider behavior

| Provider | Prior behavior | V2 behavior |
|---|---|---|
| Agy | Over-promoted I1 to `validated`. | Preserved all statuses. |
| Claude | Preserved status without new evidence. | Preserved all statuses again. |

## Normalization

No provider output required status correction. The normalized ledger only
rewrites evidence row references to this run's `V2-*` rows.
