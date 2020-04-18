from abc import abstractmethod, ABC

from app.interfaces.board_list_interface import BoardListInterface
from app.interfaces.card_interface import CardInterface


class CardFactoryInterface(ABC):
    @abstractmethod
    def create_card(self, name: str, description: str) -> CardInterface:
        pass

    @abstractmethod
    def get_with_id(self, id: str) -> BoardListInterface: pass
