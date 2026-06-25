"""
api_tester.py - API Health Checker for public-apis

Tests a sample of APIs from README.md and reports their status.
Usage: python scripts/validate/api_tester.py
       python scripts/validate/api_tester.py --category Weather
       python scripts/validate/api_tester.py --all
"""

import argparse
import re
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: 'requests' library not found. Run: pip install requests")
    sys.exit(1)

# ── ANSI renk kodları ──────────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

def parse_readme(readme_path: str, category_filter: str = None) -> list[dict]:
    """README.md dosyasından API isimlerini ve linklerini çeker."""
    path = Path(readme_path)
    if not path.exists():
        print(f"{RED}Error: {readme_path} not found.{RESET}")
        sys.exit(1)

    content = path.read_text(encoding="utf-8")
    current_category = None
    apis = []

    for line in content.splitlines():
        # Kategori başlığı
        category_match = re.match(r"^### (.+)", line)
        if category_match:
            current_category = category_match.group(1).strip()

        # Tablo satırı: | [Name](url) | Description | Auth | HTTPS | CORS |
        row_match = re.match(
            r"^\|\s*\[([^\]]+)\]\((https?://[^\)]+)\)\s*\|", line
        )
        if row_match and current_category:
            if category_filter and category_filter.lower() not in current_category.lower():
                continue
            apis.append({
                "name": row_match.group(1),
                "url":  row_match.group(2),
                "category": current_category,
            })

    return apis


def check_api(api: dict, timeout: int = 8) -> dict:
    """Tek bir API'ye istek atar ve sonucu döner."""
    try:
        start = time.time()
        resp = requests.get(
            api["url"],
            timeout=timeout,
            headers={"User-Agent": "public-apis/api-tester"},
            allow_redirects=True,
        )
        elapsed = round((time.time() - start) * 1000)
        status = resp.status_code

        if status < 400:
            label = f"{GREEN}✓ UP{RESET}"
        elif status < 500:
            label = f"{YELLOW}⚠ {status}{RESET}"
        else:
            label = f"{RED}✗ {status}{RESET}"

        return {**api, "status": status, "ms": elapsed, "label": label, "ok": status < 400}

    except requests.exceptions.Timeout:
        return {**api, "status": None, "ms": None,
                "label": f"{RED}✗ TIMEOUT{RESET}", "ok": False}
    except requests.exceptions.ConnectionError:
        return {**api, "status": None, "ms": None,
                "label": f"{RED}✗ CONNECTION ERROR{RESET}", "ok": False}
    except Exception as e:
        return {**api, "status": None, "ms": None,
                "label": f"{RED}✗ ERROR{RESET}", "ok": False}


def print_result(result: dict):
    """Tek satır sonuç yazar."""
    ms_str = f"{result['ms']}ms" if result["ms"] else "—"
    print(
        f"  {result['label']:<30} "
        f"{CYAN}{result['name']:<30}{RESET} "
        f"{ms_str:<10} "
        f"{result['url']}"
    )


def run_tests(apis: list[dict], sample_size: int = None):
    """API listesini test eder ve özet rapor yazar."""
    if not apis:
        print(f"{YELLOW}No APIs found with the given filter.{RESET}")
        return

    if sample_size:
        import random
        random.seed(42)
        apis = random.sample(apis, min(sample_size, len(apis)))

    total   = len(apis)
    up      = 0
    results_by_cat = {}

    print(f"\n{BOLD}{'─'*70}{RESET}")
    print(f"{BOLD}  public-apis — API Health Checker{RESET}")
    print(f"{BOLD}{'─'*70}{RESET}")
    print(f"  Testing {total} APIs...\n")

    for api in apis:
        result = check_api(api)
        cat = result["category"]
        results_by_cat.setdefault(cat, []).append(result)
        if result["ok"]:
            up += 1

    # Kategorilere göre yazdır
    for cat, items in results_by_cat.items():
        print(f"\n{BOLD}  [{cat}]{RESET}")
        for r in items:
            print_result(r)

    # Özet
    down = total - up
    pct  = round(up / total * 100) if total else 0
    print(f"\n{BOLD}{'─'*70}{RESET}")
    print(f"  {BOLD}Summary:{RESET}  "
          f"{GREEN}{up} UP{RESET}  |  "
          f"{RED}{down} DOWN{RESET}  |  "
          f"Total: {total}  |  "
          f"Uptime: {pct}%")
    print(f"{BOLD}{'─'*70}{RESET}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Test API endpoints listed in public-apis README.md"
    )
    parser.add_argument(
        "--category", "-c",
        type=str,
        default=None,
        help="Filter by category name (e.g. 'Weather', 'Animals')"
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Test ALL APIs (slow — may take several minutes)"
    )
    parser.add_argument(
        "--sample", "-s",
        type=int,
        default=10,
        help="Number of random APIs to test (default: 10)"
    )
    parser.add_argument(
        "--readme",
        type=str,
        default="README.md",
        help="Path to README.md (default: README.md)"
    )
    args = parser.parse_args()

    apis = parse_readme(args.readme, category_filter=args.category)

    if args.all or args.category:
        run_tests(apis)
    else:
        run_tests(apis, sample_size=args.sample)


if __name__ == "__main__":
    main()