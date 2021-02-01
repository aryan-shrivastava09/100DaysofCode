
# Define a function called paint_calc() so that the code below works.   
import math
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
n = 0
def paint_calc(height, width, cover):
  n = (height * width) / cover
  if round(n) < n:
    n = round(n) +1
  else:
    n = round(n)
  print(f"You\'ll need {n} cans of paint.")
paint_calc(height=test_h, width=test_w, cover=coverage)
# print(math.ceil(-2.1))
# print(math.floor(-2.1))