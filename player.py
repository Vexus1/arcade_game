import pygame
import pygwidgets
from constants import *

class Player(pygame.sprite.Sprite):

    SPEED = 3

    def __init__(self, window):
        super().__init__(self.containers)
        self.window = window
        self.image = pygwidgets.Image(window, (100, 100), 'images/player.png')
        self.rect = self.image.getRect()
        self.max_x = WINDOW_WIDTH - self.rect.width
        self.max_y = WINDOW_HEIGHT - self.rect.height

    def update(self, x, y):
        '''Method that handle players moves (WASD) limits area (window size) to move for player sprite'''
        if x < 0 or x > self.max_x:
            x = 0
        if y < 0 or y > self.max_y:
            y = 0
        
        self.image.moveXY((x, y))
        return self.image.getRect()
    
    
    def draw(self):
        self.image.draw()
