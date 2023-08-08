import pygame
import pygwidgets
from constants import *

class Player(pygame.sprite.Sprite):

    SPEED = 4

    def __init__(self, window):
        # super().__init__()
        self.window = window
        self.image = pygwidgets.Image(window, (100, 100), 'images/player.png')
        self.rect = self.image.getRect()
        self.max_x = WINDOW_WIDTH - self.rect.width
        self.max_y = WINDOW_HEIGHT - self.rect.height

    def update(self, x, y):
        '''Method that handle players moves (WASD) limits area (window size) to move for player sprite'''
        # rect_loc = self.image.getRect()
     
        print(self.image.getX())

        self.image.moveXY(x*self.SPEED, y*self.SPEED)
        if self.image.getX() <= 0:
            self.image.setLoc((0, self.rect[1]))

        # print(self.rect.left)
        # if self.rect.height < 0 or self.rect.height > self.max_y:
        #     y = 0
        
 
        # return self.rect
    
    
    def draw(self):
        self.image.draw()
