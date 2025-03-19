# Day 19: More on Turtle graphics, Event Listeners, State and multiple
# Main Project: Turtles Race
# In this exercise, 6 turtles race against each other by moving a random
# amount of pixels. The user is asked to bet on which color he thinks
# is going to win. If he gets it right, he wins, if not, he loses.
# There's also an end line to show where the race is supposed to end.


from turtle import Turtle, Screen
import random

colours = ["purple", "red", "green", "blue", "orange", "pink"]
turtles_list = []
winner = None

s = Screen()
start_pos = -150
t = Turtle()
t.hideturtle()

def draw_crossing_line():
    t.speed("fastest")
    t.pu()
    t.setpos(200,170)
    t.right(90)
    for f in range(10):
        t.pd()
        t.fd(30)
        t.pu()
        t.fd(7)
    t.left(90)
    t.pu()

def check_winner():
    global winner
    for item in turtles_list:
        if item.pos()[0] >= 200:
            winner = item
            return True
    else:
        return False

draw_crossing_line()

# positions the 6 turtles on the screen and adds them to a list
for f in range(6):
    t = Turtle()
    turtles_list.append(t)
    t.pu()
    t.shape("turtle")
    t.shapesize(2)
    colour = random.choice(colours)
    t.color(colour)
    colours.remove(colour)
    t.setpos(-200, start_pos)
    start_pos += 50

bet = s.textinput("Bet", "Choose the colour you think is gonna win: ")

#game
while not check_winner():
    for item in turtles_list:
        item.fd(random.randint(1,10))

if bet==winner.color()[0]:
    print(f"{bet.capitalize()} is the winner, you win!")
else:
    print(f"{str(winner.color()[0]).capitalize()} is the winner, you lose.")


s.exitonclick()



