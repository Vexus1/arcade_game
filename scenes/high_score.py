from scenes.scene import Scene

class HighScore(Scene):
    def __init__(self, manager, screen):
        super().__init__(manager)
        self.screen = screen