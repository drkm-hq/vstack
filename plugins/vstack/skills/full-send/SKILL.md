---
name: full-send
description: Finish a scoped change through verification, independent review, PR creation, CI, and merge when the user explicitly requests the full-send workflow.
license: MIT
---

# Full Send

An explicit request to use this workflow authorizes finishing the requested
change, committing, pushing, opening or updating its PR, addressing review
feedback, and merging after the gate below passes. Preserve narrower user
instructions. Merely mentioning this skill does not invoke it. Production
operations, unrelated changes, and branch-protection bypasses remain outside
this workflow.

1. Establish the goal, intended base, current head, worktree ownership, and
   repository conventions. Read [Graphite workflow](../yeet/references/graphite.md)
   for stacks or Graphite repositories; use `gt` for their branch lifecycle and
   submission. Create a task branch if on the default branch.
2. Finish the scoped change. Use [meaningful-contribution](../meaningful-contribution/SKILL.md)
   for direct evidence: reproduce a fixed failure, exercise affected behavior,
   and run appropriate checks. Report unavailable evidence.
3. Get independent review with [review-loop](../review-loop/SKILL.md). Honor a user
   or repository choice of reviewer instead. If the requested reviewer cannot
   run, report the gap rather than inventing approval or silently substituting.
4. Use [create-pr](../create-pr/SKILL.md) to verify, commit, push, and create or
   update the PR. Describe the problem, resulting behavior, and observed proof.
5. Use [babysit](../babysit/SKILL.md) for CI, review replies, and verified fixes.
   This workflow's explicit merge request permits the repository's normal
   direct merge if it has no queue; otherwise use its queue. For Graphite, use
   the configured Graphite merge queue action, with `gt merge --dry-run` to establish any CLI merge scope;
   never substitute `gh pr merge` for Graphite enqueue. Follow through to
   confirmed merge. Changes after review need appropriately scoped rechecking.

## Merge gate

Refresh the live head, base, checks, reviews, and mergeability immediately
before merging. Evidence must cover the final change; required checks and
approvals must pass; actionable findings must be addressed; no unresolved
blocking human review may remain. Missing or skipped required verification is
not success. Reassess new base commits that affect the change and reverify
meaningful conflict resolutions. Honor the repository's update requirements.

Use the configured merge method or queue, tied to the verified head when the
tool supports it. Never use an administrative bypass. Queue entry or
auto-merge is not proof of merge; read back the merged commit.

Preserve concurrent branch work. If a published rebase is necessary and
authorized, save the old head and record the expected remote tips. Use
Graphite's default submit lease protection for the authorized stack, or an explicit Git force-with-lease
expectation for this task's branch only. A lease rejection requires reassessment.

## Completion and blockers

Stay active through the requested endpoint. Use one available watcher, or the
host's automation mechanism for an explicitly requested continuing monitor;
do not end the turn assuming an ordinary shell command will wake the chat.
Honor tool wait limits and report meaningful progress without repeated status
noise. Stop at a concrete blocker such as missing access, required human
approval, unavailable proof, or a scope decision. A review budget ending is
not approval.

Report the PR, merge commit, verification, reviewer outcome, and consequential
decisions. If blocked, state what is complete and the exact remaining action.
