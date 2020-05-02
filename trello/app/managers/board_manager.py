from typing import Dict

from app.constants import BoardPrivacy
from app.interfaces.factories.component_factory import ComponentFactory
from app.interfaces.managers.board_manager_interface import BoardManagerInterface
from app.interfaces.managers.printer_interface import PrinterInterface
from app.interfaces.models.board_interface import BoardInterface
from app.models.user import User


class BoardManager(BoardManagerInterface):
    _boards: Dict[str, BoardInterface] = {}

    # Might want to pull this from a factory
    def __init__(self, component_factory: ComponentFactory, printer: PrinterInterface):
        self._component_factory = component_factory
        self._printer = printer

    def create_board(self, name: str, privacy: BoardPrivacy) -> str:
        # Might want to use a builder/factory pattern, since we don't know the kwargs of init
        # TODO: Move to factory
        board = self._component_factory.create_board(name, privacy)
        self._boards[board.id] = board
        return board.id

    def update_board(self, id: str, name: str, privacy: BoardPrivacy) -> str:
        board = self._boards[id]
        board.name = name
        board.privacy = privacy
        return id

    def show_board(self, id: str) -> dict:
        # Can be a different strategy implementation, but using this manager for now
        if id not in self._boards:
            return {}
        board = self._boards[id]
        return self._printer.print_board(board)

    def delete_board(self, id: str) -> None:
        # TODO: Delete lists
        self._boards.pop(id, None)

    def add_members_to_board(self, id: str, user: User) -> str:
        board: BoardInterface = self._boards[id]
        board.add_member(user)
        return board.id

    def remove_members_from_board(self, id: str, user: User) -> None:
        board: BoardInterface = self._boards[id]
        board.remove_member(user)

    def get_board(self, id: str) -> BoardInterface:
        return self._boards[id]

