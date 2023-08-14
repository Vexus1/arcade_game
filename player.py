import pygame
import pygwidgets
from constants import *

SPEED = 4
class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.max_x = SCREEN_WIDTH - self.rect.width
        self.max_y = SCREEN_HEIGHT - self.rect.height

    def update(self, x, y):
        '''Method that handle players moves (WASD) limits area (window size) to move for player sprite'''
        self.rect.move_ip(x*SPEED, y*SPEED)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.top > self.max_y:
            self.rect.top = self.max_y
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.left > self.max_x:
            self.rect.left = self.max_x
