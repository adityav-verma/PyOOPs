from abc import ABC, abstractmethod


class PlayerInterface(ABC):
    @abstractmethod
    def is_white(self):
        """Return whether the player is white or not""""
        pass
