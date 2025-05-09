import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

snake = Snake()
food = Food()
score = Scoreboard()
screen = Screen()
screen.title("My Snake Gabz")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.HEAD.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.add_turtle()

    if snake.HEAD.xcor() < -280 or snake.HEAD.xcor() > 280 or snake.HEAD.ycor() < -280 or snake.HEAD.ycor() > 280:
        game_on = False
        score.game_over()

    for turtle in snake.turtles[1:]:
            if snake.HEAD.distance(turtle) < 10:
                game_on = False
                score.game_over()

screen.exitonclick()
