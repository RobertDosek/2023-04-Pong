from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize( stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def move_up(self, event):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def move_down(self, event):
        new_y = self.ycor() - 20
        self.sety(new_y)