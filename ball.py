from turtle import Turtle

SPEED_DECREASE = 1.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed /= SPEED_DECREASE

    def reset_position(self):
        self.goto(0,0)
        self.x_bounce()
        self.move_speed = 0.1
