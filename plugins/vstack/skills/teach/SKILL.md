---
name: teach
description: "Explain a code change or subsystem at the reader's level, combining concrete behavior with supported design rationale. Use when the user asks to be taught or helped to understand."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/teach
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Teach

Explain the thing itself in plain language. This is a read-only teaching request unless the user also asks for edits.

1. Infer the needed depth from the question and conversation. Start with what the thing is and the problem it solves.
2. Trace behavior from real code using the installed `trace-request-flow` skill when needed. Use [why](../why/SKILL.md) for motivation the code cannot establish. Keep that research narrow and preserve its confidence language.
3. Walk through a concrete action and its consequences. Introduce terms when they become necessary. Explain ownership and state changes instead of listing functions.
4. Use a small diagram or interactive visual when it clarifies the mechanism. Build a complex explanation in stages when that helps; do not impose several diagrams on a simple point. Use available visualization tools for spatial or interactive questions.
5. Give the smallest complete explanation at the requested depth. Let follow-ups guide additional detail. Do not quiz the user, force a teaching script, or replace a requested full explanation with a teaser.

Keep real technical names consistent. Preserve uncertainty and the distinction between observed behavior and inferred intent. The response is the explanation, not a report about the research process.
