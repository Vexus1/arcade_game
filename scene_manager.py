import pygame

from constants import *
from scenes.main_menu import MainMenu
from scenes.play import Play
from scenes.level_select import LevelSelect
from scenes.options import Options
from scenes.pause import Pause
from scenes.transition_scene import Fader

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen = pygame.display.set_mode(SCREEN_SIZE)

class SceneError(Exception):
    pass

class SceneManager():
    def __init__(self):
        self.current_scene = Fader(self, screen, [MainMenu(self, screen)])
        self.during_change = False

    def next_scene(self, next_scene):
        if self.during_change:
            return
        self.during_change = True
        if next_scene == SCENE_MAIN_MENU:
            self.current_scene = Fader(self, screen, [self.current_scene, MainMenu(self, screen)]) 
        elif next_scene == SCENE_PLAY:
            self.current_scene = Fader(self, screen, [self.current_scene, Play(self, screen)]) 
        elif next_scene == SCENE_LEVEL_SECECT:
            self.current_scene = Fader(self, screen, [self.current_scene, LevelSelect(self, screen)])
        elif next_scene == SCENE_OPTIONS:
            self.current_scene = Fader(self, screen, [self.current_scene, Options(self, screen)]) 
        elif next_scene == SCENE_PAUSE:
            self.current_scene = Pause(self, self.current_scene.screen, self.current_scene)
        else:
            raise SceneError(f"Scene {next_scene} doesn't exit")

    def get_current_scene(self):
        return self.current_scene
