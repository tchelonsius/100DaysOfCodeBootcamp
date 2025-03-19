# Day 20
# Main Project: Snake Game (Part 1)
# In the days 20 and 21, the Snake Game is being built
# in seven smaller tasks. In this first part, the tasks are:
# 1.) to create the snake, which is formed from several turtles
#     in squared shape;
# 2.) to move the snake. This was the hardest part to achieve,
#     because if the snake moves the head first, it's quite hard
#     to make it turn directions. So the solution was to
#     move the tail first (starting at the last square of the snake)
#     and move it to the position of the following square.
#     In order to make the direction turning seem smooth, the snake
#     moves all the parts, except the head, to the position of the next
#     part, and in the end the head is finally moved to the desired direction.
# 3.) to control the snake with the keyboard entries arrow up, down, left
#     or right. By pressing any of these keys, an accordingly defined function is
#     called in the Snake class. The Snake cannot move in the
#     opposite direction. For example, if it is going up, the arrow down
#     key doesn't do anything.


from turtle import Screen, Turtle
from snake import Snake
import time


s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()


game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    s.listen()
    s.onkey(snake.up, "Up")
    s.onkey(snake.down, "Down")
    s.onkey(snake.right, "Right")
    s.onkey(snake.left, "Left")










s.exitonclick()