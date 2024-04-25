from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_cord = 10
        self.y_cord = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_cord
        new_y = self.ycor() + self.y_cord
        self.goto(new_x, new_y)

    def bounce_from_wall(self):
        self.y_cord *= -1

    def bounce_from_paddle(self):
        self.x_cord *= -1
        self.ball_speed *= 0.9

    def reset_ball_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_from_paddle()
