from turtle import Turtle

UP = 0
DOWN = 180
DISTANCE = 30

class Paddle(Turtle):

    def __init__(self, x):
        """Takes in the X coordinate of the paddle"""
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x, y=0)
        self.setheading(90)


    def move_up(self):
        self.forward(DISTANCE)

    def move_down(self):
        self.backward(DISTANCE)


