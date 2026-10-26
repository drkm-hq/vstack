---
name: meaningful-contribution
description: Prove a code change works before calling it ready. Use when implementing, reviewing, finalizing, or submitting code or a pull request and the result needs reviewer-ready evidence.
---

# Meaningful Contribution

A contribution is not code. It is code proven to work. Agent-generated volume has no value by itself; do not shift verification, cleanup, or basic reasoning onto the reviewer.

## Establish the contract

Before judging readiness, state the change in plain English:

- What behavior should change?
- What are the meaningful inputs and outputs?
- What must happen outside the happy path?
- Which existing abstraction or system contract must this fit?

Treat names and types as contracts. If a name needs a qualifier such as “but it also contains…” or “except this is not actually versioned,” rename or redesign it. Do not use casts, optionality, comments, or defensive branches to conceal a dishonest model.

## Prove the behavior

Use evidence proportional to the change, but never substitute code inspection for execution.

1. Exercise the behavior on the most realistic available surface and observe the result. For user-facing or integration behavior, test the real request flow rather than only a helper in isolation.
2. Add or update an automated test that captures the behavior you observed. The test must fail for the defect or missing behavior, not merely execute the new lines.
3. Demonstrate the red/green signal when practical: run the test against the broken state or an isolated reversion, observe failure, then restore the change and observe success. Never overwrite user work to manufacture this proof; use a temporary worktree, focused mutation, or existing failing revision.
4. Test the relevant edges, especially the worst path: invalid input, partial failure, timeout, cancellation, retry, refresh, concurrency, empty state, or boundary values. Select the cases that can actually invalidate this change instead of enumerating ritual tests.
5. Run the repository’s relevant formatter, linter, type checker, and broader test suite. Passing generic checks supports the proof but does not replace a behavior-specific test.

If a realistic test is unavailable, say exactly what was not tested and why. Provide the strongest safe substitute, but do not call the change proven or ready.

## Check the abstraction

Read the surrounding implementation, not just the edited function.

- Confirm the change agrees with upstream callers, downstream consumers, persisted state, and sibling implementations.
- Verify that types reject invalid states instead of asking runtime comments or conventions to carry the contract.
- Remove redundant helpers, speculative configurability, duplicated concepts, and comments that compensate for unclear code.
- Keep the diff scoped. Report unrelated defects separately unless fixing them is necessary to prove the requested behavior.
- Be able to explain the request flow from start to finish and each changed component in isolation.

Treat the first agent pass as a draft. Re-read the complete diff, trace the behavior through its callers and consumers, simplify it, and rerun the proof after every material correction. Generated code deserves more scrutiny, not less.

## Readiness gate

Before calling work ready, answer these questions with evidence:

1. Have I personally observed the behavior work?
2. Does a focused automated test cover it?
3. Have I seen that test fail without the fix, when practical?
4. Do the types and names tell the truth?
5. Did I test the relevant failure or worst-case path?
6. Can I walk a colleague through the change without hand-waving?

Any “no” or “not sure” means the work is not ready. Continue working when safe and in scope; otherwise report the precise gap or blocker.

## Report the proof

End implementation or review work with a compact evidence record:

- **Observed:** the manual or end-to-end flow exercised and what happened.
- **Automated:** the focused tests added or run and their results.
- **Red/green:** how failure without the fix and success with it were demonstrated.
- **Edges:** the non-happy paths verified.
- **Checks:** relevant lint, type, build, and broader test commands.
- **Gaps:** anything not proven, including environment or credential blockers.

Do not write a PR description that sounds like an unverified generated summary. Describe the behavioral contract, the implementation decision, and the evidence. Never say “ready,” “fixed,” “working,” or “all tests pass” unless the corresponding evidence exists in the current work.

Make the evidence inspectable because the human contributor owns the final accountability; the agent cannot own it for them.

The governing principle is Simon Willison’s: [“your job is to deliver code you have proven to work.”](https://simonwillison.net/2025/Dec/18/code-proven-to-work/)

## Evidence from repeated or delegated work

Read [artifact evidence](references/artifact-evidence.md) for repeated transformations, generated output, or delegated contributions. Inspect the artifact and the check itself before trusting a success report.
