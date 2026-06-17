#!/usr/bin/env python3
"""
fetch_transcripts.py — Residential-IP transcript fetcher for regime_trader.

Designed to run on a self-hosted machine (home/Raspberry Pi) where YouTube
does NOT block the IP. Reads a queue written by youtube_monitor.py (cloud),
fetches transcripts, writes them to memory/transcripts/, clears the queue.

Usage:
    python scripts/fetch_transcripts.py
    python scripts/fetch_transcripts.py --dry-run   # show queue, don't fetch

Queue file:  memory/transcript-queue.json
Output dir:  memory/transcripts/{video_id}.txt
"""

import argparse
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger("fetch_transcripts")

SCRIPT_DIR   = Path(__file__).resolve().parent
REPO_ROOT    = SCRIPT_DIR.parent
QUEUE_PATH   = REPO_ROOT / "memory" / "transcript-queue.json"
TRANSCRIPTS_DIR = REPO_ROOT / "memory" / "transcripts"
MAX_CHARS    = 8000

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    YT_AVAILABLE = True
except ImportError:
    log.error("youtube-transcript-api not installed — run: pip install youtube-transcript-api")
    YT_AVAILABLE = False


def load_queue() -> list[dict]:
    if not QUEUE_PATH.exists():
        log.info("Queue file not found — nothing to do")
        return []
    with open(QUEUE_PATH, encoding="utf-8") as fh:
        data = json.load(fh)
    items = data.get("pending", [])
    log.info("Queue has %d item(s)", len(items))
    return items


def save_queue(pending: list[dict]) -> None:
    data = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "pending": pending,
    }
    with open(QUEUE_PATH, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


def fetch_transcript(video_id: str, lang: str) -> tuple[str | None, bool]:
    if not YT_AVAILABLE:
        return None, False

    api = YouTubeTranscriptApi()
    prio = [["fr"], ["en"], ["fr-FR"], ["en-US"]] if lang.upper() == "FR" \
           else [["en"], ["fr"], ["en-US"], ["fr-FR"]]

    for langs in prio:
        try:
            segs = api.fetch(video_id, languages=langs)
            text = re.sub(r"\s+", " ", " ".join(s.text for s in segs)).strip()
            return text[:MAX_CHARS], True
        except Exception:
            continue

    # Fallback: try any available transcript
    try:
        for t in api.list(video_id):
            try:
                segs = t.fetch()
                text = re.sub(r"\s+", " ", " ".join(s.text for s in segs)).strip()
                return text[:MAX_CHARS], True
            except Exception:
                continue
    except Exception as exc:
        log.info("No transcript for %s: %s", video_id, exc)

    return None, False


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch YouTube transcripts from queue")
    parser.add_argument("--dry-run", action="store_true", help="Print queue without fetching")
    args = parser.parse_args()

    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

    pending = load_queue()
    if not pending:
        log.info("Nothing in queue — exiting")
        print(json.dumps({"status": "empty", "fetched": 0, "failed": 0}))
        return

    if args.dry_run:
        print(json.dumps({"status": "dry_run", "pending": pending}, indent=2))
        return

    still_pending = []
    fetched, failed = 0, 0

    for item in pending:
        video_id = item["video_id"]
        lang     = item.get("lang", "EN")
        out_path = TRANSCRIPTS_DIR / f"{video_id}.txt"

        # Skip if already fetched
        if out_path.exists():
            log.info("Already fetched: %s", video_id)
            fetched += 1
            continue

        log.info("Fetching %s (%s) …", video_id, item.get("title", "")[:60])
        text, ok = fetch_transcript(video_id, lang)

        if ok and text:
            out_path.write_text(text, encoding="utf-8")
            log.info("  Saved %d chars → %s", len(text), out_path.name)
            fetched += 1
        else:
            log.warning("  FAILED: %s — kept in queue for retry", video_id)
            still_pending.append(item)
            failed += 1

    save_queue(still_pending)

    result = {
        "status": "ok",
        "fetched": fetched,
        "failed": failed,
        "remaining_in_queue": len(still_pending),
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    print(json.dumps(result, indent=2))
    log.info("Done — fetched=%d failed=%d", fetched, failed)


if __name__ == "__main__":
    main()
