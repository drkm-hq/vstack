---
name: resolve-conflicts
description: Resolve git merge, rebase, or restack conflicts by analyzing both sides' intent, preserving current contracts, and verifying the result. Use for a requested integration operation or conflicted files.
---

# Resolve Conflicts

Establish the operation, announce the concrete resolution, and proceed within
the user's requested scope. Resolving a rebase does not authorize merging a
PR, deleting branches, or overwriting unrelated changes.

## Establish intent and state

Inspect status, the current operation, branch or detached head, remote, and
intended target. If a merge or rebase is already running, continue that
operation rather than starting another. Preserve unrelated local work.

Resolve the actual PR base, Graphite parent, or user-named target; do not
assume main. Fetch the relevant refs and inspect both sides from their merge
base. Read surrounding callers, tests, commit messages, and repository rules.
For an aging PR whose design may be obsolete, use
[modernize](../modernize/SKILL.md) before choosing what to preserve.

For each conflict, identify the behavior each side intended, any newer
contract, and what the combined result must do. During a rebase, Git's
"ours" and "theirs" refer to the rebase sides; do not equate them blindly with
the user's branch and the remote branch.

## Resolve and prove

Use the requested tool: Graphite for its restack, Git rebase for a rebase,
or Git merge for a merge. Do not introduce a merge commit into a requested
linear history. Remember that `git merge --no-commit` can still fast-forward;
choose flags appropriate to the intended operation and checkpoint.

State the resolution plan before editing: preserve, combine, or rewrite the
specific behaviors and explain consequential tradeoffs. Ask only when an
unresolved product decision would change the result. Resolve in dependency
order, including schemas, generated outputs, callers, and tests as needed.
Regenerate generated files using repository commands.

Stage only resolved files. Inspect `git diff --check`, unmerged paths, and the
staged result. Run the repository's relevant checks; do not assume Python or
any particular test runner. Compare the resulting behavior with both sides'
intent. For a rewritten commit series, use `git range-diff` against the saved
pre-rebase revisions to catch accidental omissions.

Finish with the owning tool: `gt continue`, `git rebase --continue`, or the
appropriate merge commit. Do not bypass hooks or validation. Push only when
publication is requested. For Graphite, follow [Graphite workflow](../yeet/references/graphite.md)
and use `gt submit` with its default lease protection after rechecking affected
branches. For other authorized published-history rewrites, retain the observed
remote head and use an explicit force-with-lease expectation; if a lease fails,
fetch and reassess concurrent work.

Report the preserved behaviors, consequential decisions, checks and gaps,
completed operation, and publication state.
