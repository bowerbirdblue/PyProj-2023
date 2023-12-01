# universal serial 🅱️us
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox
def open_app_win():
    app_win = tk.Tk()
    app_win.title("")
# creating the login (+submit/cancel buttons)
def submit_login():
    username = username_entry.get()
    password = username_entry.get()
    if username == "gid.l.ehk.tom" and password == "alcid.corv.0.111.00.11":
        messagebox.showinfo("Login Successful.", "Welcome to the Tomia.")

