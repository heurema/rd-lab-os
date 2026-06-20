# Reference Atlas for an R&D Lab OS Built on Frontier Agents

## Executive summary

The strongest signal across the current landscape is that “deep research” is no longer a single product category. It has split into four adjacent layers: general-purpose web research agents, scientific-literature synthesis systems, idea-generation and autonomous-science systems, and a new “agent operating system” layer built around reusable skills, MCP-connected tools, and long-running asynchronous workflows. The open-source and product ecosystems are converging on the same basic loop: clarify scope, decompose into sub-questions, search iteratively, collect evidence, synthesize into a report, and attach citations or traceable provenance. STORM, GPT Researcher, Open Deep Research, MindSearch, OpenAI Deep Research, Gemini Deep Research, Claude Research, PaperQA2, OpenScholar, and Ai2 ScholarQA all implement variations of that loop, even though they target different users and source types. citeturn14view2turn14view0turn14view1turn0search11turn25view0turn25view1turn25view3turn15view3turn25view2turn14view3turn24search3turn23view0

For your goal, the most important design conclusion is this: the best immediate opportunity is not to build or train a new model, but to build an orchestration layer that treats products like ChatGPT Deep Research, Codex, Claude Code, Claude Research, Gemini Deep Research, Gemini CLI, Elicit, and Perplexity as interchangeable workers with specialized roles. Official docs from OpenAI, Anthropic, and Google all now expose “skills” or equivalent modular capability packaging; OpenAI and Google also expose deep-research-capable APIs, while Anthropic exposes research, skills, web search, and code-facing workflows across Claude and Claude Code. That means the frontier has shifted from “who has the best model” to “who has the best repeatable workflow, evidence ledger, evaluation harness, and memory layer.” citeturn15view0turn15view1turn15view2turn15view3turn15view4turn25view1turn17search0turn17search2turn22view3

A second major convergence is evidence-first synthesis. Scientific systems such as OpenScholar, PaperQA2, Ai2 ScholarQA, and Elicit are optimized not merely for search, but for extracting supportable claims from papers, organizing them into sections, and grounding each claim in quotes, passages, or cited sources. That is exactly the behavior you want for an R&D Lab OS that must produce reusable research artifacts instead of impressive but fragile answers. citeturn24search3turn24search11turn14view3turn23view0turn9search0turn9search3

A third convergence is long-horizon evaluation. DeepResearch Bench, DeepResearch Bench II, BrowseComp, BrowseComp-Plus, DeepResearchGym, DeepScholar-Bench, and AstaBench all exist because one-off answer quality is not enough: systems must be judged on retrieval quality, citation accuracy, report quality, reproducibility, and persistence under real browsing conditions. DeepScholar-Bench and DeepResearchGym are especially relevant because they try to fix the “moving web” problem that makes many benchmarks unstable or unfair. citeturn6search0turn27search0turn6search1turn26search3turn6search3turn7search1turn27search13

The practical implication is straightforward. R&D Lab OS v0 should be an orchestration and memory system with four hard requirements: a research-spec layer, a question-graph layer, an evidence ledger, and a benchmark/evaluation loop. The best references for those four requirements are STORM and MindSearch for planning, GPT Researcher and Open Deep Research for orchestration, OpenScholar/PaperQA2/Ai2 ScholarQA for evidence-first synthesis, GraphRAG and AgentRxiv for research memory, and DeepResearch Bench plus DeepScholar-Bench for quality control. citeturn14view2turn0search11turn14view0turn14view1turn24search3turn14view3turn23view0turn22view4turn20search1turn6search0turn7search1

## Taxonomy of the space

The space is easiest to understand as five overlapping families. The first family is **general deep-research systems**. These are designed to turn a user query into a cited report over heterogeneous web sources. STORM and Co-STORM are closest to “knowledge curation”; GPT Researcher and Open Deep Research are closest to practical open implementations; MindSearch and WebThinker are closest to algorithmic patterns for decomposition and interleaved browsing; ChatGPT Deep Research, Gemini Deep Research, Claude Research, and Perplexity represent the current subscription-grade product layer. citeturn14view2turn19search20turn14view0turn14view1turn0search11turn26search0turn25view0turn25view1turn25view3turn25view2turn25view4turn25view5

The second family is **scientific literature systems**. These care less about web breadth and more about exact evidence extraction, multi-paper synthesis, and citation fidelity. PaperQA2, OpenScholar, ScholarQABench, Ai2 ScholarQA, Ai2 Paper Finder, and Elicit all sit here, though they differ in whether they optimize for search, synthesis, or workflow support. This family matters more than generic “deep research” if your lab will often analyze papers, benchmarks, methods, and technical landscapes. citeturn14view3turn24search3turn20search10turn23view0turn25view6turn9search0

The third family is **survey-writing and related-work automation**. AutoSurvey, SurveyX, SurveyForge, and Agentic AutoSurvey are useful because they formalize a problem your lab will constantly face: how to go from many sources to a coherent landscape map, not just a bag of notes. These systems contribute structure more than state-of-the-art search. citeturn3search2turn3search3turn4search0turn4search1

The fourth family is **idea and hypothesis generation**. ResearchAgent, Can LLMs Generate Novel Research Ideas?, AI Idea Bench 2025, The AI Scientist, The AI Scientist v2, AI Co-Scientist, SciAgents, The Virtual Lab, Agent Laboratory, and AgentRxiv matter because a serious R&D lab eventually needs not only to summarize knowledge, but also to generate hypotheses, experiments, and reusable research memory. For your immediate use case, these are mostly design references rather than MVP dependencies. citeturn4search2turn13search1turn7search3turn4search11turn20search0turn5search0turn5search1turn5search2turn24search0turn20search1

The fifth family is **workflow and evaluation infrastructure**. GraphRAG, DeepResearch Bench, DeepResearch Bench II, BrowseComp, BrowseComp-Plus, GAIA, DeepResearchGym, DeepScholar-Bench, AstaBench, Codex Agent Skills, Claude Agent Skills, Claude Code Skills, Gemini CLI, Gemini CLI Agent Skills, Academic Research Skills, and the Deep Research Skill repositories all belong here. This family is the missing layer in many flashy agents: it gives you memory, reproducibility, and process packaging. citeturn22view4turn6search0turn27search0turn6search1turn26search3turn6search2turn6search3turn7search1turn27search13turn15view0turn15view1turn15view2turn22view3turn15view4turn22view0turn22view1turn22view2

One caution matters immediately: benchmark names are now confusing. There are at least two separate projects named “DeepResearch Bench” or “Deep Research Bench,” one with 100 PhD-level tasks across 22 fields and another with 89 multi-step web tasks across eight categories. If you use benchmark names in your own documents, you should include the paper title or repository to avoid ambiguity. citeturn6search0turn6search4

## Prioritized reference table

### General deep-research systems

| Priority | Reference | Type and current status | Core problem and architecture pattern | What to steal for R&D Lab OS | MVP fit | Primary sources |
|---|---|---|---|---|---|---|
| Must-study | **STORM** — Stanford OVAL, 2024 | Repo + paper; public research prototype | Long-form grounded article generation; two-stage **pre-write then write** pipeline with perspective-guided question asking and simulated writer–expert conversations | Outline-first planning; perspective expansion; question quality before drafting | Immediate | citeturn14view2turn19search17 |
| Must-study | **Co-STORM** — Stanford OVAL, 2024 | Paper + integrated package support | Human-AI collaborative knowledge curation with discourse protocol, moderator, LLM experts, and mind-map-like organization | Human steering without losing agent autonomy; discourse as research substrate | Immediate | citeturn19search20turn19search13turn19search15 |
| Must-study | **GPT Researcher** — Assaf Elovic et al. | Active public repo + docs | Planner → execution agents → publisher; parallelized research; web and local documents; cited reports | Practical baseline orchestration; planner/executor split; source summarization and source tracking | Immediate | citeturn14view0turn0search5 |
| Must-study | **Open Deep Research** — LangChain, 2025 | Active public repo + blog | Configurable deep-research agent over many model providers, search tools, and MCP servers; LangGraph-based stage separation | Bring-your-own-agent architecture; model/search abstraction; benchmark-driven iteration | Immediate | citeturn14view1turn20search15 |
| Useful | **Deep Research from Scratch** — LangChain | Tutorial repo/docs | Explicit three-step loop: **scope → research → write**; decomposes tasks into sub-agents | A minimal curriculum for your own internal protocol and templates | Immediate | citeturn20search3turn20search11 |
| Must-study | **MindSearch** — InternLM, 2024 | Public repo + arXiv | Dynamic question graph with **WebPlanner** and **WebSearcher**; hierarchical retrieval over many pages in parallel | Question graph instead of flat query list; planner/searcher separation | Immediate | citeturn0search11turn0search3 |
| Useful | **WebThinker** — RUC NLPIR, 2025 | Repo + arXiv | LRMs search, browse, and draft *during* reasoning via Deep Web Explorer and think-search-draft | Interleaving search and drafting instead of strict pipeline phases | Later | citeturn26search0turn26search4 |
| Must-study | **OpenAI Deep Research** — ChatGPT product | Closed product; official feature | Multi-step internet research for complex tasks; analyst-style report UX | Product UX target: long-running, cited, user-facing research tasks | Immediate | citeturn25view0 |
| Useful | **OpenAI Deep Research API** | Official API surface | `o3-deep-research` and `o4-mini-deep-research`; supports web search, remote MCP, file search, and optional code interpreter | Programmatic agent worker with external data and internal files | Immediate | citeturn25view1 |
| Must-study | **Gemini Deep Research** — Gemini product | Closed product; official feature | Editable plan, autonomous web/Workspace research, iterative reasoning, multi-page reports, asynchronous execution | Strong product reference for editable plans and async research jobs | Immediate | citeturn25view3 |
| Useful | **Gemini Deep Research Agent API** | Official API preview | Deep-research agent in Interactions API with collaborative planning, charts, MCP, document inputs, and required background execution | API-friendly long-running worker with visual outputs | Immediate | citeturn15view3 |
| Must-study | **Claude Research** | Closed product; official feature | Multiple searches that build on each other, systematic exploration of angles, and easy-to-check citations | Iterative search over open questions; clean citation behavior | Immediate | citeturn25view2 |
| Useful | **Perplexity** — answer engine + Agent API | Product + API | Real-time cited web answers; API exposes agentic workflows with built-in web search, URL fetch, and reasoning controls | Secondary scout; good for quick comparative sweeps and agent API abstraction | Immediate | citeturn25view4turn25view5 |
| Useful | **last30days-skill** | Community skill repo; actively described as v3 pipeline | Parallel search over Reddit, X, YouTube, TikTok, HN, Polymarket, GitHub, and web; ranks by attention and market signals | Social/recency signal layer for market and product research | Immediate | citeturn14view6 |

### Scientific literature and survey systems

| Priority | Reference | Type and current status | Core problem and architecture pattern | What to steal for R&D Lab OS | MVP fit | Primary sources |
|---|---|---|---|---|---|---|
| Must-study | **PaperQA2** — FutureHouse | Active repo + paper | High-accuracy scientific RAG over PDFs, Office docs, text, and code; supports summarization and contradiction detection | Evidence-first extraction; scientific citation discipline; contradiction workflows | Immediate | citeturn14view3turn24search2turn27search10 |
| Must-study | **OpenScholar** — Ai2/UW | Active repo + Nature/arXiv paper | Retrieval-augmented LM over 45M open-access papers with citation-backed synthesis and self-feedback loop | Large-scale literature synthesis; citation-accuracy target; retriever-reranker-generator stack | Immediate | citeturn24search3turn26search1turn14view4 |
| Useful | **ScholarQABench** | Benchmark repo from OpenScholar | Holistic evaluation platform for scientific literature synthesis | Academic benchmark for multi-paper synthesis, not just retrieval | Immediate | citeturn20search10turn24search15 |
| Must-study | **Ai2 ScholarQA** | Official product/blog + open code | Evidence-first research summaries from many documents; retrieval + three-step generator pipeline | Quote extraction → planning/clustering → section writing; claim-level evidence | Immediate | citeturn18search2turn23view0turn22view5 |
| Useful | **Ai2 Paper Finder** | Official product/blog + partial open release | Iterative paper-finding agent that decomposes queries, follows citations, evaluates relevance, and runs follow-ups | “Search like a researcher” loop for literature discovery before synthesis | Immediate | citeturn25view6 |
| Useful | **Elicit** | Official product | AI-assisted search, reports, data extraction, and systematic-review workflows over 125M+ papers | High-value workflow ideas for extraction tables and evidence synthesis | Immediate | citeturn9search0turn9search3turn9search13 |
| Must-study | **AutoSurvey** | Repo + arXiv | Retrieval and outline generation followed by subsection drafting, integration, refinement, and evaluation | Survey-writing pipeline structure; long-form output management | Later | citeturn3search2turn3search10 |
| Useful | **SurveyX** | Repo + arXiv | Two phases: preparation and generation; online retrieval, AttributeTree preprocessing, re-polishing | Pre-generation topic structuring and re-polish pass | Later | citeturn3search3turn3search15 |
| Must-study | **SurveyForge** | Repo + ACL/arXiv | Outline heuristics from human surveys; memory-driven generation; SurveyBench evaluation across references, outline, content | Outline mining from strong examples; memory-aware writing | Later | citeturn4search0turn4search8 |
| Useful | **Agentic AutoSurvey** | ArXiv paper | Multi-agent survey generation using Paper Search Specialist, Topic Mining & Clustering, Survey Writer, Quality Evaluator | Role specialization for literature synthesis | Later | citeturn4search1 |
| Useful | **DeepResearch from Scratch + Deep Agents tutorial** | Docs/tutorial | Demonstrates web-research agents that decompose into focused tasks and synthesize reports | Good internal teaching reference for your team | Immediate | citeturn20search11turn20search3 |
| Useful | **Language agents achieve superhuman synthesis of scientific knowledge** | ArXiv paper around PaperQA2 | Human-AI comparison for literature search, summarization, contradiction detection; introduces LitQA2 | Benchmarking standards and contradiction workflow importance | Immediate | citeturn24search2turn27search10 |

### Idea generation and autonomous science

| Priority | Reference | Type and current status | Core problem and architecture pattern | What to steal for R&D Lab OS | MVP fit | Primary sources |
|---|---|---|---|---|---|---|
| Must-study | **ResearchAgent** | ArXiv + Microsoft Research page | Iterative research-idea generation over literature; produces problem, method, and experiment design; reviewed by reviewing agents | Idea loop over literature graph; critique-and-revise pattern | Later | citeturn4search2turn4search10 |
| Must-study | **Can LLMs Generate Novel Research Ideas?** | ICLR 2025 + arXiv | Large human study comparing LLM and expert-generated NLP ideas on novelty and feasibility | Evaluation rubric for idea quality; feasibility vs novelty split | Immediate | citeturn13search0turn13search1 |
| Useful | **AI Idea Bench 2025** | ArXiv + repo | Benchmark with 3,495 AI papers and inspired works for evaluating research idea generation | Quantitative evaluation for idea-generation modules | Later | citeturn7search3turn7search18 |
| Useful | **The AI Scientist** | Repo + arXiv | Full loop: idea generation, code, experiments, figures, paper writing, automated review | North-star architecture for end-to-end research lifecycle | Conceptual | citeturn4search11turn12search10 |
| Useful | **The AI Scientist v2** | Repo + arXiv/Nature coverage | Generalized end-to-end scientific-discovery system with agentic tree search and workshop-paper acceptance claim | Experiment-manager pattern; tree search over research agendas | Conceptual | citeturn20search0turn20search8turn20search12 |
| Must-study | **AI Co-Scientist** — Google | ArXiv + Google Research blog | Multi-agent hypothesis generation with generate–debate–evolve process aligned to scientist goals | Debate/evolution pattern for hypothesis generation | Later | citeturn5search0turn5search4 |
| Useful | **SciAgents** | ArXiv + journal publication | Multi-agent scientific discovery over ontological knowledge graphs | Graph-based idea mining and hidden interdisciplinary link discovery | Later | citeturn5search1turn5search9 |
| Useful | **The Virtual Lab** | bioRxiv/PubMed | PI-style agent coordinating specialist scientist agents and critic over a computational nanobody pipeline | “Lab meeting” interaction pattern; specialist-agent roles | Later | citeturn24search1turn24search13 |
| Must-study | **Agent Laboratory** | Repo + arXiv | Human-provided idea enters three phases: literature review, experimentation, report writing; integrates arXiv, HF, Python, LaTeX | Explicit role/phase decomposition; human feedback at every stage | Later | citeturn14view5turn24search0 |
| Useful | **AgentRxiv** | Repo/site + arXiv | Shared preprint server for autonomous agents to upload, retrieve, and build on prior research | Cross-run research memory and cumulative progress | Later | citeturn20search1turn20search5turn14view5 |
| Conceptual | **RhinoInsight** | ArXiv paper | Verifiable checklist plus evidence audit to improve robustness and traceability without training | Checklist-driven control and evidence-audit layer | Immediate | citeturn13search2turn13search5 |

### Memory, evaluation, and workflow packaging

| Priority | Reference | Type and current status | Core problem and architecture pattern | What to steal for R&D Lab OS | MVP fit | Primary sources |
|---|---|---|---|---|---|---|
| Must-study | **Microsoft GraphRAG** | Public repo + docs | Extracts structured knowledge graphs from unstructured text; uses community summaries and graph-aware querying | Persistent research memory over prior runs and corpora | Immediate | citeturn22view4turn18search3 |
| Useful | **GraphRAG survey** | ArXiv survey | Taxonomy of graph-based indexing, graph-guided retrieval, graph-enhanced generation | Design vocabulary for memory layer decisions | Later | citeturn18search1 |
| Must-study | **DeepResearch Bench** | Benchmark paper + repo | 100 PhD-level tasks over 22 fields; evaluates report quality and citation behavior | Core benchmark for general deep-research quality | Immediate | citeturn6search0turn6search16 |
| Useful | **DeepResearch Bench II** | ArXiv + official eval pipeline | 132 grounded tasks with 9,430 fine-grained rubrics covering recall, analysis, presentation | Better report-level grading than coarse judge prompts | Immediate | citeturn27search0turn27search4 |
| Must-study | **BrowseComp** | OpenAI benchmark | 1,266 hard-to-find browsing questions with short verifiable answers | Persistence and browsing depth evaluation | Immediate | citeturn6search1turn26search19 |
| Useful | **BrowseComp-Plus** | ArXiv + repo | Fixed corpus with human-verified support docs and hard negatives for fairer evaluation | Reproducible browsing eval and retriever isolation | Immediate | citeturn26search3turn26search7 |
| Useful | **GAIA** | Benchmark paper + leaderboard | Tool use, multimodality, browsing, reasoning for general AI assistants | Sanity-check benchmark for “works on any topic” agents | Immediate | citeturn6search2turn6search10 |
| Must-study | **DeepResearchGym** | ArXiv + official site | Reproducible search API over public corpora plus evaluation protocol for deep research | Controlled eval without paying live search cost on every test | Immediate | citeturn6search3turn6search11 |
| Must-study | **DeepScholar-Bench** | ArXiv + repo/leaderboard | Live benchmark for related-work generation from recent arXiv papers; evaluates synthesis, retrieval, verifiability | Best benchmark for literature-style report generation | Immediate | citeturn7search1turn7search4turn7search11 |
| Useful | **AstaBench** | Ai2 benchmark + blog | Holistic scientific-research benchmark suite with controlled environment and baseline agents | Scientific-eval reference if your lab leans academic | Later | citeturn27search1turn27search13 |
| Must-study | **Codex Agent Skills** | Official OpenAI docs | Skill = filesystem package with `SKILL.md`, resources, scripts, progressive disclosure, explicit or implicit invocation | The packaging model for reusable workflows | Immediate | citeturn15view0 |
| Useful | **Codex web/cloud** | Official OpenAI docs | Background cloud tasks, parallel execution, custom environments, repo checkout, run checks, PR workflow | Builder/automation worker inside the OS | Immediate | citeturn15view5turn15view6turn16view0 |
| Must-study | **Claude Agent Skills** | Official Anthropic docs + engineering blog | On-demand modular capabilities with filesystem resources; compose skills across products | Organizational workflow packaging; skills as reusable know-how | Immediate | citeturn15view1turn17search0 |
| Must-study | **Claude Code Skills** | Official Claude Code docs | `.claude/skills/.../SKILL.md`, auto-discovery, direct invocation, bundled skills, subagent patterns, dynamic context | Reviewer and critic workflows; deep operational customization | Immediate | citeturn15view2turn10search6 |
| Must-study | **Gemini CLI** | Official repo + docs/blog | Open-source terminal agent with search grounding, web fetching, shell/file ops, MCP, 1M-token context | Large-context scout and utility worker | Immediate | citeturn22view3turn9search8turn17search15 |
| Must-study | **Gemini CLI Agent Skills** | Official docs | On-demand skill activation, discovery tiers, consent model, workspace and user skill locations | Cross-tool skill portability and agent-library strategy | Immediate | citeturn15view4 |
| Useful | **Academic Research Skills** — Claude + Codex | Community repos; active human-in-the-loop focus | End-to-end suites for research, review, revise, finalize; Codex version vendors workflow into a single skill | Human-in-the-loop academic workflow templates | Immediate | citeturn22view0turn22view1 |
| Useful | **Deep Research Skill for Claude/OpenCode/Codex** | Community repo | Two-phase research workflow with outline generation and deep investigation; inspired by RhinoInsight | Lightweight portable reference for your own internal skill pack | Immediate | citeturn22view2 |

## Top 10 must-study references

If you want the highest return-on-attention reading order, I would start here.

- **STORM** — the clearest reference for scope-before-writing, perspective discovery, and outline-first long-form synthesis. citeturn14view2turn19search17
- **GPT Researcher** — the best practical open baseline for planner/executor/publisher workflow design. citeturn14view0
- **Open Deep Research** — the best reference for a configurable, model-agnostic, MCP-aware research agent. citeturn14view1turn20search15
- **MindSearch** — the strongest reference for question-graph decomposition and hierarchical retrieval. citeturn0search11
- **PaperQA2** — the clearest evidence-first scientific RAG reference, especially for contradiction detection and citation quality. citeturn14view3turn24search2
- **OpenScholar** — the strongest literature-synthesis reference at scale, with a very high citation-accuracy standard. citeturn24search3turn26search1
- **Ai2 ScholarQA** — the most directly useful open workflow for quote extraction, planning/clustering, and section-by-section synthesis. citeturn23view0
- **GraphRAG** — the most actionable reference for turning finished research into reusable memory. citeturn22view4turn18search3
- **DeepResearch Bench plus DeepScholar-Bench** — together they give you a general deep-research benchmark and a literature-synthesis benchmark, which is a much better quality bar than “the answer looked good.” citeturn6search0turn7search1
- **Codex / Claude / Gemini skills docs** — not a single paper, but a critical implementation family; these docs define how to package your lab’s workflows so they survive across tools and teams. citeturn15view0turn15view1turn15view2turn15view4

## Top 10 patterns to steal

The first pattern is **scope-first, answer-last**. STORM, Open Deep Research, deep_research_from_scratch, Gemini Deep Research, and Ai2 ScholarQA all make planning or organization explicit before final synthesis. Your lab should do the same. citeturn14view2turn20search3turn14view1turn25view3turn23view0

The second pattern is **question graphs instead of flat queries**. MindSearch is the most explicit reference, but Ai2 Paper Finder and Claude Research also embody iterative branch expansion rather than one-shot search. citeturn0search11turn25view6turn25view2

The third pattern is **evidence-first synthesis**. OpenScholar, PaperQA2, Ai2 ScholarQA, and Elicit all push the system toward gathering evidence first and writing around it, rather than drafting and backfilling support afterward. citeturn24search3turn14view3turn23view0turn9search3

The fourth pattern is **separate collectors from synthesizers**. GPT Researcher’s planner/execution/publisher split, MindSearch’s planner/searcher split, and Agentic AutoSurvey’s specialized roles all argue against a single monolithic worker. citeturn14view0turn0search11turn4search1

The fifth pattern is **interleave search and reasoning when needed**. WebThinker and Gemini Deep Research explicitly treat drafting or reasoning as something that continues while browsing happens, not only afterward. citeturn26search0turn25view3

The sixth pattern is **treat skills as the packaging unit for process knowledge**. OpenAI, Anthropic, and Google now all endorse on-demand skills with progressive disclosure or activation. That is a direct blueprint for your lab’s protocols. citeturn15view0turn15view1turn15view4

The seventh pattern is **build a persistent research memory instead of relying on chat history**. GraphRAG, ResearchAgent, and AgentRxiv all point toward structured memory layers that survive across runs. citeturn22view4turn4search2turn20search1

The eighth pattern is **evaluate citations separately from prose quality**. OpenScholar, DeepResearch Bench, DeepScholar-Bench, and BrowseComp-Plus all emphasize that report quality and evidence quality are not the same thing. citeturn24search3turn6search0turn7search1turn26search3

The ninth pattern is **add a social-signal layer for market and product research**. last30days-skill is valuable precisely because many research systems still underweight Reddit, X, YouTube, HN, and market signals. citeturn14view6

The tenth pattern is **keep humans in high-leverage checkpoints**. Co-STORM, Agent Laboratory, and the Academic Research Skills suite all explicitly preserve human steering where research direction or interpretation matters most. citeturn19search20turn24search0turn22view0

## Top 10 anti-patterns to avoid

The first anti-pattern is **a single giant system prompt that tries to do everything**. Skills systems from OpenAI, Anthropic, and Google all exist because context should be loaded on demand, not always-on. citeturn15view0turn15view1turn15view4

The second is **report-first, evidence-later writing**. Ai2 ScholarQA, OpenScholar, and PaperQA2 all argue for the opposite direction. citeturn23view0turn24search3turn14view3

The third is **treating deep research as just better search**. S1-DeepResearch, DeepScholar-Bench, and OpenScholar all emphasize integration, synthesis, planning, file understanding, and report generation beyond retrieval alone. citeturn11search7turn7search1turn24search3

The fourth is **flattening decomposition into one search query**. MindSearch and Ai2 Paper Finder both show why researchers need iterative branching and follow-up. citeturn0search11turn25view6

The fifth is **evaluating via vibes**. DeepResearch Bench, DeepResearch Bench II, DeepResearchGym, and AstaBench exist because long-form agents need explicit rubrics and controlled environments. citeturn6search0turn27search0turn6search3turn27search13

The sixth is **ignoring provenance mode**. Social-signal evidence, scientific evidence, internal company documents, and open-web sources should not be blended without labels; OpenAI’s API and Gemini’s Deep Research product both explicitly distinguish between web, files, and MCP-connected sources. citeturn25view1turn25view3

The seventh is **using chat memory as research memory**. GraphRAG and AgentRxiv show why durable external memory matters. citeturn22view4turn20search1

The eighth is **fully autonomous claim generation in domains that still need critique and human review**. The AI Scientist line is impressive, but community tools like Academic Research Skills deliberately remain human-in-the-loop for good reason. citeturn20search12turn22view0

The ninth is **benchmark lock-in to one source type**. A lab that only benchmarks web QA will underperform on literature synthesis; a lab that only benchmarks literature review will underperform on market and strategic research. DeepResearch Bench, DeepScholar-Bench, BrowseComp, and AstaBench cover different slices for a reason. citeturn6search0turn7search1turn6search1turn27search13

The tenth is **assuming product claims are enough**. Closed products are useful workers, but architecture and quality control should be grounded in open references and benchmarks whenever possible. The need for controlled benchmarks like BrowseComp-Plus and DeepResearchGym is itself evidence of this. citeturn26search3turn6search3

## Proposed MVP architecture for R&D Lab OS v0

The best MVP, in my view, is an **orchestration-first research operating system** that sits above existing subscriptions and coding agents rather than replacing them. This is an inference from the reference set, but it is strongly supported by the way current systems decompose work: STORM and MindSearch separate planning from search; GPT Researcher and Agent Laboratory separate orchestration from execution; OpenScholar and Ai2 ScholarQA separate retrieval from sectioned synthesis; GraphRAG and AgentRxiv separate discovery from durable memory; the skills systems from OpenAI, Anthropic, and Google separate permanent workflow knowledge from transient chat context. citeturn14view2turn0search11turn14view0turn24search0turn24search3turn23view0turn22view4turn20search1turn15view0turn15view1turn15view4

At the product layer, I would assign roles rather than crown a single winner. ChatGPT Deep Research or Gemini Deep Research can serve as long-horizon general investigators; Codex can be the builder that writes parsers, collectors, normalization scripts, and validators; Claude Research and Claude Code can be the critic/reviewer layer; Gemini CLI can handle long-context reading and bulk source scanning; Elicit, Ai2 ScholarQA, and PaperQA2 can serve as literature specialists; Perplexity can be a fast scout; and last30days-skill can inject recency and social-signal coverage. That division of labor lines up better with the reference atlas than a “one super-agent” design. citeturn25view0turn25view3turn15view5turn17search2turn25view2turn22view3turn9search0turn23view0turn14view3turn25view4turn14view6

The minimal artifact model should look like this:

```text
rd-lab-os/
  protocols/
    research-spec.md
    source-triage.md
    evidence-ledger.md
    synthesis-rubric.md
    critic-checklist.md
    final-memo.md

  skills/
    codex/
    claude/
    gemini/

  runs/
    YYYY-MM-DD-topic/
      00_spec.md
      01_question_graph.md
      02_source_map.md
      03_evidence_ledger.csv
      04_contradictions.md
      05_synthesis.md
      06_critic_review.md
      07_final_memo.md
      08_decision_log.md

  memory/
    references/
    entities/
    claims/
    patterns/
    benchmarks/
```

The essential workflow is also simple.

```text
Research Spec
→ Question Graph
→ Multi-source Retrieval
→ Evidence Ledger
→ Contradiction Review
→ Synthesis
→ Critic Pass
→ Final Memo
→ Memory Update
```

That workflow is not explicitly copied from one source; it is a synthesis of the dominant patterns across STORM, GPT Researcher, Open Deep Research, Ai2 ScholarQA, OpenScholar, GraphRAG, and benchmark frameworks. citeturn14view2turn14view0turn14view1turn23view0turn24search3turn22view4turn6search0

## Evaluation plan

Your evaluation plan should be two-track from day one. The first track is **general deep research**, using DeepResearch Bench, BrowseComp, BrowseComp-Plus, and GAIA. The second is **research-synthesis quality**, using DeepScholar-Bench, ScholarQABench, and, if your use case becomes more science-heavy, AstaBench. Using only one track will distort the system: a strong browser may still write poor literature reviews, and a strong scientific synthesizer may still fail on fresh, noisy, real-world web tasks. citeturn6search0turn6search1turn26search3turn6search2turn7search1turn20search10turn27search13

A practical scorecard should separate at least six things. First, **coverage**: did the system identify the main sub-questions and schools of thought? Second, **source quality**: what fraction of the answer relies on primary sources? Third, **citation accuracy**: do claims point to supporting evidence? Fourth, **contradiction handling**: did the system preserve uncertainty and disagreement? Fifth, **actionability**: does the report end in decisions, experiments, or next questions? Sixth, **reproducibility**: can another worker reproduce the same artifact chain from the run folder? Those dimensions map closely to the evaluation emphases of DeepResearch Bench, DeepResearch Bench II, DeepScholar-Bench, BrowseComp-Plus, and DeepResearchGym. citeturn6search0turn27search0turn7search1turn26search3turn6search3

I would also add an internal metric that the literature does not standardize cleanly enough yet: **evidence density**, meaning the ratio of nontrivial claims in the final memo that can be traced to rows in your ledger, plus a smaller **freshness disclosure** metric that checks whether the memo labels what is recent, stable, or uncertain. That recommendation is an inference, but it follows directly from the evidence-first design of Ai2 ScholarQA, PaperQA2, OpenScholar, and the explicit citation-evaluation criteria in DeepResearch Bench. citeturn23view0turn14view3turn24search3turn6search0

## 30-day study and implementation plan

In the first week, focus on **core architecture instincts**, not tools. Read STORM, GPT Researcher, Open Deep Research, MindSearch, PaperQA2, OpenScholar, and GraphRAG. At the same time, read the official skills documentation for Codex, Claude, and Gemini so your team internalizes the packaging model early. The goal of this week is to emerge with a shared vocabulary: scope, question graph, evidence ledger, synthesis, critic pass, memory, evals. citeturn14view2turn14view0turn14view1turn0search11turn14view3turn24search3turn22view4turn15view0turn15view1turn15view4

In the second week, implement **workflow primitives**. Create the run-folder schema, the evidence-ledger schema, and three skill packs: one for planning, one for evidence extraction, and one for critique. Use Codex to generate scripts and validators, Claude Code to refine reviewer checklists, and Gemini CLI to test large-context file ingestion. If you want one community template to reverse-engineer rather than invent from scratch, inspect Academic Research Skills and the Deep Research Skill repository, but treat them as references rather than foundations. citeturn15view5turn15view6turn17search2turn22view3turn22view0turn22view1turn22view2

In the third week, run **three benchmark-like internal studies** on the same topic using different workers: one topic on frontier AI agents, one on a market/competitive domain, and one on a scientific literature question. For each topic, require the same artifact chain and compare workers on coverage, citation density, contradiction handling, and actionability. Use last30days-skill on the market topic, Elicit or ScholarQA on the paper-heavy topic, and a general deep-research product on the cross-domain topic. citeturn14view6turn9search0turn23view0turn25view0turn25view3turn25view2

In the fourth week, formalize **quality control**. Add DeepResearch Bench or BrowseComp-style tasks for general web research, and DeepScholar-Bench or ScholarQABench-style tasks for synthesis. Decide on one memory approach for v0; GraphRAG is the strongest reusable reference, while AgentRxiv is the best conceptual reference for collaborative cumulative memory. End the month by writing one internal memo that answers a strategic question using the full workflow and one follow-up memo that reuses the first run’s memory artifacts; if reuse fails, your OS still does research, but it is not yet a lab. citeturn6search0turn6search1turn7search1turn20search10turn22view4turn20search1