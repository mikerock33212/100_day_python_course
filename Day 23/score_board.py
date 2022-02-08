from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.write_up()

    def increase_level(self):
        self.score += 1

    def write_up(self):
        self.penup()
        self.goto(0, 275)
        self.clear()
        self.write(f'Level {self.score}', align='center', font=('Courier', 20, 'bold'))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f'Game Over!', align='center', font=('Courier', 20, 'bold'))
