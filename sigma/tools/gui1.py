import tkinter as tk
from tkinter import messagebox
import requests

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
