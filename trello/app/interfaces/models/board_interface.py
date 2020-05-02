from abc import ABC, abstractmethod
from typing import List

from app.constants import BoardPrivacy
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.interfaces.models.component_interface import Component
from app.models.user import User


class BoardInterface(Component, ABC):

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

    @abstractmethod
    def add_member(self, user: User) -> None: pass

    @abstractmethod
    def remove_member(self, user: User) -> None: pass

