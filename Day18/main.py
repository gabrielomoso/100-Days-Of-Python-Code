import turtle
import random
gabz = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
color_list = [(46, 102, 137), (198, 157, 119), (144, 80, 59), (134, 168, 190), (229, 213, 113), (140, 67, 84), (198, 139, 156), (19, 45, 79), (141, 180, 151), (57, 124, 94), (202, 96, 69), (67, 38, 27), (184, 91, 105), (154, 147, 68), (78, 159, 105), (31, 61, 110)]

def linear_dots(x, y, num_of_dots):
    gabz.penup()
    gabz.goto(x, y)
    for _ in range(0, num_of_dots):
        color = random.choice(color_list)
        gabz.color(color)
        gabz.dot(15)
        gabz.forward(50)

x = -250
y = -250

for _ in range(0, 10):
    linear_dots(x, y, 10)
    y += 50




screen.exitonclick()
