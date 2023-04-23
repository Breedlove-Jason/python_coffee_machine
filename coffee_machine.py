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

# print("What would you like? (espresso/latte/cappuccino):")
print("First Drink")
make_coffee("latte")
print("Second Drink")
make_coffee("latte")
print("Ending Resources")
print_report()

# TODO: 3. Process coins

# TODO: 4. Check transaction successful
