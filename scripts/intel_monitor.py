#!/usr/bin/env python3
"""
intel_monitor.py — Multi-source (YouTube + blog RSS) market intel monitor for trading bots.

Usage:
    python scripts/intel_monitor.py --mode check [--since YYYY-MM-DD] [--bot trading|regime]
    python scripts/intel_monitor.py --mode update-timestamps

Reads memory/intel-watchlist.md, fetches each source's RSS/Atom feed, and
outputs structured JSON for Claude to process.

YouTube entries yield title + publish date from RSS; transcript text is
fetched live inline via youtube-transcript-api (see fetch_transcript_live()
below). Earlier versions of this script assumed the fetch was permanently
blocked by a YouTube/Google bot-detection checkpoint from this environment's
egress IP and only ever queued items for off-cloud fetch. Re-tested
2026-07-24: that's not quite right — a handful of fetches succeed, then the
IP gets burst-blocked for the rest of that run (not a permanent per-video or
per-IP wall). So live fetch is attempted first with a consecutive-failure
circuit breaker (MAX_CONSECUTIVE_TRANSCRIPT_FAILURES): once tripped, the
rest of the run's items go straight to memory/transcript-queue.json instead
of wasting requests against an already-blocked window. Each run also drains
a few of the oldest already-queued items (MAX_BACKLOG_DRAIN_PER_RUN), so the
backlog shrinks over successive scheduled runs on its own — no external
workflow/runner needs to ever execute for this to work, though
fetch_transcripts.py / .github/workflows/fetch-transcripts.yml remain
available as an extra fallback drain path.
Blog entries carry their RSS-provided content (full text or teaser,
depending on the publisher) directly.

This script also stamps each `check` run with a same-day VIX close (FRED's
VIXCLS series) and a per-item keyword-based relevance tier, so the
qualitative news read doesn't have to stand in for an actual volatility
number, and so bulk single-stock/product noise (Motley Fool, ETF Trends
niche-fund pieces, etc.) doesn't have to be manually re-triaged every run.
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
# Vendored sgmllib — `pip install sgmllib3k` (feedparser's HTML-fallback
# dependency) fails to build in this environment (distutils/setuptools
# incompatibility in its setup.py, unrelated to the module's actual pure-
# Python content). Vendoring sidesteps needing that package to build at all.
# See scripts/vendor/sgmllib.py for the full explanation.
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parent / "vendor"))

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
    from youtube_transcript_api import YouTubeTranscriptApi
    YT_TRANSCRIPT_AVAILABLE = True
except ImportError:
    YouTubeTranscriptApi = None  # type: ignore
    YT_TRANSCRIPT_AVAILABLE = False

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

# FRED's public CSV endpoint needs no API key. VIXCLS is the CBOE Volatility
# Index daily close. Used to give the regime-consensus read in downstream
# reports an actual number instead of relying purely on news-tone inference.
VIX_CSV_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS"
VIX_TIERS = (
    (15.0, "LOW"),
    (25.0, "MID"),
    (35.0, "HIGH"),
    (float("inf"), "EXTREME"),
)

# Keyword-based relevance scoring — not a replacement for reading the item,
# just a triage aid so the same single-stock/product noise (Motley Fool
# earnings previews, ETF Trends niche-fund launches, etc.) doesn't have to be
# manually re-screened out of every report. Case-insensitive substring match
# against title + content. Tune this list as false positives/negatives show up.
RELEVANCE_KEYWORDS = (
    "spy", "qqq", "iwm", "s&p 500", "s&p500", "nasdaq", "dow jones", "russell 2000",
    "fed ", "federal reserve", "fomc", "rate hike", "rate cut", "interest rate",
    "inflation", "cpi", "pce", "yield", "treasury", "dollar index",
    "oil", "brent", "wti", "crude", "gold", "vix", "volatility",
    "recession", "gdp", "tariff", "geopolitical", "war", "iran", "houthi",
    "rotation", "equal weight", "concentration", "breadth", "ai bubble",
    "ai spending", "credit spread", "jobs report", "unemployment", "payrolls",
    "bceao", "uemoa", "brvm", "cfa franc", "franc cfa", "west africa",
)


def score_relevance(title: str, content: Optional[str], source_type: str) -> dict:
    """Cheap keyword-hit count against RELEVANCE_KEYWORDS — a triage aid,
    not a substitute for reading the item. Returns {score, tier}."""
    haystack = f"{title} {content or ''}".lower()
    hits = sum(1 for kw in RELEVANCE_KEYWORDS if kw in haystack)
    if hits >= 2:
        tier = "high"
    elif hits == 1:
        tier = "medium"
    else:
        tier = "low"
    return {"score": hits, "tier": tier}


def fetch_vix_snapshot() -> Optional[dict]:
    """Fetch the latest VIX close (and prior close) from FRED's public CSV.
    Returns None on any failure — this is a nice-to-have annotation, not a
    hard dependency of the check run."""
    if requests is None:
        return None
    try:
        resp = requests.get(VIX_CSV_URL, timeout=FEED_TIMEOUT_SECONDS)
        resp.raise_for_status()
        rows = [
            line.split(",") for line in resp.text.strip().splitlines()[1:]
            if line and "," in line
        ]
        # VIXCLS has holes ('.') on non-trading days; walk back for real prints.
        clean = [(d, v) for d, v in rows if v.strip() not in ("", ".")]
        if not clean:
            return None
        latest_date, latest_val = clean[-1]
        prior_val = float(clean[-2][1]) if len(clean) >= 2 else None
        latest_val = float(latest_val)
        tier = next(label for ceiling, label in VIX_TIERS if latest_val < ceiling)
        return {
            "date": latest_date,
            "close": latest_val,
            "prior_close": prior_val,
            "change": round(latest_val - prior_val, 2) if prior_val is not None else None,
            "tier": tier,
            "source": "FRED VIXCLS",
        }
    except Exception as exc:
        log.warning("VIX snapshot fetch failed: %s", exc)
        return None

# ---------------------------------------------------------------------------
# Locate memory/intel-watchlist.md relative to this script
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
WATCHLIST_PATH = REPO_ROOT / "memory" / "intel-watchlist.md"
QUEUE_PATH = REPO_ROOT / "memory" / "transcript-queue.json"
TRANSCRIPTS_DIR = REPO_ROOT / "memory" / "transcripts"


# ---------------------------------------------------------------------------
# Transcript cache/live-fetch/queue helpers (YouTube only)
# ---------------------------------------------------------------------------

def load_cached_transcript(video_id: str) -> Optional[str]:
    """Return locally cached transcript text if already fetched, else None."""
    path = TRANSCRIPTS_DIR / f"{video_id}.txt"
    if path.exists():
        text = path.read_text(encoding="utf-8").strip()
        return text if text else None
    return None


# Empirically (2026-07-24), YouTube's IP-reputation block is not a hard
# permanent wall from this environment — a handful of fetches succeed, then
# subsequent requests in the same run start failing outright (a session/
# burst-triggered block, not per-video). Once MAX_CONSECUTIVE_TRANSCRIPT_FAILURES
# consecutive failures are seen, stop attempting live fetches for the rest of
# the run (straight to queue) rather than burning time re-tripping an already-
# tripped block. The next run gets a fresh attempt.
MAX_CONSECUTIVE_TRANSCRIPT_FAILURES = 3
# Each run also chips away at the pre-existing backlog (oldest first), so the
# queue self-drains over successive scheduled runs without depending on any
# external workflow/runner ever executing.
MAX_BACKLOG_DRAIN_PER_RUN = 5


def fetch_transcript_live(video_id: str, lang: str) -> Optional[str]:
    """Attempt a live transcript fetch. Returns text (truncated to
    CONTENT_MAX_CHARS) on success, None on any failure (private video, no
    captions, blocked IP, etc.) — callers should fall back to queueing."""
    if not YT_TRANSCRIPT_AVAILABLE:
        return None

    api = YouTubeTranscriptApi()
    prio = [["fr"], ["en"], ["fr-FR"], ["en-US"]] if lang.upper() == "FR" \
           else [["en"], ["fr"], ["en-US"], ["fr-FR"]]

    for langs in prio:
        try:
            segs = api.fetch(video_id, languages=langs)
            text = re.sub(r"\s+", " ", " ".join(s.text for s in segs)).strip()
            if text:
                return text[:CONTENT_MAX_CHARS]
        except Exception:
            continue

    try:
        for t in api.list(video_id):
            try:
                segs = t.fetch()
                text = re.sub(r"\s+", " ", " ".join(s.text for s in segs)).strip()
                if text:
                    return text[:CONTENT_MAX_CHARS]
            except Exception:
                continue
    except Exception as exc:
        # youtube-transcript-api's exception text is a multi-paragraph
        # troubleshooting essay — log only the exception class + first line.
        first_line = str(exc).strip().splitlines()[0] if str(exc).strip() else ""
        log.info("No transcript available for %s: %s: %s", video_id, type(exc).__name__, first_line)

    return None


def _queue_item(existing: list[dict], existing_ids: set, video_id: str, channel: str,
                 title: str, lang: str, published: str) -> bool:
    if video_id in existing_ids:
        return False
    existing.append({
        "video_id": video_id,
        "channel": channel,
        "title": title,
        "lang": lang,
        "published": published,
        "queued_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    })
    existing_ids.add(video_id)
    return True


def _save_queue(pending: list[dict]) -> None:
    QUEUE_PATH.write_text(
        json.dumps(
            {"updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
             "pending": pending},
            indent=2,
        ),
        encoding="utf-8",
    )


def update_transcript_queue(youtube_items: list[dict]) -> None:
    """For each new, uncached YouTube item: try a live transcript fetch and
    write it straight to the cache (mutating the item dict in place so the
    caller's `new_items` list picks up the content immediately). Stops
    attempting live fetches after MAX_CONSECUTIVE_TRANSCRIPT_FAILURES in a
    row (see comment above) — remaining items just get queued. Items where
    the live fetch fails (or was skipped due to the breaker) get queued to
    transcript-queue.json. Afterward, also drains up to
    MAX_BACKLOG_DRAIN_PER_RUN oldest items already sitting in that queue,
    so the backlog shrinks over successive runs even with zero external
    infra (fetch_transcripts.py / the GitHub Actions job remain a fallback,
    not a requirement)."""
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

    existing: list[dict] = []
    if QUEUE_PATH.exists():
        try:
            existing = json.loads(QUEUE_PATH.read_text()).get("pending", [])
        except Exception:
            existing = []

    existing_ids = {item["video_id"] for item in existing}

    fetched_live = 0
    added = 0
    consecutive_failures = 0
    breaker_tripped = False

    for item in youtube_items:
        vid = item["entry_id"]
        out_path = TRANSCRIPTS_DIR / f"{vid}.txt"
        if out_path.exists():
            continue

        text = None if breaker_tripped else fetch_transcript_live(vid, item["language"])
        if text:
            out_path.write_text(text, encoding="utf-8")
            item["content_excerpt"] = text
            item["content_available"] = True
            fetched_live += 1
            consecutive_failures = 0
            log.info("  Live-fetched transcript: %s (%d chars)", vid, len(text))
            continue

        if not breaker_tripped:
            consecutive_failures += 1
            if consecutive_failures >= MAX_CONSECUTIVE_TRANSCRIPT_FAILURES:
                breaker_tripped = True
                log.warning(
                    "  %d consecutive transcript-fetch failures — likely IP-blocked "
                    "for this run, queueing the rest without further attempts",
                    consecutive_failures,
                )

        if _queue_item(existing, existing_ids, vid, item["source"], item["title"],
                        item["language"], item["published"]):
            added += 1

    # Backlog drain: chip away at pre-existing queue entries, oldest first,
    # skipped entirely if this run already tripped the breaker above.
    drained = 0
    if not breaker_tripped and existing:
        by_queued_at = sorted(existing, key=lambda it: it.get("queued_at", ""))
        for backlog_item in by_queued_at[:MAX_BACKLOG_DRAIN_PER_RUN]:
            vid = backlog_item["video_id"]
            out_path = TRANSCRIPTS_DIR / f"{vid}.txt"
            if out_path.exists():
                existing = [it for it in existing if it["video_id"] != vid]
                existing_ids.discard(vid)
                continue

            text = fetch_transcript_live(vid, backlog_item.get("lang", "EN"))
            if text:
                out_path.write_text(text, encoding="utf-8")
                existing = [it for it in existing if it["video_id"] != vid]
                existing_ids.discard(vid)
                drained += 1
                consecutive_failures = 0
                log.info("  Backlog-drained transcript: %s (%d chars)", vid, len(text))
            else:
                consecutive_failures += 1
                if consecutive_failures >= MAX_CONSECUTIVE_TRANSCRIPT_FAILURES:
                    log.warning("  Breaker tripped during backlog drain — stopping")
                    break

    _save_queue(existing)
    log.info(
        "Transcripts: live-fetched=%d (new), backlog-drained=%d, queued=%d (new fallback), total pending=%d",
        fetched_live, drained, added, len(existing),
    )


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
            # cache first; update_transcript_queue() below will attempt a
            # live fetch for anything still missing before falling back to
            # queueing — see module docstring.
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

    # Live-fetch (with queue fallback) any transcript-less YouTube items.
    # Mutates the dicts already referenced in new_items in place.
    update_transcript_queue(
        [it for it in new_items if it["type"] == "youtube" and not it["content_available"]]
    )

    # Relevance tagging runs last so YouTube items score against their
    # freshly live-fetched transcript, not just the title.
    for it in new_items:
        it["relevance"] = score_relevance(it["title"], it["content_excerpt"], it["type"])

    vix = fetch_vix_snapshot()
    if vix:
        log.info("VIX snapshot: %s close=%.2f (%s) tier=%s", vix["date"], vix["close"], vix["source"], vix["tier"])

    output = {
        "check_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "bot_context": bot_context,
        "vix_snapshot": vix,
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
