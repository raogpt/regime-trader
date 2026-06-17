#!/usr/bin/env python3
"""
youtube_monitor.py — YouTube channel monitor for trading bots.

Usage:
    python scripts/youtube_monitor.py --mode check [--since YYYY-MM-DD] [--bot trading|regime]
    python scripts/youtube_monitor.py --mode update-timestamps

Reads memory/youtube-watchlist.md, fetches RSS feeds, extracts transcripts,
and outputs structured JSON for Claude to process.
"""

import argparse
import json
import logging
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Logging — goes to stderr so stdout stays clean JSON
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger("youtube_monitor")

# ---------------------------------------------------------------------------
# Optional imports — graceful degradation if not installed yet
# ---------------------------------------------------------------------------
try:
    import requests
except ImportError:
    log.error("requests not installed — run: pip install requests")
    requests = None  # type: ignore

try:
    import feedparser
except ImportError:
    log.error("feedparser not installed — run: pip install feedparser>=6.0")
    feedparser = None  # type: ignore

try:
    from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
except ImportError:
    log.error("youtube_transcript_api not installed — run: pip install youtube-transcript-api>=0.6")
    YouTubeTranscriptApi = None  # type: ignore
    NoTranscriptFound = Exception  # type: ignore
    TranscriptsDisabled = Exception  # type: ignore

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
RSS_TEMPLATE = "https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
TRANSCRIPT_MAX_CHARS = 8000
RSS_TIMEOUT_SECONDS = 10
DEFAULT_LOOKBACK_DAYS = 7

# ---------------------------------------------------------------------------
# Locate memory/youtube-watchlist.md relative to this script
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
WATCHLIST_PATH   = REPO_ROOT / "memory" / "youtube-watchlist.md"
QUEUE_PATH       = REPO_ROOT / "memory" / "transcript-queue.json"
TRANSCRIPTS_DIR  = REPO_ROOT / "memory" / "transcripts"


# ---------------------------------------------------------------------------
# Transcript queue helpers (for off-cloud fetching via fetch_transcripts.py)
# ---------------------------------------------------------------------------

def load_cached_transcript(video_id: str) -> Optional[str]:
    """Return locally cached transcript text if already fetched, else None."""
    path = TRANSCRIPTS_DIR / f"{video_id}.txt"
    if path.exists():
        text = path.read_text(encoding="utf-8").strip()
        return text if text else None
    return None


def update_transcript_queue(new_videos: list[dict]) -> None:
    """
    Append any video_ids without a cached transcript to the queue file.
    fetch_transcripts.py (run on a residential IP) drains this queue.
    """
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

    # Load existing queue
    existing: list[dict] = []
    if QUEUE_PATH.exists():
        try:
            existing = json.loads(QUEUE_PATH.read_text()).get("pending", [])
        except Exception:
            existing = []

    existing_ids = {item["video_id"] for item in existing}

    added = 0
    for v in new_videos:
        vid = v["video_id"]
        if vid not in existing_ids and not (TRANSCRIPTS_DIR / f"{vid}.txt").exists():
            existing.append({
                "video_id": vid,
                "channel": v["channel"],
                "title": v["title"],
                "lang": v["language"],
                "published": v["published"],
                "queued_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            })
            existing_ids.add(vid)
            added += 1

    QUEUE_PATH.write_text(
        json.dumps(
            {"updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
             "pending": existing},
            indent=2,
        ),
        encoding="utf-8",
    )
    log.info("Transcript queue: added %d item(s), total pending=%d", added, len(existing))


# ---------------------------------------------------------------------------
# Watchlist parsing
# ---------------------------------------------------------------------------

def parse_watchlist(path: Path) -> list[dict]:
    """
    Parse the markdown table in youtube-watchlist.md.

    Returns a list of dicts:
        {id, channel, url, channel_id, lang, categories, signal_score, last_checked}
    """
    if not path.exists():
        log.error("Watchlist not found: %s", path)
        return []

    channels = []
    in_table = False

    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()

            # Detect table header
            if line.startswith("| ID |") or line.startswith("|ID|"):
                in_table = True
                continue

            # Skip separator row
            if in_table and re.match(r"^\|[-| ]+\|$", line):
                continue

            # Parse data rows
            if in_table and line.startswith("|") and line.endswith("|"):
                parts = [p.strip() for p in line.split("|")[1:-1]]
                if len(parts) < 8:
                    continue
                channels.append(
                    {
                        "id": parts[0],
                        "channel": parts[1],
                        "url": parts[2],
                        "channel_id": parts[3],
                        "lang": parts[4],
                        "categories": parts[5],
                        "signal_score": parts[6],
                        "last_checked": parts[7],
                    }
                )
            elif in_table and not line.startswith("|"):
                # End of table
                in_table = False

    log.info("Parsed %d channels from watchlist", len(channels))
    return channels


def parse_last_checked(raw: str) -> Optional[datetime]:
    """Convert 'never' or 'YYYY-MM-DD' to a timezone-aware datetime (UTC)."""
    raw = raw.strip()
    if raw.lower() in ("never", "—", "-", ""):
        return None
    try:
        dt = datetime.strptime(raw, "%Y-%m-%d")
        return dt.replace(tzinfo=timezone.utc)
    except ValueError:
        log.warning("Could not parse last_checked date: %r", raw)
        return None


# ---------------------------------------------------------------------------
# RSS fetching
# ---------------------------------------------------------------------------

def fetch_rss(channel_id: str) -> list[dict]:
    """
    Fetch and parse the YouTube RSS feed for a channel.

    Returns a list of entry dicts: {video_id, title, published, url}
    """
    if feedparser is None or requests is None:
        log.error("feedparser or requests unavailable — cannot fetch RSS")
        return []

    url = RSS_TEMPLATE.format(channel_id=channel_id)
    log.info("Fetching RSS: %s", url)

    try:
        resp = requests.get(url, timeout=RSS_TIMEOUT_SECONDS)
        resp.raise_for_status()
    except Exception as exc:
        log.warning("RSS fetch failed for channel %s: %s", channel_id, exc)
        return []

    feed = feedparser.parse(resp.text)
    entries = []

    for entry in feed.entries:
        # Extract video ID from yt:videoId or from the link
        video_id = getattr(entry, "yt_videoid", None)
        if not video_id:
            link = getattr(entry, "link", "")
            m = re.search(r"v=([A-Za-z0-9_-]{11})", link)
            video_id = m.group(1) if m else None

        if not video_id:
            continue

        # Parse published date
        published_struct = getattr(entry, "published_parsed", None)
        if published_struct:
            published_dt = datetime(*published_struct[:6], tzinfo=timezone.utc)
        else:
            published_dt = None

        entries.append(
            {
                "video_id": video_id,
                "title": getattr(entry, "title", "Untitled"),
                "published": published_dt,
                "url": f"https://www.youtube.com/watch?v={video_id}",
            }
        )

    log.info("  -> %d entries found", len(entries))
    return entries


# ---------------------------------------------------------------------------
# Transcript fetching
# ---------------------------------------------------------------------------

def fetch_transcript(video_id: str, preferred_lang: str) -> tuple[Optional[str], bool]:
    """
    Try to fetch a transcript for a YouTube video.

    Priority: preferred_lang -> opposite_lang -> auto-generated.
    Returns (transcript_text, available).
    """
    if YouTubeTranscriptApi is None:
        return None, False

    lang_priority = []

    # Build priority list: preferred first, then opposite, then auto
    if preferred_lang.upper() == "FR":
        lang_priority = [["fr"], ["en"], ["fr-FR"], ["en-US"]]
    else:
        lang_priority = [["en"], ["fr"], ["en-US"], ["fr-FR"]]

    # New API (>=0.6): instantiate, use .fetch() with languages list
    api = YouTubeTranscriptApi()

    for langs in lang_priority:
        try:
            fetched = api.fetch(video_id, languages=langs)
            text = " ".join(seg.text for seg in fetched)
            text = re.sub(r"\s+", " ", text).strip()
            return text, True
        except Exception:
            continue

    # Last resort: list available transcripts and fetch first one
    try:
        transcript_list = api.list(video_id)
        for t in transcript_list:
            try:
                fetched = t.fetch()
                text = " ".join(seg.text for seg in fetched)
                text = re.sub(r"\s+", " ", text).strip()
                return text, True
            except Exception:
                continue
    except Exception as exc:
        log.info("  Transcript unavailable for %s: %s", video_id, exc)

    return None, False


# ---------------------------------------------------------------------------
# Mode: check
# ---------------------------------------------------------------------------

def mode_check(since_override: Optional[str], bot_context: str) -> None:
    """
    Main check mode: find new videos, fetch transcripts, output JSON to stdout.
    """
    channels = parse_watchlist(WATCHLIST_PATH)
    if not channels:
        output = {
            "check_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "bot_context": bot_context,
            "new_videos": [],
            "no_new_videos": [],
            "error": "Watchlist empty or not found",
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    # Determine global since override
    global_since: Optional[datetime] = None
    if since_override:
        try:
            global_since = datetime.strptime(since_override, "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )
        except ValueError:
            log.warning("Invalid --since date: %r — ignoring", since_override)

    new_videos = []
    no_new_videos = []

    for ch in channels:
        channel_name = ch["channel"]
        channel_id = ch["channel_id"]
        lang = ch["lang"]

        # Determine cutoff date
        if global_since:
            cutoff = global_since
        else:
            last_checked = parse_last_checked(ch["last_checked"])
            if last_checked is None:
                cutoff = datetime.now(timezone.utc) - timedelta(days=DEFAULT_LOOKBACK_DAYS)
                log.info("Channel '%s' never checked — looking back %d days", channel_name, DEFAULT_LOOKBACK_DAYS)
            else:
                cutoff = last_checked
                log.info("Channel '%s' last checked: %s", channel_name, last_checked.strftime("%Y-%m-%d"))

        entries = fetch_rss(channel_id)
        channel_new = []

        for entry in entries:
            pub = entry["published"]
            if pub is None:
                log.warning("  Skipping entry with no publish date: %s", entry["video_id"])
                continue

            if pub <= cutoff:
                continue

            log.info("  New video: [%s] %s", entry["video_id"], entry["title"])

            # 1. Check local cache (written by fetch_transcripts.py on residential IP)
            cached = load_cached_transcript(entry["video_id"])
            if cached:
                log.info("  Transcript loaded from cache: %s", entry["video_id"])
                transcript_excerpt = cached
                transcript_available = True
                transcript_source = "cache"
            else:
                # 2. Try live fetch (works on residential IP, fails on cloud — graceful)
                transcript_text, transcript_available = fetch_transcript(entry["video_id"], lang)
                if transcript_available:
                    transcript_excerpt = (
                        transcript_text[:TRANSCRIPT_MAX_CHARS]
                        if transcript_text and len(transcript_text) > TRANSCRIPT_MAX_CHARS
                        else transcript_text
                    )
                    transcript_source = "live"
                else:
                    log.info("  NO_TRANSCRIPT — queued for off-cloud fetch: %s", entry["video_id"])
                    transcript_excerpt = None
                    transcript_source = "queued"

            channel_new.append(
                {
                    "channel": channel_name,
                    "video_id": entry["video_id"],
                    "title": entry["title"],
                    "published": pub.strftime("%Y-%m-%d"),
                    "url": entry["url"],
                    "language": lang,
                    "transcript_excerpt": transcript_excerpt,
                    "transcript_available": transcript_available,
                    "transcript_source": transcript_source,
                }
            )

        if channel_new:
            new_videos.extend(channel_new)
            log.info("Channel '%s': %d new video(s)", channel_name, len(channel_new))
        else:
            no_new_videos.append(channel_name)
            log.info("Channel '%s': no new videos", channel_name)

    # Write any transcript-less videos to the queue for off-cloud fetching
    update_transcript_queue([v for v in new_videos if not v["transcript_available"]])

    output = {
        "check_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "bot_context": bot_context,
        "new_videos": new_videos,
        "no_new_videos": no_new_videos,
    }

    print(json.dumps(output, ensure_ascii=False, indent=2))
    log.info("Done. %d new video(s) across %d channel(s) with no updates.", len(new_videos), len(no_new_videos))


# ---------------------------------------------------------------------------
# Mode: update-timestamps
# ---------------------------------------------------------------------------

def mode_update_timestamps() -> None:
    """
    Update the Last Checked column in youtube-watchlist.md with today's date.
    """
    if not WATCHLIST_PATH.exists():
        log.error("Watchlist not found: %s", WATCHLIST_PATH)
        sys.exit(0)  # Non-blocking

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    with open(WATCHLIST_PATH, encoding="utf-8") as fh:
        content = fh.read()

    lines = content.split("\n")
    updated_lines = []
    in_table = False
    updated_count = 0

    for line in lines:
        stripped = line.strip()

        # Detect table header
        if stripped.startswith("| ID |") or stripped.startswith("|ID|"):
            in_table = True
            updated_lines.append(line)
            continue

        # Skip separator row
        if in_table and re.match(r"^\|[-| ]+\|$", stripped):
            updated_lines.append(line)
            continue

        # Update data rows in the table
        if in_table and stripped.startswith("|") and stripped.endswith("|"):
            parts = stripped.split("|")
            # Columns: '' | ID | Channel | URL | ChannelID | Lang | Categories | Score | LastChecked | ''
            # parts[0] is empty, parts[-1] is empty; last column is parts[-2]
            if len(parts) >= 10:
                # Replace the Last Checked column (last data column = parts[-2])
                original_last = parts[-2].strip()
                parts[-2] = f" {today} "
                new_line = "|".join(parts)
                updated_lines.append(new_line)
                updated_count += 1
                log.info("Updated last_checked: '%s' -> '%s'", original_last, today)
            else:
                updated_lines.append(line)
            continue

        # End of table
        if in_table and not stripped.startswith("|"):
            in_table = False

        updated_lines.append(line)

    new_content = "\n".join(updated_lines)

    # Also update the "Last updated" header line
    new_content = re.sub(
        r"(Last updated:\s*)\d{4}-\d{2}-\d{2}",
        rf"\g<1>{today}",
        new_content,
    )

    with open(WATCHLIST_PATH, "w", encoding="utf-8") as fh:
        fh.write(new_content)

    log.info("Timestamps updated for %d channel(s). Watchlist saved.", updated_count)
    print(json.dumps({"status": "ok", "updated": updated_count, "date": today}))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="YouTube channel monitor for trading bots."
    )
    parser.add_argument(
        "--mode",
        choices=["check", "update-timestamps"],
        required=True,
        help="check: find new videos | update-timestamps: mark all channels as checked today",
    )
    parser.add_argument(
        "--since",
        metavar="YYYY-MM-DD",
        default=None,
        help="Override cutoff date for --mode check (fetch videos published after this date)",
    )
    parser.add_argument(
        "--bot",
        choices=["trading", "regime"],
        default="trading",
        help="Bot context tag for the output JSON (default: trading)",
    )

    args = parser.parse_args()

    try:
        if args.mode == "check":
            mode_check(since_override=args.since, bot_context=args.bot)
        elif args.mode == "update-timestamps":
            mode_update_timestamps()
    except Exception as exc:
        # Never crash — log and exit 0
        log.error("Unhandled error: %s", exc, exc_info=True)
        error_output = {
            "check_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "bot_context": getattr(args, "bot", "unknown"),
            "new_videos": [],
            "no_new_videos": [],
            "error": str(exc),
        }
        print(json.dumps(error_output, ensure_ascii=False, indent=2))
        sys.exit(0)


if __name__ == "__main__":
    main()
