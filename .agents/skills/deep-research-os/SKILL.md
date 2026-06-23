---
name: deep-research-os
description: Use for evidence-grounded deep research runs, reference atlases, technical landscape maps, literature reviews, market maps, idea-generation research, and strategic memos. Creates structured run artifacts before final synthesis.
---

# Deep Research OS Skill

You are operating with the R&D Lab OS workflow.

Your job is not to answer immediately. Your job is to create or update a structured research run.

The workflow has two modes:

- repo-local mode inside `rd-lab-os`, with runs under `runs/`;
- project-local mode for another repository or project, with runs under `.heurema/rdlab/runs/`.

Do not create `.rdlab/`. The canonical project-local lab path is `.heurema/rdlab/`.

## Core principles

- Scope first, answer last.
- Evidence ledger first, final memo second.
- Prefer primary sources when available.
- Separate evidence from interpretation.
- Preserve contradictions and uncertainty.
- Do not hallucinate sources, papers, repos, dates, authors, benchmarks, or metrics.
- Do not turn references into dependencies without explicit justification.
- Use existing frontier-agent subscriptions and coding agents as workers; do not train models.

## Required artifact chain

For each legacy repo-local research run, create or update:

```text
00_spec.md
01_question_graph.md
02_source_map.md
03_evidence_ledger.csv
04_contradictions.md
05_synthesis.md
06_critic_review.md
07_final_memo.md
08_decision_log.md
```

For each project-local `project_lab` run, create or update:

```text
00_spec.md
01_question_graph.md
02_source_map.md
03_evidence_ledger.csv
04_change_log.md
05_contradictions.md
06_synthesis.md
07_ideas.md
08_experiments.md
09_critic_review.md
10_final_memo.md
11_decision_log.md
12_memory_update.md
```

## Workflow

1. Create a run folder with `scripts/new_run.py` unless one already exists.
   - Repo-local: `python3 scripts/new_run.py "<topic>"`
   - Project-local: `python3 scripts/new_run.py "<topic>" --project-root <project-root>`
2. Fill `00_spec.md` with topic, decision context, scope, non-scope, success criteria, assumptions, and open questions.
3. Fill `01_question_graph.md` with root question, sub-questions, perspectives, controversies, and evidence gaps.
4. Build `02_source_map.md`; rank sources by source mode and trust level.
5. Populate `03_evidence_ledger.csv` before writing conclusions.
6. Preserve source conflicts, weak evidence, stale claims, missing primary sources, and open uncertainties.
7. Write synthesis only from the evidence ledger and source map.
8. Run an adversarial critic pass.
9. Write the final memo as a decision-grade memo with traceability to the ledger.
10. Update the decision log and memory files only if the run produces durable decisions or patterns.

When operating on a project-local lab, read `.heurema/rdlab/rdlab.toml`,
`.heurema/rdlab/sources.toml`, and `.heurema/rdlab/topics.toml` when present.

## Source modes

Always label source mode:

- academic
- official_docs
- code_repo
- benchmark
- product_docs
- market_news
- social_signal
- expert_blog
- internal_doc
- unknown

Do not mix social signal evidence with academic or official evidence without labeling the difference.

## Validation

Before claiming completion, run:

```bash
python3 scripts/validate_run.py runs/<run-folder>
```

For project-local runs:

```bash
python3 scripts/validate_project.py <project-root>
python3 scripts/validate_run.py <project-root>/.heurema/rdlab/runs/<run-folder>
```

If validation fails, fix the artifacts or clearly report what remains incomplete.
