'''
Coordinates:
x-axis : horizontal
y-axis : vertical
'''
import customtkinter as ct
from colors import Colors
from base64 import b64encode
from tkinter import messagebox
from public import Public

title = 'Secure Chat Server'
root = ct.CTk()
color = Colors()
get_screen_size = (root.winfo_screenheight(),root.winfo_screenwidth())
root.title(title)
root.geometry(f'{get_screen_size[1]}x{get_screen_size[0]}')
root.resizable(True,True)

_username = ct.StringVar()
_password = ct.StringVar()

def check_inputs():
    if len(_username.get().strip()) == 0 or len(_password.get().strip()) == 0:
        enter.configure(state='disabled')
    else:
        enter.configure(state='normal')
    
    root.after(200, check_inputs)

def login():
    get_username = _username.get().strip()
    get_password = _password.get().strip()

    if b64encode(get_username.encode()) == b'U05B' and b64encode(get_password.encode()) == b'U05B':
        Public().credentials.append(get_username.encode())
        Public().credentials.append(get_password.encode())
        messagebox.showinfo(title=title,message='Login success')
    if b64encode(get_username.encode()) != b'U05B' and b64encode(get_password.encode()) != b'U05B':
        messagebox.showerror(title=title,message='UnAutherized access')
    elif b64encode(get_username.encode()) != b'U05B':
        messagebox.showerror(title=title,message='Invalid username')
    elif b64encode(get_password.encode()) != b'U05B':
        messagebox.showerror(title=title,message='Invalid password')
    

login_banner = ct.CTkLabel(root,text='Login',font=('Arial',70))
login_banner.place(x=820,y=210)

username = ct.CTkEntry(root,text_color=color.DARK_GREEN,width=300,height=50,font=('Arial',20),placeholder_text='Enter autherized username',textvariable=_username)
username.place(x=770,y=340)

password = ct.CTkEntry(root,width=300,height=50,font=('Arial',20),show='#',placeholder_text='Enter autherized password',textvariable=_password)
password.place(x=770,y=410)

enter = ct.CTkButton(root,text='Submit',width=100,height=40,font=('Arial',20),fg_color=color.DARK_GREEN,command=login)
enter.place(x=860,y=490)

check_inputs()

root.mainloop()