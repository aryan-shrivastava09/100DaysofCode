from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
Turtlelist = []
yposition = [150, 100, 50 , 0, -50, -100, -150]

for i in range(0,7):
    a = Turtle()
    a.shape("turtle")
    a.color(color[i])
    a.penup()
    a.goto(x = -230, y= yposition[i]  )
    Turtlelist.append(a)

user_bet = screen.textinput(title = "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")

while user_bet not in color:
    user_bet = screen.textinput(title = "Make your bet", prompt= "Enter a valid color: ")
    race_is_on = False

race_is_on = True

while race_is_on:
    for turtle in Turtlelist:
        if turtle.xcor() > 230:
            winningturtle = turtle
            race_is_on = False
        randomDistance = random.randint(0,10)
        turtle.forward(randomDistance)

c = winningturtle.color() # tupple class 
if c[0] == user_bet:
    print(f"You won, {user_bet} is the winner")
else:
    print(f"You lose, {c[0]} is the winner ")

screen.exitonclick()