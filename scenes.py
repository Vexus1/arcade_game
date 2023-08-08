from abc import ABC, abstractmethod

class SceneMenager()
    def __init__(self):
        pass


class Scene(ABC):
    @abstractmethod
    def handle_inputs(self, events, keys_pressed):
        raise NotImplementedError
    
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_scene(self):
        raise NotImplementedError
    
    def next_scene(self, next_scene):
        return next_scene
    
    def _reference_to_scene_mgr(self, scene_mgr):
        self.scene_mgr = scene_mgr
