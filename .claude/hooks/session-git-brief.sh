#!/usr/bin/env bash
# SessionStart hook — hand the session a git delta brief before it reads a file.
#
# Why a hook and not "Claude, check git first": the harness runs this, so the
# orientation costs a few hundred tokens of injected text instead of a dozen
# exploratory tool calls. Everything here is read-only and deterministic.
#
# Emits JSON with hookSpecificOutput.additionalContext (see `claude` hook docs).
set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" 2>/dev/null || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

BASE_BRANCH="$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##')"
BASE_BRANCH="${BASE_BRANCH:-main}"

# Best-effort refresh; a sandbox without network must not stall the session.
timeout 20 git fetch --quiet origin "$BASE_BRANCH" >/dev/null 2>&1

BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)"
HEAD_LINE="$(git log --oneline -1 2>/dev/null)"
REMOTE="origin/$BASE_BRANCH"

{
  echo "=== git brief (SessionStart hook — already fetched, no need to re-run) ==="
  echo "branch: $BRANCH"
  echo "HEAD:   $HEAD_LINE"

  if git rev-parse --verify --quiet "$REMOTE" >/dev/null 2>&1; then
    if git merge-base --is-ancestor HEAD "$REMOTE" 2>/dev/null; then
      echo "merged into $BASE_BRANCH: YES — this branch adds nothing new"
    else
      AHEAD="$(git rev-list --count "$REMOTE"..HEAD 2>/dev/null || echo 0)"
      echo "merged into $BASE_BRANCH: NO — $AHEAD unmerged commit(s) here"
    fi

    BEHIND="$(git rev-list --count HEAD.."$REMOTE" 2>/dev/null || echo 0)"
    if [ "${BEHIND:-0}" -gt 0 ]; then
      echo
      echo "$BASE_BRANCH moved ahead by $BEHIND commit(s) not in this branch:"
      git log --oneline --no-merges -20 HEAD.."$REMOTE" 2>/dev/null | sed 's/^/  /'
      echo
      echo "files $BASE_BRANCH changed that this branch also touched (conflict risk):"
      MB="$(git merge-base HEAD "$REMOTE" 2>/dev/null)"
      comm -12 \
        <(git diff --name-only "$MB" "$REMOTE" 2>/dev/null | sort) \
        <(git diff --name-only "$MB" HEAD 2>/dev/null | sort) \
        | sed 's/^/  /' | head -20
    else
      echo "$BASE_BRANCH has nothing new for this branch"
    fi
  fi

  DIRTY="$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')"
  if [ "${DIRTY:-0}" -gt 0 ]; then
    echo
    echo "working tree: $DIRTY uncommitted path(s)"
    git status --short 2>/dev/null | head -15 | sed 's/^/  /'
  else
    echo "working tree: clean"
  fi

  if [ -f docs/HANDOFF.md ]; then
    REC="$(sed -n 's/.*<!-- head: \([0-9a-f]\{7,\}\) -->.*/\1/p' docs/HANDOFF.md | head -1)"
    CUR="$(git rev-parse --short HEAD 2>/dev/null)"
    echo
    if [ -z "$REC" ]; then
      echo "--- docs/HANDOFF.md (no head marker — treat as unverified) ---"
    elif ! git merge-base --is-ancestor "$REC" HEAD 2>/dev/null; then
      echo "--- docs/HANDOFF.md (WARNING: written at $REC, not an ancestor of $CUR) ---"
    elif git diff --quiet "$REC" HEAD -- . ':(exclude)docs/HANDOFF.md' 2>/dev/null; then
      echo "--- docs/HANDOFF.md (current) ---"
    else
      echo "--- docs/HANDOFF.md (STALE: code moved since $REC; HEAD is $CUR) ---"
    fi
    head -60 docs/HANDOFF.md
  else
    echo
    echo "docs/HANDOFF.md: missing — create it before ending a session that commits."
  fi
  echo "=== end git brief ==="
} > /tmp/claude-git-brief.$$ 2>/dev/null

python3 - "/tmp/claude-git-brief.$$" <<'PY' 2>/dev/null || cat "/tmp/claude-git-brief.$$"
import json, sys
with open(sys.argv[1], encoding="utf-8", errors="replace") as fh:
    body = fh.read()
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": body,
    }
}, ensure_ascii=False))
PY

rm -f "/tmp/claude-git-brief.$$"
exit 0
