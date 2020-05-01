from abc import ABC, abstractmethod
from typing import List

from app.constants import BoardPrivacy
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.trello import User


class BoardInterface(ABC):

    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def name(self) -> str: pass

    @property
    @abstractmethod
    def privacy(self) -> BoardPrivacy: pass

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
