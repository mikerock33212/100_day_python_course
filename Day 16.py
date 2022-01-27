# from prettytable import PrettyTable
#
# x = PrettyTable()
#
#
# x.field_names = ["Pokemon Name", "Type", "Population"]
# x.add_row(["Pikachu",'Electric', 1158259])
# x.add_row(["Squirtle",'Water', 1857594])
# x.add_row(["Charmander", 'Fire', 120900])
#
# x.align = 'c'
# print(x)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# menu_item_name = MenuItem()

my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
# TODO: print report of machine resources and machine balance
my_money_machine.report()
coffee_maker.report()


# TODO: check resources sufficient
while is_on:
    option = menu.get_items()
    choice = input(f'What would you like? {option}: or you can type o for off, r for report ')
    if choice == 'off' or choice == 'o':
        is_on = False
    elif choice == 'report' or choice == 'r':
        my_money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        # TODO: check resources sufficient
        if coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

