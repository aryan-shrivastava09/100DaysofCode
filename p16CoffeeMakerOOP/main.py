from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()

cm = CoffeeMaker()
mm = MoneyMachine()



switch = True
while switch:
  ch = input(f"What would you like? ({m.get_items()}) ")
  if ch == "off":
    switch = False
  elif ch == "report":
    cm.report()
    mm.report()
  else:
    d = m.find_drink(ch)
    p = cm.is_resource_sufficient(d)
    if p == True and mm.make_payment(d.cost):
      
      cm.make_coffee(d)