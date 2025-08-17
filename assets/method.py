#!/usr/bin/env python3
import requests
import argparse
import urllib3
import time
from colorama import Fore, Style, init

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)  # Auto reset colors after each print

def bypass_with_methods(url, delay):
    methods = [
        "GET", "POST", "HEAD", "OPTIONS", "PUT",
        "DELETE", "PATCH", "TRACE", "CONNECT",
        "PROPFIND", "COPY", "MOVE", "LOCK", "UNLOCK",
        "SEARCH", "MKCOL", "REPORT", "CHECKOUT"
    ]

    print(f"\n[*] Testing HTTP methods against: {url}\n")

    for method in methods:
        try:
            r = requests.request(method, url, verify=False, timeout=8)
            status = r.status_code
            length = len(r.text)

            # Color selection based on status code
            if 200 <= status < 300:
                color = Fore.GREEN
            elif 300 <= status < 400:
                color = Fore.YELLOW
            elif 400 <= status < 500:
                color = Fore.RED
            elif 500 <= status < 600:
                color = Fore.MAGENTA
            else:
                color = Fore.CYAN

            # Build message
            msg = f"{color}[{status}]{Style.RESET_ALL} {method} -> {url} (Length: {length})"

            # Highlight possible bypass
            if status == 200:
                msg += f"  {Fore.YELLOW}<< POSSIBLE BYPASS{Style.RESET_ALL}"

            print(msg)

        except Exception as e:
            print(f"{Fore.RED}[!] Error with {method}: {e}{Style.RESET_ALL}")

        # Apply delay (convert ms to seconds)
        if delay > 0:
            time.sleep(delay / 1000.0)

