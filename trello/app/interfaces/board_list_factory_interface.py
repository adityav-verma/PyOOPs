from abc import abstractmethod, ABC

from app.interfaces.board_interface import BoardInterface
from app.interfaces.board_list_interface import BoardListInterface


class BoardListFactoryInterface(ABC):
    @abstractmethod
    def create_board_list(self, name) -> BoardListInterface:
        pass

    @abstractmethod
    def get_with_id(self, id: str) -> BoardListInterface: pass
