import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    for car in cars.all_cars:
        if player.distance(car) < 25:
            score.game_over()
            game_is_on = False



    if player.ycor() > player.FINISH_LINE:
        player.reset_position()
        score.increase_score()
        cars.increase_speed()






screen.exitonclick()