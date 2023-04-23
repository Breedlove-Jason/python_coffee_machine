from menu import MENU, resources


# 3 Hot Flavors


# Coins Operate

def print_report():
    """Print report of all coffee machine resources"""
    for key, value in resources.items():
        print(f"{key}: {value}")


def make_coffee(drink_name):
    """Deduct resources from coffee machine and check that there are enough resources to make the drink"""
    for key, value in MENU[drink_name]["ingredients"].items():
        resources[key] -= value
        if resources[key] < 0:
            print(f"Sorry there is not enough {key}.")
            resources[key] += value
            return

    print(f"Here is your {drink_name} ☕️. Enjoy!")


print("Welcome to the Coffee Machine")
print_report()

coffee_loop = True
while coffee_loop:
    if resources["water"] < 0 or resources["milk"] < 0 or resources["coffee"] < 0:
        print("Sorry, there is not enough resources to make another drink.")
        coffee_loop = False
        break
    user_input = int(input("What would you like? (1. for espresso | 2. for latte | 3. for cappuccino):"))
    if user_input == 1:
        make_coffee("espresso")
    elif user_input == 2:
        make_coffee("latte")
    elif user_input == 3:
        make_coffee("cappuccino")
    else:
        print("Invalid input")

print("Ending Resources")
print_report()


# TODO: 3. Process coins

# TODO: 4. Check transaction successful
