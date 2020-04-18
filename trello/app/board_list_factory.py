from app.board_list import BoardList
from app.interfaces.board_interface import BoardInterface
from app.interfaces.board_list_factory_interface import BoardListFactoryInterface
from app.interfaces.board_list_interface import BoardListInterface


class BoardListFactory(BoardListFactoryInterface):
    def get_with_id(self, id: str) -> BoardListInterface:
        pass

    def create_board_list(self, name) -> BoardListInterface:
        return BoardList(name)