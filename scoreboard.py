from turtle import Turtle
import os


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("light slate gray")
        self.penup()
        self.ht()
        self.score = 0
        self.lives = []
        self.update_scoreboard()
        self.level_completed = False

    def update_scoreboard(self):
        self.clear()
        self.goto(-590, 270)
        self.write(f'Score: {self.score}', align='left', font=("Courier", 30, "normal"))
        self.goto(370, 270)
        self.write("Lives:", align='center', font=("Courier", 30, "normal"))
        for life in self.lives:
            life.showturtle()

    # add score
    def add_points(self, points):
        self.score += points
        self.update_scoreboard()

        # visually handle the loss of lives

    def one_life_less(self):
        if self.lives:
            life = self.lives.pop()
            life.clear()
            life.hideturtle()
            self.update_scoreboard()

    def reset_lives(self, ball_count):

        for life in self.lives:
            life.clear()
            life.hideturtle()
        self.lives.clear()

        for i in range(ball_count):
            life = Turtle()
            life.shape("circle")
            life.color("light slate gray")
            life.penup()
            life.goto(450 + (i * 30), 290)
            self.lives.append(life)

    # gives a window to start game:
    def game_start_txt(self, countdown=3):
        if not hasattr(self, "start_timer"):
            self.start_timer = True
            self.clear()
            self.goto(0, 0)
            self.write(f'Game Starts in {countdown}', align='center', font=('Courier', 40, 'normal'))
            if countdown > 0:
                self.getscreen().ontimer(lambda: self.game_start_txt(countdown - 1), 1000)
            else:
                self.start_timer = False
                self.clear()
                self.update_scoreboard()

    # level completed message
    def level_finished_txt(self, countdown=3):
        if not self.level_completed:
            self.level_completed = True
            self.goto(0, 0)
            self.write(f'Level Completed! {countdown}', align='center', font=('Courier', 40, 'normal'))
            if countdown > 0:
                self.getscreen().ontimer(lambda: self.level_finished_txt(countdown - 1), 1000)
            else:
                self.level_completed = False
                self.clear()
                self.update_scoreboard()

    # game completed message
    def all_levels_completed(self):
        self.clear()
        self.goto(0,150)
        self.write('Game Finished', align='center', font=('Courier', 40, 'normal'))
        self.goto(0, 100)
        self.write(f'Final Score: {self.score}', align='center', font=('Courier', 30, 'normal'))
        self.update_high_scores()
        top_scores = self.get_top_scores()
        self.goto(0, 50)
        self.write('Top 10 Scores:', align='center', font=('Courier', 40, 'normal'))
        for i, score in enumerate(top_scores, start=1):
            self.goto(0, 50-(i *30))
            self.write(f'{i}.  {score}', align='center', font=('Courier', 20, 'normal'))

    # Show game over message and scoreboard:
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('Game Over!', align='center', font=('Courier', 40, 'normal'))
        self.goto(0,-50)
        self.write(f'Final Score {self.score}', align='center', font=('Courier', 30, 'normal'))
        self.update_high_scores()

    def update_high_scores(self):
        scores = self.get_top_scores()
        scores.append(self.score)
        scores.sort(reverse=True)
        top_scores = scores[:10]
        with open("data.txt", "w") as data:
            for score in top_scores:
                data.write(f"{score}\n")

    def get_top_scores(self):
        if not os.path.exists("data.txt"):
            return []
        with open("data.txt", "r") as data:
            scores = [int(line.strip() for line in data.readlines())]
            return scores

