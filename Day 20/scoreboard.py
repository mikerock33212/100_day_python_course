from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highest_score') as f:
            self.highest_score = int(f.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def check_high_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score

    def reset_score(self):
        if self.score >= self.highest_score:
            with open('highest_score', mode='w') as f:
                f.write(f'{self.score}')
        self.update_scoreboard()
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score board: {self.score}, Highest Score: {self.highest_score}', move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write(f'Game Over!', move=False, align=ALIGNMENT, font=FONT)
