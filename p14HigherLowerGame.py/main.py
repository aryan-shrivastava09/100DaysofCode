import game_data
import art
import random
from replit import clear

score = 0
lose_game = False

compare_AB = random.sample(game_data.data,2)

def compare(compare_AB, ch):
  global score
  global lose_game
  if compare_AB[0]["follower_count"] > compare_AB[1]["follower_count"]:
    if ch.lower() == 'a':
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      lose_game = True
  else:
    if ch.lower() == 'b':
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      lose_game = True

while lose_game == False:
  clear()
  celeb_name1 = compare_AB[0]["name"]
  desc1 = compare_AB[0]["description"]
  coun1 = compare_AB[0]["country"]
  celeb_name2 = compare_AB[1]["name"]
  desc2 = compare_AB[1]["description"]
  coun2 = compare_AB[1]["country"]
  print(art.logo)
  if score > 0:
    print(f"You're right! Current score: {score}")
  print(f"Compare A: {celeb_name1}, a {desc1}, from {coun1}.")
  print(art.vs)
  print(f"Compare B: {celeb_name2}, a {desc2}, from {coun2}.")
  ch = input("Who has more followers? Type 'A' or 'B': ")
  compare(compare_AB, ch)
  if lose_game== True:
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")
  compare_AB.remove(compare_AB[0])
  compare_AB.extend(random.sample(game_data.data,1))



  #########
  #########
  #########

# Final Solution
# from game_data import data
# import random
# from art import logo, vs
# from replit import clear

# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()


# # Generate a random account from the game data.

# # Format account data into printable format.

# # Ask user for a guess.

# # Check if user is correct.
# ## Get follower count.
# ## If Statement

# # Feedback.

# # Score Keeping.

# # Make game repeatable.

# # Make B become the next A.

# # Add art.

# # Clear screen between rounds.