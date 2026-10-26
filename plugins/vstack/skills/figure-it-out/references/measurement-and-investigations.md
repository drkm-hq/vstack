# Measurement and investigations

Adapted from pstack's perf-issue, hillclimb, runtime-forensics, trace-forensics, refactoring, prototype, and visual-parity playbooks. Choose the relevant mode; these are not mandatory phases for every task.

## Performance and sustained improvement

Define the metric, workload, environment, target, and guardrails before optimizing. Save a baseline at a named revision. Repeat measurements enough to distinguish a real change from noise; compare the same workload and account for warmup and cache state. Profile before guessing which operation dominates.

For each experiment, record one hypothesis, the bounded change, before and after measurements, and correctness checks. Keep a change only if the evidence meets the target without unacceptable regressions. A benchmark change is separate from a product improvement. Respect the requested time or iteration budget and preserve measurements from rejected attempts. Commit each accepted win only if committing was requested.

## Live runtime symptoms

Reproduce the actual symptom, define its interval, and distinguish active work from idle work. Inventory resource owners: process, task, timer, subscription, request, allocation, or connection. Observe creation and teardown at the layer that owns the resource. A local mock does not establish deployed behavior.

Read-only inspection stays read-only. Instrumentation, configuration changes, or service restarts are mutations and must be within the user's authorized scope. Use an owned local instance for intrusive probes. After repeated failed fixes, test the shared premise and identify which actor still holds the resource before another patch.

## Captured profiles and traces

Identify the artifact format, capture window, sampling settings, application revision, and symbol availability. Use format-aware tooling to compute bounded summaries. Distinguish self time from inclusive time, sampled stacks from wall-clock latency, and retained memory from total allocation. Correlate stacks and task ownership with the recorded version of the code. Missing symbols or an irrelevant capture window are evidence gaps, not permission to guess.

## Behavior-preserving refactors

Name the behavior to preserve before replacing structure. Compare old and new implementations with the same representative inputs, ordering, errors, effects, and serialization. Use differential checks when both versions can run safely. Separate intentional behavior changes from refactor equivalence. A matching patch ID or green compiler does not prove behavior against a changed dependency or base revision.

## Prototypes and visual parity

Use a disposable prototype to resolve a real design uncertainty. State the question, observation, and stop condition before building; promote code into production only when implementation is requested and the result is suitable.

For visual equivalence, compare the same data, viewport, fonts, scale, interaction state, and timing. Capture a baseline and the changed view; inspect meaningful pixel differences alongside interactions, responsive behavior, and accessibility. Do not weaken a comparison by changing the baseline to the new output. Keep exploratory artifacts outside production files until the direction is chosen.
