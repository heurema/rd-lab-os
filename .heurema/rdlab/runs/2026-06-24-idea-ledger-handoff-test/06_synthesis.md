# 06 Synthesis

## Summary

The ledger passed the minimal handoff test: providers could parse it and act on
it without chat history. The test also exposed a schema gap: status updates need
explicit evidence/update policy.

## Findings

1. Agy returned a valid updated CSV, proving the ledger can function as a
   handoff artifact. Evidence: H3.
2. Agy also over-promoted I1 to `validated`, showing that the schema permits
   unsupported status inflation. Evidence: H4.
3. Claude returned the ledger unchanged and explicitly refused to update without
   new evidence, which aligns better with evidence-ledger discipline. Evidence:
   H5.
4. The normalized result should mark I1 as `candidate_validated_once`, not
   `validated`. Evidence: H6.

## Schema implication

The next ledger version should add either:

```text
update_policy
```

or a separate small Markdown policy section that defines when `status` and
`critic_verdict` may change.

## Confidence

Medium-high that `idea_ledger.csv` is useful as a handoff artifact.

Medium that the current schema is sufficient; it needs one more policy field or
status vocabulary definition before template promotion.
