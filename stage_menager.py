# from stages.stage import _reference_to_stage_menager

from stages.main_menu import *
from stages.play import *
# from stages.high_score import HighScore
# from stages.rules import Rules
# from stages.pause import Pause
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
stages_list = [MainMenu(screen), Play(screen)]

class StageMenager():
    def __init__(self):
        self.stages_dict = {}
        for stage in stages_list:
            key = stage.get_stage()
            self.stages_dict[key] = stage
        self.current_stage = stages_list[0]
        

    def _get_current_stage(self, next_stage_key):
        try:
            self.current_stage = self.stages_dict[next_stage_key]
        except KeyError:
            raise KeyError("Trying to go to scene '" + next_stage_key +
                "' but that key is not in the dictionary of stages.")
        
    def get_current_stage(self):
        return self.current_stage
