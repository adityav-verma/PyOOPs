import uuid
from typing import List, Union

from app.constants import BoardPrivacy
from app.interfaces.models.board_interface import BoardInterface
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.interfaces.models.component_interface import Component
from app.models.user import User


class Board(BoardInterface):
    def __init__(self, name: str, privacy: BoardPrivacy):
        self._id = str(uuid.uuid4())
        self._name = name
        self._privacy = privacy
        self._members: List[User] = []
        self._board_lists: List[Component] = []

    @property
    def parent(self) -> Union[Component, None]:
        return None

    @property
    def children(self) -> List[Component]:
        return self._board_lists

    def add_child_component(self, child: Component) -> None:
        self._board_lists.append(child)

    def remove_child_component(self, child: Component) -> None:
        self._board_lists.remove(child)

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def privacy(self) -> BoardPrivacy:
        return self._privacy

    @privacy.setter
    def privacy(self, value: BoardPrivacy) -> None:
        self._privacy = value

    @property
    def url(self) -> str:
        return f'/board/{self.id}/'

    @property
    def members(self) -> List[User]:
        return self._members

    def add_member(self, user: User) -> None:
        self._members.append(user)

    def remove_member(self, user: User) -> None:
        self._members.remove(user)