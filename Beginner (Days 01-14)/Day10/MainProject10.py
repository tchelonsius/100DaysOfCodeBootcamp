# Day 10: Functions with outputs
# Main Project: Calculator
# Simple calculator with exception handling by division by zero and by the input of invalid values.

from os import system, name
import sys

def clear():
    system('cls')

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operations = {
    '+': sum,
    '-': sub,
    '*': mul,
    '/': div
}

while True:
    # This loop is outside the main one, because it's possible that the question "What is the first number"
    # is not asked again in the program.
    try:
        # It must be possible to cast the input value into a float
        number1 = float(input("What is the first number? "))
        break
    except ValueError:
        print("Invalid value. Try again.")


# main loop
while True:
    while True:
        opt = input("What is the operation? +, -, *, / ")
        if opt=='+' or opt=='-' or opt=='*' or opt=='/':
            break
        else:
            # Any other symbol is considered invalid
            print("Invalid operation. Try again.")
    while True:
        try:
            # It must be possible to cast the input value into a float
            number2 = float(input("What is the next number? "))
            break
        except ValueError:
            print("Invalid value. Try again.")

    # chooses the right operation according to the input.
    if opt=='/':
        # Avoids division by zero exception.
        while number2==0:
            number2 = float(input("Division by zero is not possible."
                                  "\nTry a different number: "))
    result = operations[opt](number1, number2)
    print(f"{number1} {opt} {number2} = {result}")

    while True:
        next = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'e' to exit: ")
        if next == 'y':
            number1 = result
            break
        elif next == 'n':
            # The console is cleared in the case of a new operation.
            clear()
            number1 = float(input("What is the first number? "))
            break
        elif next == 'e':
            sys.exit()
        else:
            print("Type a valid value.")



