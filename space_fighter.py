import pygame
import os
import sys

from constants import *
from scenes.scene_main_menu import *
from scenes.scene_play import *
from scenes.scene_high_score import *
from scenes.scene_rules import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# scenes_list = [SceneSplash(window), ScenePlay(window),
#                SceneHighScore(window), SceneRules(window)]
clock = pygame.time.Clock()
scenes_list = [SceneMainMenu(screen), ScenePlay(screen)]
curent_scene = scenes_list[0]

while True:
    keys_pressed = pygame.key.get_pressed()
    events_list = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        events_list.append(event)

    if curent_scene.next_scene()
    self.oCurrentScene.handleInputs(eventsList, keysDownList)
    self.oCurrentScene.update()
    self.oCurrentScene.draw()

    pygame.display.update()

    clock.tick(FPS)
