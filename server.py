'''
Coordinates:
x-axis : horizontal
y-axis : vertical
'''
import customtkinter as ct
from colors import Colors
from base64 import b64decode
from tkinter import messagebox
from PIL import Image,ImageTk

title = 'Secure Chat Server'
root = ct.CTk()
color = Colors()
get_screen_size = (root.winfo_screenheight(),root.winfo_screenwidth())
root.title(title)
root.geometry(f'{get_screen_size[1]}x{get_screen_size[0]}')
root.resizable(True,True)
    
dashboard = Image.open('logo.png')
resized_image = dashboard.resize((200, 200))  # width, height
photo = ImageTk.PhotoImage(resized_image)

image_label = ct.CTkLabel(root, image=photo,text='')
image_label.place(x=0,y=0)

root.mainloop()