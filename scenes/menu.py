from models.menu_screen import MenuScreen


class MenuScene:
    def __init__(self, pygame):
        self.menu_screen = MenuScreen(pygame)

    def update(self, pygame):
        pass

    def show(self, canvas):
        self.menu_screen.show(canvas)
