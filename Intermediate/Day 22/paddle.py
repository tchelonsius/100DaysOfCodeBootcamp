from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos_x):
        super().__init__("square")
        self.direction = 90
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.pu()
        self.goto(pos_x, 0)
        self.left(90)
        self.color("yellow")

    # moves paddle up
    def move_up(self):
        if self.pos()[1]>230:
            return
        self.fd(20)

    # moves paddle down
    def move_down(self):
        if self.pos()[1]<-225:
            return
        self.bk(20)

    # the game can also be played with one (or both) paddle(s)
    # being automatically moved by the auto_move() method.
    def auto_move(self):
        if self.pos()[1]>=230:
            self.direction = 270
        elif self.pos()[1] <= -230:
            self.direction = 90
        self.setheading(self.direction)
        self.fd(40)


