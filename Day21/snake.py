from turtle import Turtle

STARTING = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:


    def __init__(self):
        self.turtles = []
        for location in STARTING:
            self.extend(location)
        self.HEAD = self.turtles[0]


    def add_turtle(self):
        TAIL = self.turtles[-1]
        self.extend(TAIL.position())

    def extend(self, location):
        gabz = Turtle("square")
        gabz.color("white")
        gabz.penup()
        gabz.goto(location)
        self.turtles.append(gabz)


    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):

            # Getting the cordinates of the turtle in front
            new_x = self.turtles[turtle - 1].xcor()
            new_y = self.turtles[turtle - 1].ycor()

            # making the new behind go to its previous position
            self.turtles[turtle].goto(x=new_x, y=new_y)

        self.HEAD.forward(DISTANCE)



    def up(self):
        if self.HEAD.heading() != DOWN:
            self.HEAD.setheading(UP)


    def left(self):
        if self.HEAD.heading() != RIGHT:
            self.HEAD.setheading(LEFT)

    def down(self):
        if self.HEAD.heading() != UP:
            self.HEAD.setheading(DOWN)


    def right(self):
        if self.HEAD.heading() != LEFT:
            self.HEAD.setheading(RIGHT)



