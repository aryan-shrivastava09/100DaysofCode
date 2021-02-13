from turtle import Turtle, Screen
t= Turtle()
t.shape("turtle")
t.penup()
t.setpos(-300,0)
for i in range(0,30):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)



screen = Screen()
screen.exitonclick()
