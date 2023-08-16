# from stages.stage import _reference_to_stage_menager
import pygame
from stages.main_menu import *
from stages.play import *
from stages.high_score import *
from stages.rules import *
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

class StageMenager():
    def __init__(self):
        # self.stages_list = [MainMenu(self, screen), Play(self, screen),
        #                     HighScore(self, screen), Rules(self, screen)]
        self.stages_list = [MainMenu(self, screen), Play(self, screen)]
        self.stages_dict = {}
        for stage in self.stages_list:
            key = stage.get_stage()
            self.stages_dict[key] = stage
        self.current_stage = self.stages_list[0]
    
    def next_stage(self, next_stage):
        try:
            self.current_stage = self.stages_dict[next_stage]
        except KeyError:
            raise KeyError("Stage doesn't exist.")

    def get_current_stage(self):
        return self.current_stage
