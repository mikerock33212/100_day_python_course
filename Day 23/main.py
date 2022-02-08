import time
from turtle import Screen, Turtle
from car_manager import Car
from player import Player
from score_board import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
score = Score()

screen.listen()
screen.onkey(player.move_up, 'Up')


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    # detect if turtle crashes
    for i in car.all_cars:
        if i.distance(player) < 25:
            game_on = False
            score.game_over()

    # detect if turtle crossed the finish line
    if player.is_at_finishline():
        player.go_to_start()
        car.level_up()
        score.increase_level()
        score.write_up()


screen.exitonclick()


