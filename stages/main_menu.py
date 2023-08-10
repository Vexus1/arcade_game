from stages.stage import Stage
from constants import *
from graphic_tools import TextButton
import pygame
import sys

class MainMenu(Stage):
    def __init__(self, manager, screen):
        super().__init__(manager)
        self.screen = screen
        self.start_button = TextButton(self.screen, 'Start', (500, 100), STAGE_PLAY)
        self.high_score_button = TextButton(self.screen, 'High Score', (500, 200), STAGE_HIGH_SCORE)
        self.rules_button = TextButton(self.screen, 'Rules', (500, 300), STAGE_RULES)
        self.quit_button = TextButton(self.screen, 'Quit', (500, 400))
        self.buttons_list = [self.start_button, self.high_score_button,
                        self.rules_button, self.quit_button]
        self.button_number = 0
    
    def get_stage(self):
        return STAGE_MAIN_MENU

    def handle_inputs(self, events, key_pressed_list):
        self.buttons_list[self.button_number].selected()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.buttons_list[self.button_number].unselected()
                    self.button_number += 1
                    if self.button_number > len(self.buttons_list)-1:
                        self.button_number = 0
                    self.buttons_list[self.button_number].selected()
                    print(self.button_number)
                elif event.key == pygame.K_w:
                    self.buttons_list[self.button_number].unselected()
                    self.button_number -= 1
                    if self.button_number < 0:
                        self.button_number = len(self.buttons_list)-1
                    self.buttons_list[self.button_number].selected()
                    print(self.button_number)
                elif event.key == pygame.K_RETURN:
                    if self.button_number == len(self.buttons_list)-1:
                        pygame.quit()
                        sys.exit()
                    self.manager.next_stage(self.buttons_list[self.button_number].stage_reference())
        
    def draw(self):
        self.start_button.draw()
        self.high_score_button.draw()
        self.rules_button.draw()
        self.quit_button.draw()
