import rss


def report():
    print(f"Water: {resources_water}ml")
    print(f"Milk: {resources_milk}ml")
    print(f"Coffee: {resources_coffee}g")
    print(f"Money: ${money}")


def check_resources():
    if resources_water < water:
        return "Sorry there is not enough water"
    elif resources_milk < milk:
        return "Sorry there is not enough milk"
    elif resources_coffee < coffee:
        return "Sorry there is not enough coffee"
    else:
        return True


def process_payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total = quarters + dimes + nickles + pennies

    if total < cost:
        return "Sorry that is not enough money. Money refunded"
    else:
        change = round(total - cost, 2)
        return change


def update_resources():
    global money, resources

    resources = {
        "water": resources_water - water,
        "milk": resources_milk - milk,
        "coffee": resources_coffee - coffee
    }

    money += cost


def get_user_choice():
    user_answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while (user_answer != "espresso" and user_answer != "latte" and user_answer != "cappuccino" and user_answer != "end"
           and user_answer != "report"):
        print("Sorry, You have inputted a wrong option")
        print("Please select from the options given")
        user_answer = input("espresso/latte/cappuccino: ").lower()

    return user_answer


resources = rss.resources
MENU = rss.MENU
money = 0
coffee_machine = True


while coffee_machine:
    user_choice = get_user_choice()

    if user_choice == "end":
        coffee_machine = False
    elif user_choice == "report":
        report()
    else:
        menu = MENU[user_choice]

        ingredients = menu["ingredients"]
        water = ingredients["water"]
        milk = ingredients["milk"]
        coffee = ingredients["coffee"]
        cost = menu["cost"]

        resources_water = resources["water"]
        resources_milk = resources["milk"]
        resources_coffee = resources["coffee"]

        sufficient = check_resources()

        if sufficient == True:
            user_change = process_payment()
            if type(user_change) == float:
                print(f"Here is {user_change} in change.")
                print(f"Here is your {user_choice} ☕ Enjoy!")
                update_resources()
            else:
                print(user_change)
        else:
            print(sufficient)
