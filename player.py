import pygame
from constants import *
from beam import *

SPEED = 10
class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.surf = pygame.image.load('images/player.png').convert_alpha()
        self.start_position()
        self.max_x = self.screen.get_width() - self.rect.width
        self.max_y = self.screen.get_height() - self.rect.height

    def move(self, x, y):
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

    def shoot(self):
        beam_position = (self.rect.x, self.rect.y)
        beam = Beam(self.screen, beam_position)
        return beam

    def start_position(self):
        self.rect = self.surf.get_rect()
        self.rect.x = self.screen.get_width()//2 - self.rect.width//2
        self.rect.y = self.screen.get_height() - self.rect.height
