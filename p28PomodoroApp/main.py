from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
window = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_app():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    mainlabel.config(text = "Timer", fg = GREEN)
    check.config(text = "")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global window
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps%8==0:
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        mainlabel.config(text = "Break", fg = RED)
        count_down(long_break_sec)

    elif reps%2 == 0:
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        mainlabel.config(text = "Break", fg = PINK)
        count_down(short_break_sec)

    else:
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        mainlabel.config(text = "Work", fg = GREEN)
        count_down(work_sec)
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check.config(text = mark)
        
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000,count_down, count -1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.minsize(width = 300, height = 400)
window.config(padx = 100, pady = 50, bg = YELLOW)


canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato = PhotoImage(file = "./p28PomodoroApp/tomato.png")
canvas.create_image(100,112, image = tomato)
timer_text = canvas.create_text(100, 130, text= "00:00", fill = "white", font = (FONT_NAME, "28", "bold"))
canvas.grid(row = 1, column = 1)

#Labels
mainlabel = Label(text = "Timer",bg = YELLOW, fg = GREEN, font = (FONT_NAME, "25", "bold"))
mainlabel.grid(row = 0, column = 1)
mainlabel.config(padx = 10, pady= 10)

check = Label(bg = YELLOW, fg = GREEN, font = (FONT_NAME,"20","normal" ))
check.grid(row = 3, column = 1)

# Buttons
button1 = Button(text = "Start", command = start_timer)
button1.config(bg = YELLOW)
button1.grid(row =2 , column = 0)

button2 = Button(text = "Reset", command = reset_app)
button2.config(bg = YELLOW)
button2.grid(row = 2, column = 2)


window.mainloop()