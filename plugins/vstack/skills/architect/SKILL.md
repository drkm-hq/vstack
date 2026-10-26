---
name: architect
description: "Design caller usage, types, module boundaries, and state ownership. Use for architecture, deep-module and interface design, testability, or changes whose design is unsettled."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/architect
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Architect

Settle the shape around a real caller before filling in the code. For deep
modules, test seams, and reducing caller coordination, read
[deep modules](references/deep-modules.md). A design question is read-only; implement only when the task includes implementation. Honor requested checkpoints and stop points.

1. Read the area's conventions, decision records, relevant callers, and tests. Trace the current behavior using the installed `trace-request-flow` skill when needed. Use [why](../why/SKILL.md) if ownership or historical constraints are unclear.
2. Write the caller's usage first: what it imports, supplies, receives, and does on failure. Derive types and signatures from this usage. Sketch in the response or a scratch artifact unless a repository design document was requested. Do not add unused production scaffolding.
3. Name the data owner, dominant access patterns, state transitions, validation boundaries, and effects. For retries or concurrent actors, read [state and boundaries](references/state-and-boundaries.md).
4. Compare structurally different designs when a consequential choice remains open. Explain the complexity each interface hides and what it makes callers coordinate. Use [arena](../arena/SKILL.md) when independent candidates are requested; a routine decision does not require agents or multiple prototypes.
5. Screen the proposal with [design red flags](references/design-red-flags.md). Record the chosen shape, a meaningful alternative, tradeoffs, and the first consumer. The [rationale template](references/rationale-template.md) is available for larger designs.
6. If implementation is authorized, fill in the smallest useful slice and verify it. Repeated casts, special cases, new shared state, or callers depending on internals are evidence to revisit the shape. Redesign within the requested scope instead of accumulating workarounds.

Report the design, why it fits the caller, the important tradeoff, and remaining uncertainty. Use repository terminology and keep a small design small.

For an uncertain interaction or appearance, use a disposable prototype or comparable screenshots as described in [prototype and visual checks](../figure-it-out/references/measurement-and-investigations.md#prototypes-and-visual-parity).
