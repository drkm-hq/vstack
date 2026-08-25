---
name: check-ci
description: Check GitHub Actions/CI status for the current branch or PR, diagnose failures, and propose fixes. Use when asked to check CI, investigate failing workflows, or summarize status checks for a PR.
---

# Check CI

## Overview

Use `gh` to gather CI status for a PR/branch, inspect failed runs, and propose fixes with clear next actions.

## Workflow

1. Gather PR and branch context.
2. List recent workflow runs for the branch.
3. For failures, pull job details and failed logs.
4. Categorize failures and identify root cause.
5. Report status, failures, and recommended actions.

## Commands

```bash
gh pr view --json number,headRefName,statusCheckRollup,url
gh run list --branch $(git branch --show-current) --limit 5 --json status,conclusion,name,databaseId,url
gh run view {run_id} --json jobs
gh run view {run_id} --log-failed
```

## Analysis Checklist

- Categorize: tests, lint/format, build, deploy, infra/flaky.
- For tests: identify test file/name, error, and whether code or assumptions changed.
- For lint/type: suggest `uv run ruff check --fix && uv run ruff format` and `uv run mypy`.
- For integration: check environment dependencies, timeouts, or race conditions.

## Output Format

```markdown
## CI Status: {PASSING|FAILING|PENDING}

### Workflow Runs
| Workflow | Status | Conclusion | Link |
|----------|--------|------------|------|
| ... | ... | ... | ... |

### Failures (if any)

#### {Job Name}
- **Error:** Brief description
- **File:** `path/to/file.py:line`
- **Root Cause:** Analysis
- **Proposed Fix:** Specific action

### Recommended Actions
1. [ ] First action
2. [ ] Second action
```

## Notes

- If no PR exists, use branch runs only.
- Do not propose changes without inspecting failing logs or code.
