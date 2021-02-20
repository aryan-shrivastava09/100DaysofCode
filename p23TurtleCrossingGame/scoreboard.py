from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-200,260)
        self.write(f"LEVEL : {self.level}", align= "center", font= FONT)

    def updation(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL : {self.level}", align= "center", font= FONT)
    
    def game_over(self):
        self.home()
        self.write("GAME OVER", align= "center", font = ("Arial", "50", "bold"))


    