---
name: technical-writing
description: "Write and review technical docs, RFCs, READMEs, PR descriptions, and procedures for clarity and accurate instructions. Use for substantive technical writing tasks."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/technical-writing
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Technical writing

Write for the reader's job and use the repository's real names. Follow supplied templates and local documentation conventions.

Choose the dominant document mode:

| Mode | Reader needs | Shape |
| --- | --- | --- |
| Tutorial | Learn by doing | A working result, guided steps, visible checkpoints |
| How-to | Complete a known task | Preconditions, actions, branches, expected outcomes |
| Reference | Look up facts | Stable structure mirroring the actual API or system |
| Explanation | Understand why | Context, mechanism, decisions, alternatives, tradeoffs |

Separate material when mixing modes makes navigation harder; do not fragment a useful small document to satisfy the taxonomy. PR descriptions and commit messages follow their own repository templates.

Put a condition before the instruction it controls. Give each step one action and the result the reader can observe. Name the actor, use present tense for current behavior, and prefer direct commands in procedures. Keep warnings attached to the relevant action.

Use one name per concept. Keep `only` and `not` beside the words they modify. Replace ambiguous pronouns and long noun chains with concrete nouns. Keep articles and connecting words when they prevent a second reading. Prefer plain words and vary sentence length naturally.

Verify symbols, paths, flags, links, counts, and code examples against the actual revision. Match code formatting to the language and repository. Distinguish facts, assumptions, and recommendations; never remove a necessary hedge to sound certain.

Lead a PR description with the problem and resulting behavior, then consequential choices and observed validation. Link large logs rather than pasting them. Preserve explicit commit, publish, and review boundaries.

Use [unslop](../unslop/SKILL.md) for a prose cleanup when needed. Do not edit the writing skills themselves just because a new awkward phrase appears in a document.
