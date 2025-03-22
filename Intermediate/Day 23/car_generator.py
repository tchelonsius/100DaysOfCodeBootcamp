from car import Car
from random import randint
from turtle import Turtle

car_list = []


# When the level is increased, the car list becomes empty again
# and the cars generated so far disappear from the screen by
# calling the method hideturtle().
def reset_generation():
    global car_list
    for item in car_list:
        for part in item.car_parts:
            part.hideturtle()
    car_list = []


class CarGenerator(Turtle):
    def __init__(self, car_speed):
        # In order to control the speed in which cars are created,
        # it'll happen only when a number of value 1 is generated
        # by the random module, in a range of 3 possible numbers.
        aux = randint(1,3)
        if aux == 1:
            super().__init__()
            self.hideturtle()
            self.pu()
            self.pos_x = 320
            self.pos_y = randint(-260,260)
            self.car = Car(self.pos_x, self.pos_y, car_speed)
            car_list.append(self.car)









