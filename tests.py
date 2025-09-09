import socket

# Server host and port
HOST = '127.0.0.1'  # localhost
PORT = 12345        # port to listen on

# Create socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to host and port
server_socket.bind((HOST, PORT))

# Start listening for connections
server_socket.listen(5)
print(f"[*] Server listening on {HOST}:{PORT}")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"[+] Connected to {client_address}")

# Communication loop
while client_socket:
    try:
        print(client_socket.recv(1024).decode())
    except Exception as e:
        print(e)
client_socket.close()
server_socket.close()
