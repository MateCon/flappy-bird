class Background:
    def __init__(self, pygame):
        self.position = [0, 0]
        self.images = {
            "day": pygame.image.load("./assets/sprites/background-day.png").convert(),
            "night": pygame.image.load("./assets/sprites/background-night.png").convert()
        }

    def update(self):
        self.position[0] -= 0.2
        if self.position[0] < -288:
            self.position[0] += 288

    def show(self, game_score, canvas):
        daytime = "day"
        if game_score >= 50:
            daytime = "night"
        canvas.blit(self.images[daytime],
                    (self.position[0], self.position[1]))
        canvas.blit(self.images[daytime],
                    (self.position[0] + 288, self.position[1]))
