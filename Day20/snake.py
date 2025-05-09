from turtle import Turtle

STARTING = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0)]
DISTANCE = 20

class Snake:


    def __init__(self):
        self.turtles = []
        self.create_turtles()




    def create_turtles(self):
        for location in STARTING:
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

        self.turtles[0].forward(DISTANCE)



    def up(self):
        self.turtles[0].setheading(90)


    def left(self):
        self.turtles[0].setheading(180)

    def down(self):
        self.turtles[0].setheading(270)

    def right(self):
        self.turtles[0].setheading(0)



