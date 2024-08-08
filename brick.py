from turtle import Turtle


class Brick(Turtle):
    def __init__(self, color, points, position):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.pencolor("light slate grey")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(position)
        self.points = points

    def position(self):
        return self.xcor(), self.ycor()

    def destroy(self):
        self.hideturtle()
        self.clear()

