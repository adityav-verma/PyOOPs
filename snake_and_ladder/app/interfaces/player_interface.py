from abc import ABC, abstractmethod

from app.interfaces.box_interface import BoxInterface


class PlayerInterface(ABC):
    @property
    @abstractmethod
    def current_box(self) -> BoxInterface: pass

    @property
    @abstractmethod
    def name(self): pass