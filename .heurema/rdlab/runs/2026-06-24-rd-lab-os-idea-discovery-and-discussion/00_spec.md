# 00 Spec

## Topic

R&D Lab OS idea discovery and discussion lab.

## Project context

This run attaches the portable project-local lab to the `rd-lab-os` repository
itself at `.heurema/rdlab/`. The purpose is to make the repository dogfood its
own idea-generation, provider-debate, evidence-ledger, and experiment-planning
workflow.

## Decision context

The user wants agents to do the idea search and discussion, not to manually
drive every source/provider pass. The immediate need is a useful first lab run
that can seed future product work without expanding into a backend, UI, vector
database, scheduler, or heavy multi-agent framework.

## Intended audience

- User/operator of Heurema project labs.
- Future Codex/Claude/Vibe/Agy agents continuing `rd-lab-os`.

## Output type

Project-local `project_lab` run with evidence ledger, idea shortlist,
experiment candidates, provider debate notes, and memory update guidance.

## Scope

- Initialize and validate `.heurema/rdlab/` in this repository.
- Configure project topics, sources, and subscription provider routing.
- Snapshot configured sources.
- Generate and critique first ideas for an idea discovery/discussion lab.
- Select the smallest next experiments.

## Non-scope

- Backend/API server.
- UI/dashboard.
- Vector database or embedding system.
- GraphRAG.
- Scheduler.
- Heavy multi-agent orchestration framework.
- Writing durable memory outside `.heurema/rdlab/` without a validated run.

## Topic registry link

- `idea-discovery`
- `provider-debate`
- `portable-lab-product`
- `source-watching`

## Source preferences

Prefer local repo files, project lab config, source snapshots, and external
official/public sources only when they directly constrain the lab design.

## External source requirement

External source pass is required before synthesis. This run checks:

- public GitHub README URL;
- OpenAI Codex skills documentation URL;
- local project sources from `.heurema/rdlab/sources.toml`.

## Freshness requirements

Use current repository state as of 2026-06-24. Snapshot source hashes are
recorded in `.heurema/rdlab/watch/snapshots/20260624T051742518067Z.json`.

## Critic / debate requirement

Use subscription provider routing:

- primary/synthesis route: `claude-sonnet`;
- independent critic route excluding Anthropic: `vibe-default`;
- additional critic/triage route: `agy-default`.

Provider availability must be recorded in `09_critic_review.md`.

## Success criteria

- Project lab validates.
- Source snapshot exists.
- Provider router probe identifies usable subscription providers.
- Evidence ledger has non-template rows before synthesis.
- Ideas are traceable to evidence rows.
- Experiments are small, stdlib-first, and reversible.

## Constraints

- Keep `.heurema/rdlab/` as canonical path.
- Do not create `.rdlab/`.
- Keep tooling stdlib-first.
- Keep the evidence ledger as source of truth.
- Do not claim multi-provider debate unless provider calls actually ran.

## Assumptions

- This repository can dogfood project-local mode even though it also owns the
  toolkit core.
- Provider outputs are useful as critique signals but are not authoritative
  evidence about project constraints.

## Open questions

- Should idea artifacts stay run-local only, or should promoted ideas also land
  in `.heurema/rdlab/ideas/` after validation?
- Should `providers.toml` become required for new project labs or remain
  optional for backward compatibility?
- Which idea should become the first implementation issue/branch?
