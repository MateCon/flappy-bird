from models.game_over_screen import GameOverScreen


class GameOverScene:
    def __init__(self, pygame):
        self.game_over_screen = GameOverScreen(pygame)

    def show(self, canvas):
        self.game_over_screen.show(canvas)
