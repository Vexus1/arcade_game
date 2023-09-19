from constants import * 
import pygame

# Need rework!!
class Text():
    def __init__(self, screen, text, loc: tuple, font='Arial', size=20, color=WHITE):
        self.screen = screen
        self.loc = loc
        self.font = pygame.font.SysFont(font, size)
        self.text = None
        self.color = color
        self.set_text(text)

    def set_text(self, new_text):
        if self.text == new_text:
            return
        
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.loc)

    def draw(self):
        self.screen.blit(self.text_surface, self.text_rect)
    

class TextButton():
    def __init__(self, screen, text, loc: tuple, scene=None, font='Arial', size=20, color=WHITE):
        self.screen = screen
        self.loc = loc
        self.font = pygame.font.SysFont(font, size)
        self.text = None
        self.color = color
        self.set_text(text)
        self.scene = scene

    def set_text(self, new_text):
        if self.text == new_text:
            return
        
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.loc)

    def draw(self):
        self.screen.blit(self.text_surface, self.text_rect)

    def selected(self):
        self.text_surface = self.font.render(self.text, True, RED)

    def unselected(self):
        self.text_surface = self.font.render(self.text, True, WHITE)
    
    def scene_reference(self):
        return self.scene
    
