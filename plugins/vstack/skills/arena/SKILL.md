---
name: arena
description: "Compare independent candidates for the same design, implementation, or artifact and synthesize the strongest result. Use when the user requests an arena or competing agent attempts."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/arena
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Arena

Give independent candidates the same task, compare their artifacts, then verify the synthesis.

1. State the artifact, constraints, and a short rubric before candidates start. Respect the requested count and budget. Keep the judgment rubric separate from candidate results so it cannot be retrofitted to the favorite.
2. Use available subagent tools when the user requests independent agents. Inherit the current model unless a supported model was explicitly requested. Report when requested model diversity is unavailable. If delegation is unavailable, offer sequential alternatives and label that limitation.
3. Give each candidate a separate writable directory or worktree and explicit ownership. Pass the same task and raw evidence, without other candidates' conclusions. Design-only requests stay read-only apart from scratch artifacts. Candidates must not launch another arena.
4. Collect all outcomes, including failures. Read the actual artifacts before judging. Score the candidates against the rubric. An independent judge can help for consequential choices, within the available concurrency and budget.
5. Choose a base with the simplest interface that satisfies the constraints. Adapt useful ideas from other candidates without combining incompatible assumptions. Record the base, adopted ideas, rejected alternatives, and dropouts.
6. Verify the combined result. Candidate checks do not prove the combined artifact. If the candidates disagree because the task was ambiguous, resolve that ambiguity before combining them.

Return one result and a compact comparison with evidence. Do not commit, publish, or create tasks solely because the arena finished.

For skill or prompt evaluations, hold the realistic task and raw inputs constant, isolate runs, label outputs without revealing which prompt produced them, and judge with a rubric fixed before reading results. Repeat variable outcomes when the budget allows. Do not supply the expected answer or prior diagnosis to the evaluated candidate.
