"""
fetcher.py — Fetcher Agent (Module 2)

Downloads Zillow Home Value Index (ZHVI) data for all California zip codes
and saves the result to data/raw/. El Dorado Hills (95762) and Folsom (95630)
are highlighted in the output but all ~1,800 CA zip codes are included.

Usage:
    python src/agents/fetcher.py              # run once
    python src/agents/fetcher.py --schedule   # run on a schedule (every 24h)
"""

import csv
import io
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────────

# Filter to California; all ~1,800 zip codes are included.
TARGET_STATE = "CA"

# Zip codes we care most about — highlighted in the summary output.
HIGHLIGHT_ZIPS = {"95762", "95630"}  # El Dorado Hills, Folsom

# Zillow Research: ZHVI by zip code (single-family + condo, smoothed/seasonally adjusted)
# Free public data — no API key required.
DATA_URL = (
    "https://files.zillowstatic.com/research/public_csvs/zhvi/"
    "Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"


# ── Fetch ──────────────────────────────────────────────────────────────────────

def fetch():
    """Download Zillow ZHVI, filter to all California zip codes, save to data/raw/."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d")
    out_path = RAW_DIR / f"zhvi_california_{timestamp}.csv"

    print("[fetcher] Downloading Zillow ZHVI data (this may take a moment)...")
    print(f"[fetcher] Source: {DATA_URL}")

    with urllib.request.urlopen(DATA_URL) as response:
        text = response.read().decode("utf-8")

    reader = csv.DictReader(io.StringIO(text))
    fieldnames = reader.fieldnames

    rows = [
        row for row in reader
        if row.get("State", "") == TARGET_STATE
    ]

    if not rows:
        print(f"[fetcher] WARNING: No rows matched State={TARGET_STATE!r}.")
        return None

    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    last_col = fieldnames[-1]
    print(f"[fetcher] Done — saved {len(rows)} CA zip codes -> {out_path.relative_to(PROJECT_ROOT)}")
    print(f"[fetcher] Most recent month: {last_col}")

    # Show a summary for our highlight zip codes
    for row in rows:
        if row.get("RegionName") in HIGHLIGHT_ZIPS:
            val = row.get(last_col, "")
            try:
                price = f"${float(val):,.0f}"
            except (ValueError, TypeError):
                price = "n/a"
            city = row.get("City", "?")
            print(f"          * Zip {row['RegionName']} ({city}) · latest ZHVI: {price}")

    return out_path


# ── Schedule ───────────────────────────────────────────────────────────────────

def start_scheduler(interval_hours: int = 24):
    """
    Run the fetcher on a repeating schedule using APScheduler.
    Fetches once immediately on startup, then every `interval_hours` hours.
    """
    from apscheduler.schedulers.blocking import BlockingScheduler

    scheduler = BlockingScheduler()
    scheduler.add_job(fetch, "interval", hours=interval_hours)

    print(f"[fetcher] Scheduler active — fetching every {interval_hours}h.")
    print("[fetcher] Press Ctrl+C to stop.")

    try:
        fetch()           # run immediately so you don't wait for the first interval
        scheduler.start()
    except KeyboardInterrupt:
        print("\n[fetcher] Scheduler stopped.")


# ── Entry Point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if "--schedule" in sys.argv:
        start_scheduler()
    else:
        fetch()
