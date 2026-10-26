---
name: figure-it-out
description: "Design and execute an evidenced workflow for a complex migration or investigation with no established recipe. Use for open-ended multi-phase work that needs measurable checkpoints."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/figure-it-out
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Figure it out

Turn the requested outcome into verifiable units. Preserve the task's scope, budget, and stop points; a broad request is not permission to merge, deploy, or work indefinitely.

1. State completion as an observable condition. Inventory the affected units and the first uncertain assumption. Read the conventions and existing consumer before choosing a workflow.
2. Establish a baseline and the cheapest useful observation before editing. Resolve high-risk unknowns early. Use [architect](../architect/SKILL.md) when the design is unsettled, and [measurement and investigations](references/measurement-and-investigations.md) for performance, profiling, runtime evidence, or behavior-preserving refactors.
3. Split the work into units that each end in a verifiable state. Build a reusable codemod or checker when repetition or reliability justifies it, not for every small edit. Parallelize only independently useful slices when delegation is authorized.
4. For each unit, state a hypothesis, make a bounded change, measure, and retain or undo only your own experimental edits. Treat `VERIFIED`, `NOT VERIFIED`, and `INCONCLUSIVE` as different outcomes.
5. After repeated failures of the same premise, stop patching symptoms. Inventory which actors own the affected state, test a competing explanation, and revise the model. More retries without new evidence are not progress.
6. Keep a compact decision record with [show-me-your-work](../show-me-your-work/SKILL.md) when a long run needs one. Record decisions and evidence, not private reasoning or every tool call.
7. Verify the whole against the original outcome, not just each helper. Before a pause or handoff, record the current revision, local edits, evidence, owned processes, next step, and unresolved constraints. Do not make an automatic WIP commit.

Report the completed outcome, material decisions, proof, and remaining gaps. Use the Codex automation tool only when the user actually requested later or recurring work.
