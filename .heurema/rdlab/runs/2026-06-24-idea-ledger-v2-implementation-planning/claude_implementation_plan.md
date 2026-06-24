# Claude Implementation Plan

## verdict

Implement a validator to enforce `allowed_statuses` and `update_policy`
constraints for the idea ledger.

## why

The ledger explicitly blocks other work on this requirement. I1 identifies
unsupported status upgrades as its main risk, and I3 states: test score columns
only after update policy prevents status inflation. Building a validator is the
smallest safe step before template promotion.

## files_to_change

- `scripts/validate_run.py` or a new `scripts/validate_ledger.py`
- schema documentation for the idea ledger

## tests

1. A test ledger that attempts an invalid status upgrade must fail validation.
2. A test ledger with a valid status transition must pass validation.

## explicit_deferred

- I1 template promotion
- I2 debate automation
- I3 score columns
- I4 pipeline report
- I5 change brief generator
- I6 discussion import parser
