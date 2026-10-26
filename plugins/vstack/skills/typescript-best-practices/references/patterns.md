# TypeScript patterns

These examples illustrate contracts, not mandatory new abstractions. Use existing repository schemas and conventions.

## Variants

```ts
type LoadState<T> =
  | { kind: "loading" }
  | { kind: "ready"; value: T }
  | { kind: "failed"; message: string };

function describe(state: LoadState<string>): string {
  switch (state.kind) {
    case "loading": return "Loading";
    case "ready": return state.value;
    case "failed": return state.message;
    default: {
      const unreachable: never = state;
      return unreachable;
    }
  }
}
```

Adding a new variant forces this function to handle it. Runtime boundary parsing is still required for untrusted objects.

## Nonempty input and honest absence

```ts
type NonEmpty<T> = readonly [T, ...T[]];

function first<T>(values: NonEmpty<T>): T {
  return values[0];
}

function firstOrMissing<T>(values: readonly T[]): T | undefined {
  return values[0];
}
```

Choose according to the actual caller contract. `NonEmpty<T>` proves index zero exists, not that an arbitrary numeric index is in bounds.

## Parse the boundary

```ts
function parseName(input: unknown): string {
  if (typeof input !== "string" || input.trim().length === 0) {
    throw new Error("Expected a nonempty name");
  }
  return input.trim();
}
```

For structured data, reuse the repository's runtime schema and infer the domain type from it. Do not cast `JSON.parse` results into a domain type or write a guard that checks only part of its claim.

## Check compatibility

```ts
type ThemeConfig = { theme: "dark" | "light"; columns: number };
const config = { theme: "dark", columns: 3 } satisfies ThemeConfig;
```

This checks assignability while keeping an inferred result type. `theme` remains a specific union member here, while `columns` is still `number`. `satisfies` performs no runtime validation.

## Numeric invariants

A `durationMs: number` field accepts negative values, `NaN`, and infinity. Validate the invariant at construction or with the existing schema library. A start-plus-duration representation removes duplicated endpoint state; it does not itself make an invalid duration impossible.

## Derived shapes

Reuse a generated response type, an existing schema's inferred type, or a projection such as `Pick<Response, "id" | "status">` when that is the contract. A generated file is regenerated from its source; it is not edited to make a caller compile.
