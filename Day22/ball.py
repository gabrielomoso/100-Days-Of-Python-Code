from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_distance = 10
        self.y_distance = 10
        self.ball_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_distance
        y = self.ycor() + self.y_distance
        self.goto(x, y)


    def y_bounce(self):
        self.y_distance *= -1



    def x_bounce(self):
        self.x_distance *= -1
        self.ball_speed *= 0.9


    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_bounce()