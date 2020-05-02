import uuid
from typing import List

from app.interfaces.models.board_interface import BoardInterface
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.interfaces.models.card_interface import CardInterface


class BoardList(BoardListInterface):
    def __init__(self, name, parent_board: BoardInterface):
        self._parent_board = parent_board
        self._name = name
        self._id = str(uuid.uuid4())

        self._cards: List[CardInterface] = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def cards(self) -> List[CardInterface]:
        return self._cards

    @property
    def parent_board(self) -> BoardInterface:
        return self._parent_board

    def add_card(self, card: CardInterface) -> None:
        self._cards.append(card)

    def remove_card(self, card: CardInterface) -> None:
        self._cards.remove(card)
