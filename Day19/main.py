from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
gabz_wrld = []

# Creating 6 instances of gabz turtles
for turtle_index in range(0, 6):
    gabz = Turtle(shape="turtle")
    gabz.penup()
    gabz.color(colors[turtle_index])
    gabz.goto(x=-230, y=y_positions[turtle_index])
    gabz_wrld.append(gabz)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in gabz_wrld:

        # When a turtle gets to the end of the line
        if turtle.xcor() > 230:
            is_race_on = False

            # Getting the color of the gabz turtle that won
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()