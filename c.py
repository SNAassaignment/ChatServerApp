import socket
import threading
import tkinter as tk
from tkinter import messagebox
import json

def listen_for_updates(sock, listbox):
    while True:
        try:
            data = sock.recv(1024).decode()
            if not data:
                break

            msg = json.loads(data)
            if msg["type"] == "userlist":
                users = msg["users"]

                # update UI in Tkinter thread
                listbox.delete(0, tk.END)
                for user in users:
                    listbox.insert(tk.END, user)
        except:
            break

def start_client(username):
    root = tk.Tk()
    root.title(f"Chat - {username}")

    listbox = tk.Listbox(root, height=10, width=30)
    listbox.pack(pady=10)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 9999))
    sock.sendall(username.encode())

    threading.Thread(target=listen_for_updates, args=(sock, listbox), daemon=True).start()

    root.mainloop()

start_client("mohamed")  # change username
