from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1
    
    def paddlebounce(self):
        self.x_move *= -1
    
    def reset_position(self):
        self.hideturtle()
        self.home()
        self.paddlebounce()
        ch = random.randint(1,2)
        if ch == 1:
            self.bounce()
        self.showturtle()
            