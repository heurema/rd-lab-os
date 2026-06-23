# Codex Instructions

## What Codex should do

Codex is the builder and normalizer for the lab. It should:

- create run folders;
- maintain templates;
- write validators;
- normalize source maps and evidence ledgers;
- inspect code repos referenced by research;
- create small deterministic scripts;
- enforce artifact completeness.

## What Codex should not do in v0

- Do not create a full backend.
- Do not create a UI/dashboard.
- Do not add vector databases.
- Do not deploy GraphRAG.
- Do not train or fine-tune models.
- Do not automate paid product UIs.

## Default first move for any research task

Repo-local task:

```bash
python3 scripts/new_run.py "<topic>"
```

Project-local task:

```bash
python3 scripts/init_project.py <project-root>
python3 scripts/new_run.py "<topic>" --project-root <project-root>
```

Then fill:

1. `00_spec.md`
2. `01_question_graph.md`
3. `02_source_map.md`

Only after those exist should the evidence ledger and synthesis begin.

For project-local work, use `.heurema/rdlab/` as the canonical path. Do not create `.rdlab/`.
