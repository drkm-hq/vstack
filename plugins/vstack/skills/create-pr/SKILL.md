---
name: create-pr
description: Create or update a GitHub pull request or prepare a dependency-ordered PR stack from the current work. Use when the user asks to open, submit, update, or organize PRs for shipping.
---

# Create PR

Read [contribution and stack guidance](../yeet/references/contributions.md)
when preparing to ship. Use the repository's instructions and PR template.

## Establish what to publish

Inspect the worktree, current branch, remote, and existing PR before choosing
the head and base. Keep unrelated changes out of the contribution. Reuse an
existing PR for the branch instead of creating a duplicate.

For a standalone PR, use the intended integration branch. For a stack, base
each PR on its actual parent and describe only that contribution's changes.
Use the existing Graphite relationships when available. Do not target every
stack entry at the default branch or consolidate a stack without an agreed
mapping. Apply the shared guidance before restructuring changes.

## Prepare the contribution

If the relevant work needs formatting, verification, committing, or pushing,
use `yeet` for that preparation. Reuse verification evidence for the unchanged
revision; run additional checks when changed code or missing evidence warrants
them. Respect an explicit instruction to leave commits or pushes undone.

Read the complete proposed diff and the repository's review guidance before
requesting review. When gaps remain, describe them accurately and use a draft
PR unless the user specified otherwise. Creating a PR does not authorize
merging it, deploying it, or rewriting published history.

## Write and publish

Lead the title and description with the capability and the problem it solves.
Explain the final behavior, consequential choices, and actual verification.
For a stack, identify dependencies and the scope available at this branch's
tip. Scale the description to the change and follow the repository template.

Use the available GitHub tools or `gh` to create or update the PR. When GraphQL
is rate-limited, the REST API is an alternative; preserve the exact head, base,
draft state, and body. Inspect title, body, quotes, and attachments for private
material before publishing. Follow repository attribution rules; when adding
model credit, use only a model identity exposed by the harness. Do not guess.
For an authorized follow-up comment, use
[leaving-pr-comments](../leaving-pr-comments/SKILL.md); creating a PR alone
does not require a comment. Attach the created or updated PR to the current
chat when the host provides that capability.

With `gh`,
write multiline descriptions to a temporary file and pass `--body-file`.
Specify the intended head and base when creating the PR. Inspect existing
description content before updating it so contributor context is preserved.

Report the PR link, base branch, draft status, and any unresolved verification
or publishing blockers. Stop after the requested publishing work.
