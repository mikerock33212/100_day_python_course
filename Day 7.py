# import random
# import urllib.request as req
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
#
# def random_word_generator():
#     """return a random word from word site"""
#     word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
#     res = req.urlopen(word_site, timeout=500)
#     txt = res.read()
#     processed = txt.splitlines()
#     final_res = []
#     for i in processed:
#         final_res.append(i.strip().decode('utf-8'))
#     random_num = random.randint(0, len(final_res) - 1)
#     return final_res[random_num]
# aaa = random_word_generator()
# print(aaa)
# life = 6
# fil_answer = "_" * len(aaa)
# temp_list = list(fil_answer)
# result = ''
# while fil_answer != aaa and life > 0:
#     your_word = input('Please guess a character in a word\n')
#     if your_word in temp_list:
#         life -= 1
#         print(stages[life])
#     for i in range(len(aaa)):
#         if your_word == aaa[i]:
#             temp_list[i] = aaa[i]
#     if your_word not in aaa:
#         life -= 1
#         print(stages[life])
#     for y in temp_list:
#         result += y
#     if result == aaa:
#         fil_answer = result
#         print(aaa)
#         print('You have saved hangman')
#         break
#     elif life <= 0:
#         print(temp_list)
#         print(f'You have {life} left. Game Over!')
#         print(stages[0])
#         break
#     else:
#         result = ''
#         print(temp_list)
#         print(life)
#         continue

#Step 1

# import random
#
# word_list = ["aardvark", "baboon", "camel"]
#
# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#
# chosen_word = word_list[random.randint(0, len(word_list) - 1)]
#
# guess = input('Guess a letter.\n').lower()
# temp_list = []
#
# for i in chosen_word:
#     if i == guess:
#         temp_list.append('RIGHT')
#     else:
#         temp_list.append('WRONG')
#
# for x in temp_list:
#     print(x)

