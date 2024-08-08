from game import Game

#ref "C:\Users\hisan\Downloads\turtle-crossing-start"

def breakout():
    game = Game()
    game.scoreboard.game_start_txt()
    game.game_loop()
    game.screen.mainloop()


if __name__ == "__main__":
    breakout()
