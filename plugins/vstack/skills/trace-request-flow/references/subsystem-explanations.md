# Subsystem and ownership explanations

Keep the question read-only. Identify the subsystem's purpose, entry points, central types, owners, and boundaries from actual code and decision records. Trace one representative flow only where it helps explain the shape.

For a placement question, compare the proposed responsibility to existing callers, dependencies, and module ownership. Explain what knowledge belongs in each module and what crosses the boundary. Do not create the suggested file or class merely because its location is now clear.

A small question needs one direct investigation. Broad subsystem research can use authorized read-only delegates with distinct slices, but the parent must reconcile overlaps and verify disputed claims.

Walk through a concrete action and its consequences. Introduce terms when
needed, explain ownership and state changes, and give the smallest complete
explanation at the requested depth. Do not quiz the user or replace a complete
answer with a teaser.

Give the purpose, essential concepts, mechanism, a small file map, and consequential gotchas. Use only the pieces the question needs. A diagram helps when relationships are otherwise hard to follow; exact payloads and a sequence diagram are not mandatory for every architecture question.

Reference actual files and symbols. Separate observed behavior from inferred rationale. Use the installed `why` skill when historical intent is the unresolved part, and say what remains untraced.

Adapted from pstack: [how](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/how). See `../PSTACK-LICENSE.txt`.
