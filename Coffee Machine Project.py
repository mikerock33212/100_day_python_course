MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# ------------------------


def ingredients_cost(coffee_name):
    """find how many ingredients costs for given coffee type"""
    if coffee_name == 'e' or coffee_name == 'espresso':
        return MENU['espresso']['ingredients']

    elif coffee_name == 'l' or coffee_name == 'latte':
        return MENU['latte']['ingredients']

    elif coffee_name == 'c' or coffee_name == 'cappuccino':
        return MENU['cappuccino']['ingredients']


def coffee_cost(coffee):
    '''find how much the coffee costs'''
    if coffee == 'e' or coffee == 'espresso':
        return MENU['espresso']['cost']

    elif coffee == 'l' or coffee == 'latte':
        return MENU['latte']['cost']

    elif coffee == 'c' or coffee == 'cappuccino':
        return MENU['cappuccino']['cost']


def update_stocking(user_demand, stocking):
    """update machine stocking according to user demand"""
    for x in user_demand:
        if x in stocking.keys():
            stocking[x] -= user_demand[x]
            if stocking[x] <= 0:
                return False
    return stocking



# TODO: 1 print report, how much resources left; then ask what would you like?


print('Welcome to the coffee machine, current stocking are: ')

for remaining in RESOURCES:
    print(f'{remaining}: {RESOURCES[remaining]} ml')

do_not_wants_drink = False
VENDING_MACHINE_BALANCE = 0

while not do_not_wants_drink:
    user_choice = input('Please select which coffee would you like? espresso/latte/cappuccino? ')

    COST_OF_INGREDIENTS = ingredients_cost(user_choice)

    COST_OF_COFFEE = coffee_cost(user_choice)

    print(f'The ingredients cost for this coffee is: {COST_OF_INGREDIENTS}')
    print(f'The money cost for this coffee is: {COST_OF_COFFEE}')

    remaining = update_stocking(COST_OF_INGREDIENTS, RESOURCES)

    # TODO: 2 check if resources sufficient
    if remaining:
        # TODO: 3 ask user to pay with coins
        coins = float(input('Please choose how much you would like to pay? '))
        # TODO: 4 check if money paid is enough for drink, if it is, return changes; if not, refund and notify
        if coins >= COST_OF_COFFEE:
            VENDING_MACHINE_BALANCE += COST_OF_COFFEE
            changes = coins - COST_OF_COFFEE
            print(f'Here is your change {changes}. Have a nice day! ')
        else:
            print('Not enough money, please try again! ')

        # TODO: 5 update the remaining resources and print report
        print(f'After the service remaining would be: {remaining}')
        print(f'Vending machine currently has {VENDING_MACHINE_BALANCE} in green :)')
    else:
        print('Sorry, out of stock! Please come back later! ')
        re_stock = input('Would you like to restock? ')
        if re_stock == 'yes' or re_stock == 'y':
            RESOURCES = {
                "water": 300,
                "milk": 200,
                "coffee": 100,
            }
        else:
            do_not_wants_drink = True
