#!/usr/bin/env python3
"""
intel_monitor.py — Multi-source (YouTube + blog RSS) market intel monitor for trading bots.

Usage:
    python scripts/intel_monitor.py --mode check [--since YYYY-MM-DD] [--bot trading|regime]
    python scripts/intel_monitor.py --mode update-timestamps

Reads memory/intel-watchlist.md, fetches each source's RSS/Atom feed, and
outputs structured JSON for Claude to process.

YouTube entries yield title + publish date from RSS; transcript text is not
fetched live here because this environment's egress IP is caught by
YouTube/Google's bot-detection checkpoint (a redirect to
google.com/sorry/index, i.e. a CAPTCHA wall) before any page or caption
content loads. This is IP-reputation-based, not client-specific — curl,
requests, and headless-browser navigation all hit the same wall. Instead,
transcript-less YouTube items are checked against a local cache
(memory/transcripts/{video_id}.txt) and, if missing, queued to
memory/transcript-queue.json for fetch_transcripts.py to drain on a
residential IP (see .github/workflows/fetch-transcripts.yml, self-hosted).
Blog entries carry their RSS-provided content (full text or teaser,
depending on the publisher) directly, which is not affected by this block.
"""

import argparse
import json
import logging
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
log = logging.getLogger("intel_monitor")

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

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CONTENT_MAX_CHARS = 8000
FEED_TIMEOUT_SECONDS = 15
DEFAULT_LOOKBACK_DAYS = 7
HTML_TAG_RE = re.compile(r"<[^>]+>")

# Some publishers (e.g. CNBC) return 403 for the default python-requests
# user-agent string; a browser-like one is accepted by every source tested.
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    )
}

# Fallback formats for feeds whose date string feedparser can't auto-parse
# into published_parsed/updated_parsed (e.g. investing.com: "Jul 11, 2026 10:15 GMT").
FALLBACK_DATE_FORMATS = (
    "%b %d, %Y %H:%M GMT",
    "%a, %d %b %Y %H:%M:%S %Z",
    "%Y-%m-%dT%H:%M:%SZ",
)

# ---------------------------------------------------------------------------
# Locate memory/intel-watchlist.md relative to this script
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
WATCHLIST_PATH = REPO_ROOT / "memory" / "intel-watchlist.md"
QUEUE_PATH = REPO_ROOT / "memory" / "transcript-queue.json"
TRANSCRIPTS_DIR = REPO_ROOT / "memory" / "transcripts"


# ---------------------------------------------------------------------------
# Transcript cache/queue helpers (YouTube only — off-cloud fetch via
# fetch_transcripts.py, drained by the fetch-transcripts.yml self-hosted
# GitHub Actions workflow since this environment's IP is blocked)
# ---------------------------------------------------------------------------

def load_cached_transcript(video_id: str) -> Optional[str]:
    """Return locally cached transcript text if already fetched, else None."""
    path = TRANSCRIPTS_DIR / f"{video_id}.txt"
    if path.exists():
        text = path.read_text(encoding="utf-8").strip()
        return text if text else None
    return None


def update_transcript_queue(youtube_items: list[dict]) -> None:
    """Append any YouTube video_ids without a cached transcript to the queue."""
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

    existing: list[dict] = []
    if QUEUE_PATH.exists():
        try:
            existing = json.loads(QUEUE_PATH.read_text()).get("pending", [])
        except Exception:
            existing = []

    existing_ids = {item["video_id"] for item in existing}

    added = 0
    for item in youtube_items:
        vid = item["entry_id"]
        if vid not in existing_ids and not (TRANSCRIPTS_DIR / f"{vid}.txt").exists():
            existing.append({
                "video_id": vid,
                "channel": item["source"],
                "title": item["title"],
                "lang": item["language"],
                "published": item["published"],
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
    Parse the markdown table in intel-watchlist.md.

    Returns a list of dicts:
        {id, source, type, url, feed_url, lang, categories, signal_score, last_checked}
    """
    if not path.exists():
        log.error("Watchlist not found: %s", path)
        return []

    sources = []
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
                if len(parts) < 9:
                    continue
                sources.append(
                    {
                        "id": parts[0],
                        "source": parts[1],
                        "type": parts[2].lower(),
                        "url": parts[3],
                        "feed_url": parts[4],
                        "lang": parts[5],
                        "categories": parts[6],
                        "signal_score": parts[7],
                        "last_checked": parts[8],
                    }
                )
            elif in_table and not line.startswith("|"):
                # End of table
                in_table = False

    log.info("Parsed %d source(s) from watchlist", len(sources))
    return sources


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


def clean_html(raw: Optional[str]) -> Optional[str]:
    """Strip HTML tags and collapse whitespace."""
    if not raw:
        return None
    text = HTML_TAG_RE.sub(" ", raw)
    text = re.sub(r"\s+", " ", text).strip()
    return text or None


def parse_entry_date(entry) -> Optional[datetime]:
    """
    Resolve an entry's publish date, tolerating feeds feedparser can't
    auto-parse into published_parsed/updated_parsed (e.g. investing.com's
    "Jul 11, 2026 10:15 GMT" style).
    """
    struct = getattr(entry, "published_parsed", None) or getattr(entry, "updated_parsed", None)
    if struct:
        return datetime(*struct[:6], tzinfo=timezone.utc)

    raw = (getattr(entry, "published", None) or getattr(entry, "updated", None) or "").strip()
    if not raw:
        return None

    for fmt in FALLBACK_DATE_FORMATS:
        try:
            return datetime.strptime(raw, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue

    log.warning("Could not parse entry date: %r", raw)
    return None


# ---------------------------------------------------------------------------
# Feed fetching
# ---------------------------------------------------------------------------

def fetch_feed(feed_url: str) -> list[dict]:
    """
    Fetch and parse an RSS/Atom feed (YouTube or blog).

    Returns a list of entry dicts: {entry_id, title, published, url, content}
    """
    if feedparser is None or requests is None:
        log.error("feedparser or requests unavailable — cannot fetch feed")
        return []

    log.info("Fetching feed: %s", feed_url)

    try:
        resp = requests.get(feed_url, timeout=FEED_TIMEOUT_SECONDS, headers=REQUEST_HEADERS)
        resp.raise_for_status()
    except Exception as exc:
        log.warning("Feed fetch failed for %s: %s", feed_url, exc)
        return []

    feed = feedparser.parse(resp.text)
    entries = []

    for entry in feed.entries:
        link = getattr(entry, "link", "")

        # YouTube feeds carry yt:videoId; used as a stable entry id when present
        entry_id = getattr(entry, "yt_videoid", None) or getattr(entry, "id", None) or link
        if not entry_id:
            continue

        published_dt = parse_entry_date(entry)

        # Prefer full body (content:encoded) over summary/description teaser
        content_raw = None
        if getattr(entry, "content", None):
            content_raw = entry.content[0].get("value")
        if not content_raw:
            content_raw = getattr(entry, "summary", None) or getattr(entry, "description", None)

        entries.append(
            {
                "entry_id": entry_id,
                "title": getattr(entry, "title", "Untitled"),
                "published": published_dt,
                "url": link,
                "content": clean_html(content_raw),
            }
        )

    log.info("  -> %d entries found", len(entries))
    return entries


# ---------------------------------------------------------------------------
# Mode: check
# ---------------------------------------------------------------------------

def mode_check(since_override: Optional[str], bot_context: str) -> None:
    """
    Main check mode: find new items across all sources, output JSON to stdout.
    """
    sources = parse_watchlist(WATCHLIST_PATH)
    if not sources:
        output = {
            "check_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "bot_context": bot_context,
            "new_items": [],
            "no_new_items": [],
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

    new_items = []
    no_new_items = []

    for src in sources:
        source_name = src["source"]
        source_type = src["type"]
        feed_url = src["feed_url"]
        lang = src["lang"]

        # Determine cutoff date
        if global_since:
            cutoff = global_since
        else:
            last_checked = parse_last_checked(src["last_checked"])
            if last_checked is None:
                cutoff = datetime.now(timezone.utc) - timedelta(days=DEFAULT_LOOKBACK_DAYS)
                log.info("Source '%s' never checked — looking back %d days", source_name, DEFAULT_LOOKBACK_DAYS)
            else:
                cutoff = last_checked
                log.info("Source '%s' last checked: %s", source_name, last_checked.strftime("%Y-%m-%d"))

        entries = fetch_feed(feed_url)
        source_new = []

        for entry in entries:
            pub = entry["published"]
            if pub is None:
                log.warning("  Skipping entry with no publish date: %s", entry["entry_id"])
                continue

            if pub <= cutoff:
                continue

            log.info("  New item [%s]: %s", source_type, entry["title"])

            content = entry["content"]
            content_excerpt = (
                content[:CONTENT_MAX_CHARS] if content and len(content) > CONTENT_MAX_CHARS else content
            )

            # YouTube: RSS never carries transcript text. Check the local
            # cache (written by fetch_transcripts.py on a residential IP)
            # before falling back to title-only — see module docstring.
            if source_type == "youtube":
                cached = load_cached_transcript(entry["entry_id"])
                content_excerpt = cached

            source_new.append(
                {
                    "type": source_type,
                    "entry_id": entry["entry_id"],
                    "source": source_name,
                    "title": entry["title"],
                    "published": pub.strftime("%Y-%m-%d"),
                    "url": entry["url"],
                    "language": lang,
                    "content_excerpt": content_excerpt,
                    "content_available": content_excerpt is not None,
                }
            )

        if source_new:
            new_items.extend(source_new)
            log.info("Source '%s': %d new item(s)", source_name, len(source_new))
        else:
            no_new_items.append(source_name)
            log.info("Source '%s': no new items", source_name)

    # Queue any transcript-less YouTube items for off-cloud fetching
    update_transcript_queue(
        [it for it in new_items if it["type"] == "youtube" and not it["content_available"]]
    )

    output = {
        "check_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "bot_context": bot_context,
        "new_items": new_items,
        "no_new_items": no_new_items,
    }

    print(json.dumps(output, ensure_ascii=False, indent=2))
    log.info("Done. %d new item(s) across %d source(s) with no updates.", len(new_items), len(no_new_items))


# ---------------------------------------------------------------------------
# Mode: update-timestamps
# ---------------------------------------------------------------------------

def mode_update_timestamps() -> None:
    """
    Update the Last Checked column in intel-watchlist.md with today's date.
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
            # Columns: '' | ID | Source | Type | URL | FeedURL | Lang | Categories | Score | LastChecked | ''
            # parts[0] is empty, parts[-1] is empty; last column is parts[-2]
            if len(parts) >= 11:
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

    log.info("Timestamps updated for %d source(s). Watchlist saved.", updated_count)
    print(json.dumps({"status": "ok", "updated": updated_count, "date": today}))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Multi-source (YouTube + blog RSS) market intel monitor for trading bots."
    )
    parser.add_argument(
        "--mode",
        choices=["check", "update-timestamps"],
        required=True,
        help="check: find new items | update-timestamps: mark all sources as checked today",
    )
    parser.add_argument(
        "--since",
        metavar="YYYY-MM-DD",
        default=None,
        help="Override cutoff date for --mode check (fetch items published after this date)",
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
            "new_items": [],
            "no_new_items": [],
            "error": str(exc),
        }
        print(json.dumps(error_output, ensure_ascii=False, indent=2))
        sys.exit(0)


if __name__ == "__main__":
    main()
