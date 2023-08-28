import pygame

from constants import *
from scenes.main_menu import MainMenu
from scenes.play import Play
from scenes.level_select import HighScore
from scenes.options import Rules
from scenes.transition_scene import Fader

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

class SceneError(Exception):
    pass

class SceneManager():
    def __init__(self):
        self.current_scene = Fader(screen, [MainMenu(self, screen)])

    def get_scene_names(self):
        '''Method implemented in future when there will be to many scenes'''
        pass
    
    def next_scene(self, next_scene):
        if next_scene == SCENE_MAIN_MENU:
            self.current_scene = Fader(screen, [self.current_scene, MainMenu(self, screen)]) 
        elif next_scene == SCENE_PLAY:
            self.current_scene = Fader(screen, [self.current_scene, Play(self, screen)]) 
        elif next_scene == SCENE_LEVEL_SECECT:
            self.current_scene = HighScore(self, screen)
        elif next_scene == SCENE_OPTIONS:
            self.current_scene = Rules(self, screen)
        elif next_scene == SCENE_PAUSE:
            self.current_scene = MainMenu(self, screen)
        else:
            raise SceneError(f"Scene {next_scene} doesn't exit")

    def get_current_scene(self):
        return self.current_scene
