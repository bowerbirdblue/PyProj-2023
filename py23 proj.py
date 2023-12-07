# universal serial 🅱️us
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox
# creating the application window
def open_app_win():
    app_win = tk.Tk()
    app_win.title("TomSys")
    # window size
    app_win.geometry("1200x1000")
    #wiget
    tk.Label(app_win, text="da title",font=('Menlo', 25)).place(relx=0.5,rely=0, anchor="n")
    tk.Label(app_win, text="")
    # event loop for the app win
    app_win.mainloop()

# creating a function to destroy root
def destroy1():
    root.destroy()

# creating the login (+submit/cancel buttons)
username = []
password = []

captcha = ""      
def captcha_opener():
    captchawin = tk.Tk()
    captchawin.title("Captcha") 
    def destroy2():
        captchawin.destroy()
    def captcha_submitter():
        if captcha.isdigit():
            if int(captcha) == 4:
                destroy2()
                open_app_win()
    tk.Label(captchawin, text="Please complete the captcha.\n((11+3)*2)/7").grid(row=0,column=0)
    frame2 = ttk.Frame(captchawin)
    frame2.grid(row=2,column=0)
    captcha_entry = tk.Entry(captchawin)
    captcha_entry.grid(row=1,column=0)
    tk.Button(frame2, text="Cancel", command=destroy2).grid(row=2, column=0, padx=2, pady=10)
    tk.Button(frame2, text="Submit", command=captcha_submitter).grid(row=2, column=1, padx=2, pady=10)
    captcha = captcha_entry.get()
    captchawin.mainloop()


def submit_login():
    inv_char_p = ""
    inv_char_u = ""
    setusername = username_entry.get()
    setpassword = password_entry.get()
    if setusername.isalnum() and setpassword.isalnum():
        username.insert(0, setusername)
        password.append(setpassword)
        messagebox.showinfo("Confirm Credentials", f"Username: {username}\nPassword: {password}")
        messagebox.showinfo("Login Successful.", "Please complete the Captcha.")
        # destroy login window
        destroy1()
        captcha_opener()
        

    else:
        for smth in setusername:
            if smth.isalnum():
                pass
            else:
                inv_char_u += smth
        for smth in setpassword:
            if smth.isalnum():
                pass
            else:
                inv_char_p += smth
        messagebox.showerror("Error - Invalid Username or Password", f"Invalid Characters (Usr): {inv_char_u}" + f"\nInvalid Characters (Pwd): {inv_char_p}")
    return setusername, setpassword             
root = tk.Tk()
root.title("TomSys Login")

# username/password labels
frame = ttk.Frame(root)

frame.grid(row=5,column=0)
frame['relief'] = 'flat'
tk.Label(root, text="Please set your username and password and login to continue.").grid(row=0,column=0,padx=10,pady=5)
tk.Label(root, text="Username:").grid(row=1, column=0, padx=1, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=2, column=0, padx=1, pady=5)
tk.Label(root, text="Password:").grid(row=3, column=0, padx=1, pady=5)
password_entry = tk.Entry(root, show = "*")
password_entry.grid(row=4, column=0, padx=1, pady=5)
# captcha labels/buttons

#Buttons (in the login win)
tk.Button(frame, text="Cancel", command=destroy1).grid(row=5, column=0, padx=2, pady=10)
tk.Button(frame, text="Submit", command=submit_login).grid(row=5, column=1, padx=2, pady=10)
root.mainloop()
