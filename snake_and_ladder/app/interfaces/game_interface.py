from abc import abstractmethod, ABC
from typing import List

from app.interfaces.board_interface import BoardInterface
from app.interfaces.move_interface import MoveInterface


class GameInterface(ABC):
    @property
    @abstractmethod
    def board(self) -> BoardInterface: pass

    @property
    @abstractmethod
    def moves(self) -> List[MoveInterface]: pass

    @abstractmethod
    def add_player(self, name) -> None: pass

    @abstractmethod
    def add_snake(self, start, end) -> None: pass

    @abstractmethod
    def add_ladder(self, start, end) -> None: pass

    @abstractmethod
    def start_game(self) -> None: pass

    @abstractmethod
    def reset(self) -> None: pass
