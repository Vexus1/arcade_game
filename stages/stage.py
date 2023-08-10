from abc import ABC, abstractmethod

class Stage(ABC):
    @abstractmethod
    def __init__(self, manager):
        self.manager = manager

    @abstractmethod
    def handle_inputs(self, events, keys_pressed):
        raise NotImplementedError
    
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_stage(self):
        raise NotImplementedError
    