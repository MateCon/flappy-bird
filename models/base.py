class Base:
    def __init__(self, pygame):
        self.position = (0, 400)
        self.image = pygame.image.load("./assets/sprites/base.png").convert()

    def show(self, canvas):
        canvas.blit(self.image, self.position)
