# System Administrator and Network Production Application
# A comprehensive tool for system monitoring and network diagnostics

import os
import platform
import socket
import subprocess
import time
import datetime
import shutil

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False


# ─────────────────────────────────────────────
# SYSTEM INFORMATION
# ─────────────────────────────────────────────

def get_system_info():
    """Return basic OS and hardware information."""
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Hostname": socket.gethostname(),
        "Python Version": platform.python_version(),
        "Uptime": get_uptime(),
    }
    return info


def get_uptime():
    """Return system uptime as a human-readable string."""
    if PSUTIL_AVAILABLE:
        boot_time = psutil.boot_time()
        elapsed = time.time() - boot_time
        hours, remainder = divmod(int(elapsed), 3600)
        minutes, seconds = divmod(remainder, 60)
        return "{:02d}h {:02d}m {:02d}s".format(hours, minutes, seconds)
    return "N/A (psutil not installed)"


# ─────────────────────────────────────────────
# CPU / MEMORY / DISK
# ─────────────────────────────────────────────

def get_cpu_info():
    """Return CPU usage statistics."""
    if not PSUTIL_AVAILABLE:
        return {"CPU Usage": "N/A (psutil not installed)"}
    return {
        "Physical Cores": psutil.cpu_count(logical=False),
        "Logical Cores": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
    }


def get_memory_info():
    """Return RAM usage statistics."""
    if not PSUTIL_AVAILABLE:
        return {"Memory Usage": "N/A (psutil not installed)"}
    mem = psutil.virtual_memory()
    return {
        "Total (GB)": round(mem.total / (1024 ** 3), 2),
        "Available (GB)": round(mem.available / (1024 ** 3), 2),
        "Used (GB)": round(mem.used / (1024 ** 3), 2),
        "Usage (%)": mem.percent,
    }


def get_disk_info():
    """Return disk usage for all mounted partitions."""
    if not PSUTIL_AVAILABLE:
        total, used, free = shutil.disk_usage("/")
        gb = 1024 ** 3
        return [{
            "Mount": "/",
            "Total (GB)": round(total / gb, 2),
            "Used (GB)": round(used / gb, 2),
            "Free (GB)": round(free / gb, 2),
        }]
    partitions = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            partitions.append({
                "Device": part.device,
                "Mount": part.mountpoint,
                "FS Type": part.fstype,
                "Total (GB)": round(usage.total / (1024 ** 3), 2),
                "Used (GB)": round(usage.used / (1024 ** 3), 2),
                "Free (GB)": round(usage.free / (1024 ** 3), 2),
                "Usage (%)": usage.percent,
            })
        except PermissionError:
            pass
    return partitions


# ─────────────────────────────────────────────
# NETWORK INFORMATION
# ─────────────────────────────────────────────

def get_local_ip():
    """Return the machine's primary local IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return "Unavailable"


def get_network_interfaces():
    """Return network interface names and their IP addresses."""
    interfaces = []
    if PSUTIL_AVAILABLE:
        for iface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    interfaces.append({"Interface": iface, "IP": addr.address, "Netmask": addr.netmask})
    else:
        interfaces.append({"Interface": "primary", "IP": get_local_ip(), "Netmask": "N/A"})
    return interfaces


def ping_host(host, count=4):
    """Ping a host and return the full ping command output."""
    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", "-n", str(count), host]
    else:
        cmd = ["ping", "-c", str(count), host]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        return result.stdout
    except (subprocess.TimeoutExpired, FileNotFoundError) as err:
        return "Ping failed: {}".format(err)


def check_port(host, port, timeout=3):
    """Check whether a TCP port is open on the given host."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def dns_lookup(hostname):
    """Resolve a hostname to an IP address."""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror as err:
        return "DNS lookup failed: {}".format(err)


def get_network_stats():
    """Return cumulative network I/O counters."""
    if not PSUTIL_AVAILABLE:
        return {"Network Stats": "N/A (psutil not installed)"}
    counters = psutil.net_io_counters()
    return {
        "Bytes Sent (MB)": round(counters.bytes_sent / (1024 ** 2), 2),
        "Bytes Received (MB)": round(counters.bytes_recv / (1024 ** 2), 2),
        "Packets Sent": counters.packets_sent,
        "Packets Received": counters.packets_recv,
    }


# ─────────────────────────────────────────────
# PROCESS MANAGEMENT
# ─────────────────────────────────────────────

def get_top_processes(n=10):
    """Return the top N processes sorted by CPU usage."""
    if not PSUTIL_AVAILABLE:
        return [{"Process Info": "N/A (psutil not installed)"}]
    procs = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            procs.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    # Sort by CPU usage descending
    procs.sort(key=lambda p: p.get("cpu_percent", 0) or 0, reverse=True)
    return procs[:n]


# ─────────────────────────────────────────────
# DISPLAY HELPERS
# ─────────────────────────────────────────────

def print_header(title):
    width = 60
    print("\n" + "=" * width)
    print(" " + title.center(width - 2))
    print("=" * width)


def print_dict(data):
    for key, value in data.items():
        print("  {:<25} {}".format(str(key) + ":", value))


def print_list_of_dicts(data_list):
    for item in data_list:
        for key, value in item.items():
            print("  {:<25} {}".format(str(key) + ":", value))
        print()


# ─────────────────────────────────────────────
# MENU
# ─────────────────────────────────────────────

MENU = """
  1. System Information
  2. CPU & Memory Usage
  3. Disk Usage
  4. Network Interfaces
  5. Network I/O Statistics
  6. Ping a Host
  7. Check Port Availability
  8. DNS Lookup
  9. Top Processes (by CPU)
  Q. Quit
"""


def run_menu():
    print_header("System Administrator & Network Tool")
    print("  Started: {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    while True:
        print(MENU)
        choice = input("  Select option ==> ").strip().upper()

        if choice == "1":
            print_header("System Information")
            print_dict(get_system_info())

        elif choice == "2":
            print_header("CPU Information")
            print_dict(get_cpu_info())
            print_header("Memory Information")
            print_dict(get_memory_info())

        elif choice == "3":
            print_header("Disk Usage")
            print_list_of_dicts(get_disk_info())

        elif choice == "4":
            print_header("Network Interfaces")
            print_list_of_dicts(get_network_interfaces())

        elif choice == "5":
            print_header("Network I/O Statistics")
            stats = get_network_stats()
            if isinstance(stats, dict):
                print_dict(stats)
            else:
                print(" ", stats)

        elif choice == "6":
            host = input("  Enter hostname or IP to ping ==> ").strip()
            if host:
                print_header("Ping: {}".format(host))
                print(ping_host(host))

        elif choice == "7":
            host = input("  Enter hostname or IP ==> ").strip()
            port_str = input("  Enter port number ==> ").strip()
            if host and port_str.isdigit():
                port = int(port_str)
                open_flag = check_port(host, port)
                status = "OPEN" if open_flag else "CLOSED / UNREACHABLE"
                print_header("Port Check: {}:{}".format(host, port))
                print("  Status: {}".format(status))

        elif choice == "8":
            hostname = input("  Enter hostname to resolve ==> ").strip()
            if hostname:
                ip = dns_lookup(hostname)
                print_header("DNS Lookup: {}".format(hostname))
                print("  Resolved IP: {}".format(ip))

        elif choice == "9":
            print_header("Top 10 Processes by CPU Usage")
            for proc in get_top_processes():
                print("  PID {pid:<8} CPU {cpu_percent:<6}%  MEM {memory_percent:.1f}%  {name}".format(
                    pid=proc.get("pid", "?"),
                    cpu_percent=proc.get("cpu_percent", 0),
                    memory_percent=proc.get("memory_percent") or 0,
                    name=proc.get("name", "unknown"),
                ))

        elif choice == "Q":
            print("\n  Goodbye!\n")
            break

        else:
            print("  Invalid option. Please try again.")


if __name__ == "__main__":
    run_menu()
