# vstack

Vishaal's engineering stack for Claude Code and Codex: 32 skills combining
personal workflows with selected, adapted [pstack](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack)
and [tstack](https://github.com/t3dotgg/tstack) guidance.

The aim is one clear workflow per job, direct proof before shipping, and short,
useful handoffs. This is the consolidated home of
[vishytheswishy/skills](https://github.com/vishytheswishy/skills).
See [sources and consolidation](SOURCES.md) for upstream revisions, licenses,
and the mapping from old names.

## Install

Claude Code:

```bash
claude plugin marketplace add drkm-hq/vstack
claude plugin install vstack@vstack
```

Codex versions with plugin support:

```bash
codex plugin marketplace add drkm-hq/vstack
codex plugin add vstack@vstack
```

Restart Claude Code or start a new Codex task after installation. Remove or
disable the old `vishaal@vishaal-skills` plugin when switching to avoid duplicate
skill discovery. If you maintain copies in personal skill directories, compare
and migrate those intentionally; plugin installation does not reconcile them.

For hosts without plugin support, clone this repository and copy selected
folders from `plugins/vstack/skills/` into the host's documented skills
directory. Keep sibling skills that a workflow links to; installing the whole
plugin supplies those dependencies.

## Picking a workflow

- `create-pr` replaces tstack's `file-pr`; `babysit` replaces `babysit-pr`.
- `babysit` covers a one-time CI check, monitoring, or repairs through the
  requested endpoint. Status checks are read-only; do-not-merge takes priority.
- `full-send` explicitly carries a scoped change to merge. `full-stop` prepares
  it for your merge and never queues it. An ordinary request to stop means stop.
- `review-loop` handles independent review, an isolated Claude CLI review,
  or a requested council with three actual providers.
- `arena` compares candidates for the same problem; `swarm` divides the work.

Eight overlapping entry points have been folded into their owning workflows.
See the [old-to-current mapping](SOURCES.md#retired-entry-points) when migrating
personal instructions. Remove retired local copies to avoid duplicate discovery.

## Skills

### Understand and design

| Skill | Purpose |
| --- | --- |
| `recall` | Rebuild context from prior work and the current repository. |
| `trace-request-flow` | Explain code and subsystems, or trace a concrete request end to end. |
| `why` | Recover design rationale from history and evidence. |
| `architect` | Design caller usage, ownership, deep modules, and testable interfaces. |
| `grill-me` | Pressure-test a proposal with pointed questions. |
| `blast-radius` | Find consequences beyond the changed lines. |

### Implement and prove

| Skill | Purpose |
| --- | --- |
| `figure-it-out` | Build an evidenced workflow for an unfamiliar problem. |
| `debug-performance` | Diagnose defects, leaks, and slow paths with measurements. |
| `refactor` | Preserve behavior while restructuring code or removing unused compatibility paths. |
| `typescript-best-practices` | Model truthful types and validate external boundaries. |
| `tdd` | Develop behavior with red, green, and refactor cycles. |
| `meaningful-contribution` | Require observed evidence before declaring code ready. |
| `deslop` | Remove unnecessary generated code and comments. |
| `cli-creator` | Build composable, durable command-line tools. |
| `create-verification-skill` | Create, audit, and repair reusable real-app verification recipes. |

### Review and ship

| Skill | Purpose |
| --- | --- |
| `review-loop` | Run independent, isolated, or council reviews with a bounded loop. |
| `grab` | Read a PR's metadata, diff, and complete changed files. |
| `resolve-conflicts` | Resolve merge or rebase conflicts while preserving intent. |
| `modernize` | Reassess an aging PR before rebasing or reworking it. |
| `takeover` | Continue existing work while preserving contributor credit. |
| `create-pr` | Create or update a concise PR or dependency-ordered stack. |
| `yeet` | Format, verify, sign off, commit, and push the requested changes. |
| `babysit` | Check CI, diagnose failures, or shepherd a PR to the requested endpoint. |
| `full-send` | Finish an explicitly requested change through verified merge. |
| `full-stop` | Prepare a PR for the user to merge, leaving it open. |

### Coordinate and improve

| Skill | Purpose |
| --- | --- |
| `arena` | Compare independent candidates for the same task. |
| `swarm` | Coordinate agents across separate slices of work. |
| `show-me-your-work` | Keep a compact decision log linked to evidence. |
| `technical-writing` | Write accurate technical docs and procedures. |
| `unslop` | Remove filler and canned phrasing from prose. |
| `reflect` | Extract durable lessons and targeted workflow improvements. |
| `automate-me` | Capture explicit working preferences in a personal skill. |

## Requirements

GitHub workflows use an authenticated [GitHub CLI](https://cli.github.com)
or equivalent host tools. Independent review requires the requested model to
be available through the host or a configured CLI. Model aliases are not
portable; configure personal choices in `AGENTS.md`, `CLAUDE.md`, or the
review runner's environment.

The isolated review helper needs Bash, Git, and Claude CLI. It uses Claude's
configured model unless `--model` or `ADVERSARIAL_REVIEW_MODEL` is supplied.
It reviews committed changes only and refuses dirty worktrees. The decision
log helper needs Bash. Product-specific tools and live deployment credentials
are not bundled.

## Validate locally

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
claude plugin validate --strict .
claude plugin validate --strict plugins/vstack
```

The validator checks both marketplaces, skill metadata, inventory, and local
references. Integration tests run the shell helpers against disposable Git
repositories and a fake reviewer; they do not make paid model calls. CI runs
the Python validator, helper tests, and shell syntax checks. Provider access,
review quality, and live GitHub shipping still depend on the target environment.
