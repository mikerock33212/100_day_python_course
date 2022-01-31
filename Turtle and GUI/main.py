from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()

tim.shape('turtle')
tim.color('green')

# tim.setpos(-50, 200)
# tim.pendown()

# colors1 = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']


screen.colormode(255)
tim.penup()
# tim.setpos(-350, 320)
xcor = -340
ycor = -310

tim.setpos(xcor, ycor)
tim.pendown()
# tim.goto(-350, 50)

# print(tim.xcor())
# print(tim.ycor())
tim.speed('fastest')

while ycor <= 300:
    color_r = random.randint(1, 255)
    color_g = random.randint(1, 255)
    color_b = random.randint(1, 255)
    tim.dot(30, color_r, color_g, color_b)
    tim.penup()
    tim.forward(50)
    if tim.xcor() >= 330:
        ycor += 50
        tim.setpos(xcor, ycor)








# tim.pensize(1)

# tim.speed('fastest')
# directions = [0, 90, 180, 270]
# direc = 0
# times = 100

# for _ in range(times):
#     color_r = random.randint(1, 255)
#     color_g = random.randint(1, 255)
#     color_b = random.randint(1, 255)
#     tim.pencolor(color_r, color_g, color_b)
#     tim.circle(100)
#     direc += (360 / times)
#     tim.setheading(direc)


# for _ in range(100):
#     color_r = random.randint(1, 255)
#     color_g = random.randint(1, 255)
#     color_b = random.randint(1, 255)
#     tim.pencolor(color_r, color_g, color_b)
#     tim.forward(50)
#     tim.setheading(random.choice(directions))

# for _ in range(40):
#     screen.colormode(255)
#     ran_num = random.randi
# #         tim.pencolor(color_r, color_g, color_b)
# #         tim.forward(50)
# #     elif ran_num == 2:
# #         tim.pencolor(color_r, color_g, color_b)
# #         tim.backward(50)
# #     elif ran_num == 3:
# #         tim.pencolor(color_r, color_g, color_b)
# #         tim.right(90)
# #         tim.forward(50)
# #     elif ran_num == 4:
# #         tim.pencolor(color_r, color_g, color_b)
# #         tim.left(90)
# #         tim.forward(50)
#
#
# # colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
# # col = 0
# # turns = 0
# # counter = 3
# # while counter < 14:
# #     color_r = random.randint(1, 255)
# #     color_g = random.randint(1, 255)
# #     color_b = random.randint(1, 255)
# #     tim.pencolor(color_r, color_g, color_b)
# #     # if col == (len(colors) - 1):
# #     #     col = 0
# #     # else:
# #     #     col += 1
# #     turns = 360 / counter
# #     for _ in range(counter):
# #         tim.forward(100)
# #         tim.right(turns)
# #     counter += 1
#
# screen.exitonclick()nt(1, 4)
#     color_r = random.randint(1, 255)
#     color_g = random.randint(1, 255)
#     color_b = random.randint(1, 255)
#     if ran_num == 1:


screen.exitonclick()