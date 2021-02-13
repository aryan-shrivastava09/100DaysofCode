import random
from turtle import Turtle, Screen
color = ["red", "green", "blue", "coral", "black", "purple", "IndianRed", "LightSalmon","pink", "DarkBlue",
"crimson", "maroon", "dark green", "firebrick", "goldenrod", "midnightblue", "orchid", "MediumPurple"
]
t = Turtle()
t.shape("turtle")
t.pensize(10)
t.speed(0)
directions = [0,90,180,270]
for  i in range(10001):
    c = random.choice(color)
    t.color(c)
    t.forward(30)
    t.setheading(random.choice(directions))

######## My solution not entirely random as it couldn't go in the backward direction directly
# for i in range(0,10001):
#     c = random.choice(color)
#     t.color(c)
#     ch = random.choice([1,2,3,4])
#     if ch == 1:
#         t.forward(30)
#     elif ch == 2:
#         t.left(90)
#         t.forward(30)
#     elif ch == 3:
#         t.right(90)
#         t.forward(30)
#     elif ch == 4:
#         t.right(270)
#         t.forward(30)

screen = Screen()
screen.exitonclick()