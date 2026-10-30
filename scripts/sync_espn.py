#!/usr/bin/env python3
"""Fetch public ESPN Fantasy league snapshots without credentials."""
import datetime as dt
import json
import os
import pathlib
import urllib.error
import urllib.parse
import urllib.request

LEAGUE = "829453220"
YEAR = "2026"
BASE = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{YEAR}/segments/0/leagues/{LEAGUE}"
VIEWS = ["mTeam", "mRoster", "mMatchup", "mSettings", "mTransactions2"]
OUT = pathlib.Path("data")
OUT.mkdir(exist_ok=True)
now = dt.datetime.now(dt.timezone.utc).isoformat()
summary = {"league_id": LEAGUE, "season": int(YEAR), "fetched_at_utc": now, "views": {}, "errors": {}}
for view in VIEWS:
    url = BASE + "?" + urllib.parse.urlencode({"view": view})
    request = urllib.request.Request(url, headers={"User-Agent": "LMEYP-Fantasy-Sync/1.0", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=35) as response:
            data = json.load(response)
        if str(data.get("id")) != LEAGUE:
            raise ValueError("ESPN response did not match the expected league")
        (OUT / f"{view}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        summary["views"][view] = "ok"
    except (urllib.error.URLError, ValueError, json.JSONDecodeError, TimeoutError) as exc:
        summary["errors"][view] = str(exc)
(OUT / "sync_status.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2))
if not summary["views"]:
    raise SystemExit("No ESPN views could be retrieved. Check league public visibility.")
