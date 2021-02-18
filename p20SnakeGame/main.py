from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
s = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detection Collision with food
    if snake.Turtlelist[0].distance(food) < 15:
        food.refesh()
        s.score_update()
        snake.extend()

    #Detect collision with wall
    if snake.Turtlelist[0].xcor() > 280 or snake.Turtlelist[0].ycor() > 280 or snake.Turtlelist[0].xcor() < -280 or snake.Turtlelist[0].ycor() < -280:
        game_is_on = False
        s.game_over()

    #Detect collision with own tail
    for q in snake.Turtlelist[1:len(snake.Turtlelist)]:
        if snake.Turtlelist[0].distance(q) < 5:
            game_is_on = False
            s.game_over()


    

    
screen.exitonclick()