---
name: adversarial-review
description: Run an adversarial code review of the current git branch by cloning it into a temporary directory and invoking Claude non-interactively with `-p`, defaulting to the `fable` model. Use when the user asks for an outside-sandbox, fable, Claude, or adversarial review of the current branch, PR, stack, or local changes, especially before pushing or addressing review comments.
---

# Adversarial Review

Use this skill to get a separate Claude pass over the current branch without touching the working tree.

## Workflow

1. Start from the repository root of the branch under review.
2. Choose the model:
   - Use `fable` by default.
   - Use the user-specified model when provided.
   - Ask one concise question when the user explicitly wants to choose the model or when using `fable` is inappropriate.
3. Choose the base ref:
   - Prefer the PR/Graphite parent branch when reviewing one layer of a stack.
   - Otherwise use `origin/main`.
   - Pass a custom base with `--base <ref>` when needed.
4. Run `scripts/run_adversarial_review.sh` from this skill.
5. Treat the review as advisory. Verify any finding against the real working tree before changing code.

## Command

From this skill directory, run:

```bash
./scripts/run_adversarial_review.sh --model fable --base origin/main
```

Useful flags:

- `--model <model>`: Claude model alias or full model name. Defaults to `fable`.
- `--base <ref>`: Git ref to compare against. Defaults to the PR base when `gh pr view` works, otherwise `origin/main`.
- `--prompt <file>`: Append extra review instructions from a file.
- `--keep`: Keep the temporary clone for inspection.
- `--dry-run`: Clone and print the Claude command without invoking Claude.

## Review Standard

Ask Claude for findings first, ordered by severity. Require file/line references, concrete failure modes, and suggested fixes. Tell it not to edit files. Good reviews focus on correctness, security, data integrity, concurrency, migration risk, API contracts, deployment behavior, and missing tests.
