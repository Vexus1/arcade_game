import pygame
from constants import *
from player.player_beam import *
import time

SPEED = 10
FIRERATE = 5 # shoots per seocnd
class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.surf = pygame.image.load('images/player.png').convert_alpha()
        self.rect = self.surf.get_rect()
        self.starting_position()
        self.max_x = self.screen.get_width() - self.rect.width
        self.max_y = self.screen.get_height() - self.rect.height
        self.time = 0
        self.fire_delay = 0 # in milliseconds
    
    def starting_position(self):
        self.rect.centerx = self.screen.get_width()//2
        self.rect.y = self.screen.get_height() - self.rect.height

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

    def fire_rate(self):
        if self.time + self.fire_delay <= pygame.time.get_ticks():
            self.fire_delay = 1000/FIRERATE
            self.time = pygame.time.get_ticks()
            return True

    def shoot(self):
        if self.fire_rate():
            beam_position = (self.rect.centerx, self.rect.y)
            beam = PlayerBeam(self.screen, beam_position)
            return beam
