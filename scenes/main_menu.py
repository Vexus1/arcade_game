from scenes.scene import Scene
from constants import *
from graphic_tools import TextButton
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
        self.high_score_button = TextButton(self.screen, 'High Score',
                                            (screen_width//2, screen_height*4/10), SCENE_HIGH_SCORE)
        self.rules_button = TextButton(self.screen, 'Rules',
                                       (screen_width//2, screen_height*5/10), SCENE_RULES)
        self.quit_button = TextButton(self.screen, 'Quit',
                                      (screen_width//2, screen_height*6/10))
        self.buttons_list = [self.start_button, self.high_score_button, self.rules_button, self.quit_button]
        self.button_number = 0

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
        self.screen.fill(BLACK)
        self.start_button.draw()
        self.high_score_button.draw()
        self.rules_button.draw()
        self.quit_button.draw()
