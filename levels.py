from brick import Brick

COLORS = ["red", "orange", "yellow", "lime green", "blue", "indigo", "purple"]
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
SCREEN_WIDTH = 1200


class Walls:
    def __init__(self):
        self.bricks = []

    # used this as a level-creator blue print.
    def level_1(self):
        # start your points system
        points = 1
        brick_line = 0

        # mark where the bricks should start on the yaxis (midpoint is -50, top is 250, bottom -350)
        y_start = 220

        # bricks per line. if every line has the same, you just need one line of code.
        bricks_pl = SCREEN_WIDTH // BRICK_WIDTH

        # where to start laying bricks on the x axis
        x_start = -SCREEN_WIDTH / 2 + BRICK_WIDTH / 2

        # how are you gonna mange color combinations
        colors = []
        for color in COLORS:
            colors.append(color)
            colors.append(color)

        # lay them like you're bob the builder
        for color in colors:
            for _ in range(bricks_pl):
                brick_position = (x_start, y_start)
                brick = Brick(color, points, brick_position)
                self.bricks.append(brick)
                x_start += BRICK_WIDTH

            # reset your starting points
            y_start -= BRICK_HEIGHT
            x_start = -SCREEN_WIDTH / 2 + BRICK_WIDTH / 2

            # reset your point values
            brick_line += 1
            if brick_line % 2 == 0:
                points += 2



    def level_2(self):
        points = 1
        brick_line = 0
        y_start = -50
        bricks_pl = 2

        colors = []
        for color in COLORS:
            colors.append(color)
            colors.append(color)

        for color in colors:
            x_start = -(bricks_pl * BRICK_WIDTH) / 2 + BRICK_WIDTH / 2
            for _ in range(bricks_pl):
                brick_position = (x_start, y_start)
                brick = Brick(color, points, brick_position)
                self.bricks.append(brick)
                x_start += BRICK_WIDTH

            y_start += BRICK_HEIGHT
            bricks_pl += 2

            brick_line += 1
            if brick_line % 2 == 0:
                points += 2

    def level_3(self):
        points = 1
        y_start = 220
        bricks_pl = SCREEN_WIDTH // BRICK_WIDTH
        x_start = -SCREEN_WIDTH / 2 + BRICK_WIDTH / 2

        colors = []
        for color in COLORS:
            colors.append(color)

        for color in colors:
            for _ in range(bricks_pl):
                brick_position = (x_start, y_start)
                brick = Brick(color, points, brick_position)
                self.bricks.append(brick)
                x_start += BRICK_WIDTH

            y_start -= (BRICK_HEIGHT * 2)
            x_start = -SCREEN_WIDTH / 2 + BRICK_WIDTH / 2

            points += 1

    def clear_bricks(self):
        for brick in self.bricks:
            brick.destroy()
        self.bricks.clear()

