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
    # event loop for the app win
    app_win.mainloop()
# creating a function to destroy root
def destroy():
    root.destroy()

# creating the login (+submit/cancel buttons)

def submit_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "a" and password == "b":
        messagebox.showinfo("Login Successful.", "Welcome to the Tomia.")
        # destroy login window
        destroy()
        # call the app window function + open app window
        open_app_win()
    else:
        messagebox.showerror("Error", "Invalid username or password. Please try again.")
                
root = tk.Tk()
root.title("TomSys")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show = "*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Cancel", command=destroy).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(root, text="Submit", command=submit_login).grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()
