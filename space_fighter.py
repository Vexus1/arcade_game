import pygame
import os
import sys

from constants import *
from scene_manager import *

os.chdir(os.path.dirname(os.path.abspath(__file__))) 

pygame.init() 
clock = pygame.time.Clock()
current_scene = SceneManager()
pygame.mouse.set_visible(False)

while True:
    keys_pressed = pygame.key.get_pressed()
    events_list = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

        events_list.append(event)
 
    current_scene.get_current_scene().handle_inputs(events_list, keys_pressed)
    current_scene.get_current_scene().update()
    current_scene.get_current_scene().draw()

    pygame.display.update()

    clock.tick(FPS)
