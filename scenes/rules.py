from scenes.scene import Scene

class Rules(Scene):
    def __init__(self, manager, screen):
        super().__init__(manager)
        self.screen = screen