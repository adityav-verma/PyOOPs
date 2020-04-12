from abc import ABC, abstractmethod


class BoxInterface(ABC):
    @property
    @abstractmethod
    def position(self): pass

    @abstractmethod
    def next_position(self): pass
