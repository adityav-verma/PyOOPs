import uuid
from typing import List

from app.constants import BoardPrivacy
from app.interfaces.models.board_interface import BoardInterface
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.trello import User


class Board(BoardInterface):
    def __init__(self, name: str, privacy: BoardPrivacy):
        self._id = str(uuid.uuid4())
        self._name = name
        self._privacy = privacy
        self._members: List[User] = []
        self._board_lists: List[BoardListInterface] = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def privacy(self) -> BoardPrivacy:
        return self._privacy

    @property
    def url(self) -> str:
        return f'/board/{self.id}/'

    @property
    def members(self) -> List[User]:
        return self._members

    @property
    def board_lists(self) -> List[BoardListInterface]:
        return self._board_lists

    def add_member(self, user: User) -> None:
        self._members.append(user)

    def add_board_list(self, board_list: BoardListInterface) -> None:
        self._board_lists.append(board_list)

    def remove_member(self, user: User) -> None:
        self._members.remove(user)

    def remove_board_list(self, board_list: BoardListInterface) -> None:
        self._board_lists.remove(board_list)
