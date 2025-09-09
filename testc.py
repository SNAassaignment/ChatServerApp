import socket
from time import sleep

# Server host and port
HOST = '127.0.0.1'
PORT = 12345

# Create socket (IPv4, TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((HOST, PORT))
print(f"[+] Connected to server {HOST}:{PORT}")

# Communication loop
while client_socket:
    try:
        client_socket.send(b'Hi!')
        sleep(1)
    except Exception as e:
        print(e)
client_socket.close()
