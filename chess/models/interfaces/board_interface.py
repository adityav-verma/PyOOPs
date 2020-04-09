from abc import ABC, abstractmethod


class BoardInterface(ABC):
    @abstractmethod
    def reset_board(self):
        pass

    @abstractmethod
    def get_box(self, x, y):
        pass
