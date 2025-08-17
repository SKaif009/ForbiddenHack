#!/usr/bin/env python3

# -----------------------------------------------
# main.py is main file for running ForbiddenHack v1.0
# -----------------------------------------------
from assets import header, method, path, wayback_check
import argparse
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)




def banner():
    banners = [
        r"""
  █████▒▒█████   ██▀███   ▄▄▄▄    ██▓▓█████▄ ▓█████▄ ▓█████  ███▄    █  ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀
▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▓█████▄ ▓██▒▒██▀ ██▌▒██▀ ██▌▓█   ▀  ██ ▀█   █ ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒
▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒██▒ ▄██▒██▒░██   █▌░██   █▌▒███   ▓██  ▀█ ██▒▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░
░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒██░█▀  ░██░░▓█▄   ▌░▓█▄   ▌▒▓█  ▄ ▓██▒  ▐▌██▒░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄
░▒█░   ░ ████▓▒░░██▓ ▒██▒░▓█  ▀█▓░██░░▒████▓ ░▒████▓ ░▒████▒▒██░   ▓██░░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
 ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▒▓███▀▒░▓   ▒▒▓  ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ▒ ▒  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ░       ░ ▒ ▒░   ░▒ ░ ▒░▒░▒   ░  ▒ ░ ░ ▒  ▒  ░ ▒  ▒  ░ ░  ░░ ░░   ░ ▒░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
 ░ ░   ░ ░ ░ ▒    ░░   ░  ░    ░  ▒ ░ ░ ░  ░  ░ ░  ░    ░      ░   ░ ░  ░  ░░ ░  ░   ▒   ░        ░ ░░ ░
           ░ ░     ░      ░       ░     ░       ░       ░  ░         ░  ░  ░  ░      ░  ░░ ░      ░  ░
                               ░      ░       ░                                          ░
""",
        r"""
    ______              __     _      __     __              __  __              __
   / ____/____   _____ / /_   (_)____/ /____/ /___   ____   / / / /____ _ _____ / /__
  / /_   / __ \ / ___// __ \ / // __  // __  // _ \ / __ \ / /_/ // __ `// ___// //_/
 / __/  / /_/ // /   / /_/ // // /_/ // /_/ //  __// / / // __  // /_/ // /__ / ,<
/_/     \____//_/   /_.___//_/ \__,_/ \__,_/ \___//_/ /_//_/ /_/ \__,_/ \___//_/|_|
""",
        r"""
___________            ___.    .__     .___   .___                 ___ ___                   __
\_   _____/____ _______\_ |__  |__|  __| _/ __| _/ ____    ____   /   |   \ _____     ____  |  | __
 |    __) /  _ \\_  __ \| __ \ |  | / __ | / __ |_/ __ \  /    \ /    ~    \\__  \  _/ ___\ |  |/ /
 |     \ (  <_> )|  | \/| \_\ \|  |/ /_/ |/ /_/ |\  ___/ |   |  \\    Y    / / __ \_\  \___ |    <
 \___  /  \____/ |__|   |___  /|__|\____ |\____ | \___  >|___|  / \___|_  / (____  / \___  >|__|_ \
     \/                     \/          \/     \/     \/      \/        \/       \/      \/      \/
"""
    ]

    chosen_banner = random.choice(banners)
    print(Fore.RED + chosen_banner)
    print(Fore.CYAN + Style.BRIGHT + "           [ 🚀 ForbiddenHack – Made By BlackForgeX 🚀 ]\n")


# ==========================
# ANSI color constants
# ==========================
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# ==========================
# MAIN FUNCTION
# ==========================
def main():
    banner()
    parser = argparse.ArgumentParser(
        description="Advanced 403 Bypass & Recon Tool (Headers, Methods, Path Obfuscation, Wayback)"
    )
    parser.add_argument(
        "-u", "--url", required=True, help="Target URL (e.g. http://127.0.0.1:8080/secret)"
    )
    parser.add_argument(
        "-d", "--delay", type=float, default=0.2, help="Delay between requests in seconds (default: 0.2)"
    )
    parser.add_argument(
        "-t", "--timeout", type=float, default=8.0, help="Timeout for requests in seconds (default: 8.0)"
    )
    args = parser.parse_args()

    url = args.url
    delay = args.delay
    timeout = args.timeout

    print(f"{CYAN}{BOLD}[*] Processing target: {url}{RESET}\n")

    # --------------------------
    # 1. Header-based bypass
    # --------------------------
    print(f"{CYAN}{BOLD}[*] Testing headers...{RESET}")
    header.bypass_with_headers(url)

    # --------------------------
    # 2. Method-based bypass
    # --------------------------
    print(f"\n{CYAN}{BOLD}[*] Testing HTTP methods...{RESET}")
    method.bypass_with_methods(url, delay * 1000)  # convert to ms

    # --------------------------
    # 3. Path obfuscation bypass
    # --------------------------
    print(f"\n{CYAN}{BOLD}[*] Testing path obfuscation...{RESET}")
    path.run(url, delay, timeout)

    # --------------------------
    # 4. Wayback snapshots
    # --------------------------
    print(f"\n{CYAN}{BOLD}[*] Checking Historical snapshots...{RESET}")
    snapshots = wayback_check.check_wayback_url(url)
    if snapshots:
        print(f"{CYAN}{BOLD}[+] Found {len(snapshots)} snapshots for {url}:{RESET}")
        for snap in snapshots:
            print(f"   {GREEN}{snap['time']}{RESET}  ->  {snap['url']}")
    else:
        print(f"{YELLOW}[-] No snapshots found for {url}{RESET}")

    print("\n" + "="*80 + "\n")
    time.sleep(delay)

if __name__ == "__main__":
    main()

