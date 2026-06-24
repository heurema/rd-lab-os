# 07 Ideas

## Candidate ideas

| ID | Idea | Evidence rows | Confidence | Next step |
|---|---|---|---|---|
| I1 | Add a minimal `idea_ledger.csv` artifact for project-lab runs. | E3,E4,E7,E12 | medium-high | Prototype in one run before changing global templates. |
| I2 | Add `scripts/debate_ideas.py` only after manual `provider_router.py run` debate is repeated and annoying. | E5,E8,E10,E12 | medium | Run 1-2 manual debates first; script only the observed pattern. |
| I3 | Add an idea triage scorecard CSV after there are enough ideas to compare. | E7,E12 | medium | Test manually in this run or next run with 3-5 ideas. |
| I4 | Add `scripts/pipeline_report.py` to scan runs and output a Markdown idea status table. | E7,E11 | medium | Defer until there are at least 3 idea runs. |
| I5 | Add a change brief generator that turns snapshot diffs into an idea/research run scaffold. | E9,E11 | medium | Create deterministic scaffold only; no semantic diffing yet. |
| I6 | Add a discussion import path for Markdown transcripts into question graph + ledger stubs. | E3,E4,E11 | low-medium | Test manually with one real transcript first. |

## Rejected ideas

| Idea | Reason |
|---|---|
| Semantic idea clustering with vector DB | Conflicts with stdlib-first and no-vector-DB constraint. Evidence: E1,E12. |
| Backend/UI idea dashboard | Conflicts with current no-backend/no-UI scope. Evidence: E1,E4. |
| Lab-to-lab idea sync now | Privacy, conflict resolution, and sharing rules are not defined. Evidence: E6,E11. |
| Provider-generated idea promotion directly to memory | Provider outputs are critique signals, not durable verified memory. Evidence: E3,E11,E12. |

## Open idea questions

- Should `idea_ledger.csv` be a new optional project-lab artifact or should
  `07_ideas.md` remain the only idea surface for now?
- Should `scripts/debate_ideas.py` save raw provider output inside a run folder,
  or only append summarized objections to `09_critic_review.md`?
- What status vocabulary should ideas use: `candidate`, `accepted`,
  `experimenting`, `rejected`, `deferred`, `promoted`?
- Should top-level `.heurema/rdlab/ideas/` be a promoted backlog or only a
  manually curated index?
