from .cell import Cell


class Snake(Cell):
    def __init__(self, delta_x, delta_y):
        """A snake can alter the current position by delta in both the axis"""
        self._delta_x = delta_x
        self._delta_y = delta_y

    @property
    def delta_x(self):
        return self._delta_x

    @delta_x.setter
    def delta_x(self, delta_x):
        self._delta_x = delta_x

    @property
    def delta_y(self):
        return self._delta_y

    @delta_y.setter
    def delta_y(self, delta_y):
        self._delta_y = delta_y
