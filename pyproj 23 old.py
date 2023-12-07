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
    tk.Label(app_win, text="da title",font=('Arial', 50)).place(relx=0.5,rely=0, anchor="n")
    # event loop for the app win
    app_win.mainloop()
# creating a function to destroy root
def destroy():
    root.destroy()


# creating the login (+submit/cancel buttons)
username = []
password = []
def submit_login():
    setusername = username_entry.get()
    setpassword = password_entry.get()
    if setusername.isalnum() and setpassword.isalnum():
        username.insert(0, setusername)
        password.append(setpassword)
        messagebox.showinfo("Login Successful.", "Welcome to the Tomia.")
        messagebox.showinfo("Confirm", username + password)
        # destroy login window
        destroy()
        # call the app window function + open app window
        open_app_win()
    else:
        messagebox.showerror("Error", "Invalid username or password. Please try again.")
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

#Buttons
tk.Button(frame, text="Cancel", command=destroy).grid(row=5, column=0, padx=2, pady=10)
tk.Button(frame, text="Submit", command=submit_login).grid(row=5, column=1, padx=2, pady=10)


root.mainloop()
