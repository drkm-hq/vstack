# Sources and consolidation

vstack preserves the history of [Vishaal's skills](https://github.com/vishytheswishy/skills)
at `a1fc612207e698d659a9aea7e15236a9e6a4f28d`. It incorporates the personal
adaptations installed on 2026-10-27, including the later pstack references,
`create-pr`, `babysit`, `codebase-design`, and `zero-tech-debt`.

This is a maintained selection, not a mirror. Machine-specific operations,
private fleet configuration, bundled product skills, and externally managed
CLI plugins are not distributed here.

## pstack

Source: [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack),
revision `640ea3abfbdef74aad432b58d8586e4bf645f42d`.
Related guidance is consolidated into existing personal skills:

| Upstream material | vstack home |
| --- | --- |
| `how` | `trace-request-flow` |
| `interrogate` | `review-loop` review lenses |
| `no-comments` | `deslop` comment review |
| `tdd` and behavior-testing principles | `tdd` regression evidence |
| proof and artifact principles | `meaningful-contribution` |
| babysit and shipping playbooks | `create-pr`, `babysit`, `yeet` |
| performance and forensics playbooks | `debug-performance`, `figure-it-out` |
| refactoring playbook | `refactor` |
| design and type principles | `architect`, `typescript-best-practices` |

The Cursor-specific sticky mode, bot infrastructure, and many standalone
principle triggers are omitted. Their useful guidance lives with the workflow
that consumes it instead of creating overlapping entry points.

## tstack

Source: [t3dotgg/tstack](https://github.com/t3dotgg/tstack/tree/7de017b3fc9d50c03cf3ecb98fb71e0ca65a78bd),
revision `7de017b3fc9d50c03cf3ecb98fb71e0ca65a78bd`.
| Upstream skill | vstack home |
| --- | --- |
| `file-pr` | `create-pr`: concise problem-first descriptions, attribution, REST fallback |
| `babysit-pr` | `babysit`: one watcher, rate limits, scoped fixes, current-head gates |
| `full-send` | `full-send`, calling the consolidated shipping skills |
| `full-stop` | `full-stop`, with an explicit no-merge endpoint |
| `council` | `review-loop` council reference, bounded rounds and honest provider availability |
| `sol-loop` | `review-loop`, model-agnostic bounded review with evidence-based severity |
| `takeover` | `takeover`, preserving authorship and the requested endpoint |
| `modernize` | `modernize`, delegating mechanical conflicts to `resolve-conflicts` |
| `leaving-pr-comments` | Shared comment guidance in `create-pr/references/pr-comments.md` |

The upstream `pr-wait` script is not bundled: it encodes specific review bots
and platform assumptions. vstack uses host-native monitoring or GitHub CLI
check watching, with separate paginated review inspection and a fresh merge
gate. No named bot is unconditionally exempted from repository requirements.
Review-only requests do not authorize fixes or publishing. Full-stop never
inherits babysit's merge-queue permission.

## Other retained sources

The locally installed `codebase-design` derives from
[Matt Pocock's skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design);
its useful design guidance now lives in `architect/references/deep-modules.md`,
with the MIT notice retained as `architect/MATT-POCOCK-LICENSE.txt`. The design
comparison workflow routes to `arena` instead of duplicating delegation rules.
The material is adapted from the local snapshot, not represented as an exact
copy of today's upstream revision.

Original Apache notices in `cli-creator` and `yeet` remain intact, as does
`architect/MATT-POCOCK-LICENSE.txt`. The collection itself is MIT; see the
repository root `LICENSE`.

## Retired entry points

The collection now exposes 32 skills. These eight entry points were removed;
use the owning skill or reference instead. No alias skills remain to compete
for discovery.

| Previous entry point | Current home |
| --- | --- |
| `adversarial-review` | [review-loop](plugins/vstack/skills/review-loop/SKILL.md), including its isolated clone helper |
| `council` | [review-loop council mode](plugins/vstack/skills/review-loop/references/council.md) |
| `codebase-design` | [architect deep-module guidance](plugins/vstack/skills/architect/references/deep-modules.md) |
| `teach` | [trace-request-flow](plugins/vstack/skills/trace-request-flow/SKILL.md) and its subsystem explanation guidance |
| `zero-tech-debt` | [refactor](plugins/vstack/skills/refactor/SKILL.md), including cleanup of an accreted patch |
| `check-ci` | [babysit CI status mode](plugins/vstack/skills/babysit/references/ci-status.md), read-only by default |
| `maintain-verification-skill` | [create-verification-skill maintenance](plugins/vstack/skills/create-verification-skill/references/maintenance.md) |
| `leaving-pr-comments` | [shared PR comment guidance](plugins/vstack/skills/create-pr/references/pr-comments.md) |

The isolated-review helper and its environment options remain available under
`review-loop/scripts/`; helper tests and CI use that location. Comment-formatting
guidance never grants permission to post, and a CI status request never grants
permission to repair, queue, or merge.

## Maintenance

Keep one canonical workflow for each job. Update callers when renaming a
skill. Record imported upstream revisions in this file. Run the validator and
helper integration tests before publishing.
Model selections belong in user or repository configuration; named models
must be available, and missing reviewers are never reported as approval.
