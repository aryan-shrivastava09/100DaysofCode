# from replit import clear
# import art
import os

ch = 'y'
i = 0
n3 = 0
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# print(art.logo)
print(logo)
while ch == 'y'or ch == 'n':
  if i > 0 and ch != 'n':
    n1 = n3
    op = input("Pick an operation: ")
    n2 = float(input("What's the next number?: "))
  if i == 0 or ch == 'n':
    if i > 0:
    #   clear()
    #   print(art.logo)
      os.system("cls")
      print(logo)
    
    n1 = float(input("What's the first number?: "))
    op = input("+\n-\n*\n/\nPick an operation: ")
    n2 = float(input("What's the next number?: "))

  def add(na1,na2):
    return na1 + na2

  def subtract(ns1,ns2):
    return ns1 - ns2

  def multiply(nm1,nm2):
    return nm1 * nm2

  def divide(nd1,nd2):
    return nd1/nd2

  if op == "+":
    n3 = add(n1,n2)
  if op == "-":
    n3 = subtract(n1,n2)
  if op == "*":
    n3 = multiply(n1,n2)
  if op == "/":
    n3 = divide(n1,n2)
  print(f"{n1} {op} {n2} = {n3}")
  ch = input(f"Press 'y' to continue with {n3} or press 'n' to start a new calculation.\n")
  i = i+1


  ####################
  ####################
#   from replit import clear
# from art import logo

# def add(n1, n2):
#   return n1 + n2

# def subtract(n1, n2):
#   return n1 - n2

# def multiply(n1, n2):
#   return n1 * n2

# def divide(n1, n2):
#   return n1 / n2

# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }

# def calculator():
#   print(logo)

#   num1 = float(input("What's the first number?: "))
#   for symbol in operations:
#     print(symbol)
#   should_continue = True
 
#   while should_continue:
#     operation_symbol = input("Pick an operation: ")
#     num2 = float(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")

#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
#       num1 = answer
#     else:
#       should_continue = False
#       clear()
#       calculator()

# calculator()