---
name: review-loop
description: Review a scoped change with one independent reviewer, verify findings, and iterate within a bounded budget. Use when the user requests an iterative review or a shipping workflow calls for it.
license: MIT
---

# Review Loop

Use the reviewer and model the user requests, then any repository or personal
reviewer configuration. Otherwise use the host's configured default for a
separate reviewer. Discover actual capabilities rather than guessing model IDs.
Do not silently substitute a specifically requested model. If it cannot run,
report the missing prerequisite.

Use native subagents or a configured reviewer CLI. In T3 Code, use capability
discovery and `delegate_task` only when available. A separate reviewer must
inspect the raw change independently; the author's self-review is not a second
reviewer. If no independent runner is available, report that limitation.

## Scope and budget

Inspect worktree status and establish the actual PR base or intended local
base. Record the head and include relevant staged, unstaged, and untracked
changes. Preserve unrelated edits. Give the reviewer the goal, scope, base,
exact diff or revision, and observed check results. Do not edit scoped files
while review runs.

Default to three rounds: a full first pass, then changed behavior and open
findings only. Extend to five only when security, authorization, data loss, or
concurrency findings justify it, or when the user asks. Stop early for nits.
Use one reviewer at a time; that reviewer must not delegate further. A review
request alone does not authorize implementation or publication.

## Reviewer brief

Ask for a read-only review: no edits, commits, pushes, PR comments, or agents.
Require surrounding-code inspection, concrete failure modes, and stable IDs:

```text
VERDICT: APPROVE or CHANGES
S1 [blocker|should|nit] file:line — observed problem and suggested correction
```

Blockers break the intended case or a consequential invariant. "Should"
findings are real defects in affected callers; nits are optional improvements.
Judge by evidence and impact, not frequency alone: a rare data-loss or security
failure can still block. Unsupported claims and timeouts are not approval.

## Resolve and repeat

Maintain a short ledger of ID, severity, evidence, and disposition. Verify each
finding against source or a reproduction. Make the smallest justified fix when
edits are authorized; disagree with evidence when it is wrong; defer unrelated
improvements. Rerun checks affected by fixes.

Request another round only if behavior changed, a material finding remains,
or approval no longer covers the current diff. Supply the original scope,
ledger, and delta; ask the reviewer to close or substantiate each open item.
Wait through the host's supported mechanism. On reviewer failure, establish
that it stopped before restarting; do not run duplicate reviewers.

Finish when the current behavior is approved and material findings are
resolved. A finding disputed after two replies or an exhausted round budget
is a blocker to agreement, not permission to ship. Report both positions and
the remaining decision. Push only when publishing is part of the user's task.
If updating a PR, record actual rounds, model, and verdict in its description.
Report fixed and declined findings, checks, and any unverified behavior.
