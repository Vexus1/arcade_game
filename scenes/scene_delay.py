from constants import SCENE_DELAY
import pygame

class Delay:
    def __init__(self):
        pass
        # self.scene_delay = SCENE_DELAY

    def scene_starting_delay(func):
        """Delay at the start of the level in milliseconds"""
        def inner(self, *kwargs, **args):
            print(pygame.time.get_ticks(), self.scene_delay, pygame.time.get_ticks() >= self.scene_delay)
            if pygame.time.get_ticks() >= self.scene_delay:
                func(self, *kwargs, **args)
        return inner
