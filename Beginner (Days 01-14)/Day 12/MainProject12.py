# Day 12: Local vs. Global Scope
# Main Project: Number Guessing Project

import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Type 'easy' or 'hard': ")

lives = 10 if difficulty == 'easy' else 5
number_to_guess = random.randint(1,100)

def guessing_game():
    global number_to_guess, lives
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}.")
        return
    elif guess < number_to_guess:
        print("Too low.")
    elif guess > number_to_guess:
        print("Too high.")
    lives -= 1
    if lives == 0:
        print("You've run out of guesses.")
    else:
        guessing_game()

guessing_game()


