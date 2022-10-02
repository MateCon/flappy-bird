class Background:
    def __init__(self, pygame):
        self.position = (0, 0)
        self.daytime = "day"
        self.images = {
            "day": pygame.image.load("./assets/sprites/background-day.png").convert(),
            "night": pygame.image.load("./assets/sprites/background-night.png").convert()
        }

    def setDaytime(self, daytime):
        if daytime == "day" or daytime == "night":
            self.daytime = daytime
        else:
            raise Exception(
                'Background Error: daytime is either "day" or "night"')

    def show(self, canvas):
        canvas.blit(self.images[self.daytime], self.position)
