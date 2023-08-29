import pygame

class Delay:
    def scene_starting_delay(func):
        """Delay at the start of the level in milliseconds"""
        def inner(self, *kwargs, **args):
            if pygame.time.get_ticks() >= self.scene_delay:
                func(self, *kwargs, **args)
        return inner
