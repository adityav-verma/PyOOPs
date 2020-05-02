from app.constants import BoardPrivacy
from app.interfaces.factories.component_factory import ComponentFactory
from app.interfaces.models.board_interface import BoardInterface
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.interfaces.models.card_interface import CardInterface
from app.models.board import Board
from app.models.board_list import BoardList
from app.models.card import Card
from app.utilities import singleton


@singleton
class SimpleComponentFactory(ComponentFactory):
    def create_board(self, name: str, privacy: BoardPrivacy) -> BoardInterface:
        return Board(name, privacy)

    def create_board_list(self, name: str, board: BoardInterface) -> BoardListInterface:
        return BoardList(name, board)

    def create_card(self, name: str, description: str, board_list: BoardListInterface) -> CardInterface:
        return Card(name, description, board_list)
