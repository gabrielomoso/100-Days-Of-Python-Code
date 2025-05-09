from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def restart_coffee_machine():
    answer = input("Do you want to make another coffee? Y or N: ").lower()
    if answer == "y":
        return True
    else:
        return False

def start_machine():
    coffee_machine = True
    while coffee_machine:
        user_choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            coffee_machine = False
        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_choice == "add":
            coffee_maker.add_resources()
        else:
            drink = menu.find_drink(user_choice)
            if drink:
                is_sufficient = coffee_maker.is_resource_sufficient(drink)
                if is_sufficient:
                    payment = money_machine.make_payment(drink.cost)
                    if payment:
                        coffee_maker.make_coffee(drink)

        restart = restart_coffee_machine()
        if not restart:
            coffee_machine = False

start_machine()