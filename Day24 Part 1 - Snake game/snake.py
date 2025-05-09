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
        self.reset_snake()
        self.HEAD = self.turtles[0]  # This variable is here so it can be global

    def reset_snake(self):
        """This function moves, clear and calls the create_snake function"""
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear() #Clears all the objects in the list
        self.create_snake()



    def create_snake(self):
        """This function creates 3 new turtles inside the turtles list"""
        for location in STARTING:
            self.extend_snake(location)

        self.HEAD = self.turtles[0]  #Setting the head so the move_snake function can use it

    def add_snake(self):
        """This function gets the location of the last turtle and calls the extend_snake function"""
        TAIL = self.turtles[-1]
        self.extend_snake(TAIL.position())

    def extend_snake(self, location):
        """This function adds a new turtle to the snake"""
        gabz = Turtle("square")
        gabz.color("white")
        gabz.penup()
        gabz.goto(location)
        self.turtles.append(gabz)

    def move_snake(self):
        """This function moves the snake"""
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
