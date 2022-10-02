from scenes.game import GameScene
from scenes.menu import MenuScene
from scenes.game_over import GameOverScene


class SceneManager:
    def __init__(self, pygame):
        self.curr_scene = "menu"
        self.menu = MenuScene(pygame)
        self.game = GameScene(pygame)
        self.game_over = GameOverScene(pygame)

        self.click_sound = pygame.mixer.Sound("./assets/audio/swoosh.wav")

    def on_click(self, pygame):
        if self.curr_scene == "game":
            self.game.bird.jump(pygame)
        elif self.curr_scene == "menu":
            self.curr_scene = "game"
            self.game.bird.jump(pygame)
        elif self.curr_scene == "game_over":
            self.curr_scene = "menu"
            self.game.bird.restart()
            self.game.pipe_spawner.restart(pygame)
            pygame.mixer.Sound.play(self.click_sound)

    def update(self, pygame, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.on_click(pygame)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.on_click(pygame)

        if self.curr_scene != "menu":
            scene = self.game.update(pygame)
            if scene:
                self.curr_scene = scene
        self.menu.update(pygame)

    def show(self, canvas):
        self.game.show(canvas)
        if self.curr_scene == "menu":
            self.menu.show(canvas)
        elif self.curr_scene == "game_over":
            self.game_over.show(canvas)
