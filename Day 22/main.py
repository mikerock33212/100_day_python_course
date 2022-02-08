from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
from scoreboard import Score
import time

screen = Screen()

screen.setup(width=1000, height=600)
screen.bgcolor('black')
screen.title('Pong')

screen.tracer(0)

r_paddle = Paddle((450, 0))
l_paddle = Paddle((-460, 0))

ball = Ball()

score = Score()

screen.update()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with the paddle
    elif ball.distance(r_paddle) < 50 and ball.xcor() >= 435 \
            or ball.distance(l_paddle) < 50 and ball.xcor() <= -445:
        ball.bounce_x()
    else:
        if ball.xcor() >= 490:
            ball.restart()
            score.l_score += 1
            score.write_out()
        elif ball.xcor() <= -490:
            ball.restart()
            score.r_score += 1
            score.write_out()

screen.exitonclick()

