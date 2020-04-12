"""TODO: Do we really need to store self position in the box?"""
from app.interfaces.box_interface import BoxInterface


class Box(BoxInterface):
    def __init__(self, position):
        self._position = position

    def __str__(self):
        return f'Box: {self.position}, next -> {self.next_position()}'

    @property
    def position(self):
        return self._position

    def next_position(self):
        return self.position


class Snake(Box):
    def __init__(self, position, next):
        super(Snake, self).__init__(position)
        self.next = next

    def next_position(self):
        return self.next

    def __str__(self):
        return f'Snake: {self.position}, next -> {self.next_position()}'


class Ladder(Box):
    def __init__(self, position, next=0):
        super(Ladder, self).__init__(position)
        self.next = next

    def next_position(self):
        return self.next

    def __str__(self):
        return f'Ladder: {self.position}, next -> {self.next_position()}'
