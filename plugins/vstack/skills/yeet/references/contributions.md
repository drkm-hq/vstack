# Contributions and stacked PRs

Apply this guidance when preparing to ship. Follow the user's agreed scope
and the repository's contribution rules.

## Contribution boundaries

- Each PR delivers a coherent capability or an independently meaningful
  dependency change. Judge reviewability by the behavior and ownership a
  reviewer must understand; do not split by file or an arbitrary line count.
- Include relevant tests and documentation with the implementation. Introduce
  shared fixtures with their first consumers. A separate acceptance PR must
  verify a meaningful integrated capability.
- Reuse existing abstractions and repository patterns. Justify new abstractions
  by their present consumers.
- If shipping requires a substantial split or consolidation not already agreed
  with the user, present the proposed capability-to-PR mapping before rewriting
  the changes. Prior approval remains authorization for the agreed mapping.

## Stack changes

Read [Graphite workflow](graphite.md) for stacks and Graphite repositories.
Use `gt` for stack creation, tracking, restacking, and submission by default;
choose the configured Graphite merge queue when the endpoint includes merging.
Do not wait for the user to repeat this tool choice.

- Prefer a linear Graphite stack in dependency order when preparing a stack.
  Explain necessary side branches and which changes are absent from each tip.
- Put review fixes in their owning PR and restack descendants. Avoid a catch-all
  fix PR that obscures ownership.
- Preserve concurrent work when restacking. Before an authorized rewrite of
  published history, retain backup refs and record the expected remote tips;
  protect Graphite submissions with their default lease protection, or Git
  pushes with explicit force-with-lease expectations. This guidance
  does not itself authorize rewriting published history.
- Before consolidating existing PRs, establish the mapping from old PRs to new
  ones. Preserve review history and link superseded PRs to replacements. Earlier
  approvals do not cover substantially rewritten changes.
- For multi-stage shipping work, report progress by completed capabilities and
  honor the user's agreed review milestones.

## Review evidence

Read the repository's review guidance before requesting review. Describe each
PR's capability, why it is needed, and the observed verification evidence.
Distinguish completed checks from skipped checks and unproven behavior.
