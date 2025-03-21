from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.pu()
        self.color("white")
        self.setpos(0, 0)
        self.x_move = 10
        self.y_move = -10
        # The move_speed determines for how long the program
        # sleeps in the loop from the main file.
        self.move_speed = 0.06

    def move(self):
        # changes the direction of y if it hits the upper or the lower bound
        if self.pos()[1] > 280 or self.pos()[1] < -280:
            self.bounce_y()
        # new position is the current one plus the respective move rates
        # (x_move and y_move), that can have their values changed by other
        # methods in this class.
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    # The bounce_x method is supposed to be called when the ball
    # hits one of the paddles, so that's when the sleep time is
    # decreased, and the move_speed increased.
    def bounce_x(self):
        self.move_speed *= 0.97
        self.x_move *= -1

    def change_direction(self):
        self.x_move *= -1
        self.y_move *= -1

    def reset_position(self):
        self.goto(0,0)





