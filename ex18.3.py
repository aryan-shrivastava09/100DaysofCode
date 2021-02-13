import random
from turtle import Turtle, Screen
color = ["red", "green", "blue", "coral", "black", "purple", "IndianRed", "LightSalmon","pink", "DarkBlue"]
random.shuffle(color)
t = Turtle()
t.shape("turtle")
t.penup()
t.setpos(-50,-50)
t.pendown()
for i in range(3,11):
    t.color(color[i])
    for j in range(0,i):
        t.forward(100)
        t.left(360/i)

screen = Screen()
screen.exitonclick()


#######################################################################################################
# import turtle as t
# import random

# tim = t.Turtle()

# ########### Challenge 3 - Draw Shapes ########

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)