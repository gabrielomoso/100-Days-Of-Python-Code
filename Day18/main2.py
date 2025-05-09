from turtle import Turtle, Screen
import random

gabz_turtle = Turtle()
gabz_turtle.color("blue")
gabz_turtle.shape("turtle")


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def draw_shape(num_of_sides, color):
    """This function draws a shape, takes number of sides as input"""
    angle = 360 / num_of_sides
    gabz_turtle.color(color)
    for _ in range(0, num_of_sides):
        gabz_turtle.forward(50)
        gabz_turtle.right(angle)


def random_walk(num_of_walks, distance):
    directions = {
        "forward": gabz_turtle.forward,
        "right": gabz_turtle.right,
        "left": gabz_turtle.left
    }

    for walks in range(num_of_walks):
        # Geting a random choice from the list of directions keys
        direction = random.choice(list(directions.keys()))
        gabz_turtle.color(random_color())
        directions["forward"](distance)
        directions[direction](90)


# for side in range(3, 11):
#     color = random_color()
#     draw_shape(side, color)

random_walk(20, 20)

screen = Screen()

screen.exitonclick()