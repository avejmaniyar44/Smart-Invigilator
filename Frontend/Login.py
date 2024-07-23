import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from FirebaseConn import auth
import tkinter as tk
from Dashboard import Dashboard
import requests

# def show_instruction_frame():
#     login_frame.pack_forget()
#     instruction_frame.pack()
    
                                        
def internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False    
# if internet_connection():
#     print("The Internet is connected.")
# else:
#     print("The Internet is not connected.")

# Place Holder Logic
def on_entry_click_username(event):
    if username.get() == "Username":
        username.delete(0, tk.END)
        username.config(fg='black')
        
def on_focusout_username(event):
    if username.get() == '':
        username.insert(0, "Username")
        username.config(fg='grey')
        
def on_entry_click_password(event):
    if password.get() == "Password":
        password.delete(0, tk.END)
        password.config(fg='black')

def on_focusout_password(event):
    if password.get() == '':
        password.insert(0, "Password")
        password.config(fg='grey')

def toggle_password():
    if show_password_var.get():
        password.config(show='')
    else:
        password.config(show='*')
        
def signin():
    User=username.get()
    Pass=password.get()
    if internet_connection():
        try:
            login= auth.sign_in_with_email_and_password(User,Pass)
            print("login Sucess!")
            root.destroy()
            # open_dashboard(User)
            Dashboard(User)
        except:
            print("failed")
            messagebox.showerror('Login Error', 'Error: Username or Password Incorrect')
    else:
        messagebox.showerror('Connection Error', 'Please check your internet connection!')


root = tk.Tk()
# FullScreenApp(root)
# self.dashboard_window.attributes('-fullscreen',True)
# root.attributes('-fullscreen',True)
root.title('ExamSecurePlatform (SEP)')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


# Dashboard image
image = Image.open('D:/SEP/Frontend/Assets/Login/login.jpg')
image = image.resize((390, 350), Image.LANCZOS)
img = ImageTk.PhotoImage(image)
label = tk.Label(root, image=img, bg='white')
label.place(x=50, y=68)

frame = tk.Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading= tk.Label(frame,text='Sign in', fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=130,y=5)


# UserName Textfield
username = tk.Entry(frame, width=25,fg='black', border=0, bg='white',font=('Microsoft YaHei UI Light',11))
username.place(x=30,y=80)
username.insert(0,'Username')
username.bind('<FocusIn>', on_entry_click_username)
username.bind('<FocusOut>', on_focusout_username)
tk.Frame(frame,width=950, height=2,bg='black').place(x=25,y=107)


# Password Field 
password = tk.Entry(frame, width=25,fg='black', border=0,show="*",bg='white',font=('Microsoft YaHei UI Light',11))
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>', on_entry_click_password)
password.bind('<FocusOut>', on_focusout_password)
tk.Frame(frame,width=950, height=2,bg='black').place(x=25,y=177)


show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(frame,border=0, text="Show Password",fg='black',bg='white',variable=show_password_var, command=toggle_password)
show_password_checkbox.place(x=25,y=190)


# Login Button 
tk.Button(frame,width=39,pady=7,text="Sign in",bg='#57a1f8',fg='white',border=0,command=signin).place(x= 50,y=250)

# label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
# label.place(x=75,y=270)

# sign_up = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
# sign_up.place(x=215,y=270)

root.mainloop()