---
name: unslop
description: "Edit prose to remove filler, canned AI phrasing, vague claims, and unnecessary jargon while preserving meaning and tone. Use for writing cleanup or a requested plain-language rewrite."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/unslop
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Unslop

Edit the supplied writing, preserving facts, technical meaning, uncertainty, citations, and the intended voice. For source-code cleanup use the installed `deslop` skill.

1. Remove throat-clearing, canned praise, generic conclusions, and filler that adds no information.
2. Replace vague attribution with a real source when available. Never fabricate a source or strengthen a claim to make prose smoother.
3. State the point directly instead of using "not just X, but Y," artificial groups of three, or false ranges.
4. Use concrete verbs and familiar words. Replace metaphorical jargon when a literal description is clearer, while retaining real domain terminology.
5. Keep one term for each concept. Do not cycle synonyms for a protocol, role, or data structure.
6. Remove excessive emphasis, decorative headings, repeated inline labels, and punctuation used as a substitute for sentence structure. Respect the user's requested format and voice.
7. Split sentences that carry unrelated thoughts. Keep complete grammar and connecting words; compressed fragments can cost more attention than a longer sentence.
8. Prefer active voice when the actor matters. Replace unmeasured intensifiers with a measured result or a modest claim. Keep uncertainty that reflects limited evidence.

Read the result once for lost meaning. Return the edited text directly unless the user asks for an explanation or tracked comparison. A request to restate the last answer plainly needs only that restatement.
