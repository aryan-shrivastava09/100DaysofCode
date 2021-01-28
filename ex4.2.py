import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length = len(names)
rand = random.randint(0,length-1)
print(f"{names[rand]} is going to buy the meal today!")