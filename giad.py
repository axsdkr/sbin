#!/usr/bin/env python3

import socket


def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror as error:
        raise ValueError(
            f"Failed to retrieve IP address for {hostname}\nError: {error}"
        )


def main():
    hostname = input("Please enter a website address (URL): ")
    try:
        ip_address = get_ip_address(hostname)
        print(f"\nDomain Name: {hostname}")
        print(f"IP Address: {ip_address}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
