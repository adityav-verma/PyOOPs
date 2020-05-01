from app.constants import BoardPrivacy
from app.managers.board_list_manager import BoardListManager
from app.managers.board_manager import BoardManager
from app.managers.card_manager import CardManager
from app.managers.dict_printer import DictPrinter
from app.models.user import User


class Trello:
    def __init__(self):
        # TODO: Use dependency injection here
        self._board_manager = BoardManager(printer=DictPrinter())
        self._list_manager = BoardListManager(self._board_manager, printer=DictPrinter())
        self._card_manager = CardManager(self._list_manager, printer=DictPrinter())

    def create_board(self, name: str, privacy: BoardPrivacy) -> str:
        return self._board_manager.create_board(name, privacy)

    def update_board(self, id: str, name: str, privacy: BoardPrivacy) -> str:
        return self._board_manager.update_board(id, name, privacy)

    def show_board(self, id: str) -> dict:
        return self._board_manager.show_board(id)

    def add_members_to_board(self, id: str, user: User) -> str:
        return self._board_manager.add_members_to_board(id, user)

    def create_list(self, name: str, board_id: str) -> str:
        return self._list_manager.create_list(name, board_id)

    def show_list(self, id: str) -> dict:
        return self._list_manager.show_list(id)

    def create_card(self, name: str, description: str, list_id: str) -> str:
        return self._card_manager.create_card(name, description, list_id)

    def assign_user_to_card(self, id: str, user: User) -> str:
        self._card_manager.assign_user_to_card(id, user)

    def show_card(self, id: str) -> dict:
        return self._card_manager.show_card(id)

    def delete_board(self, id: str) -> None:
        return self._board_manager.delete_board(id)

    def delete_list(self, id: str) -> None:
        return self._list_manager.delete_list(id)

    def delete_card(self, id: str) -> None:
        self._card_manager.delete_card(id)

    def remove_members_from_board(self, id: str, user: User) -> None:
        self._board_manager.remove_members_from_board(id, user)

    def un_assign_user_from_card(self, id: str, user: User) -> None:
        self._card_manager.un_assign_user_from_card(id, user)

