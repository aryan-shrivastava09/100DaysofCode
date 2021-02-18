from turtle import Turtle

class Score(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.s = 0
        self.goto(pos)
        self.write(f"{self.s}", align= "center", font= ("Arial", 30, "bold"))
    
    def updation(self):
        self.clear()
        self.s += 1
        self.write(f"{self.s}", align= "center", font= ("Arial", 30, "bold"))
    
    def game_over(self, side):
        self.home()
        self.write(f"GAME OVER\n {side} Wins!", align = "center", font = ("Arial", 60, "bold"))
