# 06 Synthesis

## Summary

`idea_ledger_v2_normalized.csv` successfully drove the expected implementation
choice from provider-only handoff: build a validator before template promotion.

## Findings

1. Providers converged on validator/docs before templates. Evidence: P2,P3.
2. The exact validator name must be `validate_idea_ledger.py`, not
   `validate_ledger.py`, because the latter already validates evidence ledgers.
   Evidence: P4,P5.
3. The smallest useful validator scope is status membership and required policy
   fields. Evidence: P6.
4. Everything else remains deferred. Evidence: P7.

## Recommended next implementation

Add `scripts/validate_idea_ledger.py` with focused CSV validation:

- required columns;
- duplicate `idea_id` detection;
- `status in allowed_statuses.split("|")`;
- non-empty `update_policy`;
- non-empty `status_update_reason` in strict mode.

## Confidence

High. Both independent providers selected the same class of next step, and repo
inspection clarified the filename.
