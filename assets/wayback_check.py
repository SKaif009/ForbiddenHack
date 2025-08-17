import requests
import argparse
from datetime import datetime

# ANSI color constants
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def check_wayback_url(target_url: str):
    """
    Check if a specific URL has historical snapshots in the Wayback Machine.
    """
    wayback_api = (
        f"http://web.archive.org/cdx/search/cdx?url={target_url}&output=json&fl=timestamp,original&collapse=digest"
    )

    try:
        r = requests.get(wayback_api, timeout=15)
        if r.status_code == 200:
            data = r.json()
            if len(data) > 1:  # first row is header
                snapshots = []
                for row in data[1:]:
                    timestamp, original = row
                    # Convert YYYYMMDDhhmmss → readable date
                    readable_time = datetime.strptime(timestamp, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S UTC")
                    snapshots.append({
                        "url": f"https://web.archive.org/web/{timestamp}/{original}",
                        "time": readable_time
                    })
                return snapshots
            else:
                return []
        else:
            print(f"[!] Wayback API returned {r.status_code}")
            return []
    except Exception as e:
        print(f"{RED}{BOLD}[!] Error fetching Wayback snapshots: {e}{RESET}")
        return []

