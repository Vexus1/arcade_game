from constants import * 
import pygame

class TextButton():
    def __init__(self, screen, text, loc: tuple, font=None, size=20, color=BLACK):
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

    def draw(self):
        self.screen.blit(self.text_surface, self.loc)

