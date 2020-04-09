from abc import ABC, abstractmethod


class PlayerInterface(ABC):
    @abstractmethod
    def is_white(self):
        pass
