from ..models.board import Board


class BoardService:
    def __init__(self):
        self._board_model = Board

    def create_board(self, length, width):
        return self._board_model(length, width)

    def add_snake(self, board, start, delta):
        board.ladder()

    def add_ladder(self, start, delta):
        pass
