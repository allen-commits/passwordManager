from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_pass():
    """Generates a password, then prints it to the console and the password entry field."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # The below 3 lines of code uses list comprehension to replace cumbersome for loops
    # Remember: new_list = [the_action for item in list or range]
    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for number in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers  # combines the lists into a single list

    random.shuffle(password_list)  # shuffles the characters of the list

    user_password = "".join(password_list)  # join method that converts the list into a string.

    email_entry.delete(0, END)  # clears the password box
    email_entry.insert(0, user_password)  # adds the password into the box
    pyperclip.copy(user_password)  # copies the password into the users clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    """This method saves the data to the file, and then clears the entries."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    record = f"{website},{email},{password}\n"
    json_data = {
        website: {
            "email": email,
            "password": password
        }}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:  ##checking for empty fields
        messagebox.showerror(title="Error", message="No empty fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "a") as data_file:
                json.dump(json_data, data_file, indent=2)
        else:
            # Updating old data with new data
            data.update(json_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=2) #the .dump method "dumps" the data into a file.
        finally:
            website_entry.delete(0, END)  # this clears or deletes the entries.
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- Search --------------------------------- #

def search():
    pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()  # creates a window from the tkinter class
window.title("Password Manager")
window.config(padx=50, pady=50, bg="WHITE")

canvas = Canvas(width=200, height=200, bg="WHITE", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="WHITE")
website_label.grid(column=0, row=1)

website_entry = Entry(width=34)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

search_button = Button(text="Search", command=search, width=14)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:", bg="WHITE")
email_label.grid(column=0, row=2)

email_entry = Entry(width=34)
email_entry.grid(column=1, row=2, columnspan=1)
email_entry.insert(0, "")  # automatically insert your email at the beginning.

password_label = Label(text="Password:", bg="WHITE")
password_label.grid(column=0, row=3)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

gen_pass_button = Button(text="Generate Password", command=generate_pass)
gen_pass_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=45, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
