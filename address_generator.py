#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-Country Address Generator
================================
A tool to generate random virtual identity data from meiguodizhi.com API.
Supports 22+ countries including US, UK, CA, JP, DE, FR, etc.

WARNING: This tool is for educational purposes only.
Do not use the generated data for illegal activities.

License: MIT
"""

import json
import time
import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library is required.")
    print("Install it with: pip install requests")
    sys.exit(1)


# ============================================================================
# CONFIGURATION
# ============================================================================

API_URL = "https://www.meiguodizhi.com/api/v1/dz"
DEFAULT_COUNT = 10
MAX_RETRIES = 3
TIMEOUT = 10
RETRY_DELAY = 2  # seconds

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}

# Supported countries mapping
COUNTRIES = {
    "us": {"name": "United States", "path": "/", "code": "us"},
    "uk": {"name": "United Kingdom", "path": "/uk-address", "code": "uk"},
    "ca": {"name": "Canada", "path": "/ca-address", "code": "ca"},
    "au": {"name": "Australia", "path": "/au-address", "code": "au"},
    "jp": {"name": "Japan", "path": "/jp-address", "code": "jp"},
    "tw": {"name": "Taiwan", "path": "/tw-address", "code": "tw"},
    "kr": {"name": "South Korea", "path": "/kr-address", "code": "kr"},
    "hk": {"name": "Hong Kong", "path": "/hk-address", "code": "hk"},
    "de": {"name": "Germany", "path": "/de-address", "code": "de"},
    "sg": {"name": "Singapore", "path": "/sg-address", "code": "sg"},
    "fr": {"name": "France", "path": "/fr-address", "code": "fr"},
    "it": {"name": "Italy", "path": "/it-address", "code": "it"},
    "es": {"name": "Spain", "path": "/es-address", "code": "es"},
    "nl": {"name": "Netherlands", "path": "/nl-address", "code": "nl"},
    "my": {"name": "Malaysia", "path": "/my-address", "code": "my"},
    "ru": {"name": "Russia", "path": "/ru-address", "code": "ru"},
    "cn": {"name": "China", "path": "/cn-address", "code": "cn"},
    "th": {"name": "Thailand", "path": "/th-address", "code": "th"},
    "ph": {"name": "Philippines", "path": "/ph-address", "code": "ph"},
    "ar": {"name": "Argentina", "path": "/ar-address", "code": "ar"},
    "tr": {"name": "Turkey", "path": "/tr-address", "code": "tr"},
    "vn": {"name": "Vietnam", "path": "/vn-address", "code": "vn"},
}

DEFAULT_COUNTRY = "uk"


# ============================================================================
# CORE FUNCTIONS
# ============================================================================


def fetch_address(country_code: str) -> Optional[Dict]:
    """
    Fetch a single address from the API with retry logic.

    Args:
        country_code: Country code (e.g., 'us', 'uk', 'jp')

    Returns:
        dict: Address data if successful, None otherwise
    """
    if country_code not in COUNTRIES:
        print(f"  ✗ Invalid country code: {country_code}")
        return None

    country_path = COUNTRIES[country_code]["path"]
    payload = {"path": country_path, "method": "address"}

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(
                API_URL, json=payload, headers=HEADERS, timeout=TIMEOUT
            )

            # Check HTTP status
            if response.status_code != 200:
                print(
                    f"  ⚠ HTTP {response.status_code} on attempt {attempt}/{MAX_RETRIES}"
                )
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY)
                    continue
                return None

            # Parse JSON
            data = response.json()

            # Validate response structure
            if data.get("status") == "ok" and "address" in data:
                return data
            else:
                print(
                    f"  ⚠ Invalid response structure: {data.get('status', 'unknown')}"
                )
                return None

        except requests.exceptions.Timeout:
            print(f"  ⚠ Timeout on attempt {attempt}/{MAX_RETRIES}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)

        except requests.exceptions.ConnectionError:
            print(f"  ⚠ Connection error on attempt {attempt}/{MAX_RETRIES}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)

        except json.JSONDecodeError as e:
            print(f"  ✗ Failed to parse JSON: {e}")
            return None

        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
            return None

    print(f"  ✗ Failed after {MAX_RETRIES} attempts")
    return None


def generate_batch(country_code: str, count: int, delay: float = 0.5) -> List[Dict]:
    """
    Generate a batch of addresses for a specific country.

    Args:
        country_code: Country code (e.g., 'us', 'uk', 'jp')
        count: Number of addresses to generate
        delay: Delay between requests in seconds (to avoid rate limiting)

    Returns:
        list: List of address data dictionaries
    """
    addresses = []
    failed_count = 0

    country_name = COUNTRIES[country_code]["name"]

    print(f"\n{'=' * 60}")
    print(f"  Generating {count} {country_name} Virtual Identities")
    print(f"{'=' * 60}\n")

    for i in range(1, count + 1):
        print(f"[{i}/{count}] Fetching address...", end=" ")

        data = fetch_address(country_code)

        if data:
            addresses.append(data)
            name = data["address"].get("Full_Name", "N/A")
            print(f"✓ Success ({name})")
        else:
            failed_count += 1
            print("✗ Failed")

        # Rate limiting: add delay between requests
        if i < count:
            time.sleep(delay)

    print(f"\n{'=' * 60}")
    print(f"  Summary: {len(addresses)} succeeded, {failed_count} failed")
    print(f"{'=' * 60}\n")

    return addresses


def save_to_json(data: List[Dict], filepath: Path) -> bool:
    """
    Save address data to a JSON file.

    Args:
        data: List of address dictionaries
        filepath: Output file path

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Ensure output directory exists
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # Write JSON with pretty formatting
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return True

    except IOError as e:
        print(f"✗ File I/O error: {e}")
        return False

    except Exception as e:
        print(f"✗ Unexpected error while saving: {e}")
        return False


def list_countries():
    """Print all supported countries."""
    print("\n" + "=" * 60)
    print("  SUPPORTED COUNTRIES")
    print("=" * 60 + "\n")

    for code, info in sorted(COUNTRIES.items()):
        print(f"  {code.upper():4s} - {info['name']}")

    print("\n" + "=" * 60)
    print(f"  Total: {len(COUNTRIES)} countries")
    print("=" * 60 + "\n")


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Generate random virtual identity data for multiple countries",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python uk_address_generator.py                        # Generate 10 UK addresses (default)
  python uk_address_generator.py -c us -n 50            # Generate 50 US addresses
  python uk_address_generator.py -c jp -n 20 -d 1.0     # 20 Japanese addresses, 1s delay
  python uk_address_generator.py --list                 # Show all supported countries
  python uk_address_generator.py -c de -o german.json   # German addresses, custom filename

Supported countries: us, uk, ca, au, jp, tw, kr, hk, de, sg, fr, it, es, nl, my, ru, cn, th, ph, ar, tr, vn

Note: This tool is for educational purposes only.
        """,
    )

    parser.add_argument(
        "-c",
        "--country",
        type=str,
        default=DEFAULT_COUNTRY,
        help=f"Country code (default: {DEFAULT_COUNTRY}). Use --list to see all options.",
    )

    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=DEFAULT_COUNT,
        help=f"Number of addresses to generate (default: {DEFAULT_COUNT})",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output JSON filename (default: addresses_COUNTRY_TIMESTAMP.json)",
    )

    parser.add_argument(
        "-d",
        "--delay",
        type=float,
        default=0.5,
        help="Delay between requests in seconds (default: 0.5)",
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="List all supported countries and exit",
    )

    return parser.parse_args()


def main():
    """
    Main entry point of the program.
    """
    print(
        """
╔════════════════════════════════════════════════════════════╗
║      Multi-Country Address Generator v2.0                  ║
║      Educational Use Only - 22+ Countries Supported        ║
╚════════════════════════════════════════════════════════════╝
    """
    )

    # Parse arguments
    args = parse_arguments()

    # Handle --list flag
    if args.list:
        list_countries()
        sys.exit(0)

    # Validate country code
    country_code = args.country.lower()
    if country_code not in COUNTRIES:
        print(f"✗ Error: Invalid country code '{args.country}'")
        print(f"  Use --list to see all supported countries")
        sys.exit(1)

    # Validate count
    if args.count < 1:
        print("✗ Error: Count must be at least 1")
        sys.exit(1)

    if args.count > 1000:
        print("⚠ Warning: Generating more than 1000 addresses may take a long time")
        print("          and could trigger API rate limiting.")
        response = input("Continue? (y/n): ")
        if response.lower() != "y":
            print("Aborted.")
            sys.exit(0)

    # Generate output filename
    if args.output:
        output_file = Path(args.output)
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = Path(f"addresses_{country_code}_{timestamp}.json")

    # Display selected country
    country_name = COUNTRIES[country_code]["name"]
    print(f"Selected Country: {country_name} ({country_code.upper()})")

    # Generate addresses
    start_time = time.time()
    addresses = generate_batch(country_code, args.count, delay=args.delay)
    elapsed_time = time.time() - start_time

    # Check if we got any data
    if not addresses:
        print("✗ No addresses were generated. Exiting.")
        sys.exit(1)

    # Save to file
    print(f"Saving to '{output_file}'...", end=" ")
    if save_to_json(addresses, output_file):
        file_size = output_file.stat().st_size / 1024  # KB
        print(f"✓ Done ({file_size:.1f} KB)")

        print(f"\n{'=' * 60}")
        print("  SUCCESS!")
        print(f"  Country: {country_name}")
        print(f"  File: {output_file.absolute()}")
        print(f"  Records: {len(addresses)}")
        print(f"  Time: {elapsed_time:.1f}s")
        print(f"{'=' * 60}\n")
    else:
        print("✗ Failed to save file")
        sys.exit(1)


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")
        sys.exit(1)
