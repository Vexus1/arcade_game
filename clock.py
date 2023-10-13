import pygame
from scene_manager import SceneManager
from constants import *

class Timer():
    def __init__(self):
        self.time = pygame.time.get_ticks()
        self.update_timer()

    def update_timer(self):
        if SceneManager.get_current_scene() == SCENE_PAUSE:
            time = self.time
        if SceneManager.get_current_scene() == SCENE_PLAY:
            self.time -= time
        
    def current_time(self):
        return self.time
    