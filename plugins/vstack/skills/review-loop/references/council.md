# Council review

Use this mode only for a requested council or cross-provider review. Follow
the parent skill's scope, read-only reviewer rules, evidence standard, and
three-round default budget.

Use configured council members, or discover one capable reviewer from each
of three providers. Use high reasoning effort where supported. If a named
member or three distinct providers are unavailable, report the missing
coverage; do not silently substitute or count same-provider models as three
providers.

Start independent reviewers in parallel within available capacity. Give each
the same goal, revision, raw diff, and check results without showing the
others' answers. Reviewers cannot edit, publish, or delegate further. Ask for
file/line evidence, concrete failure modes, severity, and a score out of 10.
Scores are advisory; verify findings against code and observed behavior.

Reconcile overlapping findings in one ledger. For authorized fixes, request
fresh review of changed behavior and unresolved findings within the budget.
Do not let repeated review expand the task. A review-only request ends with
findings; it does not authorize fixes or PR edits.

Record actual models, rounds, scores, disagreements, and dispositions.
Never invent missing scores or usage. When PR editing is part of the request,
include a compact round-by-round table in its description; otherwise return
results in chat. An unavailable or silent reviewer is not approval.
