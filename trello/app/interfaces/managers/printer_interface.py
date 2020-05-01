from abc import ABC, abstractmethod

from app.interfaces.models.board_interface import BoardInterface
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.interfaces.models.card_interface import CardInterface


class PrinterInterface(ABC):
    @abstractmethod
    def print_board(self, board: BoardInterface) -> dict: pass

    @abstractmethod
    def print_board_list(self, board_list: BoardListInterface) -> dict: pass

    @abstractmethod
    def print_board_card(self, card: CardInterface) -> dict: pass
