from constants import * 
import pygame

class TextButton():
    def __init__(self, screen, text, loc: tuple, stage=None, font='Arial', size=20, color=WHITE):
        self.screen = screen
        self.loc = loc
        self.font = pygame.font.SysFont(font, size)
        self.text = None
        self.color = color
        self.set_text(text)
        self.stage = stage

    def set_text(self, new_text):
        if self.text == new_text:
            return
        
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.screen.blit(self.text_surface, self.loc)

    def selected(self):
        self.text_surface = self.font.render(self.text, True, RED)

    def unselected(self):
        self.text_surface = self.font.render(self.text, True, WHITE)
    
    def stage_reference(self):
        return self.stage



# class Button():
#     def __init__(self, screen, )

