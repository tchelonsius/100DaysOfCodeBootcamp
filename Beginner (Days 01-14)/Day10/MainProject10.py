# Day 10: Functions with outputs
# Main Project: Calculator
# Simple calculator with exception handling by division by zero and by the input of invalid values.

import sys

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

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
    result = 0
    # chooses the right operation according to the input.
    if opt =="+":
        result = sum(number1, number2)
        print(f"The result is {result}")
    elif opt =="-":
        result = sub(number1, number2)
        print(f"The result is {result}")
    elif opt =="*":
        result = mul(number1, number2)
        print(f"The result is {result}")
    elif opt =="/":
        try:
            # If the second number is zero and operation is division,
            # it is going to ask the user for a different value.
            result = div(number1, number2)
            print(f"The result is {result}")
        except ZeroDivisionError:
            print("Invalid input.")
            while True:
                number2 = float(input("Type a valid divisor: "))
                if number2!=0:
                    result = div(number1,number2)
                    print(f"The result is {result}")
                    break

    while True:
        next = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'e' to exit: ")
        if next == 'y':
            number1 = result
            break
        elif next == 'n':
            number1 = float(input("What is the first number? "))
            break
        elif next == 'e':
            sys.exit()
        else:
            print("Type a valid value.")



