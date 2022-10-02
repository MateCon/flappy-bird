class MenuScreen:
    def __init__(self, pygame):
        self.image = pygame.image.load(
            "./assets/sprites/message.png").convert_alpha()

    def show(self, canvas):
        canvas.blit(self.image, (50, 100))
