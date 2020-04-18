from abc import abstractmethod, ABC

from app.interfaces.board_interface import BoardInterface


class BoardFactoryInterface(ABC):
    @abstractmethod
    def create_board(self, name: str) -> BoardInterface:
        pass

    @abstractmethod
    def get_with_id(self, id: str) -> BoardInterface: pass
