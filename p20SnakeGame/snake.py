from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.Turtlelist = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)    
    
    def add_segment(self, pos):
        a = Turtle()
        a.shape("square")
        a.color("white")
        a.penup()
        a.goto(pos)
        self.Turtlelist.append(a)
    
    def extend(self):
        posx = self.Turtlelist[-1].xcor()
        posy = self.Turtlelist[-1].ycor()
        posnew = (posx, posy)
        self.add_segment(posnew)    

    def move(self):
        for t in range(len(self.Turtlelist)-1,0,-1):
            self.Turtlelist[t].goto(self.Turtlelist[t-1].pos())
        self.Turtlelist[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.Turtlelist[0].heading() == 0: 
            self.Turtlelist[0].left(90)
        elif self.Turtlelist[0].heading() == 180:
            self.Turtlelist[0].right(90)
    
    def down(self):
        if self.Turtlelist[0].heading() == 0:
            self.Turtlelist[0].right(90)
        elif self.Turtlelist[0].heading() == 180:
            self.Turtlelist[0].left(90)

    def left(self):
        if self.Turtlelist[0].heading() == 90:
            self.Turtlelist[0].left(90)
        elif self.Turtlelist[0].heading() == 270:
            self.Turtlelist[0].right(90)
    
    def right(self):
        if self.Turtlelist[0].heading() == 90:
            self.Turtlelist[0].right(90)
        elif self.Turtlelist[0].heading() == 270:
            self.Turtlelist[0].left(90)
        

