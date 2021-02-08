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
  compare_AB.remove(compare_AB[0])
  compare_AB.extend(random.sample(game_data.data,1))