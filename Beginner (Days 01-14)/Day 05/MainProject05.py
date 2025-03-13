# Day 05: For Loops, Range, Code Blocks
# Main Project: strong password generator
# The user is asked to give an amount of letters, symbols and numbers
# as inputs, and the program creates a password with that amount of
# those types of characters.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

chosen_characters = []
password = ""

print("Welcome to the password generator!")
nr_letters = int(input("How many letters?\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers?\n"))

for f in range(0,nr_letters):
    chosen_characters += random.choice(letters)

for f in range(0,nr_symbols):
    chosen_characters += random.choice(symbols)

for f in range(0,nr_numbers):
    chosen_characters += random.choice(numbers)

for f in range(len(chosen_characters)):
    next_character = random.choice(chosen_characters)
    password += next_character
    chosen_characters.remove(next_character)

print(f"Your password is: {password}")
