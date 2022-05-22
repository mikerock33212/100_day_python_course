from flask import Flask
import random

app = Flask(__name__)


def random_number():
    num = random.randint(0, 9)
    return num


RANDOM_NUM = random_number()


@app.route('/')
def random_num_page():
    return '<h1> that says "Guess a number between 0 and 9"</h1> ' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def detect_number(number):
    if number == RANDOM_NUM:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number > RANDOM_NUM:
        return '<h1 style="color: red">Too High!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < RANDOM_NUM:
        return '<h1 style="color: purple">Too Low!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
