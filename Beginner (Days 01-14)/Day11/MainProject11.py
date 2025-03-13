# Day 11
# Main Project: Blackjack Capstone Project
# Game between 2 players. The goal of is to have cards that sum up as close as possible to 21.
# If the sum goes beyond that, you lose.

import random, sys, os
from turtledemo.nim import computerzug

possible_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

players_hand = []
computers_hand = []

def hands_sum(cards):
    return sum(cards)

def print_current_points():
    print(f"\tYour cards: {players_hand}, current score: {hands_sum(players_hand)}")
    print(f"\tComputer's first card: {computers_hand[0]}")

def print_final_points():
    print(f"\tYour final hand: {players_hand}, final score: {hands_sum(players_hand)}")
    print(f"\tComputer's final hand: {computers_hand}, final score: {hands_sum(computers_hand)}")

def end_game(message=None):
    while hands_sum(computers_hand)<14:
        computers_hand.append(random.choice(possible_cards))

    print_final_points()
    if hands_sum(players_hand)>hands_sum(computers_hand):
        print("You win! :)" if message is None else message)
    elif hands_sum(computers_hand)>hands_sum(players_hand):
        print("You lose :(" if message is None else message)
    else:
        print("Same amount on points. Draw!")

while True:
    for _ in range(2):
        players_hand.append(random.choice(possible_cards))
        computers_hand.append(random.choice(possible_cards))

    while True:
        if hands_sum(players_hand)>21:
            if 11 in players_hand:
                players_hand.remove(11)
                players_hand.append(1)
            else:
                end_game("You went over. You lose :(")
                break
        elif hands_sum(computers_hand)>21:
            if 11 in computers_hand:
                computers_hand.remove(11)
                computers_hand.append(1)
            else:
                end_game("Computer went over. You win! :)")
                break
        elif hands_sum(players_hand)==21:
            end_game("You win with a Blackjack! :)")
            break
        elif hands_sum(computers_hand)==21:
            end_game("Computer wins with a Blackjack! :)")
            break

        print_current_points()
        move = input("Type 'y' to get another card, type 'n' to pass: ")
        if move == 'n':
            end_game()
            break
        else:
            players_hand.append(random.choice(possible_cards))

    again = input("Do you want to play again? Type 'y' or 'n': ")

    if again=='y':
        players_hand = []
        computers_hand = []
        os.system('cls')
    else:
        sys.exit()



