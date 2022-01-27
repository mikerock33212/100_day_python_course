# tw = input("Type a two digit number: ")
# print(int(tw[0]) + int(tw[1]))

# --------------
# band name generator

# create a greeting for your program
# print('Hello there, welcome to the band name generator game!')
#
# #ask user for th city they grew up in
# city = input('where do you live? \n')
#
# #ask user for the name of your pet
# pet1 = input('what is the name of your pets? \n')
#
# #combine city and pet name show their band name
# band_name = city + ' ' + pet
#
# print(f'Your band name is: {band_name}')

# ------------------
# BMI calculator

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆
# new_weight = float(weight)
# new_height = float(height)
#
# #Write your code below this line 👇
# print("{:.0f}".format(new_weight / (new_height ** 2)))

# ---------------
# age left calculator
# age = input('Tell me your age? ')
#
# days = (90 - int(age)) * 365
# weeks = (90 - int(age)) * 52
# months = (90 - int(age)) * 12
#
# print(f'You have {days} days, {weeks} weeks, and {months} months left')

# ---------------
# tip split calculator
# print('Welcome to the tip calculator')
# bill = input('How much is the total bill? ')
# tip = input('What percentage of tip would you like to give? from 5 % to 20% ')
# people = input('How many people for the bill? ')
# result = "{:.2f}".format((float(bill) + float(bill) * (float(tip)/100)) / float(people))
#
# print(f'Each person should pay {result}')
#

# ---
# BMI 2.0
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# #Write your code below this line 👇
# result = "{:.0f}".format(weight / (height ** 2))
#
# if float(result) < 18.5:
#     print(f'Your BMI is {result}, you are underweight.')
# elif float(result) > 18.5 and float(result) < 25:
#     print(f'Your BMI is {result}, you have a normal weight.')
# elif float(result) > 25 and float(result) < 30:
#     print(f'Your BMI is {result}, you are slightly overweight.')
# elif float(result) > 30 and float(result) < 35:
#     print(f'Your BMI is {result}, you are obese.')
# else:
#     print(f'Your BMI is {result}, you are clinically obese.')

# check leap year
# year = int(input('Please enter a year\n'))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Leap year.')
#         else:
#             print('Not leap year.')
#     else:
#         print('Leap year.')
# else:
#     print('Not leap year.')

# ----
# pizza price

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# # add_pepperoni = input("Do you want pepperoni? Y or N ")
# # extra_cheese = input("Do you want extra cheese? Y or N ")
# #
# # bill = 0
# #
# # if size == 'S' or size == 's':
# #     bill = 15
# #     if add_pepperoni == 'Y' or add_pepperoni == 'y':
# #         bill += 2
# #     if extra_cheese == 'Y' or extra_cheese == 'y':
# #         bill += 1
# # elif size == 'M' or size == 'm':
# #     bill = 20
# #     if add_pepperoni == 'Y' or add_pepperoni == 'y':
# #         bill += 3
# #     if extra_cheese == 'Y' or extra_cheese == 'y':
# #         bill += 1
# # elif size == 'L' or size == 'l':
# #     bill = 25
# #     if add_pepperoni == 'Y' or add_pepperoni == 'y':
# #         bill += 3
# #     if extra_cheese == 'Y' or extra_cheese == 'y':
# #         bill += 1
# #
# # print(f'Your final bill is: ${bill}')
#
# # ---
# # love calculator
# # print("Welcome to the Love Calculator!")
# # name1 = input("What is your name? \n").lower()
# # name2 = input("What is their name? \n").lower()
# #
# # combined = name1 + name2
# #
# # t = combined.count('t')
# # r = combined.count('r')
# # u = combined.count('u')
# # e = combined.count('e')
# #
# # l = combined.count('l')
# # o = combined.count('o')
# # v = combined.count('v')
# # e1 = combined.count('e')
# #
# # true = t + r + u + e
# # love = l + o + v + e1
# #
# # results = str(true) + str(love)
# # if int(results) < 10 or int(results) > 90:
# #     print(f'Your love score is {results}, you go together like coke and mentos.')
# # elif int(results) >= 40 and int(results) <= 50:
# #     print(f'Your love score is {results}, you are alright together.')
# # else:
# #     print(f'Your score is {results}')
#
# # ---
# # treasure hunt game
#
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
#
# # Write your code below this line 👇
# choice1 = input('Which way you want to go? Left or right? Type l for left, r for right\n').lower()
#
# if choice1 == 'r':
#     print('Fall into a hole. Game over.')
#     print("""
#         ________________________________
#       /                                "-_
#      /      .  |  .                       \
#     /      : \ | / :                       \
#    /        '-___-'                         \
#   /_________________________________________ \
#        _______| |________________________--""-L
#       /       F J                              \
#      /       F   J                              L
#     /      :'     ':                            F
#    /        '-___-'                            /
#   /_________________________________________--"
#
#     """)
# elif choice1 == 'l':
#     choice2 = input('Now you need to either swim or wait for a boat to continue onward. Type swim or wait\n').lower()
#     if choice2 == 'swim' or choice2 == 's':
#         print('You have been attacked by a trout, Game over. ')
#     elif choice2 == 'wait' or choice2 == 'w':
#         choice3 = input('Now you have 3 doors to enter, red, blue and yellow, '
#                         'which door do you want to enter? Type r, b or y \n').lower()
#         if choice3 == 'yellow' or choice3 == 'y':
#             print('You win!')
#         else:
#             if choice3 == 'blue' or choice3 == 'b':
#                 print('Eaten by beasts. Game over.')
#                 print("""
#                              (    )
#                   ((((()))
#                   |o\ /o)|
#                   ( (  _')
#                    (._.  /\__
#                   ,\___,/ '  ')
#     '.,_,,       (  .- .   .    )
#      \   \\     ( '        )(    )
#       \   \\    \.  _.__ ____( .  |
#        \  /\\   .(   .'  /\  '.  )
#         \(  \\.-' ( /    \/    \)
#          '  ()) _'.-|/\/\/\/\/\|
#              '\\ .( |\/\/\/\/\/|
#                '((  \    /\    /
#                ((((  '.__\/__.')
#                 ((,) /   ((()   )
#                  "..-,  (()("   /
#             pils  _//.   ((() ."
#           _____ //,/" ___ ((( ', ___
#                            ((  )
#                             / /
#                           _/,/'
#                         /,/,"
#                 """)
#             elif choice3 == 'red' or choice3 == 'r':
#                 print('Burned by fire. Game over.')
#                 print("""
#                 (  .      )
#            )           (              )
#                  .  '   .   '  .  '  .
#         (    , )       (.   )  (   ',    )
#          .' ) ( . )    ,  ( ,     )   ( .
#       ). , ( .   (  ) ( , ')  .' (  ,    )
#      (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
#  jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                 """)
# import random
# print(random.randint(0,0))

# answer = int(input('enter number'))
# print(isinstance(answer, int))
resources1 = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
resources2 = {
    "water": 100,
    "milk": 50,
    "coffee": 50,
}
for i in resources1:
    if i in resources2.keys():
        resources1[i] -= resources2[i]
        print('Found')
print(resources1)