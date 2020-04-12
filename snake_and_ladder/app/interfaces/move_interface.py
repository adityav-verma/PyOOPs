from abc import ABC, abstractmethod


class MoveInterface(ABC):
    @abstractmethod
    def invoke(self): pass

    @abstractmethod
    def undo(self): pass
