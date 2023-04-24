from menu import MENU, resources
from art import logo

print(logo)


def print_report(total):
    """Print report of all coffee machine resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total:.2f}")


def make_coffee(drink_name):
    """Deduct resources from coffee machine and check that there are enough resources to make the drink"""
    for key, value in MENU[drink_name]["ingredients"].items():
        resources[key] -= value
        if resources[key] < 0:
            print(f"Sorry there is not enough {key}.")
            resources[key] += value
            return False
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    return True


def coins_operate():
    """Process coins and return total"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return round(total, 2)


print("Welcome to the Coffee Machine")

machine_total = 0
coffee_loop = True
while coffee_loop:
    if resources["water"] < 0 or resources["milk"] < 0 or resources["coffee"] < 0:
        print("Sorry, there is not enough resources to make another drink.")
        coffee_loop = False
        break

    user_input = input("What would you like? (espresso = 'esp' | latte = 'lat' | cappuccino = 'cap' | report) ")

    if user_input == 'esp':
        money = coins_operate()
        if money >= MENU["espresso"]["cost"]:
            money -= MENU["espresso"]["cost"]
            make_coffee("espresso")
            machine_total += MENU["espresso"]["cost"]
            print(f"Here is ${money:.2f} in change.")
            continue
        else:
            print("Sorry that's not enough money. Money refunded.")
        break
    elif user_input == 'lat':
        money = coins_operate()
        if money >= MENU["latte"]["cost"]:
            money -= MENU["latte"]["cost"]
            make_coffee("latte")
            machine_total += MENU["latte"]["cost"]
            print(f"Here is ${money:.2f} in change.")
            continue
        else:
            print("Sorry that's not enough money. Money refunded.")
            break
    elif user_input == 'cap':
        money = coins_operate()
        if money >= MENU["cappuccino"]["cost"]:
            money -= MENU["cappuccino"]["cost"]
            make_coffee("cappuccino")
            machine_total += MENU["cappuccino"]["cost"]
            print(f"Here is ${money:.2f} in change.")
            continue
        else:
            print("Sorry that's not enough money. Money refunded.")
            break
    elif user_input == 'report':
        print_report(machine_total)
        continue
    elif user_input == 'off':
        coffee_loop = False
        break
    else:
        print("Invalid input")
        continue
