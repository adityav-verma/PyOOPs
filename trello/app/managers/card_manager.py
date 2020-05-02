from typing import Dict

from app.interfaces.managers.board_list_manager_interface import BoardListManagerInterface
from app.interfaces.managers.card_manager_interface import CardManagerInterface
from app.interfaces.managers.printer_interface import PrinterInterface
from app.interfaces.models.card_interface import CardInterface
from app.models.card import Card
from app.models.user import User


class CardManager(CardManagerInterface):
    _cards: Dict[str, CardInterface] = {}

    def __init__(self, list_manager: BoardListManagerInterface, printer: PrinterInterface):
        self._list_manager = list_manager
        self._printer = printer

    def create_card(self, name: str, description: str, list_id: str) -> str:
        board_list = self._list_manager.get_board_list(list_id)
        card = Card(name, description, board_list)

        board_list.add_child_component(card)

        self._cards[card.id] = card
        return card.id

    def assign_user_to_card(self, id: str, user: User) -> str:
        card = self._cards[id]
        card.user = user
        return card.id

    def un_assign_user_from_card(self, id: str, user: User) -> None:
        card = self._cards[id]
        card.user = None

    def show_card(self, id: str) -> dict:
        if id not in self._cards:
            return {}
        card = self._cards[id]
        return self._printer.print_board_card(card)

    def delete_card(self, id: str) -> None:
        self._cards.pop(id)

    def get_card(self, id) -> CardInterface:
        return self._cards[id]
