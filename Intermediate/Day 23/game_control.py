from turtle import Turtle, Screen
from player import Player
import car_generator

# This class controls different parts of the game:
# 1.) Displays and updates the current game level;
# 2.) Checks collision between player and car;
# 3.) Displays the game over message.

class GameControl(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 10
        self.level = 1
        self.player = Player()
        self.display_configs()
        self.update_level()

    def display_configs(self):
        self.pu()
        self.hideturtle()
        self.color("black")
        self.setpos(-240, 270)

    def update_level(self):
        self.clear()
        self.player.reset_position()
        car_generator.reset_generation()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "normal"))

    def increase_level(self):
        self.level+=1
        self.car_speed += 2
        self.update_level()

    def check_collision(self):
        for item in car_generator.car_list:
            for part in item.car_parts:
                if self.player.distance(part)<12:
                    return True
        return False

    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 40, "normal"))

