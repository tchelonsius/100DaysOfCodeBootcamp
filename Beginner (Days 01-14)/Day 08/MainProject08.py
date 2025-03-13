# Day 08: Functions with inputs
# Main Project: Caeser Cipher
# Simple encryption by shifting the letters by a number n or decryption by shifting by -n,
# in which n is an integer given by the user.


alphabet = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]

def action(message, shift, direction):
    new_message = ""
    if direction == "encode":
        for letter in message:
            new_message += alphabet[(alphabet.index(letter)+shift)%26]
    elif direction == "decode":
        for letter in message:
            new_message += alphabet[(alphabet.index(letter)-shift)%26]
    return new_message


while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    new_message = action(message, shift, direction)
    print(f"Here's the encoded result: {new_message}")
    again = input("Type 'yes' to go again. Otherwise type 'no'.\n")
    if again == "no":
        break

