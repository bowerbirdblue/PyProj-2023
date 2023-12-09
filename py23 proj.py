# universal serial 🅱️us
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox
# creating the application window
def open_app_win():
    # creating app_win
    app_win = tk.Tk()
    app_win.title("TomSys")
    # window size
    app_win.geometry("1200x1000")
    # pre-setting profile vars
    firstname = ""
    lastname = ""
    ageyear = ""
    agemonth = ""
    usrpronoun = ""
    # submit command button

    # profile setting widgets
    frame = tk.Frame(app_win)
    frame.place(x=0,y=0,height=800, width=1200)
    frame["relief"]="groove"
    while True:
        # flavor text (title etc)
        tk.Label(app_win, text="TomSys SetProfile",font=('Menlo',20)).place(relx=0.5,rely=0, anchor="n")
        tk.Label(frame, text="Welcome. Please complete your profile.",font=('Menlo',18)).place(relx=.5, rely=.05, anchor="n")
        # first name
        tk.Label(frame, text="First Name:", font=('Menlo',15)).place(relx=.3, rely=.16, anchor="w")
        fname_entry = tk.Entry(frame)
        fname_entry.place(relx=.3,rely=.19,anchor="w")
        # last name
        tk.Label(frame, text="Last Name:", font=('Menlo',15)).place(relx=.3,rely=.23,anchor="w")
        lname_entry = tk.Entry(frame)
        lname_entry.place(relx=.3,rely=.26,anchor="w")
        # age (years)
        tk.Label(frame, text="Age (Years):", font=('Menlo',15)).place(relx=.7,rely=.16,anchor="e")
        yrage_entry = tk.Entry(frame)
        yrage_entry.place(relx=.7,rely=.19,anchor="e")
        # age (months)
        tk.Label(frame, text="Age (Addl. Months):",font=('Menlo',15)).place(relx=.7,rely=.23,anchor="e")
        mnage_entry = tk.Entry(frame)
        mnage_entry.place(relx=.7,rely=.26,anchor="e")
        # pronouns
        tk.Label(frame, text="Pronouns:", font=('Menlo', 15)).place(relx=.5, rely=.46,anchor="center")
        current_var = tk.StringVar()
        current_value = current_var.get()
        prncombo = ttk.Combobox(frame, state="readonly", textvariable=current_var)
        prncombo['values'] = ("He/Him/His", "She/Her/Hers", "They/Them/Theirs", "Other")
        prncombo.place(relx=.5, rely=.50,anchor="center")
        tk.Label(frame, text="If 'Other', please specify here.", font=('Menlo', 12)).place(relx=.5,rely=.56,anchor='center')
        prnother = tk.Entry(frame)
        prnother.place(relx=.5,rely=.6, anchor='center')
        # actually assigning profile vars
        firstname = fname_entry.get()
        lastname = lname_entry.get()
        ageyear = yrage_entry.get()
        agemonth = mnage_entry.get()
        def submit_profile():
            messagebox.showinfo("Profile Confirm", f"First Name: {fname_entry.get()}\tLast Name: {lname_entry.get()}\nAge: {yrage_entry.get()} years {mnage_entry.get()} months\nPronouns: {prncombo.get()}")
            frame.destroy()  
        tk.Button(frame, text="Submit",font=('Menlo', 12), command=submit_profile).place(relx=.5,rely=.7,anchor="center")
        break
    
    # event loop for the app win   
    app_win.mainloop()

# creating a function to destroy root
def destroy1():
    root.destroy()
# creating the login (+submit/cancel buttons)
username = []
password = []
def submit_login():
    inv_char_p = ""
    inv_char_u = ""
    setusername = username_entry.get()
    setpassword = password_entry.get()
    if setusername.isalnum() and setpassword.isalnum():
        username.insert(0, setusername)
        password.append(setpassword)
        messagebox.showinfo("Confirm Credentials", f"Username: {username}\nPassword: {password}")
        messagebox.showinfo("Login Successful.", "Welcome to the System of the Starship Tomia.")
        # destroy login window
        destroy1()
        open_app_win()
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
tk.Label(root, text="Please set your username and password and login to continue.", font=('Menlo')).grid(row=0,column=0,padx=10,pady=5)
tk.Label(root, text="Username:", font=('Menlo')).grid(row=1, column=0, padx=1, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=2, column=0, padx=1, pady=5)
tk.Label(root, text="Password:", font=('Menlo')).grid(row=3, column=0, padx=1, pady=5)
password_entry = tk.Entry(root, show = "*")
password_entry.grid(row=4, column=0, padx=1, pady=5)
#Buttons (in the login win)
tk.Button(frame, text="Cancel", font=('Menlo'), command=destroy1).grid(row=5, column=0, padx=2, pady=10)
tk.Button(frame, text="Submit", font=('Menlo'), command=submit_login).grid(row=5, column=1, padx=2, pady=10)
root.mainloop()
