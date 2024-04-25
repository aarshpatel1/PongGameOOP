from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(position)

    def paddle_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def paddle_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
