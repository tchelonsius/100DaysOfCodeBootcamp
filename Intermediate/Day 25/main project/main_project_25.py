# Day 25: CSV Data and Pandas Library
# Main Project: US States Game
# From a csv file containing a state name, and x and y values that
# represent the center of the state on the screen, the goal is to
# create a simple game that asks from the user a state name as the
# input, until they get all 50 right. Nothing happens in the case
# of an incorrect input. In the end, a csv file is containing all
# non guessed states is created.

import pandas
from turtle import Turtle, Screen
import sys

s = Screen()
s.title("U.S. States Game")
s.setup(width=725, height=491)
s.bgpic("blank_states_img.gif")

t = Turtle()
t.hideturtle()
t.pu()


def display_name(name,x,y):
    t.goto(x,y)
    t.write(name, align="center", font=("Courier", 10, "normal"))


states_file = pandas.read_csv("50_states.csv")


already_answered = []
states_list = states_file["state"].to_list()


while len(already_answered)<=50:
    answer_state = s.textinput(f"{len(already_answered)}/50 States Correct", "What's another state's name?").title()
    if answer_state == "Exit":
        break
    elif answer_state in states_list and answer_state not in already_answered:
        already_answered.append(answer_state)
        fetch = states_file[states_file["state"]==answer_state]
        display_name(answer_state, *fetch.x.values, *fetch.y.values)


# Create a csv file that contains all non guessed states.


not_guessed = []
for item in states_list:
    if item not in already_answered:
        not_guessed.append(item)

data_dict = {"states": not_guessed}

new_file = pandas.DataFrame(data_dict)
new_file.to_csv("states_to_learn.csv")

