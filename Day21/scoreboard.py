from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Arial", 12, "normal"))



    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", move=False, align="center", font=("Arial", 12, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Arial", 12, "normal"))