"""TODO: Should Board hold information about players?"""

from abc import ABC, abstractmethod

from app.interfaces.box_interface import BoxInterface


class BoardInterface(ABC):
    @abstractmethod
    def add_snake(self, start: int, end: int): pass

    @abstractmethod
    def add_ladder(self, start: int, end: int): pass

    @abstractmethod
    def reset(self): pass

    @abstractmethod
    def get_box(self, index) -> BoxInterface : pass
