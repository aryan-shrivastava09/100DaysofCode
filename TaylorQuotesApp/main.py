from tkinter import *
import requests
THEME_COLOR = "#375362"

def get_quote():
    response = requests.get(url= "https://api.taylor.rest/")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text = quote)



window = Tk()
window.title("Taylor Says...")
window.config(bg = THEME_COLOR, padx=20, pady=20)

canvas = Canvas(width=300, height=414, bg = THEME_COLOR, highlightthickness = 0)
background_img = PhotoImage(file="./TaylorQuotesApp/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Taylor Quote Goes HERE", width=250, font=("Arial", 18, "bold"), fill="white")
canvas.grid(row=0, column=0)

Taylor_img = PhotoImage(file="./TaylorQuotesApp/index.png")
Taylor_button = Button(image=Taylor_img, highlightthickness=0, command=get_quote, bg = THEME_COLOR)
Taylor_button.grid(row=1, column=0)



window.mainloop()