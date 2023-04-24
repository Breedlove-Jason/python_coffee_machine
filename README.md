# Coffee Machine

This is a simple command-line Python program that simulates a coffee machine. The coffee machine offers three different types of coffee: espresso, latte, and cappuccino. Users can interact with the coffee machine to select a drink, insert coins, and receive change. The program also includes a report feature to display the machine's resources and earnings.

## Features

* Select from three different coffee types:
  * Espresso
  * Latte
  * Cappuccino
* Insert coins (quarters, dimes, nickels, and pennies)
* Receive change if overpayment occurs
* Print a report of the coffee machine's resources and earnings

## Dependencies

To run this program, you need Python 3.x installed on your machine.

## How to run

1. Clone this repository or download the files.
2. Navigate to the folder containing the `coffee_machine.py` file in your terminal or command prompt.
3. Run the command `python coffee_machine.py` to start the program.

## Usage

The program will prompt you to enter your desired drink:

```
What would you like? (espresso = 'esp' | latte = 'lat' | cappuccino = 'cap' | report)
```

Type `esp`, `lat`, or `cap` to select espresso, latte, or cappuccino, respectively.

After selecting a drink, you will be asked to insert coins. Type the number of each coin type you are inserting:

```
Please insert coins.
How many quarters?:
How many dimes?:
How many nickles?:
How many pennies?:
```

If you have inserted enough money, the coffee machine will dispense the drink and return change if necessary. If not, the transaction will be cancelled and the money refunded.

To print a report of the coffee machine's resources and earnings, type `report` at the main prompt.

To turn off the coffee machine, type `off` at the main prompt.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).