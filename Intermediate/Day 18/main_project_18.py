# Day 18: Turtle Graphics Documentation
# Main Project: The Hirst Painting Project
# This script draws and ordered sequence of dots
# on the screen accordingly to the screen's width
# and height with random colors, simulating
# the paintings from the artist Hirst.

from turtle import Turtle, Screen
import random, colorgram

t = Turtle()
s = Screen()

t.hideturtle()
t.speed("fastest")
s.colormode(255)
s.setup(768,648,-384,-324)

def random_color():
    r = random.randint(1,255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r,g,b


print(s.window_width())
print(s.window_height())
print(s.setup())


for f in range(-int(s.window_height()/2)+25, int(s.window_height()/2), 60):
    for i in range(-int(s.window_width()/2)+25, int(s.window_width()/2),60):
        t.pu()
        t.setpos(i,f)
        t.pd()
        t.dot(20,random_color())


s.exitonclick()
