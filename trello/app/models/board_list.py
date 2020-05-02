import uuid
from typing import List, Union

from app.interfaces.models.board_interface import BoardInterface
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.interfaces.models.card_interface import CardInterface
from app.interfaces.models.component_interface import Component


class BoardList(BoardListInterface):

    def __init__(self, name, parent_board: BoardInterface):
        self._parent_board = parent_board
        self._name = name
        self._id = str(uuid.uuid4())

        self._cards: List[Component] = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def parent(self) -> Union[Component, None]:
        return self._parent_board

    @parent.setter
    def parent(self, value: Component) -> None:
        self._parent_board= value

    @property
    def children(self) -> List[Component]:
        return self._cards

    def add_child_component(self, child: Component) -> None:
        self._cards.append(child)

    def remove_child_component(self, child: Component) -> None:
        self._cards.remove(child)
