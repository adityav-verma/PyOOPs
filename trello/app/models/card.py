from __future__ import annotations
import uuid
from typing import TYPE_CHECKING

from app.interfaces.models.board_list_inteface import BoardListInterface
from app.interfaces.models.card_interface import CardInterface

if TYPE_CHECKING:
    from app.trello import User


class Card(CardInterface):

    def __init__(self, name: str, description: str, parent_list: BoardListInterface):
        self._user: (User, None) = None
        self._id = str(uuid.uuid4())
        self._name = name
        self._description = description

        self._parent_list = parent_list

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def parent_list(self) -> BoardListInterface:
        return self._parent_list

    @property
    def user(self) -> None:
        return self._user

    @user.setter
    def user(self, user: User) -> None:
        self._user = user
