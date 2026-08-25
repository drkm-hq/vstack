#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf '%s\n' "Usage: run_adversarial_review.sh [--model MODEL] [--base REF] [--prompt FILE] [--keep] [--dry-run]"
}

MODEL="${ADVERSARIAL_REVIEW_MODEL:-fable}"
BASE=""
EXTRA_PROMPT_FILE=""
KEEP=0
DRY_RUN=0
CLAUDE_BIN="${CLAUDE_BIN:-claude}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --model)
      MODEL="${2:?--model requires a value}"
      shift 2
      ;;
    --base)
      BASE="${2:?--base requires a value}"
      shift 2
      ;;
    --prompt)
      EXTRA_PROMPT_FILE="${2:?--prompt requires a value}"
      shift 2
      ;;
    --keep)
      KEEP=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if ! command -v git >/dev/null 2>&1; then
  printf 'git is required\n' >&2
  exit 1
fi
if [[ "$DRY_RUN" -eq 0 ]] && ! command -v "$CLAUDE_BIN" >/dev/null 2>&1; then
  printf '%s is required; set CLAUDE_BIN to override\n' "$CLAUDE_BIN" >&2
  exit 1
fi
if [[ -n "$EXTRA_PROMPT_FILE" && ! -f "$EXTRA_PROMPT_FILE" ]]; then
  printf 'Prompt file not found: %s\n' "$EXTRA_PROMPT_FILE" >&2
  exit 1
fi

SOURCE_ROOT="$(git rev-parse --show-toplevel)"
SOURCE_BRANCH="$(git -C "$SOURCE_ROOT" rev-parse --abbrev-ref HEAD)"
SOURCE_HEAD="$(git -C "$SOURCE_ROOT" rev-parse HEAD)"
SOURCE_STATUS="$(git -C "$SOURCE_ROOT" status --short)"

if [[ -z "$BASE" ]]; then
  if command -v gh >/dev/null 2>&1; then
    PR_BASE="$(gh pr view --repo "$(git -C "$SOURCE_ROOT" remote get-url origin 2>/dev/null || true)" --json baseRefName --jq .baseRefName 2>/dev/null || true)"
  else
    PR_BASE=""
  fi
  if [[ -n "${PR_BASE:-}" ]]; then
    BASE="origin/$PR_BASE"
  else
    BASE="origin/main"
  fi
fi

TMP_PARENT="${TMPDIR:-/tmp}"
TMP_DIR="$(mktemp -d "${TMP_PARENT%/}/adversarial-review.XXXXXX")"
CLONE_DIR="$TMP_DIR/repo"
PROMPT_FILE="$TMP_DIR/prompt.md"

cleanup() {
  if [[ "$KEEP" -eq 1 ]]; then
    printf 'Kept temporary clone: %s\n' "$CLONE_DIR" >&2
  else
    rm -rf "$TMP_DIR"
  fi
}
trap cleanup EXIT

git clone --quiet --no-hardlinks "$SOURCE_ROOT" "$CLONE_DIR"

if [[ "$SOURCE_BRANCH" != "HEAD" ]]; then
  git -C "$CLONE_DIR" checkout --quiet "$SOURCE_BRANCH"
else
  git -C "$CLONE_DIR" checkout --quiet "$SOURCE_HEAD"
fi

REMOTE_URL="$(git -C "$SOURCE_ROOT" remote get-url origin 2>/dev/null || true)"
if [[ -n "$REMOTE_URL" ]]; then
  git -C "$CLONE_DIR" remote set-url origin "$REMOTE_URL" >/dev/null 2>&1 || true
  git -C "$CLONE_DIR" fetch --quiet origin >/dev/null 2>&1 || true
fi

if ! git -C "$CLONE_DIR" rev-parse --verify "$BASE" >/dev/null 2>&1; then
  printf 'Base ref not found in temp clone: %s\n' "$BASE" >&2
  printf 'Try passing --base <ref>.\n' >&2
  exit 1
fi

MERGE_BASE="$(git -C "$CLONE_DIR" merge-base HEAD "$BASE" 2>/dev/null || true)"
if [[ -n "$MERGE_BASE" ]]; then
  DIFF_RANGE="$MERGE_BASE...HEAD"
else
  DIFF_RANGE="$BASE...HEAD"
fi

{
  printf '# Adversarial Code Review\n\n'
  printf 'You are an adversarial senior code reviewer. Review this branch against `%s`.\n\n' "$BASE"
  printf 'Do not edit files. Do not create commits. Use the repository in the current working directory only.\n\n'
  printf 'Prioritize bugs, security issues, data loss, authorization flaws, race conditions, migration/deployment risks, API contract regressions, and missing tests. Ignore pure style unless it hides a bug.\n\n'
  printf 'Output format:\n'
  printf '1. Findings first, ordered by severity.\n'
  printf '2. Each finding must include severity, file/line, concrete failure mode, and suggested fix.\n'
  printf '3. Then list open questions or assumptions.\n'
  printf '4. If there are no material issues, say that clearly and list residual risks/test gaps.\n\n'
  printf 'Repository metadata:\n'
  printf -- '- Source root: `%s`\n' "$SOURCE_ROOT"
  printf -- '- Temp clone: `%s`\n' "$CLONE_DIR"
  printf -- '- Branch: `%s`\n' "$SOURCE_BRANCH"
  printf -- '- Head: `%s`\n' "$SOURCE_HEAD"
  printf -- '- Base: `%s`\n' "$BASE"
  printf -- '- Diff range: `%s`\n\n' "$DIFF_RANGE"
  if [[ -n "$SOURCE_STATUS" ]]; then
    printf 'Important: the source working tree had uncommitted changes. The temp clone contains committed git state only:\n\n'
    printf '```text\n%s\n```\n\n' "$SOURCE_STATUS"
  fi
  printf 'Start by inspecting:\n\n'
  printf '```bash\n'
  printf 'git status --short\n'
  printf 'git diff --stat %s\n' "$DIFF_RANGE"
  printf 'git diff %s\n' "$DIFF_RANGE"
  printf '```\n'
} > "$PROMPT_FILE"

if [[ -n "$EXTRA_PROMPT_FILE" ]]; then
  {
    printf '\n\n# Additional User Instructions\n\n'
    cat "$EXTRA_PROMPT_FILE"
    printf '\n'
  } >> "$PROMPT_FILE"
fi

printf 'Temp clone: %s\n' "$CLONE_DIR" >&2
printf 'Model: %s\n' "$MODEL" >&2
printf 'Base: %s\n' "$BASE" >&2
printf 'Diff range: %s\n' "$DIFF_RANGE" >&2

if [[ "$DRY_RUN" -eq 1 ]]; then
  printf 'Dry run only. Would execute:\n' >&2
  printf '  cd %q && %q -p --model %q < %q\n' "$CLONE_DIR" "$CLAUDE_BIN" "$MODEL" "$PROMPT_FILE" >&2
  exit 0
fi

cd "$CLONE_DIR"
exec "$CLAUDE_BIN" -p --model "$MODEL" < "$PROMPT_FILE"
