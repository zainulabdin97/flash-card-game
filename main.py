import random
import time
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)
random_num = {}
window.config(background=BACKGROUND_COLOR)

# flip card

def flip_card():
    canvas.itemconfig(front_card_img, image=card_back_img)
    canvas.itemconfig(headline_word, text="English", fill="white")
    canvas.itemconfig(french_word, text=f"{random_num["English"]}", fill="white")


# card front
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
front_card_img = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_back_img = PhotoImage(file="images/card_back.png")

# delay of 3ms
after = window.after(3000, flip_card)


# french txt
headline_word = canvas.create_text(400, 150, text="French", fill="black", font=('Ariel 40 italic'))

# displaying French word
try:
    df = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
dataframe_dictionary = df.to_dict(orient="records")

#generate random number
def random_number():
    global random_num
    random_num = random.choice(dataframe_dictionary)
    return random_num

# trouve txt
french_word = canvas.create_text(400, 263, text=f"{random_number()["French"]}", fill="black", font=('Ariel 60 bold'))

def next_card():
    global french_word, after
    window.after_cancel(after)
    canvas.itemconfig(french_word, text=f"{random_number()["French"]}", fill="black")
    canvas.itemconfig(front_card_img, image=card_front_img)
    canvas.itemconfig(headline_word, text="French", fill="black")
    after = window.after(3000, flip_card)

def guessed_right():
    dataframe_dictionary.remove(random_num)
    data_frame = pd.DataFrame(dataframe_dictionary)
    data_frame.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# cross btn
cross_btn_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_btn_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
cross_button.grid(row=1, column=0)

# right btn
right_btn_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_btn_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=guessed_right)
right_button.grid(row=1, column=1)


window.mainloop()

