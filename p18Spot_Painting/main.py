# import colorgram
# colors = colorgram.extract('image1.jpg', 30)
# rgb_list = []
# for i in range(0, len(colors)):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     new_color = (r, g, b)
#     rgb_list.append(new_color)
#
#
# print(rgb_list)

color_list =[(202, 164, 110), (149, 75, 50),
             (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
             (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
             (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
             (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
tim.penup()
tim.setposition(-290, -290)
tim.pendown()
tim.hideturtle()
for i in range(0, 10):
    for j in range(0,10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.setposition(-290, -290 + 50*i)

screen = t.Screen()
screen.exitonclick()

