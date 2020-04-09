from .interfaces.piece_interface import PieceInterface


class Piece(PieceInterface):
    def __init__(self, is_white, is_active=True):
        self._is_white = is_white
        self._is_active = is_active

    @property
    def is_white(self):
        return self._is_white

    @is_white.setter
    def is_white(self, is_white):
        self._is_white = is_white

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        self._is_active = is_active



# TODO: Add implementation for these
class Pawn(Piece):
    pass


class Bishop(Piece):
    pass


class Rook(Piece):
    pass


class Knight(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass
