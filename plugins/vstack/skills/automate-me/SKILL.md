---
name: automate-me
description: "Create or refine a personal working-style skill from explicit preferences and repeated patterns in relevant conversations. Use when the user asks to capture how they work in a skill."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/automate-me
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Automate me

Turn demonstrated working conventions into a small personal skill. This creates instructions, not a scheduled automation.

1. Look for an existing personal style skill in the configured skill roots. Prefer updating it when the request is an update. Preserve unrelated guidance and invocation settings.
2. Start from explicit preferences and the current conversation. If history is needed, use available Codex task tools and restrict reads to the named project, topic, and period. Do not scan every project's private transcripts.
3. Distinguish explicit instructions, recurring corrections, and one-off task constraints. A clearly stated preference needs no artificial repetition; inferred habits need repeated evidence and must not contradict newer instructions.
4. Ask only for missing intent that materially changes the skill. Do not make a questionnaire or approval round mandatory when the request already supplies the conventions.
5. Use `skill-creator` when available; otherwise follow the host's documented SKILL.md format to write or update the skill in the requested location, otherwise the personal skill root. Keep the trigger specific to the working style. Reference task-specific skills instead of copying them.
6. Preserve automatic discovery unless the user requests explicit-only invocation. A style skill cannot override task scope, approval rules, repository conventions, or model availability.
7. Validate the result and report the exact path plus what changed. Commit or open a PR only when the request includes repository publishing.

Avoid generic sections such as "communicate clearly." Include only preferences that change future decisions. Use [unslop](../unslop/SKILL.md) for a final prose pass when useful.
