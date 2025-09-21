# from customtkinter import *
# from socket import *
# from threading import Thread
# from tkinter.messagebox import showerror,showinfo,askyesno
# import random
# from datetime import datetime
# from time import sleep

# set_appearance_mode("light")
# set_default_color_theme("blue")

# app_name = 'Mohamed\'s server'
# app = CTk()
# username = StringVar()
# app.geometry("1400x800")
# app.title(app_name)
# app.configure(fg_color="#f5f7fa") 
# sock = socket(AF_INET,SOCK_STREAM)
# showed_users = set()

# sidebar_frame = CTkFrame(app, width=300, fg_color="#2c3e50", corner_radius=0)
# sidebar_frame.pack(side="left", fill="y", padx=(0, 10))

# # Main content frame
# content_frame = CTkFrame(app, fg_color="#ffffff", corner_radius=12)
# content_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

# # -------------------- Online Users Section --------------------
# # Online users header
# online_users_header = CTkFrame(sidebar_frame, fg_color="#34495e", height=60,corner_radius=0)
# online_users_header.pack(fill="x", pady=(0, 10))

# CTkLabel(online_users_header, text="Online Users", 
#          font=("Arial", 20, "bold"), text_color="white").pack(expand=True, pady=15)


# users_scrollable = CTkScrollableFrame(sidebar_frame, fg_color="transparent")
# users_scrollable.pack(fill="both", expand=True, padx=10, pady=10)

# users = []

# def create_user_card(parent, user):
#     card = CTkFrame(parent, height=60, fg_color="#34495e", corner_radius=8)
#     card.pack(fill="x", pady=5)
    
#     colors = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6", "#1abc9c"]
#     color = random.choice(colors)
    
#     avatar = CTkLabel(card, text=user[0], 
#                     width=5, height=40,
#                     fg_color=color, 
#                     text_color="white",
#                     corner_radius=18,
#                     font=("Arial", 16, "bold"))
#     avatar.place(x=10, y=10)

#     CTkLabel(card, text='You' if user == _username else user, 
#             font=("Arial", 14, "bold"),
#             text_color="white").place(x=80, y=12)
#     showed_users.add(user)
    
#     return card
    
# def refresh_user_cards(user_list):
#     for widget in users_scrollable.winfo_children():
#         widget.destroy()

#     showed_users.clear()

#     for u in user_list:
#         if u:
#             create_user_card(users_scrollable,u)

# header_frame = CTkFrame(content_frame, fg_color="transparent", height=80)
# header_frame.pack(fill="x", padx=30, pady=(30, 20))

# CTkLabel(header_frame, textvariable=username, 
#          font=("Arial", 32, "bold"),
#          text_color="#2c3e50").pack(side="left")

# chat_frame = CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=12)
# chat_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))

# chat_header = CTkFrame(chat_frame, fg_color="#e9ecef", height=60, corner_radius=12)
# chat_header.pack(fill="x", pady=(0, 5))

# CTkLabel(chat_header, text="General Chat Room", 
#          font=("Arial", 18, "bold"),
#          text_color="#2c3e50").pack(side="left", padx=20)

# messages_frame = CTkScrollableFrame(chat_frame, fg_color="transparent")
# messages_frame.pack(fill="both", expand=True, padx=10, pady=10)

# sample_messages = [
    
# ]

# # Function to create message bubbles
# def create_message_bubble(parent, message, is_own=False):
#     bubble_frame = CTkFrame(parent, fg_color="transparent")
#     bubble_frame.pack(fill="x", pady=8)
    
#     # Align to right if it's our message
#     if is_own:
#         inner_frame = CTkFrame(bubble_frame, fg_color="transparent")
#         inner_frame.pack(anchor="e")
        
#         # Time label
#         CTkLabel(inner_frame, text=message["time"], 
#                 font=("Arial", 10),
#                 text_color="#7f8c8d").pack(anchor="e", padx=(0, 10))
        
#         # Message bubble
#         bubble = CTkFrame(inner_frame, fg_color="#3498db", corner_radius=12)
#         bubble.pack(anchor="e", pady=2)
        
#         CTkLabel(bubble, text=message["text"], 
#                 font=("Arial", 14),
#                 text_color="white",
#                 wraplength=400, justify="left").pack(padx=15, pady=10)
        
#         # Sender name
#         CTkLabel(inner_frame, text="You", 
#                 font=("Arial", 12, "bold"),
#                 text_color="#2c3e50").pack(anchor="e", padx=(0, 10))
#     else:
#         inner_frame = CTkFrame(bubble_frame, fg_color="transparent")
#         inner_frame.pack(anchor="w")
        
#         # Sender name
#         CTkLabel(inner_frame, text=message["sender"], 
#                 font=("Arial", 12, "bold"),
#                 text_color="#2c3e50").pack(anchor="w", padx=(10, 0))
        
#         # Message bubble
#         bubble = CTkFrame(inner_frame, fg_color="#e9ecef", corner_radius=12)
#         bubble.pack(anchor="w", pady=2)
        
#         CTkLabel(bubble, text=message["text"], 
#                 font=("Arial", 14),
#                 text_color="#2c3e50",
#                 wraplength=400, justify="left").pack(padx=15, pady=10)
        
#         # Time label
#         CTkLabel(inner_frame, text=message["time"], 
#                 font=("Arial", 10),
#                 text_color="#7f8c8d").pack(anchor="w", padx=(10, 0))

# # Add sample messages to the chat
# for msg in sample_messages:
#     is_own = msg["sender"] == "Hathim"
#     Thread(target=create_message_bubble,args=(messages_frame, msg, is_own),daemon=True).start()

# # Message input area
# input_frame = CTkFrame(chat_frame, fg_color="transparent", height=70)
# input_frame.pack(fill="x", padx=10, pady=10)

# # Message input field
# message_entry = CTkEntry(input_frame, 
#                         placeholder_text="Type your message here...",
#                         font=("Arial", 14),
#                         height=45,
#                         corner_radius=20,
#                         border_width=0,
#                         fg_color="#e9ecef")
# message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

# def send_message():
#     message_text = message_entry.get()
#     if message_text.strip():
#         # Get current time
#         now = datetime.now()
#         time_str = now.strftime("%H:%M %p")
        
#         # Create new message
#         new_message = {
#             "sender": "Hathim",
#             "text": message_text,
#             "time": time_str
#         }
        
#         # Add to chat
#         create_message_bubble(messages_frame, new_message, True)
        
#         # Clear input
#         message_entry.delete(0, END)
        
#         # Scroll to bottom
#         messages_frame._parent_canvas.yview_moveto(1.0)

# # Send button
# send_button = CTkButton(input_frame, 
#                        text="Send",
#                        command=send_message,
#                        font=("Arial", 14, "bold"),
#                        height=45,
#                        width=100,
#                        fg_color="#3498db",
#                        hover_color="#2980b9",
#                        corner_radius=20)
# send_button.pack(side="right")

# message_entry.bind("<Return>", lambda event: send_message())

# def ask_username():
#     popup = CTkToplevel(app)
#     popup.title("Enter Username")
#     popup.geometry("500x300")
#     popup.resizable(False, False)
#     popup.grab_set()  # Make it modal (block main window until closed)
#     popup.configure(fg_color="#f5f7fa")  # soft background

#     # Header
#     header = CTkLabel(
#         popup, 
#         text="👤 Welcome!",
#         font=("Arial", 22, "bold"),
#         text_color="#2c3e50"
#     )
#     header.pack(pady=(20, 10))

#     subtitle = CTkLabel(
#         popup,
#         text="Please enter your username to continue",
#         font=("Arial", 14),
#         text_color="#7f8c8d"
#     )
#     subtitle.pack(pady=(0, 20))

#     # Username entry
#     username_entry = CTkEntry(
#         popup,
#         placeholder_text="Type your username...",
#         width=280,
#         height=40,
#         corner_radius=15,
#         font=("Arial", 14),
#         fg_color="#ecf0f1"
#     )
#     username_entry.pack(pady=10)

#     # Action buttons frame
#     button_frame = CTkFrame(popup, fg_color="transparent")
#     button_frame.pack(pady=20)

#     def confirm_username():
#         global _username
#         _username = username_entry.get().strip()
#         if _username:
#             username.set(f'Welcome, {username_entry.get().strip()}')
#             sock.sendall(f'NEW-{username.get().split(',')[1].strip()}'.encode())
#             popup.destroy()
#         if not _username:
#             showinfo(title=app_name,message='enter your username to continue')
#             ask_username()

#     def cancel():
#         if askyesno(title=app_name,message='You don\'t continue the app without username!'):
#             app.destroy()
#         else:
#             popup.destroy()
#             ask_username()

#     confirm_btn = CTkButton(
#         button_frame,
#         text="Confirm",
#         command=confirm_username,
#         fg_color="#3498db",
#         hover_color="#2980b9",
#         corner_radius=15,
#         width=120,
#         height=50,
#         font=("Arial", 14, "bold")
#     )
#     confirm_btn.pack(side="left", padx=10)

#     cancel_btn = CTkButton(
#         button_frame,
#         text="Cancel",
#         command=cancel,
#         fg_color="#e74c3c",
#         hover_color="#c0392b",
#         corner_radius=15,
#         width=120,
#         height=50,
#         font=("Arial", 14, "bold")
#     )
#     cancel_btn.pack(side="right", padx=10)

#     username_entry.focus()

# def on_close():
#     try:
#         sock.send(f'CC-{username.get().split(',')[1].strip()}'.encode())
#         sleep(0.8)
#         sock.close()
#     except:
#         pass
#     finally:
#         sock.close()
#         app.destroy()

# def add_users(user_list):
#     rm_dup = set()
#     rm_dup.clear()
#     for u in user_list:
#         rm_dup.add(u)
    
#     for _u in rm_dup:
#         users.append({'name':_u})
    
#     return rm_dup

# def _refresh(u_list):
#     app.after(0,lambda:refresh_user_cards(u_list))

# def start_server():
#     try:
#         sock.connect(('127.0.0.1',2222))
#         ask_username()
#         #get online users from the server to show case clients each other.
#         while True:
#             get_o_users = sock.recv(1024).decode().strip()

#             if not get_o_users:
#                 continue

#             if get_o_users.startswith('OU:'):
#                 user = get_o_users.split(':')[1].split(',')
#                 #Remove duplicate user for iteration
#                 rm_dup_u = add_users(user)

#                 Thread(target=_refresh,args=(rm_dup_u,),daemon=True).start()

#             if get_o_users == 'RU':
#                 showinfo(title=app_name,message='Server rejects you')

#             continue

#     except ConnectionRefusedError:
#         showerror(title=app_name,message='Now the server get down, try again later')

#     except ConnectionResetError:
#         showerror(title=app_name,message='Server issue try again')

#     except Exception as e:
#         print(e)

# Thread(target=start_server,daemon=True).start()
# app.protocol('WM_DELETE_WINDOW',on_close)
# app.mainloop()
from customtkinter import *
from socket import *
from threading import Thread
from tkinter.messagebox import showerror, showinfo, askyesno
import random
from datetime import datetime
from time import sleep

# ------------------ Setup ------------------
set_appearance_mode("light")
set_default_color_theme("blue")

app_name = "Mohamed's server"
app = CTk()
username = StringVar()
app.geometry("1400x800")
app.title(app_name)
app.configure(fg_color="#f5f7fa")

sock = socket(AF_INET, SOCK_STREAM)
showed_users = set()
_username = ""

# ------------------ Frames ------------------
sidebar_frame = CTkFrame(app, width=300, fg_color="#2c3e50", corner_radius=0)
sidebar_frame.pack(side="left", fill="y", padx=(0, 10))

content_frame = CTkFrame(app, fg_color="#ffffff", corner_radius=12)
content_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

# ------------------ Online Users ------------------
online_users_header = CTkFrame(sidebar_frame, fg_color="#34495e", height=60, corner_radius=0)
online_users_header.pack(fill="x", pady=(0, 10))

CTkLabel(online_users_header, text="Online Users",
         font=("Arial", 20, "bold"), text_color="white").pack(expand=True, pady=15)

users_scrollable = CTkScrollableFrame(sidebar_frame, fg_color="transparent")
users_scrollable.pack(fill="both", expand=True, padx=10, pady=10)

# ------------------ User Cards ------------------
def create_user_card(parent, user):
    card = CTkFrame(parent, height=60, fg_color="#34495e", corner_radius=8)
    card.pack(fill="x", pady=5)

    colors = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6", "#1abc9c"]
    color = random.choice(colors)

    avatar = CTkLabel(card, text=user[0].upper(),
                      width=5, height=40,
                      fg_color=color,
                      text_color="white",
                      corner_radius=18,
                      font=("Arial", 16, "bold"))
    avatar.place(x=10, y=10)

    CTkLabel(card, text=user,
             font=("Arial", 14, "bold"),
             text_color="white").place(x=80, y=12)

    showed_users.add(user)
    return card


def refresh_user_cards(user_list):
    for widget in users_scrollable.winfo_children():
        widget.destroy()

    showed_users.clear()

    for u in user_list:
        if not u:
            continue
        display_name = "You" if u == _username else u
        create_user_card(users_scrollable, display_name)


# ------------------ Header & Chat ------------------
header_frame = CTkFrame(content_frame, fg_color="transparent", height=80)
header_frame.pack(fill="x", padx=30, pady=(30, 20))

CTkLabel(header_frame, textvariable=username,
         font=("Arial", 32, "bold"),
         text_color="#2c3e50").pack(side="left")

chat_frame = CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=12)
chat_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))

chat_header = CTkFrame(chat_frame, fg_color="#e9ecef", height=60, corner_radius=12)
chat_header.pack(fill="x", pady=(0, 5))

CTkLabel(chat_header, text="General Chat Room",
         font=("Arial", 18, "bold"),
         text_color="#2c3e50").pack(side="left", padx=20)

messages_frame = CTkScrollableFrame(chat_frame, fg_color="transparent")
messages_frame.pack(fill="both", expand=True, padx=10, pady=10)

# ------------------ Messages ------------------
def create_message_bubble(parent, message, is_own=False):
    bubble_frame = CTkFrame(parent, fg_color="transparent")
    bubble_frame.pack(fill="x", pady=8)

    if is_own:
        inner_frame = CTkFrame(bubble_frame, fg_color="transparent")
        inner_frame.pack(anchor="e")

        CTkLabel(inner_frame, text=message["time"],
                 font=("Arial", 10), text_color="#7f8c8d").pack(anchor="e", padx=(0, 10))

        bubble = CTkFrame(inner_frame, fg_color="#3498db", corner_radius=12)
        bubble.pack(anchor="e", pady=2)

        CTkLabel(bubble, text=message["text"],
                 font=("Arial", 14), text_color="white",
                 wraplength=400, justify="left").pack(padx=15, pady=10)

        CTkLabel(inner_frame, text="You",
                 font=("Arial", 12, "bold"),
                 text_color="#2c3e50").pack(anchor="e", padx=(0, 10))

    else:
        inner_frame = CTkFrame(bubble_frame, fg_color="transparent")
        inner_frame.pack(anchor="w")

        CTkLabel(inner_frame, text=message["sender"],
                 font=("Arial", 12, "bold"), text_color="#2c3e50").pack(anchor="w", padx=(10, 0))

        bubble = CTkFrame(inner_frame, fg_color="#e9ecef", corner_radius=12)
        bubble.pack(anchor="w", pady=2)

        CTkLabel(bubble, text=message["text"],
                 font=("Arial", 14), text_color="#2c3e50",
                 wraplength=400, justify="left").pack(padx=15, pady=10)

        CTkLabel(inner_frame, text=message["time"],
                 font=("Arial", 10), text_color="#7f8c8d").pack(anchor="w", padx=(10, 0))


# ------------------ Message Input ------------------
input_frame = CTkFrame(chat_frame, fg_color="transparent", height=70)
input_frame.pack(fill="x", padx=10, pady=10)

message_entry = CTkEntry(input_frame,
                         placeholder_text="Type your message here...",
                         font=("Arial", 14),
                         height=45,
                         corner_radius=20,
                         border_width=0,
                         fg_color="#e9ecef")
message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))


def send_message():
    message_text = message_entry.get()
    if message_text.strip():
        now = datetime.now()
        time_str = now.strftime("%H:%M %p")
        new_message = {"sender": _username, "text": message_text, "time": time_str}
        create_message_bubble(messages_frame, new_message, True)
        message_entry.delete(0, END)
        messages_frame._parent_canvas.yview_moveto(1.0)


send_button = CTkButton(input_frame,
                        text="Send",
                        command=send_message,
                        font=("Arial", 14, "bold"),
                        height=45,
                        width=100,
                        fg_color="#3498db",
                        hover_color="#2980b9",
                        corner_radius=20)
send_button.pack(side="right")

message_entry.bind("<Return>", lambda event: send_message())

# ------------------ Username Popup ------------------
def ask_username():
    popup = CTkToplevel(app)
    popup.title("Enter Username")
    popup.geometry("500x300")
    popup.resizable(False, False)
    popup.grab_set()
    popup.configure(fg_color="#f5f7fa")

    CTkLabel(popup, text="👤 Welcome!", font=("Arial", 22, "bold"), text_color="#2c3e50").pack(pady=(20, 10))
    CTkLabel(popup, text="Please enter your username to continue",
             font=("Arial", 14), text_color="#7f8c8d").pack(pady=(0, 20))

    username_entry = CTkEntry(popup, placeholder_text="Type your username...",
                              width=280, height=40, corner_radius=15,
                              font=("Arial", 14), fg_color="#ecf0f1")
    username_entry.pack(pady=10)

    button_frame = CTkFrame(popup, fg_color="transparent")
    button_frame.pack(pady=20)

    def confirm_username():
        global _username
        _username = username_entry.get().strip()
        if _username:
            username.set(f'Welcome, {_username}')
            sock.sendall(f'NEW-{_username}'.encode())
            popup.destroy()
        else:
            showinfo(title=app_name, message='Enter your username to continue')
            ask_username()

    def cancel():
        if askyesno(title=app_name, message='You cannot continue without username!'):
            app.destroy()
        else:
            popup.destroy()
            ask_username()

    CTkButton(button_frame, text="Confirm", command=confirm_username,
              fg_color="#3498db", hover_color="#2980b9",
              corner_radius=15, width=120, height=50,
              font=("Arial", 14, "bold")).pack(side="left", padx=10)

    CTkButton(button_frame, text="Cancel", command=cancel,
              fg_color="#e74c3c", hover_color="#c0392b",
              corner_radius=15, width=120, height=50,
              font=("Arial", 14, "bold")).pack(side="right", padx=10)

    username_entry.focus()


# ------------------ Close Event ------------------
def on_close():
    try:
        sock.send(f'CC-{_username}'.encode())
        sleep(0.8)
        sock.close()
    except:
        pass
    finally:
        sock.close()
        app.destroy()


# ------------------ Online Users ------------------
def add_users(user_list):
    return set([u.strip() for u in user_list if u.strip()])


def _refresh(u_list):
    app.after(0, lambda: refresh_user_cards(u_list))


# ------------------ Server Listener ------------------
def start_server():
    try:
        sock.connect(('127.0.0.1', 2222))
        ask_username()
        while True:
            get_o_users = sock.recv(1024).decode().strip()
            if not get_o_users:
                continue

            if get_o_users.startswith('OU:'):
                user_list = get_o_users.split(':')[1].split(',')
                rm_dup_u = add_users(user_list)
                Thread(target=_refresh, args=(rm_dup_u,), daemon=True).start()

            elif get_o_users == 'RU':
                showinfo(title=app_name, message='Server rejects you')

    except ConnectionRefusedError:
        showerror(title=app_name, message='Server is down, try again later')
    except ConnectionResetError:
        showerror(title=app_name, message='Server issue, try again')
    except Exception as e:
        print(e)


Thread(target=start_server, daemon=True).start()
app.protocol('WM_DELETE_WINDOW', on_close)
app.mainloop()
