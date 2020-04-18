from abc import ABC, abstractmethod
from typing import List

from app.interfaces.card_interface import CardInterface


class BoardListInterface(ABC):
    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def cards(self) -> List[CardInterface]:
        pass

    @abstractmethod
    def add_card(self, card: CardInterface):
        pass