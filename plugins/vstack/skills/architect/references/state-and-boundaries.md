# State and boundaries

Read for stateful, concurrent, or retryable designs. Adapted from pstack's foundational-thinking, model-the-domain, boundary-discipline, type-system-discipline, make-operations-idempotent, separate-before-serializing-shared-state, and migrate-callers-then-delete-legacy-apis principles.

## Model the invariant

Represent the domain's states and transitions once. Avoid boolean combinations or optional fields that permit contradictory states. Derive secondary values from one authoritative representation when practical. Choose data structures from the dominant reads and writes, not a hypothetical future consumer.

Parse external data into the domain at the trust boundary. Keep transport, storage, and framework details behind a boundary when callers do not need them. Public contracts that deliberately expose a protocol remain valid; hiding them is not an end in itself.

## Identify the writer

List each concurrent actor and the file, row, key, branch, or object it can change. Prefer isolated per-actor state when no real shared-writer invariant exists. If state must be shared, choose an explicit owner, transaction, queue, or lock with a defined lifetime. A process-local lock does not protect writers in other processes.

## Reconcile retries and interruption

Ask what happens on a duplicate request, a crash before and after each effect, and a retry after an uncertain result. Define how to distinguish already complete, partially complete, conflicting, and failed states. A retry should converge on the intended state without duplicating external effects. Use the system's idempotency or transaction mechanism where available; do not claim exactly-once behavior from a local flag.

## Migrate real callers

Inventory in-repository callers and external consumers before replacing an API. Migrate owned callers and remove obsolete code when that fits the scope. Keep compatibility when public consumers, rollout order, persisted data, or mixed versions require it. Do not break the current build or add temporary scaffolding without an explicit migration need.

## Keep the interface useful

Remove redundant layers in the changed path when they obstruct the current caller. Preserve unrelated working code. A simpler implementation is not a win if it shifts coordination or invalid-state handling onto every caller.
