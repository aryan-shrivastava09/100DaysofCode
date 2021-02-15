from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def forwards():
    tim.forward(10)

def backwards():
    tim.backward(10)

def lefts():
    tim.left(5)

def rights():
    tim.right(5)

def clear():
    tim.reset()

screen.listen()
screen.onkeypress(key = "w", fun=forwards)
screen.onkeypress(key = "s", fun=backwards)
screen.onkeypress(key = "a", fun=lefts)
screen.onkeypress(key = "d", fun=rights)
screen.onkeypress(key = "c", fun=clear)

screen.exitonclick()