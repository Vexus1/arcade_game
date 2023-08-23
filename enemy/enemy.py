import pygame

from constants import *
from math import floor
from random import randint

MOVEMENT_SPEED = 1
BEAM_SPEED = 2
RANDOM_FIRERATE = (0.25, 1) # minimum and maximum shoots per second

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.set_position = set_position
        self.max_left_reached = False
        self.max_right_reached = False
        self.time = SCENE_DELAY
        self.random_fire_delay()
        self.surf = pygame.image.load('images/enemy.png').convert_alpha()
        self.rect = self.surf.get_rect()
        self.starting_position()

    def starting_position(self):
        self.rect.centerx = self.set_position[0] 
        self.rect.y = self.set_position[1]

    def route(self):
        '''Enemy route through Ox axis (10% of current window width)'''
        max_left_route = self.set_position[0] - self.screen.get_width()//20
        max_right_route = self.set_position[0] + self.screen.get_width()//20
        if self.rect.centerx >= max_left_route and self.max_left_reached is False:
            self.rect.centerx -= MOVEMENT_SPEED
            if self.rect.centerx <= max_left_route:
                self.max_left_reached, self.max_right_route = True, False
        elif self.rect.centerx <= max_right_route and self.max_right_reached is False:
            self.rect.centerx += MOVEMENT_SPEED
            if self.rect.centerx >= max_right_route:
                self.max_left_reached, self.max_right_route = False, True

    def random_fire_delay(self):
        self.delay = randint(int(1000/RANDOM_FIRERATE[1]), int(1000/RANDOM_FIRERATE[0]))
    
    def _random_shoot(self):
        if self.time + self.delay <= pygame.time.get_ticks():
            self.random_fire_delay()
            self.time = pygame.time.get_ticks()
            return True

    def shoot(self):
        if self._random_shoot():
            beam_position = (self.rect.centerx, self.rect.y)
            beam = EnemyBeam(self.screen, beam_position)
            return beam
        

class EnemyBeam(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.surf = pygame.Surface((4,20))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(topleft=set_position)

    def travel(self):
        self.rect.y += BEAM_SPEED
        if self.rect.bottom <= 0:
            self.kill()
