from abc import ABC, abstractmethod

class Scene(ABC):
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
    
    def on_enter(self):
        pass

    def on_exit(self):
        pass
    