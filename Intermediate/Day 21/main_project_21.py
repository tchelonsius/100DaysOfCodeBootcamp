# Day 21: Completing the snake game; lists and tuples slicing
# Main Project: Snake Game (Part 2)
# In this second part, the tasks are:
# 4.) detect collision with food. The food is a subclass from Turtle,
#     which objects appear randomly on the screen. When the head of
#     the snake gets close enough to a food instance (less than 14
#     pixels), it moves to another random coordinate of the screen.
# 5.) create a scoreboard. Defined in the class Scoreboard, it shows
#     the player's current score during the whole game, which is
#     increased when an instance of food is eaten.
# 6.) detect collision with the wall. When the head of the snake
#     reaches the end of the screen, the game comes to an end.
# 7.) detect collision with the tail. If the head of the snake
#     meets any of its other parts (obviously except for the
#     head itself), the player loses.



from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.right, "Right")
s.onkey(snake.left, "Left")

game_is_on = True
refresh_time = 0.13
while game_is_on:
    s.update()
    time.sleep(refresh_time)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # changes the position of the food
        food.refresh()
        score.increase_score()
        # extends the snake in one piece
        snake.extend()
        # makes the game faster
        refresh_time = refresh_time - 0.005 if refresh_time > 0.05 else 0.05

    # Detect collision with wall
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        score.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.game_over()
            game_is_on = False

s.exitonclick()
