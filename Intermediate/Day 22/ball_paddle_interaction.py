# This class controls the interactions between ball and paddles.

from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

class Interaction:
    def __init__(self):
        self.l_paddle = Paddle(-350)
        self.r_paddle = Paddle(350)
        self.game_ball = Ball()
        self.scoreboard = Scoreboard()
        self.game_running = True

    # Detects collision between the paddles and the ball.
    def detect_collision(self):
        if self.l_paddle.distance(self.game_ball)<50 and self.game_ball.pos()[0]<-315:
            self.game_ball.bounce_x()
            return

        if self.r_paddle.distance(self.game_ball)<50 and self.game_ball.pos()[0]>315:
            self.game_ball.bounce_x()
            return

    # Detects whether the ball goes beyond one of the paddles,
    # meaning a point was made.
    def detect_point(self):
        if self.game_ball.pos()[0] > 370:
            self.scoreboard.increase_l_score()
            self.point_made()
        elif self.game_ball.pos()[0] < -370:
            self.scoreboard.increase_r_score()
            self.point_made()

    # When a point is made, the ball goes back to position (0,0)
    # and starts over in the opposite direction.
    def point_made(self):
        self.game_ball.change_direction()
        self.game_ball.reset_position()


