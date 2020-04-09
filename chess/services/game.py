from ..models.interfaces.player_interface import  PlayerInterface
from ..constants.game_status import GameStatus

from ..models.board import Board

class Game:
    def __init__(self, player_1: PlayerInterface, player_2: PlayerInterface):
        self._player_1 = player_1
        self._player_2 = player_2
        self._moves_list = []
        self._current_turn = None
        self._game_status = GameStatus.ACTIVE
        self._board = Board()

        self._init_game()

    @property
    def board(self):
        return self._board

    @property
    def current_turn(self):
        return self._current_turn

    @property
    def player_1(self):
        return self._player_1

    @player_1.setter
    def player_1(self, value):
        self._player_1 = value

    @property
    def player_2(self):
        return self._player_2

    @player_2.setter
    def player_2(self, value):
        self._player_2 = value

    @property
    def move_list(self):
        return self._moves_list

    @property
    def game_status(self):
        return self._game_status

    def _init_game(self):
        if self.player_1.is_white():
            self.current_turn = self.player_1
        else:
            self.current_turn = self.player_2
