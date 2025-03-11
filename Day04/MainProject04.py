# Day 04: Randomisation and Lists
# Main project: Rock Paper Scissors

import random

number_to_movement = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

users_number = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
users_choice = number_to_movement[users_number]
random_number = random.randint(0,2)
computer_choice = number_to_movement[random_number]
winner = None

if users_number == random_number:
    winner = "draw"
elif users_number == 0:
    if random_number == 1:
        winner = "computer wins"
    elif random_number == 2:
        winner = "player wins"
elif users_number == 1:
    if random_number == 2:
        winner = "computer wins"
    elif random_number == 0:
        winner = "player wins"
elif users_number == 2:
    if random_number == 0:
        winner = "computer wins"
    elif random_number == 1:
        winner = "player wins"


print(f"You chose: {users_choice}")
print(f"computer chose: {computer_choice}")

