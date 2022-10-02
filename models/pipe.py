import random
import math


class Pipe:
    def __init__(self, position, gap_height, game_height, pygame):
        self.position = position
        self.pipe_height = 320

        self.gap_height = gap_height

        gap_limit = 150
        self.gap_position = math.floor(
            random.random() * (game_height - gap_height - gap_limit)) + gap_limit / 2

        self.image = pygame.image.load(
            "./assets/sprites/pipe-green.png").convert()
        self.flipped_image = pygame.transform.flip(self.image, False, True)

    def show(self, canvas):
        canvas.blit(
            self.image, (self.position, self.gap_position + self.pipe_height / 2))
        canvas.blit(
            self.flipped_image, (self.position, self.gap_position - self.pipe_height / 2 - self.gap_height))

    def update(self, velocity):
        self.position -= velocity
