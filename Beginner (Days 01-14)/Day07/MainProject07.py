# Day 07: Hangman Project
# The goal is to discover the hidden word making less than 6 mistakes.
# A Hangman is going to be drawn as long as wrong answers are given.

import random

word_list = ["john", "barboza", "bastos", "vitinho", "alex telles", "marlon freitas", "gregore", "thiago almada", "savarino", "igor jesus", "luis henrique"]

word_to_guess = random.choice(word_list)
word_hidden = ["_" for f in range(len(word_to_guess))]
lives_left = 6

hangman6 = '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
hangman5 = '''
  +---+
  |   |
  o   |
      |
      |
      |
=========
'''
hangman4 = '''
  +---+
  |   |
  o   |
  |   |
      |
      |
=========
'''
hangman3 = '''
  +---+
  |   |
  o   |
 /|   |
      |
      |
=========
'''
hangman2 = '''
  +---+
  |   |
  o   |
 /|\  |
      |
      |
=========
'''
hangman1 = '''
  +---+
  |   |
  o   |
 /|\  |
 /    |
      |
=========
'''
hangman0 = '''
  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |
=========
'''
hangmans = [hangman0,hangman1,hangman2,hangman3,hangman4,hangman5,hangman6]



def mistake(letter):
    global lives_left
    lives_left -= 1

    print(f"\nYou guessed {letter}, that's not in the word. You lose a life.",end="")
    print(hangmans[lives_left], end="")
    print("*"*10+" "+str(lives_left)+"/6 LIVES LEFT "+"*"*10)

    if lives_left==0:
        return 1

def win_check():
    global word_to_guess, word_hidden
    for f in range(len(word_hidden)):
        if word_hidden[f]!=word_to_guess[f]:
            return 0
    return 1




while True:
    print("\nWord to guess: ", end="")
    for f in range(len(word_hidden)):
        if f==len(word_hidden)-1:
            print(word_hidden[f])
        else:
            print(word_hidden[f], end="")
    letter = input("guess a letter: ")

    if letter not in word_to_guess:
        if mistake(letter)==1:
            print("The word was "+ word_to_guess+"!")
            print("*"*10,"YOU LOSE","*"*10)
            break
    else:
        for f in range(len(word_to_guess)):
            if letter==word_to_guess[f]:
                word_hidden[f]=letter
        if win_check()==1:
            print(f"\nWord to be guessed: {word_to_guess}")
            print("*"*10,"YOU WIN","*"*10)
            break








