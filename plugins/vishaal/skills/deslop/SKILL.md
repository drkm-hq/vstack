---
name: deslop
description: Remove AI-generated code slop from a branch. Use when cleaning up AI-generated code, removing unnecessary comments, defensive checks, try/catch blocks, casts, inline imports, or other style inconsistencies. Checks the diff against main and fixes style inconsistencies while preserving legitimate behavior.
---

# Remove AI Code Slop

Check the diff against main and remove AI-generated slop introduced in this branch.

## What To Remove

- Extra comments that a human would not add or that are inconsistent with the rest of the file
- Extra defensive checks or try/catch blocks that are abnormal for that area of the codebase, especially if called by trusted or validated code paths
- Casts to `any` that work around type issues instead of solving them
- Inline imports in Python; move them to the top of the file with other imports
- Any other style that is inconsistent with the file

## Process

1. Get the diff against main: `git diff main...HEAD`.
2. Review each changed file for slop patterns.
3. Remove identified slop while preserving legitimate changes.
4. Run focused formatting, linting, type checking, or tests when the edit risk justifies it.
5. Report a 1-3 sentence summary of what changed.
