STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("coral")
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def moveup(self):
        self.forward(MOVE_DISTANCE)

    def homepos(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()

