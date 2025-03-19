from turtle import Screen, Turtle

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
        starting_pos = 0
        for f in range(10):
            segment_part = Turtle(shape="square")
            segment_part.pu()
            self.segments.append(segment_part)
            segment_part.color("white")
            segment_part.setpos(starting_pos,0)
            starting_pos -= 20



    def move(self):
        # the segment part n moves to the position of the
        # segment part n-1 and so on until part 0, which
        # moves forward or receives a direction
        # change by the user.
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


