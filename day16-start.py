import turtle
#can also use from turtle import Turtle as t 
t = turtle.Turtle() #Turtle is a class inside turtle module
t.shape("turtle")
t.color('coral')
t.forward(100)
my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()