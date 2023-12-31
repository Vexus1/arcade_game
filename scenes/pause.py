import pygame

from scenes.scene import Scene
from graphic_tools import Text
from constants import *

FADE = 150

class Pause(Scene):
    def __init__(self, manager, screen, paused_scene):
        super().__init__(manager)
        self.screen = screen
        self.paused_scene = paused_scene
        self.time_before_pause = pygame.time.get_ticks()
        self.surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)

    def pause_screen(self):
        screen_rect = self.screen.get_rect()
        pause_text = Text(self.surface, ('Game paused: SPACE to resume or press ESC to main menu'), screen_rect.center, size=40, color=BLACK)
        faded_screen = pygame.draw.rect(self.surface, (GRAY + (FADE,)), [0, 0, self.screen.get_width(), self.screen.get_height()])
        return faded_screen, pause_text.draw()

    def handle_inputs(self, events, key_pressed_list):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.manager.during_change = False                 
                    self.manager.current_scene = self.paused_scene  # relocate this into abstract class when more stages will be added
                if event.key == pygame.K_ESCAPE:
                    self.manager.during_change = False 
                    self.manager.next_scene(SCENE_MAIN_MENU)
    
    def draw(self):
        self.paused_scene.draw()
        self.pause_screen()
        self.screen.blit(self.surface, (0, 0))