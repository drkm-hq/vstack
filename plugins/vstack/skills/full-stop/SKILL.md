---
name: full-stop
description: Prepare a change through verification, independent review, PR creation, and CI, then leave it ready for the user to merge. Use when explicitly asked for the full-stop PR workflow; an ordinary request to stop means stop.
license: MIT
---

# Full Stop

Follow [full-send](../full-send/SKILL.md) through implementation, proof, review,
PR creation, and CI, with a strict endpoint: leave the PR open and unmerged.
An explicit request to use this workflow authorizes that preparation. A user
saying "stop" or "full stop" to halt work is not invoking this workflow.

Do not merge, enable auto-merge, enter a merge queue, push to the default
branch, or delegate those actions. These restrictions also apply when calling
[babysit](../babysit/SKILL.md); override its usual queue endpoint.

Before pushing, inspect existing auto-merge and queue state. Prevent automatic
merging of this task's PR using the repository's supported cancellation action
and report the change. If that cannot be done, stop before the push and explain
the blocker. Recheck before handoff.

Use full-send's merge gate as the readiness gate. Verify the live head, base,
checks, reviews, draft state, and mergeability. Evidence must cover the final
revision. Report one of:

- **Ready to merge:** the gate passes; the PR remains open and unmerged.
- **Waiting for required approval:** identify the actual outstanding approval.
- **Blocked:** identify the missing proof, failing check, or decision.

Stop any watcher owned by this task at handoff. Return the PR, final head,
proof, review outcome, and confirmed open/unmerged state. If someone else
merged it, report that fact instead of claiming the handoff condition holds.
