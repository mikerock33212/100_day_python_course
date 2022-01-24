# paint area calculator
# import numpy as np
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
#
#
# def paint_calc(height=test_h, width=test_w, cover=coverage):
#     """calculate how many cans of paint are required"""
#     return "You'll need: " + str(np.ceil((height * width) / 5)) +' cans'
#
# print(paint_calc())


# import numpy as np
#
#
# def paint_calc(height, width, cover):
#     """calculate how many cans of paint are required"""
#     print("You'll need: " + str(np.ceil((height * width) / 5)) +' cans')
#
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# prime number checker

# def prime_checker(number):
#     """check if the given number is prime number or not"""
#     flag = True
#     if number == 1 or number <= 0:
#         flag = False
#         print("It's not a prime number.")
#     if number > 1:
#         for num in range(2, number-1):
#             if number % num == 0:
#                 flag = False
#                 print("It's not a prime number.")
#                 break
#         if flag and number % 1 == 0 and number % number == 0:
#             print("It's a prime number.")
#
#
# n = int(input("Check this number: "))
# prime_checker(number=n)
#
# def loop_prime_checker(number):
#     """check if the given number is prime number or not"""
#     for num in range(1, number + 1):
#         count = 0
#         for i in range(2, (num // 2 + 1)):
#             if num % i == 0:
#                 count += 1
#                 break
#
#         if count == 0 and num != 1:
#             print(" %d" % num)
#
# loop_prime_checker(500)

# Caesar Cipher project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(tex, shif):
#     """Encrypt the message"""
#     temp_str1 = ''
#     for char in tex:
#         if char == ' ':
#             temp_str1 += ' '
#         for i in range(len(alphabet)):
#             if char == alphabet[i]:
#                 if (len(alphabet) - 1) - i >= shif:
#                     temp_str1 += alphabet[i + shif]
#                 else:
#                     temp_str1 += alphabet[shift - ((len(alphabet)) - i)]
#     return temp_str1
#
#
# encrypted_message = encrypt(text, shift)
# print(encrypted_message)


# def encrypt_method2(plain_text, shift_amount):
#     """another way to encrypt"""
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#

# decrypt the message


def decrypt(tex, shif):
    """Decrypt the message"""
    temp_str = ''
    if shif <= len(tex):
        shif = shif
    else:
        shif = shif % len(alphabet)
    for char in tex:
        if char not in alphabet:
            temp_str += char
        for i in range(len(alphabet)):
            if char == alphabet[i]:
                if (i - shif) >= 0:
                    temp_str += alphabet[i - shif]
                else:
                    temp_str += alphabet[(i - shif)]
    return temp_str

print(decrypt('meet me at 3', 2))


# def caesar(start_text = text, shift_amount = shift, cipher_direction = direction):
#     """simplified version"""
#     end_test = ''
#     if cipher_direction == 'decode' or cipher_direction == 'd':
#         shift_amount = shift_amount * -1
#     else:
#         for char in start_text:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_test += alphabet[new_position]
#     print(f'Here is the {cipher_direction} result: {end_test}.')

