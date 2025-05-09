from turtle import Turtle
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.display_score()



    def display_score(self):
        self.clear()
        self.goto(-230,270)
        self.write(arg=f"Score : {self.score}", align="center", move=False, font=FONT)


    def increase_score(self):
        self.score += 1
        self.display_score()


    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", move=False, font=FONT)


