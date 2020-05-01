from typing import Dict

from app.constants import BoardPrivacy
from app.interfaces.managers.board_manager_interface import BoardManagerInterface
from app.interfaces.models.board_interface import BoardInterface
from app.models.board import Board
from app.trello import User


class BoardManager(BoardManagerInterface):
    _boards: Dict[str, BoardInterface] = {}

    # Might want to pull this from a factory
    def __init__(self):
        pass

    def create_board(self, name: str, privacy: BoardPrivacy) -> str:
        # Might want to use a builder/factory pattern, since we don't know the kwargs of init
        # TODO: Move to factory
        board = Board(name, privacy)
        self._boards[board.id] = board
        return board.id

    def update_board(self, id: str, name: str, privacy: BoardPrivacy) -> str:
        board = self._boards[id]
        board.name = name
        board.privacy = privacy
        return id

    def show_board(self, id: str) -> dict:
        # Can be a different strategy implementation, but using this manager for now
        board = self._boards[id]
        # TODO: Add lists
        return {
            'id': board.id,
            'name': board.name,
            'privacy': board.privacy.value
        }

    def delete_board(self, id: str) -> None:
        self._boards.pop(id)

    def add_members_to_board(self, id: str, user: User) -> str:
        board: BoardInterface = self._boards[id]
        board.add_member(user)
        return board.id

    def remove_members_from_board(self, id: str, user: User) -> None:
        board: BoardInterface = self._boards[id]
        board.remove_member(user)

    def get_board(self, id: str) -> BoardInterface:
        return self._boards[id]

