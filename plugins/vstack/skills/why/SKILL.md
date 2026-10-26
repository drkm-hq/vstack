---
name: why
description: "Investigate why code or a design exists using decision records, git history, PRs, and relevant connected sources. Use for design rationale, historical constraints, regressions, or unexplained thresholds."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/why
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Why

Reconstruct intent from the historical record. Current code shows behavior; it does not prove the author's motivation. Keep the investigation read-only.

1. Anchor the question to concrete files, symbols, and a revision. Read the applicable ADR or design record before inferring intent.
2. Inspect blame, file history through renames, introducing commits, associated PRs, review discussions, and linked issues. A recent formatting commit is not the origin of the decision.
3. Follow relevant leads into available connected sources. Read [source playbooks](references/source-playbook.md) for search strategy. Start with the narrow record that can answer the question; widen when it is incomplete or contradictory. Respect any user-specified source boundary.
4. Read [confidence guidance](references/epistemics.md). Separate direct evidence, corroborated conclusions, inference, competing hypotheses, and unknowns. Preserve contradictions and search misses instead of manufacturing a tidy story.
5. For a broad investigation with authorized delegation, assign nonoverlapping sources to readers and verify their citations. Otherwise investigate directly. Discover actual tools instead of assuming a particular provider or model is installed.
6. When this informs an authorized change, turn the findings into constraints: what to preserve, what can change, what to avoid, and what risk remains. Answering why does not itself authorize the change.

Lead with the answer at the confidence the evidence supports. Cite the source adjacent to each consequential historical claim. Briefly name relevant sources searched, missing access, and unresolved questions. Do not contact authors, post comments, or create issues as part of research.
