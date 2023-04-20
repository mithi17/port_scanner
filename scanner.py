import socket
import threading

target = input("Enter the host to scan: ")
ip = socket.gethostbyname(target)

print("Scanning host: ", ip)

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print("Port {}: Open".format(port))
    sock.close()

for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    t.start()
