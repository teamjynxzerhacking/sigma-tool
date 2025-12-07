import socket
from urllib.parse import urlparse

ART = r""" 
                 ___                   __                        
 __             /\_ \                 /\ \                       
/\_\  _____     \//\ \     ___     ___\ \ \/'\   __  __  _____   
\/\ \/\ '__`\     \ \ \   / __`\  / __`\ \ , <  /\ \/\ \/\ '__`\ 
 \ \ \ \ \L\ \     \_\ \_/\ \L\ \/\ \L\ \ \ \\`\\ \ \_\ \ \ \L\ \
  \ \_\ \ ,__/     /\____\ \____/\ \____/\ \_\ \_\ \____/\ \ ,__/
   \/_/\ \ \/      \/____/\/___/  \/___/  \/_/\/_/\/___/  \ \ \/ 
        \ \_\                                              \ \_\ 
         \/_/                                               \/_/ 
"""

print(ART)


def extract_hostname(url: str) -> str:
    """Extract hostname from a URL or plain text."""
    url = url.strip()
    if not url:
        return ""
    if "://" not in url:
        url = "http://" + url
    parsed = urlparse(url)
    return parsed.hostname or ""

def resolve_host(hostname: str):
    """Return all DNS info using getaddrinfo."""
    try:
        infos = socket.getaddrinfo(hostname, None)
        return infos
    except socket.gaierror as e:
        print(f"❌ Unable to resolve DNS: {e}")
        return None

def main():
    print("🔍 DNS Resolver — enter a URL / host (q to quit)\n")

    while True:
        user = input("Enter URL/host: ").strip()
        if not user:
            continue
        if user.lower() in ("q", "quit", "exit"):
            print("Exiting.")
            break

        host = extract_hostname(user)
        if not host:
            print("⚠️ Invalid input — try example.com or https://example.com\n")
            continue

        print(f"\n🔎 Resolving: {host}\n")
        infos = resolve_host(host)
        if not infos:
            continue

        seen_ips = set()
        for i, info in enumerate(infos, 1):
            family, socktype, proto, canonname, sockaddr = info
            ip = sockaddr[0]
            if ip in seen_ips:
                continue
            seen_ips.add(ip)

            print(f"🧩 Record {i}:")
            print(f"   🌍 Canonical Name : {canonname or '—'}")
            print(f"   💾 IP Address    : {ip}")
            print(f"   🧭 IP Type       : {'IPv4' if family == socket.AF_INET else 'IPv6'}")
            print(f"   ⚙️  Socket Type  : {'Stream (TCP)' if socktype == socket.SOCK_STREAM else 'Datagram (UDP)'}")
            print(f"   📡 Socket Family : {family}")
            print()

        print("-" * 50)

if __name__ == "__main__":
    main()
