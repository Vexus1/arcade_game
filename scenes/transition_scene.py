import pygame
from constants import *
from scenes.scene import Scene

class Fader(Scene): 
    def __init__(self, manager, screen, scenes: list):
        super().__init__(manager)
        self.screen = screen
        self.scenes = scenes
        self.scene = self.scenes[0]
        self.scene_delay = SCENE_DELAY # 1000ms
        self.fading = 'OUT'
        self.alpha_dt = 0
        self.alpha = 0
        self.alpha_max = 255
        self.first_scene()
        self.veil = pygame.Surface(self.screen.get_size())
        self.veil.fill((0, 0, 0))

    def first_scene(self):
        if len(self.scenes) == 1: 
            self.alpha = 255
            self.alpha_dt = 255
            self.fading = 'IN'
            self.scene_delay = SCENE_DELAY*2
    
    def handle_inputs(self, events, keys_pressed):
        self.scene.handle_inputs(events, keys_pressed)
    
    def update(self, dt):
        self.scene.update(dt)
        if self.fading == 'OUT':
            self.alpha_dt += dt/(self.scene_delay/2000)*self.alpha_max 
            self.alpha = self.alpha_dt
            if self.alpha >= 255 and len(self.scenes) > 1:
                self.fading = 'IN'
                self.scene = self.scenes[1]
        elif self.fading == 'IN':
            self.alpha_dt -= dt/(self.scene_delay/2000)*self.alpha_max
            self.alpha = self.alpha_dt
            if self.alpha <= 0:
                self.fading = None
                self.manager.during_change = False

    def draw(self):
        self.scene.draw()
        if self.fading:
            self.veil.set_alpha(self.alpha)
            self.screen.blit(self.veil, (0, 0))
