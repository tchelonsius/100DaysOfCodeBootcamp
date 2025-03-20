from turtle import Turtle

# displays the score on the screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.pencolor("white")
        self.setpos(0,270)
        self.score = -1
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.pencolor("yellow")
        self.write(f"Score = {self.score}", False, align="center", font=("Courier", 20, "normal"))
        self.pencolor("white")

    # displays the game over message in the center when the player loses.
    def game_over(self):
        self.goto(0,0)
        self.pencolor("yellow")
        self.write("GAME OVER", False, align="center", font=("Courier", 25, "normal"))
        self.pencolor("white")


