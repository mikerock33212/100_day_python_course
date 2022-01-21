# calculate average height

# student_heights = '150 142 185 120 171 184 149 199'
# stu_split = student_heights.split()
# for n in range(0, len(stu_split)):
#   stu_split[n] = int(stu_split[n])
# print(stu_split)
# # 🚨 Don't change the code above 👆
# sum = 0
# for num in stu_split:
#   sum += num
# print(round(sum / len(stu_split)))

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# pointer = 0
# for i in range(len(student_scores) - 1):
#   if student_scores[i] > student_scores[i+1] and student_scores[i] > pointer:
#     pointer = student_scores[i]
#   elif student_scores[i] == student_scores[i+1]:
#     pass
#   elif student_scores[i] < student_scores[i+1] and student_scores[i+1] > pointer:
#     pointer = student_scores[i+1]
# print(pointer)

# for i in student_scores:
#   if i > pointer:
#     pointer = i
# print(pointer)

# fizzbuzz game
# for i in range(1,101):
#   if i % 3 == 0 and i % 5 == 0:
#     print('FizzBuzz')
#   if i % 3 == 0:
#     print('Fizz')
#   elif i % 5 == 0:
#     print('Buzz')
#   else:
#     print(i)

# ---
# password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

result = ''
for i in range(nr_letters):
  result += letters[random.randint(0, len(letters)) - 1]
for x in range(nr_symbols):
  result += symbols[random.randint(0,len(symbols)) - 1]
for y in range(nr_numbers):
  result += numbers[random.randint(0, len(numbers)) - 1]

print(result)

print(''.join(random.choice(result) for i in range(len(result))))
