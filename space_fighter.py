import pygame
import pyghelpers
from constants import *
from scenes.scene_splash import *
from scenes.scene_play import *
from scenes.scene_high_score import *
from scenes.scene_rules import *

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# scenes_list = [SceneSplash(window), scene_play(window),
#                scene_high_score(window), scene_rules(window)]
scenes_list = [SceneSplash(window)]
scene_mgr = pyghelpers.SceneMgr(scenes_list, FPS)
scene_mgr.run()
