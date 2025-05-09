from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

all_french_words = pandas.read_csv("data/french_words.csv")


try:
    learning_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    all_french_words.to_csv("data/words_to_learn.csv", index=False)
    learning_words = all_french_words.to_dict(orient="records")
else:
    learning_words = learning_data.to_dict(orient="records")


current_words = {}


def remove_words():
    print(current_words)
    learning_words.remove(current_words)
    updated_words = pandas.DataFrame(learning_words)
    updated_words.to_csv("data/words_to_learn.csv", index=False)
    next_card()



def next_card():
    global current_words, flip_timer
    window.after_cancel(id=flip_timer)
    current_words = choice(learning_words)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_words["French"], fill="black")
    flip_timer = window.after(ms=3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_words["English"], fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(ms=10000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=remove_words)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
