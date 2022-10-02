class ScoreDisplay:
    def __init__(self, pygame):
        self.position = [144, 60]
        self.images = [pygame.image.load(
            f"./assets/sprites/{d}.png").convert() for d in range(10)]

    def show(self, score, canvas):
        if score < 10:
            canvas.blit(self.images[score],
                        (self.position[0] - 24, self.position[1]))
        elif score < 100:
            digits = [int(d) for d in str(score)]
            canvas.blit(self.images[digits[0]],
                        (self.position[0] - 24, self.position[1]))
            canvas.blit(self.images[digits[1]],
                        (self.position[0], self.position[1]))
        elif score < 1000:
            digits = [int(d) for d in str(score)]
            canvas.blit(self.images[digits[0]],
                        (self.position[0] - 48, self.position[1]))
            canvas.blit(self.images[digits[1]],
                        (self.position[0] - 24, self.position[1]))
            canvas.blit(self.images[digits[2]],
                        (self.position[0], self.position[1]))
