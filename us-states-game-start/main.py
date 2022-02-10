from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

t = Turtle(image)


def turtle_write(x, y, ans):
    new_t = Turtle()
    new_t.hideturtle()
    new_t.penup()
    new_t.goto(x, y)
    new_t.write(ans, align='center', font=('Arial', 12, 'normal'))


def missed_states(guessed):
    final_data_list = data['state'].to_list()
    for lis in guessed:
        if lis in final_data_list:
            final_data_list.remove(lis)
    return final_data_list


data = pd.read_csv('50_states.csv')

# print(data['state'].to_list())

total_questions = len(data)
counter = 0
guessed_list = []

game_on = True
while counter < len(data) and game_on:
    if counter == 0:
        state_input = screen.textinput(title=f'Guess a state? ', prompt='What is another state name? ').title()
    else:
        state_input = screen.textinput(title=f'Current {counter} / {total_questions}',
                                       prompt='What is another state name?').title()
    if state_input in data['state'].to_list():
        counter += 1
        x_cor = int(data[data['state'] == state_input]['x'])
        y_cor = int(data[data['state'] == state_input]['y'])
        turtle_write(x_cor, y_cor, state_input)
        guessed_list.append(state_input)
    if counter == len(data):
        game_on = False
    if state_input == 'Exit':
        game_on = False
        fil_lst = missed_states(guessed_list)
        new_ls = pd.DataFrame(fil_lst)
        new_ls.to_csv('missed_states.csv')
