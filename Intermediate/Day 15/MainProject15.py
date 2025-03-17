# Day 15
# Main Project: Coffe Machine
# Today's project is a simulation of a coffe machine.
# Program requirements:
# 1.) Prints a report on the amount of resources remaining.
# 2.) Check if the resources are sufficient.
# 3.) Process coins.
# 4.) Checks if the transaction was successful.
# 5.) Make Coffee
# 6.) Updates the amount on resources left.

import Data

def check_enough_resources(drink):
    for key in Data.MENU[drink]["ingredients"]:
        if Data.MENU[drink]["ingredients"][key] > Data.resources[key]:
            return key
    return 'True'

def updates_resources(drink):
    Data.resources["water"] -= Data.MENU[drink]["ingredients"]["water"]
    Data.resources["coffee"] -= Data.MENU[drink]["ingredients"]["coffee"]
    if drink !="espresso":
        Data.resources["milk"] -= Data.MENU[drink]["ingredients"]["milk"]


while True:
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command == 'off':
        print("Turning off...")
        break
    elif command == 'report':
        for key in Data.resources:
            print(f"{key}: {Data.resources[key]}")
        continue
    elif command == 'espresso':
        if check_enough_resources('espresso') != 'True':
            print(f"Sorry, there's not enough {check_enough_resources('espresso')}.")
            continue
    elif command == 'latte':
        if check_enough_resources('latte') != 'True':
            print(f"Sorry, there's not enough {check_enough_resources('latte')}.")
            continue
    elif command == 'cappuccino':
        if check_enough_resources('cappuccino') != 'True':
            print(f"Sorry, there's not enough {check_enough_resources('cappuccino')}.")
            continue
    else:
        print(f"Sorry, '{command}' is not a possible command.")
        continue

    print("Please insert coins.")
    value_inserted = 0
    value_inserted += 0.25*(int(input("How many quarters? ")))
    value_inserted += 0.1 *(int(input("How many dimes? ")))
    value_inserted += 0.05*int(input("How many nickles? "))
    value_inserted += 0.01*int(input("How many pennies? "))

    if value_inserted < Data.MENU[command]["cost"]:
        print("Not enough money. Money refunded...")
        break
    elif value_inserted > Data.MENU[command]["cost"]:
        print(f"Here is the {round(value_inserted - Data.MENU[command]['cost'],2)} dollars in change.")
    Data.resources["money"]+=Data.MENU[command]["cost"]
    updates_resources(command)
    print(f"Here's your {command}. Enjoy!")




