from models.background import Background
from models.base import Base
from models.bird import Bird
from models.pipe_spawner import PipeSpawner


class GameScene:
    def __init__(self, pygame):
        self.background = Background(pygame)
        self.base = Base(pygame)
        self.bird = Bird(pygame)
        self.pipe_spawner = PipeSpawner((512, 400), pygame)

    def should_kill(self, pipe_pos, bird_pos):
        if pipe_pos[0] < bird_pos[0] + 34 and pipe_pos[0] + 52 > bird_pos[0]:
            if pipe_pos[1] > bird_pos[1] or pipe_pos[1] + pipe_pos[2] < bird_pos[1]:
                return True
        return False

    def update(self, scene, pygame):
        if scene != "menu":
            self.background.update()
            self.base.update()

        self.pipe_spawner.update(pygame)
        pipe_position = self.pipe_spawner.get_pipe_position()
        bird_position = self.bird.update(pipe_position)

        if self.should_kill(pipe_position, bird_position):
            self.bird.kill(pygame)
            self.pipe_spawner.can_add_to_score_two = False
            return "game_over"
        return None

    def show(self, canvas):
        self.background.show(canvas)
        self.pipe_spawner.show(canvas)
        self.base.show(canvas)
        self.bird.show(canvas)
