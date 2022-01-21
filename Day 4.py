import random

# random_int = random.randint(0,1)
#
# if random_int == 0:
#     print('Head')
# else:
#     print('Tail')

# ---
# pay the bill roulette
# import random
#
# names_string = input("Give me everybody's names, separated by a comma. \n")
# names = names_string.split(", ")
#
# ran = random.randint(0, len(names)-1)
# print(names[ran] + ' is going to buy the meal today!')

# ---
# treasure map game

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

location = input('Type two number to select your location, first number for column, second number for row\n')
map[int(location[1]) - 1][int(location[0]) - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")

# ---
# rock paper scissors
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
print('Welcome to rock paper scissors game!')
start = input('Would you liek to start game?\n')
if start == 'Y' or start == 'y':
    while True:
            computer_num = random.randint(0, 2)
            your_num = int(input('What do you choose? 0 for rock, 1 for paper, 2 for scissors.'))
            while your_num > 2:
                your_num = int(input('What do you choose? 0 for rock, 1 for paper, 2 for scissors, please do not go above 2.'))
            if your_num == 0:
                if computer_num == 0:
                    print(rock)
                    print(f'Computer choose: \n {rock}')
                    print('Draw')
                elif computer_num == 1:
                    print(rock)
                    print(f'Computer choose: \n {paper}')
                    print('You lose')
                elif computer_num == 2:
                    print(rock)
                    print(f'Computer choose: \n {scissors}')
                    print('You win')
            if your_num == 1:
                if computer_num == 0:
                    print(paper)
                    print(f'Computer choose: \n {rock}')
                    print('You win')
                elif computer_num == 1:
                    print(paper)
                    print(f'Computer choose: \n {paper}')
                    print('Draw')
                elif computer_num == 2:
                    print(paper)
                    print(f'Computer choose: \n {scissors}')
                    print('You lose')
            if your_num == 2:
                if computer_num == 0:
                    print(scissors)
                    print(f'Computer choose: \n {rock}')
                    print('You lose')
                elif computer_num == 1:
                    print(scissors)
                    print(f'Computer choose: \n {paper}')
                    print('You win')
                elif computer_num == 2:
                    print(scissors)
                    print(f'Computer choose: \n {scissors}')
                    print('Draw')
            choice = input('Do you want to continue?\n')
            if choice == 'Y' or choice == 'y':
                continue
            else:
                break

