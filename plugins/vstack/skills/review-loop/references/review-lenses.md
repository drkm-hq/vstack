# Review lenses and triage

Establish the intended behavior, exact base and head revisions, and constraints before review. Supply the same raw diff and relevant context to independent reviewers; do not seed them with the parent's expected findings.

For an explicitly requested panel, partition lenses such as correctness and lifecycle, contracts and data migration, security boundaries, and interface quality. Use supported requested models or the existing configured default; do not invent provider availability. Reviewers are read-only and own no production files.

Require each finding to name a concrete failure, reachable trigger, file and line, consequence, and supporting evidence. A preference, hypothetical path, or opinion about abstraction is not a defect without a consequential contract violation.

Deduplicate findings, inspect the real code, and test consequential claims when safe. Classify each as act, consider, or dismiss with a short reason. Agreement between reviewers is not proof. Keep the final findings ordered by severity and make gaps explicit.

Apply fixes only when requested or included in an existing authorized implementation task. Do not add unrelated changes to satisfy a reviewer. Posting review comments or resolving remote threads also requires that communication to be authorized.

Adapted from pstack: [interrogate](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/interrogate).
