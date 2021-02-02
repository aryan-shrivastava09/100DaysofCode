# from replit import clear
#HINT: You can call clear() to clear the output in the console.
import os
import time
# for windows
# os.system('cls')
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
auctionlist = []
flag = "yes"
max = 0
maxname = ""
while flag == "yes":
    
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    def auction(name, bid):
        entry = {}
        entry["name"] = name
        entry["bid"]= bid 
        auctionlist.append(entry)
    flag = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if flag == "yes":
      os.system("cls")
      time.sleep(2)
    auction(name,bid)
for i in range(0,len(auctionlist)):
    if auctionlist[i]["bid"] > max:
        max = auctionlist[i]["bid"]
        maxname= auctionlist[i]["name"]
print(f"The winner is {maxname} with a bid of ${max}")
    


