# Vishaal's Skills

A portable collection of personal engineering skills for Claude Code and Codex.

## Install in Claude Code

```bash
claude plugin marketplace add vishytheswishy/skills
claude plugin install vishaal@vishaal-skills
```

Restart Claude Code after installation so the new skills are discovered.

## Install in Codex

```bash
codex plugin marketplace add vishytheswishy/skills
codex plugin add vishaal@vishaal-skills
```

Start a new Codex task after installation so the new skills are discovered.

## Included skills

| Skill | Purpose |
| --- | --- |
| `adversarial-review` | Run an independent Claude review in a temporary clone. |
| `check-ci` | Diagnose GitHub Actions failures and recommend next steps. |
| `cli-creator` | Build durable, composable command-line tools for agents. |
| `deslop` | Remove unnecessary AI-generated code patterns from a diff. |
| `grab` | Load a pull request's metadata, diff, and changed files into context. |
| `grill-me` | Pressure-test a plan, design, or technical argument with pointed questions. |
| `meaningful-contribution` | Require observable proof before declaring code complete. |
| `resolve-conflicts` | Analyze and resolve merge conflicts while preserving branch intent. |
| `tdd` | Develop behavior incrementally with red-green-refactor cycles. |
| `trace-request-flow` | Trace a concrete request through every participating system. |
| `yeet` | Format, verify, sign off, commit, and push relevant changes. |

## Validate locally

```bash
python3 scripts/validate.py
claude plugin validate --strict .
```
