from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_out()

    def write_out(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align='center', font=('Courier', 100, 'normal'))
        self.goto(100, 190)
        self.write(self.r_score, align='center', font=('Courier', 100, 'normal'))
