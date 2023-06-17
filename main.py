from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.getcanvas().bind("<Up>", r_paddle.move_up)
screen.getcanvas().bind("<Down>", r_paddle.move_down)
screen.getcanvas().bind("<w>", l_paddle.move_up)
screen.getcanvas().bind("<s>", l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls (up / dowm)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Detect if ball goes out of bounds on R side
    if ball.xcor() > 380:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.l_poit()

    # Detect if ball goes out of bounds on L side
    if ball.xcor() < -380:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.r_poit()








screen.exitonclick()
