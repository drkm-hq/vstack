---
name: adversarial-review
description: Run an independent adversarial review of committed branch changes in a temporary clone using the Claude CLI. Use when asked for an isolated or adversarial review; use review-loop for a model-agnostic iterative review.
---

# Adversarial Review

Run the bundled helper from the repository being reviewed, using the helper's
absolute path. It reviews committed state only and refuses a dirty worktree
rather than silently omitting changes. For uncommitted work, use a native
read-only reviewer with the complete diff or commit only when authorized.

```bash
/path/to/adversarial-review/scripts/run_adversarial_review.sh --base origin/main
```

Resolve the actual PR or stack parent; do not assume every PR targets main.
The helper tries the current PR base, then the remote's configured default.
Fetch the intended base beforehand when current remote state matters.

The helper runs Claude in print mode with the CLI's configured model. Set
`ADVERSARIAL_REVIEW_MODEL` or pass `--model` for an available model or personal
alias such as `fable`. `CLAUDE_BIN` overrides the executable. Do not pass a
Codex binary: its noninteractive interface differs. For an iterative review with a different runner, use [review-loop](../review-loop/SKILL.md).

Flags:

- `--base REF`: source-checkout ref or commit to compare against.
- `--model MODEL`: explicit model supported by the configured Claude endpoint.
- `--prompt FILE`: append task-specific review context.
- `--keep`: retain the owned temporary clone and prompt for inspection.
- `--dry-run`: prepare the clone and print the command without running a model.

The helper pins the source head and resolved base, uses no remote fetch, and
cleans its clone on normal completion or failure unless `--keep` is set.
It preserves the reviewer's exit status. The clone isolates repository edits;
it is not an operating-system sandbox or permission to bypass host controls.

Require findings ordered by severity with file/line references, a reachable
failure, consequence, and evidence. Treat review as advisory and verify claims
against the actual code before fixing them. Read
[review lenses and triage](references/review-lenses.md) for a broader review.
