import levels
from levels import Walls
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from turtle import Screen


class Game:
    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.walls = Walls()
        self.scoreboard = Scoreboard()
        self.current_level = 0
        self.levels = self.get_levels()
        self.paddle = Paddle((0, -330))
        self.ball = Ball()
        self.ball.goto(0, -310)
        self.ball_count = 3
        self.scoreboard.reset_lives(self.ball_count)
        self.paddle_controls()

    def setup_screen(self):
        self.screen = Screen()
        self.screen.setup(1200, 700)
        self.screen.bgcolor("white")
        self.screen.title("Brick Breaker")
        self.screen.tracer(0)

    def get_levels(self):
        levels = []
        for method_name in dir(self.walls):

            if method_name.startswith('level_'):
                method = getattr(self.walls, method_name, None)
                if callable(method):
                    levels.append(method)
        return levels

    def next_level(self):

        if self.current_level < len(self.levels):
            self.walls.clear_bricks()
            level_method = self.levels[self.current_level]
            level_method()
            self.current_level += 1
            self.ball_count = 3
            self.scoreboard.reset_lives(self.ball_count)
        else:
            self.scoreboard.all_levels_completed()

    def check_level_completion(self):
        if not self.walls.bricks:
            if not self.scoreboard.level_completed:
                self.scoreboard.level_finished_txt()
                self.next_level()

    def paddle_controls(self):
        self.screen.listen()
        self.screen.onkey(self.paddle.go_left, "Left")
        self.screen.onkey(self.paddle.go_right, "Right")
        self.screen.onkey(self.paddle.go_left, "a")
        self.screen.onkey(self.paddle.go_right, "d")

    def check_collision_with_paddle(self):
        if (abs(self.ball.ycor() - self.paddle.ycor()) < 10 and
                self.paddle.xcor() - 50 <= self.ball.xcor() <= self.paddle.xcor() + 50):
            self.ball.paddle_bounce(self.paddle)

    def check_collision_with_bricks(self):
        for brick in self.walls.bricks:
            if (abs(self.ball.xcor() - brick.xcor()) < 40
                    and abs(self.ball.ycor() - brick.ycor()) < 20):
                self.ball.brick_bounce(brick)
                self.scoreboard.add_points(brick.points)
                brick.destroy()
                self.walls.bricks.remove(brick)
                break


    # check if you have lives
    def ball_tracking(self):
        if self.ball.bottom_touch():
            self.ball_count -= 1
            self.scoreboard.one_life_less()
            if self.ball_count > 0:
                self.ball = Ball()
                self.ball.goto(0, -310)
                self.ball.setheading(135)
                self.ball.showturtle()
            else:
                self.scoreboard.game_over()

    def game_loop(self):
        self.ball.move()
        self.check_collision_with_bricks()
        self.check_collision_with_paddle()
        self.ball_tracking()
        self.check_level_completion()
        self.screen.update()
        self.screen.ontimer(self.game_loop, 50)
