#!/usr/bin/env bash
# Stop hook — a session that added commits must leave docs/HANDOFF.md current.
#
# HANDOFF.md carries `<!-- head: <sha> -->`. The handoff counts as current when
# nothing OTHER than HANDOFF.md itself has changed since that sha — writing the
# handoff necessarily creates a commit the handoff cannot name, so an exact
# sha match would be unsatisfiable. Otherwise the turn is blocked once with an
# explanation.
#
# Fires at most ONCE per session (sentinel keyed by session_id) — a Stop hook
# that keeps blocking would trap the session in a loop.
set -uo pipefail

INPUT="$(cat 2>/dev/null || echo '{}')"
SESSION="$(printf '%s' "$INPUT" | python3 -c 'import json,sys
try: print(json.load(sys.stdin).get("session_id","nosession"))
except Exception: print("nosession")' 2>/dev/null || echo nosession)"

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" 2>/dev/null || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

SENTINEL="/tmp/claude-handoff-guard.${SESSION}"
[ -f "$SENTINEL" ] && exit 0            # already nudged this session

CUR="$(git rev-parse --short HEAD 2>/dev/null)" || exit 0

BASE_BRANCH="$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##')"
BASE_BRANCH="${BASE_BRANCH:-main}"
AHEAD=0
if git rev-parse --verify --quiet "origin/$BASE_BRANCH" >/dev/null 2>&1; then
  AHEAD="$(git rev-list --count "origin/$BASE_BRANCH"..HEAD 2>/dev/null || echo 0)"
fi

# Nothing committed beyond the base branch — a read-only or advisory session
# owes no handoff.
[ "${AHEAD:-0}" -eq 0 ] && exit 0

REC=""
[ -f docs/HANDOFF.md ] && \
  REC="$(sed -n 's/.*<!-- head: \([0-9a-f]\{7,\}\) -->.*/\1/p' docs/HANDOFF.md | head -1)"

# Current when no tracked file except the handoff itself has moved since REC.
if [ -n "$REC" ] && git rev-parse --verify --quiet "$REC^{commit}" >/dev/null 2>&1; then
  if git diff --quiet "$REC" HEAD -- . ':(exclude)docs/HANDOFF.md' 2>/dev/null; then
    exit 0
  fi
fi

touch "$SENTINEL"
if [ -z "$REC" ]; then
  REASON="docs/HANDOFF.md is missing or carries no head marker, and this branch has $AHEAD commit(s) beyond origin/$BASE_BRANCH. Write it (see CLAUDE.md → Handoff protocol) so the next Claude starts from the real state, then commit it."
else
  REASON="docs/HANDOFF.md still describes $REC but HEAD is $CUR ($AHEAD commit(s) beyond origin/$BASE_BRANCH). Update it — what changed, why, what is verified, what is open — bump the head marker to $CUR, and commit."
fi

python3 - "$REASON" <<'PY'
import json, sys
print(json.dumps({"decision": "block", "reason": sys.argv[1]}, ensure_ascii=False))
PY
exit 0
