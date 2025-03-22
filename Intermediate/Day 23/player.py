from turtle import Turtle

class Player(Turtle):
    # initialises the turtle controlled by the player.
    def __init__(self):
        super().__init__("turtle")
        self.pu()
        self.left(90)
        self.setpos(0,-280)

    def move(self):
        self.fd(20)

    def reset_position(self):
        self.goto(0,-280)

