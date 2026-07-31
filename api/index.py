"""
Vercel serverless entrypoint.

Vercel's @vercel/python runtime detects the ASGI `app` object exported here and
serves it. `vercel.json` rewrites every path to this function so FastAPI answers
for the whole site — frontend at `/`, API under `/api/...`, docs at `/docs`.

## Why the path has to be restored

A rewrite hands the function its **destination** path, not the path the browser
asked for. Every request therefore arrived as `/api/index.py`, no route ever
matched, and the catch-all answered *everything* with the frontend HTML — the
same 200 and the same body for `/`, `/api/info`, `/api/lookups` and even
`/nonexistent.js`. The site looked up while every API endpoint was dead, which
is what the "לא מחובר" badge was reporting: the page fetches `/api/lookups`,
gets HTML back, cannot parse it, and file checking never runs.

Two things were wrong. The rewrite pointed at `/api/index.py` — the file on
disk — rather than `/api/index`, the route Vercel actually publishes for this
function; a destination that names a file is taken literally, which is how the
function ended up being handed its own filename as the request path. And
nothing recovered the real path afterwards. Both are fixed: the destination is
now the route, and the rewrite carries the original path as a query marker so
the app does not have to trust any undocumented `x-vercel-*` header:

    { "source": "/(.*)", "destination": "/api/index?__path=/$1" }

`_RestoreOriginalPath` reads `__path`, puts it back into the ASGI scope, and
drops it from the query string so handlers never see it. If it is ever missing
the request passes through untouched — the catch-all then serves the frontend,
so the failure mode is the old behaviour rather than an error page.
"""

import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlencode

# Ensure the project root (where main.py and the data files live) is importable.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import app as _app  # noqa: E402

PATH_PARAM = "__path"

# Checked in order when the rewrite's query string does not survive. Vercel's
# forwarded-path header is not contractual, so nothing here is assumed to exist
# — a name that is absent simply doesn't match, and `x-req-header-names` on the
# response says what WAS available.
HEADER_SOURCES = (
    "x-vercel-original-path",
    "x-vercel-original-pathname",
    "x-original-uri",
    "x-forwarded-uri",
    "x-rewrite-url",
)


class _RestoreOriginalPath:
    """Put the browser's path back into the ASGI scope before routing.

    Touches only `path`, `raw_path` and `query_string`, and only when the
    rewrite supplied `__path`. Non-HTTP scopes (lifespan) pass straight through.
    """

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope.get("type") not in ("http", "websocket"):
            await self.app(scope, receive, send)
            return

        received = scope.get("path", "")
        headers = {k.decode("latin-1").lower(): v.decode("latin-1")
                   for k, v in (scope.get("headers") or [])}
        pairs = parse_qsl((scope.get("query_string") or b"").decode("latin-1"),
                          keep_blank_values=True)

        original = next((v for k, v in pairs if k == PATH_PARAM), None)
        source = PATH_PARAM
        if not original:
            # The rewrite's query string did not survive. Fall back to whichever
            # header the platform does forward the real path in; each is checked
            # by name so an absent one simply doesn't match.
            for name in HEADER_SOURCES:
                v = headers.get(name)
                if v and v.startswith("/") and v != received:
                    original, source = v.split("?", 1)[0], name
                    break

        if original:
            if not original.startswith("/"):
                original = "/" + original
            scope = dict(scope)
            scope["path"] = original
            scope["raw_path"] = original.encode("utf-8")
            scope["query_string"] = urlencode(
                [(k, v) for k, v in pairs if k != PATH_PARAM]).encode("latin-1")

        # Report what arrived on every response. Without this the only way to
        # learn why routing misfires in production is to guess and redeploy —
        # and while routing is broken no diagnostic ENDPOINT is reachable, so it
        # has to ride on the response itself. Names only, never header values:
        # those carry cookies and auth.
        async def _send(message):
            if message.get("type") == "http.response.start":
                message = dict(message)
                message["headers"] = list(message.get("headers") or []) + [
                    (b"x-path-received", received.encode("latin-1", "replace")),
                    (b"x-path-restored",
                     (f"{original} via {source}" if original else "none")
                     .encode("latin-1", "replace")),
                    (b"x-req-header-names",
                     ",".join(sorted(headers)).encode("latin-1", "replace")[:900]),
                ]
            await send(message)

        await self.app(scope, receive, _send)


# The ASGI app Vercel serves. `_app` stays importable for tests and local runs.
app = _RestoreOriginalPath(_app)

__all__ = ["app"]
