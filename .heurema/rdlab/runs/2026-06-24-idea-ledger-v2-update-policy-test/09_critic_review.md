# 09 Critic Review

## Critical issues

- Do not promote v2 to templates yet.
- Do not remove update policy just because it makes CSV wider.

## Medium issues

- Status vocabulary is still informal.
- `candidate_validated_once` may need a shorter canonical status.
- A validator may be needed before multiple agents edit the ledger.

## Minor issues

- `status_update_reason` wording differs between providers but semantics match.

## Missing primary sources

- No downstream implementation-planning run has consumed v2 yet.
- No validator exists yet.

## Unsupported claims

- "Template-ready" is not supported.
- "Final schema" is not supported.

## Provider / critic debate

| Reviewer | Provider / role | Main objection | Change made or reason rejected |
|---|---|---|---|
| Agy | v2 handoff updater | Preserved status because no new evidence rows were present. | Accepted as successful policy behavior. |
| Claude Haiku | v2 handoff updater | Preserved status because no new evidence rows were present. | Accepted as independent confirmation. |
| Codex | synthesis owner | Policy fixed safety issue but schema may be too wide. | Deferred template promotion; proposed validator/status docs. |

## Overconfident recommendations

- Avoid "ship it to templates now".
- Avoid "no validator needed"; repeated agent edits still need guardrails.

## Final confidence rating

High that v2 prevents the observed unsupported status upgrade.

Medium that v2 is ready for general use.
