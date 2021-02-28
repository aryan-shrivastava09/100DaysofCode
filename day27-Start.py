import tkinter
window = tkinter.Tk()

window.title("First GUI program")
window.minsize(width  = 500, height = 300)
window.config(padx = 20, pady = 20)

# Entry
input = tkinter.Entry(width = 50)
input.insert(index = 0, string = "Some text to begin with")
# input.pack()
input.grid(column = 4, row = 2)


#Label
my_label = tkinter.Label(text = "I am a label", font = ("Arial", "24", "bold"))
# my_label.pack()
my_label.config(padx = 20, pady = 20)
my_label.grid(column = 0, row = 0)
my_label["text"] = "Changing label text"

#Button
def button_clicked():
    my_label.config(text = input.get())   ## Third way of changing attributes
    print("I got clicked")
my_button = tkinter.Button(text = "Click Me")
my_button["command"] = button_clicked
# my_button.pack()
my_button.grid(column = 1, row = 1)

#New button 
my_button2 = tkinter.Button(text = "Click Me")
my_button2.grid(column = 2, row =0)


window.mainloop()