# 00 Spec

## Topic

deep research agents reference atlas

## Decision context

R&D Lab OS needs a reproducible operating model for deep technical research.
The local Reference Atlas argues that the near-term opportunity is not model
training, but an orchestration layer over existing frontier-agent tools with a
durable artifact chain:

```text
Research Spec -> Question Graph -> Evidence Ledger -> Critic Pass -> Final Memo -> Memory Update
```

This run should turn the Reference Atlas into a structured research plan for
the first usable version of that workflow.

## Intended audience

Primary: the builder/operator of R&D Lab OS.

Secondary: future Codex, Claude, Gemini, or other coding/research agents that
need clear repo-local instructions before continuing the research.

## Output type

Structured research run artifacts. This test task only fills:

- `00_spec.md`
- `01_question_graph.md`

Later work may fill source map, evidence ledger, contradictions, synthesis,
critic review, final memo, and decision log.

## Scope

- Derive the research questions from `source/reference-atlas-input.md` and
  `docs/05-reference-atlas-digest.md`.
- Focus on orchestration patterns for deep research agents.
- Compare workflow families: general deep research, scientific literature
  synthesis, survey automation, research memory, and evaluation.
- Identify which references are design inputs, which could become dependencies,
  and which should remain only benchmarks or inspiration.
- Preserve the repo's v0 boundary: artifact workflow first, no backend, no UI,
  no custom model training.

## Non-scope

- No live external research in this first test pass.
- No final recommendations without evidence ledger rows.
- No dependency selection or implementation work.
- No backend, UI, vector database, GraphRAG deployment, model training, or
  paid-product UI automation.
- No attempt to verify every Reference Atlas citation during this initial
  two-artifact setup.

## Source preferences

- Start with local sources:
  - `source/reference-atlas-input.md`
  - `docs/05-reference-atlas-digest.md`
  - `memory/references/references.yaml`
  - `memory/references/patterns.yaml`
  - `memory/references/anti_patterns.yaml`
- Prefer primary sources in later passes: official docs, papers, repos,
  benchmark pages, and product documentation.
- Label source modes explicitly: `academic`, `official_docs`, `code_repo`,
  `benchmark`, `product_docs`, `market_news`, `social_signal`,
  `expert_blog`, `internal_doc`, or `unknown`.
- Keep social and recency signals separate from scientific or official
  evidence.

## Freshness requirements

This first pass uses the local bootstrap archive snapshot dated 2026-06-20.
Later source-map and ledger work should verify current status for active tools,
APIs, repos, and benchmarks before using them in a final memo.

## Success criteria

- The research scope is narrow enough to start evidence collection.
- The root question is explicit.
- Sub-questions map to the main workflow layers:
  - planning and decomposition
  - source discovery
  - evidence capture
  - contradiction handling
  - synthesis
  - critique
  - memory update
  - evaluation
- Future agents can continue from the artifacts without rereading the chat.
- No conclusion is presented as final before the ledger exists.

## Constraints

- Use Markdown, CSV, YAML, and Python stdlib-first tooling.
- Treat references as inputs, not dependencies.
- Do not create or update long-term memory unless a durable decision or pattern
  is explicitly accepted.
- Do not write `07_final_memo.md` during this test task.
- Run `scripts/validate_run.py` after artifact creation.

## Assumptions

- The Reference Atlas is the current source of truth for initial landscape
  coverage.
- R&D Lab OS v0 should optimize for repeatability, traceability, and low setup
  cost over automation breadth.
- Existing frontier-agent products can be used as interchangeable workers, but
  the repo should own the process, artifacts, and validation gates.
- Benchmark and product names may be ambiguous or stale and require later
  verification before final claims.

## Open questions

- Which references are must-study for v0 versus later-stage inspiration?
- What minimum evidence ledger schema is sufficient for decision-grade memos?
- Which quality gates can be enforced by deterministic scripts versus human or
  critic review?
- How should cross-run memory be represented before adopting heavier graph or
  retrieval systems?
- Which worker roles should be manual prompts first, and which deserve scripts
  or skills?
