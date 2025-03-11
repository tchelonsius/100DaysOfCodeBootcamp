# Day 08: Functions with inputs
# Main Project: Caeser Cipher
# Simple encryption by shifting the letters by a number n or decryption by shifting by -n,
# in which n is an integer given by the user.


alphabet = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]


while True:
    action = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
    new_message = ""
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    if action == "encode":
        for letter in message:
            new_message += alphabet[(alphabet.index(letter)+shift)%26]
    elif action == "decode":
        for letter in message:
            new_message += alphabet[(alphabet.index(letter)-shift)%26]

    print(f"Here's the encoded result: {new_message}")
    again = input("Type 'yes' to go again. Otherwise type 'no'.\n")
    if again == "no":
        break

