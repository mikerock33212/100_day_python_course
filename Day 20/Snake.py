import time
from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            new_snake = Turtle('square')
            new_snake.color('white')
            new_snake.penup()
            new_snake.goto(pos)
            self.segments.append(new_snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)