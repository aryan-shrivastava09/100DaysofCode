from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.write(f"SCORE: {self.score}", align="center", font = ("Arial", 10, "bold"))
        

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", align="center", font = ("Arial", 10, "bold"))
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"SCORE: {self.score}", align="center", font = ("Arial", 10, "bold"))
        self.goto(0,30)
        self.write("GAME OVER", align="center", font = ("Arial", 20, "bold"))

