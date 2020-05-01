from abc import ABC, abstractmethod
from typing import List

from app.interfaces.models.board_interface import BoardInterface
from app.interfaces.models.card_interface import CardInterface


class BoardListInterface(ABC):
    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def name(self) -> str: pass

    @property
    @abstractmethod
    def cards(self) -> List[CardInterface]: pass

    @property
    @abstractmethod
    def parent_board(self) -> BoardInterface: pass

    @abstractmethod
    def add_card(self, card: CardInterface) -> None: pass

    @abstractmethod
    def remove_card(self, card: CardInterface) -> None: pass
