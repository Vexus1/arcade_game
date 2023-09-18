from scene import Scene

class Pause(Scene):
    def __init__(self, manager, screen):
        super.__init__(manager)
        self.screen = screen

    def get_current_scene(self):
        pass

    def handle_inputs(self, events, keys_pressed):
        return super().handle_inputs(events, keys_pressed)
    
    def draw(self):
        return super().draw()