from abc import abstractmethod, ABC

from app.interfaces.board_interface import BoardInterface


class GameInterface(ABC):
    @property
    @abstractmethod
    def board(self) -> BoardInterface: pass

    @abstractmethod
    def add_player(self, name) -> None: pass

    @abstractmethod
    def add_snake(self, start, end) -> None: pass

    @abstractmethod
    def add_ladder(self, start, end) -> None: pass

    @abstractmethod
    def start_game(self) -> None: pass
