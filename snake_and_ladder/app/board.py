from typing import List

from app.box import Box, Snake, Ladder
from app.exceptions.exceptions import InvalidPosition
from app.interfaces.board_interface import BoardInterface
from app.interfaces.box_interface import BoxInterface


class Board(BoardInterface):
    def __init__(self, size: int):
        self.boxes: List[BoxInterface or None] = [None for _ in range(size + 1)]
        self.reset()

    def _validate_index(self, index):
        if index < 0 or index >= len(self.boxes):
            raise InvalidPosition('Invalid index for box')

    def add_snake(self, start: int, end: int):
        self._validate_index(start)
        self._validate_index(end)
        self.boxes[start] = Snake(position=start, next=end)

    def add_ladder(self, start: int, end: int):
        self._validate_index(start)
        self._validate_index(end)
        self.boxes[start] = Ladder(position=start, next=end)

    def get_box(self, index):
        self._validate_index(index)
        return self.boxes[index]

    def reset(self):
        for index in range(len(self.boxes)):
            self.boxes[index] = Box(position=index)