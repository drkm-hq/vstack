---
name: grab
description: Pull a GitHub PR's full content into context via the gh CLI — metadata, diff, and the complete post-change contents of every changed file.
---

Argument: a PR number or URL. If omitted, default to the PR for the current branch via `gh pr view`.

Pull ALL content of the target PR into context so you can discuss, explain, or review it with full knowledge. Run the commands — do not guess.

## Step 1 — Metadata
```bash
gh pr view <PR> --json number,title,body,baseRefName,headRefName,state,url,additions,deletions
```
Add `,comments,reviews` to the `--json` list only if the user asks about the PR discussion.

## Step 2 — Changed file list
```bash
gh pr view <PR> --json files -q '.files[].path'
```

## Step 3 — Full diff
```bash
gh pr diff <PR>
```
For very large PRs, chunk it: `gh pr diff <PR> | head -n 500` / `gh pr diff <PR> | sed -n '500,1000p'`, or go per-file via `gh api repos/{owner}/{repo}/pulls/<PR>/files --paginate`.

## Step 4 — Full post-change file contents
For each changed file, get the complete contents as of the head branch:
- Prefer the local checkout (avoids API rate limits):
  ```bash
  git show <headRefName>:<path>
  ```
  If that fails, fetch then read the remote ref:
  ```bash
  git fetch origin <headRefName>
  git show origin/<headRefName>:<path>
  ```
- Fall back to the API when there is no local clone:
  ```bash
  gh api repos/{owner}/{repo}/contents/<path>?ref=<headRefName> --jq .content | base64 -d
  ```
- Skip binary files. For deleted files, note the deletion instead of fetching content.

## Step 5 — Load it
Actually run these commands and read the output into context. For large local files, use the Read tool on the file rather than dumping it through the shell. Do not summarize prematurely — the goal is to HAVE the content in context.

## Output
After grabbing, confirm what was loaded: PR title, N files changed, +additions/−deletions. Then perform (or await) whatever analysis the user requested alongside the grab.

## Do not
- Don't fetch content for files >2000 lines in one gulp — read them in chunks.
- Don't grab vendored files or lockfiles (`package-lock.json`, `uv.lock`, `*.min.js`) unless asked.
- Don't use the GitHub web UI or scraping — use the `gh` CLI only.
