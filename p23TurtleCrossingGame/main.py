import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cm = CarManager()
p = Player()
sb = Scoreboard()

screen.listen()
screen.onkeypress(p.moveup, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ch = random.choice([1,2,3,4])
    if ch == 1:
        cm.create()
    cm.move()

    #Detecting finidh line
    if p.ycor() >= 280:
        cm.next_level()
        p.homepos()
        sb.updation()

    #detecting collinsion with car
    for t in cm.TurtleList:
        if (abs(p.ycor() - t.ycor()) < 20) and (abs(p.xcor() - t.xcor()) < 20):
            sb.game_over()
            game_is_on = False


screen.exitonclick()


