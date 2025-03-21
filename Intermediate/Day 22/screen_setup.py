from turtle import Turtle

class ScreenSetup:
    def __init__(self):
        t = Turtle()
        t.hideturtle()
        t.right(90)
        t.pu()
        t.color("white")
        t.width(3)
        t.goto(0, 290)
        for _ in range(29):
            t.pd()
            t.fd(12)
            t.pu()
            t.fd(8)