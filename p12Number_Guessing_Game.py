#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
logo = '''     __                                              __ ,                                         
   /  -,                ,,                        ,-| ~                                          
  ||   )                ||                       ('||/__,                          '         _   
 ~||---) \\ \\ \\/\\/\\ ||/|,  _-_  ,._-_       (( |||  | \\ \\  _-_   _-_,  _-_, \\ \\/\\  / \\ 
 ~||---, || || || || || || || || \\  ||         (( |||==| || || || \\ ||_.  ||_.  || || || || || 
 ~||  /  || || || || || || |' ||/    ||          ( / |  , || || ||/    ~ ||  ~ || || || || || || 
  |, /   \\/\\ \\ \\ \\ \\/   \\,/   \\,          -____/  \\/\\ \\,/  ,-_-  ,-_-  \\ \\ \\ \\_-| 
-_-  --~                                                                                    /  \ 
                                                                                           '----`
'''
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
n = random.randint(1,100)
print(f"Pssst, the correct answer is {n}")

def check(number, guesses):
  i = 0
  while i <= guesses:
    if guesses - i == 0:
      print("You've run out of guesses, you lose.")
      break
    else:
      print(f"You have {guesses - i} attempts remaining to guess the number.")
    n = int(input("Make a guess: "))
    if n != number:
      if n > number:
        print("Too High")
      elif n < number:
        print("Too Low")
    if n == number:
      print(f"You got it! The answer was {number}")
      break
    i += 1



ch = input("Choose a difficulty. Type 'easy' or 'hard': ")

if ch == 'easy':
  check(n, 10)
elif ch == 'hard':
  check(n, 5)


#####
#####
#####

# Given Solution

# from random import randint
# from art import logo

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()