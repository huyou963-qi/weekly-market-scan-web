#!/usr/bin/env python3
"""POST a weekly report payload to hblook.com."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("payload", type=Path, help="Path to payload JSON")
    p.add_argument(
        "--url",
        default=os.environ.get("WEEKLY_REPORT_API_URL", "https://hblook.com"),
    )
    args = p.parse_args()
    token = os.environ.get("WEEKLY_REPORT_INGEST_TOKEN", "").strip()
    if not token:
        print("Error: WEEKLY_REPORT_INGEST_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    payload = json.loads(args.payload.read_text(encoding="utf-8"))
    we = payload.get("meta", {}).get("weekEnding")
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        f"{args.url.rstrip('/')}/api/weekly-reports",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read().decode()
            print(f"OK {resp.status} weekEnding={we} {body[:300]}")
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"FAIL {e.code} weekEnding={we} {err}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
