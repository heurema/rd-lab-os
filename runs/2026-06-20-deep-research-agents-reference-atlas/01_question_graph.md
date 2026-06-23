# 01 Question Graph

## Root question

How should R&D Lab OS turn the Reference Atlas of deep research agents into a
minimal, reproducible workflow that produces traceable research artifacts before
any backend, UI, model training, or heavy memory system exists?

## Sub-questions

1. What workflow loop is common across the strongest references?
   - Scope clarification
   - Question decomposition
   - Iterative source discovery
   - Evidence capture
   - Synthesis
   - Citation or provenance tracing
   - Critique and memory update

2. Which systems best inform each workflow layer?
   - Planning: STORM, Co-STORM, MindSearch
   - Orchestration: GPT Researcher, Open Deep Research, Deep Research from
     Scratch
   - Evidence-first synthesis: PaperQA2, OpenScholar, Ai2 ScholarQA, Elicit
   - Survey structure: AutoSurvey, SurveyX, SurveyForge
   - Memory: GraphRAG, AgentRxiv
   - Evaluation: DeepResearch Bench, DeepResearch Bench II, BrowseComp,
     DeepResearchGym, DeepScholar-Bench, AstaBench
   - Packaging: Codex skills, Claude skills, Gemini CLI skills

3. What should be implemented as repo artifacts first?
   - Research spec
   - Question graph
   - Source map
   - Evidence ledger
   - Contradiction review
   - Synthesis
   - Critic review
   - Final memo
   - Decision log and memory update

4. What should remain out of scope for v0?
   - Model training or fine-tuning
   - Custom multi-agent backend
   - UI/dashboard
   - Vector database or GraphRAG deployment
   - Paid-product UI automation
   - Unverified benchmark claims

5. What validation should exist before a run is considered useful?
   - Required files exist
   - Ledger columns are valid
   - Claims cite source rows
   - Source modes are labeled
   - Contradictions are explicit
   - Critic pass is separate from synthesis
   - Final recommendations trace back to evidence

## Alternative framings

- "Research workflow OS" rather than "deep research agent."
- "Artifact pipeline" rather than "multi-agent system."
- "Evidence ledger plus validators" rather than "knowledge base."
- "Portable skills and protocols" rather than "product integration."
- "Reference atlas as design input" rather than "dependency list."

## Stakeholders

- Lab operator: needs repeatable research outcomes and low maintenance cost.
- Codex/coding agents: need repo-local instructions, templates, and validators.
- Research agents: need bounded tasks, source preferences, and artifact targets.
- Critic/reviewer role: needs traceability from memo claims back to evidence.
- Future collaborators: need decisions recorded outside chat history.

## Schools of thought

- Product-worker approach: use ChatGPT Deep Research, Gemini Deep Research,
  Claude Research, Perplexity, Elicit, and similar tools as external workers.
- Open-agent approach: adapt patterns from GPT Researcher, Open Deep Research,
  MindSearch, and similar repos.
- Scientific-RAG approach: prioritize PaperQA2, OpenScholar, ScholarQA, and
  Elicit-style evidence discipline.
- Memory-first approach: build durable cross-run memory early.
- Evaluation-first approach: define benchmark and rubric gates before expanding
  worker automation.
- Minimal-artifact approach: keep v0 as Markdown/CSV/YAML plus deterministic
  validators until repeated use proves where automation belongs.

## Likely controversies

- Whether GraphRAG or another memory system should be adopted early, or delayed
  until plain-file memory proves insufficient.
- Whether product research agents should be treated as reliable sources or only
  as scouts whose output must be re-ledgered.
- Whether final memo quality should be judged by human review, benchmark-style
  rubrics, deterministic checks, or a mix.
- Whether a question graph should be a static artifact or updated throughout
  search.
- Whether social and market signals belong in the same run as academic and
  official sources.
- Whether benchmark names and reported capabilities are current enough to use
  without fresh verification.

## Evidence gaps

- Current status of each reference repo, product API, and benchmark.
- Primary URLs and canonical paper/repo names for similarly named benchmarks.
- Concrete failure modes from prior research runs.
- Minimum ledger fields needed to prevent unsupported final memo claims.
- Best representation for cross-run memory before heavier retrieval systems.
- Clear acceptance criteria for when a run is "decision-grade."

## Follow-up branches

- Build `02_source_map.md` from the local reference YAML files and Atlas text.
- Populate `03_evidence_ledger.csv` with claim-level rows for the must-study
  references.
- Create a contradiction review focused on benchmark ambiguity, product/API
  drift, and "reference versus dependency" confusion.
- Test whether validators can detect unsupported final memo claims.
- Draft worker prompts for product scouts, repo inspectors, literature scouts,
  and critic reviewers.
- Compare a plain-file memory approach against GraphRAG-style memory after
  several completed runs.

## Kill criteria / what would change the conclusion

- If live verification shows the referenced tools no longer expose usable
  research, skill, or API workflows, worker orchestration must be reframed.
- If repeated runs fail because plain files cannot preserve traceability, a
  stronger memory/index layer becomes a v0 requirement.
- If deterministic validators cannot catch the main quality failures, the v0
  quality gate must rely more heavily on critic review and rubric checks.
- If evidence-ledger maintenance costs exceed the value of final memos, the
  ledger schema must be simplified before expanding scope.
- If the strongest references point to dependency-heavy architecture as
  unavoidable, the current "no backend/UI/heavy system" boundary needs review.
