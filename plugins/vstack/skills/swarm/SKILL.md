---
name: swarm
description: "Coordinate agents across separate slices of a broad task and return one evidenced result. Use when the user requests a swarm, delegated coverage, or parallel agent work."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/swarm
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Swarm

Use parallel workers for independently useful slices. For competing answers to the same task, use [arena](../arena/SKILL.md).

1. Define completion, required slices, and the output from each. Keep the number of workers proportional to independent work and the available slots.
2. State ownership before spawning. Readers may share files; writers need disjoint files or isolated checkouts. The coordinator owns integration and any shared application session.
3. Send self-contained briefs with scope, evidence, constraints, writable paths, verification, and required report. Use available subagent tools, inherit model settings, and honor an explicitly requested supported model. Do not invent cloud environments or create sidebar tasks for subtasks.
4. Collect `PASS`, `ISSUES`, or `BLOCKED` reports with artifact paths and observed results. Continue useful local work. Every required slice needs a result; a missing worker is a gap, not a pass.
5. Inspect artifacts and consequential claims. When implementation is authorized, resolve conflicts, integrate accepted changes, and verify the combined result. Review-only workers return findings without edits. A worker's success summary is not independent proof.

Return a compact coverage table, evidenced issues, and gaps. Keep raw worker output out of the main response. Preserve the user's commit, push, and merge boundaries.
