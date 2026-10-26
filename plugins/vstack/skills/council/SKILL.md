---
name: council
description: Obtain independent reviews from three model providers and reconcile supported findings within a bounded review budget. Use when the user requests a council or cross-provider review.
license: MIT
---

# Council

Use the user's configured council members. Otherwise discover available
models and choose one capable reviewer from each of three providers. Use high
reasoning effort where supported. Never invent a model ID or substitute a
named member without agreement. If three providers are unavailable, report
which can run and the missing coverage; three same-provider reviews are not
a cross-provider council.

Use the host's delegation tools. In T3 Code, discover capabilities and use
`delegate_task` only when those tools are available. Elsewhere use native
subagents or configured provider CLIs. Give each reviewer the same goal,
exact revision or scoped diff, relevant raw context, and verification results.
Ask for independent findings without showing other reviewers' answers.
Reviews are read-only; reviewers must not edit, publish, or start more agents.

For code review, require concrete failure modes, file/line evidence, severity,
and a score out of 10. A score is advisory, not a merge gate. Verify findings
yourself. Implement agreed fixes only when the request includes edits;
a review-only request ends with findings.

Default to at most three rounds. The first reviews the whole change; later
rounds examine changed behavior and unresolved findings. Stop early when no
material findings remain. Do not extend the loop for nits or let reviewers
expand the task. At budget exhaustion or persistent disagreement, report the
evidence on each side and what remains unresolved. Silence, failure, or an
unavailable reviewer is not approval.

Record actual models, rounds, scores, and dispositions. Never invent missing
scores or usage. When PR creation or editing is part of the request, put a
compact round-by-round table in its description while preserving existing
content. Otherwise return results in chat; council invocation alone does not
authorize PR edits or comments.
