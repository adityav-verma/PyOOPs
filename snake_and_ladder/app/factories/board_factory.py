from app.board import Board
from app.factories.box_factory import BoxFactory
from app.interfaces.board_interface import BoardInterface
from app.interfaces.factories.board_factory_interface import BoardFactoryInterface


class BoardFactory(BoardFactoryInterface):
    @staticmethod
    def create_board(size: int) -> BoardInterface:
        return Board(size, BoxFactory)