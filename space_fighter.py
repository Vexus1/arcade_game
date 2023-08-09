import pygame
import os
import sys

from constants import *
from stage_menager import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# scenes_list = [SceneSplash(window), ScenePlay(window),
#                SceneHighScore(window), SceneRules(window)]
clock = pygame.time.Clock()

while True:
    keys_pressed = pygame.key.get_pressed()
    events_list = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        events_list.append(event)

    # if curent_scene.next_scene():
    current_stage = StageMenager()
    current_stage.get_current_stage().handle_inputs(events_list, keys_pressed)
    current_stage.get_current_stage().update()
    current_stage.get_current_stage().draw()

    pygame.display.update()

    clock.tick(FPS)
