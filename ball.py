from turtle import Turtle
import math


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("light slate grey")
        self.penup()
        self.x_move = 20
        self.y_move = 20
        self.setheading(135)
        self.move_speed = 0.1
        self.goto(0, -310)

    def position(self):
        return self.xcor(), self.ycor()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        # lateral walls bounce
        if new_x <= -590 or new_x >= 590:
            self.x_move *= -1

        # top bounce
        if new_y >= 230:
            self.y_move += -1

        self.goto(new_x, new_y)

    def paddle_bounce(self, paddle):
        if abs(self.xcor() - paddle.xcor()) > (paddle.shapesize()[1] * 10 -10):
            self.x_move *= -1
        self.y_move *= -1


    def brick_bounce(self, brick):
        ball_x = self.xcor()
        ball_y = self.ycor()
        brick_x = brick.xcor()
        brick_y = brick.ycor()

        if abs(ball_x - brick_x) > abs(ball_y - brick_y):
            self.x_move *= -1
        else:
            self.y_move *= -1

    def bottom_touch(self):
        bottom_screen = -350
        if self.ycor() <= bottom_screen:
            self.destroy_ball()
            return True
        return False

    def reset_position(self):
        self.goto(0, -310)
        self.move_speed = 0.1
        self.paddle_bounce()

    def destroy_ball(self):
        self.hideturtle()
        self.clear()
