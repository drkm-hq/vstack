# Maintain a verification skill

Keep a verification recipe accurate. Edit only the target skill, its feature map, and its owned helpers. Report product regressions separately instead of changing the map to bless them.

1. Locate the target in the repository's skill roots. Inspect its launch and drive instructions and feature index. If several plausible targets remain, clarify the intended app. If none exists, use [create-verification-skill](../SKILL.md) when creation is requested.
2. Reconcile the index with feature files and source entry points. For each feature, identify likely drift and a concrete live recipe. A broad map can use authorized read-only delegates with disjoint feature ownership; the coordinator owns all app interaction.
3. Run the skill's health check and drive every mapped feature in the authorized environment. Reuse one owned instance where appropriate. After an unexpected failure, check health again and restore known state before continuing.
4. Capture each feature's action and observable outcome. Preserve proof through cleanup. Mark unavailable prerequisites or unreachable routes explicitly; they are coverage gaps, not successful verification.
5. Correct documented drift or helper defects within scope, then re-drive affected recipes. If a focused correction does not restore the path, report the blocker instead of guessing through repeated resets.
6. Clean up only processes and scratch state the run created. Inspect changed files and validate the skill. Publishing a PR or scheduling future runs requires that work to be part of the user's request.

Report `clean`, `changed`, or `blocked`, with source coverage, live coverage, corrections, and remaining gaps. A source-only audit may still be useful, but cannot establish a clean live pass.
