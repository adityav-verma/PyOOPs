from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from app.interfaces.models.card_interface import CardInterface

if TYPE_CHECKING:
    from app.trello import User


class CardManagerInterface(ABC):

    @abstractmethod
    def create_card(self, name: str, description: str, list_id: str) -> str: pass

    @abstractmethod
    def assign_user_to_card(self, id: str, user: User) -> str: pass

    @abstractmethod
    def un_assign_user_from_card(self, id: str, user: User) -> None: pass

    @abstractmethod
    def show_card(self, id: str) -> dict: pass

    @abstractmethod
    def delete_card(self, id: str) -> None: pass

    @abstractmethod
    def get_card(self, id) -> CardInterface: pass