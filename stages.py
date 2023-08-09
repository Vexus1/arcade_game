from abc import ABC, abstractmethod

class Stage(ABC):
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
    
    def next_stage(self, next_scene):
        return next_scene
    
    def _reference_to_stage_menager(self, stage_mgr):
        self.stage_mgr = stage_mgr
