from customtkinter import *
from tkinter.messagebox import *
from threading import Thread
from socket import *
import sys

app = CTk()
app_name = 'mohamed screen'
app.title(app_name)
app.geometry('1920x1080')

user = ''

_man = StringVar(app)

def auto_refresh():
    show_online_users()
    # online.after(1000, show_online_users)
    app.update()

def ask_username():
    popup = CTkToplevel(app)
    popup.geometry("300x180")
    popup.title("Enter Username")
    popup.grab_set()

    label = CTkLabel(popup, text="Enter your username:")
    label.pack(pady=10)

    username_entry = CTkEntry(popup, placeholder_text="Username")
    username_entry.pack(pady=5)

    def reopen_window():
        popup.destroy()
        app.after(0,ask_username)

    def on_close():
        if askyesno(title=app_name,message='Do you want to close the app?'):
            app.after(100,close_app)

    def on_continue():
        global user 
        username = username_entry.get().strip()
        if username:
            user = username
            popup.destroy()
            gou = Thread(target=get_online_users, daemon=True)
            gou.start()
            main()
            auto_refresh()
        else:
            showwarning(title=app_name, message="Please enter a username!")
            reopen_window()

    continue_btn = CTkButton(popup, text="Continue", command=on_continue)
    continue_btn.pack(pady=15)

    popup.protocol('WM_DELETE_WINDOW',on_close)

def get_online_users():
    global on_users,server_status,sock
    on_users = []
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        sock.connect(('127.0.0.1', 2222))
        server_status = True
        sock.send(user.encode())
        while True:
            payloads = sock.recv(1024).decode().strip()
            if payloads == 'B':
                showerror(message='you are blocked from server')
                sock.close()
                server_status = False
                sys.exit()
            if payloads == 'MAX-ERR':
                showinfo(title=app_name,message='Maximum users in server. so sorry!')
                server_status = False
            else:
                on_users = payloads.split("\n")
                app.after(100,show_online_users)

    except ConnectionRefusedError:
        server_status = False
        showerror(title=app_name,message='Server is now off!')
        sock.close()

    except BrokenPipeError:
        server_status = False
        showerror(title=app_name,message='Server is now odsdsdsdsdsdsdff!')
        sock.close()

    except Exception as e:
        server_status = False
        showerror(title=app_name, message=f'Error : {str(e)}')

def send_():
    CTkLabel(
        chats_frame,
        text=f'{user}:{chat_box.get().strip()}',
        font=('Arial', 22)
    ).pack(anchor='nw', padx=10, pady=10)
    _man.set('')

def close_app():
    if askyesno(title=app_name,message='Do you want to exit?'):
        try:
            print(on_users)
            on_users.remove(user)
            print(on_users)
            sock.send(f'APP-CLOSE,{user}'.encode())
            app.destroy()
        except:
            pass

def _on_mouse_wheel(event):
    if event.num == 4:
        chats_frame._parent_canvas.yview_scroll(-3, "units")
    elif event.num == 5:
        chats_frame._parent_canvas.yview_scroll(3, "units")


def main():
    global chats_frame, chat_box, online
    toptab = CTkTabview(app)
    toptab.pack(fill='both', expand=True)

    home = toptab.add('Home')
    online = toptab.add('Online users')

    CTkLabel(home, text=f'Hi, {user}', font=('Arial', 33)).pack(pady=30)
    chats_frame = CTkScrollableFrame(home, fg_color='grey', width=1990, height=700)
    chats_frame.pack(padx=0, pady=5, fill="both", expand=True)

    chats_frame.bind_all("<Button-4>", _on_mouse_wheel)
    chats_frame.bind_all("<Button-5>", _on_mouse_wheel)

    chat_box = CTkEntry(home, font=('Arial', 22), width=1000, height=50, textvariable=_man)
    chat_box.pack(side="left", fill="x", expand=True, padx=(0, 10))

    send_btn = CTkButton(home, text="➤", width=100, height=50, font=('Arial', 28), state='disabled' if server_status == False else 'normal',command=send_)
    send_btn.pack(side="right")

shown_users = set()
user_positions = [0, 0]
def show_online_users():
    for widget in online.winfo_children():
        widget.destroy()

    r, c = 0, 0
    for u in on_users:
        label = CTkLabel(
            online,
            text='You' if u == user else u,
            fg_color='green',
            corner_radius=10,
            font=('Arial', 20),
            width=120,
            height=50
        )
        label.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")

        if c < 4: 
            c += 1
        else:
            r += 1
            c = 0

app.after(600,ask_username)
app.protocol('WM_DELETE_WINDOW',close_app)
app.mainloop()
