from .interfaces.board_interface import BoardInterface


class Board(BoardInterface):
    def __init__(self):
        self._board = [[]]
        self.reset_board()

    @property
    def board(self):
        return self._board

    def get_box(self, x, y):
        x, y = x - 1, y - 1
        if x > len(self.board) or y > len(self.board[0]) or x < 0 or y < 0:
            raise Exception('Invalid box in board')
        return self.board[x - 1][y - 1]

    def reset_board(self):
        self._board = [[None] for _ in range(8) for __ in range(8)]
        self._add_pawns()
        self._add_knights()
        self._add_ishops()
        self._add_rook()
        self._add_knight()
        self._add_queeen()
        self._add_king()

    def _add_pawns(self):
        pass

    def _add_knights(self):
        pass

    def _add_ishops(self):
        pass

    def _add_rook(self):
        pass

    def _add_knight(self):
        pass

    def _add_queeen(self):
        pass

    def _add_king(self):
        pass
