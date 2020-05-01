from abc import ABC, abstractmethod

from app.interfaces.models.board_list_inteface import BoardListInterface
from app.trello import User


class CardInterface(ABC):

    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def name(self) -> str: pass

    @property
    @abstractmethod
    def description(self) -> str: pass

    @property
    @abstractmethod
    def parent_list(self) -> BoardListInterface: pass

    @abstractmethod
    def assign_user(self, user: User) -> None: pass

    @abstractmethod
    def un_assign_user(self, user: User) -> None: pass

