import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
rand = random.randint(0,2)
print("Computer chose:")
if rand == 0:
  print(rock)
elif rand == 1:
  print(paper)
elif rand == 2:
  print(scissors)

#Result
if (choice==0):
  if (rand==0):
    print("It's a draw")
  elif (rand == 1):
    print("You lose")
  else:
    print("You win")

if (choice==1):
  if (rand==1):
    print("It's a draw")
  elif (rand == 2):
    print("You lose")
  else:
    print("You win")

if (choice==2):
  if (rand==2):
    print("It's a draw")
  elif (rand == 0):
    print("You lose")
  else:
    print("You win")