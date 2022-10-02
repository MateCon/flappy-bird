class GameOverScreen:
    def __init__(self, pygame):
        self.image = pygame.image.load(
            "./assets/sprites/gameover.png").convert_alpha()

    def show(self, canvas):
        canvas.blit(self.image, (40, 200))
