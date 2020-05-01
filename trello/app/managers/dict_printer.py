from app.interfaces.managers.printer_interface import PrinterInterface
from app.interfaces.models.board_interface import BoardInterface
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.interfaces.models.card_interface import CardInterface


class DictPrinter(PrinterInterface):
    def print_board(self, board: BoardInterface) -> dict:
        return {
            'id': board.id,
            'name': board.name,
            'privacy': board.privacy.value,
            'members': board.members,
            'board_lists': [
                self.print_board_list(item) for item in board.board_lists
            ]
        }

    def print_board_list(self, board_list: BoardListInterface) -> dict:
        return {
            'id': board_list.id,
            'name': board_list.name,
            'cards': [
                self.print_board_card(item) for item in board_list.cards
            ]
        }

    def print_board_card(self, card: CardInterface) -> dict:
        return {
            'id': card.id,
            'name': card.name,
            'description': card.description,
            'user': card.user
        }
