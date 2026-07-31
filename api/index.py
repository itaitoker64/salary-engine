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

Rather than depend on an undocumented `x-vercel-*` header, the rewrite carries
the original path itself:

    { "source": "/(.*)", "destination": "/api/index.py?__path=/$1" }

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

        pairs = parse_qsl((scope.get("query_string") or b"").decode("latin-1"),
                          keep_blank_values=True)
        original = next((v for k, v in pairs if k == PATH_PARAM), None)
        if original:
            if not original.startswith("/"):
                original = "/" + original
            scope = dict(scope)
            scope["path"] = original
            scope["raw_path"] = original.encode("utf-8")
            scope["query_string"] = urlencode(
                [(k, v) for k, v in pairs if k != PATH_PARAM]).encode("latin-1")

        await self.app(scope, receive, send)


# The ASGI app Vercel serves. `_app` stays importable for tests and local runs.
app = _RestoreOriginalPath(_app)

__all__ = ["app"]
