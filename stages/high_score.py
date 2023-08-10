from stages.stage import Stage

class HighScore(Stage):
    def __init__(self, manager, screen):
        super().__init__(manager)
        self.screen = screen