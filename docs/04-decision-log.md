# Decision Log

Use this format for important architecture and workflow decisions.

```text
Date:
Project:
Decision:
Reason:
What this prevents:
Review date:
```

Seed decision:

```text
Date: 2026-06-20
Project: R&D Lab OS
Decision: Build an orchestration-first research workflow over existing frontier-agent subscriptions instead of training custom models.
Reason: The bottleneck is repeatability, evidence discipline, memory, and evaluation, not base model capability.
What this prevents: Premature ML/RL work, custom multi-agent backend scope creep, and chaotic research chats without durable artifacts.
Review date: 2026-07-20
```

Bootstrap decision:

```text
Date: 2026-06-20
Project: R&D Lab OS
Decision: Create bootstrap archive for Codex that generates a repo scaffold with protocols, skill, templates, validators, and memory seeds.
Reason: Codex should build from a reproducible artifact structure, not from a one-off chat prompt.
What this prevents: chaotic repo setup, missing evidence ledger, premature backend/UI, and unstructured research runs.
Review date: 2026-07-04
```
