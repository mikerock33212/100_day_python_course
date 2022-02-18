from tkinter import *
import random

import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# def title_and_words():
#     with open('data/french_words.csv', 'r') as f:
#         scripts = [lis.strip() for lis in f.readlines()]
#         complete_scripts = [scrip.split(',') for scrip in scripts]
#         random_index = random.randint(0,1)
#         random_title = complete_scripts[0][random_index]
#         random_words = random.choice(complete_scripts[1:])[random_index]
#         return random_title, random_words
#
# results = title_and_words()
current_card = {}
to_learn = {}
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data_1 = pandas.DataFrame(to_learn)
    data_1.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage('images/card_front.png')
card_back_img = PhotoImage('images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, font=('Arial', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)



next_card()

window.mainloop()


