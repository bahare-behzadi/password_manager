import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

GREEN = "#9BE8D8"
FONT = ("time new roman", 12, "normal")


# ------------------------------ FIND PASSWORD  --------------------------------- #
def find():
    web = web_entry.get()
    try:
        with open("data.json") as data:
            temp_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="warning", message="there is no file")
    else:
        if web in temp_data:
            messagebox.showinfo(title="Your user and password",
                                message=f"email/username:{temp_data[web]['email/username']}"
                                        f"\npassword:{temp_data[web]['password']}")
        else:
            messagebox.showinfo(title="warning", message="you dont have password for this website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = web_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = {
        web: {
            "email/username": user,
            "password": password
        }
    }
    if web == "":
        messagebox.showinfo(title="warning", message="Website is empty, you can not leave any field empty")
    elif user == "":
        messagebox.showinfo(title="warning", message="user is empty, you can not leave any field empty")
    elif password == "":
        messagebox.showinfo(title="warning", message="password is empty, you can not leave any field empty")
    else:
        try:
            with open("data.json", "r") as data:
                temp_data = json.load(data)
        except FileNotFoundError or temp_data == "":
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            temp_data.update(new_data)
            with open("data.json", "w") as data:
                json.dump(temp_data, data, indent=4)
        finally:
            web_entry.delete(0, END)
            web_entry.focus()
            user_entry.delete(0, END)
            user_entry.insert(0, 'example@google.com')
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80, bg=GREEN)
window.iconbitmap("key_icon.ico")
canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
photo = PhotoImage(file="3.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)
web_label = Label(text="Website: ", bg=GREEN, highlightthickness=0, font=FONT)
web_label.grid(column=0, row=1)
web_entry = Entry(width=21, font=FONT)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=1)
search_button = Button(text="Search", font=FONT, width=16, command=find)
search_button.grid(column=2, row=1)
user_label = Label(text="Email/Username: ", bg=GREEN, highlightthickness=0, font=FONT)
user_label.grid(column=0, row=4)
user_entry = Entry(width=38, font=FONT)
user_entry.grid(column=1, row=4, columnspan=2)
user_entry.insert(0, "example@google.com")
pass_label = Label(text="Password: ", bg=GREEN, highlightthickness=0, font=FONT)
pass_label.grid(column=0, row=7)
pass_entry = Entry(width=21, font=FONT)
pass_entry.grid(column=1, row=7, columnspan=1)
pass_button = Button(text="Generate Password", font=FONT, command=generator)
pass_button.grid(column=2, row=7, columnspan=1)
add_button = Button(text="Add", width=38, font=FONT, command=save)
add_button.grid(column=1, row=9, columnspan=2)

window.mainloop()
