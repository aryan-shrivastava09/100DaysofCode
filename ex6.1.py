# Hurdles race
# Reeborg has entered a hurdles race. Make him run the course, following the path shown.
# What you need to know
# The functions move() and turn_left().
# Difficulty level

# More advanced
# You may have noticed that your solution has some repeated patterns. If you know how to define functions, define a function named jump() and use it to simplify your program.

# Difficulty level

# Background image: www.pexels.com
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for step in range(6):
    jump()