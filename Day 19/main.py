from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=700, height=500)

race_on = False
user_bet = screen.textinput(title='Please place your bet.', prompt='Which turtle is going to win? Enter its color: ' )
colors1 = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
all_turtles = []

ycor = -150

for li in colors1:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(li)
    new_turtle.penup()
    new_turtle.goto(x=-340, y=ycor)
    ycor += 50
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for tur in all_turtles:
        random_distance = random.randint(1, 10)
        tur.forward(random_distance)
        if tur.xcor() >= 320:
            race_on = False
            if tur.pencolor() == user_bet:
                print(f'You won! The winner is: {tur.pencolor()} turtle')
            else:
                print(f'You lose! The winner is: {tur.pencolor()} turtle')






#
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def turn_right():
#     tim.right(10)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def clear():
#     tim.reset()
#
#
# screen.onkey(key='w', fun=move_forward)
# screen.onkey(key='s', fun=move_backward)
# screen.onkey(key='a', fun=turn_left)
# screen.onkey(key='d', fun=turn_right)
# screen.onkey(key='space', fun=clear)
# screen.listen()


screen.exitonclick()
