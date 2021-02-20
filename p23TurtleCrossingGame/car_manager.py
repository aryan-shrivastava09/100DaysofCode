from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.TurtleList = [] 
        self.movedistance = STARTING_MOVE_DISTANCE
        for _ in range(0,100):
            ch = random.choice([1,2,3])
            if ch == 1:
                self.create()
            self.move()
        
    def create(self):        
        a = Turtle()
        a.penup()
        a.color(random.choice(COLORS))
        a.shape("square")
        a.shapesize(stretch_len= 2, stretch_wid= 1)
        a.goto(300,random.randint(-220, 240))
        self.TurtleList.append(a)
    
    def move(self):
        for t in self.TurtleList:
            t.backward(self.movedistance)

    def next_level(self):
        self.movedistance += MOVE_INCREMENT    


        
        

        

    