import pygame
import pygwidgets
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.image = pygwidgets.Image(window, (100, 100), 'images/player.png')
        player_rect = self.image.getRect()
        self.max_x = WINDOW_WIDTH - player_rect.width
        self.max_y = WINDOW_HEIGHT - player_rect.height

    def update(self, x, y):
        '''Method that limits area (window size) to move for player sprite'''
        if x < 0:
            x = 0
        elif x > self.max_x:
            x = self.max_x
        if y < 0:
            y = 0
        elif y > self.max_y:
            y = self.max_y
        
        self.image.setLoc((x, y))
        return self.image.getRect()
    
    def draw(self):
        self.image.draw()
