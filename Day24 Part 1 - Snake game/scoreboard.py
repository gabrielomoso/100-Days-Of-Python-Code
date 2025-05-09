from turtle import Turtle

#Getting the highscore from a file
with open("data.txt") as data:
    data_score = int(data.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = data_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write_score()

    def reset_score(self):
        """This function resets the score and adds a new highscore when necessary"""
        if self.score > self.high_score:
            self.high_score = self.score

            #Saves the highscore to a file
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.write_score()



    def write_score(self):
        """This function writes the score on the screen"""
        self.clear()
        self.write(arg=f"Score : {self.score}  Highscore : {self.high_score}", move=False, align="center", font=("Arial", 12, "normal"))


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"Game Over", move=False, align="center", font=("Arial", 12, "normal"))

    def increase_score(self):
        """This function increases the score when called"""
        self.score += 1
        self.write_score()