# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1l = name1.lower()
name2l = name2.lower()
combined = name1l + name2l
firstd = combined.count('t') + combined.count('r') + combined.count('u') + combined.count('e')
secondd = combined.count('l') + combined.count('o') + combined.count('v') + combined.count('e')
score = int(str(firstd) + str(secondd))
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")