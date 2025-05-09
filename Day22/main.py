from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
scoreboard = Scoreboard()

left_paddle = Paddle(-380)
right_paddle = Paddle(380)
ball = Ball()

game = True

while game:
    screen.update()
    time.sleep(ball.ball_speed)
    screen.listen()
    ball.move()

    #Detect collision with Top Wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.y_bounce()


    #Detect collision with Paddles
    if ball.distance(left_paddle) < 50 and ball.xcor() < -350 or ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        ball.x_bounce()


    #Detect collision with side Walls
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()



    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    screen.onkey(key="Up", fun=right_paddle.move_up)
    screen.onkey(key="Down", fun=right_paddle.move_down)
    screen.onkey(key="w", fun=left_paddle.move_up)
    screen.onkey(key="s", fun=left_paddle.move_down)





screen.exitonclick()