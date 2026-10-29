# Graphite stacks and merging

Use `gt` for branch relationships, restacking, and PR submission in Graphite
repositories. This is the default for vstack stacks unless the user or repo
requires another tool; the user should not need to repeat it. Git remains
appropriate for inspection, staging, and signed-off commits. GitHub APIs or
`gh` remain useful for checks, reviews, and PR metadata.

## Establish the stack

Read repository instructions and inspect `gt --version`, `gt log`, `gt parent`,
Git status, worktrees, and existing PR heads/bases. Confirm the trunk and actual
parent; do not assume every PR targets main. For a new Graphite checkout,
`gt init --trunk <trunk>` establishes local metadata. Track an existing branch
with `gt track <branch> --parent <parent>` only after verifying that relationship.
Do not reset existing metadata. Resolve or report missing CLI/authentication
for operations that need them, and establish any unknown parent before changing
the stack. Do not silently rebuild the stack with plain Git. Missing `gt`
authentication need not block a configured queue action through another
authenticated interface when publication and verification are already complete.

Create a child with `gt create <branch>` from its intended parent; it commits
staged changes, or creates an empty branch when there are none. Stage only
owned files. For required sign-off, create the empty branch first and use
`git commit --signoff`, then `gt restack` if descendants need updating. Do not
invent a `gt --signoff` flag. Use `gt checkout` to navigate tracked branches.

Put fixes in their owning branch. `gt modify` amends by default and restacks
descendants; `gt modify --commit` adds a commit instead. Preserve required
trailers. A signed-off Git commit followed by `gt restack` is also appropriate.
Restacking can rewrite descendants, so inspect worktree ownership and preserve
concurrent work before using it. Resolve Graphite conflicts with `gt continue`;
do not run a competing Git rebase. Use `gt sync` after upstream merges only
when its fetch, restack, and branch-cleanup effects fit the task's ownership.

## Submit the intended branches

Check installed command help rather than guessing flags. Inspect the proposed
publication with `gt submit --dry-run` and choose the smallest authorized scope:

- `gt submit --no-stack` submits the current branch and its ancestors.
- `gt submit --stack` also submits descendants; it can publish more than the
  current PR. Use it when those branches and their changes are in scope.
- `--update-only` avoids creating PRs for branches without an existing PR.
- `--draft` creates new PRs as drafts; `--publish` publishes every submitted PR.
  Preserve each PR's intended state rather than applying a blanket flag.
- `--no-interactive --no-edit --no-ai` avoids prompts and generated metadata.
  Supply deliberate titles and descriptions, using `gh pr edit --body-file`
  afterward if needed, while preserving Graphite's stack navigation content.

Use `gt submit` for creation and branch updates rather than combining raw
`git push` and `gh pr create`. Its default lease protection rejects unexpected
remote changes. Record remote tips and retain backup refs before an authorized
published restack; never use `gt submit --force` to defeat a rejection. Fetch
and reassess concurrent changes instead. Recheck affected descendants after
restacking, and inspect every resulting PR's head, parent base, and draft state.
Link each published PR to the host thread when supported.

## Merge through Graphite's configured queue

Queue or merge only when the user's endpoint authorizes it. Discover the queue
from repository guidance and Graphite configuration/integration evidence;
GitHub rules alone do not establish whether Graphite's queue is enabled.
A Graphite-managed stack does not by itself prove a merge queue exists.

For an enabled Graphite merge queue, use its supported enqueue action. A
repository-configured enqueue label is a documented API-friendly option:
`gh pr edit <PR> --repo <OWNER/REPO> --add-label <configured-label>`.
Discover the exact label; do not invent one. Adding it to a stacked PR also
adds it to downstack PRs, so verify authorization and readiness for that scope.
Removing it propagates upstack; inspect those effects before cancellation.

For CLI merging, `gt merge --dry-run` reports all PRs from trunk through the
current branch. Inspect that set before `gt merge`; all of it must be authorized
and pass the workflow's merge gate. Confirm the installed CLI's integration
routes through the configured queue before treating this as enqueue. Otherwise
use the configured label or Graphite app's queue action. If no supported action
is accessible, report that blocker. Do not substitute `gh pr merge`, direct
GitHub merging, or an admin override for Graphite's queue. Do not use fast-track
unless requested. A no-queue repository may use its normal Graphite merge path
when merging is authorized.

Keep submission separate from merge intent: `gt submit --merge-when-ready`
can enable automatic merging for every submitted PR. Do not add it to routine
publication, review-only work, or full-stop. Full-stop must also inspect and
cancel existing Graphite merge-when-ready or queued state before pushing, using
the supported cancellation action and respecting propagation to other PRs.

Read back Graphite's merge status/comment or queue activity and the live GitHub
PR state. A label, accepted command, or merge-when-ready setting alone does not
prove queue entry or completion. Follow queue CI and ejections; repeat the gate
if the head changes. Confirm each merged PR and merge commit before reporting
success. Use the host's watcher for pending work when available.

References: [CLI commands](https://graphite.com/docs/command-reference),
[queue actions and label propagation](https://graphite.com/docs/get-started-merge-queue),
[stack merging](https://graphite.com/docs/merge-pull-requests).
