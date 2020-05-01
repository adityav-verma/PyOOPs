from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

from app.interfaces.models.card_interface import CardInterface
if TYPE_CHECKING:
    from app.interfaces.models.board_interface import BoardInterface


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
