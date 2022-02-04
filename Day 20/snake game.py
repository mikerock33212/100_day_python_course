import time
from turtle import Turtle, Screen
from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)

    snake.move()


screen.exitonclick()

