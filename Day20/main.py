import time
from turtle import Screen
from snake import Snake


snake = Snake()
screen = Screen()
screen.title("My Snake Gabz")
screen.screensize(canvwidth=600, canvheight=600, bg="black")
screen.tracer(0)




game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)


screen.exitonclick()
