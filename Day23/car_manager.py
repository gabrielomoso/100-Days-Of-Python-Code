from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_DISTANCE
        self.all_cars = []


    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)


    def create_car(self):
        """This function has a chance to create a car once every 6th time it is called"""
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            random_color = random.randint(0, len(COLORS) - 1)
            car.color(COLORS[random_color])
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            car.setheading(180)
            self.all_cars.append(car)


