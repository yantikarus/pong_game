from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_cor, y_cor)

    def move_up(self):
        up_y = self.ycor() + 20
        x_cor = self.xcor()
        self.goto(x_cor, up_y)

    def move_down(self):
        down_y = self.ycor() - 20
        x_cor = self.xcor()
        self.goto(x_cor, down_y)

