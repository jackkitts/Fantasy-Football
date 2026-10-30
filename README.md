# LMEYP Fantasy — ESPN data sync

League **829453220**, season **2026**.

GitHub Actions fetches ESPN's unofficial Fantasy read API every day at **11:00 UTC** (7 AM Eastern in daylight saving time, 6 AM in standard time). You can manually run it under **Actions → Sync ESPN Fantasy → Run workflow**.

The `data/` directory stores raw JSON snapshots for ESPN views and `sync_status.json` reporting successes and failures. ESPN can change or restrict this unofficial API. A successful run depends on public league access.

**Privacy:** This repository is currently public. Do not add private ESPN cookies or credentials. If authentication becomes necessary, first make the repository private and use GitHub Actions secrets.

GitHub syncing does not automatically send data into ChatGPT; ask ChatGPT to inspect the repository when needed.
