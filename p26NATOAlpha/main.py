import pandas as pd


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("./p26NATOAlpha/nato_phonetic_alphabet.csv")
new_dic = {rows.letter : rows.code for (index,rows) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def Inputword():
    try:
        word = input("Enter a word: ")
        wordlist = [f"{w.upper()} : {new_dic[w.upper()]}" for w in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        Inputword()
    else:
        print(wordlist)

Inputword()