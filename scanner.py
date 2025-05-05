import nmap

def scan(target_ip, ports="1-1024"):
    scanner = nmap.PortScanner()
    print(f"Scanning {target_ip}...")
    scanner.scan(target_ip, ports)

    for host in scanner.all_hosts():
        print(f"Host: {host}")
        for port in scanner[host]['tcp']:
            print(f"Port {port}: {scanner[host]['tcp'][port]['state']}")

target = input("Enter target IP address: ")
scan(target)
