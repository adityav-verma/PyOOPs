from typing import Dict

from app.interfaces.managers.board_list_manager_interface import BoardListManagerInterface
from app.interfaces.managers.board_manager_interface import BoardManagerInterface
from app.interfaces.managers.printer_interface import PrinterInterface
from app.interfaces.models.board_list_inteface import BoardListInterface
from app.models.board_list import BoardList


class BoardListManager(BoardListManagerInterface):

    _lists: Dict[str, BoardListInterface] = {}

    def __init__(self, board_manager: BoardManagerInterface, printer: PrinterInterface):
        self._board_manager = board_manager
        self._printer = printer

    def create_list(self, name: str, board_id: str) -> str:
        # TODO: Add a factory
        board = self._board_manager.get_board(board_id)
        board_list = BoardList(name, board)

        board.add_board_list(board_list)

        self._lists[board_list.id] = board_list
        return board_list.id

    def show_list(self, id: str) -> dict:
        if id not in self._lists:
            return {}

        board_list = self._lists[id]
        return self._printer.print_board_list(board_list)

    def delete_list(self, id: str) -> None:
        # TODO: delete cards
        self._lists.pop(id)

    def get_board_list(self, id: str) -> BoardListInterface:
        return self._lists[id]
