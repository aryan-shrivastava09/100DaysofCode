import random
import turtle as t
t.colormode(255)
tim = t.Turtle()
tim.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# for i in range(0,361):
#     tim.color(randomcolor())
#     if i % 2 == 0:
#         tim.circle(150)
#     else:
#         tim.circle(100)
#     tim.right(i)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
