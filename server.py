from customtkinter import *
from socket import *
from threading import Thread
from tkinter.messagebox import showerror

app = CTk()
app.title("Admin Panel")
app.geometry("800x600")

blocked = set()
users = dict()
logs = []
ADMIN_USER = ""
ADMIN_PASS = ""

def server():
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sock.bind(('',2222))

    while True:
        print(users)
        mon = sock.recvfrom(1024)
        
        if not mon:
            continue

        try:
            username = mon[0].decode().strip()
            ip = mon[1]
            getuser = {username:ip[0]}

            if username in blocked:
                logs.append(f'blocked user {username} try to connect')
                continue

            if username not in users.keys() and username not in blocked:
                users.update(getuser)
                logs.append(f'{username} joined to the server with {ip}')

            elif username in users.keys():
                logs.append(f'{username} does suspicious connect to the server. user blocked')
                blocked.add(username)

        except Exception as e:
            print(e)


# ---------- Login Frame ----------
login_frame = CTkFrame(app, corner_radius=20, width=400, height=300, fg_color="#2e2e2e")
login_frame.place(relx=0.5, rely=0.5, anchor="center")

title = CTkLabel(login_frame, text="🔐 Admin Login", font=("Arial", 28, "bold"))
title.pack(pady=20)

username_entry = CTkEntry(login_frame, placeholder_text="Username", font=("Arial", 18), width=250, height=40)
username_entry.pack(pady=10)

password_entry = CTkEntry(login_frame, placeholder_text="Password", show="*", font=("Arial", 18), width=250, height=40)
password_entry.pack(pady=10)

# ---------- Logs Panel ----------
def show_logs_panel():
    global logs_frame
    logs_frame = CTkFrame(app, corner_radius=15, fg_color="#1e1e1e")
    logs_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Show button first
    def start_server():
        Thread(target=server,daemon=True).start()
        start_btn.destroy()  
        build_logs_panel(logs_frame)  

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
    start_btn.pack(pady=200)  # center button


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
    logs_box.delete("1.0", "end")   # clear before re-adding
    for log in logs:
        logs_box.insert("end", log + "\n")
    logs_box.configure(state="disabled")

    logs_frame.after(200, show_logs)  # schedule next update

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

# Thread(target=show_logs,daemon=True).start()
app.mainloop()
