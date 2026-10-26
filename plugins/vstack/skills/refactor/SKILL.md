---
name: refactor
description: "Restructure code while preserving observable behavior, migrating real callers, and checking equivalence. Use for refactoring, simplification, internal API migration, or removing unused compatibility code and accumulated patch scaffolding."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/poteto-mode/playbooks/refactoring.md
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Refactor

Name the behavior to preserve and the structural problem to remove. Keep a request to assess a refactor read-only; edit when implementation is requested.

1. Read the area's conventions, decision records, current caller, sibling paths, and tests. Inventory internal and external consumers before changing an interface.
2. State the target shape and what it simplifies for the reader: fewer concepts, clearer ownership, less mutable state, or less knowledge required of callers. Fewer lines alone are not evidence of a better design.
3. Capture behavior that must stay equal: outputs, errors, order, effects, serialization, persistence, and lifecycle. Read [refactor equivalence](../figure-it-out/references/measurement-and-investigations.md#behavior-preserving-refactors) for choosing checks.
4. Move one coherent unit at a time, migrate its owned callers, and verify it before proceeding. Remove obsolete internal code when its callers are gone. Preserve compatibility required by public consumers, deployment order, persisted rows, or mixed versions.
5. Use a codemod for repetitive edits when it reduces risk, verify a representative unit, and inspect the resulting diff. Do not create helpers, options, or new directories without a real consumer.
6. Keep intentional behavior changes separate and visible. If the new shape repeatedly needs casts, conditional workarounds, or shared state that was absent from the design, use [architect](../architect/SKILL.md) to revisit it within scope.
7. Run focused equivalence or behavior checks and the repository's required formatting, lint, and type checks. Inspect the final diff for missed consumers and unsupported compatibility claims.

## Clean up an accreted patch

For a zero-tech-debt or compatibility-cleanup request, state the intended end
state before optimizing the current patch. Search real callers, external
contracts, persisted data, deployment order, and mixed versions before deleting
a flag, route alias, fallback, or wrapper. Remove unused paths instead of
building a generic replacement, and centralize duplicated rules with their
owner. Verify affected navigation, permissions, serialization, and lifecycle
behavior. Preserve compatibility that still has a concrete consumer.

Report what became simpler, which behavior was compared, observed results, and gaps. Preserve commit and publishing stop points.
