from customtkinter import *
from tkinter.messagebox import *
from json import load,dump

app = CTk()
app.title('mohamed screen')
app.geometry('1920x1080')

_message_man = StringVar(app)

def set_user():
    with open('userinfo.json','w') as conf:
        data = {'username':name.get()}
        try:
            dump(data,conf,indent=4)
            showinfo(title='info',message='new user updated')
            first_frame.destroy()
        except:
             showerror(title='error',message='failed to update user')
    conf.close()

def get_user():
    with open('userinfo.json','r') as conf:
        return load(conf)['username']
    conf.close()

def send_message():
    CTkLabel(chats_frame,text=f'{get_user()}:{chat_box.get().strip()}',font=('Arial',22)).pack(anchor='nw',padx=10,pady=10)
    _message_man.set('')

def main():
    global chats_frame,chat_box
    toptab = CTkTabview(app)
    toptab.pack(fill='both',expand=True)

    home = toptab.add('Home')
    online = toptab.add('Online users')

    CTkLabel(home,text=f'Hi, {get_user()}',font=('Arial',33)).pack(pady=30)
    chats_frame = CTkScrollableFrame(home,fg_color='grey',width=1990,height=700)
    chats_frame.pack(padx=0, pady=5,fill="both", expand=True)
    canvas = chats_frame._parent_canvas
    canvas.bind("<Enter>", lambda e: canvas.focus_set())
    canvas.bind("<Button-4>", lambda e: canvas.yview_scroll(-3, "units"))  # scroll up
    canvas.bind("<Button-5>", lambda e: canvas.yview_scroll(3, "units"))   # scroll down

    chat_box = CTkEntry(home, font=('Arial',22), width=1000, height=50,textvariable=_message_man)
    chat_box.pack(side="left", fill="x", expand=True, padx=(0,10))

    send_btn = CTkButton(home, text="➤", width=100, height=50,font=('Arial',28),command=send_message)
    send_btn.pack(side="right")

with open('userinfo.json') as conf:
    user = load(conf)
    
    if user['username'] == 'mohamed':
        # showinfo(title='',message='username is found')
        main()
    else:
        first_frame = CTkFrame(app,corner_radius=7,width=800,height=700,fg_color='green')
        first_frame.pack(expand=True)
        first_frame.pack_propagate(False)

        intro = CTkLabel(first_frame,text='Welcome to chat app',font=('Arial',42))
        intro.pack(pady=100)

        intro = CTkLabel(first_frame,text='enter your name to continue',font=('Arial',32))
        intro.pack(pady=14)

        name = CTkEntry(first_frame,width=500,height=50,font=('Arial',22))
        name.pack(pady=37)

        submit = CTkButton(first_frame,width=200,height=50,text='Continue',font=('Arial',22),fg_color='grey',command=set_user)
        submit.pack(pady=20)
conf.close()


app.mainloop()
