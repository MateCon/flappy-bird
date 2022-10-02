class Bird:
    def __init__(self, pygame):
        self.position = [48, 180]
        self.velocity = 0
        self.acceleration = 0.1

        self.max_y = 378
        self.jump_force = -5

        self.images = {
            "yellow": {
                "downflap": pygame.image.load("./assets/sprites/yellowbird-downflap.png").convert(),
                "midflap": pygame.image.load("./assets/sprites/yellowbird-midflap.png").convert(),
                "upflap": pygame.image.load("./assets/sprites/yellowbird-upflap.png").convert(),
            },
            "blue": {
                "downflap": pygame.image.load("./assets/sprites/bluebird-downflap.png").convert(),
                "midflap": pygame.image.load("./assets/sprites/bluebird-midflap.png").convert(),
                "upflap": pygame.image.load("./assets/sprites/bluebird-upflap.png").convert(),
            },
            "red": {
                "downflap": pygame.image.load("./assets/sprites/redbird-downflap.png").convert(),
                "midflap": pygame.image.load("./assets/sprites/redbird-midflap.png").convert(),
                "upflap": pygame.image.load("./assets/sprites/redbird-upflap.png").convert(),
            },
        }

        self.jump_sound = pygame.mixer.Sound("./assets/audio/wing.wav")
        self.jump_sound.set_volume(0.5)
        self.death_sound = pygame.mixer.Sound("./assets/audio/hit.wav")
        self.death_sound.set_volume(0.5)

        self.midflap_range = 2

    def jump(self, pygame):
        self.velocity = self.jump_force
        pygame.mixer.Sound.play(self.jump_sound)

    def kill(self, pygame):
        self.position = [-1000, -1000]
        self.velocity = 0
        self.acceleration = 0
        pygame.mixer.Sound.play(self.death_sound)

    def update(self, pipe_pos):
        self.velocity += self.acceleration
        self.position[1] += self.velocity

        if self.position[1] > self.max_y:
            self.position[1] = self.max_y
        elif self.position[1] < 0:
            self.position[1] = 0
            self.velocity = 0

        return self.position

    def show(self, game_score, canvas):
        color = "yellow"
        if game_score >= 100:
            color = "red"
        elif game_score >= 25:
            color = "blue"
        position = ""
        if self.velocity < -self.midflap_range:
            position = "downflap"
        elif self.velocity > self.midflap_range:
            position = "upflap"
        else:
            position = "midflap"

        canvas.blit(self.images[color][position],
                    (self.position[0], self.position[1]))

    def restart(self):
        self.position = [48, 180]
        self.velocity = 0
        self.acceleration = 0.1
