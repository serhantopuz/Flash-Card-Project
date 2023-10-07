from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
data_frame = pd.read_csv("data/french_words.csv")
words_to_learn = data_frame.to_csv("data/words_to_learn.csv", index=False)
words_list = data_frame.to_dict(orient="records")

current_card = {}


# ----------------- Flip The Card -----------------#
def flip_card():
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=back_flashcard)


# ----------------- Next Card -----------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_list)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=front_flashcard)
    flip_timer = window.after(3000, flip_card)


# ----------------- UI Design ----------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_flashcard = PhotoImage(file="images/card_front.png")
back_flashcard = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_flashcard)
language = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

false_image = PhotoImage(file="images/wrong.png")
false_button = Button(image=false_image, highlightthickness=0, command=next_card)
false_button.grid(row=1, column=0)

true_image = PhotoImage(file="images/right.png")
true_button = Button(image=true_image, highlightthickness=0, command=next_card)
true_button.grid(row=1, column=1)

next_card()
window.mainloop()