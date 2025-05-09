from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ("Courier", 11, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = random_letters + random_symbols + random_numbers

    shuffle(password_list)
    password = "".join(password_list) #This joins all elements in the list
    password_entry.insert(0, password)
    pyperclip.copy(password) #This copies to the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """This function manages the input and saves it to a text file"""
    website_value = website_entry.get().title()
    email_value = email_entry.get()
    password_value = password_entry.get()

    if website_value == "" or password_value == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        #messagebox returns a boolean
        is_ok = messagebox.askokcancel(title=website_value,
                                       message=f"This are the details\nEmail: {email_value}\nPassword: {password_value}"
                                               f"\nIs it OK to save?")

        if is_ok: #if the return is true
            with open("data.txt", mode="a") as data:
                data.write(f"{website_value} | {email_value} | {password_value}\n")

            # This deletes the items in the entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(pady=50, padx=50, bg="white")

# Setting up Row 0
canvas = Canvas(width=200, height=200)
canvas.config(bg="white", highlightthickness=0)
img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Setting up Row 1
website = Label(text="Website:", font=FONT, bg="white")
website.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

# Setting up Row 2
email = Label(text="Email/Username:", font=FONT, bg="white")
email.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.insert(0, "gabrielomoso@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Setting up Row 3
password_label = Label(text="Password:", font=FONT, bg="white")
password_label.grid(row=3, column=0)

password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

generate_password = Button(text="Generate Password", bg="white", command=password_generator)
generate_password.grid(row=3, column=2)

# Setting up Row 4
add = Button(width=32, text="Add", bg="white", command=save)
add.grid(row=4, column=1, columnspan=2)

windows.mainloop()
