from typing import List

from app.interfaces.app_interface import AppInterface
from app.interfaces.board_factory_interface import BoardFactoryInterface
from app.interfaces.board_interface import BoardInterface
from app.interfaces.board_list_factory_interface import BoardListFactoryInterface
from app.interfaces.card_factory_interface import CardFactoryInterface


class App(AppInterface):
    def __init__(
            self, board_factory: BoardFactoryInterface, list_factory: BoardListFactoryInterface,
            card_factory: CardFactoryInterface):
        self.board_factory = board_factory
        self.board_list_factory = list_factory
        self.card_factory = card_factory
        self.boards: List[BoardInterface] = []

    def _get_board_with_id(self, id):
        for board in self.boards:
            if board.id == id:
                return board

    def _get_list_with_id(self, id):
        for board in self.boards:
            for board_list in board.lists:
                if board_list.id == id:
                    return board_list

    def create_board(self, name: str, privacy: str) -> str:
        # TODO: add privacy
        board = self.board_factory.create_board(name)
        self.boards.append(board)
        return board.id

    def create_list(self, name: str, board_id: str) -> str:
        board = self._get_board_with_id(board_id)
        board_list = self.board_list_factory.create_board_list(name)
        board.add_list(board_list)
        return board_list.id

    def create_card(self, name: str, description: str, list_id: str) -> str:
        board_list = self._get_list_with_id(list_id)
        card = self.card_factory.create_card(name, description)
        board_list.add_card(card)
        return card.id

    def create_user(self, name: str, email: str) -> str:
        pass

    def add_user_to_board(self, board_id: str, user_id: str):
        pass

    def add_user_to_card(self, card_id: str, user_id: str):
        pass

    def show_board(self, board_id: str):
        pass

    def show_list(self, list_id: str):
        pass

    def show_card(self, card_id: str):
        pass