#!/usr/bin/env python

import requests
import argparse

def get_ip_info(ip_address):
    """Gather information about the given IP address."""
    print(f"Gathering information for IP: {ip_address}")

    apis = {
        "ip-api.com": f"http://ip-api.com/json/{ip_address}",
        "ipapi.co": f"https://ipapi.co/{ip_address}/json/",
        "reallyfreegeoip.org": f"https://reallyfreegeoip.org/json/{ip_address}",
    }

    for name, url in apis.items():
        try:
            response = requests.get(url)
            data = response.json()
            print(f"\n--- {name} ---")
            for key, value in data.items():
                print(f"{key}: {value}")
        except requests.exceptions.RequestException as e:
            print(f"Error with {name}: {e}")
        except Exception as e:
            print(f"An error occurred with {name}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get information about an IP address.")
    parser.add_argument("ip_address", help="The IP address to get information about.")
    args = parser.parse_args()

    get_ip_info(args.ip_address)
