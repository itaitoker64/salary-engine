"""
Vercel serverless entrypoint.

Vercel's @vercel/python runtime serves the ASGI `app` exported here, and
`vercel.json` rewrites every path to this function so FastAPI answers for the
whole site — frontend at `/`, API under `/api/...`, docs at `/docs`.

Keep this file a plain re-export. Wrapping `app` in ASGI middleware **here does
not work**: a build carrying such a wrapper went live (proved by `/api/index`
serving the page, which only the new `main.py` does) while not one response
carried the headers the wrapper stamps — so the runtime does not call the
object this module exports. Anything that must run per-request belongs on the
FastAPI app itself, in `main.py`, where `_RestoreOriginalPath` now lives.
"""

import sys
from pathlib import Path

# Ensure the project root (where main.py and the data files live) is importable.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import app  # noqa: E402

# Expose the ASGI app for the Vercel Python runtime.
__all__ = ["app"]
