from customtkinter import *
from socket import *
from threading import Thread
from tkinter.messagebox import showerror
from time import sleep

app = CTk()
app.title("Admin Panel")
app.geometry("800x600")

blocked = set()
users = dict()
identity = []
logs = []
ADMIN_USER = ""
ADMIN_PASS = ""

sock = socket(AF_INET,SOCK_STREAM)
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sock.bind(('',2222))
sock.listen()

def update_users():
    while True:
        for cons in identity:
            try:
                users_list = ''.join(users.keys())
                cons.sendall(f':{users_list}'.encode())
            except Exception:
                continue    
        sleep(3)

def remove_user(user,con,block=False):
    try:
        for _users,identities in zip(users.keys(),identity):
            if user in _users:
                del users[_users]
            if con in identity:
                identity.remove(identities)
    
        if block:
            for blkd in blocked:
                if user in blkd:
                    blocked.remove(user)
    except Exception as e:
        print(e)

def server(con,addr):
    try:
        while True:
            getinfo = con.recv(1024).decode().strip()
            username = getinfo
            ip = addr[0]
            getuser = {username:[username,ip]}

            if not getinfo:
                continue

            elif getinfo.startswith('CLOSE-'):
                c_user = getinfo.split('-')[1]
                remove_user(c_user,con)
                logs.append(f'{c_user} is disconnected from the chat')
                con.close()
                break

            elif getinfo.startswith('S-'):
                user = getinfo.split('-')[1]
                if user in users.keys():
                    logs.append(f'user {user} try to connect in same name')
                    logs.append(f'{user} blocked from server')
                    blocked.add(user)
                    con.close()
                elif user in blocked:
                    logs.append(f'blocked user {user} try to connect in server')
                    con.close()
                else:
                    users.update(getuser)
                    logs.append(f'{user} connected to the server')
            else:pass

    except Exception as e:
        print(e)

    except BrokenPipeError:
        print(username)
        print(users)

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
    Thread(target=ac,daemon=True).start()

def ac():
    while True:
        con,addr = sock.accept()
        Thread(target=server,args=(con,addr),daemon=True).start()

def show_logs_panel():
    global logs_frame,start_btn
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

Thread(target=update_users,daemon=True).start()
app.mainloop()