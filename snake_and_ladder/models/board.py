class Board:
    def __init__(self, length, width, cell_model):
        self._length = length
        self._width = width
        self._cell_model = cell_model
        self.grid = self._init_board()

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def cell_model(self):
        return self._cell_model

    @cell_model.setter
    def cell_model(self, cell_model):
        self._cell_model = cell_model

    def _init_board(self):
        return [[self.cell_model() for _ in range(self._width)] for __ in range(self.length)]
