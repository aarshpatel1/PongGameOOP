from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)  # turns off an animation  

# created both paddles from the paddle module's Paddle class
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # print log of ball's coordinates
    # print(f"x: {ball.xcor()}\ty: {ball.ycor()}\ty_cord: {ball.y_cord}")

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_from_wall()

    # detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_from_paddle()

    # detect if ball is missed by the right paddle
    if ball.xcor() > 360:
        ball.reset_ball_position()
        scoreboard.left_player_point()

    # detect if ball is missed by the right paddle
    if ball.xcor() < -360:
        ball.reset_ball_position()
        scoreboard.right_player_point()

screen.exitonclick()
