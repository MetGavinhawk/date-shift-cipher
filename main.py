
from tkinter import *
window = Tk()

#sets the button status
button_status = IntVar()
button_status.set(0)

#explantion of what the program does
explantion = Label(window, text="This program will encrypt or decrypt messages using a date shift cipher")
explantion.grid(row=0, column=0, columnspan=3)

#creates the letter dictionary
letter_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

#takes the users message
users_message_entry = Entry(window, width=30)
users_message_entry.insert(0, "Enter the message here")
users_message_entry.grid(row=3, column=1)

#actully gets the date
users_date_entry = Entry(window, width=13)
users_date_entry.insert(0, "Enter date here")
users_date_entry.grid(row=6, column=1)

def disable_message_submit_button():
    submit_message_button.config(state="disabled")

def disable_button_and_get_date():
    submit_date_button.config(state="disabled")

def convert_users_date():
    users_date = list(users_date_entry.get())
    for i in range(2):
        users_date.remove("/")
    return users_date

#submit buttons
submit_message_button = Button(window, text="Submit", command=disable_message_submit_button, anchor="center")
submit_message_button.grid(row=4, column=1)
submit_date_button = Button(window, text="Submit", command=disable_button_and_get_date, anchor="center")
submit_date_button.grid(row=7, column=1)

#tells the user how to format the date
users_date_warning = Label(window, text="Use day/month/year format. Eg:03/04/2025")
users_date_warning.grid(row=5, column=1)

#Allows the user to decrypt or encrypt
encryption_radio_button = Radiobutton(window, text="Encrypt", variable=button_status, value=1)
decryption_radio_button = Radiobutton(window, text="Decrypt", variable=button_status, value=2)
encryption_radio_button.grid(row=2, column=0)
decryption_radio_button.grid(row=2, column=2)
encryption_or_decryption_label = Label(window, text="To encrypt select 'Encrypt', to decrypt select 'Decrypt'", anchor="center")
encryption_or_decryption_label.grid(row=1, column=0, columnspan=3)

def check_buttons():
    if submit_message_button.cget('state') == "disabled" and submit_date_button.cget("state") == "disabled" and ((button_status.get() == 1) == True or (button_status.get() == 2) == True):
        encryption_and_decryption()
    else:
        window.after(100, check_buttons)

check_buttons()

#does the encryption and or decryption
def encryption_and_decryption():
    global returning_string_label
    loop_num = 0
    returning_list = []
    message_string = users_message_entry.get()
    message_string = str(message_string).lower()
    message_list = list(message_string)
    converted_user_date = convert_users_date()
    if button_status.get() == 1:
        for item in message_list:
            if item != " " and loop_num < 8:
                value = letter_dictionary.get(item.lower()) + int(converted_user_date[loop_num])
                if value > 26:
                    value = 0 + (value-26)
                letter = [key for key, place in letter_dictionary.items() if place == value]
                returning_list.extend(letter)
                loop_num += 1
            elif item != " " and loop_num == 8:
                loop_num = 0
                value = letter_dictionary[item.lower()] + int(converted_user_date[loop_num])
                if value > 26:
                    value = 0 + (value-26)
                letter = [key for key, place in letter_dictionary.items() if place == value]
                returning_list.extend(letter)
                loop_num += 1
            elif item == " " and loop_num < 8:
                returning_list.append(" ")
            elif item == " " and loop_num == 8:
                loop_num = 0
                returning_list.append(" ")
        returning_list_string = "".join(map(str, returning_list))                
        print(returning_list_string)
        returning_string_label = Label(window, text=returning_list_string)
        returning_string_label.grid(row=8, column=0, columnspan=2)
    elif button_status.get() == 2:
        for item in message_list:
            if item != " " and loop_num < 8:
                value = letter_dictionary[item.lower()] - int(converted_user_date[loop_num])
                if value <= 0:
                    value = 26 - abs(value)
                letter = [key for key, place in letter_dictionary.items() if place == value]
                returning_list.extend(letter)
                loop_num += 1
            elif item != " " and loop_num == 8:
                loop_num = 0
                value = letter_dictionary[item.lower()] - int(converted_user_date[loop_num])
                if value <= 0:
                    value = 26 - abs(value)
                letter = [key for key, place in letter_dictionary.items() if place == value]
                returning_list.extend(letter)
                loop_num += 1
            elif item == " " and loop_num == 8:
                loop_num = 0
                returning_list.append(" ")
            elif item == " " and loop_num < 8:
                returning_list.append(" ")
        returning_list_string = "".join(map(str, returning_list))
        print(returning_list_string)  
        returning_string_label = Label(window, text=returning_list_string, anchor="center")
        returning_string_label.grid(row=7, column=1, columnspan=2)


def reset():
    submit_date_button.config(state="normal")
    submit_message_button.config(state="normal")
    users_message_entry.delete(0, END)
    users_date_entry.delete(0, END)
    returning_string_label.config(text="")
    users_message_entry.insert(0,"Enter the message here")
    users_date_entry.insert(0, "Enter date here")
    check_buttons()


reset_button = Button(window, text="Reset", command=reset)
reset_button.grid(row=9, column=1)

mainloop()
