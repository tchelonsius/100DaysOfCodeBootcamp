import tkinter as tk
from tkinter import PhotoImage
import pandas
import random


# This function deletes the words already known by the user and updates the csv file.
def already_known(to_remove):
    global to_learn_list
    to_learn_list.remove(to_remove)
    pandas.DataFrame(to_learn_list).to_csv("to_learn.csv")

# shows the next card by choosing a new word from the database, uploading the image and the texts
# and also by deleting already known words by calling already_known(). This last function is only called
# if the user directly pressed check, but not if he saw the translation (controlled with current_image).
def next_card():
    global word_dict, current_image
    # global flip_timer
    if current_image == 0:
        already_known(word_dict)
    # root.after_cancel(flip_timer)
    word_dict = random.choice(to_learn_list)
    canvas.itemconfig(canvas_image, image=front_image)
    current_image = 0
    canvas.itemconfig(canvas_language,text="German", fill="black")
    canvas.itemconfig(canvas_word, text=word_dict["german"], fill="black")
    #flip_timer = root.after(3000, func=show_translation)

# shows the back of the flashcard
def show_translation():
    global current_image
    canvas.itemconfig(canvas_language, text="enlish", fill="white")
    canvas.itemconfig(canvas_word, text=word_dict["english"], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)
    current_image = 1


# Get the data from the to_learn file. If it doesn't exist yet, it'll be created.
try:
    data = pandas.read_csv("to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("words_translation.csv")
    pandas.DataFrame(data).to_csv("to_learn.csv")

# data = pandas.read_csv("to_learn.csv")
to_learn_list = data.to_dict(orient="records")

# global variables
word_dict = random.choice(to_learn_list)
# *front_image: 0, back_image: 1*
current_image = 0

# Root
root = tk.Tk()
root.config(width=600,height=400,padx=30, pady=30, bg="#B1DDC6")
root.title("Flash Cards App")
root.iconbitmap("images/icon.ico")
#flip_timer = root.after(3000, func=show_translation)

# Images
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
back_image = tk.PhotoImage(file="images/card_back.png")
front_image = tk.PhotoImage(file="images/card_front.png")

# Canvas
canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg="#B1DDC6")
canvas_image = canvas.create_image(400, 263, image=front_image)
if front_image==0:
    print("front image")
canvas.grid(column=0, row=0, columnspan=2)
canvas_language = canvas.create_text(400, 150, text="German", font=("Courier", 40, "bold"))
canvas_word = canvas.create_text(400, 263, text=word_dict["german"], font=("Courier", 60, "bold"))

# buttons
right_button = tk.Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=0,row=1)
wrong_button = tk.Button(image = wrong_image, highlightthickness=0, command=show_translation)
wrong_button.grid(column=1,row=1)



root.mainloop()