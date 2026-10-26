---
name: babysit
description: Check CI status, diagnose failures, or shepherd a PR through requested repairs, reviews, and shipping. Use for CI checks, PR monitoring, or babysitting; a status request is read-only and never implies merge permission.
---

# Babysit

Select the endpoint from the user's request before taking action:

- **Status or diagnosis:** follow [CI status](references/ci-status.md), report
  the evidence, and stop. This mode is read-only and works without a PR.
- **Watch only:** observe changes without edits, replies, retries, or merging.
- **Repair or ready for review:** fix and verify within scope, preserving the
  user's commit/push boundary; do not queue or merge.
- **Babysit through shipping:** handle verified fixes and review feedback,
  then use the repository's merge queue and follow it through merge. Observe
  deployment only when production delivery is requested.

The remaining sections support those endpoints; loading this skill does not
upgrade a status or repair request into shipping. Keep updates terse.

## Establish the target and scope

- Resolve the PR from an explicit number or URL, the chat's attached PR, or the current branch. A detached checkout or several plausible PRs requires clarification; never pick the newest PR by assumption. Attach the target PR to the chat when the app supports it.
- Read repository instructions and inspect the worktree before editing. Record the repository, PR number, head branch and SHA, base, draft state, review decision, and queue provider. Preserve unrelated local work and existing stack dependencies.
- An explicit invocation to babysit a PR through this workflow authorizes relevant code fixes, verification, commits and pushes, evidence-based review replies and resolutions, and ordinary merge-queue submission. Respect narrower instructions such as watch-only or do-not-merge. Do not expand this into unrelated messages, bypassed branch protections, or manual production operations.

## Inspect the current revision

Use GitHub APIs or `gh` to collect all check runs, statuses, review threads, review summaries, and ordinary PR comments. Paginate collections; `gh pr view --comments` alone does not cover inline review threads. Capture comment IDs and links so every finding can be accounted for.

Useful starting points:

```bash
gh pr view <PR> --repo <OWNER/REPO> --json url,headRefName,headRefOid,baseRefName,isDraft,mergeStateStatus,reviewDecision,statusCheckRollup
gh pr checks <PR> --repo <OWNER/REPO>
gh run view <RUN_ID> --repo <OWNER/REPO> --log-failed
```

Read findings against current source, including unresolved comments marked outdated. Classify each actionable finding as requiring a fix, already addressed, or unsupported by the code. Verify bot findings instead of accepting them automatically. Pending, missing, or skipped checks are not proof that required verification passed.

## Fix and verify

- Diagnose failing checks from logs and relevant code before editing. A failure outside the diff can still be caused by the PR. Use reproduction and run evidence to distinguish defects from infrastructure problems.
- Make scoped fixes consistent with the codebase. Exercise the affected behavior and run relevant formatting, lint, type, unit, and integration checks. Add regression coverage when it meaningfully protects the corrected behavior. Follow repository-specific skills and verification commands where available.
- Read the final diff, commit using repository conventions, and push to the actual PR head. Do not force-push or rewrite unrelated stack history as a routine repair.
- After pushing, record the new SHA and evaluate checks and reviews for that revision. Old green checks do not validate a new head. If another contributor changes the branch, refresh before proceeding.
- Rerun a failed job only when evidence supports a transient cause. Bound reruns, normally at most two for the same failure; repeated failures require diagnosis or a concrete blocker report. Never repeatedly rerun tests merely to obtain a green result.

## Address and resolve review comments

Use [PR comment guidance](../create-pr/references/pr-comments.md) for authorized
replies. For each actionable comment, reply briefly with the fix commit and relevant verification, or a specific code-based explanation when no change is needed. Avoid duplicate replies on repeated monitoring passes.

Resolve a review thread only after its concern is demonstrably addressed or disproven. Outdated status alone is insufficient. Ordinary PR comments and review summaries cannot be resolved like inline threads; address their concerns and track their disposition. Do not dismiss a blocking review or manufacture approval to clear the queue. If a reviewer or owner must act, identify the exact remaining action.

## Queue and delivery

Immediately before queue submission, refresh the head SHA, required checks, unresolved threads, approvals, mergeability, and stack dependencies. Proceed only when the current revision is green, review concerns are accounted for, and required approvals and prerequisites are satisfied. Mark a draft ready only when this shipping request authorizes it and those readiness conditions hold.

Determine the configured queue from repository instructions, rules, and existing integration evidence. Use its supported enqueue action. For a GitHub native merge queue, after confirming that the target branch requires that queue:

```bash
gh pr merge <PR> --repo <OWNER/REPO> --match-head-commit <VERIFIED_SHA>
```

That command can merge directly on a branch without a native queue; do not use it as a generic enqueue command for Graphite or another provider. Never use `--admin`, disable checks, or bypass the configured queue. If no queue exists or its supported action is unavailable, report the blocker rather than silently switching to a direct merge.

Read back the queue state after submission. Distinguish auto-merge enabled, actually queued, merged, and deployed. Follow queue checks for the merge candidate; diagnose ejection or failure and re-enter only after the cause is fixed. If the head changes before submission, repeat the readiness gate for the new revision.

When the requested outcome includes production, inspect the repository's deployment workflow and observe the deployment corresponding to the merged commit. Queue entry or merge alone does not establish production delivery. Report unavailable deployment evidence accurately; do not start ad hoc production writes.

## Continue without losing ownership

Use one watcher per PR. Prefer a host-native watcher when available; otherwise
`gh pr checks <PR> --repo <OWNER/REPO> --watch --interval 30` watches checks
only, so inspect review threads and mergeability separately. A check watcher
is not a merge gate. Keep shell waits within host tool limits. On rate limits,
respect the reset time or use the independently limited REST API; do not run
duplicate pollers or restart in a tight loop. Stop only watchers owned by this
task. Do not hardcode a review-bot allowlist: repository requirements decide
which checks and approvals gate shipping.

During active work, use bounded status checks and keep the user informed of meaningful changes. For monitoring that must continue after the turn, use the app's heartbeat automation when available. Reuse a matching automation instead of creating duplicates, and save the exact PR, latest known SHA, authorization scope, outstanding findings, and completion condition in its prompt.

Tell the heartbeat to stay quiet while state is unchanged or non-actionable and notify only on meaningful progress, completion, failure, or required user action. Stop the monitor at the requested endpoint or when the PR closes without merging. Pause and report a concrete blocker when access, required human approval, repeated unexplained failures, or a product decision prevents safe progress; do not retry indefinitely. If scheduling is unavailable, state that ongoing monitoring has not been established.

Finish with the PR link, verified revision, checks and review disposition, and confirmed queue/merge/deployment state. Name any remaining blocker precisely. Never claim queued, green, resolved, merged, or deployed without read-back evidence.
