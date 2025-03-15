# Day 14
# Main Project: Higher or Lower Game
# The goal is to guess, between two possibilities,
# which has the highest amount on the given aspect,
# in this case, which instagram account has more
# followers.

import game_data, random, os


already_used = []
points = 0

def pick_one():
    while True:
        result = random.choice(game_data.data)
        if result not in already_used:
            already_used.append(result)
            return result

element_A = pick_one()

while True:
    element_B = pick_one()
    print(f"Compare A: {element_A['name']}, a {element_A['description']}, from {element_A['country']}.")
    print(f"Against B: {element_B['name']}, a {element_B['description']}, from {element_B['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    answer = 'A' if element_A['follower_count']>=element_B['follower_count'] else 'B'
    if guess == answer:
        os.system('cls')
        points += 1
        print(f"You're right! Current score: {points}.")
        element_A = element_A if answer == 'A' else element_B
    else:
        print(f"Sorry, that's wrong. Final score: {points}.")
        break




