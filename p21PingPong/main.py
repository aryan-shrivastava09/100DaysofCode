from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong")
screen.tracer(0)

line = Turtle()
line.hideturtle()
line.color("white")
line.penup()
line.setheading(270)
line.goto(0,-300)
line.setheading(90)
line.pendown()
for i in range(0,80):
    line.pensize(5)
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()

r_pad = Paddle((350,0))
l_pad = Paddle((-350,0))
b = Ball()
r_s = Score((75, 250))
l_s = Score((-75, 250))

screen.listen()
screen.onkeypress(r_pad.up, "Up")
screen.onkeypress(r_pad.down, "Down" )
screen.onkeypress(l_pad.up, "w")
screen.onkeypress(l_pad.down, "s" )

game_is_on = True
t = 0.2
while game_is_on:
    time.sleep(t)
    screen.tracer(1)
    b.move()

    #Detect collision wall
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce()

    #Detect collision paddle
    if (b.distance(l_pad) < 50 and b.xcor() < -320) or (b.distance(r_pad) < 50 and b.xcor() > 320):
        b.paddlebounce()
        t /= 1.5

    #Detect when ball goes out of bounds
    # For right paddle
    if b.xcor() > 380:
        b.reset_position()
        l_s.updation()
        t = 0.2
    
    #For left paddle
    elif b.xcor() < -380:
        b.reset_position()
        r_s.updation()
        t = 0.2

    if r_s.s == 7:
        line.clear()
        r_s.game_over("Right")
        game_is_on = False
    elif l_s.s == 7:
        line.clear()
        l_s.game_over("Left")
        game_is_on = False


screen.exitonclick()
