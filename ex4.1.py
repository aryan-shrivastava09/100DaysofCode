#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random
toss = [1,0]
choice = random.choice(toss)
if choice == 1 :
  print("Heads")
elif choice == 0:
  print("Tails")

#2 
toss = random.randint(0,1)
if toss == 1:
  print("Heads")
elif toss == 0:
  print("Tails")