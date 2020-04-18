import uuid
from typing import List

from app.interfaces.board_list_interface import BoardListInterface
from app.interfaces.card_interface import CardInterface


class BoardList(BoardListInterface):
    def __init__(self, name):
        self._name = name
        self._id = str(uuid.uuid4())
        self._cards: List[CardInterface] = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def cards(self) -> List[CardInterface]:
        return self._cards

    def add_card(self, card: CardInterface):
        self._cards.append(card)

