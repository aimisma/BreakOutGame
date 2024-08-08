from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('light slate grey')
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 60
        if new_x + 50 <= 600:
            self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 60
        if new_x - 50 >= -600:
            self.goto(new_x, self.ycor())

    def shrink(self):
        self.shapesize(stretch_wid=1, stretch_len=4)

    def reset_position(self, position):
        self.goto(position)
