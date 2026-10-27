# Monitor the current PR revision

Record the PR head SHA, base, latest push, checks, and review state. Diagnose actionable checks and findings for the current revision; do not act on stale comments as if they describe the latest code. Re-read any carried-forward unresolved finding against current source.

Verify bot findings before editing. Fix only defects within the authorized task. When authorized to respond and resolve review threads, provide a short evidence-based reason for each dismissal; do not silently leave a blocking thread behind. A bare request to check status is not authorization to post comments.

Classify a failing check from its logs. Rate limits, interrupted runners, and external outages may justify a bounded rerun. A failure outside the diff is not automatically unrelated, and a repeated failure is not automatically deterministic. Use timestamps, environment, and reproduction to distinguish code defects from flakes.

After a fix, rerun affected checks and evaluate the new head. Keep one owner for each branch or stack. If merging is explicitly authorized, follow the requested order, update and re-verify each next PR after the prior merge. Otherwise stop at the requested readiness state.

For requested ongoing monitoring, use available Codex automation tools and keep notifications quiet while state is unchanged or non-actionable. Notify on meaningful progress, completion, failure, or required action. Do not introduce a polling loop or background process for an ordinary status query.

Adapted from pstack: [poteto-mode/playbooks/babysit.md](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/poteto-mode/playbooks/babysit.md), [poteto-mode/playbooks/shipping.md](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/poteto-mode/playbooks/shipping.md).
