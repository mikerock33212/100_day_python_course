from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('yellow')
        self.speed('fastest')
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-285, 285)
        random_y = random.randint(-285, 285)
        self.penup()
        self.goto(random_x, random_y)