---
name: typescript-best-practices
description: "Design truthful TypeScript types, parse external data at boundaries, and reuse authoritative schemas. Use for substantive TypeScript or TSX implementation and type reviews."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/typescript-best-practices
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# TypeScript best practices

Follow the repository's TypeScript, frontend, and generated-client conventions. Use the simplest types that express the actual contract.

- Model mutually exclusive states as discriminated unions. Distinguish absent, unknown, empty, zero, and failed when behavior differs.
- Parse untrusted data from `unknown` at the boundary. Prefer the existing schema library and derive types from its schemas. Do not add a dependency for a trivial guard or duplicate generated schemas.
- Use narrowing and schema inference instead of casts or non-null assertions that hide a mismatch. A type assertion does not perform runtime validation. Follow stricter repository rules where present.
- Reuse authoritative types through inference, `Pick`, `Omit`, `Parameters`, `ReturnType`, `Awaited`, or `typeof`. Regenerate generated clients instead of editing them.
- Check union exhaustiveness with `never` or the repository's established helper. Use `satisfies` to check compatibility without asserting an unrelated type; it is not runtime validation or a promise to preserve every literal.
- Keep plain arrays when empty input is valid. Use a nonempty tuple only where the operation requires an element. A nonempty array does not make arbitrary numeric indexing safe under strict index checks.
- Consider brands when semantically different primitives can actually be confused. Reuse the repository's convention and parse once. Do not brand every string or build abstractions without consumers.
- Choose data representations that reduce invalid combinations. `number` still permits negative and nonfinite values; changing field names does not enforce numeric invariants.
- Prefer named object arguments when they prevent real positional confusion. Preserve established APIs and account for measured hot-path costs.
- Keep domain logic independent of framework adapters where useful. Validate at trust boundaries and avoid redundant internal checks that mask invalid models.

Read [patterns](references/patterns.md) for concrete examples. Run the relevant type checker and behavioral checks; compiler success alone does not prove the user path.
