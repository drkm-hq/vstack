# Comment review

Read a comment with the implementation and its caller before deciding it is redundant. Separate:

- Narration of obvious syntax or repeated code: remove or simplify.
- A stale claim: verify the current behavior and correct the claim.
- A non-obvious invariant or external workaround: check its evidence and preserve the useful explanation.
- A suppression or compiler directive: understand what it controls before changing it.
- A license or generated marker: preserve its required meaning and tooling role.

When a comment carries a rule the type system, test, or lint can enforce, propose or implement that encoding only within the requested scope. Verify the invariant before replacing its explanation. If the constraint remains ambiguous, retain it and report uncertainty; declining an enforcement change is not a reason to erase the knowledge.

Count how many concepts and mutable values the reader must hold, not only lines. Collapse a pass-through layer only when it adds no useful policy, adaptation, or boundary. Keep unrelated cleanup out of the diff.

Adapted from pstack: [no-comments](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/no-comments), [principle-encode-lessons-in-structure](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/principle-encode-lessons-in-structure), [principle-minimize-reader-load](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/principle-minimize-reader-load). See `../PSTACK-LICENSE.txt`.
