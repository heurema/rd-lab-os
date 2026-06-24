# Idea Ledger

The idea ledger is an optional run-local artifact for project-lab runs that
generate, compare, or discuss product/research ideas.

It does not replace `03_evidence_ledger.csv`. The evidence ledger remains the
source of truth for claims and source support. The idea ledger tracks idea
status, allowed status changes, and the reason a status changed or did not
change.

## When To Use

Use an idea ledger when a run has multiple candidate ideas, provider debate, or
follow-up experiments.

Do not require it for every research run.

## Template

```text
templates/idea_ledger/idea_ledger_v2.csv
```

Copy it into a project-local run when needed:

```text
<project>/.heurema/rdlab/runs/<run>/idea_ledger_v2.csv
```

Then replace the example row with real ideas.

## Required Columns

- `idea_id`: stable ID for the idea.
- `title`: short human-readable name.
- `premise`: what the idea claims could be useful.
- `evidence_rows`: evidence ledger row IDs that support or constrain the idea.
- `status`: current idea status.
- `allowed_statuses`: pipe-separated status values allowed for this row.
- `update_policy`: rule for when the status may change.
- `next_test`: smallest useful next action.
- `main_risk`: primary reason the idea may be wrong or premature.
- `critic_verdict`: critic summary.
- `status_update_reason`: why the current status is preserved or changed.

## Status Values

`candidate`: worth considering, but not validated.

`candidate_validated_once`: passed one narrow handoff or critique test, but is
not ready for template or product promotion.

`candidate_modified`: still viable, but the shape or scope changed after
critique.

`deferred`: plausible, but prerequisites are missing.

`deferred_until_repeated_manual_debate`: plausible automation, but only after
manual provider debate repeats and creates real friction.

`stopped`: do not continue unless new evidence changes the constraint.

`promoted`: accepted into a durable template, script, docs, memory, or roadmap
artifact after evidence supports it.

## Update Rules

- Do not change `status` unless `update_policy` allows it.
- Do not promote an idea because a provider likes it.
- Do not promote without new evidence rows or a completed test named in
  `next_test`.
- If no new evidence exists, preserve `status` and write that in
  `status_update_reason`.
- Keep `allowed_statuses` narrow for each row.

## Validation

```bash
python3 scripts/validate_idea_ledger.py <path-to-idea-ledger.csv> --strict
```

The validator checks structure and status rules only. It does not judge whether
an idea is good.
