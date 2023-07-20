from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

GREEN = "#9BE8D8"
FONT = ("time new roman", 13, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] +\
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
    if web == "":
        messagebox.showinfo(title="warning", message="Website is empty, you can not leave any field empty")
    elif user == "":
        messagebox.showinfo(title="warning", message="user is empty, you can not leave any field empty")
    elif password == "":
        messagebox.showinfo(title="warning", message="password is empty, you can not leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"The data which you entered is:\nEmail/username:"
                                                              f"{user}\npassword: {password}\nis it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{web} | {user} | {password} |\n")
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
web_entry = Entry(width=38, font=FONT)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)
user_label = Label(text="Email/Username: ", bg=GREEN, highlightthickness=0, font=FONT)
user_label.grid(column=0, row=2)
user_entry = Entry(width=38, font=FONT)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "example@google.com")
pass_label = Label(text="Password: ", bg=GREEN, highlightthickness=0, font=FONT)
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=21, font=FONT)
pass_entry.grid(column=1, row=3, columnspan=1)
pass_button = Button(text="Generate Password", font=FONT, command=generator)
pass_button.grid(column=2, row=3, columnspan=1)
add_button = Button(text="Add", width=32, font=FONT, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
