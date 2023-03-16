from turtle import Turtle

FONT = ('Arial', 30, 'normal')
ALIGNMENT = "center"


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(position)
        self.score = 0
        self.pendown()
        self.write(f"{self.score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()


    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, align=ALIGNMENT, font=FONT)
