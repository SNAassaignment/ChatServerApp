from customtkinter import *
from socket import *
from threading import Thread
from tkinter.messagebox import showerror
from time import time
from inspect import currentframe

app = CTk()
app.title("Admin Panel")
app.geometry("800x600")

blocked = set()
users = dict()
identity = set()
logs = []
ADMIN_USER = ""
ADMIN_PASS = ""

sock = socket(AF_INET,SOCK_STREAM)
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sock.bind(('',2222))
sock.listen()

def update_users():
    all_users = ','.join(set(users.keys()))
    for con in identity:
        try:
            con.sendall(f'OU:{all_users}'.encode())
        except Exception as e:
            print(e,f'line number:{currentframe().f_lineno}')

def remove_user(user,con,block=False):
    try:
        identity.discard(con)
        for _user in list(users.keys()): list(users.keys()).remove(user) if user == _user else None
        blocked.remove(user) if block else None
    except Exception as e:
        print(e,f'line number:{currentframe().f_lineno}')

def check_new_user(user,con,addr):
    is_new_user = True
    try:
        for blk_user in blocked:
            if user == blk_user:
                logs.append(f'Blocked user {user} try to connect.')
                con.sendall('RU'.encode())
                is_new_user = False

        for _user in users.keys():
            if user == _user:
                logs.append(f'User {user} try to connect again while in server')
                con.sendall('RU'.encode())
                is_new_user = False

        if is_new_user:
            logs.append(f'{user} connected to the server')
            users.update({user:[user,addr[1]]})

    except Exception as e:
        print(e,f'line number:{currentframe().f_lineno}')

def server(con,addr):
    try:
        while True:
            getinfo = con.recv(1024).decode().strip()

            if not getinfo:
                continue

            if getinfo.startswith('NEW-'):
                getuser = getinfo.split('-')[1]
                check_new_user(getuser,con,addr)
                update_users()

            #Close connection - CC
            if getinfo.startswith('CC-'):
                global get_user
                get_user = getinfo.split('-')[1]
                remove_user(get_user,con)
                for _con in identity:
                    try:
                        if _con != con:
                            _con.sendall(f'LEFT-{get_user}'.encode())
                    except:pass
                # logs.append(f'{get_user} left from the chat server')
                logs.append(f'{get_user} is disconnected')
                con.close()

    except OSError:
        remove_user(get_user,con)

    except Exception as e:
        print(e,f'line number:{currentframe().f_lineno}')


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
    Thread(target=accept_users,daemon=True).start()

def accept_users():
    while True:
        starttm = int(time() % 60)
        con,addr = sock.accept()
        if con:
            end = int(time() % 60)
            delay = end - starttm
            if delay < 1:
                print(starttm)
                print(end)
                print(delay)
                con.close()
                logs.append(f'client {addr[0]} too fast to connect to server')

                try:
                    if con in identity:
                        identity.remove(con)
                        print('con is removed')
                except Exception as e:
                    print(e)
            else:
                identity.add(con)
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
        font=("Consolas", 25),
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

app.mainloop()