from models.pipe import Pipe
from models.score_display import ScoreDisplay


class PipeSpawner:
    def __init__(self, screen_dimensions, pygame):
        self.screen_height = screen_dimensions[1]
        self.starting_position = screen_dimensions[0] + 20
        self.pipes = []
        self.curr_gap = 160
        self.min_gap = 120
        self.velocity = 1.2
        self.acceleration = 0.02

        self.score_display = ScoreDisplay(pygame)
        self.show_score = False
        self.game_score = 0
        self.can_add_to_score = True
        self.can_add_to_score_two = True
        for _ in range(3):
            self.add_pipe(pygame)

        self.point_sound = pygame.mixer.Sound("./assets/audio/point.wav")
        self.point_sound.set_volume(0.5)

    def get_pipe_position(self):
        return [self.pipes[0].position, self.pipes[0].gap_position, self.pipes[0].gap_height]

    def add_pipe(self, pygame):
        position = self.starting_position
        if len(self.pipes) > 0:
            position = self.pipes[len(self.pipes) - 1].position + 200

        self.pipes.append(Pipe(position, self.curr_gap,
                               self.screen_height, pygame))

        self.curr_gap -= 1
        if self.curr_gap < self.min_gap:
            self.curr_gap = self.min_gap

    def update(self, pygame):
        self.show_score = True
        for pipe in self.pipes:
            pipe.update(self.velocity)

        if self.pipes[0].position < 50 and self.can_add_to_score and self.can_add_to_score_two:
            pygame.mixer.Sound.play(self.point_sound)
            self.game_score += 1
            self.can_add_to_score = False

        if self.pipes[0].position < -50:
            self.pipes.pop(0)
            self.add_pipe(pygame)
            self.velocity += self.acceleration

            self.curr_gap -= 0.2
            if self.curr_gap < self.min_gap:
                self.curr_gap = self.min_gap

            self.can_add_to_score = True

    def show(self, canvas):
        for pipe in self.pipes:
            pipe.show(canvas)
        if self.show_score:
            self.score_display.show(self.game_score, canvas)

    def restart(self, pygame):
        self.pipes = []
        self.curr_gap = 160
        self.min_gap = 120
        self.velocity = 1.2
        self.acceleration = 0.02
        self.show_score = False
        self.game_score = 0
        self.can_add_to_score = True
        self.can_add_to_score_two = True

        for _ in range(3):
            self.add_pipe(pygame)
