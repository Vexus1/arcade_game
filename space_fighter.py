import pygame
import pyghelpers
import os

from constants import *
from scenes.scene_main_menu import *
from scenes.scene_play import *
from scenes.scene_high_score import *
from scenes.scene_rules import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# scenes_list = [SceneSplash(window), ScenePlay(window),
#                SceneHighScore(window), SceneRules(window)]
scenes_list = [SceneMainMenu(window), ScenePlay(window)]
scene_mgr = pyghelpers.SceneMgr(scenes_list, FPS)
scene_mgr.run()
