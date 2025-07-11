#!/usr/bin/env python

import requests
import argparse

def get_ip_info(ip_address):
    """Gather information about the given IP address."""
    print(f"Gathering information for IP: {ip_address}")

    # Using ip-api.com
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        if data["status"] == "success":
            print("\n--- ip-api.com ---")
            for key, value in data.items():
                print(f"{key}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"Error with ip-api.com: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get information about an IP address.")
    parser.add_argument("ip_address", help="The IP address to get information about.")
    args = parser.parse_args()

    get_ip_info(args.ip_address)
