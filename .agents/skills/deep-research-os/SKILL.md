---
name: deep-research-os
description: Use for evidence-grounded deep research runs, reference atlases, technical landscape maps, literature reviews, market maps, idea-generation research, and strategic memos. Creates structured run artifacts before final synthesis.
---

# Deep Research OS Skill

You are operating inside the R&D Lab OS repository.

Your job is not to answer immediately. Your job is to create or update a structured research run.

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

For each research run, create or update:

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

## Workflow

1. Create a run folder with `scripts/new_run.py` unless one already exists.
2. Fill `00_spec.md` with topic, decision context, scope, non-scope, success criteria, assumptions, and open questions.
3. Fill `01_question_graph.md` with root question, sub-questions, perspectives, controversies, and evidence gaps.
4. Build `02_source_map.md`; rank sources by source mode and trust level.
5. Populate `03_evidence_ledger.csv` before writing conclusions.
6. Fill `04_contradictions.md` with source conflicts, weak evidence, stale claims, missing primary sources, and open uncertainties.
7. Write `05_synthesis.md` only from the evidence ledger and source map.
8. Run an adversarial pass in `06_critic_review.md`.
9. Write `07_final_memo.md` as a decision-grade memo with traceability to the ledger.
10. Update `08_decision_log.md` and memory files if the run produces durable decisions or patterns.

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

If validation fails, fix the artifacts or clearly report what remains incomplete.
