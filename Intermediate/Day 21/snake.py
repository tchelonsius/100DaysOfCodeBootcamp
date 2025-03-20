from turtle import Turtle
from food import Food

UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # creates the snake with length n given in the range function
        # in order to make the head with a different shape from the tail,
        # the function extend is called 3 times instead of using a loop for it.
        # extend() can receive the shape of the new segment as a parameter, which
        # is squared by default.
        self.extend(0,0,"triangle")
        self.extend(-20, 0)
        self.extend(-40, 0)

    # creates a new piece of snake and positions it in the
    # coordinates pos_x and pos_y in the screen
    def extend(self, pos_x=None, pos_y=None, shape="square"):
        #adds a new segment to the snake
        if pos_x is None and pos_y is None:
            pos_x, pos_y = self.segments[-1].pos()
        new_segment = Turtle(shape=shape)
        new_segment.pu()
        new_segment.setpos(pos_x, pos_y)
        self.segments.append(new_segment)
        new_segment.color("white")



    def move(self):
        # the n-th segment moves to the position of the
        # (n-1)-th segment and so on until part 0, which
        # moves forward or receives a direction
        # change as a keyboard input by the user.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setpos(new_x, new_y)
        self.head.fd(20)

    # it is not possible to move to the opposite direction.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


