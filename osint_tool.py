# OSINT Reconnaissance Tool (Simple CLI-Based Python Project)

import socket
import requests
import whois
import json
import subprocess
import sys

# 1. Get IP Address of a Domain
def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception as e:
        return f"Error: {e}"

# 2. Get IP Details using ipinfo.io
def get_ip_details(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# 3. MAC Address Info (Explain in result)
def get_mac_note():
    return "MAC Address cannot be obtained remotely. Only accessible within local network."

# 4. Domain WHOIS Details
def get_domain_whois(domain):
    try:
        data = whois.whois(domain)
        return data
    except Exception as e:
        return f"Error: {e}"

# 5. Reverse IP Lookup using HackerTarget
def reverse_ip_lookup(ip):
    try:
        response = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}")
        return response.text
    except Exception as e:
        return f"Error: {e}"

# 6. Technology Stack (using Wappalyzer API demo alternative)
def get_tech_stack(domain):
    return "Technology detection requires tools like Wappalyzer, which have paid APIs. For learning, use Wappalyzer browser extension manually."

# 7. Subdomain Enumeration using crt.sh
def get_subdomains(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url)
        data = response.json()
        subdomains = set(entry['name_value'] for entry in data)
        return list(subdomains)
    except Exception as e:
        return [f"Error: {e}"]

# Main Program
if __name__ == "__main__":
    domain = input("Enter domain (example.com): ")
    print("\n--- OSINT Reconnaissance Report ---\n")

    ip = get_ip(domain)
    print(f"1. IP Address: {ip}")

    print("\n2. IP Address Details:")
    ip_info = get_ip_details(ip)
    print(json.dumps(ip_info, indent=2))

    print("\n3. MAC Address:")
    print(get_mac_note())

    print("\n4. Domain WHOIS Details:")
    whois_info = get_domain_whois(domain)
    print(whois_info)

    print("\n5. Reverse IP Lookup:")
    print(reverse_ip_lookup(ip))

    print("\n6. Technology Stack:")
    print(get_tech_stack(domain))

    print("\n7. Subdomain Enumeration:")
    subdomains = get_subdomains(domain)
    for sub in subdomains:
        print(f"- {sub}")


# OSINT Reconnaissance Tool (Double Version)

import socket
import requests
import whois
import json
import subprocess
import sys

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception as e:
        return f"Error: {e}"

def get_ip_details(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_mac_note():
    return "MAC Address cannot be obtained remotely. Only accessible within local network."

def get_domain_whois(domain):
    try:
        data = whois.whois(domain)
        return data
    except Exception as e:
        return f"Error: {e}"

def reverse_ip_lookup(ip):
    try:
        response = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}")
        return response.text
    except Exception as e:
        return f"Error: {e}"

def get_tech_stack(domain):
    return "Technology detection requires tools like Wappalyzer, which have paid APIs. For learning, use Wappalyzer browser extension manually."

def get_subdomains(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url)
        data = response.json()
        subdomains = set(entry['name_value'] for entry in data)
        return list(subdomains)
    except Exception as e:
        return [f"Error: {e}"]

if __name__ == "__main__":
    domain = input("Enter domain (example.com): ")
    print("\n--- OSINT Reconnaissance Report ---\n")

    ip = get_ip(domain)
    print(f"1. IP Address: {ip}")

    print("\n2. IP Address Details:")
    ip_info = get_ip_details(ip)
    print(json.dumps(ip_info, indent=2))

    print("\n3. MAC Address:")
    print(get_mac_note())

    print("\n4. Domain WHOIS Details:")
    whois_info = get_domain_whois(domain)
    print(whois_info)

    print("\n5. Reverse IP Lookup:")
    print(reverse_ip_lookup(ip))

    print("\n6. Technology Stack:")
    print(get_tech_stack(domain))

    print("\n7. Subdomain Enumeration:")
    subdomains = get_subdomains(domain)
    for sub in subdomains:
        print(f"- {sub}")
