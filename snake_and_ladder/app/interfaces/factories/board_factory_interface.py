from abc import abstractmethod, ABC

from app.interfaces.board_interface import BoardInterface


class BoardFactoryInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_board(size: int) -> BoardInterface: pass
