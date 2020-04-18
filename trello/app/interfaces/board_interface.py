from abc import ABC, abstractmethod
from typing import List

from app.interfaces.board_list_interface import BoardListInterface


class BoardInterface(ABC):
    @property
    @abstractmethod
    def id(self) -> str: pass

    @property
    @abstractmethod
    def lists(self) -> List[BoardListInterface]:
        pass

    @abstractmethod
    def add_list(self, board_list: BoardListInterface):
        pass
