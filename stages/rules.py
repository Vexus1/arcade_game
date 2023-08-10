from stages.stage import Stage

class Rules(Stage):
    def __init__(self, manager, screen):
        super().__init__(manager)
        self.screen = screen