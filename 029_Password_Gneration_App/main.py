from json import JSONDecodeError
from tkinter import  *
from tkinter import  messagebox
from random import randint, choice
import json
import pyperclip
COLOR = "#9ACBD0"
GRAY = "#F4D793"
GREEN = "#889E73"
FONT = ("Times New Roman", 12 , "bold" )


# password generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    password = "".join(password_list)

    pyperclip.copy(password)   # copying to the clip board

    entry_password.insert(0, f"{password}")


# saving the password
def save_file():
    with open("data.json", "r") as data_file:
        data1 = json.load(data_file)
    website_name = entry_website.get()
    if website_name in data1:
        messagebox.showwarning(title="Same website", message="Same website name already present")
    user_name = entry_email_user.get()
    password_gen = entry_password.get()
    new_json_data = {
        website_name:{
            "User Name": user_name,
            "Password": password_gen,
    }}
    if len(website_name) == 0 or len(password_gen) == 0:
        messagebox.showerror(title="Error!", message= "Empty Fields")
    else:
        satisfied = messagebox.askokcancel(title="Entry Satisfaction",message=f" Are you satisfied with your entry?\n The website name is:{website_name}\n"
                                     f" The email or username is: {user_name}\n The password is: {password_gen}")
        if satisfied:
                try:
                    with open("data.json", "r") as data_file:
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("data.json", "w") as data_json:
                        json.dump(new_json_data, data_json, indent= 4)
                        print("Json added")
                except JSONDecodeError:
                    with open("data.json", "w") as data_json:
                        json.dump(new_json_data, data_json, indent= 4)
                        print("Json added")
                else:
                    data.update(new_json_data)
                    with open("data.json", "w") as data_file:
                        # print(data)
                        json.dump(data, data_file, indent= 4)
                finally:
                    print("Values added successfully")
                    entry_website.delete(0, END)
                    entry_email_user.delete(0, END)
                    entry_email_user.insert(0, "@gmail.com")
                    entry_password.delete(0, END)
                    messagebox.showinfo("Success", "Data inserted successfully!")


# Searching the username and password for the website in the json file using the name of website
def search():
    search_value = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load((data_file))
    except FileNotFoundError:
        messagebox.showerror(title="No File", message="No json file available!!")
    except JSONDecodeError:
        messagebox.showerror(title="Empty File", message="The Json file is empty!!")
    else:
        try:
            email = data[search_value]["User Name"]
            password = data[search_value]["Password"]
        except KeyError:
            messagebox.showerror(title="No Data", message="Website with name not available")
        else:
            messagebox.showinfo(title=f"{search_value}", message= f'The user_name is: {email}\n The password is: {password}')


# setting the UI
window = Tk()
window.title("Password Generator App")
window.config(padx=50, pady=50,bg= COLOR)

canvas_img = Canvas(height=200, width=200)
canvas_img.config(bg=COLOR, highlightthickness = 0)
photo = PhotoImage(file = "logo.png")
canvas_img.create_image(100,100, image = photo)
canvas_img.grid(row = 0, column = 1)

website_label = Label(text= "Website", font= FONT, bg = COLOR )
website_label.grid(row = 1 , column = 0, pady = 3 )

entry_website = Entry(width= 37, bg = GRAY, highlightthickness = 0)
entry_website.grid(row = 1, column = 1, pady = 3)
entry_website.focus()

search = Button(text="Search", width= 18, height= 1, bg = GREEN, highlightthickness = 0, command=search)
search.grid(column = 2, row = 1)

Email_User_label = Label(text= "Email/Username:", font= FONT, bg = COLOR  )
Email_User_label.grid(row = 2 , column = 0, pady = 3 )

entry_email_user = Entry(width= 60, bg = GRAY, highlightthickness = 0)
entry_email_user.insert(0, "@gmail.com")
entry_email_user.grid(row = 2, column = 1, columnspan = 2, pady = 3)

password_label = Label(text= "Password:", font= FONT, bg = COLOR  )
password_label.grid(row = 3, column = 0, pady = 3)

entry_password = Entry(width= 37, bg = GRAY, highlightthickness = 0)
entry_password.grid(row = 3, column = 1, pady = 3)

button_gen_pass = Button(text="Generate Password", width= 18, height= 1, bg = GREEN, highlightthickness = 0, command= generate_password)
button_gen_pass.grid(row = 3, column = 2, pady = 3)

button_Add_pass = Button(text = "Add", width = 51, bg = GREEN, highlightthickness = 0, command=save_file)
button_Add_pass.grid(row = 4, column = 1, columnspan = 2, pady = 3)

window.mainloop()