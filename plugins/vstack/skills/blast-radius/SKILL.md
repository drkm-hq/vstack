---
name: blast-radius
description: "Assess what a proposed change could break outside its diff, including indirect consumers, persisted data, protocols, and lifecycle timing. Use for impact analysis or focused risk review."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/blast-radius
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Blast radius

Find the assumptions a change depends on and test the consequential ones. Assessment is read-only unless changes are requested; use existing checks or isolated scratch probes without altering the worktree.

1. Read the exact diff and surrounding behavior. Identify changed contracts, not just changed symbols.
2. Trace direct consumers and boundaries a symbol search misses: serialized payloads, database rows, generated clients, other languages, feature flags, deployment order, retries, teardown, and asynchronous scheduling.
3. Inspect the pinned dependency version and local patches when safety depends on a library behavior. Do not infer its behavior from its name or latest documentation.
4. Identify the one or two assumptions that clear most of the risk. Try the real function, protocol, or application path with a focused test or probe. Avoid touching shared services or production state to manufacture proof.
5. Separate confirmed defects, plausible risks, cleared cases, and unproven assumptions. Cite code and observed output. Do not invent numerical probabilities.

Label evidence accurately: source citation, reasoned failure-path analysis, executable probe, or observed application behavior. Static reasoning does not become runtime proof because it is convincing.

Report what changes, what it is safe because of, proof or the precise gap, confirmed risks, and the cheapest useful remaining check. Route broader independent review to the installed `adversarial-review` skill when requested.
