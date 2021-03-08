from quiz_brain import QuizBrain
from tkinter import *
import time
THEME_COLOR = "#375362"
class UserInterface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg = THEME_COLOR, pady =20, padx = 20)

        #Label
        self.score = Label(text = "Score:0", bg = THEME_COLOR, fg = "white", font = ("Arial", "10", "normal"))
        self.score.grid(column = 1, row = 0)
        self.score.config(padx = 20, pady = 20)

        #Canvas
        self.canvas = Canvas(width = 300, height = 250, bg = "white")
        self.question_text = self.canvas.create_text(150, 125, text = "Some Text", fill = THEME_COLOR, font=("Arial", 20, "italic"), width = 280)
        self.canvas.grid(column = 0, row = 1, columnspan =2, pady = 50)

        #Buttons
        image_right = PhotoImage(file = "./p34QuizzlerApp/images/true.png")  
        self.button1 = Button(image =image_right, highlightthickness = 0, command = self.true_click)
        self.button1.grid(column = 0, row =2)

        image_wrong = PhotoImage(file = "./p34QuizzlerApp/images/false.png")
        self.button2 = Button(image = image_wrong, highlightthickness = 0, command = self.false_click)
        self.button2.grid(column = 1, row =2)

        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg = "white")
            q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q)
        else:
            self.canvas.config(bg = "white")
            self.canvas.itemconfig(self.question_text, text = f"You've completed the quiz\nScore:{self.quiz.score}/10" )
            self.button1.config(state = "disabled")
            self.button2.config(state = "disabled")

    def true_click(self):
        self.flash(self.quiz.check_answer("True"))

        self.score.config(text = f"Score:{self.quiz.score}")

    def false_click(self):
        self.flash(self.quiz.check_answer("False"))

        self.score.config(text = f"Score:{self.quiz.score}")   

    def flash(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000,self.get_next_question)
        


