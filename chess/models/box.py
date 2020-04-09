from .interfaces.box_interface import BoxInterface


class Box(BoxInterface):
    def __init__(self, x, y, piece=None):
        self._piece = piece
        self._x = x
        self._y = yp

    @property
    def x(self):
        return _x

    @x.getter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return _y

    @y.getter
    def y(self, y):
        self._y = y

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, piece):
        self._piece = piece
