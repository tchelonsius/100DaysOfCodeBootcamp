# Day 23
# Main Project: Pong Arcade Game
# In this game, two paddles, each on a side of the screen, compete against
# each other to make the ball go through the end of the screen and score
# points. The left one is controlled with the keys 'w' and 's' and the right
# one, with the arrows up and down.

from turtle import Screen, Turtle
import time
import screen_setup
from ball_paddle_interaction import Interaction

# screen configs. tracer set to 0, this means the animation
# must be updated manually throughout the game
s = Screen()
s.tracer(0)
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")

# necessary classes
ball_paddle = Interaction()
screen_config = screen_setup.ScreenSetup()

# keys interactions and their respective function calls
s.listen()
s.onkeypress(ball_paddle.r_paddle.move_up, "Up")
s.onkeypress(ball_paddle.r_paddle.move_down, "Down")
s.onkeypress(ball_paddle.l_paddle.move_up, "w")
s.onkeypress(ball_paddle.l_paddle.move_down, "s")


while ball_paddle.game_running:
    time.sleep(ball_paddle.game_ball.move_speed)
    s.update()

    # The right paddle can be automatically moved
    # by uncommenting the method call below.
    # ball_paddle.r_paddle.auto_move()
    ball_paddle.game_ball.move()

    # detects points or collisions with the paddles
    ball_paddle.detect_point()
    ball_paddle.detect_collision()


s.exitonclick()