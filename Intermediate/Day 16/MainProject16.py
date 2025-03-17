# Day 16: Object-Oriented Programming
# Main Project: Coffee Machine with OOP
# The classes contained in the scripts coffee_maker, menu and money_machine
# were already set up and ready to be used. The exercise was to do was understand how those
# classes are structured and work on this file to create the same version
# of the coffee_machine as done on day 15.

import coffee_maker, menu, money_machine

coffee_maker = coffee_maker.CoffeeMaker()
menu = menu.Menu()
money_machine = money_machine.MoneyMachine()

while True:
    command = input("What would you like? (espresso/latte/cappuccino) ")
    if command == 'off':
        break
    elif command == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        if menu.find_drink(command):
            drink = menu.find_drink(command)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
