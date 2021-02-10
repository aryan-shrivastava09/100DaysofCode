MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def cost():
  print("Please insert coins.")
  q = int(input("how many quarters?: "))
  d = int(input("how many dimes?: "))
  n = int(input("how many nickels?: "))
  p = int(input("how many pennies?: "))
  amount = 0.25*q + 0.10*d + 0.05*n + 0.01*p
  return amount 

def check(resources, ch, a):
  if a >= MENU[ch]["cost"]:
    if MENU[ch]["ingredients"]["water"] >= resources["water"]:
      return "Not enough water"
    elif MENU[ch]["ingredients"]["milk"] >= resources["milk"]:
      return "Not enough milk"
    elif MENU[ch]["ingredients"]["coffee"] >= resources["coffee"]:
      return "Not enough coffee"
  else:
    return "Not enough Money"

def deduction(a, ch):
  if a > MENU[ch]["cost"]:
    al = a - MENU[ch]["cost"]
  return al

def updation(ch):
  resources["water"] -= MENU[ch]["ingredients"]["water"]
  resources["milk"] -= MENU[ch]["ingredients"]["milk"]
  resources["coffee"] -= MENU[ch]["ingredients"]["coffee"]
  resources["money"] += MENU[ch]["cost"]
  return resources


def report():
  w = resources["water"]
  mk = resources["milk"]
  c = resources["coffee"]
  m = resources["money"]
  print(f"Water: {w}")
  print(f"Milk: {mk}")
  print(f"Coffee: {c}")
  print(f"Money: {m}")

switch = True
reason = None
while switch:
  ch = (input(" What would you like? (espresso/latte/cappuccino): ")).lower()
  if ch == "off":
    break
  if ch == "report":
    report()
    continue
  a = cost()
  reason = check(resources, ch, a)
  if reason == None:
    updation(ch)
    d = round(deduction(a,ch), 2)
    print(f"Here is ${d} in change.")
    print(f"Here is your {ch} ☕️. Enjoy!")
  else:
    print(reason)
    break
  

######
######
######
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])