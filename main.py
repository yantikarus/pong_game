from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
pong_ball = Ball()
l_player_score = Score((-200, 260))
r_player_score = Score((200, 260))

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    #detect wall collison
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280 :
        pong_ball.bounce_y()
    elif pong_ball.xcor() > 380 or pong_ball.xcor() < -380:
        pong_ball.bounce_x()

    # Detect collison with the paddle
    if pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 320 \
            or pong_ball.distance(left_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    # Detect right paddle missed the ball
    elif pong_ball.xcor() >= 380:
        pong_ball.reset_position()
        l_player_score.add_score()

    # Detect left paddle missed the ball
    elif pong_ball.xcor() <= -380:
        pong_ball.reset_position()
        r_player_score.add_score()





screen.exitonclick()