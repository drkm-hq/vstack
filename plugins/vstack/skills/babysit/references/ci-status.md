# One-time CI diagnosis

A status request is read-only and ends with the report. Do not start a
watcher, retry jobs, change code, post comments, or queue a PR just because a
check is failing.

Resolve the requested PR or branch and record the current head SHA. If no PR
exists, inspect branch runs. Distinguish checks for the current head from
older runs.

```bash
gh pr view <PR> --repo <OWNER/REPO> --json url,headRefName,headRefOid,statusCheckRollup
gh pr checks <PR> --repo <OWNER/REPO>
gh run list --repo <OWNER/REPO> --branch <BRANCH> --limit 5 --json headSha,status,conclusion,name,databaseId,url
gh run view <RUN_ID> --repo <OWNER/REPO> --json jobs
gh run view <RUN_ID> --repo <OWNER/REPO> --log-failed
```

Classify each failure from logs and relevant code: tests, lint/types, build,
deployment, or infrastructure. Name the failing behavior and repository
command, and distinguish a demonstrated cause from a hypothesis. Use
[revision and failure guidance](pr-monitoring.md) to avoid treating old green
runs or repeated failures as proof about this revision.

Report passing, failing, pending, or unavailable status, with the revision,
relevant run links, supported diagnosis, and recommended next action.
Stop there unless the user requested repairs or continuing monitoring.
