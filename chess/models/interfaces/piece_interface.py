from abc import ABC, abstractmethod


class PieceInterface(ABC):
    @abstractmethod
    def is_white(self):
        pass

    @abstractmethod
    def is_active(self):
        pass

    @abstractmethod
    def can_move(self):
        pass
