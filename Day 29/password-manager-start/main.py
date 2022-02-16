from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pass():
    password_entry.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letter = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pass_letter + pass_symbol + pass_number
    random.shuffle(password_list)

    passss = ''.join(password_list)
    password_entry.insert(0, passss)
    return passss

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_out():
    web = website_entry.get()
    email = email_entry.get()
    passw = password_entry.get()
    new_data = {
        web: {
            'email': email,
            'password': passw
        }
    }

    if not web or not email or not passw:
        messagebox.askyesno(title='Error!', message='You have not entered all required information. \n Please go back try again.')
    else:
        is_ok = messagebox.askokcancel(title=web, message=f'You have entered: {email}\n {passw}\n Is it OK to save?')
        if is_ok:
            try:
                with open('data.json', 'r') as f:
                    da = json.load(f)
                    da.update(new_data)
            except FileNotFoundError:
                with open('data.json', 'w') as f:
                    json.dump(new_data, f, indent=4)
            else:
                with open('data.json', 'w') as f:
                    json.dump(da, f, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


def search_in_json():
    input_key_data = website_entry.get()
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title='Not Found!', message='Not Found! Please Try Other Domain!')
    else:
        if input_key_data in data.keys():
            messagebox.showinfo(title='Search Results', message=f'{data[input_key_data]["email"]}, {data[input_key_data]["password"]}')
        else:
            if not input_key_data:
                messagebox.showinfo(title='Search Results', message='Please Type a Domain.')
            else:
                messagebox.showinfo(title='Search Results', message=f'Not Found {input_key_data} in Records.')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
# window.minsize(width=400, height=400)
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, 'mikerock332@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
generate_pass = Button(text='Generate Password', command=generate_pass)
generate_pass.grid(row=3, column=2, columnspan=2)
add_button = Button(text='Add', width=36, command=write_out)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text='Search', command=search_in_json, width=13, height=1)
search_button.grid(row=1, column=2)


window.mainloop()