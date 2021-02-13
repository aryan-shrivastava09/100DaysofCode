import random
# from turtle import Turtle, Screen
# we need to change this and import the whole turtle module to change the color mode
import turtle as tim

tim.colormode(255)

t = tim.Turtle()
t.shape("turtle")
t.pensize(10)
t.speed(0)
directions = [0,90,180,270]

def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b) #returns a tuple


for  i in range(10001):
    t.color(randomcolor())
    t.forward(30)
    t.setheading(random.choice(directions))

screen = tim.Screen()
screen.exitonclick()
