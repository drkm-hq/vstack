---
name: yeet
description: Run the repository's formatter, linter, unit tests, and integration tests before shipping when available, then create a meaningful signed-off git commit and push it. Use this skill when the user asks to clean up, verify, commit, or push local changes.
---

# Yeet

## Overview

Use this skill when the user wants a standard "wrap up and ship it" workflow. It must run the repo's formatter first, then verify the current changes with linting and tests, stage only the relevant files, commit with a concise message using `git commit --signoff`, and push the current branch unless the user explicitly asks not to push.

## Workflow

1. Inspect the worktree with `git status --short` and identify unrelated local changes before staging anything.
2. Discover the repo's standard verification commands from `package.json`, existing scripts, or nearby project conventions.
3. Run formatting first. If the repo exposes a formatter, this step is mandatory for every yeet flow before linting, tests, or commit.
4. Run unit tests for the touched area when possible. Prefer targeted tests over the full suite unless the user asked for a broad verification pass or the repo only exposes one unit-test command.
5. Run integration tests before committing or pushing whenever the repo has an integration path. Only skip them when there is a concrete blocker such as missing services, credentials, browsers, or long-running infrastructure, and state that blocker explicitly.
6. If verification fails, stop and report the failing command unless the fix is obvious and directly related to the current task.
7. Stage only the files relevant to the user's requested change. Never sweep unrelated edits into the commit.
8. Write an imperative commit message that reflects the change, not the mechanics.
9. Commit with Vishaal sign-off using `git commit --signoff -m "<message>"`.
10. Push the current branch with `git push`. If the push is rejected because the remote branch moved, integrate the remote changes safely first, such as with `git pull --rebase`, then push again. Do not force-push unless the user explicitly asks for it.

## Command Policy

- Prefer the repo's explicit commands such as `pnpm run format`, `pnpm run lint`, `pnpm test`, `pnpm jest ...`, `pnpm vitest ...`, `pnpm playwright test`, or project-specific wrappers.
- If a repo exposes a `format` script, you must run it on every yeet flow instead of calling `prettier` directly.
- If both unit and integration commands exist, run the narrowest useful unit coverage first, then integration coverage, and do both before shipping.
- If there is no integration test command, say that clearly in the final update.
- Push after a successful commit by default. If the user explicitly says not to push, skip it and say so.

## Commit Rules

- Use a meaningful subject line such as `Tighten chart prompt color guidance`, not `fix stuff` or `update files`.
- The commit must include the contributor's configured sign-off via `git commit --signoff`.
- If the user asked to amend or squash, follow that instruction; otherwise create a normal commit.

## Reporting Back

Report:

- which commands were run
- which tests were skipped and why
- the final commit hash and message
- whether the branch was pushed or left local
- if pushing required rebasing or other non-destructive remote integration
