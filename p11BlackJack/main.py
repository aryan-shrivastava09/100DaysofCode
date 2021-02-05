############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.



# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# ch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# pos = []
# i = 0
# player_cards = random.sample(cards,2)
# computer_cards = random.sample(cards,2)
# print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
# print(f"Computer's first card: {computer_cards[0]}")
# if sum(computer_cards) == 21 or sum(player_cards) == 21:
#   if sum(player_cards) == 21 and sum(computer_cards) == 21:
#     print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
#     print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
#     print("You win, you have Blackjack")

#   if sum(player_cards) == 21:
#     print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
#     print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
#     print("You win, you have Blackjack")

#   elif sum(computer_cards) == 21:
#     print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
#     print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
#     print("You Lose, opponent has Blackjack")
# else:
#   ch1 = input("Type 'y' to get another card, type 'n' to pass: ")
# while ch == 'y':
#   while (i == 0 and sum(player_cards) < 21):
#     c = random.sample(cards,1)
#     if c not in player_cards:
#       player_cards.extend(c)
#       i = 1
#   if sum(player_cards) > 21:
#     print(f"{sum(player_cards)}")
#     print("You lose")
#   ch1 = input("Type 'y' to get another card, type 'n' to pass: ") 

# if ch1 == "n":
#   print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
#   print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
#   if sum(player_cards) > sum(computer_cards):
#     print(f"p {sum(player_cards)}")
# import random
# i = 0
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# ch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# if ch == 'y':
#   while ch== 'y':
#     player_cards = random.sample(cards,2)
#     computer_cards = random.sample(cards,2)
#     def blackjack1():
#       sp = sum(player_cards)
#       cp = sum(computer_cards)
#       print(f"Your cards: {player_cards}, current score: {sp}")
#       print(f"Computer's first card: {computer_cards[0]}")
#       if cp == 21 or sp == 21:
#         if sp == 21 and cp == 21:
#           print(f"Your final hand: {player_cards}, final score: {sp}")
#           print(f"Computer's final hand: {computer_cards}, final score: {cp}")
#           print("You win, you have Blackjack")

#         if sp == 21:
#           print(f"Your final hand: {player_cards}, final score: {sp}")
#           print(f"Computer's final hand: {computer_cards}, final score: {cp}")
#           print("You win, you have Blackjack")

#         elif cp == 21:
#           print(f"Your final hand: {player_cards}, final score: {sp}")
#           print(f"Computer's final hand: {computer_cards}, final score: {cp}")
#           print("You Lose, opponent has Blackjack")
#       if sp > 21:
#         if 11 in player_cards:
#           player_cards[player_cards.index(11)] = 1
#           sp = sum(player_cards)
#           if sp > 21:
#             print(f"Your final hand: {player_cards}, final score: {sp}")
#             print(f"Computer's final hand: {computer_cards}, final score: {cp}")
#             print("You Lose, score over 21")
#           else :
#             c = input("Type 'y' to get another card, type 'n' to pass: ")
#             while c == 'y':
#               i=0
#               while (i == 0 and sum(player_cards) < 21):
#                 s = random.sample(cards,1)
#                 if s not in player_cards:
#                   player_cards.extend(s)
#                   i = 1
#               c = input("Type 'y' to get another card, type 'n' to pass: ")
#               blackjack1()
            
                



#         else:
#           c = input("Type 'y' to get another card, type 'n' to pass: ")
#           while c == 'y':
#             while (i == 0 and sum(player_cards) < 21):
#               s = random.sample(cards,1)
#               if s not in player_cards:
#                 player_cards.extend(s)
#                 i = 1
#             c = input("Type 'y' to get another card, type 'n' to pass: ")
#             blackjack1()

#     ch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

#######
#######
#######
# My Solution


# import random
# import art
# from replit import clear
# def card_deal():
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   c = random.choice(cards)
#   return c

# ch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# while ch == 'y':
#   print(art.logo)
#   player_cards = []
#   computer_cards = []
#   player_cards.append(card_deal())
#   player_cards.append(card_deal())
#   computer_cards.append(card_deal())
#   computer_cards.append(card_deal())


#   def calculate_score(cards):
#     s = sum(cards)
#     if 11 in cards:
#       if s>21:
#         cards.remove(11)
#         cards.append(1)
#         s = sum(cards)
#     if s == 21:
#       return 0
#     else:
#       return s

#   print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
#   print(f"Computer's first card: {computer_cards[0]}")

#   ps = calculate_score(player_cards)
#   cs = calculate_score(computer_cards)
#   def check(ps, cs):  
#     if ps == 0 and cs == 0:
#       print(f"Your final hand: {player_cards}, final score: {ps}")
#       print(f"Computer's final hand: {computer_cards}, final score: {cs}")
#       print("Draw, you both have a Blackjack")
#     elif ps == 0 and cs!=0:
#       print(f"Your final hand: {player_cards}, final score: {ps}")
#       print(f"Computer's final hand: {computer_cards}, final score: {cs}")
#       print("You win, you have Blackjack")
#     elif cs == 0:
#       print(f"Your final hand: {player_cards}, final score: {ps}")
#       print(f"Computer's final hand: {computer_cards}, final score: {cs}")
#       print("You Lose, opponent has Blackjack")
#     elif ps > 21 or cs >21:
#       if ps >21:
#         print(f"Your final hand: {player_cards}, final score: {ps}")
#         print(f"Computer's final hand: {computer_cards}, final score: {cs}")
#         print("You Lose, BUST")
#       else:
#         print(f"Your final hand: {player_cards}, final score: {ps}")
#         print(f"Computer's final hand: {computer_cards}, final score: {cs}")
#         print("You win, computer's BUST")
#     elif ps > cs:
#       print(f"Your final hand: {player_cards}, final score: {ps}")
#       print(f"Computer's final hand: {computer_cards}, final score: {cs}")
#       print("You win")
#     elif cs > ps:
#       print(f"Your final hand: {player_cards}, final score: {ps}")
#       print(f"Computer's final hand: {computer_cards}, final score: {cs}")
#       print("You lose, computer's BUST")



#   if ps == 0 or cs == 0:
#     check(ps,cs)
#   else:
#     ch1 = input("Type 'y' to get another card, type 'n' to pass: ")
#     i = 0 
#     while ch1 == 'y' and i == 0:
#       i = 0
#       player_cards.append(card_deal())
#       ps = calculate_score(player_cards)
      
#       print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
#       print(f"Computer's first card: {computer_cards[0]}")

#       if ps == 0 or ps > 21:
#         check(ps,cs)
#         i = 1

      
#       ch1 = input("Type 'y' to get another card, type 'n' to pass: ")
#     while cs < 17 and i == 0:
#       i = 0
#       computer_cards.append(card_deal())
#       cs = calculate_score(computer_cards)
#       if cs == 0 or cs > 21:
#         check(ps,cs)
#         i = 1
#     check(ps,cs)

#   ch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")  
#   if ch == 'y':
#     clear()


#######
#######
#######
# Given Solution
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()