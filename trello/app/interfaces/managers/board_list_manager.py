from abc import ABC, abstractmethod

from app.interfaces.models.board_list_inteface import BoardListInterface


class BoardListManager(ABC):

    @abstractmethod
    def create_list(self, name: str, board_id: str) -> str: pass

    @abstractmethod
    def show_list(self, id: str) -> dict: pass

    @abstractmethod
    def delete_list(self, id: str) -> None: pass

    @abstractmethod
    def get_board_list(self, id: str) -> BoardListInterface: pass
