from turtle import Turtle, Screen
import pandas as pd
screen = Screen()
screen.title("U.S States Game")
image = "./p25UsStatesGame/blank_states_img.gif"
screen.addshape(image)
screen.setup(width= 800, height=567)
t = Turtle()
t.penup()
t.shape(image)
s = Turtle()
s.hideturtle()
s.penup()

# def get_mouse_click_coor(x,y):
#     print(x,y)

# t.onscreenclick(get_mouse_click_coor)
#t.mainloop()
guessedstate = []
while len(guessedstate) <= 50:
    answer_state = screen.textinput(title= "Guess the state", prompt= "What's another state?")
    data = pd.read_csv("./p25UsStatesGame/50_states.csv")
    dn = data
    ##### doesn't work until the answer is actually in the state names, if it isn't it just return None to x_cor and y_cor
    # try:
    #     x_cor = data[data.state == answer_state.title()].x
    #     y_cor = data[data.state == answer_state.title()].y
    #     print(x_cor, y_cor)
    #     count +=1
    # except:
    #     print("Wrong State, Try again")
    #     answer_state = screen.textinput(title= "Guess the state", prompt= "What's another state?")
    all_states = data.state.to_list()

    if answer_state == "Exit":
        for state in guessedstate:
            l = dn[dn.state == state].index
            dn = dn.drop(l)
        dn.to_csv("./p25UsStatesGame/states_not_guessed.csv")
        break

    if answer_state.title() in all_states:
        if answer_state.title() in guessedstate:
            print("Already Guessed")
        else:
            guessedstate.append(answer_state.title())
            x_cor = data[data.state == answer_state.title()].x
            y_cor = data[data.state == answer_state.title()].y
            s.goto(float(x_cor),float(y_cor))
            s.write(answer_state.title(), align= "center", font= ("Arial", 10, "normal"))

    else:
        print("Wrong State")
        continue
