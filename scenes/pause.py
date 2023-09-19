import pygame

from scenes.scene import Scene

ALPHA = 100

class Pause(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.veil = pygame.Surface(self.screen.get_size())

    def pause_game(func):
        def inner(self, *kwargs, **args):
            if not self.paused:
                func(self, *kwargs, **args)
        return inner

    def handle_inputs(self, events, key_pressed_list):
        if key_pressed_list[pygame.K_ESCAPE]:

            self.paused = False
    
    def draw(self):
        self.veil.set_alpha(100)
        self.screen.blit(self.veil, (0, 0))
        # self.screen.set_alpha(ALPHA)
