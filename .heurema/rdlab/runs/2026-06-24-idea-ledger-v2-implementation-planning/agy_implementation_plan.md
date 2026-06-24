# Agy Implementation Plan

## verdict

Write the minimal validator that checks each row's `status` is included in
`allowed_statuses`.

## why

The ledger blocks score columns and template work until update policy prevents
status inflation. A mechanical validator is the smallest step with clear proof.

## files_to_change

- `scripts/validate_ledger.py` as a proposed new validator name from provider
  output.
- `scripts/smoke_test.py` if a smoke check is added.

## tests

- Invalid row: `status=promoted` and `allowed_statuses=candidate|deferred`
  should fail.
- Current normalized v2 ledger should pass.

## explicit_deferred

- Schema documentation until template work starts.
- Debate automation until manual debate repeats.
- Score fields until validation exists.
- Pipeline report until three runs exist.
- Change brief until a second snapshot exists.
- Discussion import remains stopped.
