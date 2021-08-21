import time
from turtle import Screen
from padle import Padle
from ball import Ball
from scoreboard import Scoreboard
x = 0
y = 0
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



padle_l = Padle(-350)
padle_r = Padle(350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(padle_r.move_up, "Up")
screen.onkey(padle_r.move_down, "Down")
screen.onkey(padle_l.move_up, "w")
screen.onkey(padle_l.move_down, "s")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)

    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()

    if ball.xcor() > 320 and ball.distance(padle_r) < 50 or ball.xcor() < -320 and ball.distance(padle_l) < 50:
        ball.bounce_padle()

    if ball.xcor() > 380:
        ball.reset_ball()
        x += 1
        scoreboard.score_point(x, y)
    if ball.xcor() < -380:
        ball.reset_ball()
        y += 1
        scoreboard.score_point(x, y)

screen.exitonclick()
