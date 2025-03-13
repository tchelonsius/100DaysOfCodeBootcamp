# Day 09: Dictionaries and Nesting
# Main Project: The Secret Auction Program
# This Script simulates an Action Program, in which the participants enter their names
# and their bids as inputs *anonymously*. For that to happen, the clear() function was
# implemented, so that after every user input, the next one doesn't have access to the
# previous bid proposed. In the end, the greatest bid and its according owner are
# displayed on the console.

from os import system, name
#define our clear function
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('cls')

bids = {}

print("Welcome to the secret auction program.")

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bids[bid]=name
    others = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if others == "yes":
        clear()
    else:
        clear()
        break

greatest = 0

for key in bids:
    if key>greatest:
        greatest = key

print(f"The winner is {bids[greatest].capitalize()} with a bid of ${greatest}.")

