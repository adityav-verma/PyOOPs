from abc import ABC, abstractmethod

from app.constants import BoardPrivacy
from app.interfaces.models.board_interface import BoardInterface
from app.models.user import User


class BoardManagerInterface(ABC):

    @abstractmethod
    def create_board(self, name: str, privacy: BoardPrivacy) -> str: pass

    @abstractmethod
    def update_board(self, id: str, name: str, privacy: BoardPrivacy) -> str: pass

    @abstractmethod
    def show_board(self, id: str) -> dict: pass

    @abstractmethod
    def delete_board(self, id: str) -> None: pass

    @abstractmethod
    def add_members_to_board(self, id: str, user: User) -> str: pass

    @abstractmethod
    def remove_members_from_board(self, id: str, user: User) -> None: pass

    # Might have to figure out some other places to persist data
    @abstractmethod
    def get_board(self, id: str) -> BoardInterface: pass
