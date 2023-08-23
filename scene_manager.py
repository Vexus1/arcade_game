import pygame

from constants import *
from scenes.main_menu import MainMenu
from scenes.play import Play
from scenes.high_score import HighScore
from scenes.rules import Rules

class SceneError(Exception):
    pass

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

class SceneManager():
    def __init__(self):
        self.current_scene = MainMenu(self, screen)

    def get_scene_names(self):
        '''Method implemented in future when there will be to many scenes'''
        pass
    
    def next_scene(self, next_scene):
        del self.current_scene
        if next_scene == SCENE_MAIN_MENU:
            self.current_scene = MainMenu(self, screen)
        elif next_scene == SCENE_PLAY:
            self.current_scene = Play(self, screen)
        elif next_scene == SCENE_HIGH_SCORE:
            self.current_scene = HighScore(self, screen)
        elif next_scene == SCENE_RULES:
            self.current_scene = Rules(self, screen)
        elif next_scene == SCENE_PAUSE:
            self.current_scene = MainMenu(self, screen)
        else:
            raise SceneError(f"Scene {next_scene} doesn't exit")

    def get_current_scene(self):
        return self.current_scene
