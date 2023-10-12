import pygame
from scenes.pause import Pause

class Timer():
    def __init__(self):
        self.time = pygame.time.get_ticks()
        self.pause = Pause()
        self.update_timer()

    def update_timer(self):
        if Pause:
            self.time_before_pause = self.pause._pause_time()
            self.time += self.time_before_pause

    def current_time(self):
        return self.time
    
    # def __repr__(self):
    #     return self.time
    