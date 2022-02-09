import time
from turtle import Screen, Turtle
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        score.add_score()
        food.refresh()
        snake.extend()
        score.check_high_score()
        score.update_scoreboard()

    elif snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()
        score.check_high_score()
        score.update_scoreboard()
        score.reset_score()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            score.game_over()
            score.check_high_score()
            score.update_scoreboard()
            score.reset_score()


screen.exitonclick()

