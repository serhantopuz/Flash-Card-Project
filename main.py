from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ----------------- Next Card -----------------#
data_frame = pd.read_csv("data/french_words.csv")
words_list = data_frame.to_dict(orient="records")
print(words_list)


def next_card():
    rand_word = random.choice(words_list)
    canvas.itemconfig(word, text=rand_word["French"])
    canvas.itemconfig(language, text="French")


# ----------------- UI Design ----------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_flashcard = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_flashcard)
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