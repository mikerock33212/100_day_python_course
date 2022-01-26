# from random import randint
# from art import logo_blackJack
#
# card_set = []
#
#
# # build the deck first
#
#
# def create_cards():
#     """create sets of cards"""
#     points = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     pattern = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#     cards = {}
#     for index in range(len(points)):
#         cards[pattern[index]] = points[index]
#     return cards
#
#
# def pop_key(dictionary_set):
#     """pop remaining key from deck cardset"""
#     tem_lst = []
#     for key in dictionary_set:
#         tem_lst.append(key)
#     ram_index = randint(0, len(tem_lst) - 1)
#     return tem_lst[ram_index]
#
#
# def deal_cards():
#     """deal cards from deck, remove cards afterwards"""
#     random_set = randint(0, len(card_set) - 1)
#     temp_key = pop_key(card_set[random_set])
#     temp_card_value = card_set[random_set][temp_key]
#     card_set[random_set].pop(temp_key)
#     return temp_key, temp_card_value
#
#
# def check_win(yourscore, dealerscore):
#     """check if winning condition met"""
#     if yourscore == 21:
#         if dealerscore == 21:
#             return 'Draw'
#         else:
#             return 'Win'
#     elif yourscore == 21 and dealerscore != 21:
#         return 'Win'
#     elif yourscore < 21:
#         if dealerscore == 21:
#             return 'Lose'
#         if dealerscore > 21:
#             return 'Win'
#     elif yourscore > 21:
#         return 'Lose'
#
#
# # need to decide how many set of cards you would like to play? Default is 1
#
#
# card_set_num = (input('Please select how many set of cards you want to play, default is 1: '))
# while not card_set_num.isnumeric():
#     card_set_num = (input('Please enter a valid number! '))
# if int(card_set_num) > 0:
#     for i in range(int(card_set_num)):
#         card_set.append(create_cards())
#
# print(logo_blackJack)
# print('Welcome to Black Jack 21! ')
# print('Initial card set is: ', card_set)
#
# try:
#     dealer_money_pool = int(input('Please specify dealer money pool: '))
# except ValueError:
#     dealer_money_pool = int(input('Please specify dealer money pool with a valid number input: '))
#
# try:
#     your_initial_money = int(input('Please decide how much money you would like to play total for this game: '))
# except ValueError:
#     your_initial_money = int(input('Please enter a valid number for your initial money: '))
#
# # start the game
# start_game = input('Would you like to start the game? Type yes or y to begin: ')
# while start_game == 'yes' or start_game == 'y':
#     your_bet = int(input('Please enter your bet to start game: '))
#     your_initial_money -= your_bet
#     print(f'Your money left: {your_initial_money}, your bet {your_bet}')
#     your_cards = []
#     dealer_cards = []
#     your_score = 0
#     dealer_score = 0
#     try:
#         your_cards.append(deal_cards())
#         your_cards.append(deal_cards())
#         dealer_cards.append(deal_cards())
#         dealer_cards.append(deal_cards())
#     except (ValueError, IndexError):
#         print('You have run out of cards, game over.')
#     else:
#         print(f'This is your cards: {your_cards}')
#         print(f'This is dealer cards: {dealer_cards[0]}')
#         print(f'This is the cards left: {card_set}')
#     your_score += your_cards[0][1]
#     your_score += your_cards[1][1]
#     dealer_score += dealer_cards[0][1]
#     dealer_score += dealer_cards[1][1]
#     if check_win(your_score, dealer_score) == 'Win':
#         your_initial_money += (your_bet * 2)
#         dealer_money_pool -= your_bet
#         print(your_cards, dealer_cards)
#         print(f'You Win! Your balance right now is: {your_initial_money}')
#         if dealer_money_pool <= 0:
#             print('OMG, you beat the dealer, dealer is now broke! Game is over!')
#             break
#         start_game = input('Would you like to start the game again? ')
#     elif check_win(your_score, dealer_score) == 'Lose':
#         dealer_money_pool += your_bet
#         print(your_cards, dealer_cards)
#         print(f'You lose! Your balance right now is: {your_initial_money}')
#         if your_initial_money <= 0:
#             print('OMG, you are now broke! Game is over!')
#             break
#         start_game = input('Would you like to start the game again? ')
#     elif check_win(your_score, dealer_score) == 'Draw':
#         your_initial_money += your_bet
#         print(your_cards, dealer_cards)
#         print(f'Draw! Your balance right now is: {your_initial_money}')
#         start_game = input('Would you like to start the game again? ')
#     else:
#         your_counter = 2
#         dealer_counter = 2
#         choice = input('Would you like to hit for another card? ')
#         if choice == 'no' or choice == 'n':
#             if 21 > dealer_score >= 17:
#                 if check_win(your_score, dealer_score) == 'Win':
#                     your_initial_money += (your_bet * 2)
#                     dealer_money_pool -= your_bet
#                     print(your_cards, dealer_cards)
#                     print(f'You WIn! Your balance right now is: {your_initial_money}')
#                     if dealer_money_pool <= 0:
#                         print('OMG, you beat the dealer, dealer is now broke! Game is over!')
#                         break
#                 elif check_win(your_score, dealer_score) == 'Lose':
#                     dealer_money_pool += your_bet
#                     print(your_cards, dealer_cards)
#                     print(f'You lose! Your balance right now is: {your_initial_money}')
#                     if your_initial_money <= 0:
#                         print('OMG, you are now broke! Game is over!')
#                         break
#                 elif check_win(your_score, dealer_score) == 'Draw':
#                     your_initial_money += your_bet
#                     print(your_cards, dealer_cards)
#                     print(f'Draw! Your balance right now is: {your_initial_money}')
#
#             while dealer_score < 17:
#                 dealer_cards.append(deal_cards())
#                 dealer_score += dealer_cards[dealer_counter][1]
#                 dealer_counter += 1
#                 print(dealer_cards, dealer_score)
#             if dealer_score == 21:
#                 dealer_money_pool += your_bet
#                 print(your_cards, dealer_cards)
#                 print(f'You lose! Your balance right now is: {your_initial_money}')
#                 if your_initial_money <= 0:
#                     print('OMG, you are now broke! Game is over!')
#                     break
#             if dealer_score > 21:
#                 your_initial_money += (your_bet * 2)
#                 dealer_money_pool -= your_bet
#                 print(your_cards, dealer_cards)
#                 print(f'You WIn! Your balance right now is: {your_initial_money}')
#                 if dealer_money_pool <= 0:
#                     print('OMG, you beat the dealer, dealer is now broke! Game is over!')
#                     break
#             if 17 <= dealer_score < 21:
#                 if check_win(your_score, dealer_score) == 'Win':
#                     your_initial_money += (your_bet * 2)
#                     dealer_money_pool -= your_bet
#                     print(your_cards, dealer_cards)
#                     print(f'You WIn! Your balance right now is: {your_initial_money}')
#                     if dealer_money_pool <= 0:
#                         print('OMG, you beat the dealer, dealer is now broke! Game is over!')
#                         break
#                 elif check_win(your_score, dealer_score) == 'Lose':
#                     dealer_money_pool += your_bet
#                     print(your_cards, dealer_cards)
#                     print(f'You lose! Your balance right now is: {your_initial_money}')
#                     if your_initial_money <= 0:
#                         print('OMG, you are now broke! Game is over!')
#                         break
#                 elif check_win(your_score, dealer_score) == 'Draw':
#                     your_initial_money += your_bet
#                     print(your_cards, dealer_cards)
#                     print(f'Draw! Your balance right now is: {your_initial_money}')
#         if choice == 'yes' or choice == 'y':
#             your_cards.append(deal_cards())
#             your_score += your_cards[your_counter][1]
#             your_counter += 1
#             print(your_cards, your_score)
#             if your_score == 21:
#                 your_initial_money += (your_bet * 2)
#                 dealer_money_pool -= your_bet
#                 print(your_cards, dealer_cards)
#                 print(f'You WIn! Your balance right now is: {your_initial_money}')
#                 if dealer_money_pool <= 0:
#                     print('OMG, you beat the dealer, dealer is now broke! Game is over!')
#                     break
#             if your_score < 21:
#                 choice = input('Would you like to hit for another card? ')
#             if your_score > 21:
#                 dealer_money_pool += your_bet
#                 print(your_cards, dealer_cards)
#                 print(f'Busted! You lose! Your balance right now is: {your_initial_money}')
#     start_game = input('Would you like to start the game? Type yes or y to begin: ')

# enter your bet

# 2 cards for you, 1 of cards face above for dealer, another 1 face down

# if you have A, or you have both same cards, you can always split;

# if you choose to split, then your bet is doubled; initial 2 cards split, and you're given 2 cards each
# for 2 new pair of cards, then you need to decide if you want to hit or stay put for both pair


# if your score equal 21 you win, or dealer equal 21 deal wins, or both 21, you draw

# do you want to hit

# if you do hit, check if your score <= 21, if == 21, then bet += bet

# if you do not, dealer continue to draw until above 17 to stop

# else dealer bust, you win

# if deal score between 17 and 21, and score greater than your, you lose

# ask do you want to continue the game?


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
import random
from art import logo_blackJack


def deal_card():
    """return random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.


def compare(userscore, computerscore):
    """compare"""

    if userscore == computerscore:
        return 'Draw!'
    elif computerscore == 0:
        return 'Lose, opponent has a Black Jack!'
    elif userscore == 0:
        return 'Win, you have a Black Jack!'
    elif userscore > 21:
        return 'You busted, over 21!'
    elif computerscore > 21:
        return 'Your opponent busted, over 21, you win!'
    elif userscore > computerscore:
        return 'You win!'
    elif userscore < computerscore:
        return 'You lose!'


def play_game():

  print(logo_blackJack)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

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
  if sum(user_cards) > 21:
      pass
  else:
      while computer_score != 0 and computer_score < 17:
          computer_cards.append(deal_card())
          computer_score = calculate_score(computer_cards)

  print('Game Over!')
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()



#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
