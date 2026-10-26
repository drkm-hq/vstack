---
name: reflect
description: "Extract durable lessons from the current task and identify targeted skill improvements. Use when the user asks to reflect, capture lessons, or improve a workflow after doing it."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/reflect
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Reflect

Find lessons that would change the next attempt. Prefer a precise correction to another universal rule.

1. Use the current conversation, observed tool results, and artifacts. Retrieve additional task history only when needed and within the requested scope. Do not invent transcript locations.
2. Review judgment, tooling, and alternative approaches: where the task changed direction, which checks caught a real issue, which tools wasted work, and which assumption failed.
3. Separate repeated problems and explicit preferences from isolated mishaps. Read existing skill guidance before proposing a change. A rule that was already clear but ignored may not need more prose.
4. Map each supported lesson to the smallest appropriate edit: an existing instruction, a better description, a reference, or a deterministic check. Prefer a lint rule or script for a mechanically enforceable invariant when it is within scope.
5. If the user requested saving lessons or updating skills, use `skill-creator` when available to apply the supported changes and validate them. If the request was reflection only, present findings and proposed edits without changing files. Do not file backlog items or contact other people automatically.
6. Use independent reviewers only when the user requests them or the task warrants an authorized broad review. Give them raw evidence and distinct lenses; the parent owns edits.

Report accepted lessons with evidence, applied or proposed destinations, and any rejected inference that matters. Keep the review proportional to the task.
