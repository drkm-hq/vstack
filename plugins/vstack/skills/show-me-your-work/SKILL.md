---
name: show-me-your-work
description: "Keep a compact, evidence-linked decision log for long or multi-phase work. Use when the user asks for an audit trail or reviewable record of decisions and outcomes."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/show-me-your-work
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Show me your work

Record consequential decisions and observable results. This is a concise decision record, not a transcript of hidden reasoning.

Use one TSV with columns `ts`, `phase`, `decision`, `why`, `evidence`, and `result`. The [template](references/decision-log-template.tsv) supplies the header. Evidence cells contain paths, URLs, revisions, or file references.

Append a row with the executable helper from this skill directory:

```sh
./scripts/log.sh /path/to/decisions.tsv design 'Keep the existing parser' 'It covers the required format' /path/to/test-output.txt 'Focused tests passed'
```

The helper stamps UTC time, creates the parent directory and header, flattens tabs and newlines, and prefixes cells beginning with spreadsheet formula markers. It does not lock a shared file: one coordinator writes the canonical log. Give parallel workers separate outputs.

Log a choice, rejected experiment, completed unit, changed assumption, verification result, or blocker. Write only events that happened, with short user-facing reasons. Never include credentials or copy unrelated private conversation content.

Keep the log in a task scratch directory unless the user wants it in the repository. A log does not authorize committing or publishing. Correct inaccurate entries with a superseding row so the sequence remains inspectable.

Before delivery, compare rows with observed tool results and artifacts. Check that evidence paths resolve and support the claim. Report weak evidence and missing verification. Use an independent reviewer only when such review is authorized and useful; do not invent a reviewer or model name.

Return the log path and any consequential gaps. Do not add ceremonial logging to routine edits.
