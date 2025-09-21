from customtkinter import *
from socket import *
from threading import Thread
from tkinter.messagebox import showerror

# ------------------ App Setup ------------------
app = CTk()
app.title("Admin Panel")
app.geometry("800x600")

blocked = set()
users = {}           # username -> [username, ip]
identity = []        # list of connections (sockets)
logs = []

ADMIN_USER = ""
ADMIN_PASS = ""

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(('', 2222))
sock.listen()


# ------------------ Utils ------------------
def safe_close(con):
    try:
        con.close()
    except:
        pass
    if con in identity:
        identity.remove(con)

def remove_user(user, con, block=False):
    users.pop(user, None)
    safe_close(con)
    if block:
        blocked.add(user)


def update_users():
    """Send list of online users to all clients"""
    all_users = " ".join(users.keys())  # empty string if no users
    for con in identity[:]:
        try:
            con.sendall(f"OU:{all_users}".encode())
        except:
            safe_close(con)


# ------------------ Server Thread ------------------
def server(con, addr):
    username = None
    try:
        while True:
            data = con.recv(1024)
            if not data:
                if username:
                    logs.append(f"{username} disconnected")
                    remove_user(username, con)
                    update_users()
                break

            msg = data.decode().strip()

            if msg.startswith("S-"):
                # New connection
                username = msg.split("-")[1]
                if username in users:
                    logs.append(f"user {username} tried duplicate login → blocked")
                    remove_user(username, con, block=True)
                    break
                elif username in blocked:
                    logs.append(f"blocked user {username} tried to connect")
                    safe_close(con)
                    break
                else:
                    users[username] = [username, addr[0]]
                    logs.append(f"{username} connected from {addr[0]}")
                    update_users()

            elif msg.startswith("CC-"):
                # Client clean exit
                leaving_user = msg.split("-")[1]
                logs.append(f"{leaving_user} exited")
                remove_user(leaving_user, con)
                update_users()
                break

    except Exception as e:
        logs.append(f"Error with {username or addr}: {e}")
        remove_user(username, con)
        update_users()


def accept_users():
    while True:
        con, addr = sock.accept()
        identity.append(con)
        Thread(target=server, args=(con, addr), daemon=True).start()


# ------------------ GUI ------------------
login_frame = CTkFrame(app, corner_radius=20, width=400, height=300, fg_color="#2e2e2e")
login_frame.place(relx=0.5, rely=0.5, anchor="center")

title = CTkLabel(login_frame, text="🔐 Admin Login", font=("Arial", 28, "bold"))
title.pack(pady=20)

username_entry = CTkEntry(login_frame, placeholder_text="Username", font=("Arial", 18), width=250, height=40)
username_entry.pack(pady=10)

password_entry = CTkEntry(login_frame, placeholder_text="Password", show="*", font=("Arial", 18), width=250, height=40)
password_entry.pack(pady=10)

def start_server():
    start_btn.destroy()
    build_logs_panel(logs_frame)
    Thread(target=accept_users, daemon=True).start()

def show_logs_panel():
    global logs_frame, start_btn
    logs_frame = CTkFrame(app, corner_radius=15, fg_color="#1e1e1e")
    logs_frame.pack(fill="both", expand=True, padx=20, pady=20)

    start_btn = CTkButton(
        logs_frame,
        text="🚀 Turn on Server",
        font=("Arial", 20, "bold"),
        fg_color="green",
        width=250,
        height=60,
        corner_radius=15,
        command=start_server
    )
    start_btn.pack(pady=200)

def build_logs_panel(parent):
    global logs_box
    header = CTkLabel(parent, text="📜 System Logs", font=("Arial", 24, "bold"))
    header.pack(pady=10)

    logs_box = CTkTextbox(
        parent,
        font=("Consolas", 16),
        width=700,
        height=400,
        corner_radius=10
    )
    logs_box.pack(pady=10, padx=20)
    show_logs()

def show_logs():
    global logs_box
    logs_box.configure(state="normal")
    logs_box.delete("1.0", "end")
    for log in logs:
        logs_box.insert("end", log + "\n")
    logs_box.configure(state="disabled")
    logs_frame.after(500, show_logs)

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if username == ADMIN_USER and password == ADMIN_PASS:
        login_frame.destroy()
        show_logs_panel()
    else:
        showerror("Error", "Invalid Username or Password")

login_btn = CTkButton(login_frame, text="Login", font=("Arial", 18), width=200, height=40, fg_color="green", command=login)
login_btn.pack(pady=20)

# ------------------ Run ------------------
app.mainloop()
