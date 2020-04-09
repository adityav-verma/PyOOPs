from .interfaces.player_interface import PlayerInterface


class Player(PlayerInterface):
    def __init__(self, is_white):
        self._is_white = is_white
        self._is_checked = False

    @property
    def is_white(self):
        return self._is_white

    @is_white.setter
    def is_white(self, is_white):
        self._is_white = is_white

    @property
    def is_checked(self):
        return self._is_checked

    @is_checked.setter
    def is_checked(self, is_checked):
        self._is_checked = is_checked


class Player2:
    def __init__(self, is_white):
        self.is_white = is_white