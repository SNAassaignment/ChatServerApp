a = ['a','d']

b = ['d']

c = {'a':1,'c':2,'d':3}
print('\n'.join(c.keys()))
# for i in c.keys():
#     print(i)
# from customtkinter import *
# from socket import *
# from threading import Thread
# from tkinter.messagebox import showerror
# from time import sleep

# # ------------------ App Setup ------------------
# app = CTk()
# app.title("Admin Panel")
# app.geometry("800x600")

# blocked = set()
# users = dict()       # username -> [username, ip]
# identity = []        # list of socket connections
# logs = []

# ADMIN_USER = ""
# ADMIN_PASS = ""

# sock = socket(AF_INET, SOCK_STREAM)
# sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# sock.bind(('', 2222))
# sock.listen()

# # ------------------ Utility Functions ------------------
# def safe_close(con):
#     try:
#         con.close()
#     except OSError:
#         pass
#     if con in identity:
#         identity.remove(con)

# def remove_user(user, con, block=False):
#     try:
#         users.pop(user, None)
#         safe_close(con)
#         if block:
#             blocked.discard(user)
#     except Exception as e:
#         logs.append(f"Error removing user {user}: {e}")

# def update_users():
#     """Send the full online user list to all connected clients"""
#     if not users:
#         user_list = ""
#     else:
#         user_list = ','.join(users.keys())

#     for con in identity[:]:
#         try:
#             con.sendall(f'OU:{user_list}'.encode())
#         except OSError:
#             safe_close(con)

# # ------------------ Server Thread ------------------
# def server(con, addr):
#     username = None
#     try:
#         while True:
#             data = con.recv(1024)
#             if not data:
#                 if username:
#                     logs.append(f'{username} disconnected abruptly')
#                     remove_user(username, con)
#                     update_users()
#                 break

#             getinfo = data.decode().strip()
            
#             if getinfo.startswith('CLOSE-'):
#                 c_user = getinfo.split('-')[1]
#                 remove_user(c_user, con)
#                 logs.append(f'{c_user} is disconnected from the chat')
#                 update_users()
#                 break

#             elif getinfo.startswith('S-'):
#                 user = getinfo.split('-')[1]
#                 if user in users:
#                     logs.append(f'user {user} tried to connect with the same name')
#                     logs.append(f'{user} blocked from server')
#                     blocked.add(user)
#                     safe_close(con)
#                     break
#                 elif user in blocked:
#                     logs.append(f'blocked user {user} tried to connect')
#                     safe_close(con)
#                     break
#                 else:
#                     username = user
#                     ip = addr[0]
#                     users[user] = [user, ip]
#                     logs.append(f'{user} connected to the server')
#                     update_users()

#             elif getinfo.startswith('CC-'):
#                 get_user = getinfo.split('-')[1]
#                 logs.append(f'{get_user} exited from the chat server')
#                 remove_user(get_user, con, False)
#                 update_users()
#                 break

#     except Exception as e:
#         logs.append(f"Error with {username if username else addr}: {e}")
#         remove_user(username, con)
#         update_users()

# # ------------------ Accept Users ------------------
# def accept_users():
#     while True:
#         con, addr = sock.accept()
#         identity.append(con)
#         Thread(target=server, args=(con, addr), daemon=True).start()

# # ------------------ GUI ------------------
# login_frame = CTkFrame(app, corner_radius=20, width=400, height=300, fg_color="#2e2e2e")
# login_frame.place(relx=0.5, rely=0.5, anchor="center")

# title = CTkLabel(login_frame, text="🔐 Admin Login", font=("Arial", 28, "bold"))
# title.pack(pady=20)

# username_entry = CTkEntry(login_frame, placeholder_text="Username", font=("Arial", 18), width=250, height=40)
# username_entry.pack(pady=10)

# password_entry = CTkEntry(login_frame, placeholder_text="Password", show="*", font=("Arial", 18), width=250, height=40)
# password_entry.pack(pady=10)

# def start_server():
#     start_btn.destroy()
#     build_logs_panel(logs_frame)
#     Thread(target=accept_users, daemon=True).start()

# def show_logs_panel():
#     global logs_frame, start_btn
#     logs_frame = CTkFrame(app, corner_radius=15, fg_color="#1e1e1e")
#     logs_frame.pack(fill="both", expand=True, padx=20, pady=20)

#     start_btn = CTkButton(
#         logs_frame,
#         text="🚀 Turn on Server",
#         font=("Arial", 20, "bold"),
#         fg_color="green",
#         width=250,
#         height=60,
#         corner_radius=15,
#         command=start_server
#     )
#     start_btn.pack(pady=200)

# def build_logs_panel(parent):
#     global logs_box
#     header = CTkLabel(parent, text="📜 System Logs", font=("Arial", 24, "bold"))
#     header.pack(pady=10)

#     logs_box = CTkTextbox(
#         parent,
#         font=("Consolas", 16),
#         width=700,
#         height=400,
#         corner_radius=10
#     )
#     logs_box.pack(pady=10, padx=20)
#     show_logs()

# def show_logs():
#     global logs_box
#     logs_box.configure(state="normal")
#     logs_box.delete("1.0", "end")
#     for log in logs:
#         logs_box.insert("end", log + "\n")
#     logs_box.configure(state="disabled")
#     logs_frame.after(200, show_logs)

# def login():
#     username = username_entry.get().strip()
#     password = password_entry.get().strip()
#     if username == ADMIN_USER and password == ADMIN_PASS:
#         login_frame.destroy()
#         show_logs_panel()
#     else:
#         showerror("Error", "Invalid Username or Password")

# login_btn = CTkButton(login_frame, text="Login", font=("Arial", 18), width=200, height=40, fg_color="green", command=login)
# login_btn.pack(pady=20)

# # ------------------ Run ------------------
# app.mainloop()
