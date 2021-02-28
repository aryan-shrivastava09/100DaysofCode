from tkinter import *

FONT = ("Arial", 10, "normal")
window = Tk()
window.title("Miles to Kms")
window.config(padx = 10, pady =10)

mlabel = Label(text = "Miles", font = FONT)
mlabel.grid(column = 1, row =1)
mlabel.config(padx = 5, pady =5)

input = Entry(width =30)
input.insert(END, string = "Enter number of Miles")
input.grid(column = 4, row =1)


kmlabel = Label(text = "KMs", font = FONT)
kmlabel.grid(column = 1, row= 3)
kmlabel.config(padx = 5, pady=5)

answerlabel = Label(text = "None", font = ("Times New Roman", 10, "bold"))
answerlabel.grid(column = 4, row = 3)

def miles_to_km():
    try:
        m = float(input.get())
        km = m * 1.609
        answerlabel.config(text = km)
    except:
        answerlabel.config(text = "Enter valid number of miles")
    
button = Button(text = "Convert", command = miles_to_km)
button.grid(column= 4, row = 5)


window.mainloop()