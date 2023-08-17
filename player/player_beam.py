import pygame
from constants import *
import time

SPEED = 10
class PlayerBeam(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.surf = pygame.Surface((4,20))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(topleft=set_position)

    def travel(self):
        self.rect.y -= 5
        if self.rect.top <= 0:
            self.kill()
