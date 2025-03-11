# Day 03: Conditional Statements, Logical Operators, Code Blocks and Scope
# Main project: Treasure Island
# The goal is to learn above all how to use conditionals in pyhon by creating a simple interactive game that offers
# a variety of nested choices, but only one leads to the win.

print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
direction = input("left or right?\n")
if direction == "right":
    print("game over.")
else:
    action = input("swim or wait?\n")
    if action=="swim":
        print("game over.")
    else:
        door = input("which door?\n")
        if door == "red":
            print("game over.")
        elif door == "blue":
            print("game over.")
        elif door == "yellow":
            print("you win!")

