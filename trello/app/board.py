from typing import List
import uuid

from app.interfaces.board_interface import BoardInterface
from app.interfaces.board_list_interface import BoardListInterface


class Board(BoardInterface):
    def __init__(self, name):
        self._name = name
        self._id = str(uuid.uuid4())
        self._lists: List[BoardListInterface] = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def lists(self) -> List[BoardListInterface]:
        return self._lists

    def add_list(self, board_list: BoardListInterface):
        self._lists.append(board_list)

