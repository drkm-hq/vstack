---
name: resolve-conflicts
description: Resolve git merge conflicts by analyzing branch intent, planning resolutions, and asking for approval before applying changes. Use when asked to merge main into a feature branch or fix conflicted files.
---

# Resolve Merge Conflicts

## Overview

Analyze branch intent, pull from the parent branch, document conflicts, and get user approval before resolving.

## Phase 1: Understand Current Branch Changes

```bash
git branch --show-current
git log --oneline -1 origin/main
git log --oneline main..HEAD
git diff --stat main...HEAD
git diff main...HEAD
git log --format="%s%n%b" main..HEAD
```

Summarize:
- Feature goal
- Key files
- Critical changes to preserve

## Phase 2: Pull and Identify Conflicts

```bash
git fetch origin main
git merge origin/main --no-commit
git diff --name-only --diff-filter=U
git diff --check
```

Categorize conflicts by type (schema, logic, imports, config, tests) and severity.

## Phase 3: Create Resolution Plan

For each conflict, prepare:

```markdown
### Conflict: `path/to/file.py`

**Conflict Type:** [Schema | Logic | Imports | Config | Tests]
**Severity:** [Trivial | Moderate | Complex]

**Our Changes (HEAD):**
- What we changed and why

**Their Changes (origin/main):**
- What changed in main and why

**Resolution Strategy:**
- [ ] Keep ours
- [ ] Keep theirs
- [ ] Merge both
- [ ] Rewrite

**Proposed Resolution:**
Description of how to resolve this specific conflict
```

Resolve in order: schema/migrations, models, services, routers, tests, config/imports.

## Phase 4: Execute Resolution (With User Approval)

Stop and ask the user to approve the plan before editing files. After approval:

1. Apply resolutions and `git add` each file.
2. Verify no conflicts remain.
3. Run tests and type checks.

```bash
git diff --check
uv run pytest -v -m "not integration" -x
uv run mypy
```

## Phase 5: Complete Merge

```bash
git commit -m "Merge origin/main into $(git branch --show-current)

Resolved conflicts:
- file1.py: [brief description]
- file2.py: [brief description]"
```

## Output Format

```markdown
## Branch Analysis

**Branch:** `feature-branch-name`
**Feature Goal:** Brief description of what this branch accomplishes
**Commits:** N commits ahead of main

### Key Changes to Preserve
| File | Change Type | Importance |
|------|-------------|------------|
| `app/services/foo.py` | New feature logic | Critical |
| `app/models/bar.py` | Schema addition | Critical |
| `tests/unit/test_foo.py` | New tests | Important |

---

## Conflict Resolution Plan

### 1. `path/to/conflicted_file.py`
- **Type:** Logic conflict
- **Their Change:** Added field X to model
- **Our Change:** Added method Y to model
- **Resolution:** Merge both - changes are independent

---

## Questions for User

1. In `service.py`, main added a new validation. Should we:
   - A) Keep their validation and adapt our code?
   - B) Replace with our approach?

---

## Ready to Proceed?

Please review the plan above and let me know:
- [ ] Proceed with all proposed resolutions
- [ ] Discuss specific conflicts before proceeding
```

## Notes

- Prioritize preserving the current branch's feature intent.
