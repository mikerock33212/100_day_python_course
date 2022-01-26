# # number gessing game
# import random
# # a = []
# # for i in range(100):
# #     a.append(i)
# # print(random.choice(a))
#
# # generate a random number between 1 and 100
#
#
# def generate_number(num):
#     """generate a random number between 1 and given number"""
#     temp_lst = []
#     for i in range(1, num + 1):
#         temp_lst.append(i)
#     return random.choice(temp_lst)
#
#
# def difficulty(str_selection):
#     """return attempts according to user choice"""
#     if str_selection == 'easy' or str_selection == 'e':
#         return 10
#     else:
#         return 5
#
#
# def check(usernumber):
#     """check the user guessed number with hidden answer number"""
#     if usernumber == HIDDEN_ANSWER:
#         return('You won the guess!')
#     if usernumber > HIDDEN_ANSWER:
#         return('Higher, guess again.')
#     if usernumber < HIDDEN_ANSWER:
#         return('Lower, guess again.')
#
#
#
#
# UP_LIMIT_NUM = int(input('Please enter a number to begin: '))
# HIDDEN_ANSWER = generate_number(UP_LIMIT_NUM)
# # select difficulty, easy, medium or hard
# DIFF = input('Please select your difficulty to begin the game: ')
# DIFFICULTY_GAME = difficulty(DIFF)
# # tell the user how many attempts remaining according to difficulty
# print(f'Now you have {DIFFICULTY_GAME} attempts left. ')
#
# game_end = False
# while not game_end and DIFFICULTY_GAME > 0:
#     # ask user to input a number
#     user_choice = int(input('Please enter a number to guess: '))
#     checkanswer = check(user_choice)
#     if checkanswer == 'You won the guess!':
#         game_end = True
#         print('You won, game over.')
#     if checkanswer == 'Higher, guess again.':
#         DIFFICULTY_GAME -= 1
#         print(f'{checkanswer} You have {DIFFICULTY_GAME} attempts left.')
#         if DIFFICULTY_GAME == 0:
#             game_end = True
#             print('You lose with no attempts left.')
#     if checkanswer == 'Lower, guess again.':
#         DIFFICULTY_GAME -= 1
#         print(f'{checkanswer} You have {DIFFICULTY_GAME} attempts left.')
#         if DIFFICULTY_GAME == 0:
#             game_end = True
#             print('You lose with no attempts left.')

# another version from tutorial
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turn):
    """check and return turn - 1"""
    if guess > answer:
        print('Too high.')
        return turn - 1
    elif guess < answer:
        print('Too low.')
        return turn - 1
    else:
        print(f'You got it, answer is {answer}.')


def set_difficulty():
    level = input('Choose difficulty, easy or hard: ')
    if level == 'easy' or level == 'e':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# choose a random numnber between 1 and 100
def play_game():
    print('Welcome to the guessing game')
    print('Generating a numnber between 1 and 100...')
    answer = random.randint(1,100)
    turns = set_difficulty()
    print(f'You have {turns} attempts left.')

    # let user guess a number
    guess = 0
    while guess != answer:
        guess = int(input('Make a guess: '))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('You have run out of attempts, game over.')
            break
        elif guess == answer:
            break
        else:
            print(f'Guess again. Now you have {turns} attempts left.')
play_game()
    # track the number of turns and reduce by 1 if user is wrong
