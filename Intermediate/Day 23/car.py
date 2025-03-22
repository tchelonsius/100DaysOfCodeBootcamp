# In order to detect collisions between the player turtle
# and the cars with more precision, the car is formed by
# two turtle objects that positioned together in the screen,
# so that it seems like only one object.

from turtle import Turtle, Screen
from random import randint

Screen().colormode(255)

# Function to generate a random color for a new car.
def random_color():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    return r, g, b

class Car:
    def __init__(self, pos_x, pos_y, car_speed):
        self.car_parts = []
        self.car_speed = car_speed
        self.color = random_color()
        # the car is formed by two square shaped turtles.
        for f in range(2):
            self.t = Turtle("square")
            self.t.pu()
            self.t.color(self.color)
            self.t.left(180)
            self.t.setpos(pos_x, pos_y)
            self.car_parts.append(self.t)
            pos_x += 10

    def move(self):
        for part in self.car_parts:
            if part.pos()[0]>-320:
                part.fd(self.car_speed)



