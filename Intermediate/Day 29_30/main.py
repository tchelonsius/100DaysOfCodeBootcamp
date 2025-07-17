import tkinter as tk
from tkinter import messagebox
import random_password
import pyperclip
import json
import os
import sys


# gets the real path of files, so that they can be included in the exe files.
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def login():
    # global pw_given
    with open("data.json") as file:
        values = json.loads(file.read())
        if values["pw_access"]["password"] != login_input.get():
            pw_given = ""
            login_input.delete(0,'end')
            return
    frame1.grid_remove()
    frame2.grid(column=0, row=0)

# --------------------------------- SEARCH -------------------------------------- #
def search():
    try:
        with open("data.json") as file:
            all_values = json.loads(file.read())
            try:
                info = all_values[website_input.get()]
            except KeyError:
                messagebox.showinfo(title=f"Search request not found",message="This account has not been registered yet.")
            else:
                messagebox.showinfo(title=website_input.get(),message=f"email: {info['email']}\npassword: {info['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title=f"Search request not found", message="This account has not been registered yet.")


# -------------------------- OTHER FUNCTIONALITIES ------------------------------ #
def empty_fields_check():
    if website_input.get()=="" or email_input.get()=="" or password_input.get()=="":
        messagebox.showinfo(title="Empty Inputs", message="Please insert values in all fields!")
        return True
    return False
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    if password_input.get() != "":
        password_input.delete(0, "end")
    password = random_password.password()
    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if empty_fields_check():
        return
    values_check = messagebox.askokcancel(title=website_input.get(), message=f"Confirm the values given"+" "*10+"\n\n"
                                                    f"Email: {email_input.get()}\nPassword: {password_input.get()}")
    if not values_check:
        return

    new_data = {
        website_input.get(): {
            "email": email_input.get(),
            "password": password_input.get()
        }
    }
    try:
        with open("data.json", "r") as data_file:
            original = json.load(data_file)
            original.update(new_data)
    except FileNotFoundError:
        original = new_data
    finally:
        with open("data.json", "w") as data_file:
            json.dump(original, data_file, indent=4)
        # file.write(f"{website_input.get()} / {email_input.get()} / {password_input.get()} \n")
    website_input.delete(0,'end')
    password_input.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=40, pady=30)
# window.iconbitmap("images/icon.ico")

frame1 = tk.Frame(window, padx=100, pady=100)
frame2 = tk.Frame(window)



""" FRAME 1 WIDGETS """
# Password Label
login_label = tk.Label(frame1,text="Enter your access code: ", font=("Courier",15,"bold"))
login_label.config(pady=10)
login_label.grid(column=0,row=0)

empty_label = tk.Label(frame1, text="")
empty_label.grid(column=0,row=2)

# Password Input
login_input = tk.Entry(frame1, width=15, show="*")
login_input.grid(column=0,row=1)
login_input.focus()



# Enter Button
enter_button = tk.Button(frame1,text="Enter", command=login, width=10)
enter_button.grid(column=0,row=3)



""" FRAME 2 WIDGETS """
# Background Image
canvas = tk.Canvas(frame2, width=200,height=189)
bg_image_path = get_resource_path("images/logo.png")
bg_image = tk.PhotoImage(file=bg_image_path)
canvas.create_image(60,100, image=bg_image)
canvas.grid(column=1,row=0, columnspan=2)

# Labels
website_label = tk.Label(frame2, text="Website:", width=15)
website_label.grid(column=0, row=1)

email_label = tk.Label(frame2,text="Email/Username:", width=15)
email_label.grid(column=0, row=2)

password_label = tk.Label(frame2,text="Password:", width=15)
password_label.grid(column=0,row=3)

# Inputs
website_input = tk.Entry(frame2,width=28)
website_input.grid(column=1,row=1)
website_input.focus()

email_input = tk.Entry(frame2,width=47)
email_input.insert(0, "name@email.com")
email_input.grid(column=1,row=2, columnspan=2)

password_input = tk.Entry(frame2,width=28)
password_input.grid(column=1,row=3)

# Buttons
search_button = tk.Button(frame2,text="Search", width=14, command=search, background="#D66A50")
search_button.grid(column=2, row=1)

generate_button = tk.Button(frame2,text="Generate Password", width=14, command=generate_password, background="#D66A50")
generate_button.grid(column=2,row=3)

add_button = tk.Button(frame2,text="Add", width=39, command=save_password, background="#D66A50")
add_button.grid(column=1,row=4, columnspan=2)



frame1.grid(column=0,row=0, sticky="nsew")
frame2.grid(column=0,row=0, sticky="nsew")
frame2.grid_remove()

window.mainloop()