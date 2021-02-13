from turtle import Turtle, Screen
t = Turtle()
t.shape("turtle")
t.color("red")
t.pencolor("green")
def square():
    for _ in range(0,4):
        t.forward(100)
        t.left(90)
square()
screen = Screen()
screen.exitonclick()