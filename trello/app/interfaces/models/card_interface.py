from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from app.interfaces.models.component_interface import Component
from app.models.user import User

if TYPE_CHECKING:
    from app.interfaces.models.board_list_inteface import BoardListInterface


class CardInterface(Component, ABC):

    @property
    @abstractmethod
    def description(self) -> str: pass

    @property
    @abstractmethod
    def user(self) -> None: pass

    @user.setter
    @abstractmethod
    def user(self, user: User) -> None: pass
