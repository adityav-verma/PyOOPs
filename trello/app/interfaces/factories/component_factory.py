from abc import abstractmethod, ABC

from app.constants import BoardPrivacy
from app.interfaces.models.board_interface import BoardInterface
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.interfaces.models.card_interface import CardInterface


class ComponentFactory(ABC):
    @abstractmethod
    def create_board(self, name: str, privacy: BoardPrivacy) -> BoardInterface: pass

    @abstractmethod
    def create_board_list(self, name: str, board: BoardInterface) -> BoardListInterface: pass

    @abstractmethod
    def create_card(self, name: str, description: str, board_list: BoardListInterface) -> CardInterface: pass
