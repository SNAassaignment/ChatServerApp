import socket
import threading
import json

clients = []  # list of (conn, username)

def broadcast_user_list():
    user_list = [u for _, u in clients]  # extract usernames
    data = json.dumps({"type": "userlist", "users": user_list}).encode()
    for conn, _ in clients:
        try:
            conn.sendall(data)
        except:
            pass

def handle_client(conn, addr):
    username = conn.recv(1024).decode()  # first msg is username
    clients.append((conn, username))
    broadcast_user_list()  # send updated list to everyone

    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
        except:
            break

    # remove user if disconnected
    clients.remove((conn, username))
    broadcast_user_list()
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen()
    print("Server started...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

start_server()
