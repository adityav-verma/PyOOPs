from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

from app.constants import BoardPrivacy
from app.interfaces.models.board_list_inteface import BoardListInterface

if TYPE_CHECKING:
    from app.trello import User


class BoardInterface(ABC):

    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def name(self) -> str: pass

    @name.setter
    @abstractmethod
    def name(self, value: str) -> None: pass

    @property
    @abstractmethod
    def privacy(self) -> BoardPrivacy: pass

    @privacy.setter
    @abstractmethod
    def privacy(self, value: BoardPrivacy) -> None: pass

    @property
    @abstractmethod
    def url(self) -> str: pass

    @property
    @abstractmethod
    def members(self) -> List[User]: pass

    @property
    @abstractmethod
    def board_lists(self) -> List[BoardListInterface]: pass

    @abstractmethod
    def add_member(self, user: User) -> None: pass

    @abstractmethod
    def add_board_list(self, board_list: BoardListInterface) -> None: pass

    @abstractmethod
    def remove_member(self, user: User) -> None: pass

    @abstractmethod
    def remove_board_list(self, board_list: BoardListInterface) -> None: pass