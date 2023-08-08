from abc import ABC, abstractmethod

class scene(ABC):
    @abstractmethod
    def handle_inputs(self, events, keys_pressed):
        """This method is called in every frame of the scene to handle events and key presses

        Your code MUST override this method.

        Parameters:
            |    events - a list of events your method should handle.
            |    keys_pressed - a list of keys that are pressed (a Boolean for each key).

        """
        raise NotImplementedError
    
    def update(self):
        """This method is called in every frame of the scene do any processing you need to do here

        Your code will typically override this method.

        """
        pass

    @abstractmethod
    def draw(self):
        """This method is called in every frame of the scene to draw anything that needs to be drawn

        Your code MUST override this method.

        """
        raise NotImplementedError
    
    @abstractmethod
    def get_scene(self):
        """This method must return the scene key for this scene

        Your code MUST override this method.

        """
        raise NotImplementedError
    
    def next_scene(self, next_scene):
        """Call this method whenever you want to go to a new scene

        Parameters:
            |    nextSceneKey - the scene key (string) of the scene to go to

        """
        return next_scene
