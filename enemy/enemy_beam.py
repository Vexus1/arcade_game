import pygame
from constants import *

SPEED = 5
class EnemyBeam(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.surf = pygame.Surface((4,20))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(topleft=set_position)

    def travel(self):
        self.rect.y -= SPEED
        if self.rect.top <= 0:
            self.kill()
