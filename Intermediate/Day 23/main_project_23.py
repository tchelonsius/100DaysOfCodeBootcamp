# Day 23
# Main Project: Turtle Crossing Game
# The goal is to cross the screen with the turtle, avoiding
# being hit by the moving cars. The turtle can only move
# forwards with the "Up" key. Cars are randomly generated
# along the y-axis and will move from the right edge to the
# left edge of the screen. When the top-end is reached, the
# game levels up and the car speed increases.
# This game was broken down in 4 classes and 5 files.

from turtle import Screen
import car_generator
from game_control import GameControl
import time

# Screen configs, the tracer set to 0 makes it necessary
# to update the animations manually
s = Screen()
s.setup(width=600, height=600)
s.tracer(0)

# The Game Control class contains the Player and the
# CarGenerator objects
control = GameControl()

s.listen()
s.onkeypress(control.player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()

    # in the case of a collision with a car, the game ends
    if control.check_collision():
        control.game_over()
        break

    # if the player goes beyond the value 290 in the x-axis,
    # the value is increased.
    if control.player.pos()[1]>290:
        control.increase_level()

    # generates a new car.
    car_generator.CarGenerator(control.car_speed)

    # moves all the cars generated.
    for item in car_generator.car_list:
        item.move()

s.exitonclick()

