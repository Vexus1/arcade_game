import pygame

from abc import ABC, abstractmethod
from constants import DELAY_TIME
from scenes.scene_delay import Delay

class Scene(ABC):
    @abstractmethod
    def __init__(self, manager):
        self.manager = manager
        self.scene_delay = pygame.time.get_ticks() + DELAY_TIME # ms

    @abstractmethod
    def handle_inputs(self, events, key_pressed_list):
        raise NotImplementedError
    
    def update(self, dt):
        pass
    
    @abstractmethod
    def draw(self):
        raise NotImplementedError
    