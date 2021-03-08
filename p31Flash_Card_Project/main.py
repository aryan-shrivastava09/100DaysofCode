from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
ch = {}

#_________________________________CHANGE CARDS__________________________________#

def next_card():
    global ch, flip_timer
    window.after_cancel(flip_timer)
    ch = random.choice(wordlist)
    w = ch["French"]
    canvas.itemconfig(language, text = "French", fill = "black")
    canvas.itemconfig(word, text = w, fill = "black")
    canvas.itemconfig(cardimage, image = card)
    flip_timer = window.after(3000, func= english_translation)

def right_click():
    wordlist.remove(ch)
    dataframe = pd.DataFrame(wordlist)
    dataframe.to_csv("./p31Flash_Card_Project/data/words_to_learn.csv", index =False)
    next_card()

def english_translation():
    canvas.itemconfig(cardimage, image = cardb)
    w = ch["English"]
    canvas.itemconfig(language, text = "English", fill = "white")
    canvas.itemconfig(word, text = w, fill = "white")



#______________________________________UI_______________________________________#
window = Tk()
window.title("Flashy The Flash Card App")
window.config(bg = BACKGROUND_COLOR, pady=30, padx = 30)
flip_timer = window.after(3000, func= english_translation)

try: 
    data = pd.read_csv("./p31Flash_Card_Project/data/words_to_learn.csv")

# except FileNotFoundError: could've used this but its not catching the custom index error of pandas when words_to_learn.csv is empty
except:
    data = pd.read_csv("./p31Flash_Card_Project/data/french_words.csv")

# wordlist = [{row.French:row.English} for label,row in data.iterrows()]
wordlist = data.to_dict(orient = "records")

canvas = Canvas(width = 800, height = 530, bg = BACKGROUND_COLOR, highlightthickness = 0 )
card = PhotoImage(file = "./p31Flash_Card_Project/images/card_front.png")
cardimage = canvas.create_image(400,265, image = card )
cardb = PhotoImage(file = "./p31Flash_Card_Project/images/card_back.png")

language = canvas.create_text(400,150,text = "Language", font = ("Arial", "40","italic" ))
word = canvas.create_text(400, 270, text ="Word" , font = ("Arial", 60, "bold"))

canvas.grid(column = 0, row = 0, columnspan = 2)

#Buttons
ricon = PhotoImage(file = "./p31Flash_Card_Project/images/right.png")
right = Button(image = ricon, bg = BACKGROUND_COLOR, highlightthickness = 0, command = right_click)
right.grid(column = 1, row =1)
wicon = PhotoImage(file ="./p31Flash_Card_Project/images/wrong.png")
wrong = Button(image = wicon, bg = BACKGROUND_COLOR, highlightthickness = 0, command = next_card)
wrong.grid(column = 0, row =1)

next_card()

window.mainloop()