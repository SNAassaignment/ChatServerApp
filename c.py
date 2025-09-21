from customtkinter import *
from socket import *
from threading import Thread
from tkinter.messagebox import showerror, showinfo, askyesno
import random
from datetime import datetime
from time import sleep

# ------------------ Config ------------------
SERVER_IP = "127.0.0.1"
SERVER_PORT = 2222

set_appearance_mode("light")
set_default_color_theme("blue")

app_name = "Mohamed's server (Client)"
app = CTk()
my_username = None            # string username
username_var = StringVar()    # for header label

app.geometry("1000x700")
app.title(app_name)
app.configure(fg_color="#f5f7fa")

sock = None
listener_thread = None
connected = False

# ------------------ UI Layout ------------------
# Sidebar frame for online users
sidebar_frame = CTkFrame(app, width=300, fg_color="#2c3e50", corner_radius=0)
sidebar_frame.pack(side="left", fill="y", padx=(0, 10))

# Main content frame
content_frame = CTkFrame(app, fg_color="#ffffff", corner_radius=12)
content_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

# Online users header
online_users_header = CTkFrame(sidebar_frame, fg_color="#34495e", height=60, corner_radius=0)
online_users_header.pack(fill="x", pady=(0, 10))
CTkLabel(online_users_header, text="Online Users", font=("Arial", 20, "bold"), text_color="white").pack(expand=True, pady=15)

users_scrollable = CTkScrollableFrame(sidebar_frame, fg_color="transparent")
users_scrollable.pack(fill="both", expand=True, padx=10, pady=10)

# Welcome header
header_frame = CTkFrame(content_frame, fg_color="transparent", height=80)
header_frame.pack(fill="x", padx=30, pady=(30, 20))
CTkLabel(header_frame, textvariable=username_var, font=("Arial", 28, "bold"), text_color="#2c3e50").pack(side="left")

# Chat area (simple message list)
chat_frame = CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=12)
chat_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))

chat_header = CTkFrame(chat_frame, fg_color="#e9ecef", height=60, corner_radius=12)
chat_header.pack(fill="x", pady=(0, 5))
CTkLabel(chat_header, text="General Chat Room", font=("Arial", 18, "bold"), text_color="#2c3e50").pack(side="left", padx=20)

messages_frame = CTkScrollableFrame(chat_frame, fg_color="transparent")
messages_frame.pack(fill="both", expand=True, padx=10, pady=10)

input_frame = CTkFrame(chat_frame, fg_color="transparent", height=70)
input_frame.pack(fill="x", padx=10, pady=10)

message_entry = CTkEntry(input_frame, placeholder_text="Type your message here...", font=("Arial", 14), height=45, corner_radius=20, border_width=0, fg_color="#e9ecef")
message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

def create_message_bubble(parent, message, is_own=False):
    bubble_frame = CTkFrame(parent, fg_color="transparent")
    bubble_frame.pack(fill="x", pady=8)
    if is_own:
        inner_frame = CTkFrame(bubble_frame, fg_color="transparent")
        inner_frame.pack(anchor="e")
        CTkLabel(inner_frame, text=message["time"], font=("Arial", 10), text_color="#7f8c8d").pack(anchor="e", padx=(0,10))
        bubble = CTkFrame(inner_frame, fg_color="#3498db", corner_radius=12)
        bubble.pack(anchor="e", pady=2)
        CTkLabel(bubble, text=message["text"], font=("Arial", 14), text_color="white", wraplength=400, justify="left").pack(padx=15, pady=10)
        CTkLabel(inner_frame, text="You", font=("Arial", 12, "bold"), text_color="#2c3e50").pack(anchor="e", padx=(0,10))
    else:
        inner_frame = CTkFrame(bubble_frame, fg_color="transparent")
        inner_frame.pack(anchor="w")
        CTkLabel(inner_frame, text=message["sender"], font=("Arial", 12, "bold"), text_color="#2c3e50").pack(anchor="w", padx=(10,0))
        bubble = CTkFrame(inner_frame, fg_color="#e9ecef", corner_radius=12)
        bubble.pack(anchor="w", pady=2)
        CTkLabel(bubble, text=message["text"], font=("Arial", 14), text_color="#2c3e50", wraplength=400, justify="left").pack(padx=15, pady=10)
        CTkLabel(inner_frame, text=message["time"], font=("Arial", 10), text_color="#7f8c8d").pack(anchor="w", padx=(10,0))

def send_message():
    text = message_entry.get().strip()
    if not text:
        return
    now = datetime.now()
    time_str = now.strftime("%H:%M %p")
    new_message = {"sender": my_username or "You", "text": text, "time": time_str}
    create_message_bubble(messages_frame, new_message, True)
    message_entry.delete(0, END)
    # send to server as raw text (server ignores non-protocol messages in current implementation)
    try:
        if sock and connected:
            sock.sendall(text.encode())
    except:
        pass
    # scroll
    try:
        messages_frame._parent_canvas.yview_moveto(1.0)
    except:
        pass

send_button = CTkButton(input_frame, text="Send", command=send_message, font=("Arial", 14, "bold"), height=45, width=100, fg_color="#3498db", hover_color="#2980b9", corner_radius=20)
send_button.pack(side="right")
message_entry.bind("<Return>", lambda ev: send_message())

# ------------------ helper UI functions ------------------
def clear_user_cards():
    # destroy children of users_scrollable
    for child in users_scrollable.winfo_children():
        child.destroy()

def create_user_card(parent, name):
    card = CTkFrame(parent, height=60, fg_color="#34495e", corner_radius=8)
    card.pack(fill="x", pady=5)
    colors = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6", "#1abc9c"]
    color = random.choice(colors)
    avatar = CTkLabel(card, text=name[0].upper(), width=5, height=40, fg_color=color, text_color="white", corner_radius=18, font=("Arial", 16, "bold"))
    avatar.place(x=10, y=10)
    CTkLabel(card, text=name, font=("Arial", 14, "bold"), text_color="white").place(x=80, y=12)
    return card

def update_user_list_in_ui(user_list):
    # schedule on main thread
    def _update():
        clear_user_cards()
        if not user_list:
            CTkLabel(users_scrollable, text="No users online", font=("Arial", 12), text_color="#ffffff").pack(pady=10)
            return
        for name in user_list:
            create_user_card(users_scrollable, name)
    app.after(0, _update)

# ------------------ Networking ------------------
def safe_close_sock():
    global sock, connected
    try:
        if sock:
            sock.close()
    except:
        pass
    sock = None
    connected = False

def listener():
    """Background thread to listen to server messages"""
    global connected
    try:
        while connected:
            data = sock.recv(1024)
            if not data:
                break
            msg = data.decode().strip()
            if msg.startswith("OU:"):
                payload = msg[3:].strip()
                # server sends space-separated usernames
                if payload == "":
                    user_list = []
                else:
                    user_list = payload.split(" ")
                update_user_list_in_ui(user_list)
            else:
                # any other text: show in chat area
                now = datetime.now().strftime("%H:%M %p")
                create_message_bubble(messages_frame, {"sender": "Server", "text": msg, "time": now}, False)
    except Exception as e:
        # connection dropped
        pass
    finally:
        safe_close_sock()
        # update UI to show no users
        update_user_list_in_ui([])

def start_connection_and_listen():
    """Connect to server and start listener; called after username entered"""
    global sock, connected, listener_thread
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((SERVER_IP, SERVER_PORT))
        connected = True
        # send S-username once we have my_username
        sock.sendall(f"S-{my_username}".encode())
        # start listener thread
        listener_thread = Thread(target=listener, daemon=True)
        listener_thread.start()
    except Exception as e:
        showerror("Connection Error", f"Could not connect to server: {e}")
        safe_close_sock()

# ------------------ Username popup ------------------
def ask_username_popup():
    popup = CTkToplevel(app)
    popup.title("Enter Username")
    popup.geometry("420x240")
    popup.resizable(False, False)
    popup.grab_set()
    popup.configure(fg_color="#f5f7fa")

    CTkLabel(popup, text="👤 Enter username", font=("Arial", 18, "bold"), text_color="#2c3e50").pack(pady=(20,10))
    entry = CTkEntry(popup, placeholder_text="Type your username...", width=300, height=40, corner_radius=10, font=("Arial", 14))
    entry.pack(pady=(0, 10))
    entry.focus()

    def confirm():
        global my_username
        name = entry.get().strip()
        if not name:
            showinfo("Required", "Please enter a username")
            return
        my_username = name
        username_var.set(f"Welcome, {my_username}")
        popup.destroy()
        # connect and send S-username (start background listener)
        start_connection_and_listen()

    def cancel():
        if askyesno("Exit", "You won't continue without a username. Exit app?"):
            app.destroy()
        else:
            popup.destroy()
            ask_username_popup()

    btn_frame = CTkFrame(popup, fg_color="transparent")
    btn_frame.pack(pady=10)
    CTkButton(btn_frame, text="Confirm", command=confirm, width=120, fg_color="#3498db").pack(side="left", padx=8)
    CTkButton(btn_frame, text="Cancel", command=cancel, width=120, fg_color="#e74c3c").pack(side="right", padx=8)

# ------------------ Close handling ------------------
def on_close():
    try:
        if connected and sock and my_username:
            try:
                sock.sendall(f"CC-{my_username}".encode())
            except:
                pass
            sleep(0.2)
    except:
        pass
    finally:
        safe_close_sock()
        app.destroy()

# ------------------ Start ------------------
# open username popup on start
app.after(200, ask_username_popup)
app.protocol("WM_DELETE_WINDOW", on_close)
app.mainloop()
