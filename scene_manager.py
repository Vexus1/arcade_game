import pygame

from scenes.main_menu import *
from scenes.play import *
from scenes.high_score import *
from scenes.rules import *

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

class SceneManager():
    def __init__(self):
        self.scenes_list = [MainMenu(self, screen), Play(self, screen)]
        self.scenes_dict = {}
        for scene in self.scenes_list:
            key = scene.get_scene()
            self.scenes_dict[key] = scene
        self.current_scene = self.scenes_list[0]

    def get_scene_names(self):
        '''Method implemented in future when there will be to many scenes'''
        pass
    
    def next_scene(self, next_scene):
        try:
            self.current_scene = self.scenes_dict[next_scene]
        except KeyError:
            raise KeyError("Scene doesn't exist.")

    def get_current_scene(self):
        return self.current_scene
