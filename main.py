# ui
import ttkbootstrap as ttk

# password
import string
import secrets

# clipboard
import pyperclip


def create_password(length, use_numbers, use_upper_char, use_special_char):
    alphabet = string.ascii_lowercase

    if use_numbers:
        alphabet += string.digits

    if use_upper_char:
        alphabet += string.ascii_uppercase

    if use_special_char:
        alphabet += string.punctuation

    new_password = ''.join(secrets.choice(alphabet) for _ in range(length))
    password.set(new_password)


def copy_to_clip_board():
    print(f"{password.get()} copied to clipboard")

    pyperclip.copy(password.get())
    pyperclip.paste()


TITLE_CONTENT = "Password Generator"

# window
window = ttk.Window(themename="darkly")
window.title(TITLE_CONTENT)
window.geometry("400x600")

# title
title_lable = ttk.Label(master=window, text=TITLE_CONTENT, font=60)
title_lable.pack(pady=10)

# input frame
input_frame = ttk.Frame(master=window)

# length of password frame
length_frame = ttk.Frame(master=input_frame)
length_frame_lable = ttk.Label(master=length_frame, text="Length of the Password", font=20)
length_frame_lable.pack()

# length of password options
length = ttk.IntVar(value=20)

length10 = ttk.Radiobutton(master=length_frame, text="10", value=10, variable=length)
length10.pack(anchor="w", padx=50)
length12 = ttk.Radiobutton(master=length_frame, text="12", value=12, variable=length)
length12.pack(anchor="w", padx=50)
length14 = ttk.Radiobutton(master=length_frame, text="14", value=14, variable=length)
length14.pack(anchor="w", padx=50)
length16 = ttk.Radiobutton(master=length_frame, text="16", value=16, variable=length)
length16.pack(anchor="w", padx=50)
length18 = ttk.Radiobutton(master=length_frame, text="18", value=18, variable=length)
length18.pack(anchor="w", padx=50)
length20 = ttk.Radiobutton(master=length_frame, text="20", value=20, variable=length)
length20.pack(anchor="w", padx=50)

length_frame.pack(pady=20)

# password options
options_frame = ttk.Frame(master=input_frame)
options_frame_lable = ttk.Label(master=options_frame, text="Password Options", font=20)
options_frame_lable.pack(pady=5)

use_numbers = ttk.BooleanVar(value=True)
use_upper_char = ttk.BooleanVar(value=True)
use_special_char = ttk.BooleanVar(value=True)

check_box_numbers = ttk.Checkbutton(master=options_frame,
                                    text="Use Numbers?",
                                    onvalue=True,
                                    offvalue=False,
                                    variable=use_numbers)
check_box_char = ttk.Checkbutton(master=options_frame,
                                 text="Use Upper Characters?",
                                 onvalue=True,
                                 offvalue=False,
                                 variable=use_upper_char)
check_box_special_char = ttk.Checkbutton(master=options_frame,
                                         text="Use Special Characters?",
                                         onvalue=True,
                                         offvalue=False,
                                         variable=use_special_char)

check_box_numbers.pack()
check_box_char.pack()
check_box_special_char.pack()

options_frame.pack()
input_frame.pack(pady=20)

# generate button
generate_button = ttk.Button(master=window,
                             text="Generate",
                             cursor="hand2",
                             command=lambda: create_password(length.get(), use_numbers.get(), use_upper_char.get(),
                                                             use_special_char.get()))
generate_button.pack(pady=20)

# output frame
output_frame = ttk.Frame(master=window, borderwidth=10)

# output lable
password = ttk.StringVar(value="Chose settings")
output_lable = ttk.Label(master=output_frame, textvariable=password)
output_lable.pack(side="left", padx=10)

copy_button = ttk.Button(master=output_frame, text="Copy", command=copy_to_clip_board, cursor="hand2")
copy_button.pack(padx=10)
output_frame.pack()

# display things on the screen
window.mainloop()
