---
name: create-verification-skill
description: "Create or maintain a project-local app-verification skill and feature map. Use for a new reusable verification workflow or an audit and repair of a recipe that has drifted from actual behavior."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/create-verification-skill
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Create or maintain a verification skill

Write instructions another agent can execute cold to prove real behavior. Use `skill-creator` when available; otherwise follow the host's documented SKILL.md format and reuse an existing project verification skill when one already covers the app.

For an existing recipe that needs auditing or repair, follow
[maintenance](references/maintenance.md) instead of recreating it. For a new
recipe, use the steps below.

1. Inspect the repository's startup instructions, supported entry points, existing tests and control tools, auth requirements, fixture data, ports, and isolation options. Name the real caller and observable outcome. Ask only for prerequisites the repository cannot establish.
2. Choose the existing browser, HTTP, CLI, PTY, or desktop control path. Consult that tool's skill before using it. Do not add a custom driver when the current harness is enough.
3. Write `.agents/skills/verify-<app>/SKILL.md`, or the repository's established discoverable skill location. Include a specific description and the actual commands for launch, readiness, read-only health checks, driving, evidence, and cleanup.
4. Record process IDs and isolate data, ports, and profiles. Never kill by process name or alter another instance. Keep evidence outside disposable state so cleanup preserves it.
5. Add a feature index and recipes covering the task's user-facing paths. The [example map](references/feature-map-example/README.md) demonstrates the shape only; its Notes commands are fictional and must be replaced with observed commands and handles from this repository. Name prerequisites, alternate entry points, reverse actions, and observable side effects.
6. Run the generated instructions once: launch, health-check, drive one mapped feature, capture action and outcome, clean up, and confirm evidence survives. A dry-run label does not prove absence of side effects; verify its actual behavior.
7. Validate the skill and report exactly which feature was exercised. If runtime prerequisites are unavailable, complete the source-grounded recipe as an explicitly unverified draft and name the blocker. Leave unknown live selectors unresolved instead of inventing them. Do not fix unrelated startup failures or claim that one feature proves the whole map.

Do not schedule maintenance unless requested.
