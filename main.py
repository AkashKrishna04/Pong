from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

right = Paddle((350, 0))
left = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(right.up, "Up")
screen.onkey(right.down, "Down")
screen.onkey(left.up, "w")
screen.onkey(left.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # right
    if ball.xcor() > 360:
        ball.reset_position()
        score.l_point()

    # left
    if ball.xcor() < -360:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
