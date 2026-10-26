# vstack

Vishaal's engineering stack for Claude Code and Codex: 40 skills combining
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
- `check-ci` is a status/diagnosis task. `babysit` continues through the
  requested endpoint; monitor-only and do-not-merge instructions take priority.
- `full-send` explicitly carries a scoped change to merge. `full-stop` prepares
  it for your merge and never queues it. An ordinary request to stop means stop.
- `adversarial-review` uses a temporary clone and Claude CLI. `review-loop` uses
  your requested or configured independent reviewer. `council` requires three actual providers.
- `arena` compares candidates for the same problem; `swarm` divides the work.

## Skills

### Understand and design

| Skill | Purpose |
| --- | --- |
| `recall` | Rebuild context from prior work and the current repository. |
| `trace-request-flow` | Trace behavior through callers, services, storage, and integrations. |
| `why` | Recover design rationale from history and evidence. |
| `teach` | Explain a change or subsystem at the reader's level. |
| `architect` | Design real caller usage, ownership, types, and module boundaries. |
| `codebase-design` | Use deep modules and testable interfaces. |
| `grill-me` | Pressure-test a proposal with pointed questions. |
| `blast-radius` | Find consequences beyond the changed lines. |

### Implement and prove

| Skill | Purpose |
| --- | --- |
| `figure-it-out` | Build an evidenced workflow for an unfamiliar problem. |
| `debug-performance` | Diagnose defects, leaks, and slow paths with measurements. |
| `refactor` | Restructure code while preserving observable behavior. |
| `zero-tech-debt` | Remove unused compatibility paths and accumulated scaffolding. |
| `typescript-best-practices` | Model truthful types and validate external boundaries. |
| `tdd` | Develop behavior with red, green, and refactor cycles. |
| `meaningful-contribution` | Require observed evidence before declaring code ready. |
| `deslop` | Remove unnecessary generated code and comments. |
| `cli-creator` | Build composable, durable command-line tools. |
| `create-verification-skill` | Create a reusable real-app verification recipe. |
| `maintain-verification-skill` | Repair a verification recipe against current behavior. |

### Review and ship

| Skill | Purpose |
| --- | --- |
| `adversarial-review` | Review committed changes in a temporary clone with Claude CLI. |
| `review-loop` | Run a bounded review loop with your chosen independent reviewer. |
| `council` | Compare independent reviews from three model providers. |
| `grab` | Read a PR's metadata, diff, and complete changed files. |
| `check-ci` | Inspect current CI status and diagnose failures. |
| `resolve-conflicts` | Resolve merge or rebase conflicts while preserving intent. |
| `modernize` | Reassess an aging PR before rebasing or reworking it. |
| `takeover` | Continue existing work while preserving contributor credit. |
| `create-pr` | Create or update a concise PR or dependency-ordered stack. |
| `yeet` | Format, verify, sign off, commit, and push the requested changes. |
| `babysit` | Handle CI and reviews through the requested queue or merge endpoint. |
| `full-send` | Finish an explicitly requested change through verified merge. |
| `full-stop` | Prepare a PR for the user to merge, leaving it open. |
| `leaving-pr-comments` | Format authorized PR comments with verified attribution. |

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
