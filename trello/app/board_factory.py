from app.board import Board
from app.interfaces.board_factory_interface import BoardFactoryInterface
from app.interfaces.board_interface import BoardInterface


class BoardFactory(BoardFactoryInterface):
    def create_board(self, name: str) -> BoardInterface:
        return Board(name)

    def get_with_id(self, id: str) -> BoardInterface:
        pass