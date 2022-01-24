# def is_leap(year):
#   if year % 4 == 0:
#      if year % 100 == 0:
#        if year % 400 == 0:
#          return True
#        else:
#          return False
#      else:
#        return True
#   else:
#     return False
#
#
# def days_in_month(y, m):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(y):
#     month_days[1] = 29
#   return month_days[m-1]
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# Calculator project
from art import logo
# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operator = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


def calc():
    print(logo)
    num1 = float(input('What is the first number? '))
    for symbol in operator:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input('Please choose the operator, + or - or * or /: ')
        num2 = float(input('What is the second number? '))
        calculation_function = operator[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        cont = input('Type yes or y to continue ')
        if cont == 'y' or cont == 'yes':
            num1 = answer
        else:
            should_continue = False
            inquiry = input('Do you want to start a new calculation? ')
            if inquiry == 'yes' or inquiry == 'y':
                calc()
            else:
                should_continue = False
                break
calc()