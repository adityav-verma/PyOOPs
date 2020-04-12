from app.interfaces.box_interface import BoxInterface
from app.interfaces.player_interface import PlayerInterface


class Player(PlayerInterface):
    def __init__(self, name: str):
        self._name: str = name
        self._box: BoxInterface = None

    def __str__(self):
        return f'Player: {self.name} is on box: {self.current_box}'

    @property
    def name(self):
        return self._name

    @property
    def current_box(self) -> BoxInterface:
        return self._box

    @current_box.setter
    def current_box(self, box: BoxInterface):
        self._box = box

