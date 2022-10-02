class Base:
    def __init__(self, pygame):
        self.position = [0, 400]
        self.image = pygame.image.load("./assets/sprites/base.png").convert()

    def update(self):
        self.position[0] -= 0.4
        if self.position[0] < -288:
            self.position[0] += 288

    def show(self, canvas):
        canvas.blit(self.image,
                    (self.position[0], self.position[1]))
        canvas.blit(self.image,
                    (self.position[0] + 288, self.position[1]))
