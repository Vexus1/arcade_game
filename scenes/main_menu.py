from scenes.scene import Scene
from constants import *
from graphic_tools import TextButton
from scenes.scene_delay import Delay

import pygame
import sys

class MainMenu(Scene):
    def __init__(self, manager, screen):
        super().__init__(manager)
        self.screen = screen
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        self.start_button = TextButton(self.screen, 'Start', 
                                       (screen_width//2, screen_height*3/10), SCENE_PLAY)
        self.level_select_button = TextButton(self.screen, 'Level select',
                                            (screen_width//2, screen_height*4/10), SCENE_LEVEL_SECECT)
        self.option_button = TextButton(self.screen, 'options',
                                       (screen_width//2, screen_height*5/10), SCENE_OPTIONS)
        self.quit_button = TextButton(self.screen, 'Quit',
                                      (screen_width//2, screen_height*6/10))
        self.buttons_list = [self.start_button, self.level_select_button, self.option_button, self.quit_button]
        self.scene_delay = pygame.time.get_ticks() + SCENE_DELAY
        self.button_number = 0

    @Delay.scene_starting_delay
    def handle_inputs(self, events, key_pressed_list):
        for button in self.buttons_list:
            button.unselected()
        self.buttons_list[self.button_number].selected()
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.button_number += 1
                    if self.button_number > len(self.buttons_list)-1:
                        self.button_number = 0
                elif event.key == pygame.K_w:
                    self.button_number -= 1
                    if self.button_number < 0:
                        self.button_number = len(self.buttons_list)-1
                elif event.key == pygame.K_RETURN:
                    if self.button_number == len(self.buttons_list)-1:
                        pygame.quit()
                        sys.exit()
                    self.manager.next_scene(self.buttons_list[self.button_number].scene_reference())
        
    def draw(self):
        self.screen.fill(BLUE)
        self.start_button.draw()
        self.level_select_button.draw()
        self.option_button.draw()
        self.quit_button.draw()
