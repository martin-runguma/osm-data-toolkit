"""Persistent cache for raw Overpass API responses.

Responses are keyed by the SHA-256 hash of the exact Overpass query. This means
that changing the AOI or selected feature categories naturally creates a
separate cache entry. Cache files are JSON and are written atomically.
"""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional, Tuple

CACHE_MAX_AGE_DAYS = 30
CACHE_SCHEMA_VERSION = 1


def query_cache_path(query: str, cache_dir: str) -> str:
    """Return the deterministic cache-file path for an exact query string."""
    query_hash = hashlib.sha256(query.encode("utf-8")).hexdigest()
    return os.path.join(cache_dir, f"overpass_{query_hash}.json")


def load_cached_response(
    query: str,
    cache_dir: str,
    max_age_days: int = CACHE_MAX_AGE_DAYS,
) -> Tuple[Optional[Dict[str, Any]], str]:
    """Return a fresh cached response and a human-readable cache status."""
    path = query_cache_path(query, cache_dir)
    if not os.path.isfile(path):
        return None, "Cache miss: no saved response exists for this query."

    try:
        with open(path, "r", encoding="utf-8") as stream:
            payload = json.load(stream)

        if payload.get("schema_version") != CACHE_SCHEMA_VERSION:
            return None, "Cache miss: saved response uses an unsupported cache format."
        if payload.get("query_hash") != hashlib.sha256(query.encode("utf-8")).hexdigest():
            return None, "Cache miss: query hash does not match the saved response."

        cached_at = datetime.fromisoformat(payload["cached_at"])
        if cached_at.tzinfo is None:
            cached_at = cached_at.replace(tzinfo=timezone.utc)
        age = datetime.now(timezone.utc) - cached_at.astimezone(timezone.utc)
        if age > timedelta(days=max_age_days):
            return None, f"Cache miss: saved response is older than {max_age_days} days."

        response = payload.get("response")
        if not isinstance(response, dict) or not isinstance(response.get("elements"), list):
            return None, "Cache miss: saved response is incomplete or invalid."

        return response, f"Cache hit: using saved Overpass response ({age.days} day(s) old)."
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return None, f"Cache miss: could not read saved response ({exc})."


def save_cached_response(query: str, response: Dict[str, Any], cache_dir: str) -> str:
    """Save a valid Overpass response atomically and return its path."""
    if not isinstance(response, dict) or not isinstance(response.get("elements"), list):
        raise ValueError("Only validated Overpass responses can be cached.")

    os.makedirs(cache_dir, exist_ok=True)
    path = query_cache_path(query, cache_dir)
    payload = {
        "schema_version": CACHE_SCHEMA_VERSION,
        "query_hash": hashlib.sha256(query.encode("utf-8")).hexdigest(),
        "cached_at": datetime.now(timezone.utc).isoformat(),
        "response": response,
    }

    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=cache_dir,
            prefix=".overpass_cache_", suffix=".tmp", delete=False
        ) as stream:
            temporary_path = stream.name
            json.dump(payload, stream, ensure_ascii=False, separators=(",", ":"))
        os.replace(temporary_path, path)
    finally:
        if temporary_path and os.path.exists(temporary_path):
            try:
                os.remove(temporary_path)
            except OSError:
                pass

    return path
